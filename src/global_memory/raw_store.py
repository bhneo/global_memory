from __future__ import annotations

import json
import mimetypes
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .errors import ValidationError
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso, sha256_bytes


FailureHook = Callable[[str], None]


@dataclass(frozen=True)
class RawMigrationReport:
    dry_run: bool
    scanned_objects: int
    unique_contents: int
    merged_duplicates: int
    updated_sources: int
    errors: list[str]
    backup_path: str | None = None


class RawStoreService:
    JOURNAL_VERSION = 1

    def __init__(self, repository: Repository, failure_hook: FailureHook | None = None):
        self.repository = repository
        self.failure_hook = failure_hook
        self.journal_path = repository.root / "system" / "recovery" / "raw-store-migration.json"

    def _source_entries(self) -> tuple[list[dict[str, Any]], list[str]]:
        entries: list[dict[str, Any]] = []
        errors: list[str] = []
        for source_path in sorted(self.repository.source_documents()):
            metadata, body = read_document(source_path)
            relative = str(metadata.get("raw_content_path", ""))
            try:
                raw_path = self.repository.resolve_inside(relative)
            except Exception as exc:
                errors.append(f"source raw path 无效: {self.repository.rel(source_path)}: {exc}")
                continue
            if not raw_path.is_file():
                errors.append(f"source raw object 不存在: {self.repository.rel(source_path)} -> {relative}")
                continue
            digest = sha256_bytes(raw_path.read_bytes())
            expected = str(metadata.get("content_sha256", ""))
            if digest != expected:
                errors.append(f"source raw hash 不匹配: {self.repository.rel(source_path)}")
                continue
            target = self.repository.content_object_path(digest)
            migrated = dict(metadata)
            expected_id = f"content_{digest}"
            expected_path = self.repository.rel(target)
            content_type = str(migrated.get("content_type", "application/octet-stream"))
            mime_type = content_type.split(";", 1)[0].strip().lower()
            original_filename = str(migrated.get("original_filename", ""))
            if not original_filename and migrated.get("source_kind") == "files":
                original_filename = Path(str(migrated.get("original_locator", ""))).name
            display_extension = str(migrated.get("display_extension", ""))
            if not display_extension:
                display_extension = mimetypes.guess_extension(mime_type, strict=False) or ""
            changed = (
                migrated.get("content_id") != expected_id
                or migrated.get("raw_content_path") != expected_path
                or migrated.get("mime_type") != mime_type
                or migrated.get("original_filename") != original_filename
                or migrated.get("display_extension") != display_extension
            )
            migrated["content_id"] = expected_id
            migrated["raw_content_path"] = expected_path
            migrated["mime_type"] = mime_type
            migrated["original_filename"] = original_filename
            migrated["display_extension"] = display_extension
            if changed:
                migrated["updated_at"] = now_iso()
            after_text = render_document(migrated, body)
            entries.append({
                "source_path": self.repository.rel(source_path),
                "source_before_sha256": sha256_bytes(source_path.read_bytes()),
                "source_after_text": after_text,
                "requires_update": sha256_bytes(source_path.read_bytes()) != sha256_bytes(after_text.encode("utf-8")),
                "old_raw_path": relative,
                "object_path": self.repository.rel(target),
                "content_sha256": digest,
            })
        return entries, errors

    def plan(self) -> RawMigrationReport:
        entries, errors = self._source_entries()
        legacy_paths = {entry["old_raw_path"] for entry in entries}
        digests = {entry["content_sha256"] for entry in entries}
        updates = sum(bool(entry["requires_update"]) for entry in entries)
        return RawMigrationReport(
            True, len(legacy_paths), len(digests), max(0, len(legacy_paths) - len(digests)),
            updates, errors,
        )

    def _prepare(self) -> dict[str, Any]:
        entries, errors = self._source_entries()
        if errors:
            raise ValidationError("raw-store migration preflight failed: " + "; ".join(errors))
        entries = [entry for entry in entries if entry["requires_update"]]
        timestamp = now_iso().replace(":", "-")
        backup_root = self.repository.root / "data" / "backups" / f"raw-store-migration-{timestamp}"
        backup_root.mkdir(parents=True, exist_ok=False)
        for entry in entries:
            source = self.repository.resolve_inside(entry["source_path"])
            destination = backup_root / entry["source_path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            self.repository.immutable_write(destination, source.read_bytes())
        manifest = {
            "migration": "raw-store-v1", "created_at": now_iso(),
            "entries": [{
                "source_path": item["source_path"],
                "source_sha256": item["source_before_sha256"],
                "old_raw_path": item["old_raw_path"],
            } for item in entries],
        }
        atomic_write_text(backup_root / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        record = {
            "journal_version": self.JOURNAL_VERSION,
            "migration": "raw-store-v1",
            "created_at": now_iso(), "updated_at": now_iso(),
            "backup_path": self.repository.rel(backup_root),
            "entries": entries, "completed_sources": [],
        }
        atomic_write_text(self.journal_path, json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        return record

    def _load_journal(self) -> dict[str, Any]:
        record = json.loads(self.journal_path.read_text(encoding="utf-8"))
        if record.get("journal_version") != self.JOURNAL_VERSION or record.get("migration") != "raw-store-v1":
            raise ValidationError("不支持的 raw-store migration journal")
        return record

    def migrate(self) -> RawMigrationReport:
        if not self.journal_path.exists():
            planned = self.plan()
            if planned.errors:
                return RawMigrationReport(False, planned.scanned_objects, planned.unique_contents,
                                          planned.merged_duplicates, 0, planned.errors)
            if planned.updated_sources == 0:
                verification = self.verify()
                return RawMigrationReport(False, planned.scanned_objects, planned.unique_contents,
                                          planned.merged_duplicates, 0, verification["errors"])
        record = self._load_journal() if self.journal_path.exists() else self._prepare()
        completed = set(record.get("completed_sources", []))
        for entry in record["entries"]:
            object_path = self.repository.resolve_inside(entry["object_path"])
            old_raw_path = self.repository.resolve_inside(entry["old_raw_path"])
            payload = old_raw_path.read_bytes()
            if sha256_bytes(payload) != entry["content_sha256"]:
                raise ValidationError(f"migration input changed: {entry['old_raw_path']}")
            self.repository.immutable_write(object_path, payload)
        if self.failure_hook:
            self.failure_hook("objects_written")
        for entry in record["entries"]:
            relative = entry["source_path"]
            if relative in completed:
                continue
            source_path = self.repository.resolve_inside(relative)
            before = entry["source_before_sha256"]
            after_text = entry["source_after_text"]
            after = sha256_bytes(after_text.encode("utf-8"))
            current = sha256_bytes(source_path.read_bytes())
            if current == before:
                atomic_write_text(source_path, after_text)
            elif current != after:
                raise ValidationError(f"migration blocked: source changed: {relative}")
            completed.add(relative)
            record["completed_sources"] = sorted(completed)
            record["updated_at"] = now_iso()
            atomic_write_text(self.journal_path, json.dumps(record, ensure_ascii=False, indent=2) + "\n")
            if self.failure_hook:
                self.failure_hook("source_written")
        verification = self.verify()
        if not verification["ok"]:
            raise ValidationError("raw-store migration verify failed: " + "; ".join(verification["errors"]))
        self.repository.rebuild_index()
        self.journal_path.unlink()
        old_paths = {entry["old_raw_path"] for entry in record["entries"]}
        digests = {entry["content_sha256"] for entry in record["entries"]}
        return RawMigrationReport(
            False, len(old_paths), len(digests), max(0, len(old_paths) - len(digests)),
            len(record["entries"]), [], record["backup_path"],
        )

    def verify(self) -> dict[str, Any]:
        errors: list[str] = []
        checked_objects: set[str] = set()
        checked_sources = 0
        for source_path in sorted(self.repository.source_documents()):
            metadata, _ = read_document(source_path)
            digest = str(metadata.get("content_sha256", ""))
            expected_id = f"content_{digest}"
            try:
                expected_path = self.repository.content_object_path(digest)
            except ValidationError as exc:
                errors.append(f"无效 content hash: {self.repository.rel(source_path)}: {exc}")
                continue
            if metadata.get("content_id") != expected_id:
                errors.append(f"content_id 不匹配: {self.repository.rel(source_path)}")
            if metadata.get("raw_content_path") != self.repository.rel(expected_path):
                errors.append(f"object path 非全局哈希路径: {self.repository.rel(source_path)}")
            if not expected_path.is_file():
                errors.append(f"content object 缺失: {self.repository.rel(expected_path)}")
            elif digest not in checked_objects and sha256_bytes(expected_path.read_bytes()) != digest:
                errors.append(f"content object hash 不匹配: {self.repository.rel(expected_path)}")
            checked_objects.add(digest)
            checked_sources += 1
        return {
            "ok": not errors, "checked_sources": checked_sources,
            "unique_objects": len(checked_objects), "errors": errors,
        }
