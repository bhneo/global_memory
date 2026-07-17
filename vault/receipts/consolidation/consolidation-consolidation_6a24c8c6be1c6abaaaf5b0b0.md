---
id: "consolidation_6a24c8c6be1c6abaaaf5b0b0"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 来源原文：[1811.05931] Evolving intrinsic motivations for altruistic behavior"
created_at: "2026-07-17T18:35:31+08:00"
updated_at: "2026-07-17T18:35:31+08:00"
consolidation_id: "consolidation_6a24c8c6be1c6abaaaf5b0b0"
object_id: "claim_e0c466deeea1ce8281a7b176"
object_version_before: 1
object_sha256_before: "baacdc7d66f0a4eaa37fb474392f5eebbaa6070ce71745a16096a6f494b3b78f"
object_sha256_after: "3b35404fa11cbddd42e24b84b78e3d8a67a8bf317e3c64b3dce59a7b466fdb96"
source_ids: ["source_08e53bb30d37610610477e01"]
source_sha256s: ["08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6"]
source_records: [{"source_id": "source_08e53bb30d37610610477e01", "source_record_sha256": "c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272", "raw_content_sha256": "08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_098586a5f7d8cb6b40d6"]
started_at: "2026-07-17T18:35:31+08:00"
completed_at: "2026-07-17T18:35:31+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_e0c466deeea1ce8281a7b176.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_08e53bb30d37610610477e01 raw_sha256:08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_08e53bb30d37610610477e01 record_sha256:c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_098586a5f7d8cb6b40d6"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_e0c466deeea1ce8281a7b176"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_08e53bb30d37610610477e01"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:42+08:00", "source:source_08e53bb30d37610610477e01 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "3b35404fa11cbddd42e24b84b78e3d8a67a8bf317e3c64b3dce59a7b466fdb96", "source_state_sha256": "2e3c72949c16069bcd9fc3ab82cd63591b32edfac7510454aacdb89be3e2730b", "source_record_sha256s": {"source_08e53bb30d37610610477e01": "c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272"}, "raw_state_sha256": "eee56d2937719c99f080c10ce9c2c366122958db6248fe15e5a5d83ea17bcfcf", "evidence_sha256": "9b4d97f4783b549f6e72af9ae2f6264ad93d9e8cd5edce97a725dc1fd50984b8", "extraction_state_sha256": "8dcca52a50b0625d12fb6d08683faf7297413386cbf62c9c63ca94ba01243c43", "work_identity_sha256": "a2d7a7003aee53bec813762596903cefba0d039bd5a37e746a4c0cac15b50302", "relation_neighborhood_sha256": "56a9e397460fa3769e8a20415656d13f0606412b82b2a3f034a356119c32a493", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_e0c466deeea1ce8281a7b176"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:evidence_098586a5f7d8cb6b40d6"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:42+08:00",
        "source:source_08e53bb30d37610610477e01 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_08e53bb30d37610610477e01 record_sha256:c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_08e53bb30d37610610477e01 raw_sha256:08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_08e53bb30d37610610477e01"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_e0c466deeea1ce8281a7b176.md"
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
  "completed_at": "2026-07-17T18:35:31+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "9b4d97f4783b549f6e72af9ae2f6264ad93d9e8cd5edce97a725dc1fd50984b8",
    "extraction_state_sha256": "8dcca52a50b0625d12fb6d08683faf7297413386cbf62c9c63ca94ba01243c43",
    "memory_schema_version": 2,
    "object_sha256": "3b35404fa11cbddd42e24b84b78e3d8a67a8bf317e3c64b3dce59a7b466fdb96",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "eee56d2937719c99f080c10ce9c2c366122958db6248fe15e5a5d83ea17bcfcf",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "56a9e397460fa3769e8a20415656d13f0606412b82b2a3f034a356119c32a493",
    "source_record_sha256s": {
      "source_08e53bb30d37610610477e01": "c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272"
    },
    "source_state_sha256": "2e3c72949c16069bcd9fc3ab82cd63591b32edfac7510454aacdb89be3e2730b",
    "work_identity_sha256": "a2d7a7003aee53bec813762596903cefba0d039bd5a37e746a4c0cac15b50302"
  },
  "consolidation_id": "consolidation_6a24c8c6be1c6abaaaf5b0b0",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:31+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_098586a5f7d8cb6b40d6"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_6a24c8c6be1c6abaaaf5b0b0",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_e0c466deeea1ce8281a7b176",
  "object_sha256_after": "3b35404fa11cbddd42e24b84b78e3d8a67a8bf317e3c64b3dce59a7b466fdb96",
  "object_sha256_before": "baacdc7d66f0a4eaa37fb474392f5eebbaa6070ce71745a16096a6f494b3b78f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_08e53bb30d37610610477e01"
  ],
  "source_records": [
    {
      "raw_content_sha256": "08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6",
      "source_id": "source_08e53bb30d37610610477e01",
      "source_record_sha256": "c7f190db28c40d57ff26a50adb88141e8b92941315f0e4ca88f8c047ee7c9272",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "08b354940a5bd1277ad483eb96c127be3fb094322fdc1680d820be0d4503c2d6"
  ],
  "started_at": "2026-07-17T18:35:31+08:00",
  "status": "complete",
  "title": "Consolidation: 来源原文：[1811.05931] Evolving intrinsic motivations for altruistic behavior",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:31+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
