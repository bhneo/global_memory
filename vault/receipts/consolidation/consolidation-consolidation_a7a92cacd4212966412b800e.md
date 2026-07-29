---
id: "consolidation_a7a92cacd4212966412b800e"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory"
created_at: "2026-07-28T16:34:07+08:00"
updated_at: "2026-07-28T16:34:07+08:00"
consolidation_id: "consolidation_a7a92cacd4212966412b800e"
object_id: "concept_f5d1ef9eaed1cd6bec4d4c52"
object_version_before: 1
object_sha256_before: "ef6a9dbea84729676b8cd2be532e76ae428783d42d6bfb1b1f029a3ff8284400"
object_sha256_after: "bce3a2b4e112321c3d72431abb1ce9f0405bdcb1899da6a1cd644a80742782cd"
source_ids: ["source_01ed2f19e91bb0eb1ec3ee92"]
source_sha256s: ["f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9"]
source_records: [{"source_id": "source_01ed2f19e91bb0eb1ec3ee92", "source_record_sha256": "2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca", "raw_content_sha256": "f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-28T16:34:07+08:00"
completed_at: "2026-07-28T16:34:07+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_f5d1ef9eaed1cd6bec4d4c52.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_01ed2f19e91bb0eb1ec3ee92 raw_sha256:f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_01ed2f19e91bb0eb1ec3ee92 record_sha256:2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_f5d1ef9eaed1cd6bec4d4c52"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_01ed2f19e91bb0eb1ec3ee92"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-28T13:11:56+08:00", "source:source_01ed2f19e91bb0eb1ec3ee92 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "bce3a2b4e112321c3d72431abb1ce9f0405bdcb1899da6a1cd644a80742782cd", "source_state_sha256": "436a206fa98826fd4208a48fcbadd14ea030482c58ae0ab822aa2b688f2bb3b0", "source_record_sha256s": {"source_01ed2f19e91bb0eb1ec3ee92": "2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca"}, "raw_state_sha256": "50b478e19739895f639b1701e87bf308de8c1404e793d6d70e84b708e8f14154", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "03d1891580717729f585326ae382466024a0a2e14ad12d15ba0534bf2f8e536d", "relation_fingerprint": {"outgoing_relations_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df"}, "relation_neighborhood_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_f5d1ef9eaed1cd6bec4d4c52"
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
        "object_updated_at:2026-07-28T13:11:56+08:00",
        "source:source_01ed2f19e91bb0eb1ec3ee92 work_sha256:none"
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
        "source:source_01ed2f19e91bb0eb1ec3ee92 record_sha256:2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca"
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
        "source:source_01ed2f19e91bb0eb1ec3ee92 raw_sha256:f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9"
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
        "related:source_01ed2f19e91bb0eb1ec3ee92"
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
        "validated:vault/memory/concept/concept_f5d1ef9eaed1cd6bec4d4c52.md"
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
  "completed_at": "2026-07-28T16:34:07+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bce3a2b4e112321c3d72431abb1ce9f0405bdcb1899da6a1cd644a80742782cd",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "50b478e19739895f639b1701e87bf308de8c1404e793d6d70e84b708e8f14154",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df"
    },
    "relation_neighborhood_sha256": "cbd4376ff4db3f596a2aa2fccaf23ff26c28a6d498b8ff828149bb60cc2de4df",
    "source_record_sha256s": {
      "source_01ed2f19e91bb0eb1ec3ee92": "2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca"
    },
    "source_state_sha256": "436a206fa98826fd4208a48fcbadd14ea030482c58ae0ab822aa2b688f2bb3b0",
    "work_identity_sha256": "03d1891580717729f585326ae382466024a0a2e14ad12d15ba0534bf2f8e536d"
  },
  "consolidation_id": "consolidation_a7a92cacd4212966412b800e",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-28T16:34:07+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a7a92cacd4212966412b800e",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_f5d1ef9eaed1cd6bec4d4c52",
  "object_sha256_after": "bce3a2b4e112321c3d72431abb1ce9f0405bdcb1899da6a1cd644a80742782cd",
  "object_sha256_before": "ef6a9dbea84729676b8cd2be532e76ae428783d42d6bfb1b1f029a3ff8284400",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_01ed2f19e91bb0eb1ec3ee92"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9",
      "source_id": "source_01ed2f19e91bb0eb1ec3ee92",
      "source_record_sha256": "2506864b0073e9d97f697958966148413391712ed910b4ac04d3ea246b2c37ca",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f9d712543f4f027a78c64368dde07e1ae5386dd14173816d4fd26ca98c58bcf9"
  ],
  "started_at": "2026-07-28T16:34:07+08:00",
  "status": "complete",
  "title": "Consolidation: 图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-28T16:34:07+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
