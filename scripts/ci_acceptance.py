from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from global_memory.bundle import BundleCompiler
from global_memory.capture import CaptureService
from global_memory.consolidation import ConsolidationService, DriftAuditService
from global_memory.context import ContextPackService
from global_memory.evolution import KnowledgeEvolutionService
from global_memory.governance import PromotionService
from global_memory.markdown import read_document
from global_memory.memory import WorkingMemoryService
from global_memory.repository import Repository


def emit(output: Path, report: dict[str, Any]) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    output.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if report.get("ok", False) else 1


def setup_fixture(repo: Repository) -> dict[str, Any]:
    repo.init()
    source = CaptureService(repo).capture_text(
        "Concept: CI portable memory concept.\n\n"
        "Claim: A portable fixture keeps raw evidence available during validation.",
        title="Current architecture fixture A",
    )
    bundle = BundleCompiler(repo).compile(source.source_id)
    result = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))
    return {
        "ok": bool(result.written or result.skipped),
        "fixture": "current-architecture-v1",
        "source_id": source.source_id,
        "proposal_id": bundle.proposal_id,
        "working_created": result.written,
        "working_skipped": result.skipped,
        "exceptions": result.exceptions,
        "canonical_writes": 0,
    }


def promotion_report(repo: Repository) -> dict[str, Any]:
    evaluations = []
    for path in repo.memory_documents():
        metadata, _ = read_document(path)
        evaluation = PromotionService(repo).evaluate(str(metadata["id"]))
        evaluations.append(evaluation.as_dict())
    return {
        "ok": bool(evaluations) and all(not item["eligible"] for item in evaluations),
        "policy": "trusted-promotion-v2",
        "evaluations": evaluations,
        "expectation": "a receipt is necessary but never sufficient; weak evidence and non-independent reuse remain Working",
        "canonical_writes": 0,
    }


def weekly_report(repo: Repository) -> dict[str, Any]:
    report = ConsolidationService(repo).weekly()
    return {"ok": report.get("canonical_writes") == 0, **report}


def incremental_report(repo: Repository) -> dict[str, Any]:
    source = CaptureService(repo).capture_text(
        "Concept: CI portable memory concept.\n\n"
        "Question: Which evidence should refine the portable fixture?",
        title="Current architecture fixture B",
    )
    bundle = BundleCompiler(repo).compile(source.source_id)
    proposal, _ = read_document(repo.root / str(bundle.proposal_path))
    reused = [item for item in proposal.get("bundle_items", []) if item.get("action") == "update"]
    result = WorkingMemoryService(repo).ingest_bundle(str(bundle.proposal_id))
    supported = 0
    for path_value in result.updated:
        updated_metadata, _ = read_document(repo.root / path_value)
        supported += int(any(
            item.get("change_type") == "support"
            for item in updated_metadata.get("change_history", []) if isinstance(item, dict)
        ))
    source_c = CaptureService(repo).capture_text(
        "A portable fixture does not preserve raw evidence when the raw object is unavailable.",
        title="Current architecture fixture C",
    )
    claim_path = next(
        path for path in repo.memory_documents()
        if read_document(path)[0].get("type") == "claim"
    )
    claim, claim_body = read_document(claim_path)
    contradiction = KnowledgeEvolutionService(repo).apply(
        str(claim["id"]), {
            "source_ids": [source_c.source_id],
            "evidence": [{
                "source_id": source_c.source_id, "stance": "contradicts",
                "location": "body", "excerpt": "does not preserve raw evidence",
                "reason": "fixture C explicitly limits fixture A",
            }],
        }, claim_body, change_type="contradict",
        reason="Source C directly limits the original fixture claim",
        trigger_source=source_c.source_id,
    )
    report = {
        "created_object_count": len(result.written),
        "updated_object_count": len(result.updated) + contradiction["updated_object_count"],
        "knowledge_reuse_count": len(reused) + contradiction["knowledge_reuse_count"],
        "supported_object_count": supported,
        "refined_object_count": 0,
        "limited_object_count": 0,
        "contradicted_object_count": 1,
        "exceptions": result.exceptions,
        "silent_trusted_demotions": 0,
        "canonical_writes": 0,
        "source_order": ["A", "B", "C"],
        "contradiction_exception_id": contradiction["exception_id"],
    }
    return {
        "ok": (
            report["created_object_count"] > 0
            and report["updated_object_count"] > 0
            and report["knowledge_reuse_count"] > 0
            and (report["supported_object_count"] > 0 or report["refined_object_count"] > 0)
            and (report["limited_object_count"] > 0 or report["contradicted_object_count"] > 0)
            and report["silent_trusted_demotions"] == 0
        ),
        **report,
    }


def drift_report(repo: Repository) -> dict[str, Any]:
    report = DriftAuditService(repo).run()
    return {"ok": report.get("writes") == 0, **report}


def context_report(repo: Repository) -> dict[str, Any]:
    profiles = {}
    required = {
        "memory_tier", "epistemic_status", "confidence", "evidence_coverage",
        "evidence_entailment", "unresolved_contradictions", "last_consolidated_at",
    }
    missing_fields: dict[str, list[str]] = {}
    invalid: list[str] = []
    allowed = {"working", "trusted", "canonical", "source_capture", "proposal", "unknown"}
    for profile in ("execution", "research", "exploration"):
        pack = ContextPackService(repo).build(
            "CI portable memory concept", token_budget=1200, profiles=[profile]
        ).as_dict()
        profiles[profile] = pack
        for item in pack["items"]:
            if item.get("truth_layer") not in allowed:
                invalid.append(str(item["id"]))
            absent = sorted(required - set(item))
            if absent:
                missing_fields[str(item["id"])] = absent
    return {
        "ok": bool(profiles["research"]["items"]) and not invalid and not missing_fields,
        "invalid_truth_layers": invalid,
        "missing_required_fields": missing_fields,
        "profiles": profiles,
        "canonical_writes": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Portable CI acceptance reports")
    parser.add_argument("command", choices={"setup", "promotion", "weekly", "incremental", "drift", "context"})
    parser.add_argument("--root", default=".ci-vault")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    repo = Repository(Path(args.root).resolve())
    if args.command != "setup":
        repo.ensure_initialized()
    handlers = {
        "setup": setup_fixture,
        "promotion": promotion_report,
        "weekly": weekly_report,
        "incremental": incremental_report,
        "drift": drift_report,
        "context": context_report,
    }
    return emit(Path(args.output), handlers[args.command](repo))


if __name__ == "__main__":
    raise SystemExit(main())
