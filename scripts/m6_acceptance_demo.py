from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from global_memory.atomicity import AtomicClaimInspector
from global_memory.cli import doctor, lint
from global_memory.context import ContextPackService
from global_memory.markdown import read_document
from global_memory.quality import SourceQualityService
from global_memory.repository import Repository, sha256_bytes


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description="M6 real-corpus acceptance")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    repo = Repository(Path(args.root).resolve())
    repo.ensure_initialized()

    corpus = []
    for path in repo.proposal_documents():
        metadata, body = read_document(path)
        if metadata.get("proposal_kind") == "corpus_distillation" and metadata.get("status") == "pending":
            corpus.append((path, metadata, body))
    require(len(corpus) == 1, "expected exactly one pending M6 corpus bundle")
    bundle_path, bundle, _ = corpus[0]

    candidates = []
    for item in bundle.get("bundle_items", []):
        if item.get("decision") == "superseded":
            continue
        candidate_path = repo.resolve_inside(str(item["candidate_path"]))
        candidate, body = read_document(candidate_path)
        candidates.append((item, candidate, body))
    counts = Counter(candidate["type"] for _, candidate, _ in candidates)

    invalid = []
    for path in repo.source_documents():
        source, _ = read_document(path)
        assessment = SourceQualityService(repo).assess(str(source["id"]), persist=False)
        if not assessment.compile_allowed:
            invalid.append(assessment)
    require(invalid and all(item.availability_status != "available" or item.content_quality != "valid" for item in invalid), "invalid source gate failed")

    compound = AtomicClaimInspector.split_spec(
        {"object_type": "claim", "title": "compound", "body": "The model uses a planner and it uses a verifier and it records a trace."},
        "The model uses a planner and it uses a verifier and it records a trace.",
    )
    require(len(compound) >= 2 and all(item["atomicity_status"] == "atomic" for item in compound), "compound split failed")
    require(any(item.get("evidence_coverage") == "partial" for item, _, _ in candidates if item.get("object_type") == "claim"), "partial evidence was not retained")

    concept_candidates = [candidate for _, candidate, _ in candidates if candidate.get("type") == "concept"]
    require(len({candidate["id"] for candidate in concept_candidates}) == len(concept_candidates), "duplicate concept ids")
    require(any(len(candidate.get("source_ids", [])) >= 2 for candidate in concept_candidates), "no multi-source concept reuse")
    require(counts["tension"] >= 1 and counts["question"] >= 1, "tension/question missing")
    require(len(bundle.get("primary_source_followups", [])) >= 1, "primary-source follow-up missing")
    require(counts["analogy"] >= 3 and counts["synthesis"] >= 2, "graph distillation targets missing")
    require(all(candidate.get("status") == "proposal" for _, candidate, _ in candidates), "candidate escaped proposal layer")
    canonical_ids = set()
    for path in repo.canonical_documents():
        metadata, _ = read_document(path)
        canonical_ids.add(str(metadata["id"]))
    require(not (canonical_ids & {str(candidate["id"]) for _, candidate, _ in candidates}), "M6 wrote candidate into canonical")

    context = ContextPackService(repo).build(
        "Epiplexity", token_budget=1600, profiles=["exploration"], include_proposals=True,
    ).as_dict()
    selected_types = {item["type"] for item in context["items"]}
    require({"concept", "claim", "analogy"} <= selected_types, "Context Pack did not prioritize typed knowledge")
    require(all(item["truth_layer"] in {"proposal", "canonical", "source_capture"} for item in context["items"]), "truth layer missing")

    truth_paths = [*repo.canonical_documents(), *repo.proposal_documents()]
    before = {repo.rel(path): sha256_bytes(path.read_bytes()) for path in truth_paths}
    repo.index_path.unlink(missing_ok=True)
    repo.rebuild_index()
    after = {repo.rel(path): sha256_bytes(path.read_bytes()) for path in truth_paths}
    require(before == after, "rebuild changed canonical or proposal truth")
    doctor_result = doctor(repo)
    lint_result = lint(repo)
    require(doctor_result["ok"], f"doctor failed: {doctor_result['issues']}")
    require(lint_result["ok"], f"lint failed: {lint_result['errors']}")

    output = {
        "ok": True,
        "bundle_id": bundle["id"],
        "bundle_path": repo.rel(bundle_path),
        "demos": {
            "invalid_source": len(invalid),
            "compound_split_children": len(compound),
            "concept_reuse": len(concept_candidates),
            "tensions": counts["tension"],
            "primary_followups": len(bundle.get("primary_source_followups", [])),
            "bundle_items": len(candidates),
            "graph_node_counts": dict(sorted(counts.items())),
            "context_types": sorted(selected_types),
            "rebuild_and_consistency": True,
        },
        "doctor": doctor_result,
        "lint": {"ok": lint_result["ok"], "checked_documents": lint_result["checked_documents"]},
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
