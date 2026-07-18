---
id: "consolidation_551d34194f20ecd390c38ca4"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 遍历性与非遍历性"
created_at: "2026-07-18T16:03:12+08:00"
updated_at: "2026-07-18T16:03:12+08:00"
consolidation_id: "consolidation_551d34194f20ecd390c38ca4"
object_id: "concept_ergodicity"
object_version_before: 1
object_sha256_before: "2db23eed3cf30c80fb6e7f389af9ed07d4f3748d77647c61d10b81f65f66e7ce"
object_sha256_after: "38368635c3d0519ffeb9cdb21cfec168d9c1f52c662b05f2b00610d7b41845ac"
source_ids: ["source_9d39636775b188c87d6a001f"]
source_sha256s: ["0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"]
source_records: [{"source_id": "source_9d39636775b188c87d6a001f", "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:11+08:00"
completed_at: "2026-07-18T16:03:12+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_ergodicity.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_ergodicity"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 5 related objects found", "related:source_9d39636775b188c87d6a001f", "related:concept_ergodicity", "related:concept_ergodicity", "related:concept_ergodicity", "related:concept_ergodicity"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:54+08:00", "source:source_9d39636775b188c87d6a001f work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "38368635c3d0519ffeb9cdb21cfec168d9c1f52c662b05f2b00610d7b41845ac", "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8", "source_record_sha256s": {"source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"}, "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4", "relation_fingerprint": {"outgoing_relations_sha256": "36312c4a8b0d98a556bca544c795d989e36ebd16c3d430e57999c1b1e3e57193", "incoming_relations_sha256": "691de2297ad3d117feb087848fc34d897a0cea4ea4845288cd32cffe4a8bbda9", "full_neighborhood_sha256": "e7489589eecb72ed485269c9f32bc591a0850a256f2559ca5fd01e1e3ffe3425"}, "relation_neighborhood_sha256": "e7489589eecb72ed485269c9f32bc591a0850a256f2559ca5fd01e1e3ffe3425", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_ergodicity"
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
        "object_updated_at:2026-07-17T18:35:54+08:00",
        "source:source_9d39636775b188c87d6a001f work_sha256:none"
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
        "source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
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
        "source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"
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
        "relation index inspected; 5 related objects found",
        "related:source_9d39636775b188c87d6a001f",
        "related:concept_ergodicity",
        "related:concept_ergodicity",
        "related:concept_ergodicity",
        "related:concept_ergodicity"
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
        "validated:vault/memory/concept/concept_ergodicity.md"
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
  "completed_at": "2026-07-18T16:03:12+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "38368635c3d0519ffeb9cdb21cfec168d9c1f52c662b05f2b00610d7b41845ac",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "e7489589eecb72ed485269c9f32bc591a0850a256f2559ca5fd01e1e3ffe3425",
      "incoming_relations_sha256": "691de2297ad3d117feb087848fc34d897a0cea4ea4845288cd32cffe4a8bbda9",
      "outgoing_relations_sha256": "36312c4a8b0d98a556bca544c795d989e36ebd16c3d430e57999c1b1e3e57193"
    },
    "relation_neighborhood_sha256": "e7489589eecb72ed485269c9f32bc591a0850a256f2559ca5fd01e1e3ffe3425",
    "source_record_sha256s": {
      "source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
    },
    "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8",
    "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4"
  },
  "consolidation_id": "consolidation_551d34194f20ecd390c38ca4",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:12+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_551d34194f20ecd390c38ca4",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_ergodicity",
  "object_sha256_after": "38368635c3d0519ffeb9cdb21cfec168d9c1f52c662b05f2b00610d7b41845ac",
  "object_sha256_before": "2db23eed3cf30c80fb6e7f389af9ed07d4f3748d77647c61d10b81f65f66e7ce",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9d39636775b188c87d6a001f"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33",
      "source_id": "source_9d39636775b188c87d6a001f",
      "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"
  ],
  "started_at": "2026-07-18T16:03:11+08:00",
  "status": "complete",
  "title": "Consolidation: 遍历性与非遍历性",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:12+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
