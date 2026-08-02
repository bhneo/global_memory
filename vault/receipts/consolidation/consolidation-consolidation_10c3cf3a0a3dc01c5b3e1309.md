---
id: "consolidation_10c3cf3a0a3dc01c5b3e1309"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training"
created_at: "2026-08-02T19:55:04+08:00"
updated_at: "2026-08-02T19:55:04+08:00"
consolidation_id: "consolidation_10c3cf3a0a3dc01c5b3e1309"
object_id: "concept_8a7645759329c1444d94a4cf"
object_version_before: 1
object_sha256_before: "e72f72b8ebbd66336983415167e7f1fdebd503d7751c0e29e31f914282cbf5de"
object_sha256_after: "098da7b2ac093def536cb1273efa3b10cfd96db37dc6e1476a98fc2d5e79a1ff"
source_ids: ["source_bdb17eb4583ec8af52f28dfb"]
source_sha256s: ["3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24"]
source_records: [{"source_id": "source_bdb17eb4583ec8af52f28dfb", "source_record_sha256": "9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f", "raw_content_sha256": "3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:55:04+08:00"
completed_at: "2026-08-02T19:55:04+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_8a7645759329c1444d94a4cf.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_bdb17eb4583ec8af52f28dfb raw_sha256:3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_bdb17eb4583ec8af52f28dfb record_sha256:9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_8a7645759329c1444d94a4cf"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_bdb17eb4583ec8af52f28dfb", "related:concept_6a559a41722de87986c350e7", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T18:22:05+08:00", "source:source_bdb17eb4583ec8af52f28dfb work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "098da7b2ac093def536cb1273efa3b10cfd96db37dc6e1476a98fc2d5e79a1ff", "source_state_sha256": "3bda6f77ed7b0523d5bdb8cc5b5197870d3dc372de2a5366e0b5b54731368a76", "source_record_sha256s": {"source_bdb17eb4583ec8af52f28dfb": "9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f"}, "raw_state_sha256": "4b1e3786877b14a52a2671b749198993ccdc48854817416d58dedb6c8b731a5d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "c18ce9aa46f50da3b68e2288ab9e43d9be8fb08b96a8b0acdcb33a0da4eec8c9", "relation_fingerprint": {"outgoing_relations_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f"}, "relation_neighborhood_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_8a7645759329c1444d94a4cf"
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
        "object_updated_at:2026-08-02T18:22:05+08:00",
        "source:source_bdb17eb4583ec8af52f28dfb work_sha256:none"
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
        "source:source_bdb17eb4583ec8af52f28dfb record_sha256:9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f"
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
        "source:source_bdb17eb4583ec8af52f28dfb raw_sha256:3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24"
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
        "related:source_bdb17eb4583ec8af52f28dfb",
        "related:concept_6a559a41722de87986c350e7",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_8a7645759329c1444d94a4cf.md"
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
  "completed_at": "2026-08-02T19:55:04+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "098da7b2ac093def536cb1273efa3b10cfd96db37dc6e1476a98fc2d5e79a1ff",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "4b1e3786877b14a52a2671b749198993ccdc48854817416d58dedb6c8b731a5d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f"
    },
    "relation_neighborhood_sha256": "14e427b7ae4833d49bc747f542c1dbf579f7cc654d543038a3e8b5898e3a381f",
    "source_record_sha256s": {
      "source_bdb17eb4583ec8af52f28dfb": "9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f"
    },
    "source_state_sha256": "3bda6f77ed7b0523d5bdb8cc5b5197870d3dc372de2a5366e0b5b54731368a76",
    "work_identity_sha256": "c18ce9aa46f50da3b68e2288ab9e43d9be8fb08b96a8b0acdcb33a0da4eec8c9"
  },
  "consolidation_id": "consolidation_10c3cf3a0a3dc01c5b3e1309",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:55:04+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_10c3cf3a0a3dc01c5b3e1309",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_8a7645759329c1444d94a4cf",
  "object_sha256_after": "098da7b2ac093def536cb1273efa3b10cfd96db37dc6e1476a98fc2d5e79a1ff",
  "object_sha256_before": "e72f72b8ebbd66336983415167e7f1fdebd503d7751c0e29e31f914282cbf5de",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_bdb17eb4583ec8af52f28dfb"
  ],
  "source_records": [
    {
      "raw_content_sha256": "3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24",
      "source_id": "source_bdb17eb4583ec8af52f28dfb",
      "source_record_sha256": "9cbb23a25cd861dbd8786a08d726cd334239826c27652b2ed5c19adea84dee9f",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24"
  ],
  "started_at": "2026-08-02T19:55:04+08:00",
  "status": "complete",
  "title": "Consolidation: 同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:55:04+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
