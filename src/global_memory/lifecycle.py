from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .extraction import ExtractionService
from .markdown import atomic_write_text, read_document, render_document
from .quality import SourceQualityService
from .repository import Repository, now_iso


PROCESSING_STATES = {
    "captured", "extracted", "quality_checked", "compile_pending", "compiled",
    "awaiting_review", "partially_approved", "completed", "failed", "deferred",
    "superseded",
}


@dataclass(frozen=True)
class SourceState:
    source_id: str
    state: str
    extraction_status: str | None
    availability_status: str
    content_quality: str
    proposal_count: int
    pending_count: int
    terminal_count: int
    reasons: list[str]

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__


class SourceLifecycleService:
    """Derive processing state from truth objects; never mutates capture facts."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self._sources: dict[str, tuple[Path, dict[str, Any]]] | None = None
        self._latest_extractions: dict[str, dict[str, Any]] | None = None
        self._processing_proposals: dict[str, list[dict[str, Any]]] | None = None
        self._reflected_sources: set[str] | None = None
        self._pending_refresh_sources: set[str] | None = None
        self._approved_refresh_predecessors: set[str] | None = None

    def _build_source_index(self) -> None:
        if self._sources is not None:
            return
        sources: dict[str, tuple[Path, dict[str, Any]]] = {}
        for path in self.repository.source_documents():
            metadata, _ = read_document(path)
            sources[str(metadata["id"])] = (path, metadata)
        self._sources = sources

    def _build_extraction_index(self) -> None:
        if self._latest_extractions is not None:
            return
        self._build_source_index()
        assert self._sources is not None
        latest: dict[str, dict[str, Any]] = {}
        extraction_service = ExtractionService(self.repository)
        for path in extraction_service.documents():
            metadata, _ = read_document(path)
            source_id = str(metadata.get("source_id") or "")
            source = self._sources.get(source_id)
            if not source or metadata.get("input_sha256") != source[1].get("content_sha256"):
                continue
            current = latest.get(source_id)
            if current is None or str(metadata.get("extracted_at", "")) > str(current.get("extracted_at", "")):
                latest[source_id] = metadata
        self._latest_extractions = latest

    def _build_proposal_index(self) -> None:
        if self._processing_proposals is not None:
            return
        processing: dict[str, list[dict[str, Any]]] = {}
        pending_refresh_sources: set[str] = set()
        approved_refresh_predecessors: set[str] = set()
        processing_kinds = {
            "knowledge_compile", "knowledge_update", "knowledge_revision", "model_candidate",
            "compile_bundle", "source_bundle", "corpus_distillation", "deterministic_synthesis",
        }
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            proposal_kind = metadata.get("proposal_kind", "knowledge_compile")
            if proposal_kind == "source_refresh":
                status = str(metadata.get("status"))
                if status in {"pending", "deferred"}:
                    pending_refresh_sources.update(filter(None, (
                        str(metadata.get("new_source_id") or ""),
                        str(metadata.get("previous_source_id") or ""),
                    )))
                elif status == "approved" and metadata.get("previous_source_id"):
                    approved_refresh_predecessors.add(str(metadata["previous_source_id"]))
                continue
            if proposal_kind not in processing_kinds:
                continue
            for source_id in metadata.get("source_ids", []):
                item = metadata
                if source_id in metadata.get("source_only_source_ids", []):
                    item = {**metadata, "status": "source_only"}
                processing.setdefault(str(source_id), []).append(item)
        self._processing_proposals = processing
        self._pending_refresh_sources = pending_refresh_sources
        self._approved_refresh_predecessors = approved_refresh_predecessors

    def _build_reflection_index(self) -> None:
        """Index Sources that Daily Dream has already cognitively processed."""
        if self._reflected_sources is not None:
            return
        reflected: set[str] = set()
        for path in self.repository.reflection_documents():
            metadata, _ = read_document(path)
            if metadata.get("status") in {"archived", "superseded"}:
                continue
            reflected.update(str(source_id) for source_id in metadata.get("source_ids", []) if source_id)
        self._reflected_sources = reflected

    def _proposals(self, source_id: str) -> list[dict[str, Any]]:
        self._build_proposal_index()
        assert self._processing_proposals is not None
        return list(self._processing_proposals.get(source_id, []))

    def _refresh_state(self, source_id: str) -> tuple[bool, bool]:
        """Return (has_pending_refresh, has_approved_successor)."""
        self._build_proposal_index()
        assert self._pending_refresh_sources is not None
        assert self._approved_refresh_predecessors is not None
        return (
            source_id in self._pending_refresh_sources,
            source_id in self._approved_refresh_predecessors,
        )

    def status(self, source_id: str, *, assess: bool = False) -> SourceState:
        self._build_source_index()
        assert self._sources is not None
        source = self._sources.get(source_id)
        if source is None:
            # Preserve the public lookup error and behavior for an invalid id.
            self.repository.find_document(source_id)
        pending_refresh, approved_successor = self._refresh_state(source_id)
        self._build_extraction_index()
        assert self._latest_extractions is not None
        extraction = self._latest_extractions.get(source_id)
        extraction_status = str(extraction.get("status")) if extraction else None
        quality_service = SourceQualityService(self.repository)
        quality = quality_service.assess(source_id, persist=True) if assess else quality_service.load(source_id)
        availability = quality.availability_status if quality else "unknown"
        content_quality = quality.content_quality if quality else "unknown"
        proposals = self._proposals(source_id)
        active = [p for p in proposals if p.get("status") in {"pending", "deferred"}]
        terminal = [p for p in proposals if p.get("status") in {"approved", "published", "migrated", "rejected", "superseded", "source_only"}]
        self._build_reflection_index()
        assert self._reflected_sources is not None
        reflected = source_id in self._reflected_sources
        reasons: list[str] = []
        if approved_successor:
            state = "superseded"
            reasons.append("an approved immutable source version supersedes this capture")
        elif pending_refresh:
            state = "awaiting_review"
            reasons.append("source refresh version awaits review")
        elif quality and not quality.compile_allowed:
            state = "failed"
            reasons.extend(quality.reasons)
        elif active:
            bundle_items = [item for p in active for item in p.get("bundle_items", [])]
            decisions = {item.get("decision") for item in bundle_items}
            if decisions & {"approved", "rejected"} and "pending" in decisions:
                state = "partially_approved"
            elif all(p.get("status") == "deferred" for p in active):
                state = "deferred"
            else:
                state = "awaiting_review"
        elif proposals and terminal:
            state = "completed"
        elif reflected:
            state = "completed"
            reasons.append("a source-linked Reflection records completed Daily Dream processing")
        elif quality:
            state = "compile_pending" if quality.compile_allowed else "failed"
        elif extraction_status == "ready":
            state = "extracted"
        elif extraction_status == "error":
            state = "failed"
        else:
            state = "captured"
        return SourceState(
            source_id=source_id, state=state, extraction_status=extraction_status,
            availability_status=availability, content_quality=content_quality,
            proposal_count=len(proposals), pending_count=len(active), terminal_count=len(terminal) + int(reflected),
            reasons=reasons,
        )

    def all(self) -> list[dict[str, Any]]:
        result = []
        self._build_source_index()
        assert self._sources is not None
        for path, metadata in sorted(self._sources.values(), key=lambda item: item[0]):
            state = self.status(str(metadata["id"]), assess=False)
            result.append({**state.as_dict(), "title": metadata.get("title"), "source_kind": metadata.get("source_kind")})
        return result

    def history(self, source_id: str) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []
        for name in ("capture-events.jsonl", "source-processing-events.jsonl", "proposal-events.jsonl"):
            path = self.repository.root / "system/logs" / name
            if not path.exists():
                continue
            for line in path.read_text(encoding="utf-8").splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("source_id") == source_id or event.get("input_source_id") == source_id:
                    events.append(event)
        return sorted(events, key=lambda item: str(item.get("at", "")))

    def check(self) -> dict[str, Any]:
        issues = []
        states = self.all()
        for item in states:
            if item["proposal_count"] and item["state"] in {"captured", "extracted", "compile_pending"}:
                issues.append(f"{item['source_id']} has proposal but state={item['state']}")
        return {"ok": not issues, "sources": len(states), "states": states, "issues": issues}


class SourceAnnotationService:
    """Mutable user-attention annotation kept separate from immutable capture facts."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault/annotations"

    def annotate(self, source_id: str, *, why_saved: str | None = None, salience: str | None = None) -> str:
        self.repository.find_document(source_id)
        path = self.directory / f"source-{source_id}.md"
        if path.exists():
            metadata, body = read_document(path)
        else:
            timestamp = now_iso()
            metadata = {
                "id": f"annotation_{source_id}", "type": "source_annotation", "status": "active",
                "title": f"Source annotation: {source_id}", "created_at": timestamp,
                "updated_at": timestamp, "source_id": source_id,
                "why_saved_by_user": "unknown", "personal_salience": "unknown",
                "possible_relevance_inferred_by_agent": None,
            }
            body = f"# Source annotation\n\n- Source: `{source_id}`\n"
        if why_saved is not None:
            metadata["why_saved_by_user"] = why_saved or "unknown"
        if salience is not None:
            metadata["personal_salience"] = salience
        metadata["updated_at"] = now_iso()
        atomic_write_text(path, render_document(metadata, body))
        self.repository.append_event("source-processing-events", {
            "event": "source-annotated", "source_id": source_id,
            "why_saved_updated": why_saved is not None, "salience": salience,
        })
        return self.repository.rel(path)
