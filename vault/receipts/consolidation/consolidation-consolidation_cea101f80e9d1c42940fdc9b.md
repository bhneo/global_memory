---
id: "consolidation_cea101f80e9d1c42940fdc9b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示"
created_at: "2026-07-18T16:03:09+08:00"
updated_at: "2026-07-18T16:03:09+08:00"
consolidation_id: "consolidation_cea101f80e9d1c42940fdc9b"
object_id: "claim_wechat_standard_model_symmetry_group_20260716"
object_version_before: 1
object_sha256_before: "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc"
object_sha256_after: "b0bc55a82db1d17a65a43483073f26d6eef1ce6dbd00d4f986ee56ee41a10d50"
source_ids: ["source_9bcee8e0abc8386cbba43b87"]
source_sha256s: ["e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"]
source_records: [{"source_id": "source_9bcee8e0abc8386cbba43b87", "source_record_sha256": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223", "raw_content_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_3114"]
started_at: "2026-07-18T16:03:09+08:00"
completed_at: "2026-07-18T16:03:09+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9bcee8e0abc8386cbba43b87 raw_sha256:e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9bcee8e0abc8386cbba43b87 record_sha256:d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_3114"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "partial", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_standard_model_symmetry_group_20260716"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_9bcee8e0abc8386cbba43b87"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:51+08:00", "source:source_9bcee8e0abc8386cbba43b87 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "b0bc55a82db1d17a65a43483073f26d6eef1ce6dbd00d4f986ee56ee41a10d50", "source_state_sha256": "7a2fa6021db6127b615e1843967e44272365c4b877d28f26b721d86e10cff6ed", "source_record_sha256s": {"source_9bcee8e0abc8386cbba43b87": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"}, "raw_state_sha256": "4e8626f096be354c1e457a6a3262604865a81cebac36da8ca787f497fbadc386", "evidence_sha256": "c08fbb4ca6973942160e13a8aff39d130f4410b7fe88270fd45a1dd22fa0215c", "extraction_state_sha256": "953305af6e35774be1a2372fcaedbe16abf4ffe8e3439bf65e5e5d0b2add31b6", "work_identity_sha256": "f25e6766a97f0d225e614e52d8ff5d05c0f6c4ecf9cd1e552e0a537d7ad26933", "relation_fingerprint": {"outgoing_relations_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f"}, "relation_neighborhood_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_standard_model_symmetry_group_20260716"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "partial",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:partial"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:ev_3114"
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
        "object_updated_at:2026-07-17T18:35:51+08:00",
        "source:source_9bcee8e0abc8386cbba43b87 work_sha256:none"
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
        "source:source_9bcee8e0abc8386cbba43b87 record_sha256:d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"
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
        "source:source_9bcee8e0abc8386cbba43b87 raw_sha256:e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"
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
        "related:source_9bcee8e0abc8386cbba43b87"
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
        "validated:vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md"
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
  "completed_at": "2026-07-18T16:03:09+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "c08fbb4ca6973942160e13a8aff39d130f4410b7fe88270fd45a1dd22fa0215c",
    "extraction_state_sha256": "953305af6e35774be1a2372fcaedbe16abf4ffe8e3439bf65e5e5d0b2add31b6",
    "memory_schema_version": 2,
    "object_sha256": "b0bc55a82db1d17a65a43483073f26d6eef1ce6dbd00d4f986ee56ee41a10d50",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "4e8626f096be354c1e457a6a3262604865a81cebac36da8ca787f497fbadc386",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f"
    },
    "relation_neighborhood_sha256": "054c70f1a71e44a21c94eb048d79c7369940e6d89eff3e47d1f11b13bca4ad3f",
    "source_record_sha256s": {
      "source_9bcee8e0abc8386cbba43b87": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"
    },
    "source_state_sha256": "7a2fa6021db6127b615e1843967e44272365c4b877d28f26b721d86e10cff6ed",
    "work_identity_sha256": "f25e6766a97f0d225e614e52d8ff5d05c0f6c4ecf9cd1e552e0a537d7ad26933"
  },
  "consolidation_id": "consolidation_cea101f80e9d1c42940fdc9b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:09+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_3114"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_cea101f80e9d1c42940fdc9b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_standard_model_symmetry_group_20260716",
  "object_sha256_after": "b0bc55a82db1d17a65a43483073f26d6eef1ce6dbd00d4f986ee56ee41a10d50",
  "object_sha256_before": "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9bcee8e0abc8386cbba43b87"
  ],
  "source_records": [
    {
      "raw_content_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a",
      "source_id": "source_9bcee8e0abc8386cbba43b87",
      "source_record_sha256": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"
  ],
  "started_at": "2026-07-18T16:03:09+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:09+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
