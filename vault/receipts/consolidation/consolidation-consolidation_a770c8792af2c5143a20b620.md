---
id: "consolidation_a770c8792af2c5143a20b620"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Sim-to-Real 场景基础设施"
created_at: "2026-07-18T16:03:16+08:00"
updated_at: "2026-07-18T16:03:16+08:00"
consolidation_id: "consolidation_a770c8792af2c5143a20b620"
object_id: "concept_sim_to_real_scene_infrastructure"
object_version_before: 1
object_sha256_before: "fd21b4915d2a2e3f32ff6c80fec09a7853cfe46342a60a4f5c7ecd90fa0e0a8e"
object_sha256_after: "c130486d7c00333ceca8c9f4489d8f314eeebbc86afbb507964c0c7e98ffb90f"
source_ids: ["source_a20c5fb22d91216503d413e1"]
source_sha256s: ["10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"]
source_records: [{"source_id": "source_a20c5fb22d91216503d413e1", "source_record_sha256": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819", "raw_content_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:16+08:00"
completed_at: "2026-07-18T16:03:16+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_sim_to_real_scene_infrastructure.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a20c5fb22d91216503d413e1 raw_sha256:10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a20c5fb22d91216503d413e1 record_sha256:b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_sim_to_real_scene_infrastructure"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_a20c5fb22d91216503d413e1"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:58+08:00", "source:source_a20c5fb22d91216503d413e1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c130486d7c00333ceca8c9f4489d8f314eeebbc86afbb507964c0c7e98ffb90f", "source_state_sha256": "e897544983ccb657ee0d6eb13ed573ec3dce341b0ceef0d02b44d48f6c53622c", "source_record_sha256s": {"source_a20c5fb22d91216503d413e1": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"}, "raw_state_sha256": "17d5650d83a78eda91e65d61b010a1ecec820b5b588e69f6171c8c72eabd3d8a", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "5ae407b131e09514fa6474a1a3b0640942ef50ece81eb9f9b853be43c7cc1e01", "relation_fingerprint": {"outgoing_relations_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2"}, "relation_neighborhood_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_sim_to_real_scene_infrastructure"
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
        "object_updated_at:2026-07-17T18:35:58+08:00",
        "source:source_a20c5fb22d91216503d413e1 work_sha256:none"
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
        "source:source_a20c5fb22d91216503d413e1 record_sha256:b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"
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
        "source:source_a20c5fb22d91216503d413e1 raw_sha256:10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"
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
        "relation index inspected; 1 related objects found",
        "related:source_a20c5fb22d91216503d413e1"
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
        "validated:vault/memory/concept/concept_sim_to_real_scene_infrastructure.md"
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
  "completed_at": "2026-07-18T16:03:16+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c130486d7c00333ceca8c9f4489d8f314eeebbc86afbb507964c0c7e98ffb90f",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "17d5650d83a78eda91e65d61b010a1ecec820b5b588e69f6171c8c72eabd3d8a",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2"
    },
    "relation_neighborhood_sha256": "fe5b7989cad81c2c3b9df94bf2aa4e948bd2aa901808b3e0bcb70e66aabafde2",
    "source_record_sha256s": {
      "source_a20c5fb22d91216503d413e1": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819"
    },
    "source_state_sha256": "e897544983ccb657ee0d6eb13ed573ec3dce341b0ceef0d02b44d48f6c53622c",
    "work_identity_sha256": "5ae407b131e09514fa6474a1a3b0640942ef50ece81eb9f9b853be43c7cc1e01"
  },
  "consolidation_id": "consolidation_a770c8792af2c5143a20b620",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:16+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a770c8792af2c5143a20b620",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_sim_to_real_scene_infrastructure",
  "object_sha256_after": "c130486d7c00333ceca8c9f4489d8f314eeebbc86afbb507964c0c7e98ffb90f",
  "object_sha256_before": "fd21b4915d2a2e3f32ff6c80fec09a7853cfe46342a60a4f5c7ecd90fa0e0a8e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_a20c5fb22d91216503d413e1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8",
      "source_id": "source_a20c5fb22d91216503d413e1",
      "source_record_sha256": "b770c4e48a8fe72f5567d8a72bb63295ff0e4b2978060e03cc8fd4ff2b949819",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8"
  ],
  "started_at": "2026-07-18T16:03:16+08:00",
  "status": "complete",
  "title": "Consolidation: Sim-to-Real 场景基础设施",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:16+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
