from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


ATOMICITY_STATUSES = {"atomic", "compound", "uncertain"}
EVIDENCE_COVERAGE = {"full", "partial", "missing"}
_CONNECTOR = re.compile(r"(?:；|;|，(?:并且|并|同时|以及|此外|还)|\s+(?:and|as well as|while also)\s+)", re.I)
_FRAGMENT_END = re.compile(
    r"(?:,|:|;|\b(?:and|or|but|with|without|of|for|to|from|than|respectively)\.?)$",
    re.I,
)
_HEADING_LIKE = re.compile(
    r"^(?:experimental results(?: in (?:simulation|the real world))?|results|discussion|conclusion|predictive capability)\.?$",
    re.I,
)


@dataclass(frozen=True)
class AtomicityResult:
    status: str
    clauses: list[str]
    evidence_coverage: str
    reason: str


class AtomicClaimInspector:
    @staticmethod
    def is_semantically_self_contained(statement: str) -> bool:
        """Conservatively reject headings and sentence fragments as Claims."""
        text = re.sub(r"\s+", " ", statement).strip()
        if not text or _HEADING_LIKE.fullmatch(text) or _FRAGMENT_END.search(text):
            return False
        if text[0].isascii() and text[0].islower():
            return False
        latin_words = re.findall(r"[A-Za-z0-9πΦ][A-Za-z0-9_.+@×%-]*", text)
        if latin_words and len(latin_words) < 5 and not re.search(r"[\u3400-\u9fff]", text):
            return False
        return len(text) >= 10

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
        if result.status == "compound":
            return [{
                **spec,
                "atomicity_status": "compound",
                "evidence_coverage": result.evidence_coverage,
                "semantic_completeness": "complete",
                "split_reason": "automatic syntactic splitting disabled; explicit semantic split required",
            }]
        complete = bool(spec.get("explicit_marker")) or AtomicClaimInspector.is_semantically_self_contained(body)
        return [{
            **spec,
            "atomicity_status": result.status if complete else "uncertain",
            "evidence_coverage": result.evidence_coverage if complete else "missing",
            "semantic_completeness": "complete" if complete else "fragment",
            "quality_gate_reason": None if complete else "claim is not a self-contained proposition",
        }]
