---
id: "consolidation_f8ea9d647fc6a8f0735d54ef"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称非遍历情形中个体可能在经历全部路径前因一次失败出局"
created_at: "2026-07-18T16:03:07+08:00"
updated_at: "2026-07-18T16:03:07+08:00"
consolidation_id: "consolidation_f8ea9d647fc6a8f0735d54ef"
object_id: "claim_wechat_nonergodic_failure_exit_20260716"
object_version_before: 1
object_sha256_before: "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad"
object_sha256_after: "db1d01a8bcc20786dc1b34419ad07c47eb41bb08e83a3e10d4428fd97fa0c87a"
source_ids: ["source_9d39636775b188c87d6a001f"]
source_sha256s: ["0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"]
source_records: [{"source_id": "source_9d39636775b188c87d6a001f", "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_844"]
started_at: "2026-07-18T16:03:07+08:00"
completed_at: "2026-07-18T16:03:07+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_wechat_nonergodic_failure_exit_20260716.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_844"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "partial", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_nonergodic_failure_exit_20260716"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_9d39636775b188c87d6a001f"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:49+08:00", "source:source_9d39636775b188c87d6a001f work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "db1d01a8bcc20786dc1b34419ad07c47eb41bb08e83a3e10d4428fd97fa0c87a", "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8", "source_record_sha256s": {"source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"}, "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935", "evidence_sha256": "25d45151c35094150e7f4e7814723e440d19646e3631066b8b04cb531103476b", "extraction_state_sha256": "e86eedcc1f95270da76824a513fb1f5139e4a5bb14a8a782a4ac889927383616", "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4", "relation_fingerprint": {"outgoing_relations_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8"}, "relation_neighborhood_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_nonergodic_failure_exit_20260716"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "partial",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:partial"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:ev_844"
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
        "object_updated_at:2026-07-17T18:35:49+08:00",
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
        "relation index inspected; 1 related objects found",
        "related:source_9d39636775b188c87d6a001f"
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
        "validated:vault/memory/claim/claim_wechat_nonergodic_failure_exit_20260716.md"
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
      "validation_outcome": "not_applicable",
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
  "completed_at": "2026-07-18T16:03:07+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "25d45151c35094150e7f4e7814723e440d19646e3631066b8b04cb531103476b",
    "extraction_state_sha256": "e86eedcc1f95270da76824a513fb1f5139e4a5bb14a8a782a4ac889927383616",
    "memory_schema_version": 2,
    "object_sha256": "db1d01a8bcc20786dc1b34419ad07c47eb41bb08e83a3e10d4428fd97fa0c87a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8"
    },
    "relation_neighborhood_sha256": "4912f205048a435f8d649eb9ee3a4076e9859c854c800a2c9bf2dbbf484de8f8",
    "source_record_sha256s": {
      "source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
    },
    "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8",
    "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4"
  },
  "consolidation_id": "consolidation_f8ea9d647fc6a8f0735d54ef",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:07+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_844"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f8ea9d647fc6a8f0735d54ef",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_nonergodic_failure_exit_20260716",
  "object_sha256_after": "db1d01a8bcc20786dc1b34419ad07c47eb41bb08e83a3e10d4428fd97fa0c87a",
  "object_sha256_before": "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad",
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
  "started_at": "2026-07-18T16:03:07+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称非遍历情形中个体可能在经历全部路径前因一次失败出局",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:07+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
