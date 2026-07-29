---
id: "consolidation_539467aa3e9534cbc68d2aed"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 接触关键段的数据聚焦学习"
created_at: "2026-07-26T12:33:45+08:00"
updated_at: "2026-07-26T12:33:45+08:00"
consolidation_id: "consolidation_539467aa3e9534cbc68d2aed"
object_id: "concept_bfba032a868e0f7e1bcbe1d8"
object_version_before: 1
object_sha256_before: "b6be3a58568706e6453511bf1fb422601e86edae2d1323ea6dae5c85ff56941f"
object_sha256_after: "57c88897969cbd59e0566ed1afe04e466198a025c277d1b9a5f33e6141394823"
source_ids: ["source_42e52a18cc082f3af087d574"]
source_sha256s: ["ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45"]
source_records: [{"source_id": "source_42e52a18cc082f3af087d574", "source_record_sha256": "e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f", "raw_content_sha256": "ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:45+08:00"
completed_at: "2026-07-26T12:33:45+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_bfba032a868e0f7e1bcbe1d8.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_42e52a18cc082f3af087d574 raw_sha256:ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_42e52a18cc082f3af087d574 record_sha256:e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_bfba032a868e0f7e1bcbe1d8"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_42e52a18cc082f3af087d574", "related:concept_real_robot_deployment_iteration_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-22T18:11:51+08:00", "source:source_42e52a18cc082f3af087d574 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "57c88897969cbd59e0566ed1afe04e466198a025c277d1b9a5f33e6141394823", "source_state_sha256": "f8d030bcc4773237bb2c2a2614f01792b249d8dadc4d0fb2a10f0a19662d4b8f", "source_record_sha256s": {"source_42e52a18cc082f3af087d574": "e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f"}, "raw_state_sha256": "b7fc4aae1e6810079412dab428e9e06ff3389a2c3fc9e6e4d25959c10e034eb5", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "f3764f9eea9a007f1360c31633876cadf9dacfd0df843c8a90a7345dd014d913", "relation_fingerprint": {"outgoing_relations_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d"}, "relation_neighborhood_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_bfba032a868e0f7e1bcbe1d8"
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
        "object_updated_at:2026-07-22T18:11:51+08:00",
        "source:source_42e52a18cc082f3af087d574 work_sha256:none"
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
        "source:source_42e52a18cc082f3af087d574 record_sha256:e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f"
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
        "source:source_42e52a18cc082f3af087d574 raw_sha256:ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45"
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
        "relation index inspected; 2 related objects found",
        "related:source_42e52a18cc082f3af087d574",
        "related:concept_real_robot_deployment_iteration_loop"
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
        "validated:vault/memory/concept/concept_bfba032a868e0f7e1bcbe1d8.md"
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
  "completed_at": "2026-07-26T12:33:45+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "57c88897969cbd59e0566ed1afe04e466198a025c277d1b9a5f33e6141394823",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "b7fc4aae1e6810079412dab428e9e06ff3389a2c3fc9e6e4d25959c10e034eb5",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d"
    },
    "relation_neighborhood_sha256": "e6dc662b7749155e1a3058cb86514cb8d09d064dd59462118c39966f1d194f9d",
    "source_record_sha256s": {
      "source_42e52a18cc082f3af087d574": "e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f"
    },
    "source_state_sha256": "f8d030bcc4773237bb2c2a2614f01792b249d8dadc4d0fb2a10f0a19662d4b8f",
    "work_identity_sha256": "f3764f9eea9a007f1360c31633876cadf9dacfd0df843c8a90a7345dd014d913"
  },
  "consolidation_id": "consolidation_539467aa3e9534cbc68d2aed",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:45+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_539467aa3e9534cbc68d2aed",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_bfba032a868e0f7e1bcbe1d8",
  "object_sha256_after": "57c88897969cbd59e0566ed1afe04e466198a025c277d1b9a5f33e6141394823",
  "object_sha256_before": "b6be3a58568706e6453511bf1fb422601e86edae2d1323ea6dae5c85ff56941f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_42e52a18cc082f3af087d574"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45",
      "source_id": "source_42e52a18cc082f3af087d574",
      "source_record_sha256": "e1a782bf001fa65931bcee00282277ad2c39e3b8b589f57e0789ec4125725b1f",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45"
  ],
  "started_at": "2026-07-26T12:33:45+08:00",
  "status": "complete",
  "title": "Consolidation: 接触关键段的数据聚焦学习",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:45+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
