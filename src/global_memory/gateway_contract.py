from __future__ import annotations

from pathlib import Path
from typing import Any

from .consolidation import ConsolidationReceiptService
from .epistemics import infer_epistemic_status, infer_tier, truth_layer
from .governance import POLICY_VERSION
from .quality import SourceQualityService
from .repository import Repository


EVIDENCE_ITEM_VERSION = 1
EVIDENCE_PACKET_VERSION = 2
GATEWAY_CONTRACT_VERSION = 1

NON_FACTUAL_LAYERS = {"user_annotation", "reflection", "cognitive_synthesis", "source_capture", "input"}
NON_GOVERNED_TYPES = {"source", "annotation", "input", "reflection", "synthesis"}


def public_source_reference(repository: Repository, source_id: str) -> dict[str, Any]:
    """Return a stable public source locator without leaking repository paths."""
    try:
        path, metadata, _ = repository.find_document(source_id)
        if metadata.get("type") != "source":
            raise ValueError("not a source")
        assessment = SourceQualityService(repository).load(source_id)
        if assessment is None:
            assessment = SourceQualityService(repository).assess(source_id, persist=False)
        locator = str(metadata.get("canonical_locator") or metadata.get("original_locator") or "")
        return {
            "ref": source_id,
            "title": metadata.get("title") or source_id,
            "author": metadata.get("author") or None,
            "published_at": metadata.get("published_at"),
            "source_kind": metadata.get("source_kind"),
            "locator": locator if locator.startswith(("https://", "http://")) else None,
            "status": metadata.get("status"),
            "source_authority": assessment.source_authority,
            "available": path.exists(),
        }
    except Exception:
        return {"ref": source_id, "title": "Referenced source", "available": False}


def public_evidence(items: Any) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        text = item.get("text") or item.get("original_text") or item.get("interpretation") or item.get("excerpt") or ""
        result.append({
            "source_ref": item.get("source_ref") or item.get("source_id"),
            "stance": item.get("stance"),
            "evidence_kind": item.get("evidence_kind", "legacy_excerpt"),
            "page": item.get("page"),
            "section": item.get("section"),
            "text": str(text)[:240],
            "verification_status": item.get("verification_status"),
        })
    return result


def _relation_contradictions(repository: Repository, object_id: str) -> list[str]:
    contradictions: list[str] = []
    try:
        for relation in repository.related(object_id):
            if relation.get("relation_type") == "contradicts":
                other = relation.get("target_id") or relation.get("source_id")
                contradictions.append(str(other or "relation"))
    except Exception:
        contradictions.append("relation_state_unavailable")
    return sorted(set(contradictions))


