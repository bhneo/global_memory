from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .quality import SourceQualityService
from .repository import Repository, now_iso


FOLLOWUP_STATUSES = {"missing", "captured", "inaccessible", "not_identified", "not_required", "resolved"}


class FollowupService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault/followups"

    def _path(self, followup_id: str) -> Path:
        return self.directory / f"followup-{followup_id}.md"

    def create(self, source_id: str, locator: str | None, *, reason: str, kind: str = "primary_source") -> dict[str, Any]:
        digest = hashlib.sha256(f"{source_id}\n{locator or ''}\n{kind}".encode()).hexdigest()[:20]
        followup_id = f"followup_{digest}"
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

    def list(self) -> list[dict[str, Any]]:
        result = []
        if not self.directory.exists():
            return result
        for path in sorted(self.directory.glob("followup-*.md")):
            metadata, _ = read_document(path)
            result.append({**metadata, "path": self.repository.rel(path)})
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
