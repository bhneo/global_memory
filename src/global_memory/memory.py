from __future__ import annotations

import difflib
import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .errors import NotFoundError, ValidationError
from .epistemics import default_epistemic_status, infer_epistemic_status, infer_tier
from .markdown import atomic_write_text, read_document, render_document
from .repository import Repository, now_iso, sha256_bytes


FailureHook = Callable[[str], None]
MEMORY_SCHEMA_VERSION = 2


@dataclass(frozen=True)
class WorkingWriteResult:
    proposal_id: str
    written: list[str]
    updated: list[str]
    exceptions: list[str]
    skipped: list[str]


class ExceptionService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "exceptions"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("exception-*.md")) if self.directory.exists() else []

    def create(
        self, kind: str, title: str, reasons: list[str], *, object_id: str | None = None,
        source_ids: list[str] | None = None, severity: str = "attention",
        context: dict[str, Any] | None = None,
    ) -> str:
        stable = json.dumps(
            [kind, object_id, sorted(reasons), sorted(source_ids or []), context or {}],
            ensure_ascii=False, sort_keys=True,
        )
        exception_id = "exception_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24]
        path = self.directory / f"exception-{exception_id}.md"
        if path.exists():
            return exception_id
        timestamp = now_iso()
        metadata = {
            "id": exception_id, "type": "exception", "status": "open", "title": title,
            "created_at": timestamp, "updated_at": timestamp, "aliases": [], "tags": [kind],
            "domains": [], "confidence": "unknown", "source_ids": source_ids or [], "relations": [],
            "exception_kind": kind, "severity": severity, "object_id": object_id,
            "reasons": reasons, "context": context or {}, "resolution": None,
        }
        body = "# " + title + "\n\n" + "\n".join(f"- {reason}" for reason in reasons) + "\n"
        atomic_write_text(path, render_document(metadata, body))
        return exception_id

    def list(self, statuses: set[str] | None = None) -> list[dict[str, Any]]:
        items = []
        for path in self.documents():
            metadata, _ = read_document(path)
            if statuses and metadata.get("status") not in statuses:
                continue
            items.append({**metadata, "path": self.repository.rel(path)})
        return items

    def resolve(self, exception_id: str, resolution: str, action: str = "resolved") -> dict[str, Any]:
        if action not in {"resolved", "deferred", "dismissed"} or not resolution.strip():
            raise ValidationError("exception resolution requires resolved/deferred/dismissed and a reason")
        path, metadata, body = self.repository.find_document(exception_id)
        if metadata.get("type") != "exception":
            raise ValidationError("not an exception")
        metadata["status"] = action
        metadata["resolution"] = resolution.strip()
        metadata["resolved_at"] = now_iso()
        metadata["updated_at"] = metadata["resolved_at"]
        atomic_write_text(path, render_document(metadata, body))
        self.repository.append_event("memory-events", {"event": "exception-resolved", "exception_id": exception_id, "status": action})
        return {"exception_id": exception_id, "status": action}


