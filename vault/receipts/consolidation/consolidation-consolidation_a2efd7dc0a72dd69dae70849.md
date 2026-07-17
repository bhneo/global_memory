---
id: "consolidation_a2efd7dc0a72dd69dae70849"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示"
created_at: "2026-07-17T18:35:51+08:00"
updated_at: "2026-07-17T18:35:51+08:00"
consolidation_id: "consolidation_a2efd7dc0a72dd69dae70849"
object_id: "claim_wechat_standard_model_symmetry_group_20260716"
object_version_before: 1
object_sha256_before: "19407aed5217a587cec96772b9b45bfaef828459a2cca0a2ca3e8f745e0b3305"
object_sha256_after: "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc"
source_ids: ["source_9bcee8e0abc8386cbba43b87"]
source_sha256s: ["e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"]
source_records: [{"source_id": "source_9bcee8e0abc8386cbba43b87", "source_record_sha256": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223", "raw_content_sha256": "e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_3114"]
started_at: "2026-07-17T18:35:51+08:00"
completed_at: "2026-07-17T18:35:51+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_9bcee8e0abc8386cbba43b87 raw_sha256:e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_9bcee8e0abc8386cbba43b87 record_sha256:d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_3114"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_standard_model_symmetry_group_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_9bcee8e0abc8386cbba43b87"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:57+08:00", "source:source_9bcee8e0abc8386cbba43b87 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc", "source_state_sha256": "7a2fa6021db6127b615e1843967e44272365c4b877d28f26b721d86e10cff6ed", "source_record_sha256s": {"source_9bcee8e0abc8386cbba43b87": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"}, "raw_state_sha256": "4e8626f096be354c1e457a6a3262604865a81cebac36da8ca787f497fbadc386", "evidence_sha256": "c08fbb4ca6973942160e13a8aff39d130f4410b7fe88270fd45a1dd22fa0215c", "extraction_state_sha256": "953305af6e35774be1a2372fcaedbe16abf4ffe8e3439bf65e5e5d0b2add31b6", "work_identity_sha256": "f25e6766a97f0d225e614e52d8ff5d05c0f6c4ecf9cd1e552e0a537d7ad26933", "relation_neighborhood_sha256": "afdaae2cacc8008d891a904147670c5fad8f3eb78258da8b5d6624efad437f2f", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "status": "passed",
      "warnings": []
    },
    "drift_checked": {
      "findings": [
        "drift_reports:0"
      ],
      "status": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "findings": [
        "searched title; 1 candidates inspected",
        "candidate:claim_wechat_standard_model_symmetry_group_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:partial"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_3114"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:57+08:00",
        "source:source_9bcee8e0abc8386cbba43b87 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_9bcee8e0abc8386cbba43b87 record_sha256:d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_9bcee8e0abc8386cbba43b87 raw_sha256:e9b06f9a56bacf6be394e58b75466386a638f10c397f0ab5b702160f9dc45a7a"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_9bcee8e0abc8386cbba43b87"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "status": "passed",
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
  "completed_at": "2026-07-17T18:35:51+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "c08fbb4ca6973942160e13a8aff39d130f4410b7fe88270fd45a1dd22fa0215c",
    "extraction_state_sha256": "953305af6e35774be1a2372fcaedbe16abf4ffe8e3439bf65e5e5d0b2add31b6",
    "memory_schema_version": 2,
    "object_sha256": "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "4e8626f096be354c1e457a6a3262604865a81cebac36da8ca787f497fbadc386",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "afdaae2cacc8008d891a904147670c5fad8f3eb78258da8b5d6624efad437f2f",
    "source_record_sha256s": {
      "source_9bcee8e0abc8386cbba43b87": "d8f41ac5027b02b5fde37be6c8fbe757b87b8b78eb100ea6225d13b7b78c5223"
    },
    "source_state_sha256": "7a2fa6021db6127b615e1843967e44272365c4b877d28f26b721d86e10cff6ed",
    "work_identity_sha256": "f25e6766a97f0d225e614e52d8ff5d05c0f6c4ecf9cd1e552e0a537d7ad26933"
  },
  "consolidation_id": "consolidation_a2efd7dc0a72dd69dae70849",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:51+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_3114"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a2efd7dc0a72dd69dae70849",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_standard_model_symmetry_group_20260716",
  "object_sha256_after": "c506c7ad28acc25062a7cfaa20cd475d1e55c55aba8b6b1bc9bd130310f272fc",
  "object_sha256_before": "19407aed5217a587cec96772b9b45bfaef828459a2cca0a2ca3e8f745e0b3305",
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
  "started_at": "2026-07-17T18:35:51+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:51+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
