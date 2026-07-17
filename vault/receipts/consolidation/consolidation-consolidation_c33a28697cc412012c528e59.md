---
id: "consolidation_c33a28697cc412012c528e59"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文将遍历性描述为个体时间平均与群体平均相等的条件"
created_at: "2026-07-17T18:35:43+08:00"
updated_at: "2026-07-17T18:35:43+08:00"
consolidation_id: "consolidation_c33a28697cc412012c528e59"
object_id: "claim_wechat_ergodicity_time_ensemble_equivalence_20260716"
object_version_before: 1
object_sha256_before: "7efacf160d00dfcc255eec2b178a11142c128a2a3c849ce58cb327b091d9239c"
object_sha256_after: "127d97941400a8465751b4d03c1fdcea32f77bd032ceb336c0edc7c46dfa7868"
source_ids: ["source_9d39636775b188c87d6a001f"]
source_sha256s: ["0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"]
source_records: [{"source_id": "source_9d39636775b188c87d6a001f", "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_631"]
started_at: "2026-07-17T18:35:43+08:00"
completed_at: "2026-07-17T18:35:43+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_ergodicity_time_ensemble_equivalence_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_631"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_ergodicity_time_ensemble_equivalence_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_9d39636775b188c87d6a001f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:51+08:00", "source:source_9d39636775b188c87d6a001f work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "127d97941400a8465751b4d03c1fdcea32f77bd032ceb336c0edc7c46dfa7868", "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8", "source_record_sha256s": {"source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"}, "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935", "evidence_sha256": "9f1b7cdc0def5fad74e412548e51f5443f513034c522a2e35997714c61d75d0c", "extraction_state_sha256": "306b2cbf6904eded6d61fc4e5d90bf833e981d2e57afa157d99e8c38ca5d2fbe", "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4", "relation_neighborhood_sha256": "836d277838677d61941e70f6648354cdd8881432bfe1c2c41f8624550c30dafe", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "status": "passed",
      "warnings": []
    },
    "drift_checked": {
      "findings": [
        "drift_reports:0"
      ],
      "status": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "findings": [
        "searched title; 1 candidates inspected",
        "candidate:claim_wechat_ergodicity_time_ensemble_equivalence_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:partial"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_631"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:51+08:00",
        "source:source_9d39636775b188c87d6a001f work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_9d39636775b188c87d6a001f"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_ergodicity_time_ensemble_equivalence_20260716.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "status": "passed",
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
  "completed_at": "2026-07-17T18:35:43+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "9f1b7cdc0def5fad74e412548e51f5443f513034c522a2e35997714c61d75d0c",
    "extraction_state_sha256": "306b2cbf6904eded6d61fc4e5d90bf833e981d2e57afa157d99e8c38ca5d2fbe",
    "memory_schema_version": 2,
    "object_sha256": "127d97941400a8465751b4d03c1fdcea32f77bd032ceb336c0edc7c46dfa7868",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "836d277838677d61941e70f6648354cdd8881432bfe1c2c41f8624550c30dafe",
    "source_record_sha256s": {
      "source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
    },
    "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8",
    "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4"
  },
  "consolidation_id": "consolidation_c33a28697cc412012c528e59",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:43+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_631"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_c33a28697cc412012c528e59",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_ergodicity_time_ensemble_equivalence_20260716",
  "object_sha256_after": "127d97941400a8465751b4d03c1fdcea32f77bd032ceb336c0edc7c46dfa7868",
  "object_sha256_before": "7efacf160d00dfcc255eec2b178a11142c128a2a3c849ce58cb327b091d9239c",
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
  "started_at": "2026-07-17T18:35:43+08:00",
  "status": "complete",
  "title": "Consolidation: 该文将遍历性描述为个体时间平均与群体平均相等的条件",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:43+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
