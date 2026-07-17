---
id: "consolidation_910cc80f05459439514c891f"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期"
created_at: "2026-07-17T18:35:46+08:00"
updated_at: "2026-07-17T18:35:46+08:00"
consolidation_id: "consolidation_910cc80f05459439514c891f"
object_id: "claim_wechat_kairos_sim2real_training_20260716"
object_version_before: 1
object_sha256_before: "23e63958e3d3a055858e788ac659105cff778324809e80400b79177c849f4bf9"
object_sha256_after: "52112a5c143fda2fa2eafa9f1a9b33111f83c6188ae20a7c3a597de302a602b1"
source_ids: ["source_a20c5fb22d91216503d413e1"]
source_sha256s: ["10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"]
source_records: [{"source_id": "source_a20c5fb22d91216503d413e1", "source_record_sha256": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819", "raw_content_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_457", "ev_463"]
started_at: "2026-07-17T18:35:46+08:00"
completed_at: "2026-07-17T18:35:46+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_a20c5fb22d91216503d413e1 raw_sha256:10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_a20c5fb22d91216503d413e1 record_sha256:b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_457", "evidence:ev_463"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_kairos_sim2real_training_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_a20c5fb22d91216503d413e1"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:53+08:00", "source:source_a20c5fb22d91216503d413e1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "52112a5c143fda2fa2eafa9f1a9b33111f83c6188ae20a7c3a597de302a602b1", "source_state_sha256": "e897544983ccb657ee0d6eb13ed573ec3dce341b0ceef0d02b44d48f6c53622c", "source_record_sha256s": {"source_a20c5fb22d91216503d413e1": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"}, "raw_state_sha256": "17d5650d83a78eda91e65d61b010a1ecec820b5b588e69f6171c8c72eabd3d8a", "evidence_sha256": "d0cfe0407ca83677c069e972690d3115f11fe45a7feadfa94790cdfdb9e1f573", "extraction_state_sha256": "ce82a0132ad781e9e698e8527df218c19e55e914bbd661cbed855831af06be73", "work_identity_sha256": "5ae407b131e09514fa6474a1a3b0640942ef50ece81eb9f9b853be43c7cc1e01", "relation_neighborhood_sha256": "e1947a169780b8356c89d1e7d284023ac96a8a41a0463137c34764c0b9cac919", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_kairos_sim2real_training_20260716"
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
        "evidence:ev_457",
        "evidence:ev_463"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:53+08:00",
        "source:source_a20c5fb22d91216503d413e1 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_a20c5fb22d91216503d413e1 record_sha256:b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_a20c5fb22d91216503d413e1 raw_sha256:10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_a20c5fb22d91216503d413e1"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md"
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
  "completed_at": "2026-07-17T18:35:46+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "d0cfe0407ca83677c069e972690d3115f11fe45a7feadfa94790cdfdb9e1f573",
    "extraction_state_sha256": "ce82a0132ad781e9e698e8527df218c19e55e914bbd661cbed855831af06be73",
    "memory_schema_version": 2,
    "object_sha256": "52112a5c143fda2fa2eafa9f1a9b33111f83c6188ae20a7c3a597de302a602b1",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "17d5650d83a78eda91e65d61b010a1ecec820b5b588e69f6171c8c72eabd3d8a",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "e1947a169780b8356c89d1e7d284023ac96a8a41a0463137c34764c0b9cac919",
    "source_record_sha256s": {
      "source_a20c5fb22d91216503d413e1": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"
    },
    "source_state_sha256": "e897544983ccb657ee0d6eb13ed573ec3dce341b0ceef0d02b44d48f6c53622c",
    "work_identity_sha256": "5ae407b131e09514fa6474a1a3b0640942ef50ece81eb9f9b853be43c7cc1e01"
  },
  "consolidation_id": "consolidation_910cc80f05459439514c891f",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:46+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_457",
    "ev_463"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_910cc80f05459439514c891f",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_kairos_sim2real_training_20260716",
  "object_sha256_after": "52112a5c143fda2fa2eafa9f1a9b33111f83c6188ae20a7c3a597de302a602b1",
  "object_sha256_before": "23e63958e3d3a055858e788ac659105cff778324809e80400b79177c849f4bf9",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_a20c5fb22d91216503d413e1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8",
      "source_id": "source_a20c5fb22d91216503d413e1",
      "source_record_sha256": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"
  ],
  "started_at": "2026-07-17T18:35:46+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:46+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
