from __future__ import annotations

import hashlib
import json
import os
import re
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from .bundle import BundleCompiler, CompilerProvider
from .capture import CaptureService
from .errors import NotFoundError, ValidationError
from .extraction import ExtractionService
from .markdown import atomic_write_text, read_document, render_document
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
DAILY_PROTOCOL_VERSION = 2
DAILY_READABILITY = {"readable", "degraded", "unreadable"}
DAILY_SOURCE_ROLES = {"primary", "secondary", "unknown"}
DAILY_VALUE_LEVELS = {"high", "medium", "low"}
DAILY_ADMISSION_DECISIONS = {
    "create", "update", "reuse", "source_only", "review_required", "deferred",
}
DAILY_SOURCE_ONLY_REASONS = {
    "unreadable", "duplicate", "insufficient_evidence", "too_broad",
    "metadata_only", "no_reusable_increment",
}
DAILY_REVIEW_REASONS = {"needs_deep_review", "dedup_uncertain", "evidence_ambiguous"}
DAILY_DEFER_REASONS = {"daily_item_limit"}
SYNTHESIS_PROTOCOL_VERSION = 2
SYNTHESIS_SCOPE_KINDS = {"direction", "cross_direction"}
SYNTHESIS_DELTA_KINDS = {
    "new", "extend", "refine", "limit", "tension", "contradiction", "reframe", "connect",
}


@contextmanager
def _exclusive_cognitive_write(repository: Repository) -> Iterator[None]:
    """Serialize Dream writers while letting the OS release the lock after a crash."""
    lock_path = repository.root / "system" / "locks" / "cognitive-dream.lock"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+b")
    if lock_path.stat().st_size == 0:
        handle.write(b"\0")
        handle.flush()
    acquired = False
    try:
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            acquired = True
        except (OSError, BlockingIOError) as exc:
            raise ValidationError(
                "another Daily/Weekly Dream is still writing; reuse the same artifact after it completes"
            ) from exc
        yield
    finally:
        if acquired:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()
GENERIC_REFLECTION = re.compile(
    r"^(?:这篇|本文|该文|文章|论文|项目).{0,24}(?:介绍|讨论|讲述|概述|总结)(?:了|的是)?",
    re.I,
)
COGNITIVE_VALUE_SIGNAL = re.compile(
    r"(?:可复用(?:的)?认知价值|改变|区分|边界|限制|避免|误读|不再|不能(?:把|将)|"
    r"提醒.{0,64}(?:未给出|不能|需要|边界|条件|前提)|"
    r"提示.{0,64}(?:前提|条件|边界|证据|判断|机制))",
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
    generic_opener = GENERIC_REFLECTION.search(why)
    if not why or (
        generic_opener
        and not COGNITIVE_VALUE_SIGNAL.search(why, generic_opener.end())
    ):
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


def _synthesis_protocol_version(payload: dict[str, Any]) -> int:
    raw = payload.get("synthesis_protocol_version", 1)
    if isinstance(raw, bool):
        raise ValidationError("synthesis_protocol_version must be an integer")
    try:
        version = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValidationError("synthesis_protocol_version must be an integer") from exc
    if version not in {1, SYNTHESIS_PROTOCOL_VERSION}:
        raise ValidationError(f"unsupported synthesis_protocol_version: {version}")
    return version


def _validate_candidate_window(value: Any) -> dict[str, str]:
    if not isinstance(value, dict):
        raise ValidationError("synthesis v2 requires candidate_window")
    start = str(value.get("from_date", "")).strip()
    end = str(value.get("to_date", "")).strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", start) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", end):
        raise ValidationError("candidate_window dates must use YYYY-MM-DD")
    if start > end:
        raise ValidationError("candidate_window.from_date must not be after to_date")
    return {"from_date": start, "to_date": end}


def _validate_direction_assignments(
    value: Any, *, reflection_ids: set[str], scope_kind: str, scope_ids: set[str],
) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise ValidationError("synthesis v2 requires direction_assignments")
    assignments: list[dict[str, Any]] = []
    assigned: set[str] = set()
    covered_directions: set[str] = set()
    for raw in value:
        if not isinstance(raw, dict):
            raise ValidationError("direction assignment must be an object")
        reflection_id = str(raw.get("reflection_id", "")).strip()
        primary = str(raw.get("primary_direction", "")).strip()
        secondary = _list_of_text(raw.get("secondary_directions", []), "secondary_directions")
        subdirections = _list_of_text(raw.get("subdirections", []), "subdirections")
        crosscuts = _list_of_text(raw.get("crosscut_dimensions", []), "crosscut_dimensions")
        confidence = str(raw.get("routing_confidence", "unknown")).strip().lower()
        reason = str(raw.get("reason", "")).strip()
        if reflection_id not in reflection_ids or reflection_id in assigned:
            raise ValidationError("direction assignments must cover unique input_reflections")
        if not primary or not subdirections or not reason:
            raise ValidationError("direction assignment requires primary_direction, subdirections, and reason")
        if primary in secondary:
            raise ValidationError("primary_direction cannot also be a secondary_direction")
        if confidence not in CONFIDENCE_LEVELS:
            raise ValidationError(f"invalid routing confidence: {confidence}")
        directions = {primary, *secondary}
        if scope_kind == "direction" and not scope_ids <= directions:
            raise ValidationError("each direction synthesis input must route to its declared scope")
        covered_directions.update(directions)
        assigned.add(reflection_id)
        assignment = {
            "reflection_id": reflection_id,
            "primary_direction": primary,
            "secondary_directions": secondary,
            "subdirections": subdirections,
            "crosscut_dimensions": crosscuts,
            "routing_confidence": confidence,
            "reason": reason,
        }
        # Preserve optional routing provenance without changing identities for
        # the first migrated v2 artifacts, which predate these two fields.
        source_role = str(raw.get("source_role", "")).strip()
        logical_work_id = str(raw.get("logical_work_id", "")).strip()
        if source_role:
            assignment["source_role"] = source_role
        if logical_work_id:
            assignment["logical_work_id"] = logical_work_id
        assignments.append(assignment)
    if assigned != reflection_ids:
        raise ValidationError("direction assignments must cover every input_reflection exactly once")
    if scope_kind == "cross_direction" and not scope_ids <= covered_directions:
        raise ValidationError("cross-direction assignments must cover every declared scope")
    return assignments


