from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import NotFoundError, ValidationError
from .markdown import atomic_write_text, read_document
from .repository import Repository, now_iso, sha256_bytes


RUN_FILES = {
    "manifest.json", "source-summary.md", "compiler-output.json",
    "validation-report.md", "errors.jsonl", "metrics.json",
}


@dataclass(frozen=True)
class BatchMigrationResult:
    dry_run: bool
    run_id: str | None
    temporary_directories: list[str]
    files_scanned: int
    candidate_files: int
    candidates_matched_to_formal_proposals: int
    unmatched_candidates: int
    scripts: int
    backup_path: str | None
    removed_temporary_directories: list[str]
    errors: list[str]


class RunArtifactService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "system/runs"

    def list(self) -> list[dict[str, Any]]:
        result = []
        if not self.directory.exists():
            return result
        for path in sorted(self.directory.iterdir()):
            manifest = path / "manifest.json"
            if path.is_dir() and manifest.exists():
                data = json.loads(manifest.read_text(encoding="utf-8"))
                result.append({"run_id": path.name, "path": self.repository.rel(path), **data})
        return result

    def show(self, run_id: str) -> dict[str, Any]:
        path = (self.directory / run_id).resolve()
        try:
            path.relative_to(self.directory.resolve())
        except ValueError as exc:
            raise ValidationError("run id 越界") from exc
        if not path.is_dir():
            raise NotFoundError(f"run 不存在: {run_id}")
        files = []
        for item in sorted(path.iterdir()):
            files.append({"name": item.name, "bytes": item.stat().st_size, "sha256": sha256_bytes(item.read_bytes()) if item.is_file() else None})
        return {"run_id": run_id, "path": self.repository.rel(path), "files": files}

    def cleanup(self, run_id: str, *, apply: bool = False) -> dict[str, Any]:
        detail = self.show(run_id)
        path = (self.directory / run_id).resolve()
        if apply:
            shutil.rmtree(path)
        return {**detail, "dry_run": not apply, "removed": apply}


