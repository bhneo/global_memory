---
id: "consolidation_bb1412cf9bd7f1ffed67ce53"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa"
created_at: "2026-07-18T16:02:50+08:00"
updated_at: "2026-07-18T16:02:50+08:00"
consolidation_id: "consolidation_bb1412cf9bd7f1ffed67ce53"
object_id: "claim_d3c1dc84377e8ab740cf0f2b"
object_version_before: 1
object_sha256_before: "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e"
object_sha256_after: "2eb3ce101ab694bb410ed8bb96bfd7b9ffae28668ad50581f59b1e3a0c20a57b"
source_ids: ["source_deb313c98b03fc4d0b33794a"]
source_sha256s: ["86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"]
source_records: [{"source_id": "source_deb313c98b03fc4d0b33794a", "source_record_sha256": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049", "raw_content_sha256": "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_c1f2401bf75874bd5ebc"]
started_at: "2026-07-18T16:02:49+08:00"
completed_at: "2026-07-18T16:02:50+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_deb313c98b03fc4d0b33794a raw_sha256:86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_deb313c98b03fc4d0b33794a record_sha256:430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_c1f2401bf75874bd5ebc"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "none", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_d3c1dc84377e8ab740cf0f2b"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_deb313c98b03fc4d0b33794a"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:30+08:00", "source:source_deb313c98b03fc4d0b33794a work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "2eb3ce101ab694bb410ed8bb96bfd7b9ffae28668ad50581f59b1e3a0c20a57b", "source_state_sha256": "f707033b1fee301ba7bf811199b67bbd8368d107050f0b02f153d19aa21d6376", "source_record_sha256s": {"source_deb313c98b03fc4d0b33794a": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"}, "raw_state_sha256": "8a75853423e72748431dfdb042c2468cd4d3315393c9b932cef05d3e3be983bd", "evidence_sha256": "12efe4ada79191fd59ce144c0c2508725a519143cc19bfe9834896ce65307115", "extraction_state_sha256": "3ae300fa5db8edfe86b83c755c444f3963d04b94ce5df46d48df39c4ea5b4e56", "work_identity_sha256": "32b26d2c508e2305f16563833a4dc003ee0bbc478eb00ee29e4684a2904e779f", "relation_fingerprint": {"outgoing_relations_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df"}, "relation_neighborhood_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_d3c1dc84377e8ab740cf0f2b"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "none",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:none"
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
        "evidence:evidence_c1f2401bf75874bd5ebc"
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
        "object_updated_at:2026-07-17T18:35:30+08:00",
        "source:source_deb313c98b03fc4d0b33794a work_sha256:none"
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
        "source:source_deb313c98b03fc4d0b33794a record_sha256:430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"
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
        "source:source_deb313c98b03fc4d0b33794a raw_sha256:86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"
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
        "related:source_deb313c98b03fc4d0b33794a"
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
        "validated:vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md"
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
  "completed_at": "2026-07-18T16:02:50+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "12efe4ada79191fd59ce144c0c2508725a519143cc19bfe9834896ce65307115",
    "extraction_state_sha256": "3ae300fa5db8edfe86b83c755c444f3963d04b94ce5df46d48df39c4ea5b4e56",
    "memory_schema_version": 2,
    "object_sha256": "2eb3ce101ab694bb410ed8bb96bfd7b9ffae28668ad50581f59b1e3a0c20a57b",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "8a75853423e72748431dfdb042c2468cd4d3315393c9b932cef05d3e3be983bd",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df"
    },
    "relation_neighborhood_sha256": "c181e4d37cf87b4dc56ce46442a3201b173f4396463443ea6cd408bd9a2174df",
    "source_record_sha256s": {
      "source_deb313c98b03fc4d0b33794a": "430d7926a3952b4a40f2a1c59e2fffa09a5458bca48074f32e846444a637e049"
    },
    "source_state_sha256": "f707033b1fee301ba7bf811199b67bbd8368d107050f0b02f153d19aa21d6376",
    "work_identity_sha256": "32b26d2c508e2305f16563833a4dc003ee0bbc478eb00ee29e4684a2904e779f"
  },
  "consolidation_id": "consolidation_bb1412cf9bd7f1ffed67ce53",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:02:50+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_c1f2401bf75874bd5ebc"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_bb1412cf9bd7f1ffed67ce53",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_d3c1dc84377e8ab740cf0f2b",
  "object_sha256_after": "2eb3ce101ab694bb410ed8bb96bfd7b9ffae28668ad50581f59b1e3a0c20a57b",
  "object_sha256_before": "634818cbebb53122dd9ea3457f276e149475376988e11384456a3773c198b55e",
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
  "started_at": "2026-07-18T16:02:49+08:00",
  "status": "complete",
  "title": "Consolidation: 来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:02:50+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
