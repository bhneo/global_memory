from __future__ import annotations

import argparse
import json
from pathlib import Path

from global_memory.cli import doctor, lint
from global_memory.cognition import (
    DailyDreamService, InputEpisodeService, ReflectionService, WeeklyDreamService,
)
from global_memory.context import ContextPackService
from global_memory.markdown import atomic_write_text, read_document
from global_memory.metrics import ProjectMetricsService
from global_memory.raw_store import RawStoreService
from global_memory.repository import Repository, sha256_bytes


def _reflection(title: str, changed: str, surprising: str) -> dict[str, object]:
    return {
        "title": title,
        "created_by": "agent",
        "reflection_kind": "idea",
        "importance": "high",
        "why_important": (
            "It changes how expensive embodied reasoning is understood: reusable execution "
            "may be a governed consolidation product rather than only a larger runtime policy."
        ),
        "what_changed": changed,
        "surprising": surprising,
        "connections": [{
            "shared_mechanism": "expensive deliberation is consolidated into a reusable fast path",
            "boundary": "the connection concerns amortized computation, not identical implementations",
            "difference": "human habits are biological while robot skill artifacts are engineered",
        }],
        "conflicts": ["compression may hide adaptation failures when the environment changes"],
        "open_questions": ["Which typed validation boundary makes the fast path safely reusable?"],
        "possible_mechanisms": ["typed preconditions, postconditions and invalidation signals"],
        "future_directions": ["measure transfer under explicit skill validation contracts"],
        "confidence": "medium",
    }


def _truth_snapshot(repo: Repository) -> dict[str, object]:
    metrics = ProjectMetricsService(repo).collect()
    return {
        "working": metrics["working"],
        "trusted": metrics["trusted"],
        "canonical": metrics["canonical"],
        "canonical_hashes": {
            repo.rel(path): sha256_bytes(path.read_bytes())
            for path in sorted(repo.canonical_documents())
        },
    }


