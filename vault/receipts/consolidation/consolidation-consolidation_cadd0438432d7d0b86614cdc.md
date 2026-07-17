---
id: "consolidation_cadd0438432d7d0b86614cdc"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "failed"
execution_status: "complete"
validation_outcome: "failed"
title: "Consolidation: Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点"
created_at: "2026-07-17T18:38:35+08:00"
updated_at: "2026-07-17T18:38:35+08:00"
consolidation_id: "consolidation_cadd0438432d7d0b86614cdc"
object_id: "claim_agentic_vla_libero_main_20260715"
object_version_before: 1
object_sha256_before: "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068"
object_sha256_after: "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068"
source_ids: ["source_2c21320690e566fbbf80fd75"]
source_sha256s: ["8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"]
source_records: [{"source_id": "source_2c21320690e566fbbf80fd75", "source_record_sha256": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513", "raw_content_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:38:35+08:00"
completed_at: "2026-07-17T18:38:35+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": false, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_agentic_vla_libero_main_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_2c21320690e566fbbf80fd75 raw_sha256:8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_2c21320690e566fbbf80fd75 record_sha256:f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:source_2c21320690e566fbbf80fd75", "evidence:source_2c21320690e566fbbf80fd75", "evidence:source_2c21320690e566fbbf80fd75"], "warnings": []}, "evidence_entailment_rechecked": {"status": "failed", "findings": ["evidence_entailment:None"], "warnings": ["claim evidence entailment not checked"]}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_agentic_vla_libero_main_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_2c21320690e566fbbf80fd75"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:38+08:00", "source:source_2c21320690e566fbbf80fd75 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068", "source_state_sha256": "b183c849f4701693c7977f37650b2427587f12431d50db110182a346f4a1e459", "source_record_sha256s": {"source_2c21320690e566fbbf80fd75": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"}, "raw_state_sha256": "66319a8bb37a86a1f09fd9d17bb01f137b5d583ba9e3e9780a968dad976028c8", "evidence_sha256": "872764e82f9c86e0d72c6cf2fde09008e59e64a1c5279f84ed07b118fbb9d5b6", "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283", "work_identity_sha256": "a08f1abff1e75024db50cdcd272ee91bce2e46d9ce1813171e887755926028f0", "relation_neighborhood_sha256": "980b949455d75ea9cac424a29191613f5f5cbdf23064a5f7b5956b60b7db605d", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "failed"
changes: []
change_summary: "No semantic change."
warnings: ["claim evidence entailment not checked"]
exceptions_created: []
promotion_recommendation: "blocked"
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
        "candidate:claim_agentic_vla_libero_main_20260715"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:None"
      ],
      "status": "failed",
      "warnings": [
        "claim evidence entailment not checked"
      ]
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:source_2c21320690e566fbbf80fd75",
        "evidence:source_2c21320690e566fbbf80fd75",
        "evidence:source_2c21320690e566fbbf80fd75"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:38+08:00",
        "source:source_2c21320690e566fbbf80fd75 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_2c21320690e566fbbf80fd75 record_sha256:f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_2c21320690e566fbbf80fd75 raw_sha256:8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_2c21320690e566fbbf80fd75"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_agentic_vla_libero_main_20260715.md"
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
    "evidence_entailment_rechecked": false,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-17T18:38:35+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "872764e82f9c86e0d72c6cf2fde09008e59e64a1c5279f84ed07b118fbb9d5b6",
    "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283",
    "memory_schema_version": 2,
    "object_sha256": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "66319a8bb37a86a1f09fd9d17bb01f137b5d583ba9e3e9780a968dad976028c8",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "980b949455d75ea9cac424a29191613f5f5cbdf23064a5f7b5956b60b7db605d",
    "source_record_sha256s": {
      "source_2c21320690e566fbbf80fd75": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"
    },
    "source_state_sha256": "b183c849f4701693c7977f37650b2427587f12431d50db110182a346f4a1e459",
    "work_identity_sha256": "a08f1abff1e75024db50cdcd272ee91bce2e46d9ce1813171e887755926028f0"
  },
  "consolidation_id": "consolidation_cadd0438432d7d0b86614cdc",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:38:35+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_cadd0438432d7d0b86614cdc",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_agentic_vla_libero_main_20260715",
  "object_sha256_after": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
  "object_sha256_before": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
  "object_version_before": 1,
  "promotion_recommendation": "blocked",
  "receipt_schema_version": 2,
  "result": "failed",
  "source_ids": [
    "source_2c21320690e566fbbf80fd75"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43",
      "source_id": "source_2c21320690e566fbbf80fd75",
      "source_record_sha256": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"
  ],
  "started_at": "2026-07-17T18:38:35+08:00",
  "status": "failed",
  "title": "Consolidation: Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:38:35+08:00",
  "validation_outcome": "failed",
  "warnings": [
    "claim evidence entailment not checked"
  ]
}
```
