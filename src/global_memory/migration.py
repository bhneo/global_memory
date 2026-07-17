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


class TrustPolicyRequalificationMigration:
    """Mark legacy Trusted objects for policy requalification without demotion."""

    POLICY_VERSION = "trusted-promotion-v3-receipt-v2"

    def __init__(self, repository: Repository):
        self.repository = repository

    def plan(self) -> dict[str, Any]:
        from .consolidation import ConsolidationReceiptService
        receipts = ConsolidationReceiptService(self.repository)
        changes = []
        for path in self.repository.memory_documents():
            metadata, _ = read_document(path)
            if metadata.get("memory_tier") != "trusted":
                continue
            history = [item for item in metadata.get("promotion_history", []) if isinstance(item, dict) and item.get("to_status") == "trusted"]
            previous = history[-1] if history else {}
            current_receipt = receipts.valid_for(str(metadata["id"]))
            already_marked = metadata.get("needs_policy_requalification") is True
            current_policy = metadata.get("trust_policy_version") == self.POLICY_VERSION
            if current_receipt and current_policy and not already_marked:
                continue
            if already_marked and metadata.get("trust_policy_version") == previous.get("policy_version", "trusted-promotion-v1"):
                continue
            changes.append({
                "path": self.repository.rel(path), "object_id": metadata["id"],
                "action": "mark_policy_requalification", "reason": "legacy Trusted requires Policy v3 qualification",
                "previous_policy_version": previous.get("policy_version", "trusted-promotion-v1"),
                "last_policy_qualified_at": previous.get("promoted_at"),
            })
        return {"dry_run": True, "policy_version": self.POLICY_VERSION, "trusted_to_requalify": changes, "canonical_content_writes": 0}

    def apply(self) -> dict[str, Any]:
        plan = self.plan()
        if not plan["trusted_to_requalify"]:
            return {**plan, "dry_run": False, "idempotent_noop": True, "backup_path": None}
        stamp = now_iso().replace(":", "-")
        backup = self.repository.root / "data" / "backups" / f"trust-requalification-{stamp}"
        changed = []
        for item in plan["trusted_to_requalify"]:
            path = self.repository.resolve_inside(str(item["path"]))
            original = path.read_bytes()
            backup_path = backup / str(item["path"])
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            backup_path.write_bytes(original)
            metadata, body = read_document(path)
            metadata.update({
                "status": "trusted", "memory_tier": "trusted",
                "needs_policy_requalification": True,
                "trust_policy_version": item["previous_policy_version"],
                "last_policy_qualified_at": item["last_policy_qualified_at"],
                "last_valid_receipt_id": None,
                "updated_at": now_iso(), "updated_by": "trust-requalification-v2",
            })
            atomic_write_text(path, render_document(metadata, body))
            changed.append({**item, "sha256_before": sha256_bytes(original), "sha256_after": sha256_bytes(path.read_bytes())})
        self.repository.rebuild_index()
        return {**plan, "dry_run": False, "backup_path": self.repository.rel(backup), "documents_changed": len(changed), "changed": changed, "idempotent_noop": False}

    def verify(self) -> dict[str, Any]:
        issues = []
        for path in self.repository.memory_documents():
            metadata, _ = read_document(path)
            if metadata.get("updated_by") == self.POLICY_VERSION and metadata.get("memory_tier") == "working":
                issues.append({"object_id": metadata.get("id"), "path": self.repository.rel(path), "reason": "legacy faulty demotion remains"})
            if metadata.get("needs_policy_requalification") and metadata.get("memory_tier") != "trusted":
                issues.append({"object_id": metadata.get("id"), "path": self.repository.rel(path), "reason": "requalification marker requires Trusted tier"})
        return {"ok": not issues, "verified": not issues, "issues": issues, "canonical_content_writes": 0}


