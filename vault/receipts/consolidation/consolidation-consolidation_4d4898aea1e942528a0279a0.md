---
id: "consolidation_4d4898aea1e942528a0279a0"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 机器人策略的测试时快速权重记忆"
created_at: "2026-07-26T12:34:01+08:00"
updated_at: "2026-07-26T12:34:01+08:00"
consolidation_id: "consolidation_4d4898aea1e942528a0279a0"
object_id: "concept_test_time_fast_weight_robot_memory"
object_version_before: 1
object_sha256_before: "33377e8809797d2b7219bc42132cfe4f61c924509dd26f9ae045d1e66954132c"
object_sha256_after: "155596a63172548089c391d0665195de0290645d539bc5b9fe18315426d4a376"
source_ids: ["source_79475aef7849b08664b51a4e"]
source_sha256s: ["6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"]
source_records: [{"source_id": "source_79475aef7849b08664b51a4e", "source_record_sha256": "ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc", "raw_content_sha256": "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:34:01+08:00"
completed_at: "2026-07-26T12:34:01+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_test_time_fast_weight_robot_memory.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_79475aef7849b08664b51a4e raw_sha256:6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_79475aef7849b08664b51a4e record_sha256:ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_test_time_fast_weight_robot_memory"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_79475aef7849b08664b51a4e", "related:concept_native_action_aligned_vla_memory"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-21T17:41:52+08:00", "source:source_79475aef7849b08664b51a4e work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "155596a63172548089c391d0665195de0290645d539bc5b9fe18315426d4a376", "source_state_sha256": "4660c9a64869e9289246dcfd576495449d2689b652b8038252ed7651f1ebd7fa", "source_record_sha256s": {"source_79475aef7849b08664b51a4e": "ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc"}, "raw_state_sha256": "be1f199327351ee72e8497147de929215fa974f1e72c1eae7e1386fb45d7b0b9", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "88b3a0e58f1196fcb6671aa2ea72f27b5ef415175b587dcb9044a9ef6105d094", "relation_fingerprint": {"outgoing_relations_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904"}, "relation_neighborhood_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_test_time_fast_weight_robot_memory"
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
        "object_updated_at:2026-07-21T17:41:52+08:00",
        "source:source_79475aef7849b08664b51a4e work_sha256:none"
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
        "source:source_79475aef7849b08664b51a4e record_sha256:ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc"
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
        "source:source_79475aef7849b08664b51a4e raw_sha256:6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"
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
        "related:source_79475aef7849b08664b51a4e",
        "related:concept_native_action_aligned_vla_memory"
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
        "validated:vault/memory/concept/concept_test_time_fast_weight_robot_memory.md"
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
  "completed_at": "2026-07-26T12:34:01+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "155596a63172548089c391d0665195de0290645d539bc5b9fe18315426d4a376",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "be1f199327351ee72e8497147de929215fa974f1e72c1eae7e1386fb45d7b0b9",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904"
    },
    "relation_neighborhood_sha256": "7f9109c334b06552c8aa8cea501c02b9c81d9ea9436c327886b2737440d2f904",
    "source_record_sha256s": {
      "source_79475aef7849b08664b51a4e": "ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc"
    },
    "source_state_sha256": "4660c9a64869e9289246dcfd576495449d2689b652b8038252ed7651f1ebd7fa",
    "work_identity_sha256": "88b3a0e58f1196fcb6671aa2ea72f27b5ef415175b587dcb9044a9ef6105d094"
  },
  "consolidation_id": "consolidation_4d4898aea1e942528a0279a0",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:34:01+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4d4898aea1e942528a0279a0",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_test_time_fast_weight_robot_memory",
  "object_sha256_after": "155596a63172548089c391d0665195de0290645d539bc5b9fe18315426d4a376",
  "object_sha256_before": "33377e8809797d2b7219bc42132cfe4f61c924509dd26f9ae045d1e66954132c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_79475aef7849b08664b51a4e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0",
      "source_id": "source_79475aef7849b08664b51a4e",
      "source_record_sha256": "ad52c88470ccc430e4386893094b36c9a8d56d197d25ec8e5813949fb60359fc",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"
  ],
  "started_at": "2026-07-26T12:34:01+08:00",
  "status": "complete",
  "title": "Consolidation: 机器人策略的测试时快速权重记忆",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:34:01+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
