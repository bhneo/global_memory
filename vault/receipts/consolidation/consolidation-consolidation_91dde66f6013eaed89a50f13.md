---
id: "consolidation_91dde66f6013eaed89a50f13"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 类型化可验证机器人技能图"
created_at: "2026-07-19T12:20:25+08:00"
updated_at: "2026-07-19T12:20:25+08:00"
consolidation_id: "consolidation_91dde66f6013eaed89a50f13"
object_id: "concept_typed_verified_robot_skill_graph"
object_version_before: 1
object_sha256_before: "e46af5b6943493b9039a9c97d35c4595919f7958590cfb78466c17c36e556e4c"
object_sha256_after: "57dba297ac03a694ee18d980f2d4491db9c6367345947e6d5c133bcb8de04ed2"
source_ids: ["source_6fb6f0a30a013fd1ada42b57"]
source_sha256s: ["d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c"]
source_records: [{"source_id": "source_6fb6f0a30a013fd1ada42b57", "source_record_sha256": "4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b", "raw_content_sha256": "d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T12:20:25+08:00"
completed_at: "2026-07-19T12:20:25+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_typed_verified_robot_skill_graph.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_6fb6f0a30a013fd1ada42b57 raw_sha256:d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_6fb6f0a30a013fd1ada42b57 record_sha256:4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_typed_verified_robot_skill_graph"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 6 related objects found", "related:question_skill_compilation_boundary", "related:source_6fb6f0a30a013fd1ada42b57", "related:concept_skill_evolution", "related:concept_adaptive_interleaved_multimodal_planning", "related:tension_internal_reasoning_external_skills"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T12:18:23+08:00", "source:source_6fb6f0a30a013fd1ada42b57 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "57dba297ac03a694ee18d980f2d4491db9c6367345947e6d5c133bcb8de04ed2", "source_state_sha256": "608b58d7ca45e36321e49f4848f840dea5774cc2beb5cde67f66c0724336979f", "source_record_sha256s": {"source_6fb6f0a30a013fd1ada42b57": "4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b"}, "raw_state_sha256": "a7b4bb9dc614061b1d4c51d8f27bc985962dc1b7b9b2cdcdc42a25f7326f05a9", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "6f0214aaafc7a2eb01e91aaf0b76a56a78d149a4516d3d29c6b7ed849c7a975e", "relation_fingerprint": {"outgoing_relations_sha256": "5bdcf1fd4d4af03f4f917f718641619b942a4c9fad68a6d7d033e6ceb089bf00", "incoming_relations_sha256": "0de7b893ad7cfabcadfb28a1fe322aa79cfc8c7278f5749afaa47b1acb54bab7", "full_neighborhood_sha256": "00aa24bebfa120240649aff4bf769389adfab9c975dee664c066d6072216e12c"}, "relation_neighborhood_sha256": "00aa24bebfa120240649aff4bf769389adfab9c975dee664c066d6072216e12c", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_typed_verified_robot_skill_graph"
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
        "object_updated_at:2026-07-19T12:18:23+08:00",
        "source:source_6fb6f0a30a013fd1ada42b57 work_sha256:none"
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
        "source:source_6fb6f0a30a013fd1ada42b57 record_sha256:4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b"
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
        "source:source_6fb6f0a30a013fd1ada42b57 raw_sha256:d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c"
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
        "relation index inspected; 6 related objects found",
        "related:question_skill_compilation_boundary",
        "related:source_6fb6f0a30a013fd1ada42b57",
        "related:concept_skill_evolution",
        "related:concept_adaptive_interleaved_multimodal_planning",
        "related:tension_internal_reasoning_external_skills"
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
        "validated:vault/memory/concept/concept_typed_verified_robot_skill_graph.md"
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
  "completed_at": "2026-07-19T12:20:25+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "57dba297ac03a694ee18d980f2d4491db9c6367345947e6d5c133bcb8de04ed2",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a7b4bb9dc614061b1d4c51d8f27bc985962dc1b7b9b2cdcdc42a25f7326f05a9",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "00aa24bebfa120240649aff4bf769389adfab9c975dee664c066d6072216e12c",
      "incoming_relations_sha256": "0de7b893ad7cfabcadfb28a1fe322aa79cfc8c7278f5749afaa47b1acb54bab7",
      "outgoing_relations_sha256": "5bdcf1fd4d4af03f4f917f718641619b942a4c9fad68a6d7d033e6ceb089bf00"
    },
    "relation_neighborhood_sha256": "00aa24bebfa120240649aff4bf769389adfab9c975dee664c066d6072216e12c",
    "source_record_sha256s": {
      "source_6fb6f0a30a013fd1ada42b57": "4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b"
    },
    "source_state_sha256": "608b58d7ca45e36321e49f4848f840dea5774cc2beb5cde67f66c0724336979f",
    "work_identity_sha256": "6f0214aaafc7a2eb01e91aaf0b76a56a78d149a4516d3d29c6b7ed849c7a975e"
  },
  "consolidation_id": "consolidation_91dde66f6013eaed89a50f13",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T12:20:25+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_91dde66f6013eaed89a50f13",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_typed_verified_robot_skill_graph",
  "object_sha256_after": "57dba297ac03a694ee18d980f2d4491db9c6367345947e6d5c133bcb8de04ed2",
  "object_sha256_before": "e46af5b6943493b9039a9c97d35c4595919f7958590cfb78466c17c36e556e4c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_6fb6f0a30a013fd1ada42b57"
  ],
  "source_records": [
    {
      "raw_content_sha256": "d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c",
      "source_id": "source_6fb6f0a30a013fd1ada42b57",
      "source_record_sha256": "4ad3aac5c9095230c9f7baadb5f27f7cbc3edaf0ee78f5a830306acc251d891b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c"
  ],
  "started_at": "2026-07-19T12:20:25+08:00",
  "status": "complete",
  "title": "Consolidation: 类型化可验证机器人技能图",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T12:20:25+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
