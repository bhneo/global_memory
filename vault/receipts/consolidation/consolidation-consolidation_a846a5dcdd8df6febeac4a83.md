---
id: "consolidation_a846a5dcdd8df6febeac4a83"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 指向式视觉导航接口"
created_at: "2026-07-19T23:49:35+08:00"
updated_at: "2026-07-19T23:49:35+08:00"
consolidation_id: "consolidation_a846a5dcdd8df6febeac4a83"
object_id: "concept_34abf7a170a7e0fc0492fc16"
object_version_before: 1
object_sha256_before: "fb84ae26a30e2bb2ba49918be337d0c62b69ca0cd45cbd930b4fd48242ef6b9f"
object_sha256_after: "95feba5a05ecc5129668a88e31b509e0b550587ded329c278a4951d8c3a64bd8"
source_ids: ["source_886372de22c708b28cd11e4b"]
source_sha256s: ["8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939"]
source_records: [{"source_id": "source_886372de22c708b28cd11e4b", "source_record_sha256": "146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47", "raw_content_sha256": "8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T23:49:34+08:00"
completed_at: "2026-07-19T23:49:35+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_886372de22c708b28cd11e4b raw_sha256:8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_886372de22c708b28cd11e4b record_sha256:146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_34abf7a170a7e0fc0492fc16"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_886372de22c708b28cd11e4b", "related:claim_via_interface_first_robot_control_20260715"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T17:17:04+08:00", "source:source_886372de22c708b28cd11e4b work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "95feba5a05ecc5129668a88e31b509e0b550587ded329c278a4951d8c3a64bd8", "source_state_sha256": "2c1d5a1611b979bfa12bd80bdcd045ae13a50279235effce03d27c1de032b27b", "source_record_sha256s": {"source_886372de22c708b28cd11e4b": "146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47"}, "raw_state_sha256": "5aefae10e953ba94a27a1957d9a7e0e2782596f5335d723df9b72b7c5f7ad4bc", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "0e75745f4a921bc49fff188ed681101ff1d53ce348dfc8cf91608a5cb8aadb22", "relation_fingerprint": {"outgoing_relations_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce"}, "relation_neighborhood_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "unchanged"
changes: []
change_summary: "No semantic change."
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "No semantic change.",
  "changes": [],
  "check_details": {
    "contradiction_search_completed": {
      "check_name": "contradiction_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "method": "relation-index-query",
      "semantic_recheck_performed": null,
      "validation_outcome": "clear",
      "warnings": []
    },
    "drift_checked": {
      "check_name": "drift_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "drift_reports:0"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "check_name": "duplicate_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "searched title; 1 candidates inspected",
        "candidate:concept_34abf7a170a7e0fc0492fc16"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "not_applicable",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "check_name": "freshness_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "object_updated_at:2026-07-19T17:17:04+08:00",
        "source:source_886372de22c708b28cd11e4b work_sha256:none"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "check_name": "provenance_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "source:source_886372de22c708b28cd11e4b record_sha256:146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "raw_available": {
      "check_name": "raw_available",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "source:source_886372de22c708b28cd11e4b raw_sha256:8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "check_name": "related_object_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_886372de22c708b28cd11e4b",
        "related:claim_via_interface_first_robot_control_20260715"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "schema_validated": {
      "check_name": "schema_validated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "validated:vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "check_name": "source_independence_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "method": "logical-work-identity-count",
      "semantic_recheck_performed": null,
      "validation_outcome": "not_established",
      "warnings": []
    }
  },
  "checks": {
    "contradiction_search_completed": true,
    "drift_checked": true,
    "duplicate_search_completed": true,
    "evidence_entailment_rechecked": true,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-19T23:49:35+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "95feba5a05ecc5129668a88e31b509e0b550587ded329c278a4951d8c3a64bd8",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "5aefae10e953ba94a27a1957d9a7e0e2782596f5335d723df9b72b7c5f7ad4bc",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce"
    },
    "relation_neighborhood_sha256": "fad9dd59e3f5387f42c3d5dfda3dc87b69dbb2daa3eae196c3c2804bad1be7ce",
    "source_record_sha256s": {
      "source_886372de22c708b28cd11e4b": "146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47"
    },
    "source_state_sha256": "2c1d5a1611b979bfa12bd80bdcd045ae13a50279235effce03d27c1de032b27b",
    "work_identity_sha256": "0e75745f4a921bc49fff188ed681101ff1d53ce348dfc8cf91608a5cb8aadb22"
  },
  "consolidation_id": "consolidation_a846a5dcdd8df6febeac4a83",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T23:49:35+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a846a5dcdd8df6febeac4a83",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_34abf7a170a7e0fc0492fc16",
  "object_sha256_after": "95feba5a05ecc5129668a88e31b509e0b550587ded329c278a4951d8c3a64bd8",
  "object_sha256_before": "fb84ae26a30e2bb2ba49918be337d0c62b69ca0cd45cbd930b4fd48242ef6b9f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_886372de22c708b28cd11e4b"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939",
      "source_id": "source_886372de22c708b28cd11e4b",
      "source_record_sha256": "146eced484d2ac987945d682dee0c43e4deaa80aecf28eb1d28feaa4b0e10e47",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939"
  ],
  "started_at": "2026-07-19T23:49:34+08:00",
  "status": "complete",
  "title": "Consolidation: 指向式视觉导航接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T23:49:35+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
