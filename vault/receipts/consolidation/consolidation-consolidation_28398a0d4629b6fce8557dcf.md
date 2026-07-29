---
id: "consolidation_28398a0d4629b6fce8557dcf"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 多时间尺度触觉世界模型控制"
created_at: "2026-07-28T16:32:20+08:00"
updated_at: "2026-07-28T16:32:20+08:00"
consolidation_id: "consolidation_28398a0d4629b6fce8557dcf"
object_id: "concept_multitimescale_tactile_world_model"
object_version_before: 1
object_sha256_before: "1936b7c0ff2bdd55d55fa666c70664b47fb81becad87173171368571908af158"
object_sha256_after: "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58"
source_ids: ["source_283911da72edc403d1b823fb", "source_c79f943c818d06054ca5cf92"]
source_sha256s: ["1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"]
source_records: [{"source_id": "source_283911da72edc403d1b823fb", "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "work_id": null, "work_document_sha256": null}, {"source_id": "source_c79f943c818d06054ca5cf92", "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc", "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-28T16:32:19+08:00"
completed_at: "2026-07-28T16:32:20+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_multitimescale_tactile_world_model.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "source:source_c79f943c818d06054ca5cf92 raw_sha256:17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "source:source_c79f943c818d06054ca5cf92 record_sha256:986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 4 candidates inspected", "candidate:concept_multitimescale_tactile_world_model", "candidate:reflection_4b63a8834e11b28db3cf2fdc", "candidate:reflection_dc321adda5d26fa9e6f71d5a", "candidate:reflection_e8e62c04da8ad9f420c37be4"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 14 related objects found", "related:source_283911da72edc403d1b823fb", "related:concept_predictive_vla_deployment", "related:concept_d01c4f0b61292d29f0a7ffe2", "related:concept_vla_action_cache_refinement", "related:concept_world_model_evaluation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-28T16:32:03+08:00", "source:source_283911da72edc403d1b823fb work_sha256:none", "source:source_c79f943c818d06054ca5cf92 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58", "source_state_sha256": "266616e2c158263659edfa5265a37f0d341ffbecea2f46efd4f755d9532b4d5b", "source_record_sha256s": {"source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"}, "raw_state_sha256": "a6d3c04f17215cd49c8e8477f8f087d15f2c2ffe1871d3e382acfc828af4cc65", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "53d5c6138d51df85b287e305967a17ff8fd1d14620b540bd584fd59971fa06e6", "relation_fingerprint": {"outgoing_relations_sha256": "5f654e392914acc5415e211245e3458fb9f35cc8f4db4122aaac24b313388fdf", "incoming_relations_sha256": "ea7b58a108b63faa978308b03fc8381bf04b1a199df686a9284f05b69dc5176a", "full_neighborhood_sha256": "7d118dc31a8af6c182446d095eb383835f837d475c3f5144dfdeeed609067bdd"}, "relation_neighborhood_sha256": "7d118dc31a8af6c182446d095eb383835f837d475c3f5144dfdeeed609067bdd", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。\n\n## 新增来源材料\n\n- `source_c79f943c818d06054ca5cf92`：多时间尺度触觉世界模型需要同时声明各层的决策单位、信息新鲜度和升级条件。慢速语义层提出子任务，预测层形成触觉子目标，中频策略以动作块作为生成与信用分配单位，高频触觉残差处理局部接触偏差；缓存的中间动作只可在任务阶段、机器人状态和 refinement 不确定性共同通过门禁时作为暖启动。块长、缓存命中和残差幅度达到阈值时应触发拒绝复用或高层重规划，而不是继续由快环无限吸收。", "changed_fields": [], "reason": "compile bundle from source_c79f943c818d06054ca5cf92", "trigger_source": "source_c79f943c818d06054ca5cf92", "evidence_added": []}]
change_summary: "compile bundle from source_c79f943c818d06054ca5cf92"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_c79f943c818d06054ca5cf92",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。\n\n## 新增来源材料\n\n- `source_c79f943c818d06054ca5cf92`：多时间尺度触觉世界模型需要同时声明各层的决策单位、信息新鲜度和升级条件。慢速语义层提出子任务，预测层形成触觉子目标，中频策略以动作块作为生成与信用分配单位，高频触觉残差处理局部接触偏差；缓存的中间动作只可在任务阶段、机器人状态和 refinement 不确定性共同通过门禁时作为暖启动。块长、缓存命中和残差幅度达到阈值时应触发拒绝复用或高层重规划，而不是继续由快环无限吸收。",
      "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。",
      "reason": "compile bundle from source_c79f943c818d06054ca5cf92",
      "trigger_source": "source_c79f943c818d06054ca5cf92"
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
        "searched title; 4 candidates inspected",
        "candidate:concept_multitimescale_tactile_world_model",
        "candidate:reflection_4b63a8834e11b28db3cf2fdc",
        "candidate:reflection_dc321adda5d26fa9e6f71d5a",
        "candidate:reflection_e8e62c04da8ad9f420c37be4"
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
        "object_updated_at:2026-07-28T16:32:03+08:00",
        "source:source_283911da72edc403d1b823fb work_sha256:none",
        "source:source_c79f943c818d06054ca5cf92 work_sha256:none"
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
        "source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
        "source:source_c79f943c818d06054ca5cf92 record_sha256:986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"
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
        "source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
        "source:source_c79f943c818d06054ca5cf92 raw_sha256:17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
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
        "relation index inspected; 14 related objects found",
        "related:source_283911da72edc403d1b823fb",
        "related:concept_predictive_vla_deployment",
        "related:concept_d01c4f0b61292d29f0a7ffe2",
        "related:concept_vla_action_cache_refinement",
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
        "validated:vault/memory/concept/concept_multitimescale_tactile_world_model.md"
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
  "completed_at": "2026-07-28T16:32:20+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a6d3c04f17215cd49c8e8477f8f087d15f2c2ffe1871d3e382acfc828af4cc65",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "7d118dc31a8af6c182446d095eb383835f837d475c3f5144dfdeeed609067bdd",
      "incoming_relations_sha256": "ea7b58a108b63faa978308b03fc8381bf04b1a199df686a9284f05b69dc5176a",
      "outgoing_relations_sha256": "5f654e392914acc5415e211245e3458fb9f35cc8f4db4122aaac24b313388fdf"
    },
    "relation_neighborhood_sha256": "7d118dc31a8af6c182446d095eb383835f837d475c3f5144dfdeeed609067bdd",
    "source_record_sha256s": {
      "source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
      "source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"
    },
    "source_state_sha256": "266616e2c158263659edfa5265a37f0d341ffbecea2f46efd4f755d9532b4d5b",
    "work_identity_sha256": "53d5c6138d51df85b287e305967a17ff8fd1d14620b540bd584fd59971fa06e6"
  },
  "consolidation_id": "consolidation_28398a0d4629b6fce8557dcf",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-28T16:32:20+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_28398a0d4629b6fce8557dcf",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_multitimescale_tactile_world_model",
  "object_sha256_after": "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58",
  "object_sha256_before": "1936b7c0ff2bdd55d55fa666c70664b47fb81becad87173171368571908af158",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_283911da72edc403d1b823fb",
    "source_c79f943c818d06054ca5cf92"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
      "source_id": "source_283911da72edc403d1b823fb",
      "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb",
      "source_id": "source_c79f943c818d06054ca5cf92",
      "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
    "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
  ],
  "started_at": "2026-07-28T16:32:19+08:00",
  "status": "complete",
  "title": "Consolidation: 多时间尺度触觉世界模型控制",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-28T16:32:20+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
