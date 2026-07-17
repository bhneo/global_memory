---
id: "consolidation_fe76429903fca65f63cb5028"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa"
created_at: "2026-07-17T18:35:30+08:00"
updated_at: "2026-07-17T18:35:30+08:00"
consolidation_id: "consolidation_fe76429903fca65f63cb5028"
object_id: "claim_d3c1dc84377e8ab740cf0f2b"
object_version_before: 1
object_sha256_before: "5d55ca8381561f8116a81b61397309fc60efa8b1fa84bd948c53dd64551baad5"
object_sha256_after: "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e"
source_ids: ["source_deb313c98b03fc4d0b33794a"]
source_sha256s: ["86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"]
source_records: [{"source_id": "source_deb313c98b03fc4d0b33794a", "source_record_sha256": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049", "raw_content_sha256": "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_c1f2401bf75874bd5ebc"]
started_at: "2026-07-17T18:35:29+08:00"
completed_at: "2026-07-17T18:35:30+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_deb313c98b03fc4d0b33794a raw_sha256:86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_deb313c98b03fc4d0b33794a record_sha256:430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_c1f2401bf75874bd5ebc"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_d3c1dc84377e8ab740cf0f2b"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_deb313c98b03fc4d0b33794a"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:40+08:00", "source:source_deb313c98b03fc4d0b33794a work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e", "source_state_sha256": "f707033b1fee301ba7bf811199b67bbd8368d107050f0b02f153d19aa21d6376", "source_record_sha256s": {"source_deb313c98b03fc4d0b33794a": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"}, "raw_state_sha256": "8a75853423e72748431dfdb042c2468cd4d3315393c9b932cef05d3e3be983bd", "evidence_sha256": "12efe4ada79191fd59ce144c0c2508725a519143cc19bfe9834896ce65307115", "extraction_state_sha256": "3ae300fa5db8edfe86b83c755c444f3963d04b94ce5df46d48df39c4ea5b4e56", "work_identity_sha256": "32b26d2c508e2305f16563833a4dc003ee0bbc478eb00ee29e4684a2904e779f", "relation_neighborhood_sha256": "ec7ca9ef6b7383eb1758f3211bacb00fdfdc22dbb410ccb6014c1b92f9040927", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_d3c1dc84377e8ab740cf0f2b"
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
        "evidence:evidence_c1f2401bf75874bd5ebc"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:40+08:00",
        "source:source_deb313c98b03fc4d0b33794a work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_deb313c98b03fc4d0b33794a record_sha256:430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_deb313c98b03fc4d0b33794a raw_sha256:86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_deb313c98b03fc4d0b33794a"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md"
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
  "completed_at": "2026-07-17T18:35:30+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "12efe4ada79191fd59ce144c0c2508725a519143cc19bfe9834896ce65307115",
    "extraction_state_sha256": "3ae300fa5db8edfe86b83c755c444f3963d04b94ce5df46d48df39c4ea5b4e56",
    "memory_schema_version": 2,
    "object_sha256": "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "8a75853423e72748431dfdb042c2468cd4d3315393c9b932cef05d3e3be983bd",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "ec7ca9ef6b7383eb1758f3211bacb00fdfdc22dbb410ccb6014c1b92f9040927",
    "source_record_sha256s": {
      "source_deb313c98b03fc4d0b33794a": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"
    },
    "source_state_sha256": "f707033b1fee301ba7bf811199b67bbd8368d107050f0b02f153d19aa21d6376",
    "work_identity_sha256": "32b26d2c508e2305f16563833a4dc003ee0bbc478eb00ee29e4684a2904e779f"
  },
  "consolidation_id": "consolidation_fe76429903fca65f63cb5028",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:30+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_c1f2401bf75874bd5ebc"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_fe76429903fca65f63cb5028",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_d3c1dc84377e8ab740cf0f2b",
  "object_sha256_after": "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e",
  "object_sha256_before": "5d55ca8381561f8116a81b61397309fc60efa8b1fa84bd948c53dd64551baad5",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_deb313c98b03fc4d0b33794a"
  ],
  "source_records": [
    {
      "raw_content_sha256": "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09",
      "source_id": "source_deb313c98b03fc4d0b33794a",
      "source_record_sha256": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"
  ],
  "started_at": "2026-07-17T18:35:29+08:00",
  "status": "complete",
  "title": "Consolidation: 来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:30+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
