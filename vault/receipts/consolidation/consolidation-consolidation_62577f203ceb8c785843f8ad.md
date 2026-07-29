---
id: "consolidation_62577f203ceb8c785843f8ad"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 加速观察者的模式依赖粒子内容"
created_at: "2026-07-27T19:06:41+08:00"
updated_at: "2026-07-27T19:06:41+08:00"
consolidation_id: "consolidation_62577f203ceb8c785843f8ad"
object_id: "concept_81828ea915bc741846ff9e5d"
object_version_before: 1
object_sha256_before: "259148ffec3770ce31fa045f80673012c6827481bc9215fa27c8841daa70b799"
object_sha256_after: "b22dd14faeee723a48b43cd4526464886d6de826399643b50ce0e978d7a9f106"
source_ids: ["source_63ea95cc7031bab39a9b7461"]
source_sha256s: ["9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1"]
source_records: [{"source_id": "source_63ea95cc7031bab39a9b7461", "source_record_sha256": "c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa", "raw_content_sha256": "9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T19:06:41+08:00"
completed_at: "2026-07-27T19:06:41+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_81828ea915bc741846ff9e5d.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_63ea95cc7031bab39a9b7461 raw_sha256:9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_63ea95cc7031bab39a9b7461 record_sha256:c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_81828ea915bc741846ff9e5d"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_63ea95cc7031bab39a9b7461"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T09:42:51+08:00", "source:source_63ea95cc7031bab39a9b7461 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "b22dd14faeee723a48b43cd4526464886d6de826399643b50ce0e978d7a9f106", "source_state_sha256": "e0e1ecf2011aff4b94108818d6228c43a373ff57152c25dfe1305f32f0271638", "source_record_sha256s": {"source_63ea95cc7031bab39a9b7461": "c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa"}, "raw_state_sha256": "112fd25ac73d5aa12d32a789ededea1b54703f70f7773fde3d0ea668ee5914b4", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4d3b7500308b0b73f5467cfd53dd7402d37f8982384f821108190a2511a7c56c", "relation_fingerprint": {"outgoing_relations_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67"}, "relation_neighborhood_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_81828ea915bc741846ff9e5d"
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
        "object_updated_at:2026-07-27T09:42:51+08:00",
        "source:source_63ea95cc7031bab39a9b7461 work_sha256:none"
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
        "source:source_63ea95cc7031bab39a9b7461 record_sha256:c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa"
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
        "source:source_63ea95cc7031bab39a9b7461 raw_sha256:9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1"
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
        "related:source_63ea95cc7031bab39a9b7461"
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
        "validated:vault/memory/concept/concept_81828ea915bc741846ff9e5d.md"
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
  "completed_at": "2026-07-27T19:06:41+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "b22dd14faeee723a48b43cd4526464886d6de826399643b50ce0e978d7a9f106",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "112fd25ac73d5aa12d32a789ededea1b54703f70f7773fde3d0ea668ee5914b4",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67"
    },
    "relation_neighborhood_sha256": "20f7d5246365307eedb75c9758bd9cd9275d5b66aadef6a4669a086bce38fb67",
    "source_record_sha256s": {
      "source_63ea95cc7031bab39a9b7461": "c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa"
    },
    "source_state_sha256": "e0e1ecf2011aff4b94108818d6228c43a373ff57152c25dfe1305f32f0271638",
    "work_identity_sha256": "4d3b7500308b0b73f5467cfd53dd7402d37f8982384f821108190a2511a7c56c"
  },
  "consolidation_id": "consolidation_62577f203ceb8c785843f8ad",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T19:06:41+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_62577f203ceb8c785843f8ad",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_81828ea915bc741846ff9e5d",
  "object_sha256_after": "b22dd14faeee723a48b43cd4526464886d6de826399643b50ce0e978d7a9f106",
  "object_sha256_before": "259148ffec3770ce31fa045f80673012c6827481bc9215fa27c8841daa70b799",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_63ea95cc7031bab39a9b7461"
  ],
  "source_records": [
    {
      "raw_content_sha256": "9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1",
      "source_id": "source_63ea95cc7031bab39a9b7461",
      "source_record_sha256": "c28eede76c6188f5b5bb08b99139a25eb1b7ce4ff5dd0100b0a4b312a465b8fa",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1"
  ],
  "started_at": "2026-07-27T19:06:41+08:00",
  "status": "complete",
  "title": "Consolidation: 加速观察者的模式依赖粒子内容",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T19:06:41+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