def _validate_scoped_connections(
    value: Any, *, protocol_version: int, reflection_ids: set[str],
    source_ids: set[str], scope_ids: set[str], scope_kind: str,
) -> list[dict[str, Any]]:
    if protocol_version < SYNTHESIS_PROTOCOL_VERSION or scope_kind == "direction":
        return validate_connections(value)
    if value is None or value == "":
        return []
    if not isinstance(value, list):
        raise ValidationError("connections must be a list")
    normalized: list[dict[str, Any]] = []
    for raw in value:
        if not isinstance(raw, dict):
            raise ValidationError("scoped connection must be an object")
        base = validate_connections([raw])[0]
        direction_ids = _list_of_text(raw.get("direction_ids", []), "connection direction_ids")
        supporting_reflections = _list_of_text(
            raw.get("supporting_reflections", []), "connection supporting_reflections",
        )
        supporting_sources = _list_of_text(
            raw.get("supporting_sources", []), "connection supporting_sources",
        )
        counter_arguments = _list_of_text(raw.get("counter_arguments", []), "connection counter_arguments")
        required_text = {
            key: str(raw.get(key, "")).strip()
            for key in ("why_potentially_useful", "evidence_gap", "verification_path")
        }
        confidence = str(raw.get("confidence", "unknown")).strip().lower()
        if not direction_ids or not set(direction_ids) <= scope_ids:
            raise ValidationError("scoped connection direction_ids must stay within synthesis scope")
        if scope_kind == "cross_direction" and len(set(direction_ids)) < 2:
            raise ValidationError("cross-direction connection requires at least two direction_ids")
        if not supporting_reflections or not set(supporting_reflections) <= reflection_ids:
            raise ValidationError("scoped connection requires supporting_reflections from this synthesis")
        if not supporting_sources or not set(supporting_sources) <= source_ids:
            raise ValidationError("scoped connection requires supporting_sources from this synthesis")
        if not counter_arguments or not all(required_text.values()):
            raise ValidationError(
                "scoped connection requires research value, counterarguments, evidence gap, and verification path"
            )
        if confidence not in CONFIDENCE_LEVELS:
            raise ValidationError(f"invalid connection confidence: {confidence}")
        normalized.append({
            **base,
            "direction_ids": direction_ids,
            "supporting_reflections": supporting_reflections,
            "supporting_sources": supporting_sources,
            "why_potentially_useful": required_text["why_potentially_useful"],
            "counter_arguments": counter_arguments,
            "evidence_gap": required_text["evidence_gap"],
            "verification_path": required_text["verification_path"],
            "confidence": confidence,
        })
    return normalized


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


def _daily_protocol_version(payload: dict[str, Any]) -> int:
    raw = payload.get("daily_protocol_version", 1)
    if isinstance(raw, bool):
        raise ValidationError("daily_protocol_version must be an integer")
    try:
        version = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValidationError("daily_protocol_version must be an integer") from exc
    if version not in {1, DAILY_PROTOCOL_VERSION}:
        raise ValidationError(f"unsupported daily_protocol_version: {version}")
    return version


