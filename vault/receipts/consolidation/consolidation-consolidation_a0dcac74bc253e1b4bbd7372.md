---
id: "consolidation_a0dcac74bc253e1b4bbd7372"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 物理失败合成驱动的稠密机器人奖励建模"
created_at: "2026-07-20T13:37:42+08:00"
updated_at: "2026-07-20T13:37:42+08:00"
consolidation_id: "consolidation_a0dcac74bc253e1b4bbd7372"
object_id: "concept_f67f822ee20789d74d7b75e3"
object_version_before: 1
object_sha256_before: "a7080e0866d629ce1b0b4eeb8a90101d99d45c7a1cc16015769860dcb38bd11d"
object_sha256_after: "c4b638bdf05b70309275e7abd597fa581b6318e950e22e95a6d9225ae7748fc2"
source_ids: ["source_f9128ff3463cfaa7fa41ee7e"]
source_sha256s: ["115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256"]
source_records: [{"source_id": "source_f9128ff3463cfaa7fa41ee7e", "source_record_sha256": "7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627", "raw_content_sha256": "115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:42+08:00"
completed_at: "2026-07-20T13:37:42+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_f9128ff3463cfaa7fa41ee7e raw_sha256:115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_f9128ff3463cfaa7fa41ee7e record_sha256:7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_f67f822ee20789d74d7b75e3"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_f9128ff3463cfaa7fa41ee7e", "related:concept_vla_action_evaluation_distillation", "related:concept_f67f822ee20789d74d7b75e3"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:27:37+08:00", "source:source_f9128ff3463cfaa7fa41ee7e work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c4b638bdf05b70309275e7abd597fa581b6318e950e22e95a6d9225ae7748fc2", "source_state_sha256": "48a08837c42ec4c447aaecaabd353313b93fa1b7765f751b7b49bb3596055c85", "source_record_sha256s": {"source_f9128ff3463cfaa7fa41ee7e": "7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627"}, "raw_state_sha256": "13fd592ca9c852beb11794597fa1ddae755ef72fc071efe18f4ea3c40c904d5d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "064831a9832dc2ad6c3191c647ce285865b38ae6d51fff261112dbe5f1c3fbe2", "relation_fingerprint": {"outgoing_relations_sha256": "ed6fc3596640b72582a2a7dd222f6656019f126182f34ebb1973c53df4a1391b", "incoming_relations_sha256": "24ebd6f0c6ba9ec842ffe53d99fbd0f8c5c1e01e47cc79be79772b5dcff52c1b", "full_neighborhood_sha256": "f55bee2c9e8018fc207a10b5ccad0d83b3fae9ddb0785e3c4df0d86db26c0711"}, "relation_neighborhood_sha256": "f55bee2c9e8018fc207a10b5ccad0d83b3fae9ddb0785e3c4df0d86db26c0711", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_f67f822ee20789d74d7b75e3"
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
        "object_updated_at:2026-07-20T12:27:37+08:00",
        "source:source_f9128ff3463cfaa7fa41ee7e work_sha256:none"
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
        "source:source_f9128ff3463cfaa7fa41ee7e record_sha256:7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627"
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
        "source:source_f9128ff3463cfaa7fa41ee7e raw_sha256:115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256"
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
        "related:source_f9128ff3463cfaa7fa41ee7e",
        "related:concept_vla_action_evaluation_distillation",
        "related:concept_f67f822ee20789d74d7b75e3"
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
        "validated:vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md"
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
  "completed_at": "2026-07-20T13:37:42+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c4b638bdf05b70309275e7abd597fa581b6318e950e22e95a6d9225ae7748fc2",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "13fd592ca9c852beb11794597fa1ddae755ef72fc071efe18f4ea3c40c904d5d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f55bee2c9e8018fc207a10b5ccad0d83b3fae9ddb0785e3c4df0d86db26c0711",
      "incoming_relations_sha256": "24ebd6f0c6ba9ec842ffe53d99fbd0f8c5c1e01e47cc79be79772b5dcff52c1b",
      "outgoing_relations_sha256": "ed6fc3596640b72582a2a7dd222f6656019f126182f34ebb1973c53df4a1391b"
    },
    "relation_neighborhood_sha256": "f55bee2c9e8018fc207a10b5ccad0d83b3fae9ddb0785e3c4df0d86db26c0711",
    "source_record_sha256s": {
      "source_f9128ff3463cfaa7fa41ee7e": "7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627"
    },
    "source_state_sha256": "48a08837c42ec4c447aaecaabd353313b93fa1b7765f751b7b49bb3596055c85",
    "work_identity_sha256": "064831a9832dc2ad6c3191c647ce285865b38ae6d51fff261112dbe5f1c3fbe2"
  },
  "consolidation_id": "consolidation_a0dcac74bc253e1b4bbd7372",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:42+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a0dcac74bc253e1b4bbd7372",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_f67f822ee20789d74d7b75e3",
  "object_sha256_after": "c4b638bdf05b70309275e7abd597fa581b6318e950e22e95a6d9225ae7748fc2",
  "object_sha256_before": "a7080e0866d629ce1b0b4eeb8a90101d99d45c7a1cc16015769860dcb38bd11d",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_f9128ff3463cfaa7fa41ee7e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256",
      "source_id": "source_f9128ff3463cfaa7fa41ee7e",
      "source_record_sha256": "7c56b9dc6918c68ca1ea2fd8cbe363721675f4c3eeec0230bfdfeec6c9a53627",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256"
  ],
  "started_at": "2026-07-20T13:37:42+08:00",
  "status": "complete",
  "title": "Consolidation: 物理失败合成驱动的稠密机器人奖励建模",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:42+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
