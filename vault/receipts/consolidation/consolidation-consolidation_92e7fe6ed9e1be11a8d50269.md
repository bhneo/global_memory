---
id: "consolidation_92e7fe6ed9e1be11a8d50269"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: SIMPLE 仿真策略学习与评测环境"
created_at: "2026-07-19T03:05:25+08:00"
updated_at: "2026-07-19T03:05:25+08:00"
consolidation_id: "consolidation_92e7fe6ed9e1be11a8d50269"
object_id: "architecture_simple_simulation_policy_loop"
object_version_before: 1
object_sha256_before: "1ff01813a9d9ce9af4fcbb098cd68797f6d6e80af90181c3694c0fbe60ef1f3f"
object_sha256_after: "d1b3f8abc5b9d942305ef5c556ffa48205e3bc02084527ffd3590ae7975331fd"
source_ids: ["source_d75524a9040845cdc76db35c"]
source_sha256s: ["1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56"]
source_records: [{"source_id": "source_d75524a9040845cdc76db35c", "source_record_sha256": "07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00", "raw_content_sha256": "1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T03:05:24+08:00"
completed_at: "2026-07-19T03:05:25+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/architecture/architecture_simple_simulation_policy_loop.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d75524a9040845cdc76db35c raw_sha256:1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d75524a9040845cdc76db35c record_sha256:07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:architecture_simple_simulation_policy_loop"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_d75524a9040845cdc76db35c", "related:concept_sim_to_real_scene_infrastructure", "related:concept_staged_cross_embodiment_alignment"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T02:51:34+08:00", "source:source_d75524a9040845cdc76db35c work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "d1b3f8abc5b9d942305ef5c556ffa48205e3bc02084527ffd3590ae7975331fd", "source_state_sha256": "8ebe607259576f3dd3e3185c1dd378aae4a3aea01a19578d302e99793090fbfd", "source_record_sha256s": {"source_d75524a9040845cdc76db35c": "07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00"}, "raw_state_sha256": "8f1a147f8a76b7512be732ff2c1153068614c98456d32f5e6713148df4d6a8d4", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "d8c6ab2e3cf87c712b1fd69b551b52d3040dd3a9fdfc521b61f2b27617f89a15", "relation_fingerprint": {"outgoing_relations_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633"}, "relation_neighborhood_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:architecture_simple_simulation_policy_loop"
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
        "object_updated_at:2026-07-19T02:51:34+08:00",
        "source:source_d75524a9040845cdc76db35c work_sha256:none"
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
        "source:source_d75524a9040845cdc76db35c record_sha256:07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00"
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
        "source:source_d75524a9040845cdc76db35c raw_sha256:1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56"
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
        "relation index inspected; 3 related objects found",
        "related:source_d75524a9040845cdc76db35c",
        "related:concept_sim_to_real_scene_infrastructure",
        "related:concept_staged_cross_embodiment_alignment"
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
        "validated:vault/memory/architecture/architecture_simple_simulation_policy_loop.md"
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
  "completed_at": "2026-07-19T03:05:25+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "d1b3f8abc5b9d942305ef5c556ffa48205e3bc02084527ffd3590ae7975331fd",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "8f1a147f8a76b7512be732ff2c1153068614c98456d32f5e6713148df4d6a8d4",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633"
    },
    "relation_neighborhood_sha256": "3f4589fce30b31b1712084cdcce09564003e8c256d56e68b0eb99b17ccd42633",
    "source_record_sha256s": {
      "source_d75524a9040845cdc76db35c": "07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00"
    },
    "source_state_sha256": "8ebe607259576f3dd3e3185c1dd378aae4a3aea01a19578d302e99793090fbfd",
    "work_identity_sha256": "d8c6ab2e3cf87c712b1fd69b551b52d3040dd3a9fdfc521b61f2b27617f89a15"
  },
  "consolidation_id": "consolidation_92e7fe6ed9e1be11a8d50269",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:25+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_92e7fe6ed9e1be11a8d50269",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "architecture_simple_simulation_policy_loop",
  "object_sha256_after": "d1b3f8abc5b9d942305ef5c556ffa48205e3bc02084527ffd3590ae7975331fd",
  "object_sha256_before": "1ff01813a9d9ce9af4fcbb098cd68797f6d6e80af90181c3694c0fbe60ef1f3f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_d75524a9040845cdc76db35c"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56",
      "source_id": "source_d75524a9040845cdc76db35c",
      "source_record_sha256": "07ea6aaba06a152227834cdaa13cd14ff28ebc1af60185358e9188ea738f6c00",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56"
  ],
  "started_at": "2026-07-19T03:05:24+08:00",
  "status": "complete",
  "title": "Consolidation: SIMPLE 仿真策略学习与评测环境",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:25+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
