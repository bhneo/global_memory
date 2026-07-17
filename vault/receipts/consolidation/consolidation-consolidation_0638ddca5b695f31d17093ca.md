---
id: "consolidation_0638ddca5b695f31d17093ca"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线"
created_at: "2026-07-17T18:35:41+08:00"
updated_at: "2026-07-17T18:35:41+08:00"
consolidation_id: "consolidation_0638ddca5b695f31d17093ca"
object_id: "claim_wechat_embodied_data_quality_cost_tradeoff_20260716"
object_version_before: 1
object_sha256_before: "97f02271c3769ff20d1b47aa9d2a1f9e8d73deb949c7ecebf1592c1b772742a6"
object_sha256_after: "7b3d640d13ec7716985255aab654c72fc0d3b68a2c66ff414ee874751840765e"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
source_sha256s: ["4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"]
source_records: [{"source_id": "source_cda5a1b9e036598aff53e5be", "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1", "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_266", "ev_21"]
started_at: "2026-07-17T18:35:41+08:00"
completed_at: "2026-07-17T18:35:41+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_266", "evidence:ev_21"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_embodied_data_quality_cost_tradeoff_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_cda5a1b9e036598aff53e5be"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:49+08:00", "source:source_cda5a1b9e036598aff53e5be work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "7b3d640d13ec7716985255aab654c72fc0d3b68a2c66ff414ee874751840765e", "source_state_sha256": "32ba1356a827bd0c897cc3fe711b2b4b08f24b823aca805b78e6f020a3ae12ee", "source_record_sha256s": {"source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"}, "raw_state_sha256": "9a86b21f3396d91af6a552924e8f5b0167f9bb6641062936f751031d9ae1ad18", "evidence_sha256": "d591b6a11cdfb79f14af564b8716d3d27849463bc7935ecfc0cc953a995a19b6", "extraction_state_sha256": "1f7b1b2e9c7b4b288a21b41203be2a85902c26c49c2b21d01e43a97e5b52b5af", "work_identity_sha256": "95baeea6e0d387d195b8786cb0bc900a283534e962bf21d9b789a4d357dd03ac", "relation_neighborhood_sha256": "1454e56474bb991376f7869e477288fb4b9c300b7c871e30183278d7df2c5b56", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_embodied_data_quality_cost_tradeoff_20260716"
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
        "evidence:ev_266",
        "evidence:ev_21"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:49+08:00",
        "source:source_cda5a1b9e036598aff53e5be work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_cda5a1b9e036598aff53e5be"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md"
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
  "completed_at": "2026-07-17T18:35:41+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "d591b6a11cdfb79f14af564b8716d3d27849463bc7935ecfc0cc953a995a19b6",
    "extraction_state_sha256": "1f7b1b2e9c7b4b288a21b41203be2a85902c26c49c2b21d01e43a97e5b52b5af",
    "memory_schema_version": 2,
    "object_sha256": "7b3d640d13ec7716985255aab654c72fc0d3b68a2c66ff414ee874751840765e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9a86b21f3396d91af6a552924e8f5b0167f9bb6641062936f751031d9ae1ad18",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "1454e56474bb991376f7869e477288fb4b9c300b7c871e30183278d7df2c5b56",
    "source_record_sha256s": {
      "source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"
    },
    "source_state_sha256": "32ba1356a827bd0c897cc3fe711b2b4b08f24b823aca805b78e6f020a3ae12ee",
    "work_identity_sha256": "95baeea6e0d387d195b8786cb0bc900a283534e962bf21d9b789a4d357dd03ac"
  },
  "consolidation_id": "consolidation_0638ddca5b695f31d17093ca",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:41+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_266",
    "ev_21"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_0638ddca5b695f31d17093ca",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716",
  "object_sha256_after": "7b3d640d13ec7716985255aab654c72fc0d3b68a2c66ff414ee874751840765e",
  "object_sha256_before": "97f02271c3769ff20d1b47aa9d2a1f9e8d73deb949c7ecebf1592c1b772742a6",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_cda5a1b9e036598aff53e5be"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5",
      "source_id": "source_cda5a1b9e036598aff53e5be",
      "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"
  ],
  "started_at": "2026-07-17T18:35:41+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:41+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
