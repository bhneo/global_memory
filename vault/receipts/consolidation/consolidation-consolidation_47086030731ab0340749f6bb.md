---
id: "consolidation_47086030731ab0340749f6bb"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 用视觉错觉刺激测试世界模型预测偏差"
created_at: "2026-07-17T18:36:02+08:00"
updated_at: "2026-07-17T18:36:02+08:00"
consolidation_id: "consolidation_47086030731ab0340749f6bb"
object_id: "experiment_visual_illusion_world_model"
object_version_before: 1
object_sha256_before: "719c7f02722bd7eeb08b94ceff328a1b93165b49ef656775d10fd3b084e3bd77"
object_sha256_after: "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4"
source_ids: ["source_38756ea977001ddb8594f144"]
source_sha256s: ["fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"]
source_records: [{"source_id": "source_38756ea977001ddb8594f144", "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:02+08:00"
completed_at: "2026-07-17T18:36:02+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/experiment/experiment_visual_illusion_world_model.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:experiment_visual_illusion_world_model"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 3 related objects found", "related:project_embodied_agent_learning_candidate", "related:source_38756ea977001ddb8594f144", "related:hypothesis_illusion_world_model_probe"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:06+08:00", "source:source_38756ea977001ddb8594f144 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4", "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50", "source_record_sha256s": {"source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"}, "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e", "relation_neighborhood_sha256": "a4012383bfca522126633f5591916c8bbe7eca25255dbe0503fc8889a77c4107", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:experiment_visual_illusion_world_model"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:24:06+08:00",
        "source:source_38756ea977001ddb8594f144 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 3 related objects found",
        "related:project_embodied_agent_learning_candidate",
        "related:source_38756ea977001ddb8594f144",
        "related:hypothesis_illusion_world_model_probe"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/experiment/experiment_visual_illusion_world_model.md"
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
  "completed_at": "2026-07-17T18:36:02+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "a4012383bfca522126633f5591916c8bbe7eca25255dbe0503fc8889a77c4107",
    "source_record_sha256s": {
      "source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
    },
    "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50",
    "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e"
  },
  "consolidation_id": "consolidation_47086030731ab0340749f6bb",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:02+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_47086030731ab0340749f6bb",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_visual_illusion_world_model",
  "object_sha256_after": "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4",
  "object_sha256_before": "719c7f02722bd7eeb08b94ceff328a1b93165b49ef656775d10fd3b084e3bd77",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_38756ea977001ddb8594f144"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
      "source_id": "source_38756ea977001ddb8594f144",
      "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"
  ],
  "started_at": "2026-07-17T18:36:02+08:00",
  "status": "complete",
  "title": "Consolidation: 用视觉错觉刺激测试世界模型预测偏差",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:02+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
