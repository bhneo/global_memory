"""Validate and record a model-independent Discovery Benchmark fixture."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

try:
    import yaml  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover
    yaml = None


def load_yaml(path: Path) -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML is required to read the benchmark fixture")
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"invalid YAML document: {path}")
    return value


def _ratio(numerator: int, denominator: int) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def evaluate_case(case: dict, run: dict) -> dict:
    retrieved = [str(item) for item in run.get("retrieved_source_ids", [])]
    relevant = {str(item) for item in case["relevant_sources"]}
    connections = [item for item in run.get("connections", []) if isinstance(item, dict)]
    expected_mechanisms = {str(item).casefold() for item in case["expected_mechanisms"]}
    reported_mechanisms = {str(item).casefold() for item in run.get("mechanisms", [])}
    required_boundaries = {str(item).casefold() for item in case["required_boundaries"]}
    reported_boundaries = {str(item).casefold() for item in run.get("boundaries", [])}
    supported = sum(item.get("evidence_supported") is True for item in connections)
    false_analogies = sum(item.get("known_false_analogy") is True for item in connections)
    abstained = run.get("abstained") is True
    zero_expected = not relevant
    objective = {
        "relevant_source_recall_at_k": _ratio(len(relevant.intersection(retrieved)), len(relevant)),
        "connection_precision": _ratio(supported, len(connections)),
        "false_analogy_rate": _ratio(false_analogies, len(connections)),
        "mechanism_correctness": _ratio(len(expected_mechanisms & reported_mechanisms), len(expected_mechanisms)),
        "boundary_completeness": _ratio(len(required_boundaries & reported_boundaries), len(required_boundaries)),
        "evidence_support_accuracy": _ratio(supported, len(connections)),
        "abstention_quality": 1.0 if abstained == zero_expected else 0.0,
        "zero_connection_correctness": 1.0 if (not connections) == zero_expected else 0.0,
    }
    subjective = {
        key: run.get("human_scores", {}).get(key)
        for key in ("novelty", "actionability")
    }
    return {"case_id": case["case_id"], "objective_metrics": objective, "human_metrics": subjective}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", choices=["synthetic"], required=True)
    parser.add_argument("--system", default="galois_governed_context")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--responses", type=Path, help="JSON run records to score without binding a model SDK")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    schema = load_yaml(root / "release" / "discovery_benchmark_schema.yaml")
    cases = load_yaml(root / "release" / "discovery_cases.yaml").get("cases", [])
    required = set(schema["required_fields"])
    invalid = [case.get("case_id", "<missing>") for case in cases if not required <= set(case)]
    if len(cases) < 5 or invalid:
        raise RuntimeError(f"invalid benchmark: cases={len(cases)}, missing_fields={invalid}")
    report = {
        "benchmark_schema_version": schema["schema_version"], "fixture": args.fixture,
        "system": args.system, "case_count": len(cases),
        "cases": [{"case_id": case["case_id"], "expected_zero_connection": not case["relevant_sources"]} for case in cases],
        "metrics": schema["metrics"], "recording_contract": schema["run_record"],
        "timestamp": dt.datetime.now(dt.UTC).isoformat(),
        "result": "fixture_validated_only; no model claim or score was produced",
    }
    if args.responses:
        payload = json.loads(args.responses.read_text(encoding="utf-8"))
        runs = payload.get("runs", []) if isinstance(payload, dict) else []
        by_case = {str(case["case_id"]): case for case in cases}
        required_record = set(schema["run_record"])
        missing = [
            str(run.get("case_id", "<missing>")) for run in runs
            if not required_record <= set(run)
        ]
        unknown = [str(run.get("case_id")) for run in runs if str(run.get("case_id")) not in by_case]
        if missing or unknown:
            raise RuntimeError(f"invalid run records: missing_contract={missing}, unknown_cases={unknown}")
        report["evaluations"] = [evaluate_case(by_case[str(run["case_id"])], run) for run in runs]
        report["run_records"] = runs
        report["result"] = "recorded_and_scored; subjective metrics remain human-evaluator supplied"
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