class TrustRequalificationRepairMigration:
    """Safely reverse the M8.1 migration that incorrectly demoted legacy Trusted."""

    POLICY_VERSION = TrustPolicyRequalificationMigration.POLICY_VERSION
    CORRECTOR = "trust-requalification-correction-v1"

    def __init__(self, repository: Repository):
        self.repository = repository

    def _source_backup(self) -> Path | None:
        roots = sorted(
            (
                path for path in (self.repository.root / "data" / "backups").glob("trust-requalification-*" )
                if path.name.removeprefix("trust-requalification-")[:1].isdigit()
            ),
            key=lambda path: path.name,
            reverse=True,
        )
        return next((path for path in roots if (path / "vault" / "memory").is_dir()), None)

    @staticmethod
    def _promotion(metadata: dict[str, Any]) -> dict[str, Any] | None:
        history = [
            item for item in metadata.get("promotion_history", [])
            if isinstance(item, dict) and item.get("to_status") == "trusted"
        ]
        return history[-1] if history else None

    @staticmethod
    def _semantic_state(metadata: dict[str, Any]) -> dict[str, Any]:
        ignored = {"status", "memory_tier", "updated_at", "updated_by", "needs_revalidation"}
        return {key: value for key, value in metadata.items() if key not in ignored}

    def _has_demotion(self, object_id: str) -> bool:
        directory = self.repository.root / "vault" / "receipts" / "demotions"
        if not directory.exists():
            return False
        for path in directory.glob("*.md"):
            metadata, _ = read_document(path)
            if metadata.get("object_id") == object_id:
                return True
        return False

    def plan(self) -> dict[str, Any]:
        backup = self._source_backup()
        if backup is None:
            return {"dry_run": True, "source_backup": None, "original_migration_objects": 0, "restorable": [], "conflicts": [], "unrestored": [], "canonical_content_writes": 0}
        restorable, conflicts, unrestored = [], [], []
        for old_path in sorted((backup / "vault" / "memory").rglob("*.md")):
            old, old_body = read_document(old_path)
            object_id = str(old.get("id"))
            relative = old_path.relative_to(backup).as_posix()
            try:
                current_path, current, current_body = self.repository.find_document(object_id)
            except Exception:
                unrestored.append({"object_id": object_id, "path": relative, "reason": "current object missing"})
                continue
            promotion = self._promotion(old)
            basic = (
                old.get("legacy_status") == "trusted"
                and old.get("memory_tier") == "trusted"
                and promotion is not None
                and current.get("memory_tier") == "working"
                and current.get("updated_by") == self.POLICY_VERSION
                and current.get("needs_revalidation") is True
                and current.get("epistemic_status") not in {"contested", "superseded"}
                and not self._has_demotion(object_id)
            )
            unchanged = current_body == old_body and self._semantic_state(current) == self._semantic_state(old)
            item = {"object_id": object_id, "path": self.repository.rel(current_path), "backup_path": relative}
            if basic and unchanged:
                restorable.append({**item, "previous_policy_version": promotion.get("policy_version", "trusted-promotion-v1"), "last_policy_qualified_at": promotion.get("promoted_at")})
            elif current.get("updated_by") == self.POLICY_VERSION:
                conflicts.append({**item, "reason": "post-migration state cannot be proven identical to backup"})
            else:
                unrestored.append({**item, "reason": "object no longer has faulty migration signature"})
        return {
            "dry_run": True, "source_backup": self.repository.rel(backup),
            "original_migration_objects": len(restorable) + len(conflicts) + len(unrestored),
            "restorable": restorable, "conflicts": conflicts, "unrestored": unrestored,
            "canonical_content_writes": 0,
        }

    def apply(self) -> dict[str, Any]:
        plan = self.plan()
        if not plan["restorable"] and not plan["conflicts"]:
            return {**plan, "dry_run": False, "restored": 0, "idempotent_noop": True, "backup_path": None}
        stamp = now_iso().replace(":", "-")
        backup = self.repository.root / "data" / "backups" / f"trust-requalification-correction-{stamp}"
        before_images: list[tuple[Path, bytes]] = []
        restored = []
        try:
            for item in plan["restorable"]:
                path = self.repository.resolve_inside(str(item["path"]))
                before = path.read_bytes()
                before_images.append((path, before))
                backup_path = backup / str(item["path"])
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                backup_path.write_bytes(before)
                metadata, body = read_document(path)
                metadata.update({
                    "status": "trusted", "memory_tier": "trusted",
                    "needs_policy_requalification": True,
                    "trust_policy_version": item["previous_policy_version"],
                    "last_policy_qualified_at": item["last_policy_qualified_at"],
                    "last_valid_receipt_id": None,
                    "updated_at": now_iso(), "updated_by": self.CORRECTOR,
                })
                metadata.pop("needs_revalidation", None)
                atomic_write_text(path, render_document(metadata, body))
                restored.append({"object_id": item["object_id"], "path": item["path"], "sha256_before": sha256_bytes(before), "sha256_after": sha256_bytes(path.read_bytes())})
            if plan["conflicts"]:
                from .memory import ExceptionService
                exceptions = ExceptionService(self.repository)
                for item in plan["conflicts"]:
                    item["exception_id"] = exceptions.create(
                        "requalification-restore-conflict",
                        f"Trust requalification restore conflict: {item['object_id']}",
                        [str(item["reason"])], object_id=str(item["object_id"]), context=item,
                        severity="must_confirm",
                    )
            self.repository.rebuild_index()
        except Exception:
            for path, before in reversed(before_images):
                path.write_bytes(before)
            self.repository.rebuild_index()
            raise
        report = {
            **plan, "dry_run": False, "backup_path": self.repository.rel(backup),
            "restored": len(restored), "restored_objects": restored,
            "conflict_count": len(plan["conflicts"]), "unrestored_count": len(plan["unrestored"]),
            "idempotent_noop": False,
        }
        report_path = self.repository.root / "system" / "reports" / f"trust-requalification-correction-{stamp}.md"
        atomic_write_text(report_path, "# Trust Requalification Correction Report\n\n" + "\n".join([
            f"- Original migration objects: {plan['original_migration_objects']}",
            f"- Safely restored: {len(restored)}", f"- Conflicts: {len(plan['conflicts'])}",
            f"- Unrestored: {len(plan['unrestored'])}", "- Canonical writes: 0",
        ]) + "\n")
        report["report_path"] = self.repository.rel(report_path)
        return report
