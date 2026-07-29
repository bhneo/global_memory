---
id: "consolidation_db2b1388451c586474f336ba"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 训练—模型—部署三分布的操作鲁棒性诊断"
created_at: "2026-07-26T12:33:30+08:00"
updated_at: "2026-07-26T12:33:30+08:00"
consolidation_id: "consolidation_db2b1388451c586474f336ba"
object_id: "concept_3363773a8f142fcedd29ce9d"
object_version_before: 1
object_sha256_before: "c09e3dbede190abe152e48ad5dc03f430633aae6c1f92ba0faca95d03a4e8ccc"
object_sha256_after: "994363a97ca8c49f2b676f1c42b961aa7ec7e3b3beac2fda4155440e12f5157e"
source_ids: ["source_cdce2dfd2021019fc46a9ea7"]
source_sha256s: ["d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd"]
source_records: [{"source_id": "source_cdce2dfd2021019fc46a9ea7", "source_record_sha256": "f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db", "raw_content_sha256": "d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:30+08:00"
completed_at: "2026-07-26T12:33:30+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_3363773a8f142fcedd29ce9d.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_cdce2dfd2021019fc46a9ea7 raw_sha256:d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_cdce2dfd2021019fc46a9ea7 record_sha256:f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_3363773a8f142fcedd29ce9d"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_cdce2dfd2021019fc46a9ea7", "related:concept_real_robot_deployment_iteration_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-23T18:06:46+08:00", "source:source_cdce2dfd2021019fc46a9ea7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "994363a97ca8c49f2b676f1c42b961aa7ec7e3b3beac2fda4155440e12f5157e", "source_state_sha256": "9e7f15fec7d66a558ad1db1f796c0ee114b763e457c9387a1b684208b972c369", "source_record_sha256s": {"source_cdce2dfd2021019fc46a9ea7": "f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db"}, "raw_state_sha256": "196471512ba6f907f3c1e8969e43900aa5e492637c0c3eb84eec1dfb32d7b102", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "8cd95b9cc75feaf9d8809f1cc0e5a7ae6d4a2708baea8b2b9b5a75a801033ed6", "relation_fingerprint": {"outgoing_relations_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0"}, "relation_neighborhood_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_3363773a8f142fcedd29ce9d"
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
        "object_updated_at:2026-07-23T18:06:46+08:00",
        "source:source_cdce2dfd2021019fc46a9ea7 work_sha256:none"
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
        "source:source_cdce2dfd2021019fc46a9ea7 record_sha256:f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db"
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
        "source:source_cdce2dfd2021019fc46a9ea7 raw_sha256:d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd"
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
        "related:source_cdce2dfd2021019fc46a9ea7",
        "related:concept_real_robot_deployment_iteration_loop"
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
        "validated:vault/memory/concept/concept_3363773a8f142fcedd29ce9d.md"
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
  "completed_at": "2026-07-26T12:33:30+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "994363a97ca8c49f2b676f1c42b961aa7ec7e3b3beac2fda4155440e12f5157e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "196471512ba6f907f3c1e8969e43900aa5e492637c0c3eb84eec1dfb32d7b102",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0"
    },
    "relation_neighborhood_sha256": "4e7073a5f9bf62f3a19d3e8f3fca6209a05a0322d903b5adc709fda9cd3a15f0",
    "source_record_sha256s": {
      "source_cdce2dfd2021019fc46a9ea7": "f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db"
    },
    "source_state_sha256": "9e7f15fec7d66a558ad1db1f796c0ee114b763e457c9387a1b684208b972c369",
    "work_identity_sha256": "8cd95b9cc75feaf9d8809f1cc0e5a7ae6d4a2708baea8b2b9b5a75a801033ed6"
  },
  "consolidation_id": "consolidation_db2b1388451c586474f336ba",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:30+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_db2b1388451c586474f336ba",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_3363773a8f142fcedd29ce9d",
  "object_sha256_after": "994363a97ca8c49f2b676f1c42b961aa7ec7e3b3beac2fda4155440e12f5157e",
  "object_sha256_before": "c09e3dbede190abe152e48ad5dc03f430633aae6c1f92ba0faca95d03a4e8ccc",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_cdce2dfd2021019fc46a9ea7"
  ],
  "source_records": [
    {
      "raw_content_sha256": "d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd",
      "source_id": "source_cdce2dfd2021019fc46a9ea7",
      "source_record_sha256": "f626dab6edc2e7a2d7d57df5038e9d1b684fbc9ab71160151e7d3803a8e105db",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd"
  ],
  "started_at": "2026-07-26T12:33:30+08:00",
  "status": "complete",
  "title": "Consolidation: 训练—模型—部署三分布的操作鲁棒性诊断",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:30+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
