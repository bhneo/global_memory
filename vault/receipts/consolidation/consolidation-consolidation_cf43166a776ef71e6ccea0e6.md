---
id: "consolidation_cf43166a776ef71e6ccea0e6"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 用视觉错觉刺激测试世界模型预测偏差"
created_at: "2026-07-18T16:03:20+08:00"
updated_at: "2026-07-18T16:03:20+08:00"
consolidation_id: "consolidation_cf43166a776ef71e6ccea0e6"
object_id: "experiment_visual_illusion_world_model"
object_version_before: 1
object_sha256_before: "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4"
object_sha256_after: "e49a22e55d5efd38f5bc57d10a8bfc91b1177dd068597ab4de564aca5907345e"
source_ids: ["source_38756ea977001ddb8594f144"]
source_sha256s: ["fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"]
source_records: [{"source_id": "source_38756ea977001ddb8594f144", "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:20+08:00"
completed_at: "2026-07-18T16:03:20+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/experiment/experiment_visual_illusion_world_model.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:experiment_visual_illusion_world_model"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:project_embodied_agent_learning_candidate", "related:source_38756ea977001ddb8594f144", "related:hypothesis_illusion_world_model_probe"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:36:02+08:00", "source:source_38756ea977001ddb8594f144 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "e49a22e55d5efd38f5bc57d10a8bfc91b1177dd068597ab4de564aca5907345e", "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50", "source_record_sha256s": {"source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"}, "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e", "relation_fingerprint": {"outgoing_relations_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1"}, "relation_neighborhood_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:experiment_visual_illusion_world_model"
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
        "object_updated_at:2026-07-17T18:36:02+08:00",
        "source:source_38756ea977001ddb8594f144 work_sha256:none"
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
        "source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
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
        "source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"
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
        "relation index inspected; 3 related objects found",
        "related:project_embodied_agent_learning_candidate",
        "related:source_38756ea977001ddb8594f144",
        "related:hypothesis_illusion_world_model_probe"
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
        "validated:vault/memory/experiment/experiment_visual_illusion_world_model.md"
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
  "completed_at": "2026-07-18T16:03:20+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "e49a22e55d5efd38f5bc57d10a8bfc91b1177dd068597ab4de564aca5907345e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1"
    },
    "relation_neighborhood_sha256": "f535c56d5c283200b2cdbfbcf9e2ecf676155f306118deeab1b3d7fed03df4f1",
    "source_record_sha256s": {
      "source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
    },
    "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50",
    "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e"
  },
  "consolidation_id": "consolidation_cf43166a776ef71e6ccea0e6",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:20+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_cf43166a776ef71e6ccea0e6",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_visual_illusion_world_model",
  "object_sha256_after": "e49a22e55d5efd38f5bc57d10a8bfc91b1177dd068597ab4de564aca5907345e",
  "object_sha256_before": "8564c7d09bffb8b8b7fa61f3947d3e114242e59742df9b1e88affe651a34b5f4",
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
  "started_at": "2026-07-18T16:03:20+08:00",
  "status": "complete",
  "title": "Consolidation: 用视觉错觉刺激测试世界模型预测偏差",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:20+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