class WorkingMemoryService:
    """Materialize validated candidates as usable working memory without touching canonical."""

    def __init__(self, repository: Repository, failure_hook: FailureHook | None = None):
        self.repository = repository
        self.failure_hook = failure_hook
        self.exceptions = ExceptionService(repository)

    def _path(self, object_type: str, object_id: str) -> Path:
        return self.repository.root / "vault" / "memory" / object_type / f"{object_id}.md"

    def _working_text(
        self, candidate: dict[str, Any], body: str, *, proposal: dict[str, Any],
        item_id: str, candidate_path: Path, existing: tuple[Path, dict[str, Any], str] | None,
    ) -> str:
        timestamp = now_iso()
        metadata = dict(candidate)
        metadata.pop("proposed_status", None)
        metadata.update({
            "status": "working", "memory_tier": "working", "updated_at": timestamp,
            "epistemic_status": metadata.get("epistemic_status") or default_epistemic_status(str(metadata.get("type"))),
            "created_by": metadata.get("created_by") or str(proposal.get("processor", "bundle-compiler")),
            "updated_by": "working-ingestion-v1", "model_provider": proposal.get("provider"),
            "model_version": proposal.get("model"), "compiler_version": proposal.get("processor", "unknown"),
            "consolidation_count": int(metadata.get("consolidation_count", 0)),
            "last_consolidated_at": metadata.get("last_consolidated_at"),
            "last_verified_at": metadata.get("last_verified_at"), "trust_score": 0,
            "trust_reasons": [], "promotion_history": list(metadata.get("promotion_history", [])),
            "user_authored": bool(metadata.get("user_authored", False)),
            "user_locked": bool(metadata.get("user_locked", False)),
            "origin_proposal_id": proposal["id"], "origin_item_id": item_id,
            "origin_candidate_path": self.repository.rel(candidate_path),
            "origin_candidate_sha256": sha256_bytes(candidate_path.read_bytes()),
            "memory_schema_version": MEMORY_SCHEMA_VERSION,
        })
        for relation in metadata.get("relations", []):
            if relation.get("status") == "proposal":
                relation["status"] = "working"
        if existing:
            _, old, old_body = existing
            if old.get("user_locked"):
                raise ValidationError(f"working object is user locked: {old['id']}")
            metadata["created_at"] = old["created_at"]
            metadata["promotion_history"] = list(old.get("promotion_history", []))
            metadata["consolidation_count"] = int(old.get("consolidation_count", 0))
            metadata["last_consolidated_at"] = old.get("last_consolidated_at")
            metadata["last_consolidation_id"] = old.get("last_consolidation_id")
            metadata["epistemic_status"] = infer_epistemic_status(old, infer_tier(old))
            old_sources = [str(item) for item in old.get("source_ids", [])]
            metadata["source_ids"] = list(dict.fromkeys([*old_sources, *metadata.get("source_ids", [])]))
            change = {
                "change_type": metadata.get("change_type", "needs_review"),
                "previous_statement": old_body.strip(), "new_statement": body.strip(),
                "changed_fields": ["source_ids", "body"],
                "reason": "incremental compiler update", "trigger_source": (metadata.get("source_ids") or [None])[-1],
                "evidence_added": [],
            }
            metadata["change_history"] = [*old.get("change_history", []), change]
            body = old_body.rstrip() + "\n\n## Change record\n\n" + json.dumps(change, ensure_ascii=False, indent=2) + "\n"
        return render_document(metadata, body)

    def ingest_bundle(
        self, proposal_id: str, item_ids: list[str] | None = None, *,
        update_proposal: bool = True, rebuild_index: bool = True,
    ) -> WorkingWriteResult:
        proposal_path, proposal, proposal_body = self.repository.find_document(proposal_id)
        items = proposal.get("bundle_items")
        if not isinstance(items, list):
            candidate_value = proposal.get("candidate_path")
            if not candidate_value:
                exception_id = self.exceptions.create(
                    "non-working-proposal", f"Proposal requires explicit handling: {proposal_id}",
                    ["proposal has no materializable candidate"], source_ids=list(proposal.get("source_ids", [])),
                    context={"proposal_id": proposal_id},
                )
                return WorkingWriteResult(proposal_id, [], [], [exception_id], [])
            items = [{
                "item_id": "candidate", "candidate_path": candidate_value,
                "decision": "pending", "object_type": proposal.get("target_type"),
            }]
        selected_ids = set(item_ids or [str(item.get("item_id")) for item in items])
        writes: list[tuple[Path, str, bool, str]] = []
        exceptions: list[str] = []
        skipped: list[str] = []
        touched_items: list[dict[str, Any]] = []
        evolved_paths: list[str] = []
        for item in items:
            item_id = str(item.get("item_id"))
            if item_id not in selected_ids or item.get("decision") in {"approved", "rejected", "superseded", "working"}:
                continue
            candidate_value = item.get("candidate_path")
            if not candidate_value:
                skipped.append(item_id)
                continue
            candidate_path = self.repository.resolve_inside(str(candidate_value))
            candidate, body = read_document(candidate_path)
            reasons = []
            if candidate.get("type") == "claim":
                if candidate.get("atomicity_status") == "compound":
                    reasons.append("compound claim requires split")
                if not candidate.get("evidence"):
                    reasons.append("claim has no evidence")
            if reasons:
                exceptions.append(self.exceptions.create(
                    "working-ingestion", f"Cannot auto-ingest {candidate.get('title', candidate.get('id'))}", reasons,
                    object_id=str(candidate.get("id")), source_ids=list(candidate.get("source_ids", [])),
                    context={"proposal_id": proposal_id, "item_id": item_id},
                ))
                item["decision"] = "exception"
                item["exception_reasons"] = reasons
                touched_items.append(item)
                continue
            object_id = str(candidate["id"])
            target = self._path(str(candidate["type"]), object_id)
            existing = None
            if target.exists():
                old, old_body = read_document(target)
                if old.get("origin_candidate_sha256") == sha256_bytes(candidate_path.read_bytes()):
                    skipped.append(item_id)
                    item["decision"] = "working"
                    touched_items.append(item)
                    continue
                existing = (target, old, old_body)
                classification = str(candidate.get("change_type") or item.get("change_type") or "needs_review")
                if classification not in {"support", "refine", "limit", "contradict", "supersede", "metadata_only"}:
                    exceptions.append(self.exceptions.create(
                        "unclassified-change", f"Incremental change needs classification: {candidate.get('title')}",
                        ["provider must classify update as support/refine/limit/contradict/supersede/metadata_only"],
                        object_id=object_id, source_ids=list(candidate.get("source_ids", [])),
                        context={"proposal_id": proposal_id, "item_id": item_id, "classification": classification},
                    ))
                    item["decision"] = "exception"
                    item["exception_reasons"] = ["unclassified incremental change"]
                    touched_items.append(item)
                    continue
                if infer_tier(old, target) == "trusted":
                    from .evolution import KnowledgeEvolutionService
                    change_type = classification
                    evolution = KnowledgeEvolutionService(self.repository).apply(
                        object_id, candidate, body, change_type=change_type,
                        reason=str(candidate.get("change_reason") or "incremental material changed trusted memory"),
                        trigger_source=(list(candidate.get("source_ids", [])) or [None])[-1],
                    )
                    evolved_paths.append(str(evolution.get("revision_path") or self.repository.rel(target)))
                    item["decision"] = "working"
                    item["working_path"] = evolved_paths[-1]
                    item["evolution_action"] = evolution["action"]
                    item["working_at"] = now_iso()
                    touched_items.append(item)
                    continue
            elif item.get("action") == "update":
                try:
                    found = self.repository.find_document(object_id)
                    if self.repository.rel(found[0]).startswith(("vault/knowledge/", "vault/frontier/", "vault/action/")):
                        exceptions.append(self.exceptions.create(
                            "canonical-change", f"Working update would change canonical: {candidate.get('title')}",
                            ["canonical changes require promotion review"], object_id=object_id,
                            source_ids=list(candidate.get("source_ids", [])), context={"proposal_id": proposal_id, "item_id": item_id},
                            severity="must_confirm",
                        ))
                        item["decision"] = "exception"
                        touched_items.append(item)
                        continue
                except NotFoundError:
                    pass
            text = self._working_text(candidate, body, proposal=proposal, item_id=item_id, candidate_path=candidate_path, existing=existing)
            self.repository._validate_metadata(read_document_text(text), target)
            writes.append((target, text, existing is not None, item_id))
            item["decision"] = "working"
            item["working_path"] = self.repository.rel(target)
            item["working_at"] = now_iso()
            touched_items.append(item)

        backups: list[tuple[Path, bytes | None]] = []
        proposal_before = proposal_path.read_bytes()
        try:
            for target, text, _, _ in writes:
                backups.append((target, target.read_bytes() if target.exists() else None))
                atomic_write_text(target, text)
            if self.failure_hook:
                self.failure_hook("working_written")
            if update_proposal and touched_items:
                pending = [item for item in items if item.get("decision") in {"pending", "deferred"}]
                proposal["status"] = "pending" if pending else "migrated"
                proposal["migration_mode"] = "working-ingestion-v1"
                proposal["updated_at"] = now_iso()
                atomic_write_text(proposal_path, render_document(proposal, proposal_body))
            if self.failure_hook:
                self.failure_hook("proposal_written")
            if rebuild_index:
                self.repository.rebuild_index()
        except Exception:
            for path, before in reversed(backups):
                if before is None:
                    path.unlink(missing_ok=True)
                else:
                    path.write_bytes(before)
            proposal_path.write_bytes(proposal_before)
            if rebuild_index:
                self.repository.rebuild_index()
            raise
        for target, _, updated, item_id in writes:
            self.repository.append_event("memory-events", {
                "event": "working-updated" if updated else "working-created", "object_path": self.repository.rel(target),
                "proposal_id": proposal_id, "item_id": item_id,
            })
        return WorkingWriteResult(
            proposal_id, [self.repository.rel(path) for path, _, updated, _ in writes if not updated],
            [*[self.repository.rel(path) for path, _, updated, _ in writes if updated], *evolved_paths], exceptions, skipped,
        )


def read_document_text(text: str) -> dict[str, Any]:
    from .markdown import parse_document_text
    return parse_document_text(text)[0]
