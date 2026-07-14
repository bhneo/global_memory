from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ValidationError
from .markdown import atomic_write_text
from .repository import Repository, now_iso, sha256_bytes


MANIFEST_VERSION = 1
BACKUP_MANIFEST_NAME = "global-memory-raw-manifest.json"


@dataclass(frozen=True)
class BackupResult:
    manifest_path: str
    copied: list[str]
    skipped: list[str]
    conflicts: list[str]


class RawBackupService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def _raw_files(self) -> list[Path]:
        raw_root = self.repository.root / "vault" / "raw"
        if not raw_root.exists():
            return []
        return sorted(
            path for path in raw_root.rglob("*")
            if path.is_file() and path.name != ".gitkeep"
        )

    def manifest(self) -> dict[str, Any]:
        files = []
        for path in self._raw_files():
            payload = path.read_bytes()
            files.append({
                "path": self.repository.rel(path),
                "sha256": sha256_bytes(payload),
                "bytes": len(payload),
            })
        return {
            "manifest_version": MANIFEST_VERSION,
            "scope": "vault/raw",
            "created_at": now_iso(),
            "files": files,
        }

    def write_manifest(self, output: Path | str | None = None) -> str:
        path = (
            self.repository.root / "data" / "backups" / BACKUP_MANIFEST_NAME
            if output is None else Path(output).expanduser().resolve()
        )
        atomic_write_text(path, json.dumps(self.manifest(), ensure_ascii=False, indent=2) + "\n")
        return str(path)

    def _backup_root(self, directory: Path | str) -> Path:
        root = Path(directory).expanduser().resolve()
        try:
            root.relative_to(self.repository.root)
        except ValueError:
            return root
        raise ValidationError("备份目录必须位于 Global Memory 仓库之外")

    @staticmethod
    def _path_inside(root: Path, relative: str) -> Path:
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise ValidationError(f"备份 manifest 路径越界: {relative}") from exc
        return candidate

    def backup(self, directory: Path | str) -> BackupResult:
        root = self._backup_root(directory)
        manifest = self.manifest()
        copied: list[str] = []
        skipped: list[str] = []
        conflicts: list[str] = []
        for entry in manifest["files"]:
            relative = str(entry["path"])
            source = self.repository.resolve_inside(relative)
            destination = self._path_inside(root, relative)
            if destination.exists():
                if destination.is_file() and sha256_bytes(destination.read_bytes()) == entry["sha256"]:
                    skipped.append(relative)
                else:
                    conflicts.append(relative)
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            payload = source.read_bytes()
            with destination.open("xb") as handle:
                handle.write(payload)
                handle.flush()
                os.fsync(handle.fileno())
            copied.append(relative)
        manifest_path = root / BACKUP_MANIFEST_NAME
        if not conflicts:
            atomic_write_text(manifest_path, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        return BackupResult(str(manifest_path), copied, skipped, conflicts)

    def _load_backup_manifest(self, directory: Path | str) -> tuple[Path, dict[str, Any]]:
        root = self._backup_root(directory)
        manifest_path = root / BACKUP_MANIFEST_NAME
        if not manifest_path.is_file():
            raise ValidationError(f"备份 manifest 不存在: {manifest_path}")
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValidationError(f"无法读取备份 manifest: {manifest_path}") from exc
        if (
            manifest.get("manifest_version") != MANIFEST_VERSION
            or manifest.get("scope") != "vault/raw"
            or not isinstance(manifest.get("files"), list)
        ):
            raise ValidationError("不支持或无效的 raw backup manifest")
        seen_paths: set[str] = set()
        for entry in manifest["files"]:
            if not isinstance(entry, dict) or set(("path", "sha256", "bytes")) - entry.keys():
                raise ValidationError("raw backup manifest 包含无效文件条目")
            relative = str(entry["path"])
            if relative in seen_paths:
                raise ValidationError(f"raw backup manifest 包含重复路径: {relative}")
            seen_paths.add(relative)
            if not relative.startswith("vault/raw/"):
                raise ValidationError(f"raw backup manifest 超出 scope: {relative}")
            self.repository.resolve_inside(relative)
            self._path_inside(root, relative)
            if not isinstance(entry["sha256"], str) or not isinstance(entry["bytes"], int):
                raise ValidationError(f"raw backup manifest 条目类型无效: {relative}")
        return root, manifest

    def verify(self, directory: Path | str) -> dict[str, Any]:
        root, manifest = self._load_backup_manifest(directory)
        errors: list[str] = []
        for entry in manifest["files"]:
            relative = str(entry["path"])
            path = self._path_inside(root, relative)
            if not path.is_file():
                errors.append(f"备份缺少文件: {relative}")
            elif path.stat().st_size != entry["bytes"]:
                errors.append(f"备份文件大小不匹配: {relative}")
            elif sha256_bytes(path.read_bytes()) != entry["sha256"]:
                errors.append(f"备份文件哈希不匹配: {relative}")
        return {"ok": not errors, "files": len(manifest["files"]), "errors": errors}

    def restore(self, directory: Path | str, apply: bool = False) -> dict[str, Any]:
        root, manifest = self._load_backup_manifest(directory)
        verification = self.verify(root)
        if not verification["ok"]:
            return {
                "ok": False,
                "dry_run": not apply,
                "restored": [],
                "unchanged": [],
                "conflicts": [],
                "errors": verification["errors"],
            }
        missing: list[tuple[dict[str, Any], Path, Path]] = []
        unchanged: list[str] = []
        conflicts: list[str] = []
        for entry in manifest["files"]:
            relative = str(entry["path"])
            source = self._path_inside(root, relative)
            target = self.repository.resolve_inside(relative)
            if not target.exists():
                missing.append((entry, source, target))
            elif target.is_file() and sha256_bytes(target.read_bytes()) == entry["sha256"]:
                unchanged.append(relative)
            else:
                conflicts.append(relative)
        restored: list[str] = []
        if apply and not conflicts:
            for entry, source, target in missing:
                payload = source.read_bytes()
                self.repository.immutable_write(target, payload)
                restored.append(str(entry["path"]))
            if restored:
                self.repository.rebuild_index()
        return {
            "ok": not conflicts,
            "dry_run": not apply,
            "restored": restored if apply else [str(entry["path"]) for entry, _, _ in missing],
            "unchanged": unchanged,
            "conflicts": conflicts,
            "errors": [],
        }
