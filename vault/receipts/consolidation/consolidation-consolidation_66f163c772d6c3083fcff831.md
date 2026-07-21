---
id: "consolidation_66f163c772d6c3083fcff831"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 冻结 VLA 的非对称技能编排"
created_at: "2026-07-20T13:33:22+08:00"
updated_at: "2026-07-20T13:33:22+08:00"
consolidation_id: "consolidation_66f163c772d6c3083fcff831"
object_id: "concept_asymmetric_frozen_vla_harness"
object_version_before: 1
object_sha256_before: "5b13ad62d9fa7bc3ab469258cf67184f2f66bd68dacf7da23eda3fd0651b0972"
object_sha256_after: "ac1925614d58ae6652df994544c68fea38f6af61b38fb22fa6abd16e09385758"
source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386"]
source_sha256s: ["b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d"]
source_records: [{"source_id": "source_4bff03c9d5adb3463b34f947", "source_record_sha256": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "raw_content_sha256": "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "work_id": null, "work_document_sha256": null}, {"source_id": "source_6b52a51e2b4a3be43c97c386", "source_record_sha256": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e", "raw_content_sha256": "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:33:22+08:00"
completed_at: "2026-07-20T13:33:22+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4bff03c9d5adb3463b34f947 raw_sha256:b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "source:source_6b52a51e2b4a3be43c97c386 raw_sha256:89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4bff03c9d5adb3463b34f947 record_sha256:a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "source:source_6b52a51e2b4a3be43c97c386 record_sha256:ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_asymmetric_frozen_vla_harness", "candidate:synthesis_7084bca907043e3cba4afb7e"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 6 related objects found", "related:question_skill_compilation_boundary", "related:concept_real_robot_deployment_iteration_loop", "related:source_4bff03c9d5adb3463b34f947", "related:concept_dual_system_world_action_model", "related:concept_typed_verified_robot_skill_graph"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:33:12+08:00", "source:source_4bff03c9d5adb3463b34f947 work_sha256:none", "source:source_6b52a51e2b4a3be43c97c386 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "ac1925614d58ae6652df994544c68fea38f6af61b38fb22fa6abd16e09385758", "source_state_sha256": "915309bb9886ac06a5277ec293e3bae7d10828601e019c9c5b9e5d7a615e8651", "source_record_sha256s": {"source_4bff03c9d5adb3463b34f947": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "source_6b52a51e2b4a3be43c97c386": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e"}, "raw_state_sha256": "eebee2fdccd8e8bfd6c0dd3996aa640b99a319913465267c190d2877268d0ae9", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "12759a11724875b7e8f2b5e920a37c8b060332b38384d23b38f0761b35b812d0", "relation_fingerprint": {"outgoing_relations_sha256": "3bcf2ff87554c3acd4a4e04ebfd8b38992c0222578ae2a92826a4f05a5039984", "incoming_relations_sha256": "67173f1fbbbaa7bc9c749ee59e790c3b28b4b8178dffbc9b0e6dec9e80289f47", "full_neighborhood_sha256": "be03ee97e2d56a33ce5dc316ec0f185386537eb38a4ba4f2c54df6653ba2bf53"}, "relation_neighborhood_sha256": "be03ee97e2d56a33ce5dc316ec0f185386537eb38a4ba4f2c54df6653ba2bf53", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。", "changed_fields": [], "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386", "trigger_source": "source_6b52a51e2b4a3be43c97c386", "evidence_added": []}]
change_summary: "compile bundle from source_6b52a51e2b4a3be43c97c386"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_6b52a51e2b4a3be43c97c386",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。",
      "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。",
      "reason": "compile bundle from source_6b52a51e2b4a3be43c97c386",
      "trigger_source": "source_6b52a51e2b4a3be43c97c386"
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
        "searched title; 2 candidates inspected",
        "candidate:concept_asymmetric_frozen_vla_harness",
        "candidate:synthesis_7084bca907043e3cba4afb7e"
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
        "object_updated_at:2026-07-20T13:33:12+08:00",
        "source:source_4bff03c9d5adb3463b34f947 work_sha256:none",
        "source:source_6b52a51e2b4a3be43c97c386 work_sha256:none"
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
        "source:source_4bff03c9d5adb3463b34f947 record_sha256:a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a",
        "source:source_6b52a51e2b4a3be43c97c386 record_sha256:ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e"
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
        "source:source_4bff03c9d5adb3463b34f947 raw_sha256:b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349",
        "source:source_6b52a51e2b4a3be43c97c386 raw_sha256:89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d"
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
        "relation index inspected; 6 related objects found",
        "related:question_skill_compilation_boundary",
        "related:concept_real_robot_deployment_iteration_loop",
        "related:source_4bff03c9d5adb3463b34f947",
        "related:concept_dual_system_world_action_model",
        "related:concept_typed_verified_robot_skill_graph"
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
        "validated:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md"
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
  "completed_at": "2026-07-20T13:33:22+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "ac1925614d58ae6652df994544c68fea38f6af61b38fb22fa6abd16e09385758",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "eebee2fdccd8e8bfd6c0dd3996aa640b99a319913465267c190d2877268d0ae9",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "be03ee97e2d56a33ce5dc316ec0f185386537eb38a4ba4f2c54df6653ba2bf53",
      "incoming_relations_sha256": "67173f1fbbbaa7bc9c749ee59e790c3b28b4b8178dffbc9b0e6dec9e80289f47",
      "outgoing_relations_sha256": "3bcf2ff87554c3acd4a4e04ebfd8b38992c0222578ae2a92826a4f05a5039984"
    },
    "relation_neighborhood_sha256": "be03ee97e2d56a33ce5dc316ec0f185386537eb38a4ba4f2c54df6653ba2bf53",
    "source_record_sha256s": {
      "source_4bff03c9d5adb3463b34f947": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a",
      "source_6b52a51e2b4a3be43c97c386": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e"
    },
    "source_state_sha256": "915309bb9886ac06a5277ec293e3bae7d10828601e019c9c5b9e5d7a615e8651",
    "work_identity_sha256": "12759a11724875b7e8f2b5e920a37c8b060332b38384d23b38f0761b35b812d0"
  },
  "consolidation_id": "consolidation_66f163c772d6c3083fcff831",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:33:22+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_66f163c772d6c3083fcff831",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_asymmetric_frozen_vla_harness",
  "object_sha256_after": "ac1925614d58ae6652df994544c68fea38f6af61b38fb22fa6abd16e09385758",
  "object_sha256_before": "5b13ad62d9fa7bc3ab469258cf67184f2f66bd68dacf7da23eda3fd0651b0972",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_4bff03c9d5adb3463b34f947",
    "source_6b52a51e2b4a3be43c97c386"
  ],
  "source_records": [
    {
      "raw_content_sha256": "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349",
      "source_id": "source_4bff03c9d5adb3463b34f947",
      "source_record_sha256": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d",
      "source_id": "source_6b52a51e2b4a3be43c97c386",
      "source_record_sha256": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349",
    "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d"
  ],
  "started_at": "2026-07-20T13:33:22+08:00",
  "status": "complete",
  "title": "Consolidation: 冻结 VLA 的非对称技能编排",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:33:22+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
