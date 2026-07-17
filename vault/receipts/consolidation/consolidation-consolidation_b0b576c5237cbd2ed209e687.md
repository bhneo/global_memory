---
id: "consolidation_b0b576c5237cbd2ed209e687"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 符号回归"
created_at: "2026-07-17T18:35:59+08:00"
updated_at: "2026-07-17T18:35:59+08:00"
consolidation_id: "consolidation_b0b576c5237cbd2ed209e687"
object_id: "concept_symbolic_regression"
object_version_before: 1
object_sha256_before: "8579cac1c4db0d763d1469ad6764af7bc34f2ea2b0d8aeaeeabe4ab89be136a8"
object_sha256_after: "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
source_sha256s: ["fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"]
source_records: [{"source_id": "source_ef99e322cc662cffb7eb5c8f", "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:35:59+08:00"
completed_at: "2026-07-17T18:35:59+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/concept/concept_symbolic_regression.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 2 candidates inspected", "candidate:concept_symbolic_regression", "candidate:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:04+08:00", "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0", "source_state_sha256": "76d949421d93db35360c432eb5236e0804a0eba6c9af4a71469ad0285b5c3853", "source_record_sha256s": {"source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"}, "raw_state_sha256": "64308cc5642ef54084259d6818b79d8290fef9640c962e0fe5e03d8b8f1eb89d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "39e6164de950be7117eaaed37d34f224264371f72a2abfe6026e74f36a6e8d7a", "relation_neighborhood_sha256": "b87543b2419eb16fdce48b7e01f5676927d23703121dc4d500b13c2a34d05bd3", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:concept_symbolic_regression",
        "candidate:source_ef99e322cc662cffb7eb5c8f"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:24:04+08:00",
        "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_ef99e322cc662cffb7eb5c8f"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/concept/concept_symbolic_regression.md"
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
  "completed_at": "2026-07-17T18:35:59+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "64308cc5642ef54084259d6818b79d8290fef9640c962e0fe5e03d8b8f1eb89d",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "b87543b2419eb16fdce48b7e01f5676927d23703121dc4d500b13c2a34d05bd3",
    "source_record_sha256s": {
      "source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
    },
    "source_state_sha256": "76d949421d93db35360c432eb5236e0804a0eba6c9af4a71469ad0285b5c3853",
    "work_identity_sha256": "39e6164de950be7117eaaed37d34f224264371f72a2abfe6026e74f36a6e8d7a"
  },
  "consolidation_id": "consolidation_b0b576c5237cbd2ed209e687",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:59+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b0b576c5237cbd2ed209e687",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_symbolic_regression",
  "object_sha256_after": "786d37112698f1c172b9f3b1c47229ea65378047fac6d58dbb8df8f784afa6e0",
  "object_sha256_before": "8579cac1c4db0d763d1469ad6764af7bc34f2ea2b0d8aeaeeabe4ab89be136a8",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ef99e322cc662cffb7eb5c8f"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
      "source_id": "source_ef99e322cc662cffb7eb5c8f",
      "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58"
  ],
  "started_at": "2026-07-17T18:35:59+08:00",
  "status": "complete",
  "title": "Consolidation: 符号回归",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:59+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
