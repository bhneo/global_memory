---
id: "consolidation_7232c1c7516f64452c851379"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 更好的世界模型评价 vs 直接优化动作结果"
created_at: "2026-07-17T22:40:14+08:00"
updated_at: "2026-07-17T22:40:14+08:00"
consolidation_id: "consolidation_7232c1c7516f64452c851379"
object_id: "tension_world_model_eval_action"
object_version_before: 1
object_sha256_before: "8d786db3c55d3fcf4121622c2fbeb83cbfc7773e47a7b6cf51bc6f64b8878dc6"
object_sha256_after: "e710f528a0bd0a021e8063ff5a966b6973e68f587374c9ae2cf2a61319f400bb"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
source_sha256s: ["2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"]
source_records: [{"source_id": "source_2d4f3a7d3525782c8ff503ee", "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd", "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T22:40:14+08:00"
completed_at: "2026-07-17T22:40:14+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/tension/tension_world_model_eval_action.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:tension_world_model_eval_action"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_2d4f3a7d3525782c8ff503ee", "related:concept_world_model_evaluation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:41:02+08:00", "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "e710f528a0bd0a021e8063ff5a966b6973e68f587374c9ae2cf2a61319f400bb", "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020", "source_record_sha256s": {"source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"}, "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723", "relation_fingerprint": {"outgoing_relations_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d"}, "relation_neighborhood_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalification_candidate"
changes: []
change_summary: "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary",
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
        "candidate:tension_world_model_eval_action"
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
        "object_updated_at:2026-07-17T18:41:02+08:00",
        "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"
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
        "source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
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
        "source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
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
        "related:source_2d4f3a7d3525782c8ff503ee",
        "related:concept_world_model_evaluation"
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
        "validated:vault/memory/tension/tension_world_model_eval_action.md"
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
  "completed_at": "2026-07-17T22:40:14+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "e710f528a0bd0a021e8063ff5a966b6973e68f587374c9ae2cf2a61319f400bb",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d"
    },
    "relation_neighborhood_sha256": "8e644a5af8b7c330cb0fe9d58e66414956f65e293ed4aff223fcd6ecadd4fb7d",
    "source_record_sha256s": {
      "source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
    },
    "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020",
    "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723"
  },
  "consolidation_id": "consolidation_7232c1c7516f64452c851379",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:40:14+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_7232c1c7516f64452c851379",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "tension_world_model_eval_action",
  "object_sha256_after": "e710f528a0bd0a021e8063ff5a966b6973e68f587374c9ae2cf2a61319f400bb",
  "object_sha256_before": "8d786db3c55d3fcf4121622c2fbeb83cbfc7773e47a7b6cf51bc6f64b8878dc6",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
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
  "started_at": "2026-07-17T22:40:14+08:00",
  "status": "complete",
  "title": "Consolidation: 更好的世界模型评价 vs 直接优化动作结果",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:40:14+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
