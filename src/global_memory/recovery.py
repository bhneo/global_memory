from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .errors import ValidationError
from .markdown import atomic_write_text, parse_document_text
from .repository import Repository, now_iso, sha256_bytes


FailureHook = Callable[[str], None]


@dataclass(frozen=True)
class RecoveryResult:
    operation_id: str
    proposal_id: str
    target_path: str
    status: str


class ApprovalRecoveryManager:
    """Rolls canonical approvals forward from an atomic local journal."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "system" / "recovery"

    def journal_path(self, proposal_id: str) -> Path:
        return self.directory / f"approve-{proposal_id}.json"

    def pending(self) -> list[Path]:
        if not self.directory.exists():
            return []
        return sorted(self.directory.glob("approve-*.json"))

    def _write(self, path: Path, record: dict[str, Any]) -> None:
        atomic_write_text(
            path,
            json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )

    def _read(self, path: Path) -> dict[str, Any]:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValidationError(f"无法读取 recovery journal: {path.name}: {exc}") from exc
        if record.get("journal_version") != 1 or record.get("operation") != "approve_canonical":
            raise ValidationError(f"不支持的 recovery journal: {path.name}")
        return record

    def prepare(
        self,
        *,
        proposal_id: str,
        target_id: str,
        target_path: Path,
        target_before_sha256: str | None,
        target_after_text: str,
        proposal_path: Path,
        proposal_before_sha256: str,
        proposal_after_text: str,
        audit_payload: dict[str, Any],
    ) -> Path:
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.journal_path(proposal_id)
        if path.exists():
            existing = self._read(path)
            if existing.get("proposal_id") != proposal_id:
                raise ValidationError("existing recovery journal 与 proposal 不一致")
            return path

        target_metadata, _ = parse_document_text(target_after_text)
        proposal_metadata, _ = parse_document_text(proposal_after_text)
        approved_pair = (
            target_metadata.get("approved_via") == proposal_id
            and proposal_metadata.get("status") == "approved"
        )
        published_pair = (
            target_metadata.get("published_via") == proposal_id
            and target_metadata.get("status") == "provisional"
            and proposal_metadata.get("status") == "published"
        )
        if (
            target_metadata.get("id") != target_id
            or proposal_metadata.get("id") != proposal_id
            or not (approved_pair or published_pair)
        ):
            raise ValidationError("拒绝创建内容身份无效的 canonical journal")
        operation_id = f"{'approve' if approved_pair else 'publish'}_{proposal_id}"
        record = {
            "journal_version": 1,
            "operation": "approve_canonical",
            "operation_id": operation_id,
            "proposal_id": proposal_id,
            "target_id": target_id,
            "phase": "prepared",
            "created_at": now_iso(),
            "updated_at": now_iso(),
            "target_path": self.repository.rel(target_path),
            "target_before_sha256": target_before_sha256,
            "target_after_sha256": sha256_bytes(target_after_text.encode("utf-8")),
            "target_after_text": target_after_text,
            "proposal_path": self.repository.rel(proposal_path),
            "proposal_before_sha256": proposal_before_sha256,
            "proposal_after_sha256": sha256_bytes(proposal_after_text.encode("utf-8")),
            "proposal_after_text": proposal_after_text,
            "audit_log": "proposal-events",
            "audit_payload": {**audit_payload, "operation_id": operation_id},
        }
        self._write(path, record)
        return path

    def _checkpoint(self, hook: FailureHook | None, phase: str) -> None:
        if hook is not None:
            hook(phase)

    def _set_phase(self, path: Path, record: dict[str, Any], phase: str) -> None:
        record["phase"] = phase
        record["updated_at"] = now_iso()
        self._write(path, record)

    def _event_exists(self, log_name: str, operation_id: str) -> bool:
        path = self.repository.root / "system" / "logs" / f"{log_name}.jsonl"
        if not path.exists():
            return False
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                if json.loads(line).get("operation_id") == operation_id:
                    return True
            except json.JSONDecodeError:
                continue
        return False

    def recover_one(
        self,
        path: Path,
        failure_hook: FailureHook | None = None,
    ) -> RecoveryResult:
        record = self._read(path)
        target_path = self.repository.resolve_inside(record["target_path"])
        proposal_path = self.repository.resolve_inside(record["proposal_path"])
        target_after = record["target_after_text"]
        proposal_after = record["proposal_after_text"]
        if sha256_bytes(target_after.encode("utf-8")) != record["target_after_sha256"]:
            raise ValidationError(f"journal target payload 哈希不匹配: {path.name}")
        if sha256_bytes(proposal_after.encode("utf-8")) != record["proposal_after_sha256"]:
            raise ValidationError(f"journal proposal payload 哈希不匹配: {path.name}")
        target_metadata, _ = parse_document_text(target_after)
        proposal_metadata, _ = parse_document_text(proposal_after)
        approved_pair = (
            target_metadata.get("approved_via") == record["proposal_id"]
            and proposal_metadata.get("status") == "approved"
        )
        published_pair = (
            target_metadata.get("published_via") == record["proposal_id"]
            and target_metadata.get("status") == "provisional"
            and proposal_metadata.get("status") == "published"
        )
        if (
            not record["target_path"].startswith(
                ("vault/knowledge/", "vault/frontier/", "vault/action/")
            )
            or not record["proposal_path"].startswith("vault/proposals/proposal-")
            or target_metadata.get("id") != record["target_id"]
            or proposal_metadata.get("id") != record["proposal_id"]
            or not (approved_pair or published_pair)
            or record["audit_payload"].get("operation_id") != record["operation_id"]
        ):
            raise ValidationError(f"journal 身份或路径约束无效: {path.name}")

        target_current = sha256_bytes(target_path.read_bytes()) if target_path.exists() else None
        if target_current == record["target_before_sha256"]:
            atomic_write_text(target_path, target_after)
        elif target_current != record["target_after_sha256"]:
            raise ValidationError(
                f"recovery blocked: target 既不是写前也不是写后状态: {record['target_path']}"
            )
        self._set_phase(path, record, "target_written")
        self._checkpoint(failure_hook, "target_written")

        if not proposal_path.exists():
            raise ValidationError(f"recovery blocked: proposal 文件不存在: {record['proposal_path']}")
        proposal_current = sha256_bytes(proposal_path.read_bytes())
        if proposal_current == record["proposal_before_sha256"]:
            atomic_write_text(proposal_path, proposal_after)
        elif proposal_current != record["proposal_after_sha256"]:
            raise ValidationError(
                f"recovery blocked: proposal 既不是写前也不是写后状态: {record['proposal_path']}"
            )
        self._set_phase(path, record, "proposal_written")
        self._checkpoint(failure_hook, "proposal_written")

        if not self._event_exists(record["audit_log"], record["operation_id"]):
            self.repository.append_event(record["audit_log"], record["audit_payload"])
        self._set_phase(path, record, "audit_written")
        self._checkpoint(failure_hook, "audit_written")

        self.repository.rebuild_index()
        self._set_phase(path, record, "index_rebuilt")
        self._checkpoint(failure_hook, "index_rebuilt")
        path.unlink()
        return RecoveryResult(
            operation_id=record["operation_id"],
            proposal_id=record["proposal_id"],
            target_path=record["target_path"],
            status="recovered",
        )

    def recover_all(self) -> dict[str, list[dict[str, str]]]:
        recovered: list[dict[str, str]] = []
        blocked: list[dict[str, str]] = []
        for path in self.pending():
            try:
                recovered.append(self.recover_one(path).__dict__)
            except (OSError, sqlite3.Error, ValidationError) as exc:
                blocked.append({"journal": self.repository.rel(path), "error": str(exc)})
        return {"recovered": recovered, "blocked": blocked}