def run(root: Path) -> dict[str, object]:
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"refusing to reuse non-empty demo root: {root}")
    repo = Repository(root)
    repo.init()
    inputs = InputEpisodeService(repo)
    reflections = ReflectionService(repo)
    before = _truth_snapshot(repo)

    skill = inputs.capture_idea(
        "Robot skill compilation can consolidate expensive planning into a validated fast execution path.",
        title="Robot skill compilation",
    )
    habit = inputs.capture_idea(
        "Human habits consolidate repeated deliberation into fast routines that require invalidation when context changes.",
        title="Human habit consolidation",
    )
    skill_input_id = str(skill["input"]["object_id"])
    habit_input_id = str(habit["input"]["object_id"])

    daily_bundle = root / "data" / "derived" / "m91-daily-dream.json"
    atomic_write_text(daily_bundle, json.dumps({
        "provider_name": "gpt-5.6-terra-light",
        "reflections": [{
            "input_id": skill_input_id,
            "reflection": _reflection(
                "Reflection on compiled robot skills",
                "Previously reuse was treated as policy caching; now it includes a typed validation boundary.",
                "Compression and validation may need to be designed as one interface.",
            ),
            "semantic_items": [{
                "object_type": "concept",
                "title": "Validated compiled robot skill",
                "body": (
                    "A validated compiled robot skill consolidates expensive planning into a reusable "
                    "execution path with explicit preconditions, postconditions and invalidation signals."
                ),
                "metadata": {
                    "aliases": ["经验证的机器人技能编译", "validated skill compilation"],
                    "domains": ["embodied-ai", "robot-learning"],
                    "confidence": "medium",
                },
            }],
        }],
    }, ensure_ascii=False, indent=2) + "\n")
    daily = DailyDreamService(repo).run(daily_bundle, limit=5)
    daily_retry = DailyDreamService(repo).run(daily_bundle, limit=5)
    daily_concept, _ = read_document(repo.root / str(daily["working_written"][0]))
    daily_concept_id = str(daily_concept["id"])

    habit_reflection = reflections.create(
        habit_input_id,
        _reflection(
            "Reflection on habit consolidation",
            "Previously habits were only behavioral repetition; now they are also an amortization mechanism with invalidation needs.",
            "Biological habits and robot skills share a failure-sensitive fast-path structure.",
        ),
    )
    reflection_ids = [str(daily["reflection_ids"][0]), habit_reflection.object_id]
    source_ids: list[str] = []
    for reflection_id in reflection_ids:
        _, metadata, _ = repo.find_document(reflection_id)
        source_ids.extend(str(item) for item in metadata.get("source_ids", []))

    weekly_bundle = root / "data" / "derived" / "m91-weekly-dream.json"
    atomic_write_text(weekly_bundle, json.dumps({
        "provider_name": "gpt-5.6-sol-high",
        "synthesis": {
            "title": "Failure-sensitive cognitive consolidation",
            "period": "2026-W29",
            "input_reflections": reflection_ids,
            "input_concepts": [daily_concept_id],
            "emerging_patterns": [
                "slow expensive reasoning is consolidated into a fast path whose safety depends on invalidation"
            ],
            "knowledge_updates": [{
                "target_id": daily_concept_id,
                "previous": "skill reuse is primarily action caching",
                "proposed": "skill reuse may require a typed validation and invalidation boundary",
                "reason": "the two reflections expose a shared failure-sensitive fast path",
                "change_type": "refine",
                "supporting_reflections": reflection_ids,
                "supporting_sources": sorted(set(source_ids)),
            }],
            "new_connections": [{
                "shared_mechanism": "slow deliberation is amortized into a reusable fast path",
                "boundary": "the pattern concerns computation reuse and invalidation only",
                "difference": "human consolidation is biological while robot compilation is explicit engineering",
            }],
            "unresolved_tensions": [
                "more compression improves speed but can delay detection of distribution shift"
            ],
            "candidate_hypotheses": [{
                "statement": "Typed invalidation improves cross-context portability of compiled robot skills.",
                "supporting_patterns": ["slow-to-fast consolidation with failure-sensitive invalidation"],
                "supporting_reflections": reflection_ids,
                "supporting_sources": sorted(set(source_ids)),
                "counter_arguments": ["portability may depend mainly on embodiment alignment rather than invalidation"],
                "falsifier": "typed invalidation produces no transfer improvement across two changed contexts",
                "possible_experiment": "compare transfer success with and without typed invalidation contracts",
            }],
            "possible_experiments": [
                "evaluate two embodiments under matched and shifted precondition distributions"
            ],
            "confidence": "medium",
        },
        "knowledge_bundles": [{
            "source_id": source_ids[0],
            "reflection_ids": [reflection_ids[0]],
            "items": [{
                "object_type": "concept",
                "title": "Failure-sensitive execution consolidation",
                "body": (
                    "Execution consolidation amortizes expensive reasoning while retaining explicit "
                    "signals that invalidate the reusable fast path when its boundary no longer holds."
                ),
                "metadata": {"confidence": "medium", "domains": ["embodied-ai", "cognitive-systems"]},
            }],
        }],
    }, ensure_ascii=False, indent=2) + "\n")
    weekly = WeeklyDreamService(repo).run(weekly_bundle)

    research = ContextPackService(repo).build(
        "failure-sensitive skill consolidation invalidation",
        profiles=["research"], token_budget=2_000,
    ).as_dict()
    execution = ContextPackService(repo).build(
        "failure-sensitive skill consolidation invalidation",
        profiles=["execution"], token_budget=2_000,
    ).as_dict()
    research_types = {str(item["type"]) for item in research["items"]}
    execution_types = {str(item["type"]) for item in execution["items"]}

    session_path = root / "data" / "imports" / "agent-session.json"
    atomic_write_text(session_path, json.dumps({
        "goal": "validate M9.1 context isolation",
        "result": "success",
        "lesson": "Reflection and Cognitive Synthesis must remain outside Execution Context.",
    }, ensure_ascii=False, indent=2) + "\n")
    knowledge_before_session = len(list(repo.memory_documents()))
    session = inputs.import_agent_session(session_path, agent="codex")
    knowledge_after_session = len(list(repo.memory_documents()))

    _, synthesis, _ = repo.find_document(str(weekly["synthesis_id"]))
    working_documents = [read_document(path)[0] for path in repo.memory_documents()]
    weekly_working, _ = read_document(repo.root / str(weekly["working_created"][0]))
    reflection_context_bound = all(
        bool(item.get("reflection_context", {}).get("reflection_ids"))
        for item in working_documents
    )
    after = _truth_snapshot(repo)
    doctor_result = doctor(repo)
    lint_result = lint(repo)
    raw_result = RawStoreService(repo).verify()
    counts = repo.count_by_type()
    checks = {
        "input_layer_created": counts.get("input", 0) == 3,
        "reflections_created": counts.get("reflection", 0) == 2,
        "daily_working_only": daily["concepts_created"] == 1 and daily["canonical_writes"] == 0,
        "daily_restartable": (
            daily_retry["reflections_created"] == 0
            and daily_retry["reflections_reused"] == 1
            and daily_retry["working_written"] == []
        ),
        "weekly_synthesis_created": counts.get("synthesis", 0) == 1,
        "weekly_working_only": len(weekly["working_created"]) == 1 and weekly["canonical_writes"] == 0,
        "hypothesis_is_nonfactual": (
            synthesis.get("candidate_hypotheses", [{}])[0].get("epistemic_status") == "hypothetical"
            and "memory_tier" not in synthesis
            and "epistemic_status" not in synthesis
        ),
        "reflection_context_bound": reflection_context_bound,
        "weekly_provenance_is_precise": (
            weekly_working.get("reflection_context", {}).get("reflection_ids")
            == [reflection_ids[0]]
        ),
        "research_includes_cognitive_layers": {"reflection", "synthesis"} <= research_types,
        "execution_excludes_nonvalidated_layers": not (
            {"source", "input", "reflection", "synthesis", "annotation"} & execution_types
        ),
        "agent_session_writes_no_knowledge": (
            session["knowledge_writes"] == 0 and knowledge_before_session == knowledge_after_session
        ),
        "trusted_unchanged": before["trusted"] == after["trusted"],
        "canonical_unchanged": (
            before["canonical"] == after["canonical"]
            and before["canonical_hashes"] == after["canonical_hashes"]
        ),
        "doctor": doctor_result["ok"],
        "lint": lint_result["ok"],
        "raw": raw_result["ok"],
    }
    return {
        "ok": all(checks.values()),
        "checks": checks,
        "daily": daily,
        "daily_retry": daily_retry,
        "weekly": weekly,
        "session": session,
        "context": {
            "research_types": sorted(research_types),
            "execution_types": sorted(execution_types),
            "research_selected": [item["id"] for item in research["items"]],
            "execution_selected": [item["id"] for item in execution["items"]],
        },
        "truth_before": before,
        "truth_after": after,
        "counts": counts,
        "health": {"doctor": doctor_result, "lint": lint_result, "raw": raw_result},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.root.resolve())
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
