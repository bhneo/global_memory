from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


ATOMICITY_STATUSES = {"atomic", "compound", "uncertain"}
EVIDENCE_COVERAGE = {"full", "partial", "missing"}
_CONNECTOR = re.compile(r"(?:；|;|，(?:并且|并|同时|以及|此外|还)|\s+(?:and|as well as|while also)\s+)", re.I)


@dataclass(frozen=True)
class AtomicityResult:
    status: str
    clauses: list[str]
    evidence_coverage: str
    reason: str


class AtomicClaimInspector:
    @staticmethod
    def inspect(statement: str, evidence_texts: list[str] | None = None) -> AtomicityResult:
        text = re.sub(r"\s+", " ", statement).strip()
        clauses = [item.strip(" ，。;；") for item in _CONNECTOR.split(text) if item.strip(" ，。;；")]
        clauses = [item for item in clauses if len(item) >= 6]
        compound = len(clauses) > 1
        evidence_texts = [item for item in (evidence_texts or []) if item]
        if not evidence_texts:
            coverage = "missing"
        else:
            covered = [any(clause in evidence or evidence in clause for evidence in evidence_texts) for clause in (clauses or [text])]
            # String containment can prove full coverage, but absence of containment does
            # not prove no semantic support. Existing evidence is therefore partial until
            # a human/model entailment review explicitly upgrades it.
            coverage = "full" if all(covered) else "partial"
        return AtomicityResult(
            status="compound" if compound else "atomic", clauses=clauses or [text],
            evidence_coverage=coverage,
            reason="multiple independently testable clauses" if compound else "single principal assertion",
        )

    @staticmethod
    def split_spec(spec: dict[str, Any], extraction_text: str) -> list[dict[str, Any]]:
        if str(spec.get("object_type")) != "claim":
            return [spec]
        body = str(spec.get("body", ""))
        result = AtomicClaimInspector.inspect(body, [body] if body in extraction_text else [])
        if result.status != "compound":
            return [{**spec, "atomicity_status": result.status, "evidence_coverage": result.evidence_coverage}]
        split: list[dict[str, Any]] = []
        for clause in result.clauses:
            start = extraction_text.find(clause)
            split.append({
                **spec, "title": clause[:160], "body": clause, "span_start": start,
                "atomicity_status": "atomic", "evidence_coverage": "full" if start >= 0 else "partial",
                "split_from": body, "split_reason": result.reason,
            })
        return split
