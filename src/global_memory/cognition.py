from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .bundle import BundleCompiler, CompilerProvider
from .capture import CaptureService
from .errors import NotFoundError, ValidationError
from .extraction import ExtractionService
from .markdown import read_document, render_document
from .memory import WorkingMemoryService
from .proposals import CANONICAL_DIRECTORIES
from .repository import Repository, now_iso


INPUT_TYPES = {
    "article", "paper", "github", "conversation", "idea", "experiment", "meeting",
}
REFLECTION_KINDS = {"article", "conversation", "idea", "experiment", "project"}
REFLECTION_AUTHORS = {"agent", "user"}
CONFIDENCE_LEVELS = {"unknown", "low", "medium", "high"}
DAILY_OBJECT_TYPES = {"concept", "claim", "question", "tension", "work"}
WEEKLY_OBJECT_TYPES = set(CANONICAL_DIRECTORIES) - {"synthesis"}
KNOWLEDGE_CHANGE_TYPES = {
    "support", "refine", "limit", "contradict", "supersede", "metadata_only",
}
GENERIC_REFLECTION = re.compile(
    r"^(?:这篇|本文|该文|文章|论文|项目).{0,24}(?:介绍|讨论|讲述|概述|总结)(?:了|的是)?",
    re.I,
)


def _list_of_text(value: Any, field: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValidationError(f"{field} must be a list of non-empty strings")
    return [item.strip() for item in value]


def validate_connections(value: Any) -> list[dict[str, str]]:
    if value is None or value == "":
        return []
    if not isinstance(value, list):
        raise ValidationError("connections must be a list")
    normalized: list[dict[str, str]] = []
    for connection in value:
        if not isinstance(connection, dict):
            raise ValidationError("each connection must explain shared_mechanism, boundary, and difference")
        item = {
            key: str(connection.get(key, "")).strip()
            for key in ("shared_mechanism", "boundary", "difference")
        }
        if not all(item.values()):
            raise ValidationError("connection requires shared_mechanism, boundary, and difference")
        normalized.append(item)
    return normalized


def validate_reflection_payload(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValidationError("reflection payload must be an object")
    why = str(payload.get("why_important", "")).strip()
    if not why or GENERIC_REFLECTION.search(why):
        raise ValidationError("reflection why_important must explain cognitive value, not summarize the input")
    what_changed = str(payload.get("what_changed", payload.get("changed_belief", ""))).strip()
    surprising = str(payload.get("surprising", "")).strip()
    connections = validate_connections(payload.get("connections", []))
    open_questions = _list_of_text(payload.get("open_questions", []), "open_questions")
    if not any((what_changed, surprising, connections, open_questions)):
        raise ValidationError(
            "reflection requires at least one changed belief, surprising point, qualified connection, or open question"
        )
    confidence = str(payload.get("confidence", "unknown")).strip().lower()
    if confidence not in CONFIDENCE_LEVELS:
        raise ValidationError(f"invalid reflection confidence: {confidence}")
    return {
        "importance": str(payload.get("importance", "medium")).strip() or "medium",
        "why_important": why,
        "what_changed": what_changed,
        "surprising": surprising,
        "connections": connections,
        "conflicts": _list_of_text(payload.get("conflicts", []), "conflicts"),
        "open_questions": open_questions,
        "possible_mechanisms": _list_of_text(payload.get("possible_mechanisms", []), "possible_mechanisms"),
        "future_directions": _list_of_text(payload.get("future_directions", []), "future_directions"),
        "confidence": confidence,
    }


def validate_hypothesis(payload: dict[str, Any], reflection_ids: set[str], source_ids: set[str]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValidationError("candidate hypothesis must be an object")
    required_text = ("statement", "falsifier", "possible_experiment")
    normalized = {key: str(payload.get(key, "")).strip() for key in required_text}
    if not all(normalized.values()):
        raise ValidationError("hypothesis requires statement, falsifier, and possible_experiment")
    supporting_patterns = _list_of_text(payload.get("supporting_patterns", []), "supporting_patterns")
    counter_arguments = _list_of_text(payload.get("counter_arguments", []), "counter_arguments")
    supporting_reflections = _list_of_text(payload.get("supporting_reflections", []), "supporting_reflections")
    supporting_sources = _list_of_text(payload.get("supporting_sources", []), "supporting_sources")
    if not supporting_patterns or not counter_arguments or not supporting_reflections or not supporting_sources:
        raise ValidationError(
            "hypothesis requires supporting_patterns, counter_arguments, supporting_reflections, and supporting_sources"
        )
    if not set(supporting_reflections) <= reflection_ids:
        raise ValidationError("hypothesis references a reflection outside this synthesis")
    if not set(supporting_sources) <= source_ids:
        raise ValidationError("hypothesis references a source outside this synthesis")
    return {
        **normalized,
        "supporting_patterns": supporting_patterns,
        "counter_arguments": counter_arguments,
        "supporting_reflections": supporting_reflections,
        "supporting_sources": supporting_sources,
        "epistemic_status": "hypothetical",
    }


def validate_semantic_items(
    value: Any, *, allowed_types: set[str], label: str, maximum: int | None = None,
) -> list[dict[str, Any]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValidationError(f"{label} semantic_items must be a list")
    if maximum is not None and len(value) > maximum:
        raise ValidationError(f"{label} allows at most {maximum} semantic items per input")
    normalized: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            raise ValidationError(f"{label} semantic item must be an object")
        object_type = str(item.get("object_type", "")).strip()
        if object_type not in allowed_types:
            raise ValidationError(f"{label} does not allow object_type: {object_type or '<missing>'}")
        if not str(item.get("title", "")).strip() or not str(item.get("body", "")).strip():
            raise ValidationError(f"{label} semantic item requires title and body")
        metadata = item.get("metadata") or {}
        if not isinstance(metadata, dict):
            raise ValidationError(f"{label} semantic item metadata must be an object")
        normalized.append({**item, "metadata": dict(metadata)})
    return normalized


def validate_knowledge_update(
    payload: dict[str, Any], *, repository: Repository, input_concepts: set[str],
    reflection_ids: set[str], source_ids: set[str],
) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValidationError("knowledge update must be an object")
    required = ("target_id", "previous", "proposed", "reason", "change_type")
    normalized = {key: str(payload.get(key, "")).strip() for key in required}
    if not all(normalized.values()):
        raise ValidationError(
            "knowledge update requires target_id, previous, proposed, reason, and change_type"
        )
    if normalized["change_type"] not in KNOWLEDGE_CHANGE_TYPES:
        raise ValidationError(f"invalid knowledge update change_type: {normalized['change_type']}")
    if normalized["target_id"] not in input_concepts:
        raise ValidationError("knowledge update target_id must be listed in input_concepts")
    _, target, _ = repository.find_document(normalized["target_id"])
    if target.get("type") != "concept":
        raise ValidationError("knowledge update target must be an existing concept")
    supporting_reflections = _list_of_text(
        payload.get("supporting_reflections", []), "supporting_reflections",
    )
    supporting_sources = _list_of_text(
        payload.get("supporting_sources", []), "supporting_sources",
    )
    if not supporting_reflections or not set(supporting_reflections) <= reflection_ids:
        raise ValidationError("knowledge update requires supporting reflections from this synthesis")
    if not supporting_sources or not set(supporting_sources) <= source_ids:
        raise ValidationError("knowledge update requires supporting sources from this synthesis")
    return {
        **normalized,
        "supporting_reflections": supporting_reflections,
        "supporting_sources": supporting_sources,
    }


@dataclass(frozen=True)
class CognitiveWrite:
    object_id: str
    path: str
    created: bool


class InputEpisodeService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "inputs"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("input-*.md")) if self.directory.exists() else []

    @staticmethod
    def infer_input_type(source: dict[str, Any]) -> str:
        locator = str(source.get("canonical_locator", "")).casefold()
        title = str(source.get("title", "")).casefold()
        if "github.com" in locator:
            return "github"
        if "arxiv.org" in locator or locator.endswith(".pdf") or "paper" in title:
            return "paper"
        return "article"

    def create_from_source(
        self, source_id: str, *, input_type: str | None = None, title: str | None = None,
        participants: list[str] | None = None, topic: str | None = None,
        user_authored: bool = False, submitted_by: str = "capture",
        episode_kind: str | None = None, session: dict[str, Any] | None = None,
    ) -> CognitiveWrite:
        _, source, source_body = self.repository.find_document(source_id)
        if source.get("type") != "source":
            raise ValidationError(f"Input Episode source is not a source: {source_id}")
        resolved_type = input_type or self.infer_input_type(source)
        if resolved_type not in INPUT_TYPES:
            raise ValidationError(f"invalid input_type: {resolved_type}")
        stable = json.dumps([source_id, resolved_type, episode_kind or ""], ensure_ascii=False)
        input_id = "input_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24]
        path = self.directory / f"input-{input_id}.md"
        if path.exists():
            existing, _ = read_document(path)
            if existing.get("id") != input_id or existing.get("source_id") != source_id:
                raise ValidationError(f"Input Episode identity collision: {input_id}")
            return CognitiveWrite(input_id, self.repository.rel(path), False)
        timestamp = now_iso()
        metadata = {
            "id": input_id, "type": "input", "status": "active",
            "title": title or str(source.get("title") or f"Input from {source_id}"),
            "created_at": timestamp, "updated_at": timestamp,
            "aliases": [], "tags": ["input", resolved_type], "domains": [],
            "confidence": "unknown", "source_ids": [source_id], "relations": [],
            "input_type": resolved_type, "source_id": source_id,
            "participants": participants or [], "topic": topic,
            "user_authored": bool(user_authored), "submitted_by": submitted_by,
            "episode_kind": episode_kind, "session": session or {},
            "truth_layer": "input_episode", "execution_safe": False,
        }
        body = (
            f"# {metadata['title']}\n\n"
            f"Input Episode for `{source_id}`. The immutable Source remains authoritative.\n\n"
            f"{source_body.strip()}\n"
        )
        self.repository._validate_metadata(metadata, path)
        created = self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        if created:
            self.repository.append_event("cognitive-events", {
                "event": "input-created", "input_id": input_id, "source_id": source_id,
                "input_type": resolved_type,
            })
        return CognitiveWrite(input_id, self.repository.rel(path), created)

    def backfill(
        self, *, limit: int = 25, source_ids: list[str] | None = None,
    ) -> dict[str, Any]:
        if limit < 1 or limit > 100:
            raise ValidationError("Input backfill limit must be between 1 and 100")
        existing_sources: set[str] = set()
        for path in self.documents():
            metadata, _ = read_document(path)
            existing_sources.add(str(metadata.get("source_id")))
        candidates: list[tuple[str, str]] = []
        if source_ids:
            for source_id in dict.fromkeys(source_ids):
                _, source, _ = self.repository.find_document(source_id)
                if source.get("type") != "source":
                    raise ValidationError(f"Input backfill target is not a source: {source_id}")
                candidates.append((str(source.get("captured_at") or source.get("created_at") or ""), source_id))
        else:
            for path in self.repository.source_documents():
                source, _ = read_document(path)
                source_id = str(source.get("id"))
                if source_id in existing_sources or source.get("source_kind") == "personal-notes":
                    continue
                candidates.append((str(source.get("captured_at") or source.get("created_at") or ""), source_id))
            candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
        created: list[dict[str, Any]] = []
        reused: list[str] = []
        for _, source_id in candidates[:limit]:
            write = self.create_from_source(source_id, submitted_by="bounded-backfill")
            if write.created:
                created.append(write.__dict__)
            else:
                reused.append(source_id)
        self.repository.rebuild_index()
        return {
            "backfill": "completed", "selected": min(limit, len(candidates)),
            "created": created, "created_count": len(created),
            "reused_source_ids": reused,
            "remaining": max(0, len(candidates) - min(limit, len(candidates))),
            "knowledge_writes": 0, "canonical_writes": 0,
        }

    def capture_idea(self, text: str, *, title: str = "User idea") -> dict[str, Any]:
        if not text.strip():
            raise ValidationError("idea text cannot be empty")
        captured = CaptureService(self.repository).capture_text(text, "idea capture", title)
        episode = self.create_from_source(
            captured.source_id, input_type="idea", title=title,
            user_authored=True, submitted_by="user",
        )
        self.repository.rebuild_index()
        return {"source": captured.__dict__, "input": episode.__dict__, "reflection_queued": True}

    def import_conversation(
        self, path: Path | str, *, participants: list[str] | None = None,
        topic: str | None = None,
    ) -> dict[str, Any]:
        captured = CaptureService(self.repository).capture(str(Path(path).expanduser().resolve()), "conversation import")
        episode = self.create_from_source(
            captured.source_id, input_type="conversation", participants=participants,
            topic=topic, user_authored=True, submitted_by="user",
        )
        self.repository.rebuild_index()
        return {"source": captured.__dict__, "input": episode.__dict__, "reflection_queued": True}

    def import_agent_session(self, path: Path | str, *, agent: str) -> dict[str, Any]:
        source_path = Path(path).expanduser().resolve()
        text = source_path.read_text(encoding="utf-8")
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = {}
            for key in ("goal", "result", "lesson"):
                match = re.search(rf"(?im)^#{{0,3}}\s*{key}\s*:\s*(.+)$", text)
                if match:
                    data[key] = match.group(1).strip()
        if not all(str(data.get(key, "")).strip() for key in ("goal", "result", "lesson")):
            raise ValidationError("agent session requires explicit goal, result, and lesson")
        captured = CaptureService(self.repository).capture(str(source_path), f"agent session from {agent}")
        episode = self.create_from_source(
            captured.source_id, input_type="experiment", title=f"{agent} session: {data['goal']}",
            participants=[agent], user_authored=False, submitted_by=agent,
            episode_kind="agent_session", session={key: data[key] for key in ("goal", "result", "lesson")},
        )
        self.repository.rebuild_index()
        return {
            "source": captured.__dict__, "input": episode.__dict__,
            "reflection_queued": True, "knowledge_writes": 0,
        }


class ReflectionService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "reflections"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("reflection-*.md")) if self.directory.exists() else []

    def queue(self, *, limit: int = 5, max_chars: int = 6_000) -> dict[str, Any]:
        if limit < 1 or max_chars < 256:
            raise ValidationError("reflection queue requires limit >= 1 and max_chars >= 256")
        reflected = set()
        for path in self.documents():
            metadata, _ = read_document(path)
            reflected.update(str(item) for item in metadata.get("target_ids", []))
        pending: list[dict[str, Any]] = []
        for path in InputEpisodeService(self.repository).documents():
            metadata, body = read_document(path)
            if str(metadata["id"]) in reflected:
                continue
            source_id = str(metadata.get("source_id"))
            excerpt = body
            excerpt_source = "input_episode"
            extraction_id = None
            extraction_path = None
            try:
                resolved_path, extraction, extraction_body = ExtractionService(
                    self.repository
                ).latest_for_source(source_id, create=False)
                excerpt = extraction_body
                excerpt_source = "extraction"
                extraction_id = extraction.get("extraction_id")
                extraction_path = self.repository.rel(resolved_path)
            except NotFoundError:
                pass
            pending.append({
                "input_id": metadata["id"], "input_type": metadata["input_type"],
                "title": metadata["title"], "source_ids": metadata.get("source_ids", []),
                "user_authored": metadata.get("user_authored", False),
                "excerpt": excerpt[:max_chars], "excerpt_source": excerpt_source,
                "extraction_id": extraction_id, "extraction_path": extraction_path,
                "path": self.repository.rel(path),
            })
        return {
            "pending_count": len(pending), "selected_count": min(limit, len(pending)),
            "omitted_count": max(0, len(pending) - limit), "items": pending[:limit],
        }

    def prepare(self, input_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        _, episode, _ = self.repository.find_document(input_id)
        if episode.get("type") != "input":
            raise ValidationError(f"reflection target is not an Input Episode: {input_id}")
        normalized = validate_reflection_payload(payload)
        created_by = str(payload.get("created_by", "agent")).strip().lower()
        if created_by not in REFLECTION_AUTHORS:
            raise ValidationError(f"invalid reflection author: {created_by}")
        kind = str(payload.get("reflection_kind") or episode.get("input_type") or "article")
        if kind == "paper":
            kind = "article"
        if kind == "github":
            kind = "project"
        if kind == "meeting":
            kind = "conversation"
        if kind not in REFLECTION_KINDS:
            raise ValidationError(f"invalid reflection_kind: {kind}")
        source_ids = [str(item) for item in episode.get("source_ids", [])]
        title = str(payload.get("title") or f"Reflection: {episode['title']}")
        domains = _list_of_text(payload.get("domains", []), "domains")
        stable = json.dumps(
            [input_id, created_by, kind, title, domains, normalized],
            ensure_ascii=False, sort_keys=True,
        )
        reflection_id = "reflection_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24]
        path = self.directory / f"reflection-{reflection_id}.md"
        return {
            "episode": episode, "normalized": normalized, "created_by": created_by,
            "kind": kind, "source_ids": source_ids, "title": title,
            "domains": domains, "reflection_id": reflection_id, "path": path,
        }

    def create(self, input_id: str, payload: dict[str, Any], *, rebuild_index: bool = True) -> CognitiveWrite:
        prepared = self.prepare(input_id, payload)
        episode = prepared["episode"]
        normalized = prepared["normalized"]
        created_by = prepared["created_by"]
        kind = prepared["kind"]
        source_ids = prepared["source_ids"]
        reflection_id = prepared["reflection_id"]
        path = prepared["path"]
        if path.exists():
            existing, _ = read_document(path)
            if existing.get("id") != reflection_id or existing.get("input_id") != input_id:
                raise ValidationError(f"Reflection identity collision: {reflection_id}")
            return CognitiveWrite(reflection_id, self.repository.rel(path), False)
        timestamp = now_iso()
        metadata = {
            "id": reflection_id, "type": "reflection", "status": "active",
            "title": prepared["title"],
            "created_at": timestamp, "updated_at": timestamp,
            "aliases": [], "tags": ["reflection", kind], "domains": prepared["domains"],
            "confidence": normalized["confidence"], "source_ids": source_ids, "relations": [],
            "target_ids": list(dict.fromkeys([input_id, *source_ids])),
            "input_id": input_id, "created_by": created_by, "reflection_kind": kind,
            **normalized, "truth_layer": "reflection",
            "user_authored": created_by == "user", "execution_safe": False,
        }
        connection_lines = [
            f"- Shared mechanism: {item['shared_mechanism']}\n  Boundary: {item['boundary']}\n  Difference: {item['difference']}"
            for item in normalized["connections"]
        ]
        body = "\n\n".join([
            f"# {metadata['title']}",
            "## Why important\n\n" + normalized["why_important"],
            "## What changed\n\n" + (normalized["what_changed"] or "Not stated."),
            "## Surprising\n\n" + (normalized["surprising"] or "Not stated."),
            "## Connections\n\n" + ("\n".join(connection_lines) or "None recorded."),
            "## Conflicts\n\n" + ("\n".join(f"- {item}" for item in normalized["conflicts"]) or "None recorded."),
            "## Open questions\n\n" + ("\n".join(f"- {item}" for item in normalized["open_questions"]) or "None recorded."),
            "## Possible mechanisms\n\n" + ("\n".join(f"- {item}" for item in normalized["possible_mechanisms"]) or "None recorded."),
            "## Future directions\n\n" + ("\n".join(f"- {item}" for item in normalized["future_directions"]) or "None recorded."),
        ]) + "\n"
        self.repository._validate_metadata(metadata, path)
        created = self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        if created:
            self.repository.append_event("cognitive-events", {
                "event": "reflection-created", "reflection_id": reflection_id,
                "input_id": input_id, "created_by": created_by,
            })
        if rebuild_index:
            self.repository.rebuild_index()
        return CognitiveWrite(reflection_id, self.repository.rel(path), created)


class StaticBundleProvider(CompilerProvider):
    def __init__(self, items: list[dict[str, Any]], name: str):
        self.items = items
        self.name = name

    def compile(
        self, source: dict[str, Any], extraction: dict[str, Any], text: str,
        existing_context: list[dict[str, Any]], schema: dict[str, Any],
    ) -> list[dict[str, Any]]:
        return self.items


def _load_json(path: Path | str) -> dict[str, Any]:
    candidate = Path(path).expanduser().resolve()
    try:
        payload = json.loads(candidate.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f"cannot read cognitive bundle: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError("cognitive bundle must be a JSON object")
    return payload


def _context_from_reflection(reflection_id: str, reflection: dict[str, Any]) -> dict[str, Any]:
    return {
        "reflection_ids": [reflection_id],
        "importance": reflection.get("importance"),
        "changed_belief": reflection.get("what_changed"),
        "surprising": reflection.get("surprising"),
        "connections": reflection.get("connections", []),
        "open_questions": reflection.get("open_questions", []),
    }


class DailyDreamService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self, bundle_file: Path | str, *, limit: int = 5) -> dict[str, Any]:
        payload = _load_json(bundle_file)
        reflections = payload.get("reflections")
        if not isinstance(reflections, list) or not reflections:
            raise ValidationError("daily dream bundle requires reflections")
        if len(reflections) > limit:
            raise ValidationError(f"daily dream bundle exceeds limit {limit}")
        reflection_service = ReflectionService(self.repository)
        selected = {item["input_id"] for item in reflection_service.queue(limit=limit)["items"]}
        plans: list[dict[str, Any]] = []
        for item in reflections:
            if not isinstance(item, dict) or not str(item.get("input_id", "")):
                raise ValidationError("daily dream item requires input_id")
            input_id = str(item["input_id"])
            reflection_payload = item.get("reflection")
            if not isinstance(reflection_payload, dict):
                raise ValidationError("daily dream item requires reflection object")
            prepared = reflection_service.prepare(input_id, reflection_payload)
            resumable = prepared["path"].exists()
            if input_id not in selected and not resumable:
                raise ValidationError("daily dream may only process the current bounded reflection queue")
            semantic_items = validate_semantic_items(
                item.get("semantic_items", []), allowed_types=DAILY_OBJECT_TYPES,
                label="daily dream", maximum=3,
            )
            plans.append({
                "input_id": input_id, "reflection": reflection_payload,
                "prepared": prepared, "semantic_items": semantic_items,
            })
        before_canonical = len(list(self.repository.canonical_documents()))
        reflection_ids: list[str] = []
        reflections_created = 0
        reflections_reused = 0
        written: list[str] = []
        updated: list[str] = []
        source_only = 0
        for plan in plans:
            input_id = plan["input_id"]
            reflection_write = reflection_service.create(
                input_id, plan["reflection"], rebuild_index=False,
            )
            reflection_ids.append(reflection_write.object_id)
            reflections_created += int(reflection_write.created)
            reflections_reused += int(not reflection_write.created)
            _, reflection, _ = self.repository.find_document(reflection_write.object_id)
            semantic_items = plan["semantic_items"]
            if not semantic_items:
                source_only += 1
                continue
            for semantic_item in semantic_items:
                metadata = dict(semantic_item.get("metadata") or {})
                metadata["reflection_context"] = _context_from_reflection(reflection_write.object_id, reflection)
                semantic_item["metadata"] = metadata
            _, episode, _ = self.repository.find_document(input_id)
            source_id = str(episode.get("source_id"))
            provider = StaticBundleProvider(semantic_items, str(payload.get("provider_name") or "agent-semantic-daily-dream-v1"))
            compiled = BundleCompiler(self.repository, provider).compile(source_id)
            if compiled.proposal_id:
                result = WorkingMemoryService(self.repository).ingest_bundle(
                    compiled.proposal_id, rebuild_index=True,
                )
                written.extend(result.written)
                updated.extend(result.updated)
        self.repository.rebuild_index()
        after_canonical = len(list(self.repository.canonical_documents()))
        if after_canonical != before_canonical:
            raise ValidationError("daily dream violated the zero-Canonical-write boundary")
        remaining = ReflectionService(self.repository).queue(limit=limit)
        return {
            "daily_dream": "completed", "inputs_processed": len(reflections),
            "reflections_created": reflections_created,
            "reflections_reused": reflections_reused, "reflection_ids": reflection_ids,
            "concepts_created": sum("/concept/" in path for path in written),
            "concepts_updated": sum("/concept/" in path for path in updated),
            "questions_created": sum("/question/" in path for path in written),
            "questions_updated": sum("/question/" in path for path in updated),
            "left_unprocessed": remaining["pending_count"],
            "source_only": source_only, "errors": [], "working_written": written,
            "working_updated": updated, "trusted_changes": 0, "canonical_writes": 0,
        }


class SynthesisService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "synthesis"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("synthesis-*.md")) if self.directory.exists() else []

    def prepare(self, payload: dict[str, Any], *, provider_name: str) -> dict[str, Any]:
        reflection_ids = set(_list_of_text(payload.get("input_reflections", []), "input_reflections"))
        if len(reflection_ids) < 2:
            raise ValidationError("weekly synthesis requires at least two reflections")
        source_ids: set[str] = set()
        for reflection_id in reflection_ids:
            _, metadata, _ = self.repository.find_document(reflection_id)
            if metadata.get("type") != "reflection":
                raise ValidationError(f"weekly synthesis input is not a reflection: {reflection_id}")
            source_ids.update(str(item) for item in metadata.get("source_ids", []))
        input_concepts = set(_list_of_text(payload.get("input_concepts", []), "input_concepts"))
        for concept_id in input_concepts:
            _, metadata, _ = self.repository.find_document(concept_id)
            if metadata.get("type") != "concept":
                raise ValidationError(f"weekly synthesis input is not a concept: {concept_id}")
        patterns = _list_of_text(payload.get("emerging_patterns", []), "emerging_patterns")
        connections = validate_connections(payload.get("new_connections", []))
        tensions = _list_of_text(payload.get("unresolved_tensions", []), "unresolved_tensions")
        knowledge_updates = payload.get("knowledge_updates", [])
        if not isinstance(knowledge_updates, list):
            raise ValidationError("knowledge_updates must be a list")
        normalized_updates = [
            validate_knowledge_update(
                item, repository=self.repository, input_concepts=input_concepts,
                reflection_ids=reflection_ids, source_ids=source_ids,
            )
            for item in knowledge_updates
        ]
        if not any((patterns, connections, tensions)):
            raise ValidationError("weekly synthesis requires a pattern, qualified connection, or unresolved tension")
        raw_hypotheses = payload.get("candidate_hypotheses", [])
        if not isinstance(raw_hypotheses, list):
            raise ValidationError("candidate_hypotheses must be a list")
        hypotheses = [
            validate_hypothesis(item, reflection_ids, source_ids)
            for item in raw_hypotheses
        ]
        period = str(payload.get("period", "")).strip()
        if not period:
            raise ValidationError("weekly synthesis requires period")
        title = str(payload.get("title") or f"Weekly cognitive synthesis {period}")
        domains = _list_of_text(payload.get("domains", []), "domains")
        confidence = str(payload.get("confidence", "unknown")).strip().lower()
        if confidence not in CONFIDENCE_LEVELS:
            raise ValidationError(f"invalid synthesis confidence: {confidence}")
        possible_experiments = _list_of_text(
            payload.get("possible_experiments", []), "possible_experiments",
        )
        stable_payload = {
            "period": period, "input_reflections": sorted(reflection_ids),
            "input_concepts": sorted(input_concepts), "patterns": patterns,
            "connections": connections, "tensions": tensions, "hypotheses": hypotheses,
            "knowledge_updates": normalized_updates,
            "possible_experiments": possible_experiments,
            "title": title, "domains": domains, "confidence": confidence,
            "provider_name": provider_name,
        }
        synthesis_id = "synthesis_" + hashlib.sha256(
            json.dumps(stable_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        ).hexdigest()[:24]
        path = self.directory / f"synthesis-{synthesis_id}.md"
        return {
            "synthesis_id": synthesis_id, "path": path, "period": period,
            "title": title, "domains": domains, "confidence": confidence,
            "reflection_ids": reflection_ids, "source_ids": source_ids,
            "input_concepts": input_concepts, "patterns": patterns,
            "connections": connections, "tensions": tensions,
            "knowledge_updates": normalized_updates, "hypotheses": hypotheses,
            "possible_experiments": possible_experiments,
            "provider_name": provider_name,
        }

    def create_prepared(self, prepared: dict[str, Any]) -> CognitiveWrite:
        synthesis_id = prepared["synthesis_id"]
        path = prepared["path"]
        period = prepared["period"]
        if path.exists():
            existing, _ = read_document(path)
            if existing.get("id") != synthesis_id or existing.get("period") != period:
                raise ValidationError(f"Cognitive Synthesis identity collision: {synthesis_id}")
            return CognitiveWrite(synthesis_id, self.repository.rel(path), False)
        timestamp = now_iso()
        metadata = {
            "id": synthesis_id, "type": "synthesis", "status": "active",
            "title": prepared["title"],
            "created_at": timestamp, "updated_at": timestamp,
            "aliases": [], "tags": ["weekly-dream", "cognitive-synthesis"],
            "domains": prepared["domains"], "confidence": prepared["confidence"],
            "source_ids": sorted(prepared["source_ids"]), "relations": [],
            "period": period, "input_reflections": sorted(prepared["reflection_ids"]),
            "input_concepts": sorted(prepared["input_concepts"]),
            "emerging_patterns": prepared["patterns"],
            "knowledge_updates": prepared["knowledge_updates"],
            "new_connections": prepared["connections"],
            "unresolved_tensions": prepared["tensions"],
            "candidate_hypotheses": prepared["hypotheses"],
            "possible_experiments": prepared["possible_experiments"],
            "truth_layer": "cognitive_synthesis",
            "created_by": prepared["provider_name"], "execution_safe": False,
        }
        body = "\n\n".join([
            f"# {metadata['title']}",
            "## Emerging patterns\n\n" + ("\n".join(f"- {item}" for item in prepared["patterns"]) or "None."),
            "## Knowledge updates\n\n" + (json.dumps(metadata["knowledge_updates"], ensure_ascii=False, indent=2) or "None."),
            "## New connections\n\n" + (json.dumps(prepared["connections"], ensure_ascii=False, indent=2) or "None."),
            "## Unresolved tensions\n\n" + ("\n".join(f"- {item}" for item in prepared["tensions"]) or "None."),
            "## Candidate hypotheses\n\n" + (json.dumps(prepared["hypotheses"], ensure_ascii=False, indent=2) or "None."),
            "## Possible experiments\n\n" + ("\n".join(f"- {item}" for item in metadata["possible_experiments"]) or "None."),
        ]) + "\n"
        self.repository._validate_metadata(metadata, path)
        created = self.repository.immutable_write(path, render_document(metadata, body).encode("utf-8"))
        if created:
            self.repository.append_event("cognitive-events", {
                "event": "weekly-synthesis-created", "synthesis_id": synthesis_id,
                "period": period, "provider": prepared["provider_name"],
            })
        return CognitiveWrite(synthesis_id, self.repository.rel(path), created)

    def create(self, payload: dict[str, Any], *, provider_name: str) -> CognitiveWrite:
        return self.create_prepared(self.prepare(payload, provider_name=provider_name))


class WeeklyDreamService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self, bundle_file: Path | str) -> dict[str, Any]:
        payload = _load_json(bundle_file)
        synthesis_payload = payload.get("synthesis")
        if not isinstance(synthesis_payload, dict):
            raise ValidationError("weekly dream bundle requires synthesis")
        provider_name = str(payload.get("provider_name") or "agent-semantic-weekly-dream-v1")
        synthesis_service = SynthesisService(self.repository)
        prepared_synthesis = synthesis_service.prepare(
            synthesis_payload, provider_name=provider_name,
        )
        prepared_bundles: list[dict[str, Any]] = []
        allowed_reflections = set(prepared_synthesis["reflection_ids"])
        reflection_sources: dict[str, set[str]] = {}
        for reflection_id in allowed_reflections:
            _, reflection, _ = self.repository.find_document(reflection_id)
            reflection_sources[reflection_id] = {
                str(item) for item in reflection.get("source_ids", [])
            }
        for bundle in payload.get("knowledge_bundles", []):
            if not isinstance(bundle, dict) or not bundle.get("source_id"):
                raise ValidationError("weekly knowledge bundle requires source_id")
            bundle_reflections = set(_list_of_text(
                bundle.get("reflection_ids", []), "knowledge bundle reflection_ids",
            ))
            if not bundle_reflections or not bundle_reflections <= allowed_reflections:
                raise ValidationError(
                    "weekly knowledge bundle requires reflection_ids from this synthesis"
                )
            source_id = str(bundle["source_id"])
            supported_sources = set().union(
                *(reflection_sources[item] for item in bundle_reflections)
            )
            if source_id not in supported_sources:
                raise ValidationError(
                    "weekly knowledge bundle source must be covered by its reflection_ids"
                )
            semantic_items = validate_semantic_items(
                bundle.get("items"), allowed_types=WEEKLY_OBJECT_TYPES,
                label="weekly dream",
            )
            prepared_bundles.append({
                "source_id": source_id,
                "reflection_ids": sorted(bundle_reflections),
                "semantic_items": semantic_items,
            })
        before_canonical = len(list(self.repository.canonical_documents()))
        synthesis = synthesis_service.create_prepared(prepared_synthesis)
        _, synthesis_metadata, _ = self.repository.find_document(synthesis.object_id)
        written: list[str] = []
        updated: list[str] = []
        for bundle in prepared_bundles:
            source_id = bundle["source_id"]
            reflection_context = {
                "reflection_ids": bundle["reflection_ids"], "importance": "weekly",
                "changed_belief": "", "surprising": "", "connections": [],
                "open_questions": [],
            }
            changed: list[str] = []
            surprising: list[str] = []
            for reflection_id in bundle["reflection_ids"]:
                _, reflection, _ = self.repository.find_document(reflection_id)
                if reflection.get("what_changed"):
                    changed.append(str(reflection["what_changed"]))
                if reflection.get("surprising"):
                    surprising.append(str(reflection["surprising"]))
                reflection_context["connections"].extend(reflection.get("connections", []))
                reflection_context["open_questions"].extend(reflection.get("open_questions", []))
            reflection_context["changed_belief"] = "\n".join(changed)
            reflection_context["surprising"] = "\n".join(surprising)
            semantic_items: list[dict[str, Any]] = []
            for item in bundle["semantic_items"]:
                semantic_item = dict(item)
                metadata = dict(semantic_item.get("metadata") or {})
                metadata["reflection_context"] = reflection_context
                semantic_item["metadata"] = metadata
                semantic_items.append(semantic_item)
            provider = StaticBundleProvider(semantic_items, provider_name)
            compiled = BundleCompiler(self.repository, provider).compile(source_id)
            if compiled.proposal_id:
                result = WorkingMemoryService(self.repository).ingest_bundle(compiled.proposal_id, rebuild_index=True)
                written.extend(result.written)
                updated.extend(result.updated)
        self.repository.rebuild_index()
        if len(list(self.repository.canonical_documents())) != before_canonical:
            raise ValidationError("weekly dream violated the zero-Canonical-write boundary")
        return {
            "weekly_dream": "completed", "synthesis_id": synthesis.object_id,
            "synthesis_path": synthesis.path, "synthesis_created": synthesis.created,
            "input_reflections": len(synthesis_payload.get("input_reflections", [])),
            "working_created": written, "working_updated": updated,
            "candidate_hypotheses": len(synthesis_payload.get("candidate_hypotheses", [])),
            "trusted_changes": 0, "canonical_writes": 0,
        }
