from __future__ import annotations

import difflib
import hashlib
import re
from dataclasses import dataclass
from typing import Any

from .errors import ValidationError
from .markdown import read_document, render_document
from .proposals import CANONICAL_DIRECTORIES, ProposalResult
from .repository import Repository, now_iso, sha256_bytes, slugify


ARXIV_PATTERN = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?:v(\d+))?(?!\d)", re.I)


@dataclass(frozen=True)
class WorkIdentity:
    work_id: str
    arxiv_id: str | None
    version: str | None


class WorkService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def identify(self, sources: list[dict[str, Any]], arxiv_id: str | None = None) -> WorkIdentity:
        candidates: list[tuple[str, str | None]] = []
        if arxiv_id:
            match = ARXIV_PATTERN.fullmatch(arxiv_id.strip())
            if not match:
                raise ValidationError(f"无效 arXiv ID: {arxiv_id}")
            candidates.append((match.group(1), match.group(2)))
        for source in sources:
            text = " ".join([
                str(source.get("original_locator", "")), str(source.get("canonical_locator", "")),
                str(source.get("original_filename", "")), str(source.get("title", "")),
            ])
            match = ARXIV_PATTERN.search(text)
            if match:
                candidates.append((match.group(1), match.group(2)))
        ids = {item[0] for item in candidates}
        if len(ids) > 1:
            raise ValidationError("sources 指向不同 arXiv works")
        if ids:
            identifier = next(iter(ids))
            versions = [int(version) for item_id, version in candidates if item_id == identifier and version]
            version = f"v{max(versions)}" if versions else None
            return WorkIdentity(f"work_arxiv_{identifier.replace('.', '_')}", identifier, version)
        raise ValidationError("无法可靠识别 work；请显式提供 --arxiv-id")

    def propose(
        self, source_ids: list[str], *, arxiv_id: str | None = None,
        title: str | None = None, authors: list[str] | None = None,
    ) -> ProposalResult:
        ordered_ids = list(dict.fromkeys(source_ids))
        if not ordered_ids:
            raise ValidationError("work proposal 至少需要一个 source")
        sources: list[dict[str, Any]] = []
        for source_id in ordered_ids:
            _, source, _ = self.repository.find_document(source_id)
            if source.get("type") != "source":
                raise ValidationError(f"work 只能关联 source: {source_id}")
            sources.append(source)
        identity = self.identify(sources, arxiv_id)
        target_path = (
            self.repository.root / CANONICAL_DIRECTORIES["work"]
            / f"{identity.work_id}-{slugify(title or str(sources[0]['title']))}.md"
        )
        existing_paths = []
        for path in self.repository.canonical_documents():
            metadata, _ = read_document(path)
            if metadata.get("id") == identity.work_id:
                existing_paths.append((path, metadata))
        if existing_paths:
            target_path, target = existing_paths[0]
            action = "update"
            base_bytes = target_path.read_bytes()
            base_sha = sha256_bytes(base_bytes)
            combined_sources = list(dict.fromkeys([*target.get("source_ids", []), *ordered_ids]))
            created_at = target["created_at"]
            canonical_title = title or target.get("canonical_title") or target["title"]
            existing_authors = list(target.get("authors", []))
        else:
            target = {}
            action = "create"
            base_bytes = b""
            base_sha = None
            combined_sources = ordered_ids
            created_at = now_iso()
            canonical_title = title or str(sources[0]["title"])
            existing_authors = []
        timestamp = now_iso()
        metadata = {
            "id": identity.work_id, "type": "work", "status": "proposal",
            "title": canonical_title, "canonical_title": canonical_title,
            "created_at": created_at, "updated_at": timestamp,
            "aliases": list(dict.fromkeys([str(source["title"]) for source in sources if source.get("title") != canonical_title])),
            "tags": [], "domains": [], "confidence": "medium",
            "source_ids": combined_sources,
            "relations": [{"type": "derived_from", "target_id": source_id, "reason": "该 capture 属于此 logical work"} for source_id in combined_sources],
            "work_type": "paper", "authors": list(dict.fromkeys([*existing_authors, *(authors or [])])),
            "published_at": target.get("published_at"), "doi": target.get("doi"),
            "arxiv_id": identity.arxiv_id, "repository_url": target.get("repository_url"),
            "version": identity.version or target.get("version"), "language": target.get("language", "und"),
            "same_work_as": target.get("same_work_as", []),
            "supersedes_version": target.get("supersedes_version"),
        }
        if action == "update":
            metadata["proposed_status"] = target.get("status", "confirmed")
        body = (
            f"# {canonical_title}\n\n## Logical work identity\n\n"
            f"- arXiv：`{identity.arxiv_id}`\n- Version：`{metadata['version'] or 'unknown'}`\n"
            f"- Captures：{', '.join(f'`{item}`' for item in combined_sources)}\n\n"
            "此对象聚合现实世界作品身份，不替代任何 source capture 的 provenance。\n"
        )
        candidate_text = render_document(metadata, body)
        candidate_sha = sha256_bytes(candidate_text.encode("utf-8"))
        digest = hashlib.sha256(
            f"work\n{identity.work_id}\n{base_sha or ''}\n{candidate_sha}".encode("utf-8")
        ).hexdigest()
        proposal_id = f"proposal_{digest[:24]}"
        proposal_path = self.repository.root / "vault/proposals" / f"proposal-{proposal_id}.md"
        candidate_path = self.repository.root / "vault/proposals" / f"candidate-{proposal_id}.md"
        base_path = self.repository.root / "vault/proposals" / f"base-{proposal_id}.md"
        if proposal_path.exists():
            old, _ = read_document(proposal_path)
            return ProposalResult(proposal_id, self.repository.rel(proposal_path), old["candidate_path"], old["target_path"], old["action"])
        if action == "update":
            self.repository.immutable_write(base_path, base_bytes)
        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        diff = "".join(difflib.unified_diff(
            base_bytes.decode("utf-8").splitlines(keepends=True) if base_bytes else [],
            candidate_text.splitlines(keepends=True), fromfile="base" if base_bytes else "/dev/null",
            tofile=self.repository.rel(target_path),
        ))
        proposal_metadata = {
            "id": proposal_id, "type": "proposal", "status": "pending",
            "title": f"Work enrichment：{canonical_title}", "created_at": timestamp,
            "updated_at": timestamp, "aliases": [], "tags": [], "domains": [],
            "confidence": "medium", "source_ids": combined_sources, "relations": [],
            "proposal_kind": "work_enrichment", "processor": "deterministic-work-identity-v1",
            "action": action, "target_id": identity.work_id,
            "target_path": self.repository.rel(target_path),
            "base_path": self.repository.rel(base_path) if action == "update" else None,
            "base_sha256": base_sha, "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_sha, "change_reason": "显式 work identity enrichment",
            "reviewed_at": None, "review_reason": None,
        }
        proposal_body = (
            f"# {proposal_metadata['title']}\n\n"
            "Metadata enrichment 不修改 source capture；审批后只创建或更新 logical work。\n\n"
            f"## Diff\n\n```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(proposal_path, render_document(proposal_metadata, proposal_body).encode("utf-8"))
        return ProposalResult(proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path), self.repository.rel(target_path), action)
