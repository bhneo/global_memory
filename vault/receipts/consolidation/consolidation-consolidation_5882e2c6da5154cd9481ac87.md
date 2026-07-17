---
id: "consolidation_5882e2c6da5154cd9481ac87"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本"
created_at: "2026-07-17T18:38:31+08:00"
updated_at: "2026-07-17T18:38:31+08:00"
consolidation_id: "consolidation_5882e2c6da5154cd9481ac87"
object_id: "claim_wechat_skillevolver_silent_bypass_audit_20260716"
object_version_before: 1
object_sha256_before: "55efaa8f434e771de7799e46a1c083e82c61e53eab00a339cd73bd8bfa316cb2"
object_sha256_after: "29e179c53560f47e472a54847d7caf8db39eea050d8b00c83c8098a681d66bcb"
source_ids: ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"]
source_sha256s: ["f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"]
source_records: [{"source_id": "source_d01f40e4896de2e186cbbe8a", "source_record_sha256": "e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4", "raw_content_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "work_id": null, "work_document_sha256": null}, {"source_id": "source_ca1f80f2bf2e7d410ab2459e", "source_record_sha256": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a", "raw_content_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_7663", "ev_primary_cc70d0b65105"]
started_at: "2026-07-17T18:38:30+08:00"
completed_at: "2026-07-17T18:38:31+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_skillevolver_silent_bypass_audit_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_d01f40e4896de2e186cbbe8a raw_sha256:f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "source:source_ca1f80f2bf2e7d410ab2459e raw_sha256:4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_d01f40e4896de2e186cbbe8a record_sha256:e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4", "source:source_ca1f80f2bf2e7d410ab2459e record_sha256:493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_7663", "evidence:ev_primary_cc70d0b65105"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_skillevolver_silent_bypass_audit_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_ca1f80f2bf2e7d410ab2459e", "related:source_d01f40e4896de2e186cbbe8a"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:38:24+08:00", "source:source_d01f40e4896de2e186cbbe8a work_sha256:none", "source:source_ca1f80f2bf2e7d410ab2459e work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "29e179c53560f47e472a54847d7caf8db39eea050d8b00c83c8098a681d66bcb", "source_state_sha256": "7f46c89bc6dbdfcdac2cea0f5c220865ae812c058fea53cfa795ccd0c1efdb6e", "source_record_sha256s": {"source_d01f40e4896de2e186cbbe8a": "e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4", "source_ca1f80f2bf2e7d410ab2459e": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"}, "raw_state_sha256": "e943dfbf0446a244b07b031eaa0f2cd772cbb5203e9c4645706d62e07295bc21", "evidence_sha256": "3249e010b73d978e44b03b5a231ab7dc375fad499122a023e8e9f04bbfff5a5e", "extraction_state_sha256": "a38e89d385a28c159b98274eeb29ba6c2d437d5339597ea8d35820c332f4f55b", "work_identity_sha256": "2bbabee5d3564e9cc21fbf8575b85c0c589964939b560452f67f6d3f0a3d3406", "relation_neighborhood_sha256": "0924a0b1cff8ced95a754a202ec544355f09682759e29808192263a2c0b7dfe1", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalified"
changes: []
change_summary: "Trusted memory qualified under trusted-promotion-v3-receipt-v2"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Trusted memory qualified under trusted-promotion-v3-receipt-v2",
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
        "candidate:claim_wechat_skillevolver_silent_bypass_audit_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:full"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_7663",
        "evidence:ev_primary_cc70d0b65105"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T18:38:24+08:00",
        "source:source_d01f40e4896de2e186cbbe8a work_sha256:none",
        "source:source_ca1f80f2bf2e7d410ab2459e work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_d01f40e4896de2e186cbbe8a record_sha256:e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4",
        "source:source_ca1f80f2bf2e7d410ab2459e record_sha256:493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_d01f40e4896de2e186cbbe8a raw_sha256:f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0",
        "source:source_ca1f80f2bf2e7d410ab2459e raw_sha256:4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_ca1f80f2bf2e7d410ab2459e",
        "related:source_d01f40e4896de2e186cbbe8a"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_skillevolver_silent_bypass_audit_20260716.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-17T18:38:31+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "3249e010b73d978e44b03b5a231ab7dc375fad499122a023e8e9f04bbfff5a5e",
    "extraction_state_sha256": "a38e89d385a28c159b98274eeb29ba6c2d437d5339597ea8d35820c332f4f55b",
    "memory_schema_version": 2,
    "object_sha256": "29e179c53560f47e472a54847d7caf8db39eea050d8b00c83c8098a681d66bcb",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "e943dfbf0446a244b07b031eaa0f2cd772cbb5203e9c4645706d62e07295bc21",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "0924a0b1cff8ced95a754a202ec544355f09682759e29808192263a2c0b7dfe1",
    "source_record_sha256s": {
      "source_ca1f80f2bf2e7d410ab2459e": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a",
      "source_d01f40e4896de2e186cbbe8a": "e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4"
    },
    "source_state_sha256": "7f46c89bc6dbdfcdac2cea0f5c220865ae812c058fea53cfa795ccd0c1efdb6e",
    "work_identity_sha256": "2bbabee5d3564e9cc21fbf8575b85c0c589964939b560452f67f6d3f0a3d3406"
  },
  "consolidation_id": "consolidation_5882e2c6da5154cd9481ac87",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:38:31+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_7663",
    "ev_primary_cc70d0b65105"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_5882e2c6da5154cd9481ac87",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_skillevolver_silent_bypass_audit_20260716",
  "object_sha256_after": "29e179c53560f47e472a54847d7caf8db39eea050d8b00c83c8098a681d66bcb",
  "object_sha256_before": "55efaa8f434e771de7799e46a1c083e82c61e53eab00a339cd73bd8bfa316cb2",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalified",
  "source_ids": [
    "source_d01f40e4896de2e186cbbe8a",
    "source_ca1f80f2bf2e7d410ab2459e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0",
      "source_id": "source_d01f40e4896de2e186cbbe8a",
      "source_record_sha256": "e1a4eb79acc57c1f3de240eb5c9d019a00f7d78012bb28cd13a42777d87d10f4",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185",
      "source_id": "source_ca1f80f2bf2e7d410ab2459e",
      "source_record_sha256": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0",
    "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"
  ],
  "started_at": "2026-07-17T18:38:30+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:38:31+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
