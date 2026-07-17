from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from .epistemics import EPISTEMIC_STATUSES, MEMORY_TIERS, normalized_dimensions
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso, sha256_bytes


class EpistemicStatusMigration:
    """Idempotently split legacy status into orthogonal memory and epistemic dimensions."""

    def __init__(self, repository: Repository):
        self.repository = repository

    def _documents(self) -> list[Path]:
        return sorted(path for path in {
            *self.repository.memory_documents(),
            *self.repository.canonical_documents(),
            *self.repository.archive_documents(),
        } if "/vault/archive/versions/" not in f"/{path.as_posix()}")

    def _change(self, path: Path, metadata: dict[str, Any]) -> dict[str, Any] | None:
        tier, epistemic = normalized_dimensions(metadata, path)
        if metadata.get("memory_tier") == tier and metadata.get("epistemic_status") == epistemic:
            return None
        return {
            "path": self.repository.rel(path),
            "object_id": metadata.get("id"),
            "legacy_status": metadata.get("status"),
            "memory_tier": tier,
            "epistemic_status": epistemic,
        }

    def plan(self) -> dict[str, Any]:
        changes: list[dict[str, Any]] = []
        unreadable: list[str] = []
        for path in self._documents():
            try:
                metadata, _ = read_document(path)
            except Exception:
                unreadable.append(self.repository.rel(path))
                continue
            change = self._change(path, metadata)
            if change:
                changes.append(change)
        return {
            "dry_run": True,
            "documents_considered": len(self._documents()),
            "documents_to_change": len(changes),
            "changes": changes,
            "unreadable": unreadable,
            "unknown_to_canonical": 0,
            "canonical_content_writes": 0,
        }

    def apply(self) -> dict[str, Any]:
        plan = self.plan()
        if not plan["changes"]:
            return {**plan, "dry_run": False, "backup_path": None, "idempotent_noop": True}
        stamp = now_iso().replace(":", "-")
        backup = self.repository.root / "data" / "backups" / f"epistemic-status-{stamp}"
        suffix = 1
        while backup.exists():
            backup = backup.with_name(f"epistemic-status-{stamp}-{suffix}")
            suffix += 1
        changed: list[dict[str, Any]] = []
        before_images: list[tuple[Path, bytes]] = []
        try:
            for item in plan["changes"]:
                path = self.repository.resolve_inside(str(item["path"]))
                before = path.read_bytes()
                before_images.append((path, before))
                backup_path = backup / str(item["path"])
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, backup_path)
                metadata, body = read_document(path)
                if "legacy_status" not in metadata:
                    metadata["legacy_status"] = metadata.get("status")
                metadata["memory_tier"] = item["memory_tier"]
                metadata["epistemic_status"] = item["epistemic_status"]
                metadata["status"] = item["memory_tier"]
                metadata["memory_schema_version"] = 2
                text = render_document(metadata, body)
                atomic_write_text(path, text)
                changed.append({
                    **item,
                    "sha256_before": sha256_bytes(before),
                    "sha256_after": sha256_bytes(path.read_bytes()),
                })
            self.repository.rebuild_index()
        except Exception:
            for path, before in reversed(before_images):
                path.write_bytes(before)
            self.repository.rebuild_index()
            raise
        report = {
            **plan,
            "dry_run": False,
            "backup_path": self.repository.rel(backup),
            "documents_changed": len(changed),
            "changed": changed,
            "idempotent_noop": False,
        }
        report_path = self.repository.root / "system" / "reports" / f"migration-epistemic-status-{stamp}.json"
        atomic_write_text(report_path, json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        report["report_path"] = self.repository.rel(report_path)
        return report

    def verify(self) -> dict[str, Any]:
        issues: list[dict[str, Any]] = []
        for path in self._documents():
            try:
                metadata, _ = read_document(path)
            except Exception:
                continue
            tier = metadata.get("memory_tier")
            epistemic = metadata.get("epistemic_status")
            if tier not in MEMORY_TIERS or epistemic not in EPISTEMIC_STATUSES:
                issues.append({
                    "path": self.repository.rel(path),
                    "object_id": metadata.get("id"),
                    "memory_tier": tier,
                    "epistemic_status": epistemic,
                })
        return {"ok": not issues, "verified": not issues, "issues": issues, "documents_checked": len(self._documents())}
