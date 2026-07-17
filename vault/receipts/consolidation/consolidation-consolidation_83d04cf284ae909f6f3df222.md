---
id: "consolidation_83d04cf284ae909f6f3df222"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong"
created_at: "2026-07-17T18:35:23+08:00"
updated_at: "2026-07-17T18:35:23+08:00"
consolidation_id: "consolidation_83d04cf284ae909f6f3df222"
object_id: "claim_499470a2d077fe16b177bd1e"
object_version_before: 1
object_sha256_before: "ad6c232f1d5df7e8a308817957cc84b2b3177f6accea60445c0a1a4e22d8d7b0"
object_sha256_after: "6b9138463accd64e2ebe4741b75257b9fe0576f6509f710303c3818e8e23447d"
source_ids: ["source_ca1f80f2bf2e7d410ab2459e"]
source_sha256s: ["4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"]
source_records: [{"source_id": "source_ca1f80f2bf2e7d410ab2459e", "source_record_sha256": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a", "raw_content_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_66c305d8ef8ae5dbaeb5"]
started_at: "2026-07-17T18:35:23+08:00"
completed_at: "2026-07-17T18:35:23+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_499470a2d077fe16b177bd1e.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_ca1f80f2bf2e7d410ab2459e raw_sha256:4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_ca1f80f2bf2e7d410ab2459e record_sha256:493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_66c305d8ef8ae5dbaeb5"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_499470a2d077fe16b177bd1e"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_ca1f80f2bf2e7d410ab2459e"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:35+08:00", "source:source_ca1f80f2bf2e7d410ab2459e work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "6b9138463accd64e2ebe4741b75257b9fe0576f6509f710303c3818e8e23447d", "source_state_sha256": "fec2fefbecbafd93d48042f6a1e3d0c13cb4c6d4334063148d46ba15d0412fa4", "source_record_sha256s": {"source_ca1f80f2bf2e7d410ab2459e": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"}, "raw_state_sha256": "a29d1583bd2530613af82fa53caf1eff4e34101fe02e81f4ee49d945b53ced2a", "evidence_sha256": "7af3193e3163edb941e826d6051ef1c2fc7704a27e6e81510c1ec0af17f25c4e", "extraction_state_sha256": "e47c1b1119f31ff34b5cb93fb9b9a90a2c40aec54defbd1f3aacc82d5ff8cfb4", "work_identity_sha256": "43dccdde7b3abe0b5f684dd4c0051548b1c7df51f1a08602972a8f63126a9f76", "relation_neighborhood_sha256": "a6d18d5bbfc59ee3e9225a8efbf41fb352591179d693684a9560ba6dfd84e3c5", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_499470a2d077fe16b177bd1e"
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
        "evidence:evidence_66c305d8ef8ae5dbaeb5"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:35+08:00",
        "source:source_ca1f80f2bf2e7d410ab2459e work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_ca1f80f2bf2e7d410ab2459e record_sha256:493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_ca1f80f2bf2e7d410ab2459e raw_sha256:4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_ca1f80f2bf2e7d410ab2459e"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_499470a2d077fe16b177bd1e.md"
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
  "completed_at": "2026-07-17T18:35:23+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "7af3193e3163edb941e826d6051ef1c2fc7704a27e6e81510c1ec0af17f25c4e",
    "extraction_state_sha256": "e47c1b1119f31ff34b5cb93fb9b9a90a2c40aec54defbd1f3aacc82d5ff8cfb4",
    "memory_schema_version": 2,
    "object_sha256": "6b9138463accd64e2ebe4741b75257b9fe0576f6509f710303c3818e8e23447d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a29d1583bd2530613af82fa53caf1eff4e34101fe02e81f4ee49d945b53ced2a",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "a6d18d5bbfc59ee3e9225a8efbf41fb352591179d693684a9560ba6dfd84e3c5",
    "source_record_sha256s": {
      "source_ca1f80f2bf2e7d410ab2459e": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a"
    },
    "source_state_sha256": "fec2fefbecbafd93d48042f6a1e3d0c13cb4c6d4334063148d46ba15d0412fa4",
    "work_identity_sha256": "43dccdde7b3abe0b5f684dd4c0051548b1c7df51f1a08602972a8f63126a9f76"
  },
  "consolidation_id": "consolidation_83d04cf284ae909f6f3df222",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:23+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_66c305d8ef8ae5dbaeb5"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_83d04cf284ae909f6f3df222",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_499470a2d077fe16b177bd1e",
  "object_sha256_after": "6b9138463accd64e2ebe4741b75257b9fe0576f6509f710303c3818e8e23447d",
  "object_sha256_before": "ad6c232f1d5df7e8a308817957cc84b2b3177f6accea60445c0a1a4e22d8d7b0",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ca1f80f2bf2e7d410ab2459e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185",
      "source_id": "source_ca1f80f2bf2e7d410ab2459e",
      "source_record_sha256": "493f27881747d95af0426287fba8aab9cb80e9fb55669d104483aa24d452422a",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"
  ],
  "started_at": "2026-07-17T18:35:23+08:00",
  "status": "complete",
  "title": "Consolidation: Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:23+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
