---
id: "consolidation_28296a2e446a61bece411cdc"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 世界模型评价如何预测动作价值？"
created_at: "2026-07-17T18:36:10+08:00"
updated_at: "2026-07-17T18:36:10+08:00"
consolidation_id: "consolidation_28296a2e446a61bece411cdc"
object_id: "question_world_model_action_value"
object_version_before: 1
object_sha256_before: "1754f7af8fd6c4955f907b46efe5dda291e00b10618647ae85b12ec248c594db"
object_sha256_after: "bee863314ac841aa3a3b4985e299a4e4a5301d51d574b3a87b72ecf4e256b0e9"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
source_sha256s: ["2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"]
source_records: [{"source_id": "source_2d4f3a7d3525782c8ff503ee", "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd", "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:10+08:00"
completed_at: "2026-07-17T18:36:10+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/question/question_world_model_action_value.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:question_world_model_action_value"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_2d4f3a7d3525782c8ff503ee", "related:concept_world_model_evaluation"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:17:30+08:00", "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "bee863314ac841aa3a3b4985e299a4e4a5301d51d574b3a87b72ecf4e256b0e9", "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020", "source_record_sha256s": {"source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"}, "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723", "relation_neighborhood_sha256": "d959992704beba16634fcc8f1d0fc7832c2c06382a9f0e5e2e84f9276d85065d", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:question_world_model_action_value"
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
        "object_updated_at:2026-07-17T18:17:30+08:00",
        "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_2d4f3a7d3525782c8ff503ee",
        "related:concept_world_model_evaluation"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/question/question_world_model_action_value.md"
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
  "completed_at": "2026-07-17T18:36:10+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bee863314ac841aa3a3b4985e299a4e4a5301d51d574b3a87b72ecf4e256b0e9",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "d959992704beba16634fcc8f1d0fc7832c2c06382a9f0e5e2e84f9276d85065d",
    "source_record_sha256s": {
      "source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
    },
    "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020",
    "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723"
  },
  "consolidation_id": "consolidation_28296a2e446a61bece411cdc",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:10+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_28296a2e446a61bece411cdc",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "question_world_model_action_value",
  "object_sha256_after": "bee863314ac841aa3a3b4985e299a4e4a5301d51d574b3a87b72ecf4e256b0e9",
  "object_sha256_before": "1754f7af8fd6c4955f907b46efe5dda291e00b10618647ae85b12ec248c594db",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_2d4f3a7d3525782c8ff503ee"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e",
      "source_id": "source_2d4f3a7d3525782c8ff503ee",
      "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
  ],
  "started_at": "2026-07-17T18:36:10+08:00",
  "status": "complete",
  "title": "Consolidation: 世界模型评价如何预测动作价值？",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:10+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
