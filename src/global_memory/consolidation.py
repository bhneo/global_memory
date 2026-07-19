from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, TypedDict

from .bundle import BundleCompiler, DeterministicCompilerProvider
from .extraction import ExtractionService
from .errors import ValidationError
from .governance import POLICY_VERSION, PromotionService
from .markdown import atomic_write_text, read_document, render_document
from .memory import ExceptionService, WorkingMemoryService
from .proposals import ProposalService
from .repository import Repository, now_iso, sha256_bytes
from .triage import DailyTriageService


CONSOLIDATOR_VERSION = "trustworthy-consolidation-v2"
RECEIPT_SCHEMA_VERSION = 2
DRIFT_POLICY_VERSION = "semantic-drift-v2"
REQUIRED_RECEIPT_CHECKS = {
    "schema_validated", "raw_available", "provenance_revalidated",
    "evidence_revalidated", "evidence_entailment_rechecked",
    "duplicate_search_completed", "related_object_search_completed",
    "contradiction_search_completed", "freshness_checked",
    "source_independence_checked", "drift_checked",
}


class DriftReport(TypedDict):
    drift_report_id: str
    object_id: str
    object_versions_compared: list[str]
    source_evidence_ids: list[str]
    drift_type: str
    severity: str
    original_statement: str
    current_statement: str
    evidence_summary: str
    reason: str
    recommended_action: str


