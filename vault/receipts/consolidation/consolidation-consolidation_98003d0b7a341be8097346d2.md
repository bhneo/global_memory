---
id: "consolidation_98003d0b7a341be8097346d2"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 关系触发的具身过程安全"
created_at: "2026-07-26T12:32:37+08:00"
updated_at: "2026-07-26T12:32:37+08:00"
consolidation_id: "consolidation_98003d0b7a341be8097346d2"
object_id: "concept_relation_triggered_process_safety"
object_version_before: 1
object_sha256_before: "cbb8e19420195e9877f1d51c6b782d210ba589da9b8ff24f98d14e21233604dc"
object_sha256_after: "63e465dc505fddc7a47240698b419540627e7c7753f8e8bc6eb16e573c33a4f2"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
source_sha256s: ["f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"]
source_records: [{"source_id": "source_b470fe87f9d09df2b7d3b5fd", "source_record_sha256": "f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7", "raw_content_sha256": "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:32:36+08:00"
completed_at: "2026-07-26T12:32:37+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_relation_triggered_process_safety.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b470fe87f9d09df2b7d3b5fd raw_sha256:f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b470fe87f9d09df2b7d3b5fd record_sha256:f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_relation_triggered_process_safety"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_b470fe87f9d09df2b7d3b5fd", "related:concept_648a44e346f991eab5956e55", "related:concept_typed_verified_robot_skill_graph", "related:concept_relation_triggered_process_safety"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-26T12:32:28+08:00", "source:source_b470fe87f9d09df2b7d3b5fd work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "63e465dc505fddc7a47240698b419540627e7c7753f8e8bc6eb16e573c33a4f2", "source_state_sha256": "451da695349369364ca97ea32d31cb1838c3fd262bf9b7db9db435d51d344e83", "source_record_sha256s": {"source_b470fe87f9d09df2b7d3b5fd": "f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7"}, "raw_state_sha256": "a515be2b4a551ef7961ad90b1ebdd6d09c528eec5df7525169503a5a80d2f1e0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "ba3a03bc225765d2621d58524518fed2cbd8b837beaa955d6e688a233aa23727", "relation_fingerprint": {"outgoing_relations_sha256": "060e40c8c8c12031a9dc6393da0e31f86d6199139d94d37ac37b15f22682c178", "incoming_relations_sha256": "6b628d7b64f1c1b4195457502e76d53fd4c64d61865b552c89224dd245f72923", "full_neighborhood_sha256": "4c9807f526e0dda3855f07903191c8519c3ae1045253e235b9bf31a99426b266"}, "relation_neighborhood_sha256": "4c9807f526e0dda3855f07903191c8519c3ae1045253e235b9bf31a99426b266", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 关系触发的具身过程安全\n\n将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。", "new_statement": "# 关系触发的具身过程安全\n\n将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。", "changed_fields": [], "reason": "compile bundle from source_b470fe87f9d09df2b7d3b5fd", "trigger_source": "source_b470fe87f9d09df2b7d3b5fd", "evidence_added": []}]
change_summary: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_b470fe87f9d09df2b7d3b5fd",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 关系触发的具身过程安全\n\n将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。",
      "previous_statement": "# 关系触发的具身过程安全\n\n将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。",
      "reason": "compile bundle from source_b470fe87f9d09df2b7d3b5fd",
      "trigger_source": "source_b470fe87f9d09df2b7d3b5fd"
    }
  ],
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
        "candidate:concept_relation_triggered_process_safety"
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
        "object_updated_at:2026-07-26T12:32:28+08:00",
        "source:source_b470fe87f9d09df2b7d3b5fd work_sha256:none"
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
        "source:source_b470fe87f9d09df2b7d3b5fd record_sha256:f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7"
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
        "source:source_b470fe87f9d09df2b7d3b5fd raw_sha256:f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"
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
        "relation index inspected; 4 related objects found",
        "related:source_b470fe87f9d09df2b7d3b5fd",
        "related:concept_648a44e346f991eab5956e55",
        "related:concept_typed_verified_robot_skill_graph",
        "related:concept_relation_triggered_process_safety"
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
        "validated:vault/memory/concept/concept_relation_triggered_process_safety.md"
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
  "completed_at": "2026-07-26T12:32:37+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "63e465dc505fddc7a47240698b419540627e7c7753f8e8bc6eb16e573c33a4f2",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a515be2b4a551ef7961ad90b1ebdd6d09c528eec5df7525169503a5a80d2f1e0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "4c9807f526e0dda3855f07903191c8519c3ae1045253e235b9bf31a99426b266",
      "incoming_relations_sha256": "6b628d7b64f1c1b4195457502e76d53fd4c64d61865b552c89224dd245f72923",
      "outgoing_relations_sha256": "060e40c8c8c12031a9dc6393da0e31f86d6199139d94d37ac37b15f22682c178"
    },
    "relation_neighborhood_sha256": "4c9807f526e0dda3855f07903191c8519c3ae1045253e235b9bf31a99426b266",
    "source_record_sha256s": {
      "source_b470fe87f9d09df2b7d3b5fd": "f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7"
    },
    "source_state_sha256": "451da695349369364ca97ea32d31cb1838c3fd262bf9b7db9db435d51d344e83",
    "work_identity_sha256": "ba3a03bc225765d2621d58524518fed2cbd8b837beaa955d6e688a233aa23727"
  },
  "consolidation_id": "consolidation_98003d0b7a341be8097346d2",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:32:37+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_98003d0b7a341be8097346d2",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_relation_triggered_process_safety",
  "object_sha256_after": "63e465dc505fddc7a47240698b419540627e7c7753f8e8bc6eb16e573c33a4f2",
  "object_sha256_before": "cbb8e19420195e9877f1d51c6b782d210ba589da9b8ff24f98d14e21233604dc",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_b470fe87f9d09df2b7d3b5fd"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11",
      "source_id": "source_b470fe87f9d09df2b7d3b5fd",
      "source_record_sha256": "f74484e37260cab76e4e5aeecfaace943d2720496a8b926962d6fc388e883ca7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"
  ],
  "started_at": "2026-07-26T12:32:36+08:00",
  "status": "complete",
  "title": "Consolidation: 关系触发的具身过程安全",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:32:37+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
