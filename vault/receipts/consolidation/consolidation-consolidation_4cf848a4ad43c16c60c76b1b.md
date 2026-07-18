---
id: "consolidation_4cf848a4ad43c16c60c76b1b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 符号回归"
created_at: "2026-07-18T16:03:17+08:00"
updated_at: "2026-07-18T16:03:17+08:00"
consolidation_id: "consolidation_4cf848a4ad43c16c60c76b1b"
object_id: "concept_symbolic_regression"
object_version_before: 1
object_sha256_before: "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0"
object_sha256_after: "8ecb4b7da201da6fd515a73c21dc630dc6663338dd21920e096a1e7a00cdc832"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
source_sha256s: ["fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"]
source_records: [{"source_id": "source_ef99e322cc662cffb7eb5c8f", "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:17+08:00"
completed_at: "2026-07-18T16:03:17+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_symbolic_regression.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_symbolic_regression", "candidate:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:59+08:00", "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "8ecb4b7da201da6fd515a73c21dc630dc6663338dd21920e096a1e7a00cdc832", "source_state_sha256": "76d949421d93db35360c432eb5236e0804a0eba6c9af4a71469ad0285b5c3853", "source_record_sha256s": {"source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"}, "raw_state_sha256": "64308cc5642ef54084259d6818b79d8290fef9640c962e0fe5e03d8b8f1eb89d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "39e6164de950be7117eaaed37d34f224264371f72a2abfe6026e74f36a6e8d7a", "relation_fingerprint": {"outgoing_relations_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967"}, "relation_neighborhood_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:concept_symbolic_regression",
        "candidate:source_ef99e322cc662cffb7eb5c8f"
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
        "object_updated_at:2026-07-17T18:35:59+08:00",
        "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none"
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
        "source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
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
        "source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"
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
        "relation index inspected; 1 related objects found",
        "related:source_ef99e322cc662cffb7eb5c8f"
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
        "validated:vault/memory/concept/concept_symbolic_regression.md"
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
  "completed_at": "2026-07-18T16:03:17+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "8ecb4b7da201da6fd515a73c21dc630dc6663338dd21920e096a1e7a00cdc832",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "64308cc5642ef54084259d6818b79d8290fef9640c962e0fe5e03d8b8f1eb89d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967"
    },
    "relation_neighborhood_sha256": "c9558a1acc695f4cafcf22765d4d0bff299cb9ee0107bcc180ee166190f73967",
    "source_record_sha256s": {
      "source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
    },
    "source_state_sha256": "76d949421d93db35360c432eb5236e0804a0eba6c9af4a71469ad0285b5c3853",
    "work_identity_sha256": "39e6164de950be7117eaaed37d34f224264371f72a2abfe6026e74f36a6e8d7a"
  },
  "consolidation_id": "consolidation_4cf848a4ad43c16c60c76b1b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:17+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4cf848a4ad43c16c60c76b1b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_symbolic_regression",
  "object_sha256_after": "8ecb4b7da201da6fd515a73c21dc630dc6663338dd21920e096a1e7a00cdc832",
  "object_sha256_before": "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ef99e322cc662cffb7eb5c8f"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
      "source_id": "source_ef99e322cc662cffb7eb5c8f",
      "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"
  ],
  "started_at": "2026-07-18T16:03:17+08:00",
  "status": "complete",
  "title": "Consolidation: 符号回归",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:17+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