def validate_daily_admission(
    item: dict[str, Any], *, normalized_reflection: dict[str, Any],
    semantic_items: list[dict[str, Any]], protocol_version: int,
    repository: Repository,
) -> dict[str, Any]:
    """Validate the model's semantic inventory separately from Working admission."""
    if protocol_version < DAILY_PROTOCOL_VERSION:
        return {
            "protocol_version": protocol_version,
            "source_assessment": {},
            "semantic_inventory": [],
            "admission_decisions": [],
            "semantic_candidates": len(semantic_items),
            "admitted_candidates": len(semantic_items),
            "review_required": 0,
            "deferred_candidates": 0,
            "high_value_reflection_only": False,
            "source_only_by_reason": Counter({"legacy_unspecified": 1}) if not semantic_items else Counter(),
            "existing_target_ids": [],
        }

    assessment = item.get("source_assessment")
    if not isinstance(assessment, dict):
        raise ValidationError("daily v2 item requires source_assessment")
    readability = str(assessment.get("readability", "")).strip().lower()
    source_role = str(assessment.get("source_role", "")).strip().lower()
    assessment_reason = str(assessment.get("reason", "")).strip()
    if readability not in DAILY_READABILITY:
        raise ValidationError("daily v2 source_assessment requires valid readability")
    if source_role not in DAILY_SOURCE_ROLES:
        raise ValidationError("daily v2 source_assessment requires valid source_role")
    if readability != "readable" and not assessment_reason:
        raise ValidationError("degraded or unreadable source_assessment requires reason")
    source_assessment = {
        "readability": readability, "source_role": source_role, "reason": assessment_reason,
    }

    raw_inventory = item.get("semantic_inventory")
    if not isinstance(raw_inventory, list):
        raise ValidationError("daily v2 item requires semantic_inventory list")
    inventory: list[dict[str, Any]] = []
    inventory_by_id: dict[str, dict[str, Any]] = {}
    for raw_candidate in raw_inventory:
        if not isinstance(raw_candidate, dict):
            raise ValidationError("daily semantic inventory candidate must be an object")
        candidate_id = str(raw_candidate.get("candidate_id", "")).strip()
        candidate_type = str(raw_candidate.get("candidate_type", "")).strip()
        statement = str(raw_candidate.get("statement", "")).strip()
        value = str(raw_candidate.get("value", "")).strip().lower()
        value_reason = str(raw_candidate.get("value_reason", "")).strip()
        if not candidate_id or candidate_id in inventory_by_id:
            raise ValidationError("daily semantic inventory requires unique candidate_id values")
        if candidate_type not in DAILY_OBJECT_TYPES:
            raise ValidationError(f"daily semantic inventory does not allow candidate_type: {candidate_type or '<missing>'}")
        if not statement or not value_reason or value not in DAILY_VALUE_LEVELS:
            raise ValidationError("daily semantic inventory requires statement, value, and value_reason")
        if not isinstance(raw_candidate.get("source_grounded"), bool):
            raise ValidationError("daily semantic inventory requires boolean source_grounded")
        candidate = {
            "candidate_id": candidate_id, "candidate_type": candidate_type,
            "statement": statement, "value": value, "value_reason": value_reason,
            "source_grounded": raw_candidate["source_grounded"],
        }
        inventory.append(candidate)
        inventory_by_id[candidate_id] = candidate

    empty_reason = str(item.get("empty_inventory_reason_code", "")).strip().lower()
    if not inventory:
        if empty_reason not in DAILY_SOURCE_ONLY_REASONS:
            raise ValidationError("empty daily semantic inventory requires a specific source-only reason code")
        if normalized_reflection.get("importance") == "high" and readability == "readable":
            raise ValidationError("high-importance readable input cannot have an empty semantic inventory")
    elif empty_reason:
        raise ValidationError("empty_inventory_reason_code is only valid for an empty semantic inventory")

    raw_decisions = item.get("admission_decisions")
    if not isinstance(raw_decisions, list):
        raise ValidationError("daily v2 item requires admission_decisions list")
    decisions: list[dict[str, Any]] = []
    decisions_by_id: dict[str, dict[str, Any]] = {}
    source_only_by_reason: Counter[str] = Counter()
    existing_target_ids: list[str] = []
    for raw_decision in raw_decisions:
        if not isinstance(raw_decision, dict):
            raise ValidationError("daily admission decision must be an object")
        candidate_id = str(raw_decision.get("candidate_id", "")).strip()
        decision = str(raw_decision.get("decision", "")).strip().lower()
        reason_code = str(raw_decision.get("reason_code", "")).strip().lower()
        reason = str(raw_decision.get("reason", "")).strip()
        target_ids = _list_of_text(raw_decision.get("target_ids", []), "target_ids")
        if candidate_id not in inventory_by_id or candidate_id in decisions_by_id:
            raise ValidationError("daily admission decisions must cover unique inventory candidate_ids")
        if decision not in DAILY_ADMISSION_DECISIONS or not reason:
            raise ValidationError("daily admission decision requires decision and reason")
        if decision == "source_only" and reason_code not in DAILY_SOURCE_ONLY_REASONS:
            raise ValidationError("source_only decision requires a specific reason_code")
        if decision == "review_required" and reason_code not in DAILY_REVIEW_REASONS:
            raise ValidationError("review_required decision requires a review reason_code")
        if decision == "deferred" and reason_code not in DAILY_DEFER_REASONS:
            raise ValidationError("deferred decision requires daily_item_limit reason_code")
        if decision in {"update", "reuse"} and not target_ids:
            raise ValidationError(f"{decision} decision requires target_ids")
        if decision == "create" and target_ids:
            raise ValidationError("create decision cannot declare existing target_ids")
        if reason_code == "duplicate" and not target_ids:
            raise ValidationError("duplicate decision requires compared target_ids")
        candidate = inventory_by_id[candidate_id]
        for target_id in target_ids:
            try:
                _, target, _ = repository.find_document(target_id)
            except NotFoundError as exc:
                raise ValidationError(f"daily admission target does not exist: {target_id}") from exc
            if target.get("type") != candidate["candidate_type"]:
                raise ValidationError("daily admission target type must match the inventory candidate")
            if target.get("memory_tier") == "historical" or target.get("status") in {"archived", "superseded"}:
                raise ValidationError("daily admission target must be active")
        if (
            candidate["value"] == "high" and readability == "readable"
            and candidate["source_grounded"] and decision == "source_only"
            and reason_code not in {"duplicate", "insufficient_evidence"}
        ):
            raise ValidationError(
                "high-value readable source-grounded candidate must be admitted, reused, deferred, or reviewed"
            )
        normalized = {
            "candidate_id": candidate_id, "decision": decision,
            "reason_code": reason_code, "reason": reason, "target_ids": target_ids,
        }
        decisions.append(normalized)
        decisions_by_id[candidate_id] = normalized
        existing_target_ids.extend(target_ids)
        if decision == "source_only":
            source_only_by_reason[reason_code] += 1

    if set(decisions_by_id) != set(inventory_by_id):
        raise ValidationError("daily admission decisions must cover every semantic inventory candidate")

    items_by_candidate: dict[str, dict[str, Any]] = {}
    for semantic_item in semantic_items:
        candidate_id = str(semantic_item.get("candidate_id", "")).strip()
        if candidate_id not in inventory_by_id or candidate_id in items_by_candidate:
            raise ValidationError("daily v2 semantic_items require unique inventory candidate_id values")
        items_by_candidate[candidate_id] = semantic_item
    admitted_ids = {
        candidate_id for candidate_id, decision in decisions_by_id.items()
        if decision["decision"] in {"create", "update"}
    }
    if set(items_by_candidate) != admitted_ids:
        raise ValidationError("daily v2 semantic_items must exactly match create/update decisions")
    for candidate_id in admitted_ids:
        decision = decisions_by_id[candidate_id]
        candidate = inventory_by_id[candidate_id]
        semantic_item = items_by_candidate[candidate_id]
        if not candidate["source_grounded"]:
            raise ValidationError("create/update candidate must be source_grounded")
        if semantic_item.get("object_type") != candidate["candidate_type"]:
            raise ValidationError("semantic item object_type must match its inventory candidate")
        target_id = str(semantic_item.get("target_id", "")).strip()
        if decision["decision"] == "update":
            if target_id not in decision["target_ids"] or not str(semantic_item.get("change_type", "")).strip():
                raise ValidationError("update semantic item requires matching target_id and change_type")
        elif target_id:
            raise ValidationError("create semantic item cannot declare target_id")

    if not inventory:
        source_only_by_reason[empty_reason] += 1
    admitted_or_reused = sum(
        decision["decision"] in {"create", "update", "reuse"} for decision in decisions
    )
    high_value = [candidate for candidate in inventory if candidate["value"] == "high"]
    high_value_admitted = any(
        decisions_by_id[candidate["candidate_id"]]["decision"] in {"create", "update", "reuse"}
        for candidate in high_value
    )
    return {
        "protocol_version": protocol_version,
        "source_assessment": source_assessment,
        "semantic_inventory": inventory,
        "admission_decisions": decisions,
        "semantic_candidates": len(inventory),
        "admitted_candidates": admitted_or_reused,
        "review_required": sum(decision["decision"] == "review_required" for decision in decisions),
        "deferred_candidates": sum(decision["decision"] == "deferred" for decision in decisions),
        "high_value_reflection_only": bool(high_value and not high_value_admitted),
        "source_only_by_reason": source_only_by_reason,
        "existing_target_ids": list(dict.fromkeys(existing_target_ids)),
    }


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
        return self.record_agent_session(
            {key: data[key] for key in ("goal", "result", "lesson")},
            agent=agent,
            session_ref=source_path.name,
            source_path=source_path,
        )

    def record_agent_session(
        self,
        data: dict[str, Any],
        *,
        agent: str,
        session_ref: str,
        source_path: Path | None = None,
    ) -> dict[str, Any]:
        """Record one provider-neutral session summary as Source + Input only."""
        allowed = {"goal", "result", "lesson"}
        unknown = set(data) - allowed
        if unknown:
            raise ValidationError(f"agent session contains unsupported fields: {', '.join(sorted(unknown))}")
        normalized = {key: str(data.get(key, "")).strip() for key in sorted(allowed)}
        if not all(normalized.values()):
            raise ValidationError("agent session requires explicit goal, result, and lesson")
        normalized_agent = agent.strip().casefold()
        if not normalized_agent or len(normalized_agent) > 80:
            raise ValidationError("agent identity must contain 1 to 80 characters")
        normalized_session = session_ref.strip()
        if not normalized_session or len(normalized_session) > 200:
            raise ValidationError("session_ref must contain 1 to 200 characters")
        if source_path is not None:
            captured = CaptureService(self.repository).capture(
                str(source_path), f"agent session from {normalized_agent}",
            )
        else:
            body = json.dumps(
                {"agent": normalized_agent, "session_ref": normalized_session, **normalized},
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            captured = CaptureService(self.repository).capture_text(
                body,
                f"agent session from {normalized_agent}",
                title=f"{normalized_agent} session: {normalized['goal'][:120]}",
            )
        episode = self.create_from_source(
            captured.source_id, input_type="experiment",
            title=f"{normalized_agent} session: {normalized['goal'][:160]}",
            participants=[normalized_agent], user_authored=False, submitted_by=normalized_agent,
            episode_kind="agent_session",
            session={"session_ref": normalized_session, **normalized},
        )
        self.repository.rebuild_index()
        return {
            "source": captured.__dict__, "input": episode.__dict__,
            "reflection_queued": True, "knowledge_writes": 0,
            "trusted_writes": 0, "canonical_writes": 0,
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


def _artifact_sha256(path: Path | str) -> str:
    return hashlib.sha256(Path(path).expanduser().resolve().read_bytes()).hexdigest()


def _bind_proposal_to_artifact(repository: Repository, proposal_id: str, artifact_sha256: str) -> None:
    path, metadata, body = repository.find_document(proposal_id)
    metadata["cognitive_artifact_sha256"] = artifact_sha256
    atomic_write_text(path, render_document(metadata, body))


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
        with _exclusive_cognitive_write(self.repository):
            return self._run_locked(bundle_file, limit=limit)

    def _run_locked(self, bundle_file: Path | str, *, limit: int = 5) -> dict[str, Any]:
        payload = _load_json(bundle_file)
        artifact_sha256 = _artifact_sha256(bundle_file)
        protocol_version = _daily_protocol_version(payload)
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
            try:
                prepared = reflection_service.prepare(input_id, reflection_payload)
            except ValidationError as exc:
                raise ValidationError(f"daily dream input {input_id}: {exc}") from exc
            resumable = prepared["path"].exists()
            if input_id not in selected and not resumable:
                raise ValidationError("daily dream may only process the current bounded reflection queue")
            semantic_items = validate_semantic_items(
                item.get("semantic_items", []), allowed_types=DAILY_OBJECT_TYPES,
                label="daily dream", maximum=3,
            )
            admission = validate_daily_admission(
                item, normalized_reflection=prepared["normalized"],
                semantic_items=semantic_items, protocol_version=protocol_version,
                repository=self.repository,
            )
            plans.append({
                "input_id": input_id, "reflection": reflection_payload,
                "prepared": prepared, "semantic_items": semantic_items,
                "admission": admission,
            })
        before_canonical = len(list(self.repository.canonical_documents()))
        reflection_ids: list[str] = []
        reflections_created = 0
        reflections_reused = 0
        written: list[str] = []
        updated: list[str] = []
        source_only = 0
        semantic_candidates = 0
        admitted_candidates = 0
        review_required = 0
        deferred_candidates = 0
        high_value_reflection_only = 0
        source_only_by_reason: Counter[str] = Counter()
        reused_target_ids: list[str] = []
        decision_total = 0
        decision_covered = 0
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
            admission = plan["admission"]
            semantic_candidates += admission["semantic_candidates"]
            admitted_candidates += admission["admitted_candidates"]
            review_required += admission["review_required"]
            deferred_candidates += admission["deferred_candidates"]
            high_value_reflection_only += int(admission["high_value_reflection_only"])
            source_only_by_reason.update(admission["source_only_by_reason"])
            decisions = admission["admission_decisions"]
            decision_total += len(admission["semantic_inventory"])
            decision_covered += len(decisions)
            reused_target_ids.extend(
                target_id for decision in decisions if decision["decision"] == "reuse"
                for target_id in decision["target_ids"]
            )
            if not semantic_items:
                if protocol_version < DAILY_PROTOCOL_VERSION:
                    source_only += 1
                elif not any(
                    decision["decision"] in {"reuse", "review_required", "deferred"}
                    for decision in decisions
                ):
                    source_only += 1
                continue
            for semantic_item in semantic_items:
                metadata = dict(semantic_item.get("metadata") or {})
                metadata["reflection_context"] = _context_from_reflection(reflection_write.object_id, reflection)
                semantic_item["metadata"] = metadata
            _, episode, _ = self.repository.find_document(input_id)
            source_id = str(episode.get("source_id"))
            compiler_items = [
                {key: value for key, value in semantic_item.items() if key != "candidate_id"}
                for semantic_item in semantic_items
            ]
            provider = StaticBundleProvider(compiler_items, str(payload.get("provider_name") or "agent-semantic-daily-dream-v1"))
            compiled = BundleCompiler(self.repository, provider).compile(source_id)
            if compiled.proposal_id:
                _bind_proposal_to_artifact(self.repository, compiled.proposal_id, artifact_sha256)
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
            "daily_protocol_version": protocol_version,
            "reflections_created": reflections_created,
            "reflections_reused": reflections_reused, "reflection_ids": reflection_ids,
            "concepts_created": sum("/concept/" in path for path in written),
            "concepts_updated": sum("/concept/" in path for path in updated),
            "questions_created": sum("/question/" in path for path in written),
            "questions_updated": sum("/question/" in path for path in updated),
            "left_unprocessed": remaining["pending_count"],
            "source_only": source_only, "errors": [], "working_written": written,
            "working_updated": updated, "trusted_changes": 0, "canonical_writes": 0,
            "semantic_candidates": semantic_candidates,
            "admitted_candidates": admitted_candidates,
            "existing_nodes_reused": len(set(reused_target_ids)),
            "existing_node_ids_reused": sorted(set(reused_target_ids)),
            "high_value_reflection_only": high_value_reflection_only,
            "review_required": review_required,
            "deferred_candidates": deferred_candidates,
            "source_only_by_reason": dict(sorted(source_only_by_reason.items())),
            "decision_coverage": {
                "covered": decision_covered, "total": decision_total,
                "ratio": 1.0 if decision_total == 0 else decision_covered / decision_total,
            },
        }


class DailyAdmissionAuditService:
    """Read-only coverage audit over persisted Daily Dream artifacts."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "data" / "derived" / "cognitive" / "daily"

    @staticmethod
    def _validate_date(value: str | None, field: str) -> str | None:
        if value is None:
            return None
        normalized = str(value).strip()
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", normalized):
            raise ValidationError(f"{field} must use YYYY-MM-DD")
        return normalized

    def audit(self, *, from_date: str | None = None, to_date: str | None = None) -> dict[str, Any]:
        start = self._validate_date(from_date, "from_date")
        end = self._validate_date(to_date, "to_date")
        if start and end and start > end:
            raise ValidationError("from_date must not be after to_date")
        paths = sorted(self.directory.glob("*.json")) if self.directory.exists() else []
        selected = [
            path for path in paths
            if re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.name[:10])
            and (not start or path.name[:10] >= start)
            and (not end or path.name[:10] <= end)
        ]
        totals: Counter[str] = Counter()
        source_only_by_reason: Counter[str] = Counter()
        resolution_by_input: dict[str, dict[str, Any] | None] = {}
        ever_unresolved: set[str] = set()
        errors: list[dict[str, str]] = []
        for path in selected:
            try:
                payload = _load_json(path)
                version = _daily_protocol_version(payload)
                reflections = payload.get("reflections")
                if not isinstance(reflections, list):
                    raise ValidationError("daily dream bundle requires reflections")
                for index, item in enumerate(reflections):
                    if not isinstance(item, dict):
                        raise ValidationError("daily dream item must be an object")
                    totals["inputs"] += 1
                    input_id = str(item.get("input_id", "")).strip()
                    if not input_id:
                        raise ValidationError("daily dream item requires input_id")
                    semantic_items = validate_semantic_items(
                        item.get("semantic_items", []), allowed_types=DAILY_OBJECT_TYPES,
                        label="daily admission audit", maximum=3,
                    )
                    if version < DAILY_PROTOCOL_VERSION:
                        totals["legacy_inputs"] += 1
                        totals["semantic_candidates"] += len(semantic_items)
                        totals["admitted_candidates"] += len(semantic_items)
                        reflection = item.get("reflection") if isinstance(item.get("reflection"), dict) else {}
                        if not semantic_items:
                            source_only_by_reason["legacy_unspecified"] += 1
                            if str(reflection.get("importance", "medium")).lower() == "high":
                                totals["high_value_reflection_only_events"] += 1
                                current = {
                                    "artifact": self.repository.rel(path),
                                    "input_id": input_id,
                                    "reasons": ["legacy_high_value_empty"],
                                }
                                resolution_by_input[input_id] = current
                                ever_unresolved.add(input_id)
                            else:
                                resolution_by_input[input_id] = None
                        else:
                            resolution_by_input[input_id] = None
                        continue
                    totals["v2_inputs"] += 1
                    normalized_reflection = validate_reflection_payload(item.get("reflection", {}))
                    admission = validate_daily_admission(
                        item, normalized_reflection=normalized_reflection,
                        semantic_items=semantic_items, protocol_version=version,
                        repository=self.repository,
                    )
                    totals["semantic_candidates"] += admission["semantic_candidates"]
                    totals["admitted_candidates"] += admission["admitted_candidates"]
                    totals["review_required"] += admission["review_required"]
                    totals["deferred_candidates"] += admission["deferred_candidates"]
                    totals["high_value_reflection_only_events"] += int(admission["high_value_reflection_only"])
                    totals["decision_total"] += len(admission["semantic_inventory"])
                    totals["decision_covered"] += len(admission["admission_decisions"])
                    source_only_by_reason.update(admission["source_only_by_reason"])
                    reasons: list[str] = []
                    if admission["review_required"]:
                        reasons.append("review_required")
                    if admission["deferred_candidates"]:
                        reasons.append("deferred_candidates")
                    if admission["high_value_reflection_only"]:
                        reasons.append("high_value_reflection_only")
                    if reasons:
                        current = {
                            "artifact": self.repository.rel(path),
                            "input_id": input_id,
                            "reasons": reasons,
                        }
                        resolution_by_input[input_id] = current
                        ever_unresolved.add(input_id)
                    else:
                        resolution_by_input[input_id] = None
            except (OSError, UnicodeDecodeError, ValidationError) as exc:
                errors.append({"artifact": self.repository.rel(path), "error": str(exc)})
        decision_total = totals["decision_total"]
        unresolved = [
            state for input_id, state in sorted(resolution_by_input.items())
            if state is not None
        ]
        current_high_value_reflection_only = sum(
            "legacy_high_value_empty" in state["reasons"]
            or "high_value_reflection_only" in state["reasons"]
            for state in unresolved
        )
        return {
            "ok": not errors,
            "from_date": start, "to_date": end,
            "artifacts": len(selected), "inputs": totals["inputs"],
            "unique_inputs": len(resolution_by_input),
            "v2_inputs": totals["v2_inputs"], "legacy_inputs": totals["legacy_inputs"],
            "semantic_candidates": totals["semantic_candidates"],
            "admitted_candidates": totals["admitted_candidates"],
            "high_value_reflection_only": current_high_value_reflection_only,
            "high_value_reflection_only_events": totals["high_value_reflection_only_events"],
            "resolved_prior_unresolved": len(ever_unresolved - {
                item["input_id"] for item in unresolved
            }),
            "review_required": totals["review_required"],
            "deferred_candidates": totals["deferred_candidates"],
            "source_only_by_reason": dict(sorted(source_only_by_reason.items())),
            "decision_coverage": {
                "covered": totals["decision_covered"], "total": decision_total,
                "ratio": 1.0 if decision_total == 0 else totals["decision_covered"] / decision_total,
            },
            "unresolved": unresolved, "errors": errors,
            "weekly_ready": not unresolved and not errors,
            "canonical_writes": 0,
        }


class SynthesisService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "synthesis"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("synthesis-*.md")) if self.directory.exists() else []

    def prepare(self, payload: dict[str, Any], *, provider_name: str) -> dict[str, Any]:
        protocol_version = _synthesis_protocol_version(payload)
        reflection_ids = set(_list_of_text(payload.get("input_reflections", []), "input_reflections"))
        if len(reflection_ids) < 2:
            raise ValidationError("synthesis requires at least two reflections")
        source_ids: set[str] = set()
        for reflection_id in reflection_ids:
            _, metadata, _ = self.repository.find_document(reflection_id)
            if metadata.get("type") != "reflection":
                raise ValidationError(f"synthesis input is not a reflection: {reflection_id}")
            source_ids.update(str(item) for item in metadata.get("source_ids", []))
        input_concepts = set(_list_of_text(payload.get("input_concepts", []), "input_concepts"))
        for concept_id in input_concepts:
            _, metadata, _ = self.repository.find_document(concept_id)
            if metadata.get("type") != "concept":
                raise ValidationError(f"synthesis input is not a concept: {concept_id}")
        if protocol_version >= SYNTHESIS_PROTOCOL_VERSION:
            scope_kind = str(payload.get("scope_kind", "")).strip().lower()
            scope_ids = set(_list_of_text(payload.get("scope_ids", []), "scope_ids"))
            if scope_kind not in SYNTHESIS_SCOPE_KINDS or not scope_ids:
                raise ValidationError("synthesis v2 requires scope_kind and scope_ids")
            if scope_kind == "direction" and len(scope_ids) != 1:
                raise ValidationError("direction synthesis requires exactly one scope_id")
            if scope_kind == "cross_direction" and len(scope_ids) < 2:
                raise ValidationError("cross-direction synthesis requires at least two scope_ids")
            candidate_window = _validate_candidate_window(payload.get("candidate_window"))
            delta_kind = str(payload.get("delta_kind", "")).strip().lower()
            if delta_kind not in SYNTHESIS_DELTA_KINDS:
                raise ValidationError("synthesis v2 requires a valid delta_kind")
            direction_assignments = _validate_direction_assignments(
                payload.get("direction_assignments"), reflection_ids=reflection_ids,
                scope_kind=scope_kind, scope_ids=scope_ids,
            )
        else:
            scope_kind = "legacy_period"
            scope_ids = set()
            candidate_window = {}
            delta_kind = ""
            direction_assignments = []
        input_syntheses = set(_list_of_text(payload.get("input_syntheses", []), "input_syntheses"))
        for synthesis_id in input_syntheses:
            _, metadata, _ = self.repository.find_document(synthesis_id)
            if metadata.get("type") != "synthesis" or metadata.get("status") != "active":
                raise ValidationError(f"input synthesis must be active: {synthesis_id}")
            if protocol_version >= SYNTHESIS_PROTOCOL_VERSION and scope_kind == "cross_direction":
                if metadata.get("scope_kind") != "direction":
                    raise ValidationError("cross-direction synthesis inputs must be direction syntheses")
        if protocol_version >= SYNTHESIS_PROTOCOL_VERSION:
            if scope_kind == "cross_direction" and len(input_syntheses) < 2:
                raise ValidationError("cross-direction synthesis requires at least two input_syntheses")
            if scope_kind == "direction" and len(input_syntheses) > 1:
                raise ValidationError("direction synthesis may reference at most one prior synthesis")
        patterns = _list_of_text(payload.get("emerging_patterns", []), "emerging_patterns")
        connections = _validate_scoped_connections(
            payload.get("new_connections", []), protocol_version=protocol_version,
            reflection_ids=reflection_ids, source_ids=source_ids,
            scope_ids=scope_ids, scope_kind=scope_kind,
        )
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
            raise ValidationError("synthesis requires a pattern, qualified connection, or unresolved tension")
        raw_hypotheses = payload.get("candidate_hypotheses", [])
        if not isinstance(raw_hypotheses, list):
            raise ValidationError("candidate_hypotheses must be a list")
        hypotheses = [
            validate_hypothesis(item, reflection_ids, source_ids)
            for item in raw_hypotheses
        ]
        period = str(payload.get("period", "")).strip()
        if protocol_version < SYNTHESIS_PROTOCOL_VERSION and not period:
            raise ValidationError("weekly synthesis requires period")
        default_title = (
            f"{scope_kind.replace('_', '-')} cognitive synthesis: {', '.join(sorted(scope_ids))}"
            if protocol_version >= SYNTHESIS_PROTOCOL_VERSION
            else f"Weekly cognitive synthesis {period}"
        )
        title = str(payload.get("title") or default_title)
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
        if protocol_version >= SYNTHESIS_PROTOCOL_VERSION:
            stable_payload.update({
                "synthesis_protocol_version": protocol_version,
                "scope_kind": scope_kind,
                "scope_ids": sorted(scope_ids),
                "candidate_window": candidate_window,
                "delta_kind": delta_kind,
                "direction_assignments": direction_assignments,
                "input_syntheses": sorted(input_syntheses),
            })
        synthesis_id = "synthesis_" + hashlib.sha256(
            json.dumps(stable_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        ).hexdigest()[:24]
        path = self.directory / f"synthesis-{synthesis_id}.md"
        return {
            "synthesis_id": synthesis_id, "path": path, "period": period,
            "protocol_version": protocol_version,
            "scope_kind": scope_kind, "scope_ids": scope_ids,
            "candidate_window": candidate_window, "delta_kind": delta_kind,
            "direction_assignments": direction_assignments,
            "input_syntheses": input_syntheses,
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
            if existing.get("id") != synthesis_id or existing.get("period", "") != period:
                raise ValidationError(f"Cognitive Synthesis identity collision: {synthesis_id}")
            return CognitiveWrite(synthesis_id, self.repository.rel(path), False)
        timestamp = now_iso()
        protocol_version = prepared["protocol_version"]
        synthesis_tag = (
            f"{prepared['scope_kind'].replace('_', '-')}-synthesis"
            if protocol_version >= SYNTHESIS_PROTOCOL_VERSION else "weekly-dream"
        )
        metadata = {
            "id": synthesis_id, "type": "synthesis", "status": "active",
            "title": prepared["title"],
            "created_at": timestamp, "updated_at": timestamp,
            "aliases": [], "tags": [synthesis_tag, "cognitive-synthesis"],
            "domains": prepared["domains"], "confidence": prepared["confidence"],
            "source_ids": sorted(prepared["source_ids"]), "relations": [],
            "input_reflections": sorted(prepared["reflection_ids"]),
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
        if protocol_version >= SYNTHESIS_PROTOCOL_VERSION:
            metadata.update({
                "synthesis_protocol_version": protocol_version,
                "scope_kind": prepared["scope_kind"],
                "scope_ids": sorted(prepared["scope_ids"]),
                "candidate_window": prepared["candidate_window"],
                "delta_kind": prepared["delta_kind"],
                "direction_assignments": prepared["direction_assignments"],
                "input_syntheses": sorted(prepared["input_syntheses"]),
            })
        else:
            metadata["period"] = period
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
            event = {
                "event": (
                    f"{prepared['scope_kind'].replace('_', '-')}-synthesis-created"
                    if protocol_version >= SYNTHESIS_PROTOCOL_VERSION
                    else "weekly-synthesis-created"
                ),
                "synthesis_id": synthesis_id,
                "provider": prepared["provider_name"],
            }
            if protocol_version >= SYNTHESIS_PROTOCOL_VERSION:
                event.update({
                    "scope_kind": prepared["scope_kind"],
                    "scope_ids": sorted(prepared["scope_ids"]),
                    "candidate_window": prepared["candidate_window"],
                })
            else:
                event["period"] = period
            self.repository.append_event("cognitive-events", event)
        return CognitiveWrite(synthesis_id, self.repository.rel(path), created)

    def create(self, payload: dict[str, Any], *, provider_name: str) -> CognitiveWrite:
        return self.create_prepared(self.prepare(payload, provider_name=provider_name))


class WeeklyDreamService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def run(self, bundle_file: Path | str) -> dict[str, Any]:
        with _exclusive_cognitive_write(self.repository):
            return self._run_locked(bundle_file)

    def _run_locked(self, bundle_file: Path | str) -> dict[str, Any]:
        payload = _load_json(bundle_file)
        artifact_sha256 = _artifact_sha256(bundle_file)
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
                _bind_proposal_to_artifact(self.repository, compiled.proposal_id, artifact_sha256)
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
            "synthesis_protocol_version": prepared_synthesis["protocol_version"],
            "scope_kind": prepared_synthesis["scope_kind"],
            "scope_ids": sorted(prepared_synthesis["scope_ids"]),
            "trusted_changes": 0, "canonical_writes": 0,
        }
