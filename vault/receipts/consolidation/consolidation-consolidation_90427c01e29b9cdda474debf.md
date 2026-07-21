---
id: "consolidation_90427c01e29b9cdda474debf"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "failed"
execution_status: "complete"
validation_outcome: "failed"
title: "Consolidation: Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
created_at: "2026-07-19T23:49:19+08:00"
updated_at: "2026-07-19T23:49:19+08:00"
consolidation_id: "consolidation_90427c01e29b9cdda474debf"
object_id: "claim_play2perfect_realworld_tight_insertion_20260715"
object_version_before: 1
object_sha256_before: "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290"
object_sha256_after: "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
source_sha256s: ["8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"]
source_records: [{"source_id": "source_ea5eb55121fccd1ed14a40b0", "source_record_sha256": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "raw_content_sha256": "8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "work_id": null, "work_document_sha256": null}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "source_record_sha256": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7", "raw_content_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T23:49:18+08:00"
completed_at: "2026-07-19T23:49:19+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": false, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ea5eb55121fccd1ed14a40b0 raw_sha256:8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1", "source:source_05d8a9da9e0b53b94872f2a7 raw_sha256:a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ea5eb55121fccd1ed14a40b0 record_sha256:e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "source:source_05d8a9da9e0b53b94872f2a7 record_sha256:f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:source_05d8a9da9e0b53b94872f2a7", "evidence:source_05d8a9da9e0b53b94872f2a7", "evidence:source_05d8a9da9e0b53b94872f2a7"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "failed", "validation_outcome": "blocked", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": null, "findings": ["evidence_entailment:None"], "warnings": ["claim evidence entailment not checked"]}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_play2perfect_realworld_tight_insertion_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_05d8a9da9e0b53b94872f2a7", "related:source_ea5eb55121fccd1ed14a40b0"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T15:23:47+08:00", "source:source_ea5eb55121fccd1ed14a40b0 work_sha256:none", "source:source_05d8a9da9e0b53b94872f2a7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290", "source_state_sha256": "d4da862a0e60cbb5cc0a56d826ea134217ffd8e73186e6a0b90660a2b02a2690", "source_record_sha256s": {"source_ea5eb55121fccd1ed14a40b0": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286", "source_05d8a9da9e0b53b94872f2a7": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"}, "raw_state_sha256": "6eba102f1d2e90446a89bda51b90bba1bc8fce14423085230873f6194489e9f5", "evidence_sha256": "96a9a8dd0d2a3a8db23458587032e03ebc7b3a0a9844bc35adaf4958a8156da9", "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283", "work_identity_sha256": "1631c5e9b8530c25bc0bf7776050f90e143c37b67812c1ddd48e188daae5d99a", "relation_fingerprint": {"outgoing_relations_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e"}, "relation_neighborhood_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_play2perfect_realworld_tight_insertion_20260715"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": null,
      "execution_status": "failed",
      "findings": [
        "evidence_entailment:None"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": false,
      "validation_outcome": "blocked",
      "warnings": [
        "claim evidence entailment not checked"
      ]
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:source_05d8a9da9e0b53b94872f2a7",
        "evidence:source_05d8a9da9e0b53b94872f2a7",
        "evidence:source_05d8a9da9e0b53b94872f2a7"
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
        "object_updated_at:2026-07-17T15:23:47+08:00",
        "source:source_ea5eb55121fccd1ed14a40b0 work_sha256:none",
        "source:source_05d8a9da9e0b53b94872f2a7 work_sha256:none"
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
        "source:source_ea5eb55121fccd1ed14a40b0 record_sha256:e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286",
        "source:source_05d8a9da9e0b53b94872f2a7 record_sha256:f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7"
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
        "source:source_ea5eb55121fccd1ed14a40b0 raw_sha256:8670cbd229338fc8f6a66b11c60f43dd00714aab4442778246669f1d36b170f1",
        "source:source_05d8a9da9e0b53b94872f2a7 raw_sha256:a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47"
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
        "relation index inspected; 2 related objects found",
        "related:source_05d8a9da9e0b53b94872f2a7",
        "related:source_ea5eb55121fccd1ed14a40b0"
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
        "validated:vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md"
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
        "distinct_source_ids:2",
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
    "evidence_entailment_rechecked": false,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-19T23:49:19+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "96a9a8dd0d2a3a8db23458587032e03ebc7b3a0a9844bc35adaf4958a8156da9",
    "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283",
    "memory_schema_version": 2,
    "object_sha256": "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "6eba102f1d2e90446a89bda51b90bba1bc8fce14423085230873f6194489e9f5",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e"
    },
    "relation_neighborhood_sha256": "b6e0c801e9b0b35366c88fee20adbf39252423b56e115490c4ce52682c06cf6e",
    "source_record_sha256s": {
      "source_05d8a9da9e0b53b94872f2a7": "f137fef623741a32685b03f36528733821f3f93547e5a81f8a7ef7bce6f078b7",
      "source_ea5eb55121fccd1ed14a40b0": "e57aa5366536e28e4abf76fbfd6920f83010d044704b14ef2546121075f86286"
    },
    "source_state_sha256": "d4da862a0e60cbb5cc0a56d826ea134217ffd8e73186e6a0b90660a2b02a2690",
    "work_identity_sha256": "1631c5e9b8530c25bc0bf7776050f90e143c37b67812c1ddd48e188daae5d99a"
  },
  "consolidation_id": "consolidation_90427c01e29b9cdda474debf",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T23:49:19+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_90427c01e29b9cdda474debf",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_play2perfect_realworld_tight_insertion_20260715",
  "object_sha256_after": "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290",
  "object_sha256_before": "e83703256d1c9235a36fba5363c4888e055aec774b598926bed410722e55e290",
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
  "started_at": "2026-07-19T23:49:18+08:00",
  "status": "failed",
  "title": "Consolidation: Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T23:49:19+08:00",
  "validation_outcome": "failed",
  "warnings": [
    "claim evidence entailment not checked"
  ]
}
```
