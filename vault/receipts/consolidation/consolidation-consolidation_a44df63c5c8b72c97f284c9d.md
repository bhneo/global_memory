---
id: "consolidation_a44df63c5c8b72c97f284c9d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称非遍历情形中个体可能在经历全部路径前因一次失败出局"
created_at: "2026-07-17T18:35:49+08:00"
updated_at: "2026-07-17T18:35:49+08:00"
consolidation_id: "consolidation_a44df63c5c8b72c97f284c9d"
object_id: "claim_wechat_nonergodic_failure_exit_20260716"
object_version_before: 1
object_sha256_before: "1166f1a26e7967fcf8a51d1b58180ae2ec9a7cc0ec2c4faf108c7d03d118dd21"
object_sha256_after: "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad"
source_ids: ["source_9d39636775b188c87d6a001f"]
source_sha256s: ["0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"]
source_records: [{"source_id": "source_9d39636775b188c87d6a001f", "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_844"]
started_at: "2026-07-17T18:35:48+08:00"
completed_at: "2026-07-17T18:35:49+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_nonergodic_failure_exit_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_844"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_nonergodic_failure_exit_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_9d39636775b188c87d6a001f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:55+08:00", "source:source_9d39636775b188c87d6a001f work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad", "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8", "source_record_sha256s": {"source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"}, "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935", "evidence_sha256": "25d45151c35094150e7f4e7814723e440d19646e3631066b8b04cb531103476b", "extraction_state_sha256": "e86eedcc1f95270da76824a513fb1f5139e4a5bb14a8a782a4ac889927383616", "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4", "relation_neighborhood_sha256": "0da87d5f03467a08a2dc0cba1f4e570a8be3c36e56eea0412c5fa366a75c56c7", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_nonergodic_failure_exit_20260716"
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
        "evidence:ev_844"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:55+08:00",
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
        "validated:vault/memory/claim/claim_wechat_nonergodic_failure_exit_20260716.md"
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
  "completed_at": "2026-07-17T18:35:49+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "25d45151c35094150e7f4e7814723e440d19646e3631066b8b04cb531103476b",
    "extraction_state_sha256": "e86eedcc1f95270da76824a513fb1f5139e4a5bb14a8a782a4ac889927383616",
    "memory_schema_version": 2,
    "object_sha256": "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a3f1cff923aeb835c0e511147247992a41169e1cc8f74ed80848d9f4582ae935",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "0da87d5f03467a08a2dc0cba1f4e570a8be3c36e56eea0412c5fa366a75c56c7",
    "source_record_sha256s": {
      "source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
    },
    "source_state_sha256": "f29af245ab5ebc6b18532e62280ecaee9303dbd11c76d0119e5daa2059c769c8",
    "work_identity_sha256": "5964e2fe804ac780815f2480881504972cbdedbc6101df4dac289a63a0813ea4"
  },
  "consolidation_id": "consolidation_a44df63c5c8b72c97f284c9d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:49+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_844"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a44df63c5c8b72c97f284c9d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_nonergodic_failure_exit_20260716",
  "object_sha256_after": "349d35b060ea414a710cb1ffd7cc2d0d653f254e722a02b2e57429acf5961fad",
  "object_sha256_before": "1166f1a26e7967fcf8a51d1b58180ae2ec9a7cc0ec2c4faf108c7d03d118dd21",
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
  "started_at": "2026-07-17T18:35:48+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称非遍历情形中个体可能在经历全部路径前因一次失败出局",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:49+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