class ConsolidationReceiptService:
    """Create immutable, hash-bound evidence that a real consolidation occurred."""

    def __init__(self, repository: Repository):
        self.repository = repository
        self.directory = repository.root / "vault" / "receipts" / "consolidation"

    def documents(self) -> list[Path]:
        return sorted(self.directory.glob("consolidation-*.md")) if self.directory.exists() else []

    def load(self, consolidation_id: str) -> tuple[Path, dict[str, Any], str]:
        for path in self.documents():
            metadata, body = read_document(path)
            if metadata.get("consolidation_id") == consolidation_id or metadata.get("id") == consolidation_id:
                return path, metadata, body
        raise ValueError(f"consolidation receipt not found: {consolidation_id}")

    @staticmethod
    def complete(metadata: dict[str, Any]) -> bool:
        checks = metadata.get("checks", {})
        # v1 remains readable for audit history, but cannot qualify a v2
        # Trusted promotion.  Its boolean checks are intentionally preserved.
        if int(metadata.get("receipt_schema_version", 1)) < RECEIPT_SCHEMA_VERSION:
            return (
                metadata.get("status") == "complete"
                and REQUIRED_RECEIPT_CHECKS <= set(checks)
                and all(checks.get(key) is True for key in REQUIRED_RECEIPT_CHECKS)
                and metadata.get("result") not in {"failed", "needs_review"}
            )
        return (
            metadata.get("execution_status") == "complete"
            and metadata.get("validation_outcome") == "passed"
            and metadata.get("status") == "complete"
            and REQUIRED_RECEIPT_CHECKS <= set(checks)
            and all(checks.get(key) is True for key in REQUIRED_RECEIPT_CHECKS)
            and metadata.get("result") not in {"failed", "needs_review"}
            and bool(metadata.get("consolidation_fingerprint"))
        )

    @staticmethod
    def semantic_qualification_failures(object_type: str, receipt: dict[str, Any] | None) -> list[str]:
        """Return type-specific semantic failures shared by write and read gates."""
        if receipt is None:
            return []
        details = receipt.get("check_details", {}) if isinstance(receipt.get("check_details"), dict) else {}
        if object_type == "claim":
            entailment = details.get("evidence_entailment_rechecked", {})
            if not (
                entailment.get("validation_outcome") == "passed"
                and entailment.get("semantic_recheck_performed") is True
            ):
                return ["receipt_semantic_entailment_not_passed"]
        elif object_type == "concept":
            independence = details.get("source_independence_checked", {})
            if independence.get("validation_outcome") != "passed":
                return ["receipt_logical_work_independence_not_established"]
        return []

    def valid_for(self, object_id: str) -> dict[str, Any] | None:
        try:
            fingerprint = self.fingerprint(object_id)
        except Exception:
            # A receipt must never remain usable when its environment cannot be
            # read completely (notably the relation index).
            return None
        candidates = [
            item for item in self._current_for(object_id)
            if self.complete(item)
            and int(item.get("receipt_schema_version", 1)) >= RECEIPT_SCHEMA_VERSION
            and item.get("consolidation_fingerprint") == fingerprint
        ]
        return sorted(candidates, key=lambda item: str(item.get("completed_at", "")))[-1] if candidates else None

    def _current_for(self, object_id: str) -> list[dict[str, Any]]:
        """Return receipts bound to the current bytes, including explicit failures."""
        try:
            path, _, _ = self.repository.find_document(object_id)
        except Exception:
            return []
        current = hashlib.sha256(path.read_bytes()).hexdigest()
        candidates: list[dict[str, Any]] = []
        for receipt_path in self.documents():
            receipt, _ = read_document(receipt_path)
            if receipt.get("object_id") != object_id:
                continue
            if receipt.get("object_sha256_after") != current:
                continue
            candidates.append({**receipt, "path": self.repository.rel(receipt_path)})
        return candidates

    @staticmethod
    def _digest(value: Any) -> str:
        return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, default=str).encode("utf-8")).hexdigest()

    def _source_records(self, source_ids: list[str]) -> list[dict[str, Any]]:
        records = []
        for source_id in source_ids:
            try:
                source_path, source, _ = self.repository.find_document(source_id)
                raw_path = self.repository.resolve_inside(str(source["raw_content_path"])) if source.get("raw_content_path") else None
                work_id = source.get("work_id")
                work_sha = None
                if work_id:
                    try:
                        work_path, _, _ = self.repository.find_document(str(work_id))
                        work_sha = sha256_bytes(work_path.read_bytes())
                    except Exception:
                        work_sha = None
                records.append({
                    "source_id": source_id,
                    "source_record_sha256": sha256_bytes(source_path.read_bytes()),
                    "raw_content_sha256": sha256_bytes(raw_path.read_bytes()) if raw_path and raw_path.exists() else None,
                    "work_id": work_id,
                    "work_document_sha256": work_sha,
                })
            except Exception:
                records.append({"source_id": source_id, "missing": True})
        return records

    def _relation_fingerprint(self, object_id: str) -> dict[str, Any]:
        """Return an explainable, stable view of both directions of the relation index."""
        relations = self.repository.related(object_id)
        normalized = sorted(
            [
                {
                    "source_id": str(item["source_id"]),
                    "relation_type": str(item["relation_type"]),
                    "target_id": str(item["target_id"]),
                    "reason": str(item.get("reason", "")),
                }
                for item in relations
            ],
            key=lambda item: (
                item["source_id"], item["relation_type"], item["target_id"], item["reason"],
            ),
        )
        outgoing = [item for item in normalized if item["source_id"] == object_id]
        incoming = [item for item in normalized if item["target_id"] == object_id]
        return {
            "outgoing_relations_sha256": self._digest(outgoing),
            "incoming_relations_sha256": self._digest(incoming),
            "full_neighborhood_sha256": self._digest(normalized),
            "outgoing": outgoing,
            "incoming": incoming,
        }

    def fingerprint(self, object_id: str, *, metadata: dict[str, Any] | None = None, body: str | None = None) -> dict[str, Any]:
        """Hash every governed input that can invalidate a consolidation."""
        path, current, current_body = self.repository.find_document(object_id)
        metadata = metadata or current
        body = current_body if body is None else body
        source_ids = [str(item) for item in metadata.get("source_ids", [])]
        source_records = self._source_records(source_ids)
        evidence = [item for item in metadata.get("evidence", []) if isinstance(item, dict)]
        relation_fingerprint = self._relation_fingerprint(object_id)
        contradictions = {
            "metadata": sorted(str(item) for item in metadata.get("unresolved_contradictions", [])),
            "outgoing": [item for item in relation_fingerprint["outgoing"] if item["relation_type"] == "contradicts"],
            "incoming": [item for item in relation_fingerprint["incoming"] if item["relation_type"] == "contradicts"],
        }
        return {
            "object_sha256": sha256_bytes(render_document(metadata, body).encode("utf-8")),
            "source_state_sha256": self._digest(source_records),
            "source_record_sha256s": {item["source_id"]: item.get("source_record_sha256") for item in source_records},
            "raw_state_sha256": self._digest([item.get("raw_content_sha256") for item in source_records]),
            "evidence_sha256": self._digest(evidence),
            "extraction_state_sha256": self._digest([{
                "evidence_id": item.get("evidence_id"), "extraction_id": item.get("extraction_id"),
                "input_sha256": item.get("input_sha256"), "extractor_version": item.get("extractor_version"),
            } for item in evidence]),
            "work_identity_sha256": self._digest([{
                "source_id": item["source_id"], "work_id": item.get("work_id"),
                "work_document_sha256": item.get("work_document_sha256"),
            } for item in source_records]),
            "relation_fingerprint": {
                key: relation_fingerprint[key]
                for key in ("outgoing_relations_sha256", "incoming_relations_sha256", "full_neighborhood_sha256")
            },
            "relation_neighborhood_sha256": relation_fingerprint["full_neighborhood_sha256"],
            "contradictions_sha256": self._digest(contradictions),
            "receipt_schema_version": RECEIPT_SCHEMA_VERSION,
            "memory_schema_version": metadata.get("memory_schema_version", 1),
            "consolidator_version": CONSOLIDATOR_VERSION,
            "drift_policy_version": DRIFT_POLICY_VERSION,
            "promotion_policy_version": POLICY_VERSION,
        }

    def counts(self) -> dict[str, int]:
        complete = failed = 0
        for path in self.documents():
            metadata, _ = read_document(path)
            if self.complete(metadata):
                complete += 1
            else:
                failed += 1
        return {"complete": complete, "failed": failed, "total": complete + failed}

    def _source_state(self, source_ids: list[str]) -> tuple[list[str], bool, list[str]]:
        hashes: list[str] = []
        warnings: list[str] = []
        available = bool(source_ids)
        for source_id in source_ids:
            try:
                source_path, source, _ = self.repository.find_document(source_id)
                raw_value = source.get("raw_content_path")
                raw_path = self.repository.resolve_inside(str(raw_value)) if raw_value else None
                if raw_path is None or not raw_path.exists():
                    available = False
                    warnings.append(f"raw unavailable: {source_id}")
                    hashes.append(hashlib.sha256(source_path.read_bytes()).hexdigest())
                else:
                    digest = hashlib.sha256(raw_path.read_bytes()).hexdigest()
                    hashes.append(digest)
                    expected = source.get("content_sha256")
                    if expected and expected != digest:
                        available = False
                        warnings.append(f"raw hash mismatch: {source_id}")
            except Exception:
                available = False
                warnings.append(f"source unavailable: {source_id}")
        return hashes, available, warnings

    def _search_checks(
        self, metadata: dict[str, Any],
    ) -> tuple[dict[str, bool], list[str], dict[str, list[str]], dict[str, Any]]:
        checks = {
            "duplicate_search_completed": False,
            "related_object_search_completed": False,
            "contradiction_search_completed": False,
        }
        warnings: list[str] = []
        findings: dict[str, list[str]] = {
            "duplicate_search_completed": [],
            "related_object_search_completed": [],
            "contradiction_search_completed": [],
        }
        contradiction_search: dict[str, Any] = {
            "execution_status": "failed", "outgoing": [], "incoming": [],
            "unresolved_count": 0, "validation_outcome": "needs_review",
        }
        try:
            results = self.repository.search(str(metadata.get("title", metadata["id"])), 20)
            checks["duplicate_search_completed"] = True
            findings["duplicate_search_completed"] = [
                f"searched title; {len(results)} candidates inspected",
                *[f"candidate:{item.id}" for item in results[:5]],
            ]
        except Exception as exc:
            warnings.append(f"duplicate search failed: {exc}")
        try:
            relation_fingerprint = self._relation_fingerprint(str(metadata["id"]))
            related = [*relation_fingerprint["outgoing"], *relation_fingerprint["incoming"]]
            checks["related_object_search_completed"] = True
            findings["related_object_search_completed"] = [
                f"relation index inspected; {len(related)} related objects found",
                *[f"related:{item.get('id', item.get('target_id', 'unknown'))}" for item in related[:5]],
            ]
            outgoing = [
                item for item in relation_fingerprint["outgoing"]
                if item["relation_type"] == "contradicts"
            ]
            incoming = [
                item for item in relation_fingerprint["incoming"]
                if item["relation_type"] == "contradicts"
            ]
            checks["contradiction_search_completed"] = True
            contradiction_search = {
                "execution_status": "completed", "outgoing": outgoing, "incoming": incoming,
                "unresolved_count": len(outgoing) + len(incoming),
                "validation_outcome": "clear" if not outgoing and not incoming else "contested",
            }
            findings["contradiction_search_completed"] = [
                f"contradiction relations inspected; {len(outgoing) + len(incoming)} found",
                *[f"outgoing_contradicts:{item['target_id']}" for item in outgoing],
                *[f"incoming_contradicts:{item['source_id']}" for item in incoming],
            ]
        except Exception as exc:
            warnings.append(f"relation search failed: {exc}")
        return checks, warnings, findings, contradiction_search

    def consolidate(
        self, object_id: str, *, result: str | None = None,
        changes: list[dict[str, Any]] | None = None, change_summary: str = "",
        exceptions_created: list[str] | None = None,
        consolidator: str = "deterministic", model_provider: str = "none",
        model_version: str = "none", rebuild_index: bool = True,
    ) -> dict[str, Any]:
        path, metadata, body = self.repository.find_document(object_id)
        if not self.repository.rel(path).startswith(("vault/memory/", "vault/knowledge/", "vault/frontier/", "vault/action/")):
            raise ValueError("only governed knowledge objects can be consolidated")
        if metadata.get("memory_tier") == "historical" or metadata.get("status") in {"archived", "superseded"}:
            raise ValidationError("historical object is excluded from routine consolidation")
        valid = self.valid_for(object_id)
        if valid is not None and result is None and not changes and not metadata.get("needs_policy_requalification"):
            return {**valid, "reused": True}
        started = now_iso()
        before_bytes = path.read_bytes()
        before_sha = hashlib.sha256(before_bytes).hexdigest()
        source_ids = [str(item) for item in metadata.get("source_ids", [])]
        source_hashes, raw_available, warnings = self._source_state(source_ids)
        search_checks, search_warnings, search_findings, contradiction_search = self._search_checks(metadata)
        warnings.extend(search_warnings)
        object_type = str(metadata.get("type"))
        evidence = [item for item in metadata.get("evidence", []) if isinstance(item, dict)]
        evidence_ids = [str(item.get("evidence_id")) for item in evidence if item.get("evidence_id")]
        evidence_revalidated = object_type != "claim" or bool(evidence)
        entailment_rechecked = object_type != "claim" or metadata.get("evidence_entailment") is not None
        if object_type == "claim" and not evidence_revalidated:
            warnings.append("claim evidence missing")
        if object_type == "claim" and not entailment_rechecked:
            warnings.append("claim evidence entailment not checked")
        try:
            self.repository._validate_metadata(metadata, path)
            schema_validated = True
        except Exception as exc:
            schema_validated = False
            warnings.append(f"schema validation failed: {exc}")
        drift = DriftAuditService(self.repository).run_for(object_id)
        checks = {
            "schema_validated": schema_validated,
            "raw_available": raw_available,
            "provenance_revalidated": raw_available and bool(source_ids),
            "evidence_revalidated": evidence_revalidated,
            "evidence_entailment_rechecked": entailment_rechecked,
            **search_checks,
            "freshness_checked": True,
            "source_independence_checked": True,
            "drift_checked": True,
        }
        if any(item["severity"] == "high" for item in drift):
            warnings.append("high severity semantic drift detected")
            checks["drift_checked"] = False
        receipt_complete = all(checks.get(key) is True for key in REQUIRED_RECEIPT_CHECKS)
        resolved_result = result or ("unchanged" if receipt_complete else "failed")
        if resolved_result == "promotion_candidate" and not receipt_complete:
            resolved_result = "failed"
        try:
            environment_fingerprint = self.fingerprint(object_id, metadata=metadata, body=body)
        except Exception as exc:
            warnings.append(f"relation fingerprint failed: {exc}")
            checks["related_object_search_completed"] = False
            checks["contradiction_search_completed"] = False
            receipt_complete = False
            resolved_result = "failed"
            environment_fingerprint = {}
        failed_attempt_index = sum(
            1 for receipt_path in self.documents()
            for receipt_metadata, _ in [read_document(receipt_path)]
            if receipt_metadata.get("object_id") == object_id
            and not self.complete(receipt_metadata)
        ) if not receipt_complete or resolved_result in {"failed", "needs_review"} else None
        stable = json.dumps(
            [
                object_id, before_sha, environment_fingerprint, evidence_ids, checks,
                resolved_result, changes or [], exceptions_created or [], failed_attempt_index,
            ],
            ensure_ascii=False, sort_keys=True,
        )
        consolidation_id = "consolidation_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24]
        completed = now_iso()
        # Failed validation is observational only: no governed object mutation.
        updated = dict(metadata)
        if receipt_complete and not metadata.get("user_locked"):
            updated["consolidation_count"] = int(metadata.get("consolidation_count", 0)) + 1
            updated["last_consolidated_at"] = completed
            updated["last_consolidation_id"] = consolidation_id
            updated["updated_at"] = completed
            updated["updated_by"] = CONSOLIDATOR_VERSION
        after_text = render_document(updated, body)
        after_sha = sha256_bytes(after_text.encode("utf-8")) if receipt_complete else before_sha
        try:
            fingerprint = self.fingerprint(object_id, metadata=updated if receipt_complete else metadata, body=body)
        except Exception as exc:
            warnings.append(f"final relation fingerprint failed: {exc}")
            receipt_complete = False
            resolved_result = "failed"
            fingerprint = {}
        source_records = self._source_records(source_ids)
        work_ids = sorted({
            *{str(item.get("work_id")) for item in source_records if item.get("work_id")},
            *{str(item) for item in metadata.get("reuse_work_ids", []) if item},
        })
        detail_findings: dict[str, list[str]] = {
            "schema_validated": [f"validated:{self.repository.rel(path)}"] if schema_validated else [],
            "raw_available": [
                f"source:{item['source_id']} raw_sha256:{item.get('raw_content_sha256') or 'missing'}"
                for item in source_records
            ],
            "provenance_revalidated": [
                f"source:{item['source_id']} record_sha256:{item['source_record_sha256']}"
                for item in source_records
            ],
            "evidence_revalidated": [
                f"evidence:{item.get('evidence_id') or item.get('source_id') or 'inline'}"
                for item in evidence
            ] or (["not applicable for non-claim object"] if object_type != "claim" else []),
            "evidence_entailment_rechecked": [
                f"evidence_entailment:{metadata.get('evidence_entailment')}"
            ] if object_type == "claim" else ["not applicable for non-claim object"],
            "freshness_checked": [
                f"object_updated_at:{metadata.get('updated_at')}",
                *[f"source:{item['source_id']} work_sha256:{item.get('work_document_sha256') or 'none'}" for item in source_records],
            ],
            "source_independence_checked": [
                f"distinct_source_ids:{len(set(source_ids))}", f"distinct_work_ids:{len(work_ids)}",
                *[f"work_id:{item}" for item in work_ids],
            ],
            "drift_checked": [
                f"drift_reports:{len(drift)}",
                *[f"{item['drift_report_id']}:{item['severity']}:{item['drift_type']}" for item in drift],
            ],
            **search_findings,
        }
        semantic_entailment_passed = (
            object_type != "claim" or (
                metadata.get("quote_verification") == "exact"
                and bool(evidence)
                and all(item.get("evidence_kind") == "quote" for item in evidence)
            )
        )
        validation_outcomes = {
            key: ("passed" if value else "blocked") for key, value in checks.items()
        }
        validation_outcomes["evidence_entailment_rechecked"] = (
            "not_applicable" if object_type != "claim"
            else "passed" if semantic_entailment_passed
            else "needs_review" if entailment_rechecked else "blocked"
        )
        validation_outcomes["source_independence_checked"] = (
            "passed" if object_type == "concept" and len(work_ids) >= 2
            else "not_established" if object_type == "concept"
            else "not_applicable"
        )
        validation_outcomes["contradiction_search_completed"] = contradiction_search["validation_outcome"]
        check_details = {
            key: {
                "check_name": key,
                "execution_status": "completed" if value else "failed",
                "validation_outcome": validation_outcomes[key],
                "method": (
                    "declared-metadata-inspection" if key == "evidence_entailment_rechecked" else
                    "logical-work-identity-count" if key == "source_independence_checked" else
                    "relation-index-query" if key == "contradiction_search_completed" else
                    "deterministic repository check"
                ),
                "semantic_recheck_performed": semantic_entailment_passed if key == "evidence_entailment_rechecked" else None,
                "declared_value": metadata.get("evidence_entailment") if key == "evidence_entailment_rechecked" else None,
                "findings": detail_findings.get(key, []),
                "warnings": [] if value else [warning for warning in warnings if key.split("_")[0] in warning]
                    or [f"{key} did not pass"],
            }
            for key, value in checks.items()
        }
        receipt = {
            "id": consolidation_id,
            "type": "consolidation_receipt",
            "receipt_schema_version": RECEIPT_SCHEMA_VERSION,
            "status": "complete" if receipt_complete and resolved_result not in {"failed", "needs_review"} else "failed",
            "execution_status": "complete",
            "validation_outcome": "passed" if receipt_complete and resolved_result not in {"failed", "needs_review"} else "failed",
            "title": f"Consolidation: {metadata.get('title', object_id)}",
            "created_at": completed,
            "updated_at": completed,
            "consolidation_id": consolidation_id,
            "object_id": object_id,
            "object_version_before": int(metadata.get("object_version", metadata.get("version_number", 1))),
            "object_sha256_before": before_sha,
            "object_sha256_after": after_sha,
            "source_ids": source_ids,
            "source_sha256s": source_hashes,
            "source_records": source_records,
            "evidence_ids": evidence_ids,
            "started_at": started,
            "completed_at": completed,
            "consolidator": consolidator,
            "consolidator_version": CONSOLIDATOR_VERSION,
            "model_provider": model_provider,
            "model_version": model_version,
            "checks": checks,
            "check_details": check_details,
            "contradiction_search": contradiction_search,
            "consolidation_fingerprint": fingerprint,
            "drift_policy_version": DRIFT_POLICY_VERSION,
            "result": resolved_result,
            "changes": changes or [],
            "change_summary": change_summary or "No semantic change.",
            "warnings": warnings,
            "exceptions_created": exceptions_created or [],
            "promotion_recommendation": "evaluate" if receipt_complete else "blocked",
        }
        receipt_path = self.directory / f"consolidation-{consolidation_id}.md"
        # Commit the receipt first.  Only a complete receipt permits the paired
        # object write, so a failed receipt cannot leave Trusted state mutated.
        self.repository.immutable_write(
            receipt_path,
            render_document(receipt, "# Consolidation Receipt\n\n```json\n" + json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n```\n").encode("utf-8"),
        )
        if receipt_complete and not metadata.get("user_locked"):
            atomic_write_text(path, after_text)
        if rebuild_index:
            self.repository.rebuild_index()
        self.repository.append_event("memory-events", {
            "event": "consolidation-receipt", "consolidation_id": consolidation_id,
            "object_id": object_id, "result": resolved_result, "complete": receipt["status"] == "complete",
        })
        return {**receipt, "path": self.repository.rel(receipt_path), "reused": False}


class DriftAuditService:
    def __init__(self, repository: Repository):
        self.repository = repository

    @staticmethod
    def _report(
        object_id: str, versions: list[str], evidence_ids: list[str], drift_type: str,
        severity: str, original: str, current: str, reason: str, action: str,
    ) -> dict[str, Any]:
        stable = f"{object_id}:{drift_type}:{original}:{current}"
        return {
            "drift_report_id": "drift_" + hashlib.sha256(stable.encode("utf-8")).hexdigest()[:24],
            "object_id": object_id, "object_versions_compared": versions,
            "source_evidence_ids": evidence_ids, "drift_type": drift_type,
            "severity": severity, "original_statement": original.strip(),
            "current_statement": current.strip(), "evidence_summary": f"{len(evidence_ids)} evidence items inspected",
            "reason": reason, "recommended_action": action,
        }

    def compare(
        self, object_id: str, original: str, current: str, *, object_type: str = "claim",
        versions: list[str] | None = None, evidence_ids: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        lower_original = original.casefold()
        lower_current = current.casefold()
        reports: list[dict[str, Any]] = []
        args = (object_id, versions or [], evidence_ids or [])
        uncertainty = ("may", "might", "could", "possibly", "可能", "或许", "不确定")
        certainty = ("prove", "proves", "proved", "demonstrates", "establishes", "证明", "证实", "必然")
        if any(term in lower_original for term in uncertainty) and not any(term in lower_current for term in uncertainty) and any(term in lower_current for term in certainty):
            reports.append(self._report(*args, "uncertainty-erasure", "high", original, current, "qualifier disappeared while certainty increased", "create_exception"))
        correlations = ("correlat", "associated", "相关", "关联")
        causal = ("cause", "causes", "caused", "leads to", "results in", "导致", "因果")
        if any(term in lower_original for term in correlations) and any(term in lower_current for term in causal):
            reports.append(self._report(*args, "correlation-to-causation", "high", original, current, "association was rewritten as causation", "human_review"))
        secondary = ("secondary source", "commentary", "解读", "二手")
        primary_fact = ("primary fact", "direct evidence", "原始事实", "直接证明")
        if any(term in lower_original for term in secondary) and any(term in lower_current for term in primary_fact):
            reports.append(self._report(*args, "secondary-to-primary", "high", original, current, "secondary material became a primary fact", "mark_contested"))
        if object_type == "analogy" and any(term in lower_current for term in causal + ("equivalent", "identical", "等同", "就是")):
            reports.append(self._report(*args, "analogy-to-fact", "high", original, current, "heuristic similarity became factual or causal equivalence", "create_exception"))
        if object_type == "synthesis" and len(current.strip()) > len(original.strip()) * 1.25 and not any(marker in current for marker in ("source_", "evidence_", "来源", "证据")):
            reports.append(self._report(*args, "unsupported-synthesis-addition", "high", original, current, "new synthesis conclusion has no visible provenance", "human_review"))
        if object_type == "translation" and any(term in lower_original for term in uncertainty) and not any(term in lower_current for term in uncertainty):
            reports.append(self._report(*args, "translation-strengthening", "high", original, current, "translation strengthened the source modality", "human_review"))
        return reports

    def run(self) -> dict[str, Any]:
        issues: list[dict[str, Any]] = []
        checked = 0
        for path in [*self.repository.memory_documents(), *self.repository.canonical_documents()]:
            metadata, body = read_document(path)
            checked += 1
            object_id = str(metadata["id"])
            evidence_ids = [str(item.get("evidence_id")) for item in metadata.get("evidence", []) if isinstance(item, dict) and item.get("evidence_id")]
            if metadata.get("type") == "claim":
                for evidence in metadata.get("evidence", []):
                    if evidence.get("evidence_kind") == "translation" and evidence.get("verification_status") in {"exact", "verbatim"}:
                        issues.append(self._report(object_id, [], evidence_ids, "translation-as-quote", "high", "translation", "verbatim", "translation was labeled as an exact quote", "create_exception"))
                if not metadata.get("source_ids") or not metadata.get("evidence"):
                    issues.append(self._report(object_id, [], evidence_ids, "claim-source-drift", "medium", "source-linked claim", body, "claim lost source or evidence", "revise_working"))
            if metadata.get("type") == "synthesis" and (not metadata.get("source_ids") or "## New evidence" not in body):
                issues.append(self._report(object_id, [], evidence_ids, "unsupported-synthesis", "medium", "source-grounded synthesis", body, "synthesis does not return to source evidence", "human_review"))
            if metadata.get("type") == "analogy" and not metadata.get("where_it_breaks"):
                issues.append(self._report(object_id, [], evidence_ids, "analogy-boundary-loss", "high", "bounded analogy", body, "where_it_breaks is missing", "create_exception"))
            if metadata.get("claim_confidence") == "high" and metadata.get("evidence_entailment") not in {"full"}:
                issues.append(self._report(object_id, [], evidence_ids, "uncertainty-erasure", "high", "limited evidence", body, "confidence exceeds evidence entailment", "mark_contested"))
            version_dir = self.repository.root / "vault" / "archive" / "versions" / object_id
            versions = sorted(version_dir.glob("*.md")) if version_dir.exists() else []
            if versions:
                _, original_body = read_document(versions[0])
                issues.extend(self.compare(
                    object_id, original_body, body, object_type=str(metadata.get("type")),
                    versions=[self.repository.rel(versions[0]), self.repository.rel(path)], evidence_ids=evidence_ids,
                ))
        return {
            "ok": not any(item.get("severity") == "high" for item in issues),
            "checked": checked, "issues": issues,
            "high_severity": sum(item.get("severity") == "high" for item in issues),
            "writes": 0,
        }

    def run_for(self, object_id: str) -> list[DriftReport]:
        """Run the same semantic rules for one object during consolidation."""
        report = self.run()
        return [item for item in report["issues"] if item["object_id"] == object_id]


class ConsolidationService:
    def __init__(self, repository: Repository):
        self.repository = repository
        self.exceptions = ExceptionService(repository)
        self.promotions = PromotionService(repository)
        self.receipts = ConsolidationReceiptService(repository)

    def review_working_quality(self) -> dict[str, Any]:
        """Identify unsafe deterministic fallbacks without mutating memory."""
        flagged: list[dict[str, Any]] = []
        source_lengths: dict[str, int] = {}
        source_has_markers: dict[str, bool] = {}
        source_kinds: dict[str, str] = {}
        for path in self.repository.active_memory_documents():
            metadata, _ = read_document(path)
            if metadata.get("memory_tier") != "working":
                continue
            if metadata.get("compiler_version") != "deterministic-bounded-bundle-v1":
                continue
            source_ids = [str(item) for item in metadata.get("source_ids", [])]
            long_sources: list[str] = []
            for source_id in source_ids:
                if source_id not in source_lengths:
                    try:
                        _, source_metadata, _ = self.repository.find_document(source_id)
                        _, _, text = ExtractionService(self.repository).latest_for_source(source_id)
                        source_lengths[source_id] = len(text)
                        source_kinds[source_id] = str(source_metadata.get("source_kind") or "unknown")
                        source_has_markers[source_id] = any(
                            pattern.match(line.strip().lstrip("#*- ").strip())
                            for line in text.splitlines()
                            for pattern in DeterministicCompilerProvider.MARKERS.values()
                        )
                    except Exception:
                        source_lengths[source_id] = 0
                        source_has_markers[source_id] = False
                        source_kinds[source_id] = "unknown"
                if (
                    source_lengths[source_id] > BundleCompiler.UNSTRUCTURED_FALLBACK_MAX_CHARS
                    and (
                        not source_has_markers[source_id]
                        or source_kinds[source_id] != "personal-notes"
                    )
                ):
                    long_sources.append(source_id)
            if not long_sources:
                continue
            reasons: list[str] = []
            if any(source_has_markers[item] and source_kinds[item] != "personal-notes" for item in long_sources):
                reasons.append("automatic article marker misclassified as an Agent instruction")
            if metadata.get("epistemic_status") == "unknown":
                reasons.append("unknown epistemic status")
            if metadata.get("type") == "claim" and metadata.get("evidence_entailment") == "none":
                reasons.append("no semantic evidence entailment")
            if not metadata.get("applicability") and metadata.get("type") == "claim":
                reasons.append("missing applicability")
            if reasons:
                flagged.append({
                    "object_id": str(metadata["id"]), "title": str(metadata.get("title", "")),
                    "source_ids": long_sources, "reasons": reasons,
                    "recommended_action": "recompile_or_source_only",
                })
        return {
            "checked": sum(1 for _ in self.repository.active_memory_documents()),
            "flagged": flagged, "flagged_count": len(flagged), "writes": 0,
        }

    def daily(self, *, limit: int = 25) -> dict[str, Any]:
        triage = DailyTriageService(self.repository).run(limit=limit)
        compiled = []
        blocked_sources = {
            str(item.get("context", {}).get("source_id"))
            for item in self.exceptions.list({"open", "deferred"})
            if item.get("exception_kind") == "daily-compile"
        }
        for item in ProposalService(self.repository).inbox()[:limit]:
            source_id = str(item["id"])
            if source_id in blocked_sources:
                compiled.append({"source_id": source_id, "status": "blocked-by-open-exception"})
                continue
            try:
                result = BundleCompiler(self.repository).compile(source_id)
                if result.compile_disposition == "source_only":
                    compiled.append({
                        "source_id": source_id, "status": "source_only",
                        "proposal_id": result.proposal_id,
                        "reason": "no knowledge-safe deterministic candidate",
                    })
                    continue
                if result.proposal_id:
                    written = WorkingMemoryService(self.repository).ingest_bundle(
                        result.proposal_id, rebuild_index=False
                    )
                    compiled.append({"source_id": source_id, "status": "working", **written.__dict__})
            except Exception as exc:
                exception_id = self.exceptions.create(
                    "daily-compile", f"Daily compile failed: {source_id}", [str(exc)],
                    source_ids=[source_id], context={"source_id": source_id, "error": str(exc)},
                )
                compiled.append({"source_id": source_id, "status": "exception", "exception_id": exception_id})
        self.repository.rebuild_index()
        return {"mode": "daily-consolidation", "triage": triage, "compiled": compiled, "canonical_writes": 0}

    def weekly(self) -> dict[str, Any]:
        historical = list(self.repository.memory_documents())
        before = list(self.repository.active_memory_documents())
        historical_ids_skipped = []
        for path in historical:
            metadata, _ = read_document(path)
            if path not in before:
                historical_ids_skipped.append(str(metadata.get("id")))
        receipts: list[dict[str, Any]] = []
        scanned_only: list[str] = []
        for path in before:
            metadata, _ = read_document(path)
            try:
                receipt = self.receipts.consolidate(str(metadata["id"]), rebuild_index=False)
                receipts.append(receipt)
            except Exception as exc:
                scanned_only.append(str(metadata.get("id")))
                self.exceptions.create(
                    "consolidation-failed", f"Consolidation failed: {metadata.get('title')}",
                    [str(exc)], object_id=str(metadata.get("id")),
                    source_ids=[str(item) for item in metadata.get("source_ids", [])],
                )
        self.repository.rebuild_index()
        requalified, requalification_blocked = [], []
        for path in list(self.repository.active_memory_documents()):
            metadata, _ = read_document(path)
            if metadata.get("status") != "trusted" or not metadata.get("needs_policy_requalification"):
                continue
            result = self.promotions.requalify_trusted(str(metadata["id"]), rebuild_index=False)
            if result.get("requalified"):
                requalified.append(str(metadata["id"]))
            else:
                requalification_blocked.append({
                    "object_id": str(metadata["id"]),
                    "failed_conditions": result.get("evaluation", {}).get("failed_conditions", []),
                })
        self.repository.rebuild_index()
        promoted, retained = [], []
        for path in list(self.repository.active_memory_documents()):
            metadata, _ = read_document(path)
            if metadata.get("status") != "working":
                continue
            result = self.promotions.promote_trusted(
                str(metadata["id"]), automatic=True, rebuild_index=False
            )
            if result.get("promoted"):
                promoted.append(str(metadata["id"]))
            else:
                retained.append({"object_id": str(metadata["id"]), "failed_conditions": result["evaluation"]["failed_conditions"]})
        self.repository.rebuild_index()
        drift = DriftAuditService(self.repository).run()
        for issue in drift["issues"]:
            if issue.get("severity") != "high":
                continue
            self.exceptions.create(
                "memory-drift", f"Drift audit: {issue['object_id']}", [str(issue["drift_type"])],
                object_id=issue["object_id"], context=issue,
            )
        canonical_candidates = []
        for path in self.repository.active_memory_documents():
            metadata, _ = read_document(path)
            if (
                metadata.get("status") == "trusted"
                and not metadata.get("needs_policy_requalification")
                and metadata.get("type") in {"decision", "architecture", "goal", "project", "synthesis"}
            ):
                canonical_candidates.append(self.promotions.recommend_canonical(str(metadata["id"]), "high-impact trusted memory"))
        exceptions = self.exceptions.list({"open", "deferred"})
        raw_count = len(list(self.repository.source_documents()))
        working_count = sum(read_document(path)[0].get("status") == "working" for path in self.repository.active_memory_documents())
        trusted_count = sum(read_document(path)[0].get("status") == "trusted" for path in self.repository.active_memory_documents())
        review_items = len(exceptions) + len(canonical_candidates)
        original_review = max(1, raw_count)
        retention_reasons = Counter(
            reason for item in retained for reason in item["failed_conditions"]
        )
        working_quality_review = self.review_working_quality()
        report = {
            "mode": "weekly-consolidation", "raw_item_count": raw_count,
            "sources_processed": raw_count,
            "objects_considered": len(before),
            "active_objects_considered": len(before),
            "historical_objects_skipped": len(historical_ids_skipped),
            "historical_ids_skipped": historical_ids_skipped,
            "receipts_completed": sum(item.get("status") == "complete" for item in receipts),
            "receipts_failed": sum(item.get("status") != "complete" for item in receipts) + len(scanned_only),
            "objects_unchanged": sum(item.get("result") == "unchanged" for item in receipts),
            "objects_supported": sum(item.get("result") == "supported" for item in receipts),
            "objects_refined": sum(item.get("result") == "refined" for item in receipts),
            "objects_limited": sum(item.get("result") == "limited" for item in receipts),
            "objects_contradicted": sum(item.get("result") == "contradicted" for item in receipts),
            "objects_superseded": sum(item.get("result") == "superseded" for item in receipts),
            "working_revisions": sum(bool(item.get("changes")) for item in receipts),
            "trusted_demotions": 0,
            "canonical_exceptions": sum(item.get("exception_kind") == "canonical-conflict" for item in exceptions),
            "drift_warnings": len(drift["issues"]),
            "user_attention_items": review_items,
            "working_changes": sum(
                item.get("status") == "complete" and not item.get("reused", False)
                for item in receipts
            ), "working_count": working_count,
            "trusted_promotions": len(promoted), "trusted_count": trusted_count,
            "trusted_requalified": len(requalified),
            "trusted_requalification_blocked": len(requalification_blocked),
            "exceptions": len(exceptions), "canonical_candidates": len(canonical_candidates),
            "estimated_human_review_minutes": review_items * 3,
            "compression_ratio": round(1 - review_items / original_review, 4),
            "promoted_ids": promoted, "retained_working_count": len(retained),
            "requalified_ids": requalified,
            "requalification_blocked": requalification_blocked,
            "retained_working": retained[:20],
            "retained_working_omitted": max(0, len(retained) - 20),
            "retention_reason_counts": dict(retention_reasons.most_common()),
            "exception_ids": [item["id"] for item in exceptions],
            "canonical_promotion_ids": [item["promotion_id"] for item in canonical_candidates],
            "drift": drift, "canonical_writes": 0,
            "receipt_ids": [item["consolidation_id"] for item in receipts],
            "scanned_only_ids": scanned_only,
            "estimated_review_time": review_items * 3,
            "working_quality_review": working_quality_review,
        }
        report_id = "weekly_" + hashlib.sha256(now_iso()[:10].encode()).hexdigest()[:16]
        report_path = self.repository.root / "system" / "reports" / f"generated-{report_id}.md"
        atomic_write_text(report_path, "# Weekly Consolidation Digest\n\n" + "\n".join(f"- {key}: {value}" for key, value in report.items() if not isinstance(value, (list, dict))) + "\n")
        report["report_path"] = self.repository.rel(report_path)
        return report


class WorkingQualityMigration:
    """Archive unsafe legacy deterministic fallbacks with reversible snapshots."""

    POLICY = "working-quality-source-only-v1"

    def __init__(self, repository: Repository):
        self.repository = repository

    def _manifest_path(self, migration_id: str) -> Path:
        return self.repository.root / "data" / "backups" / migration_id / "manifest.json"

    def _write_manifest(self, path: Path, manifest: dict[str, Any]) -> None:
        atomic_write_text(path, json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    def _canonical_hashes(self) -> dict[str, str]:
        return {
            self.repository.rel(path): sha256_bytes(path.read_bytes())
            for path in sorted(self.repository.canonical_documents())
        }

    def _event_exists(self, migration_id: str, object_id: str, event: str) -> bool:
        path = self.repository.root / "system" / "logs" / "memory-events.jsonl"
        if not path.exists():
            return False
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (
                record.get("event") == event
                and record.get("operation_id") == migration_id
                and record.get("object_id") == object_id
            ):
                return True
        return False

    def _source_raw_valid(self, source_ids: list[Any]) -> bool:
        for source_id in source_ids:
            try:
                _, source, _ = self.repository.find_document(str(source_id))
                raw_path = self.repository.resolve_inside(str(source["raw_content_path"]))
            except Exception:
                return False
            if not raw_path.exists():
                return False
        return True

    def _incomplete_manifest(self) -> tuple[Path, dict[str, Any]] | None:
        root = self.repository.root / "data" / "backups"
        matches: list[tuple[Path, dict[str, Any]]] = []
        for path in sorted(root.glob("working_quality_*/manifest.json")) if root.exists() else []:
            manifest = json.loads(path.read_text(encoding="utf-8"))
            if manifest.get("policy") == self.POLICY and manifest.get("phase") in {"prepared", "applying", "blocked"}:
                matches.append((path, manifest))
        if len(matches) > 1:
            raise ValidationError("multiple incomplete working quality migrations; resolve one manifest explicitly")
        return matches[0] if matches else None

    def _restore_revision_conflicts(self, object_id: str) -> list[str]:
        conflicts: list[str] = []
        for path in self.repository.memory_documents():
            metadata, _ = read_document(path)
            if str(metadata.get("id")) == object_id:
                continue
            if metadata.get("revision_of") == object_id and metadata.get("status") not in {"archived", "superseded"}:
                conflicts.append(f"new working revision exists: {metadata.get('id')}")
        for path in self.repository.canonical_documents():
            metadata, _ = read_document(path)
            if str(metadata.get("id")) == object_id:
                conflicts.append(f"canonical promotion exists: {object_id}")
                continue
            for relation in metadata.get("relations", []):
                if isinstance(relation, dict) and relation.get("target_id") == object_id:
                    conflicts.append(f"canonical successor exists: {metadata.get('id')}")
                    break
        return conflicts

    def upgrade_legacy_manifest(self, migration_id: str) -> dict[str, Any]:
        """Add missing post-image fields to an older, already-completed manifest.

        This does not retroactively claim an original migration-time proof.  It
        creates an explicit safety baseline from which future Verify/Restore
        checks are hash-bound.
        """
        path = self._manifest_path(migration_id)
        if not path.exists():
            raise ValidationError(f"working quality migration manifest not found: {migration_id}")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        if manifest.get("policy") != self.POLICY:
            raise ValidationError(f"unexpected working quality migration policy: {migration_id}")
        upgraded: list[str] = []
        for item in manifest.get("objects", []):
            object_id = str(item["object_id"])
            target_path = self.repository.resolve_inside(str(item["path"]))
            metadata, _ = read_document(target_path)
            if (
                metadata.get("quality_migration_id") != migration_id
                or metadata.get("status") != "archived"
                or metadata.get("memory_tier") != "historical"
            ):
                raise ValidationError(f"cannot baseline changed historical object: {object_id}")
            snapshot = (
                self.repository.root / "vault" / "archive" / "versions" / object_id
                / f"{item['sha256_before']}.md"
            )
            if not snapshot.exists() or sha256_bytes(snapshot.read_bytes()) != item["sha256_before"]:
                raise ValidationError(f"cannot baseline missing or invalid snapshot: {object_id}")
            if not self._source_raw_valid(list(metadata.get("source_ids", []))):
                raise ValidationError(f"cannot baseline missing source/raw: {object_id}")
            if not self._event_exists(migration_id, object_id, "working-quality-archived"):
                raise ValidationError(f"cannot baseline missing archive event: {object_id}")
            item.update({
                "sha256_after": sha256_bytes(target_path.read_bytes()),
                "snapshot_path": self.repository.rel(snapshot), "status": "applied",
            })
            upgraded.append(object_id)
        manifest.update({
            "phase": "completed", "canonical_sha256": self._canonical_hashes(),
            "legacy_safety_baseline_at": now_iso(),
            "legacy_safety_baseline_note": "post-image and canonical hashes baselined after legacy migration; not retrospective proof",
        })
        self._write_manifest(path, manifest)
        return {"ok": True, "migration_id": migration_id, "upgraded_objects": upgraded, "legacy_safety_baseline": True}

    def verify(self, migration_id: str) -> dict[str, Any]:
        path = self._manifest_path(migration_id)
        if not path.exists():
            raise ValidationError(f"working quality migration manifest not found: {migration_id}")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        conflicts: list[str] = []
        checked: list[dict[str, Any]] = []
        canonical_before = manifest.get("canonical_sha256")
        canonical_unchanged: bool | None = None
        if isinstance(canonical_before, dict):
            canonical_unchanged = canonical_before == self._canonical_hashes()
            if not canonical_unchanged:
                conflicts.append("canonical state changed since migration preparation")
        else:
            # Pre-M9.0.1 manifests did not persist this baseline.  Do not
            # claim proof that cannot be reconstructed after the fact.
            canonical_unchanged = None
        for item in manifest.get("objects", []):
            object_id = str(item["object_id"])
            backup_path = self.repository.resolve_inside(item["backup_path"])
            backup_valid = backup_path.exists() and sha256_bytes(backup_path.read_bytes()) == item.get("sha256_before")
            metadata: dict[str, Any] | None = None
            try:
                target_path = self.repository.resolve_inside(str(item["path"]))
                metadata, _ = read_document(target_path)
                current_sha = sha256_bytes(target_path.read_bytes())
                current_valid = (
                    metadata.get("quality_migration_id") == migration_id
                    and metadata.get("status") == "archived"
                    and metadata.get("memory_tier") == "historical"
                    and current_sha == item.get("sha256_after")
                )
            except Exception:
                current_sha, current_valid = "", False
            snapshot_path = item.get("snapshot_path") or self.repository.rel(
                self.repository.root / "vault" / "archive" / "versions" / object_id / f"{item['sha256_before']}.md"
            )
            snapshots_valid = bool(snapshot_path) and self.repository.resolve_inside(str(snapshot_path)).exists()
            events_valid = self._event_exists(migration_id, object_id, "working-quality-archived")
            source_raw_valid = self._source_raw_valid(list(metadata.get("source_ids", []))) if metadata is not None else False
            if not backup_valid:
                conflicts.append(f"backup invalid: {object_id}")
            if not current_valid:
                conflicts.append(f"current state or SHA invalid: {object_id}")
            if not snapshots_valid:
                conflicts.append(f"snapshot missing: {object_id}")
            if not events_valid:
                conflicts.append(f"archive event missing: {object_id}")
            if not source_raw_valid:
                conflicts.append(f"source/raw missing: {object_id}")
            checked.append({"object_id": object_id, "backup_valid": backup_valid, "current_sha256": current_sha, "current_state_valid": current_valid, "snapshots_valid": snapshots_valid, "events_valid": events_valid, "source_raw_valid": source_raw_valid})
        return {"ok": not conflicts, "migration_id": migration_id, "objects": checked, "conflicts": conflicts, "canonical_unchanged": canonical_unchanged}

    def restore(self, migration_id: str, *, dry_run: bool = False) -> dict[str, Any]:
        verified = self.verify(migration_id)
        if not verified["ok"]:
            return {**verified, "dry_run": dry_run, "restored": [], "blocked": True}
        manifest = json.loads(self._manifest_path(migration_id).read_text(encoding="utf-8"))
        restore_plan: list[tuple[Path, Path, str]] = []
        conflicts: list[str] = []
        for item in manifest["objects"]:
            object_id = str(item["object_id"])
            target_path = self.repository.resolve_inside(str(item["path"]))
            metadata, _ = read_document(target_path)
            if metadata.get("quality_migration_id") != migration_id or metadata.get("status") != "archived" or metadata.get("memory_tier") != "historical":
                conflicts.append(f"restore blocked by changed object: {object_id}")
                continue
            if sha256_bytes(target_path.read_bytes()) != item.get("sha256_after"):
                conflicts.append(f"restore blocked by changed post-migration bytes: {object_id}")
                continue
            conflicts.extend(self._restore_revision_conflicts(object_id))
            restore_plan.append((target_path, self.repository.resolve_inside(item["backup_path"]), object_id))
        if conflicts or dry_run:
            return {**verified, "dry_run": dry_run, "restore_candidates": [object_id for _, _, object_id in restore_plan], "restored": [], "conflicts": [*verified["conflicts"], *conflicts], "blocked": bool(conflicts)}
        restored: list[str] = []
        for target_path, backup_path, object_id in restore_plan:
            atomic_write_text(target_path, backup_path.read_text(encoding="utf-8"))
            if not self._event_exists(migration_id, object_id, "working-quality-restored"):
                self.repository.append_event("memory-events", {"event": "working-quality-restored", "operation_id": migration_id, "object_id": object_id})
            restored.append(object_id)
        manifest["phase"] = "restored"
        manifest["restored_at"] = now_iso()
        for item in manifest["objects"]:
            if str(item["object_id"]) in restored:
                item["status"] = "restored"
        self._write_manifest(self._manifest_path(migration_id), manifest)
        self.repository.rebuild_index()
        return {**verified, "dry_run": False, "restored": restored, "canonical_writes": 0}

    def plan(self) -> dict[str, Any]:
        review = ConsolidationService(self.repository).review_working_quality()
        object_ids = sorted(item["object_id"] for item in review["flagged"])
        migration_id = "working_quality_" + hashlib.sha256(
            (self.POLICY + "\n" + "\n".join(object_ids)).encode("utf-8")
        ).hexdigest()[:24]
        return {
            "dry_run": True, "migration_id": migration_id, "policy": self.POLICY,
            "candidate_count": len(object_ids), "candidates": review["flagged"],
            "canonical_writes": 0,
        }

    def apply(self) -> dict[str, Any]:
        resumed = self._incomplete_manifest()
        if resumed is None:
            plan = self.plan()
            migration_id = str(plan["migration_id"])
            backup = self.repository.root / "data" / "backups" / migration_id
            backup.mkdir(parents=True, exist_ok=True)
            manifest_path = backup / "manifest.json"
            manifest = {
                "migration_id": migration_id, "policy": self.POLICY,
                "created_at": now_iso(), "phase": "prepared", "objects": [],
                "canonical_sha256": self._canonical_hashes(),
            }
            for item in plan["candidates"]:
                path, metadata, _ = self.repository.find_document(str(item["object_id"]))
                data = path.read_bytes()
                snapshot = backup / path.name
                self.repository.immutable_write(snapshot, data)
                manifest["objects"].append({
                    "object_id": item["object_id"], "path": self.repository.rel(path),
                    "sha256_before": sha256_bytes(data), "status": "pending",
                    "backup_path": self.repository.rel(snapshot), "reasons": item["reasons"],
                })
            self._write_manifest(manifest_path, manifest)
        else:
            manifest_path, manifest = resumed
            migration_id = str(manifest["migration_id"])
            backup = manifest_path.parent
            plan = {
                "dry_run": False, "migration_id": migration_id, "policy": self.POLICY,
                "candidate_count": len(manifest.get("objects", [])),
                "candidates": [], "canonical_writes": 0, "resumed": True,
            }
        manifest["phase"] = "applying"
        self._write_manifest(manifest_path, manifest)
        archived: list[str] = []
        unchanged: list[str] = []
        for item in manifest["objects"]:
            path = self.repository.resolve_inside(str(item["path"]))
            metadata, body = read_document(path)
            if metadata.get("quality_migration_id") == migration_id:
                current_hash = sha256_bytes(path.read_bytes())
                if item.get("sha256_after") and current_hash != item["sha256_after"]:
                    item.update({"status": "blocked", "error": "post-migration bytes changed"})
                    manifest["phase"] = "blocked"
                    self._write_manifest(manifest_path, manifest)
                    raise ValidationError(f"working quality migration blocked by changed object: {item['object_id']}")
                item["status"] = "applied"
                item.setdefault("sha256_after", current_hash)
                if not item.get("snapshot_path"):
                    recovered_snapshot = (
                        self.repository.root / "vault" / "archive" / "versions"
                        / str(metadata["id"]) / f"{item['sha256_before']}.md"
                    )
                    if not recovered_snapshot.exists():
                        item.update({"status": "blocked", "error": "snapshot missing after interrupted archive"})
                        manifest["phase"] = "blocked"
                        self._write_manifest(manifest_path, manifest)
                        raise ValidationError(f"working quality migration snapshot missing: {item['object_id']}")
                    item["snapshot_path"] = self.repository.rel(recovered_snapshot)
                if not self._event_exists(migration_id, str(metadata["id"]), "working-quality-archived"):
                    self.repository.append_event("memory-events", {
                        "event": "working-quality-archived", "operation_id": migration_id,
                        "object_id": metadata["id"], "snapshot_path": item.get("snapshot_path"),
                        "reason": metadata.get("change_reason", "legacy deterministic fallback archived as source-only"),
                    })
                self._write_manifest(manifest_path, manifest)
                unchanged.append(str(metadata["id"]))
                continue
            current_hash = sha256_bytes(path.read_bytes())
            if current_hash != item["sha256_before"]:
                item.update({"status": "blocked", "error": "pre-migration bytes changed"})
                manifest["phase"] = "blocked"
                self._write_manifest(manifest_path, manifest)
                raise ValidationError(
                    f"working quality migration blocked by changed object: {item['object_id']}"
                )
            version_path = (
                self.repository.root / "vault" / "archive" / "versions"
                / str(metadata["id"]) / f"{current_hash}.md"
            )
            self.repository.immutable_write(version_path, path.read_bytes())
            timestamp = now_iso()
            metadata.update({
                "status": "archived", "memory_tier": "historical",
                "quality_review_status": "source_only",
                "quality_review_policy": self.POLICY,
                "quality_review_reasons": list(item["reasons"]),
                "quality_migration_id": migration_id,
                "archived_at": timestamp, "updated_at": timestamp,
                "updated_by": self.POLICY,
                "change_reason": "legacy deterministic fallback archived as source-only",
            })
            atomic_write_text(path, render_document(metadata, body))
            if not self._event_exists(migration_id, str(metadata["id"]), "working-quality-archived"):
                self.repository.append_event("memory-events", {
                    "event": "working-quality-archived", "operation_id": migration_id,
                    "object_id": metadata["id"], "snapshot_path": self.repository.rel(version_path),
                    "reason": metadata["change_reason"],
                })
            item.update({
                "status": "applied", "sha256_after": sha256_bytes(path.read_bytes()),
                "snapshot_path": self.repository.rel(version_path),
            })
            self._write_manifest(manifest_path, manifest)
            archived.append(str(metadata["id"]))
        manifest["phase"] = "completed"
        manifest["completed_at"] = now_iso()
        self._write_manifest(manifest_path, manifest)
        self.repository.rebuild_index()
        return {
            **plan, "dry_run": False, "backup_path": self.repository.rel(backup),
            "archived_count": len(archived), "archived_ids": archived,
            "unchanged_count": len(unchanged), "unchanged_ids": unchanged,
            "remaining_flagged": ConsolidationService(self.repository).review_working_quality()["flagged_count"],
            "canonical_writes": 0,
        }


class ProposalGateMigration:
    def __init__(self, repository: Repository):
        self.repository = repository

    def plan(self) -> dict[str, Any]:
        pending, items, invalid, preserved = 0, 0, 0, Counter()
        for path in self.repository.proposal_documents():
            metadata, _ = read_document(path)
            status = str(metadata.get("status"))
            preserved[status] += 1
            if status not in {"pending", "deferred"}:
                continue
            pending += 1
            bundle = metadata.get("bundle_items")
            if isinstance(bundle, list):
                for item in bundle:
                    if item.get("decision") in {"pending", "deferred"}:
                        items += 1
                        if item.get("atomicity_status") == "compound" or item.get("evidence_coverage") == "missing":
                            invalid += 1
            elif metadata.get("candidate_path"):
                items += 1
            else:
                invalid += 1
        return {
            "dry_run": True, "pending_proposals": pending, "candidate_items": items,
            "predicted_working": max(0, items - invalid), "predicted_exceptions": invalid,
            "canonical_unchanged": len(list(self.repository.canonical_documents())),
            "preserved_by_status": dict(sorted(preserved.items())),
        }

    def apply(self) -> dict[str, Any]:
        plan = self.plan()
        if plan["pending_proposals"] == 0:
            return {
                **plan, "dry_run": False, "backup_path": None,
                "migrated_working_objects": 0, "exceptions_created": 0,
                "results": [], "idempotent_noop": True,
            }
        timestamp = now_iso().replace(":", "-")
        backup = self.repository.root / "data" / "backups" / f"promotion-migration-{timestamp}"
        backup.mkdir(parents=True, exist_ok=False)
        for path in self.repository.proposal_documents():
            shutil_target = backup / path.name
            shutil_target.write_bytes(path.read_bytes())
        results = []
        for path in list(self.repository.proposal_documents()):
            metadata, _ = read_document(path)
            if metadata.get("status") not in {"pending", "deferred"}:
                continue
            result = WorkingMemoryService(self.repository).ingest_bundle(
                str(metadata["id"]), rebuild_index=False
            )
            results.append(result.__dict__)
        self.repository.rebuild_index()
        report = {
            **plan, "dry_run": False, "backup_path": self.repository.rel(backup),
            "migrated_working_objects": sum(len(item["written"]) + len(item["updated"]) for item in results),
            "exceptions_created": sum(len(item["exceptions"]) for item in results),
            "results": results, "canonical_unchanged": len(list(self.repository.canonical_documents())),
        }
        return report
