from __future__ import annotations

import difflib
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso, sha256_bytes, slugify


@dataclass(frozen=True)
class ProposalResult:
    proposal_id: str
    proposal_path: str
    candidate_path: str
    target_path: str
    action: str


class ProposalService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _source(self, source_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(source_id)
        if metadata.get("type") != "source":
            raise ValidationError(f"compile 只接受 source 对象: {source_id}")
        return path, metadata, body

    def _source_text(self, metadata: dict[str, Any]) -> str:
        raw_path = self.repository.resolve_inside(metadata["raw_content_path"])
        try:
            return raw_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return ""

    def compile(self, source_id: str) -> ProposalResult:
        source_path, source, _ = self._source(source_id)
        raw_text = self._source_text(source)
        excerpt = " ".join(raw_text.split())[:500]
        if not excerpt:
            excerpt = "该来源为二进制内容，第一版规则编译器未提取正文。"
        title = f"来自《{source['title']}》的待确认主张"
        target_digest = hashlib.sha256(f"claim\n{source_id}".encode("utf-8")).hexdigest()
        target_id = f"claim_{target_digest[:24]}"
        target_path = self.repository.root / "vault" / "knowledge" / "claims" / f"{target_id}-{slugify(source['title'])}.md"
        timestamp = now_iso()
        candidate_metadata = {
            "id": target_id,
            "type": "claim",
            "status": "proposal",
            "title": title,
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [source_id],
            "relations": [
                {"type": "derived_from", "target_id": source_id, "reason": "由该原始来源的规则编译结果提出"}
            ],
            "superseded_by": None,
            "valid_during": None,
            "change_reason": "由规则编译器提出，等待人工核验",
        }
        candidate_body = (
            f"# {title}\n\n"
            "## 候选主张\n\n"
            f"{excerpt}\n\n"
            "## 证据与位置\n\n"
            f"- 来源：[[{self.repository.rel(source_path)[:-3]}|{source_id}]]\n"
            "- 位置：正文开头（第一版规则编译器截取）\n"
            "- 证据方向：待人工判断支持或反对\n\n"
            "## 不确定性\n\n"
            "该内容由确定性规则生成，尚未经过模型解释或人工事实核验。批准仅表示纳入知识库，"
            "不自动将置信度提升为高。\n"
        )
        candidate_text = render_document(candidate_metadata, candidate_body)
        candidate_hash = sha256_bytes(candidate_text.encode("utf-8"))
        proposal_digest = hashlib.sha256(f"{source_id}\n{candidate_hash}".encode("utf-8")).hexdigest()
        proposal_id = f"proposal_{proposal_digest[:24]}"
        candidate_path = self.repository.root / "vault" / "proposals" / f"candidate-{proposal_id}.md"
        proposal_path = self.repository.root / "vault" / "proposals" / f"proposal-{proposal_id}.md"
        action = "update" if target_path.exists() else "create"

        if proposal_path.exists():
            existing, _ = read_document(proposal_path)
            return ProposalResult(
                proposal_id, self.repository.rel(proposal_path), existing["candidate_path"],
                existing["target_path"], existing["action"],
            )

        self.repository.immutable_write(candidate_path, candidate_text.encode("utf-8"))
        before = target_path.read_text(encoding="utf-8").splitlines(keepends=True) if target_path.exists() else []
        after = candidate_text.splitlines(keepends=True)
        diff = "".join(
            difflib.unified_diff(
                before, after,
                fromfile=self.repository.rel(target_path) if before else "/dev/null",
                tofile=self.repository.rel(target_path),
            )
        )
        proposal_metadata = {
            "id": proposal_id,
            "type": "proposal",
            "status": "pending",
            "title": f"编译 {source['title']}",
            "created_at": timestamp,
            "updated_at": timestamp,
            "aliases": [],
            "tags": [],
            "domains": [],
            "confidence": "unknown",
            "source_ids": [source_id],
            "relations": [],
            "processor": "deterministic-excerpt-v1",
            "action": action,
            "target_id": target_id,
            "target_path": self.repository.rel(target_path),
            "candidate_path": self.repository.rel(candidate_path),
            "candidate_sha256": candidate_hash,
            "reviewed_at": None,
            "review_reason": None,
        }
        proposal_body = (
            f"# {proposal_metadata['title']}\n\n"
            "## 编译说明\n\n"
            f"- 读取来源：[[{self.repository.rel(source_path)[:-3]}|{source_id}]]\n"
            f"- 建议操作：`{action}` `{self.repository.rel(target_path)}`\n"
            "- 矛盾：第一版规则处理器未自动判定，必须人工复核\n"
            "- 原因：将来源开头转换为一个低置信度候选主张，验证审批闭环\n\n"
            "## 内容级 Diff\n\n"
            f"```diff\n{diff.rstrip()}\n```\n"
        )
        self.repository.immutable_write(proposal_path, render_document(proposal_metadata, proposal_body).encode("utf-8"))
        self.repository.append_event(
            "proposal-events",
            {"event": "compiled", "proposal_id": proposal_id, "source_ids": [source_id], "action": action},
        )
        return ProposalResult(
            proposal_id, self.repository.rel(proposal_path), self.repository.rel(candidate_path),
            self.repository.rel(target_path), action,
        )

    def list(self, status: str | None = None) -> list[dict[str, Any]]:
        proposals: list[dict[str, Any]] = []
        for path in sorted(self.repository.proposal_documents()):
            metadata, _ = read_document(path)
            if status is None or metadata.get("status") == status:
                proposals.append({**metadata, "path": self.repository.rel(path)})
        return proposals

    def inbox(self) -> list[dict[str, str]]:
        compiled_sources = {
            source_id
            for proposal in self.list()
            for source_id in proposal.get("source_ids", [])
        }
        result = []
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            if metadata["id"] not in compiled_sources:
                result.append({"id": metadata["id"], "title": metadata["title"], "path": self.repository.rel(path)})
        return sorted(result, key=lambda item: item["id"])

    def show(self, proposal_id: str) -> str:
        path, metadata, body = self.repository.find_document(proposal_id)
        if metadata.get("type") != "proposal":
            raise ValidationError(f"不是 proposal: {proposal_id}")
        return render_document(metadata, body)

    def _load_proposal(self, proposal_id: str) -> tuple[Path, dict[str, Any], str]:
        path, metadata, body = self.repository.find_document(proposal_id)
        if metadata.get("type") != "proposal":
            raise ValidationError(f"不是 proposal: {proposal_id}")
        return path, metadata, body

    def approve(self, proposal_id: str) -> str:
        proposal_path, proposal, proposal_body = self._load_proposal(proposal_id)
        if proposal.get("status") != "pending":
            raise ValidationError(f"proposal 状态不是 pending: {proposal.get('status')}")
        candidate_path = self.repository.resolve_inside(proposal["candidate_path"])
        candidate_text = candidate_path.read_text(encoding="utf-8")
        if sha256_bytes(candidate_text.encode("utf-8")) != proposal["candidate_sha256"]:
            raise ValidationError("candidate 内容哈希不匹配，拒绝批准")
        candidate, body = read_document(candidate_path)
        if candidate.get("status") != "proposal" or candidate.get("id") != proposal["target_id"]:
            raise ValidationError("candidate 身份或状态无效")
        target_path = self.repository.resolve_inside(proposal["target_path"])
        if proposal["action"] == "create" and target_path.exists():
            raise ValidationError("目标已存在；请重新 compile 生成 update proposal")
        self.repository._validate_metadata(candidate, candidate_path)
        approved_at = now_iso()
        canonical = dict(candidate)
        canonical["status"] = "confirmed"
        canonical["updated_at"] = approved_at
        canonical["approved_via"] = proposal_id
        canonical["change_reason"] = f"人工批准 proposal {proposal_id}"
        canonical_text = render_document(canonical, body)

        # Canonical is written only after all proposal and candidate validation succeeds.
        atomic_write_text(target_path, canonical_text)
        proposal["status"] = "approved"
        proposal["updated_at"] = approved_at
        proposal["reviewed_at"] = approved_at
        proposal["review_reason"] = "人工通过 CLI 明确批准"
        atomic_write_text(proposal_path, render_document(proposal, proposal_body))
        self.repository.append_event(
            "proposal-events",
            {"event": "approved", "proposal_id": proposal_id, "target_path": proposal["target_path"]},
        )
        self.repository.rebuild_index()
        return self.repository.rel(target_path)

    def reject(self, proposal_id: str, reason: str = "") -> str:
        proposal_path, proposal, proposal_body = self._load_proposal(proposal_id)
        if proposal.get("status") != "pending":
            raise ValidationError(f"proposal 状态不是 pending: {proposal.get('status')}")
        reviewed_at = now_iso()
        proposal["status"] = "rejected"
        proposal["updated_at"] = reviewed_at
        proposal["reviewed_at"] = reviewed_at
        proposal["review_reason"] = reason or "人工拒绝"
        atomic_write_text(proposal_path, render_document(proposal, proposal_body))
        self.repository.append_event(
            "proposal-events", {"event": "rejected", "proposal_id": proposal_id, "reason": reason}
        )
        return self.repository.rel(proposal_path)
