from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .quality import SourceQualityService, normalize_primary_locator
from .repository import Repository, now_iso


FOLLOWUP_STATUSES = {"missing", "captured", "inaccessible", "not_identified", "not_required", "resolved", "superseded"}


class FollowupService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault/followups"

    def _path(self, followup_id: str) -> Path:
        return self.directory / f"followup-{followup_id}.md"

    @staticmethod
    def _id(source_id: str, locator: str | None, kind: str) -> str:
        digest = hashlib.sha256(f"{source_id}\n{locator or ''}\n{kind}".encode()).hexdigest()[:20]
        return f"followup_{digest}"

    def create(self, source_id: str, locator: str | None, *, reason: str, kind: str = "primary_source") -> dict[str, Any]:
        locator = normalize_primary_locator(locator) if locator else None
        followup_id = self._id(source_id, locator, kind)
        path = self._path(followup_id)
        if path.exists():
            metadata, _ = read_document(path)
            return {**metadata, "path": self.repository.rel(path)}
        timestamp = now_iso()
        metadata = {
            "id": followup_id, "type": "followup", "status": "missing" if locator else "not_identified",
            "title": f"Primary source follow-up for {source_id}", "created_at": timestamp,
            "updated_at": timestamp, "source_id": source_id, "followup_kind": kind,
            "primary_source_locator": locator, "reason": reason,
            "captured_source_id": None, "resolution_history": [],
        }
        body = f"# Primary source follow-up\n\n- Secondary source: `{source_id}`\n- Locator: `{locator or 'not identified'}`\n- Reason: {reason}\n"
        self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        self.repository.append_event("followup-events", {"event": "followup-created", "followup_id": followup_id, "source_id": source_id, "locator": locator})
        return {**metadata, "path": self.repository.rel(path)}

    def detect(self, source_id: str) -> list[dict[str, Any]]:
        assessment = SourceQualityService(self.repository).assess(source_id, persist=True)
        if assessment.source_authority not in {"secondary_analysis", "industry_commentary", "social_post"}:
            return []
        return [self.create(source_id, locator, reason="secondary source cites an identifiable primary locator") for locator in assessment.primary_source_locators]

    def list(self, *, include_superseded: bool = False) -> list[dict[str, Any]]:
        result = []
        if not self.directory.exists():
            return result
        for path in sorted(self.directory.glob("followup-*.md")):
            metadata, _ = read_document(path)
            if metadata.get("status") == "superseded" and not include_superseded:
                continue
            result.append({**metadata, "path": self.repository.rel(path)})
        return result

    def normalize_locators(self, *, apply: bool = False) -> dict[str, Any]:
        """Canonicalize active locator identities while retaining superseded records."""
        candidates: list[tuple[Path, dict[str, Any], str, str]] = []
        for path in sorted(self.directory.glob("followup-*.md")):
            metadata, _ = read_document(path)
            locator = metadata.get("primary_source_locator")
            if not locator or metadata.get("status") == "superseded":
                continue
            normalized = normalize_primary_locator(str(locator))
            target_id = self._id(
                str(metadata["source_id"]), normalized, str(metadata.get("followup_kind", "primary_source"))
            )
            if target_id != metadata["id"] or normalized != locator:
                candidates.append((path, metadata, normalized, target_id))

        replacements = {metadata["id"]: target_id for _, metadata, _, target_id in candidates}
        proposal_changes: list[tuple[Path, dict[str, Any], str, list[str]]] = []
        for path in sorted(self.repository.proposal_documents()):
            metadata, body = read_document(path)
            refs = metadata.get("primary_source_followups")
            if not isinstance(refs, list):
                continue
            rewritten = list(dict.fromkeys(replacements.get(ref, ref) for ref in refs))
            if rewritten != refs:
                proposal_changes.append((path, metadata, body, rewritten))

        active_ids = {item["id"] for item in self.list()}
        replaced_ids = set(replacements)
        target_ids = set(replacements.values())
        result: dict[str, Any] = {
            "dry_run": not apply,
            "changed_followups": len(candidates),
            "changed_proposals": len(proposal_changes),
            "active_before": len(self.list()),
            "active_after": len(active_ids - replaced_ids | target_ids),
            "replacements": replacements,
            "backup_path": None,
        }
        if not apply or not candidates:
            return result

        timestamp = now_iso()
        backup = self.repository.root / "data/backups" / f"followup-locator-migration-{timestamp.replace(':', '-')}"
        for path, *_ in candidates:
            destination = backup / self.repository.rel(path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)
        for path, *_ in proposal_changes:
            destination = backup / self.repository.rel(path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)

        groups: dict[str, list[tuple[Path, dict[str, Any], str]]] = {}
        for path, metadata, normalized, target_id in candidates:
            groups.setdefault(target_id, []).append((path, metadata, normalized))
        for target_id, members in groups.items():
            target_path = self._path(target_id)
            normalized = members[0][2]
            if target_path.exists():
                target_metadata, target_body = read_document(target_path)
            else:
                seed = members[0][1]
                target_metadata = {
                    **seed,
                    "id": target_id,
                    "primary_source_locator": normalized,
                    "updated_at": timestamp,
                    "migrated_from": [member[1]["id"] for member in members],
                }
                target_body = (
                    "# Primary source follow-up\n\n"
                    f"- Secondary source: `{seed['source_id']}`\n"
                    f"- Locator: `{normalized}`\n"
                    f"- Reason: {seed['reason']}\n"
                )
                atomic_write_text(target_path, render_document(target_metadata, target_body))
            migrated_from = list(target_metadata.get("migrated_from", []))
            target_metadata["migrated_from"] = list(dict.fromkeys(migrated_from + [m[1]["id"] for m in members]))
            status_rank = {"resolved": 5, "captured": 4, "missing": 3, "inaccessible": 2, "not_identified": 1, "not_required": 0}
            strongest = max([target_metadata, *[member[1] for member in members]], key=lambda item: status_rank.get(str(item.get("status")), -1))
            target_metadata["status"] = strongest.get("status", "missing")
            target_metadata["captured_source_id"] = strongest.get("captured_source_id")
            target_metadata["created_at"] = min(
                str(item["created_at"]) for item in [target_metadata, *[member[1] for member in members]]
            )
            target_metadata["updated_at"] = timestamp
            atomic_write_text(target_path, render_document(target_metadata, target_body))

            for old_path, old_metadata, _ in members:
                if old_path == target_path:
                    continue
                _, old_body = read_document(old_path)
                old_metadata["status"] = "superseded"
                old_metadata["superseded_by"] = target_id
                old_metadata["updated_at"] = timestamp
                old_metadata.setdefault("resolution_history", []).append({
                    "at": timestamp, "status": "superseded", "superseded_by": target_id,
                    "reason": "primary locator canonicalization",
                })
                atomic_write_text(old_path, render_document(old_metadata, old_body))

        for path, metadata, body, rewritten in proposal_changes:
            metadata["primary_source_followups"] = rewritten
            metadata["updated_at"] = timestamp
            atomic_write_text(path, render_document(metadata, body))
        self.repository.append_event("followup-events", {
            "event": "followup-locators-normalized", "changed_followups": len(candidates),
            "changed_proposals": len(proposal_changes), "backup_path": self.repository.rel(backup),
        })
        result["backup_path"] = self.repository.rel(backup)
        return result

    def show(self, followup_id: str) -> dict[str, Any]:
        path = self._path(followup_id)
        if not path.exists():
            raise NotFoundError(f"follow-up 不存在: {followup_id}")
        metadata, body = read_document(path)
        return {"path": self.repository.rel(path), "metadata": metadata, "body": body}

    def resolve(self, followup_id: str, captured_source_id: str | None = None, *, status: str = "resolved") -> str:
        if status not in FOLLOWUP_STATUSES:
            raise ValidationError(f"非法 follow-up status: {status}")
        path = self._path(followup_id)
        if not path.exists():
            raise NotFoundError(f"follow-up 不存在: {followup_id}")
        metadata, body = read_document(path)
        if captured_source_id:
            _, captured, _ = self.repository.find_document(captured_source_id)
            if captured.get("type") != "source":
                raise ValidationError("captured_source_id 必须是 source")
            metadata["captured_source_id"] = captured_source_id
            status = "resolved"
        event = {"at": now_iso(), "status": status, "captured_source_id": captured_source_id}
        metadata["status"] = status
        metadata["updated_at"] = event["at"]
        metadata.setdefault("resolution_history", []).append(event)
        atomic_write_text(path, render_document(metadata, body))
        self.repository.append_event("followup-events", {"event": "followup-resolved", "followup_id": followup_id, **event})
        return self.repository.rel(path)