class BatchArtifactMigrator:
    """Move tracked .tmp-* batch debris out of the knowledge/proposal namespace."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.runs = RunArtifactService(repository)

    def _temporary_directories(self) -> list[Path]:
        return sorted(path for path in self.repository.root.iterdir() if path.is_dir() and path.name.startswith(".tmp-"))

    def plan(self) -> BatchMigrationResult:
        directories = self._temporary_directories()
        files = [path for directory in directories for path in directory.rglob("*") if path.is_file()]
        formal_candidates = {sha256_bytes(path.read_bytes()) for path in (self.repository.root / "vault/proposals").glob("candidate-*.md")}
        formal_object_ids: set[str] = set()
        for path in (self.repository.root / "vault/proposals").glob("candidate-*.md"):
            try:
                metadata, _ = read_document(path)
                formal_object_ids.add(str(metadata.get("id")))
            except Exception:
                continue
        candidates = [path for path in files if path.suffix.lower() == ".md" and path.name.startswith("candidate-")]
        matched = 0
        for path in candidates:
            digest = sha256_bytes(path.read_bytes())
            try:
                metadata, _ = read_document(path)
                object_id = str(metadata.get("id"))
            except Exception:
                object_id = ""
            matched += digest in formal_candidates or object_id in formal_object_ids
        return BatchMigrationResult(
            dry_run=True, run_id=None,
            temporary_directories=[self.repository.rel(path) for path in directories],
            files_scanned=len(files), candidate_files=len(candidates),
            candidates_matched_to_formal_proposals=matched,
            unmatched_candidates=len(candidates) - matched,
            scripts=sum(path.suffix.lower() == ".py" for path in files),
            backup_path=None, removed_temporary_directories=[], errors=[],
        )

    def migrate(self) -> BatchMigrationResult:
        plan = self.plan()
        if not plan.temporary_directories:
            return BatchMigrationResult(**{**plan.__dict__, "dry_run": False})
        stamp = now_iso().replace(":", "-")
        digest = hashlib.sha256("\n".join(plan.temporary_directories).encode()).hexdigest()[:10]
        run_id = f"batch-migration-{stamp}-{digest}"
        run_path = self.runs.directory / run_id
        backup = self.repository.root / "data/backups" / run_id
        run_path.mkdir(parents=True, exist_ok=False)
        backup.mkdir(parents=True, exist_ok=False)
        records: list[dict[str, Any]] = []
        formal_candidates = {
            sha256_bytes(path.read_bytes()): self.repository.rel(path)
            for path in (self.repository.root / "vault/proposals").glob("candidate-*.md")
        }
        formal_by_object: dict[str, str] = {}
        for path in (self.repository.root / "vault/proposals").glob("candidate-*.md"):
            try:
                metadata, _ = read_document(path)
                formal_by_object[str(metadata.get("id"))] = self.repository.rel(path)
            except Exception:
                continue
        for relative in plan.temporary_directories:
            source = self.repository.resolve_inside(relative)
            destination = backup / source.name
            shutil.copytree(source, destination)
            for path in source.rglob("*"):
                if not path.is_file():
                    continue
                digest_value = sha256_bytes(path.read_bytes())
                object_id = None
                if path.suffix.lower() == ".md" and path.name.startswith("candidate-"):
                    try:
                        candidate, _ = read_document(path)
                        object_id = str(candidate.get("id"))
                    except Exception:
                        pass
                records.append({
                    "path": self.repository.rel(path), "bytes": path.stat().st_size,
                    "sha256": digest_value, "object_id": object_id,
                    "formal_candidate_path": formal_candidates.get(digest_value) or formal_by_object.get(str(object_id)),
                    "kind": "candidate" if path.name.startswith("candidate-") else ("script" if path.suffix == ".py" else "artifact"),
                })
        manifest = {
            "run_id": run_id, "kind": "batch-artifact-migration", "created_at": now_iso(),
            "rebuildable": True, "formal_proposal_root": "vault/proposals",
            "temporary_directories": plan.temporary_directories,
            "backup_path": self.repository.rel(backup), "files": records,
        }
        atomic_write_text(run_path / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        atomic_write_text(run_path / "source-summary.md", "# Batch artifact migration\n\n正式 proposal 仅位于 `vault/proposals/`；本 run 不保存 candidate 正文。\n")
        atomic_write_text(run_path / "compiler-output.json", "{}\n")
        atomic_write_text(run_path / "validation-report.md", f"# Validation\n\n- Formal matches: {plan.candidates_matched_to_formal_proposals}\n- Quarantined unmatched candidates: {plan.unmatched_candidates}\n")
        atomic_write_text(run_path / "errors.jsonl", "")
        atomic_write_text(run_path / "metrics.json", json.dumps({
            "files_scanned": plan.files_scanned, "candidate_files": plan.candidate_files,
            "formal_matches": plan.candidates_matched_to_formal_proposals,
            "unmatched_candidates": plan.unmatched_candidates, "scripts": plan.scripts,
        }, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
        removed = []
        for relative in plan.temporary_directories:
            target = self.repository.resolve_inside(relative)
            target.relative_to(self.repository.root)
            shutil.rmtree(target)
            removed.append(relative)
        self.repository.append_event("source-processing-events", {
            "event": "batch-artifacts-migrated", "run_id": run_id,
            "backup_path": self.repository.rel(backup), "removed": removed,
        })
        return BatchMigrationResult(
            dry_run=False, run_id=run_id, temporary_directories=plan.temporary_directories,
            files_scanned=plan.files_scanned, candidate_files=plan.candidate_files,
            candidates_matched_to_formal_proposals=plan.candidates_matched_to_formal_proposals,
            unmatched_candidates=plan.unmatched_candidates, scripts=plan.scripts,
            backup_path=self.repository.rel(backup), removed_temporary_directories=removed, errors=[],
        )
