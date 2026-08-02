---
id: "consolidation_6ea8a499ee6725f802de8874"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 生成器状态监督的当前态预测控制接口 / Current-only predictive control interface supervised by generator states"
created_at: "2026-08-02T12:30:45+08:00"
updated_at: "2026-08-02T12:30:45+08:00"
consolidation_id: "consolidation_6ea8a499ee6725f802de8874"
object_id: "concept_a13a20254f749ae9c5484c6b"
object_version_before: 1
object_sha256_before: "d9fef66c63060af2abad1367d03d495bdb1d1f2327b8c9dffe9941453fb048f7"
object_sha256_after: "29f9210061b33c05e05facd779092b796b5906d43936f9fc74ea7e855670f5eb"
source_ids: ["source_029a4fa602a118a1ead1bbf4"]
source_sha256s: ["fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94"]
source_records: [{"source_id": "source_029a4fa602a118a1ead1bbf4", "source_record_sha256": "04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84", "raw_content_sha256": "fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T12:30:45+08:00"
completed_at: "2026-08-02T12:30:45+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_a13a20254f749ae9c5484c6b.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_029a4fa602a118a1ead1bbf4 raw_sha256:fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_029a4fa602a118a1ead1bbf4 record_sha256:04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_a13a20254f749ae9c5484c6b"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_029a4fa602a118a1ead1bbf4", "related:concept_world_model_evaluation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-01T18:22:36+08:00", "source:source_029a4fa602a118a1ead1bbf4 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "29f9210061b33c05e05facd779092b796b5906d43936f9fc74ea7e855670f5eb", "source_state_sha256": "328cb5e6023e17d9b019df6ae0507fa1e3a5ebbe6ec95d1ff5fe45f7f5cddd74", "source_record_sha256s": {"source_029a4fa602a118a1ead1bbf4": "04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84"}, "raw_state_sha256": "4ea3e81b8bfe382b0943934a21fa128defc41e12cedce759a703da4e9c271e79", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "eb8e0d5c1a22f492986ed531b53ba26705bb0ab476703d9f17059cdc1b51c8cf", "relation_fingerprint": {"outgoing_relations_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579"}, "relation_neighborhood_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_a13a20254f749ae9c5484c6b"
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
        "object_updated_at:2026-08-01T18:22:36+08:00",
        "source:source_029a4fa602a118a1ead1bbf4 work_sha256:none"
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
        "source:source_029a4fa602a118a1ead1bbf4 record_sha256:04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84"
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
        "source:source_029a4fa602a118a1ead1bbf4 raw_sha256:fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94"
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
        "related:source_029a4fa602a118a1ead1bbf4",
        "related:concept_world_model_evaluation"
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
        "validated:vault/memory/concept/concept_a13a20254f749ae9c5484c6b.md"
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
  "completed_at": "2026-08-02T12:30:45+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "29f9210061b33c05e05facd779092b796b5906d43936f9fc74ea7e855670f5eb",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "4ea3e81b8bfe382b0943934a21fa128defc41e12cedce759a703da4e9c271e79",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579"
    },
    "relation_neighborhood_sha256": "31c7ca84c9f442914ff35574089c6b8e8f8a04624a2169dd6dca5c13757ca579",
    "source_record_sha256s": {
      "source_029a4fa602a118a1ead1bbf4": "04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84"
    },
    "source_state_sha256": "328cb5e6023e17d9b019df6ae0507fa1e3a5ebbe6ec95d1ff5fe45f7f5cddd74",
    "work_identity_sha256": "eb8e0d5c1a22f492986ed531b53ba26705bb0ab476703d9f17059cdc1b51c8cf"
  },
  "consolidation_id": "consolidation_6ea8a499ee6725f802de8874",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T12:30:45+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_6ea8a499ee6725f802de8874",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_a13a20254f749ae9c5484c6b",
  "object_sha256_after": "29f9210061b33c05e05facd779092b796b5906d43936f9fc74ea7e855670f5eb",
  "object_sha256_before": "d9fef66c63060af2abad1367d03d495bdb1d1f2327b8c9dffe9941453fb048f7",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_029a4fa602a118a1ead1bbf4"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94",
      "source_id": "source_029a4fa602a118a1ead1bbf4",
      "source_record_sha256": "04db092b5f3be8abc838f0ef2e3e9642ccec78d36030be7cffd0eba4ed6cbd84",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fb5489082532dc2fd7745f0fac0c1a9285f9fb43100d39e4abf9ccfe27d1af94"
  ],
  "started_at": "2026-08-02T12:30:45+08:00",
  "status": "complete",
  "title": "Consolidation: 生成器状态监督的当前态预测控制接口 / Current-only predictive control interface supervised by generator states",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T12:30:45+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
