---
id: "consolidation_24ef7f1fa344dab4823dc2d9"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering"
created_at: "2026-08-02T12:30:56+08:00"
updated_at: "2026-08-02T12:30:56+08:00"
consolidation_id: "consolidation_24ef7f1fa344dab4823dc2d9"
object_id: "concept_e69974f653450465afb2aa3e"
object_version_before: 1
object_sha256_before: "63f3acb683ed0fa6606e0331fb0a9963a6a2a12d740638c8a95bb6c030a3d9b9"
object_sha256_after: "fbdc960884d08884af508dce285c405c97a7c0df44f635129c2992b8467e2472"
source_ids: ["source_e504623270d30d733b2cb9e1"]
source_sha256s: ["3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c"]
source_records: [{"source_id": "source_e504623270d30d733b2cb9e1", "source_record_sha256": "67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40", "raw_content_sha256": "3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T12:30:55+08:00"
completed_at: "2026-08-02T12:30:56+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_e69974f653450465afb2aa3e.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e504623270d30d733b2cb9e1 raw_sha256:3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e504623270d30d733b2cb9e1 record_sha256:67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_e69974f653450465afb2aa3e"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_e504623270d30d733b2cb9e1", "related:concept_2db7edf95d63ca80702f042e", "related:concept_6a559a41722de87986c350e7", "related:concept_vla_action_evaluation_distillation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T12:14:40+08:00", "source:source_e504623270d30d733b2cb9e1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "fbdc960884d08884af508dce285c405c97a7c0df44f635129c2992b8467e2472", "source_state_sha256": "398a4f56236dbf473c8cfbd48095671f143c4c4faef36f76bdfef975718c87e4", "source_record_sha256s": {"source_e504623270d30d733b2cb9e1": "67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40"}, "raw_state_sha256": "2d4ea1058b1bba4a6208e865ba5d7faf21b9200fc5e17840efa788298d21ed0b", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "60936917c5998e8941368ed778e99d7f253f53c53f93621b183081d53d4bdd4a", "relation_fingerprint": {"outgoing_relations_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12"}, "relation_neighborhood_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_e69974f653450465afb2aa3e"
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
        "object_updated_at:2026-08-02T12:14:40+08:00",
        "source:source_e504623270d30d733b2cb9e1 work_sha256:none"
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
        "source:source_e504623270d30d733b2cb9e1 record_sha256:67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40"
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
        "source:source_e504623270d30d733b2cb9e1 raw_sha256:3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c"
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
        "relation index inspected; 4 related objects found",
        "related:source_e504623270d30d733b2cb9e1",
        "related:concept_2db7edf95d63ca80702f042e",
        "related:concept_6a559a41722de87986c350e7",
        "related:concept_vla_action_evaluation_distillation"
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
        "validated:vault/memory/concept/concept_e69974f653450465afb2aa3e.md"
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
  "completed_at": "2026-08-02T12:30:56+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "fbdc960884d08884af508dce285c405c97a7c0df44f635129c2992b8467e2472",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "2d4ea1058b1bba4a6208e865ba5d7faf21b9200fc5e17840efa788298d21ed0b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12"
    },
    "relation_neighborhood_sha256": "0d1f91d528c96d018a668fb0ac4ac5bae05faf7bd1c32821c7dd72711072fe12",
    "source_record_sha256s": {
      "source_e504623270d30d733b2cb9e1": "67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40"
    },
    "source_state_sha256": "398a4f56236dbf473c8cfbd48095671f143c4c4faef36f76bdfef975718c87e4",
    "work_identity_sha256": "60936917c5998e8941368ed778e99d7f253f53c53f93621b183081d53d4bdd4a"
  },
  "consolidation_id": "consolidation_24ef7f1fa344dab4823dc2d9",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T12:30:56+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_24ef7f1fa344dab4823dc2d9",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_e69974f653450465afb2aa3e",
  "object_sha256_after": "fbdc960884d08884af508dce285c405c97a7c0df44f635129c2992b8467e2472",
  "object_sha256_before": "63f3acb683ed0fa6606e0331fb0a9963a6a2a12d740638c8a95bb6c030a3d9b9",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e504623270d30d733b2cb9e1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c",
      "source_id": "source_e504623270d30d733b2cb9e1",
      "source_record_sha256": "67afe4a4a1d26d94d2b5c124429a7fee2b37de99802f8b90aa4582d63b2c3e40",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c"
  ],
  "started_at": "2026-08-02T12:30:55+08:00",
  "status": "complete",
  "title": "Consolidation: 失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T12:30:56+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
