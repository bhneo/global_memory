---
id: "consolidation_ecb3605c08ad6e0181d4bad3"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "failed"
execution_status: "complete"
validation_outcome: "failed"
title: "Consolidation: Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率"
created_at: "2026-07-17T18:38:45+08:00"
updated_at: "2026-07-17T18:38:45+08:00"
consolidation_id: "consolidation_ecb3605c08ad6e0181d4bad3"
object_id: "claim_play2perfect_sample_efficiency_20260715"
object_version_before: 1
object_sha256_before: "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52"
object_sha256_after: "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
source_sha256s: ["8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"]
source_records: [{"source_id": "source_ea5eb55121fccd1ed14a40b0", "source_record_sha256": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "raw_content_sha256": "8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "work_id": null, "work_document_sha256": null}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "source_record_sha256": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7", "raw_content_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:38:45+08:00"
completed_at: "2026-07-17T18:38:45+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": false, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_ea5eb55121fccd1ed14a40b0 raw_sha256:8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "source:source_05d8a9da9e0b53b94872f2a7 raw_sha256:a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_ea5eb55121fccd1ed14a40b0 record_sha256:e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "source:source_05d8a9da9e0b53b94872f2a7 record_sha256:f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:source_05d8a9da9e0b53b94872f2a7", "evidence:source_05d8a9da9e0b53b94872f2a7", "evidence:source_05d8a9da9e0b53b94872f2a7"], "warnings": []}, "evidence_entailment_rechecked": {"status": "failed", "findings": ["evidence_entailment:None"], "warnings": ["claim evidence entailment not checked"]}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_play2perfect_sample_efficiency_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_05d8a9da9e0b53b94872f2a7", "related:source_ea5eb55121fccd1ed14a40b0"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:48+08:00", "source:source_ea5eb55121fccd1ed14a40b0 work_sha256:none", "source:source_05d8a9da9e0b53b94872f2a7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52", "source_state_sha256": "d4da862a0e60cbb5cc0a56d826ea134217ffd8e73186e6a0b90660a2b02a2690", "source_record_sha256s": {"source_ea5eb55121fccd1ed14a40b0": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "source_05d8a9da9e0b53b94872f2a7": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"}, "raw_state_sha256": "6eba102f1d2e90446a89bda51b90bba1bc8fce14423085230873f6194489e9f5", "evidence_sha256": "8aac26eed188fd0d8352d48a8dbe89b7eb0d6052a081c362b80326e6ad702821", "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283", "work_identity_sha256": "1631c5e9b8530c25bc0bf7776050f90e143c37b67812c1ddd48e188daae5d99a", "relation_neighborhood_sha256": "705850bea87db733e61e59d2c046cb81b53eb66feaff1273616d98f890e12bd2", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "failed"
changes: []
change_summary: "No semantic change."
warnings: ["claim evidence entailment not checked"]
exceptions_created: []
promotion_recommendation: "blocked"
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
        "candidate:claim_play2perfect_sample_efficiency_20260715"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:None"
      ],
      "status": "failed",
      "warnings": [
        "claim evidence entailment not checked"
      ]
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:source_05d8a9da9e0b53b94872f2a7",
        "evidence:source_05d8a9da9e0b53b94872f2a7",
        "evidence:source_05d8a9da9e0b53b94872f2a7"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:48+08:00",
        "source:source_ea5eb55121fccd1ed14a40b0 work_sha256:none",
        "source:source_05d8a9da9e0b53b94872f2a7 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_ea5eb55121fccd1ed14a40b0 record_sha256:e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286",
        "source:source_05d8a9da9e0b53b94872f2a7 record_sha256:f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_ea5eb55121fccd1ed14a40b0 raw_sha256:8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1",
        "source:source_05d8a9da9e0b53b94872f2a7 raw_sha256:a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_05d8a9da9e0b53b94872f2a7",
        "related:source_ea5eb55121fccd1ed14a40b0"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:2",
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
    "evidence_entailment_rechecked": false,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-17T18:38:45+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "8aac26eed188fd0d8352d48a8dbe89b7eb0d6052a081c362b80326e6ad702821",
    "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283",
    "memory_schema_version": 2,
    "object_sha256": "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "6eba102f1d2e90446a89bda51b90bba1bc8fce14423085230873f6194489e9f5",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "705850bea87db733e61e59d2c046cb81b53eb66feaff1273616d98f890e12bd2",
    "source_record_sha256s": {
      "source_05d8a9da9e0b53b94872f2a7": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7",
      "source_ea5eb55121fccd1ed14a40b0": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286"
    },
    "source_state_sha256": "d4da862a0e60cbb5cc0a56d826ea134217ffd8e73186e6a0b90660a2b02a2690",
    "work_identity_sha256": "1631c5e9b8530c25bc0bf7776050f90e143c37b67812c1ddd48e188daae5d99a"
  },
  "consolidation_id": "consolidation_ecb3605c08ad6e0181d4bad3",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:38:45+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_ecb3605c08ad6e0181d4bad3",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_play2perfect_sample_efficiency_20260715",
  "object_sha256_after": "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52",
  "object_sha256_before": "e2f41e552b8adcca8168d7a8d7b6eab8bb94e98ea264dabd505373fd4828ba52",
  "object_version_before": 1,
  "promotion_recommendation": "blocked",
  "receipt_schema_version": 2,
  "result": "failed",
  "source_ids": [
    "source_ea5eb55121fccd1ed14a40b0",
    "source_05d8a9da9e0b53b94872f2a7"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1",
      "source_id": "source_ea5eb55121fccd1ed14a40b0",
      "source_record_sha256": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47",
      "source_id": "source_05d8a9da9e0b53b94872f2a7",
      "source_record_sha256": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1",
    "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"
  ],
  "started_at": "2026-07-17T18:38:45+08:00",
  "status": "failed",
  "title": "Consolidation: Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:38:45+08:00",
  "validation_outcome": "failed",
  "warnings": [
    "claim evidence entailment not checked"
  ]
}
```
