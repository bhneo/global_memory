---
id: "consolidation_bb096eb2284fbebeff476862"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 控制策略的自适应潜空间推理"
created_at: "2026-07-19T23:49:33+08:00"
updated_at: "2026-07-19T23:49:33+08:00"
consolidation_id: "consolidation_bb096eb2284fbebeff476862"
object_id: "concept_0c7884679bf6d4e1287ce225"
object_version_before: 1
object_sha256_before: "54ee0a364009174df6afa014f5f30c89df69e35cf7524406cebe1a8d9d8a0172"
object_sha256_after: "46319542247a0aa8871d7d62b422c9127c4611f74b146c0cf0e23e6cbb46639d"
source_ids: ["source_be9781ec8ca637c5dfd8fabb"]
source_sha256s: ["0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d"]
source_records: [{"source_id": "source_be9781ec8ca637c5dfd8fabb", "source_record_sha256": "6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a", "raw_content_sha256": "0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T23:49:33+08:00"
completed_at: "2026-07-19T23:49:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_be9781ec8ca637c5dfd8fabb raw_sha256:0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_be9781ec8ca637c5dfd8fabb record_sha256:6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_0c7884679bf6d4e1287ce225"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_be9781ec8ca637c5dfd8fabb", "related:concept_dynamic_execution_horizon"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T17:16:26+08:00", "source:source_be9781ec8ca637c5dfd8fabb work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "46319542247a0aa8871d7d62b422c9127c4611f74b146c0cf0e23e6cbb46639d", "source_state_sha256": "9e7f74a9493022346f8ce5e8298cd489f9e88693ea8e9997606cb61a73ada120", "source_record_sha256s": {"source_be9781ec8ca637c5dfd8fabb": "6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a"}, "raw_state_sha256": "b080a1735a9078e0c9afe2e29d362ab4c4a423104a0c1cca39fe995c59e1de02", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2b239df263a517584e8ba03b21b7ef814b3819a13bd5324aba1d45fe68e5e878", "relation_fingerprint": {"outgoing_relations_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778"}, "relation_neighborhood_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_0c7884679bf6d4e1287ce225"
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
        "object_updated_at:2026-07-19T17:16:26+08:00",
        "source:source_be9781ec8ca637c5dfd8fabb work_sha256:none"
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
        "source:source_be9781ec8ca637c5dfd8fabb record_sha256:6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a"
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
        "source:source_be9781ec8ca637c5dfd8fabb raw_sha256:0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d"
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
        "related:source_be9781ec8ca637c5dfd8fabb",
        "related:concept_dynamic_execution_horizon"
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
        "validated:vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md"
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
  "completed_at": "2026-07-19T23:49:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "46319542247a0aa8871d7d62b422c9127c4611f74b146c0cf0e23e6cbb46639d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "b080a1735a9078e0c9afe2e29d362ab4c4a423104a0c1cca39fe995c59e1de02",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778"
    },
    "relation_neighborhood_sha256": "d407b7c887b46430355e473475061aea56d6ba5e76defe37c3ba50b86a828778",
    "source_record_sha256s": {
      "source_be9781ec8ca637c5dfd8fabb": "6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a"
    },
    "source_state_sha256": "9e7f74a9493022346f8ce5e8298cd489f9e88693ea8e9997606cb61a73ada120",
    "work_identity_sha256": "2b239df263a517584e8ba03b21b7ef814b3819a13bd5324aba1d45fe68e5e878"
  },
  "consolidation_id": "consolidation_bb096eb2284fbebeff476862",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T23:49:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_bb096eb2284fbebeff476862",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_0c7884679bf6d4e1287ce225",
  "object_sha256_after": "46319542247a0aa8871d7d62b422c9127c4611f74b146c0cf0e23e6cbb46639d",
  "object_sha256_before": "54ee0a364009174df6afa014f5f30c89df69e35cf7524406cebe1a8d9d8a0172",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_be9781ec8ca637c5dfd8fabb"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d",
      "source_id": "source_be9781ec8ca637c5dfd8fabb",
      "source_record_sha256": "6d762acedfe2c8bdc87e2485604d16dd5e1bd09c435be84002e25b7cc8a0962a",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d"
  ],
  "started_at": "2026-07-19T23:49:33+08:00",
  "status": "complete",
  "title": "Consolidation: 控制策略的自适应潜空间推理",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T23:49:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