def governance_snapshot(
    repository: Repository,
    path: Path,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    object_id = str(metadata.get("id") or "")
    object_type = str(metadata.get("type") or "unknown")
    layer = truth_layer(metadata, path)
    tier = None if object_type in NON_GOVERNED_TYPES else infer_tier(metadata, path)
    epistemic = (
        "user_annotation" if object_type == "annotation"
        else "reflection" if object_type == "reflection"
        else "cognitive_synthesis" if object_type == "synthesis"
        else "unknown" if object_type in {"source", "input"}
        else infer_epistemic_status(metadata, tier)
    )
    non_governed = object_type in NON_GOVERNED_TYPES
    receipt = None if non_governed else ConsolidationReceiptService(repository).valid_for(object_id)
    semantic_failures = (
        [] if non_governed
        else ConsolidationReceiptService.semantic_qualification_failures(object_type, receipt)
    )
    policy_version = metadata.get("trust_policy_version") if not non_governed else None
    policy_qualified = bool(
        tier == "trusted"
        and policy_version == POLICY_VERSION
        and not metadata.get("needs_policy_requalification")
        and receipt is not None
        and not semantic_failures
        and epistemic != "contested"
        and not metadata.get("high_risk_drift")
    )
    contradictions = sorted(set(
        map(str, metadata.get("unresolved_contradictions", []))
    ) | set(_relation_contradictions(repository, object_id)))
    execution_safe = bool(
        not non_governed
        and not contradictions
        and (
            policy_qualified
            or (
                tier == "canonical"
                and receipt is not None
                and not semantic_failures
                and epistemic not in {"contested", "hypothetical", "exploratory_analogy", "unknown"}
                and not metadata.get("high_risk_drift")
            )
        )
    )
    qualification_failures: list[str] = []
    if not non_governed:
        if tier == "trusted" and policy_version != POLICY_VERSION:
            qualification_failures.append("policy_version_not_current")
        if metadata.get("needs_policy_requalification"):
            qualification_failures.append("awaiting_requalification")
        if receipt is None:
            qualification_failures.append("receipt_missing_or_stale")
        qualification_failures.extend(semantic_failures)
        if epistemic == "contested":
            qualification_failures.append("contested")
        if metadata.get("high_risk_drift"):
            qualification_failures.append("high_risk_drift")
    blocker_codes: list[str] = []
    if layer in NON_FACTUAL_LAYERS or non_governed:
        blocker_codes.append("non_factual_layer")
    if receipt is None and not non_governed:
        blocker_codes.append("receipt_missing_or_stale")
    if object_type == "claim" and metadata.get("evidence_entailment", "unknown") != "passed":
        blocker_codes.append("semantic_entailment_unverified")
    if semantic_failures:
        blocker_codes.append("semantic_entailment_unverified")
    if tier == "trusted" and not policy_qualified:
        blocker_codes.append("policy_not_qualified")
    if metadata.get("needs_policy_requalification"):
        blocker_codes.append("awaiting_requalification")
    if contradictions:
        blocker_codes.append("unresolved_contradiction")
    if metadata.get("extraction_quality") in {"degraded", "failed"}:
        blocker_codes.append("degraded_extraction")
    if not execution_safe and not blocker_codes:
        blocker_codes.append("insufficient_execution_evidence")
    return {
        "truth_layer": layer,
        "memory_tier": tier,
        "epistemic_status": epistemic,
        "governance": {
            "receipt_state": "not_applicable" if non_governed else ("current_v2" if receipt else "missing_or_stale"),
            "receipt_current": None if non_governed else receipt is not None,
            "policy_qualified": policy_qualified,
            "qualification_scope": metadata.get("qualification_scope"),
            "qualification_failures": list(dict.fromkeys(qualification_failures)),
            "last_consolidated_at": metadata.get("last_consolidated_at"),
        },
        "contradictions": {"unresolved": contradictions},
        "execution": {"safe": execution_safe, "blocker_codes": list(dict.fromkeys(blocker_codes))},
    }


def evidence_item_from_context(item: dict[str, Any]) -> dict[str, Any]:
    governance = {
        "receipt_state": item.get("receipt_state"),
        "receipt_current": item.get("receipt_current"),
        "policy_qualified": bool(item.get("policy_qualified", False)),
        "qualification_scope": item.get("qualification_scope"),
        "qualification_failures": list(item.get("qualification_failures", [])),
        "last_consolidated_at": item.get("last_consolidated_at"),
    }
    unresolved = list(item.get("unresolved_contradictions", []))
    blocker_codes: list[str] = []
    if item.get("truth_layer") in NON_FACTUAL_LAYERS or item.get("type") in NON_GOVERNED_TYPES:
        blocker_codes.append("non_factual_layer")
    if item.get("receipt_current") is False:
        blocker_codes.append("receipt_missing_or_stale")
    failures = governance["qualification_failures"]
    if any("entailment" in str(value) or "independence" in str(value) for value in failures):
        blocker_codes.append("semantic_entailment_unverified")
    if item.get("type") == "claim" and item.get("evidence_entailment", "unknown") != "passed":
        blocker_codes.append("semantic_entailment_unverified")
    if "awaiting_requalification" in failures:
        blocker_codes.append("awaiting_requalification")
    if unresolved:
        blocker_codes.append("unresolved_contradiction")
    if not item.get("execution_safe") and not blocker_codes:
        blocker_codes.append("insufficient_execution_evidence")
    interpretation = None
    for key in ("annotation", "reflection", "cognitive_synthesis"):
        if item.get(key):
            interpretation = {"kind": key, "value": item[key]}
            break
    result = {
        "evidence_item_version": EVIDENCE_ITEM_VERSION,
        "lookup_ref": item.get("id"),
        "title": item.get("title"),
        "object_type": item.get("type"),
        "knowledge_status": item.get("knowledge_status"),
        "truth_layer": item.get("truth_layer"),
        "memory_tier": item.get("memory_tier"),
        "epistemic_status": item.get("epistemic_status"),
        "confidence": item.get("confidence"),
        "content": item.get("content", item.get("snippet", "")),
        "source_refs": list(item.get("source_ids", [])),
        "evidence": public_evidence(item.get("evidence", [])),
        "verification": {
            "source_authority": item.get("source_authority"),
            "extraction_quality": (item.get("verification") or {}).get("extraction_quality"),
            "quote_verification": (item.get("verification") or {}).get("quote_verification"),
            "evidence_coverage": item.get("evidence_coverage"),
            "evidence_entailment": item.get("evidence_entailment"),
        },
        "governance": governance,
        "contradictions": {"unresolved": unresolved},
        "execution": {
            "safe": bool(item.get("execution_safe", False)),
            "blocker_codes": list(dict.fromkeys(blocker_codes)),
        },
    }
    if interpretation:
        result["interpretation"] = interpretation
    return _compatibility_fields(result)


def evidence_item_from_document(
    repository: Repository,
    path: Path,
    metadata: dict[str, Any],
    content: str,
) -> dict[str, Any]:
    snapshot = governance_snapshot(repository, path, metadata)
    source_ids = [str(item) for item in metadata.get("source_ids", [])]
    if metadata.get("type") == "source":
        source_ids = [str(metadata.get("id"))]
    result = {
        "evidence_item_version": EVIDENCE_ITEM_VERSION,
        "lookup_ref": metadata.get("id"),
        "title": metadata.get("title"),
        "object_type": metadata.get("type"),
        "knowledge_status": metadata.get("status"),
        "truth_layer": snapshot["truth_layer"],
        "memory_tier": snapshot["memory_tier"],
        "epistemic_status": snapshot["epistemic_status"],
        "confidence": metadata.get("claim_confidence", metadata.get("confidence", "unknown")),
        "content": content,
        "source_refs": source_ids,
        "evidence": public_evidence(metadata.get("evidence", [])),
        "verification": {
            "source_authority": metadata.get("source_authority"),
            "extraction_quality": metadata.get("extraction_quality", "unknown"),
            "quote_verification": metadata.get("quote_verification", "not_applicable"),
            "evidence_coverage": metadata.get("evidence_coverage"),
            "evidence_entailment": metadata.get("evidence_entailment", "unknown"),
        },
        "governance": snapshot["governance"],
        "contradictions": snapshot["contradictions"],
        "execution": snapshot["execution"],
    }
    layer = snapshot["truth_layer"]
    if layer == "user_annotation":
        result["interpretation"] = {"kind": "annotation", "value": {
            key: metadata.get(key) for key in (
                "annotation_kind", "target_ids", "why_saved", "what_surprised_me",
                "possible_connections", "feedback_label", "feedback_note",
            )
        }}
    elif layer == "reflection":
        result["interpretation"] = {"kind": "reflection", "value": {
            key: metadata.get(key) for key in (
                "why_important", "what_changed", "connections", "conflicts", "open_questions",
            )
        }}
    elif layer == "cognitive_synthesis":
        result["interpretation"] = {"kind": "cognitive_synthesis", "value": {
            key: metadata.get(key) for key in (
                "scope_kind", "scope_ids", "candidate_window", "delta_kind",
                "emerging_patterns", "new_connections", "unresolved_tensions", "candidate_hypotheses",
            )
        }}
    return _compatibility_fields(result)


def _compatibility_fields(item: dict[str, Any]) -> dict[str, Any]:
    """Keep one compatibility window while clients move to nested contract fields."""
    governance = item["governance"]
    execution = item["execution"]
    contradictions = item["contradictions"]
    item.update({
        "source_authority": item["verification"].get("source_authority"),
        "evidence_coverage": item["verification"].get("evidence_coverage"),
        "evidence_entailment": item["verification"].get("evidence_entailment"),
        "receipt_state": governance.get("receipt_state"),
        "receipt_current": governance.get("receipt_current"),
        "policy_qualified": governance.get("policy_qualified"),
        "qualification_scope": governance.get("qualification_scope"),
        "qualification_failures": governance.get("qualification_failures", []),
        "last_consolidated_at": governance.get("last_consolidated_at"),
        "unresolved_contradictions": contradictions.get("unresolved", []),
        "execution_safe": execution.get("safe", False),
    })
    return item


def blocker_code(reason: str) -> str:
    lowered = reason.casefold()
    if "contradiction" in lowered:
        return "unresolved_contradiction"
    if "requalification" in lowered:
        return "awaiting_requalification"
    if "semantic" in lowered or "entailment" in lowered or "independence" in lowered:
        return "semantic_entailment_unverified"
    if "receipt" in lowered:
        return "receipt_missing_or_stale"
    if "degraded" in lowered or "extraction" in lowered:
        return "degraded_extraction"
    if "profile trust policy" in lowered:
        return "policy_not_qualified"
    return "insufficient_execution_evidence"
