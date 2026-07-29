---
id: "consolidation_caa20e599bd45a05fbbc62b8"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 人机客户端与 Agent 执行的双协议边界"
created_at: "2026-07-26T12:33:46+08:00"
updated_at: "2026-07-26T12:33:46+08:00"
consolidation_id: "consolidation_caa20e599bd45a05fbbc62b8"
object_id: "concept_dual_protocol_hri_agent_execution_boundary"
object_version_before: 1
object_sha256_before: "4585d29c956de3fb7ff83073ff497c20ee328c3dc1e3f29bbe3426cd2e20b6fa"
object_sha256_after: "68ff5c93c7e972985e2aff823468a9adbb7ec47b7f5d181703f19362620b0b58"
source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
source_sha256s: ["dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"]
source_records: [{"source_id": "source_a0c7811ba12c9cf80bfd26c9", "source_record_sha256": "222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3", "raw_content_sha256": "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:46+08:00"
completed_at: "2026-07-26T12:33:46+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_dual_protocol_hri_agent_execution_boundary.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a0c7811ba12c9cf80bfd26c9 raw_sha256:dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a0c7811ba12c9cf80bfd26c9 record_sha256:222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_dual_protocol_hri_agent_execution_boundary"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_a0c7811ba12c9cf80bfd26c9", "related:concept_typed_verified_robot_skill_graph", "related:concept_dual_protocol_hri_agent_execution_boundary"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-21T17:44:44+08:00", "source:source_a0c7811ba12c9cf80bfd26c9 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "68ff5c93c7e972985e2aff823468a9adbb7ec47b7f5d181703f19362620b0b58", "source_state_sha256": "8d00ef0868133f85e1eb076b7b5e0b4815deb34b39161f6b3b1dc6b4803b7fc1", "source_record_sha256s": {"source_a0c7811ba12c9cf80bfd26c9": "222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3"}, "raw_state_sha256": "34580c8a5d0bc718c76a7919c145e8659391183155c99f425e574dbfbb534cdb", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4e2e451d1fb3003669e3d2399c59cde1de8dbc98215e47b059dcc0ad81846060", "relation_fingerprint": {"outgoing_relations_sha256": "66c214356228be763fabab16f139db1cf46e998cab15b939e40d77e651f0cc3b", "incoming_relations_sha256": "bb24688038b5016992e623ac07259f4c53acfa007b4f64914d6c9ca9715badec", "full_neighborhood_sha256": "6150dbf5cc02d7c96d2c4b38f7c5deaa1b284e9228f01718fccc7419d9d4cd06"}, "relation_neighborhood_sha256": "6150dbf5cc02d7c96d2c4b38f7c5deaa1b284e9228f01718fccc7419d9d4cd06", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_dual_protocol_hri_agent_execution_boundary"
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
        "object_updated_at:2026-07-21T17:44:44+08:00",
        "source:source_a0c7811ba12c9cf80bfd26c9 work_sha256:none"
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
        "source:source_a0c7811ba12c9cf80bfd26c9 record_sha256:222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3"
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
        "source:source_a0c7811ba12c9cf80bfd26c9 raw_sha256:dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"
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
        "related:source_a0c7811ba12c9cf80bfd26c9",
        "related:concept_typed_verified_robot_skill_graph",
        "related:concept_dual_protocol_hri_agent_execution_boundary"
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
        "validated:vault/memory/concept/concept_dual_protocol_hri_agent_execution_boundary.md"
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
  "completed_at": "2026-07-26T12:33:46+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "68ff5c93c7e972985e2aff823468a9adbb7ec47b7f5d181703f19362620b0b58",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "34580c8a5d0bc718c76a7919c145e8659391183155c99f425e574dbfbb534cdb",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "6150dbf5cc02d7c96d2c4b38f7c5deaa1b284e9228f01718fccc7419d9d4cd06",
      "incoming_relations_sha256": "bb24688038b5016992e623ac07259f4c53acfa007b4f64914d6c9ca9715badec",
      "outgoing_relations_sha256": "66c214356228be763fabab16f139db1cf46e998cab15b939e40d77e651f0cc3b"
    },
    "relation_neighborhood_sha256": "6150dbf5cc02d7c96d2c4b38f7c5deaa1b284e9228f01718fccc7419d9d4cd06",
    "source_record_sha256s": {
      "source_a0c7811ba12c9cf80bfd26c9": "222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3"
    },
    "source_state_sha256": "8d00ef0868133f85e1eb076b7b5e0b4815deb34b39161f6b3b1dc6b4803b7fc1",
    "work_identity_sha256": "4e2e451d1fb3003669e3d2399c59cde1de8dbc98215e47b059dcc0ad81846060"
  },
  "consolidation_id": "consolidation_caa20e599bd45a05fbbc62b8",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:46+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_caa20e599bd45a05fbbc62b8",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_dual_protocol_hri_agent_execution_boundary",
  "object_sha256_after": "68ff5c93c7e972985e2aff823468a9adbb7ec47b7f5d181703f19362620b0b58",
  "object_sha256_before": "4585d29c956de3fb7ff83073ff497c20ee328c3dc1e3f29bbe3426cd2e20b6fa",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_a0c7811ba12c9cf80bfd26c9"
  ],
  "source_records": [
    {
      "raw_content_sha256": "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d",
      "source_id": "source_a0c7811ba12c9cf80bfd26c9",
      "source_record_sha256": "222778189fc1f158a0df1756f3daf27dd509b41e3486fe628ad313dbc8221ee3",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"
  ],
  "started_at": "2026-07-26T12:33:46+08:00",
  "status": "complete",
  "title": "Consolidation: 人机客户端与 Agent 执行的双协议边界",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:46+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
