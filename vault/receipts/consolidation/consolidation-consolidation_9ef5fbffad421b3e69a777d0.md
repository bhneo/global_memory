---
id: "consolidation_9ef5fbffad421b3e69a777d0"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 主动真机因子评测"
created_at: "2026-07-26T12:33:46+08:00"
updated_at: "2026-07-26T12:33:46+08:00"
consolidation_id: "consolidation_9ef5fbffad421b3e69a777d0"
object_id: "concept_d5965e0770273320ea6b28f2"
object_version_before: 1
object_sha256_before: "c657b26233610a34feddffb8047e13f08269a81d6f6819ad409ac2fc829d2034"
object_sha256_after: "348e22e7352d5621adea926a14dd5a7ed568a5d1bc3c42efb2d429599774fe46"
source_ids: ["source_61152ca8210ad3913764a291"]
source_sha256s: ["ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3"]
source_records: [{"source_id": "source_61152ca8210ad3913764a291", "source_record_sha256": "72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936", "raw_content_sha256": "ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:45+08:00"
completed_at: "2026-07-26T12:33:46+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_d5965e0770273320ea6b28f2.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_61152ca8210ad3913764a291 raw_sha256:ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_61152ca8210ad3913764a291 record_sha256:72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_d5965e0770273320ea6b28f2", "candidate:reflection_a7089c995e52da14c2ce2609"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_61152ca8210ad3913764a291", "related:concept_real_robot_deployment_iteration_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T18:05:29+08:00", "source:source_61152ca8210ad3913764a291 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "348e22e7352d5621adea926a14dd5a7ed568a5d1bc3c42efb2d429599774fe46", "source_state_sha256": "2257283026cbb95019deaabac291116b58f1ab0ab86f84833bb376b7bb4f06ec", "source_record_sha256s": {"source_61152ca8210ad3913764a291": "72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936"}, "raw_state_sha256": "9727d02119efa2ef3b299e30886be4da8dd7dbb4e149085a3e9c8dcf2de08c9e", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "8f612e2de6db2c6251b3a5306d224018b393dde29dbb0ef7dd16c40dd180376f", "relation_fingerprint": {"outgoing_relations_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4"}, "relation_neighborhood_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_d5965e0770273320ea6b28f2",
        "candidate:reflection_a7089c995e52da14c2ce2609"
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
        "object_updated_at:2026-07-20T18:05:29+08:00",
        "source:source_61152ca8210ad3913764a291 work_sha256:none"
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
        "source:source_61152ca8210ad3913764a291 record_sha256:72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936"
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
        "source:source_61152ca8210ad3913764a291 raw_sha256:ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3"
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
        "related:source_61152ca8210ad3913764a291",
        "related:concept_real_robot_deployment_iteration_loop"
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
        "validated:vault/memory/concept/concept_d5965e0770273320ea6b28f2.md"
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
  "completed_at": "2026-07-26T12:33:46+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "348e22e7352d5621adea926a14dd5a7ed568a5d1bc3c42efb2d429599774fe46",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9727d02119efa2ef3b299e30886be4da8dd7dbb4e149085a3e9c8dcf2de08c9e",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4"
    },
    "relation_neighborhood_sha256": "8f868a6e4405df8b1bdfdfd0bdfa1d07f8623133438def4058b0225bc72c14c4",
    "source_record_sha256s": {
      "source_61152ca8210ad3913764a291": "72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936"
    },
    "source_state_sha256": "2257283026cbb95019deaabac291116b58f1ab0ab86f84833bb376b7bb4f06ec",
    "work_identity_sha256": "8f612e2de6db2c6251b3a5306d224018b393dde29dbb0ef7dd16c40dd180376f"
  },
  "consolidation_id": "consolidation_9ef5fbffad421b3e69a777d0",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:46+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_9ef5fbffad421b3e69a777d0",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_d5965e0770273320ea6b28f2",
  "object_sha256_after": "348e22e7352d5621adea926a14dd5a7ed568a5d1bc3c42efb2d429599774fe46",
  "object_sha256_before": "c657b26233610a34feddffb8047e13f08269a81d6f6819ad409ac2fc829d2034",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_61152ca8210ad3913764a291"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3",
      "source_id": "source_61152ca8210ad3913764a291",
      "source_record_sha256": "72d9c3662b5da6e91635fe3327427e40baa6ca2b98c3783554a33230ba08c936",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3"
  ],
  "started_at": "2026-07-26T12:33:45+08:00",
  "status": "complete",
  "title": "Consolidation: 主动真机因子评测",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:46+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
