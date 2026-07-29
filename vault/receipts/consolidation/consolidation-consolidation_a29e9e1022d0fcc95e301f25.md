---
id: "consolidation_a29e9e1022d0fcc95e301f25"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 面向真实零售人形机器人的数据高效 VLA 后训练闭环"
created_at: "2026-07-26T12:33:44+08:00"
updated_at: "2026-07-26T12:33:44+08:00"
consolidation_id: "consolidation_a29e9e1022d0fcc95e301f25"
object_id: "concept_bcf39e7d937cfdf22e3c49e2"
object_version_before: 1
object_sha256_before: "8fb2e5a7bc626ccb1843ef7d344e9b308bb30759d1f706efc0345d29cd95484d"
object_sha256_after: "0293bb65399e08c133738c7c084698189133722e34d0ceb4c536083461adb42a"
source_ids: ["source_3846f8c1451f8a12e0f87b33"]
source_sha256s: ["a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab"]
source_records: [{"source_id": "source_3846f8c1451f8a12e0f87b33", "source_record_sha256": "56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac", "raw_content_sha256": "a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:44+08:00"
completed_at: "2026-07-26T12:33:44+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_3846f8c1451f8a12e0f87b33 raw_sha256:a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_3846f8c1451f8a12e0f87b33 record_sha256:56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_bcf39e7d937cfdf22e3c49e2"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_3846f8c1451f8a12e0f87b33", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-24T18:05:39+08:00", "source:source_3846f8c1451f8a12e0f87b33 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "0293bb65399e08c133738c7c084698189133722e34d0ceb4c536083461adb42a", "source_state_sha256": "bb7a8ddc04febf231e143e5ca8f27ea419bf1c83914f552e16581ec0422ed2fb", "source_record_sha256s": {"source_3846f8c1451f8a12e0f87b33": "56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac"}, "raw_state_sha256": "68fc0e6bbdb7df7acd2b109417edefd4aba73e983011a274f0b0e91432c44ffd", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "a1d6f0c999100f7694126b42d2783bd028339be16ed6dbc0955334bbc2e6c253", "relation_fingerprint": {"outgoing_relations_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd"}, "relation_neighborhood_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_bcf39e7d937cfdf22e3c49e2"
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
        "object_updated_at:2026-07-24T18:05:39+08:00",
        "source:source_3846f8c1451f8a12e0f87b33 work_sha256:none"
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
        "source:source_3846f8c1451f8a12e0f87b33 record_sha256:56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac"
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
        "source:source_3846f8c1451f8a12e0f87b33 raw_sha256:a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab"
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
        "related:source_3846f8c1451f8a12e0f87b33",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md"
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
  "completed_at": "2026-07-26T12:33:44+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "0293bb65399e08c133738c7c084698189133722e34d0ceb4c536083461adb42a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "68fc0e6bbdb7df7acd2b109417edefd4aba73e983011a274f0b0e91432c44ffd",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd"
    },
    "relation_neighborhood_sha256": "66a3cb74db75190d089cf859207ed0e9540c962117355b0a723fe833718786fd",
    "source_record_sha256s": {
      "source_3846f8c1451f8a12e0f87b33": "56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac"
    },
    "source_state_sha256": "bb7a8ddc04febf231e143e5ca8f27ea419bf1c83914f552e16581ec0422ed2fb",
    "work_identity_sha256": "a1d6f0c999100f7694126b42d2783bd028339be16ed6dbc0955334bbc2e6c253"
  },
  "consolidation_id": "consolidation_a29e9e1022d0fcc95e301f25",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:44+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a29e9e1022d0fcc95e301f25",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_bcf39e7d937cfdf22e3c49e2",
  "object_sha256_after": "0293bb65399e08c133738c7c084698189133722e34d0ceb4c536083461adb42a",
  "object_sha256_before": "8fb2e5a7bc626ccb1843ef7d344e9b308bb30759d1f706efc0345d29cd95484d",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_3846f8c1451f8a12e0f87b33"
  ],
  "source_records": [
    {
      "raw_content_sha256": "a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab",
      "source_id": "source_3846f8c1451f8a12e0f87b33",
      "source_record_sha256": "56c1368c7c4d0528e4ea027b73955aa9d3d126d6ec7138b306b4fe11f529c8ac",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab"
  ],
  "started_at": "2026-07-26T12:33:44+08:00",
  "status": "complete",
  "title": "Consolidation: 面向真实零售人形机器人的数据高效 VLA 后训练闭环",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:44+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
