---
id: "consolidation_17d11399e9ea3f4ae47dc1bf"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 冻结 VLA 的非对称技能编排"
created_at: "2026-08-02T19:27:19+08:00"
updated_at: "2026-08-02T19:27:19+08:00"
consolidation_id: "consolidation_17d11399e9ea3f4ae47dc1bf"
object_id: "concept_asymmetric_frozen_vla_harness"
object_version_before: 1
object_sha256_before: "ff04aac24933c2e22f6e5cc901d5c72591f02cfd010f7b0884a22e7cc1fbb866"
object_sha256_after: "37eb693fe3eb7b2d2bee3db688f1048bf7ca448330deb3bdcb7c358d4d7a0d29"
source_ids: ["source_4bff03c9d5adb3463b34f947", "source_6b52a51e2b4a3be43c97c386", "source_cc2f2812863ca6751c223b54", "source_40700e61702f4b5a5765e11d", "source_ddd2f65020c2e556f2b93330"]
source_sha256s: ["b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d", "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f", "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b", "add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879"]
source_records: [{"source_id": "source_4bff03c9d5adb3463b34f947", "source_record_sha256": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "raw_content_sha256": "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "work_id": null, "work_document_sha256": null}, {"source_id": "source_6b52a51e2b4a3be43c97c386", "source_record_sha256": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e", "raw_content_sha256": "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d", "work_id": null, "work_document_sha256": null}, {"source_id": "source_cc2f2812863ca6751c223b54", "source_record_sha256": "9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197", "raw_content_sha256": "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f", "work_id": null, "work_document_sha256": null}, {"source_id": "source_40700e61702f4b5a5765e11d", "source_record_sha256": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9", "raw_content_sha256": "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b", "work_id": null, "work_document_sha256": null}, {"source_id": "source_ddd2f65020c2e556f2b93330", "source_record_sha256": "3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c", "raw_content_sha256": "add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:27:18+08:00"
completed_at: "2026-08-02T19:27:19+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_asymmetric_frozen_vla_harness.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4bff03c9d5adb3463b34f947 raw_sha256:b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349", "source:source_6b52a51e2b4a3be43c97c386 raw_sha256:89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d", "source:source_cc2f2812863ca6751c223b54 raw_sha256:5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f", "source:source_40700e61702f4b5a5765e11d raw_sha256:a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b", "source:source_ddd2f65020c2e556f2b93330 raw_sha256:add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4bff03c9d5adb3463b34f947 record_sha256:a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "source:source_6b52a51e2b4a3be43c97c386 record_sha256:ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e", "source:source_cc2f2812863ca6751c223b54 record_sha256:9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197", "source:source_40700e61702f4b5a5765e11d record_sha256:67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9", "source:source_ddd2f65020c2e556f2b93330 record_sha256:3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_asymmetric_frozen_vla_harness"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 15 related objects found", "related:question_skill_compilation_boundary", "related:concept_real_robot_deployment_iteration_loop", "related:source_4bff03c9d5adb3463b34f947", "related:concept_2db7edf95d63ca80702f042e", "related:concept_3b83de1641240159d66c23d4"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T19:26:57+08:00", "source:source_4bff03c9d5adb3463b34f947 work_sha256:none", "source:source_6b52a51e2b4a3be43c97c386 work_sha256:none", "source:source_cc2f2812863ca6751c223b54 work_sha256:none", "source:source_40700e61702f4b5a5765e11d work_sha256:none", "source:source_ddd2f65020c2e556f2b93330 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:5", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "37eb693fe3eb7b2d2bee3db688f1048bf7ca448330deb3bdcb7c358d4d7a0d29", "source_state_sha256": "93538c461149f21fc7a36f8fb94f634846887b8c5cc423c894cb2e1197c9d707", "source_record_sha256s": {"source_4bff03c9d5adb3463b34f947": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a", "source_6b52a51e2b4a3be43c97c386": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e", "source_cc2f2812863ca6751c223b54": "9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197", "source_40700e61702f4b5a5765e11d": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9", "source_ddd2f65020c2e556f2b93330": "3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c"}, "raw_state_sha256": "ba5b726f050bc771b0206a9a6af7835e12267f4b5bd4f7d2ace6f22ed9877511", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "5bd8526bb450c446c953267ee34a178c704243b152a1fdd18c01ea7956e04dad", "relation_fingerprint": {"outgoing_relations_sha256": "4c7925dc3380f59c5247694b6e618f3a9a892f8448152673c8bfc3e4010e89a1", "incoming_relations_sha256": "dd3c1b5b07ba2c492da2e07d4b27ba46e01849f69ab084e1e65fbb0c486cae36", "full_neighborhood_sha256": "4c567a89a8a7bd77944c0bd5489fdb82008d08d4c7809a1a57fe2a8834f531bb"}, "relation_neighborhood_sha256": "4c567a89a8a7bd77944c0bd5489fdb82008d08d4c7809a1a57fe2a8834f531bb", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。", "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。\n\n## 新增来源材料\n\n- `source_ddd2f65020c2e556f2b93330`：ROBOBRIDGE 为基础策略外部的编排边界补充一个控制器无关的五模块运行时：Perceptor 维护对象中心状态，Planner 生成参数化 primitive，Controller 可替换为 VLA、微调适配器或 IK，Robot Interface 吸收具身 API、坐标变换与安全约束，Monitor 则把周期性轻量成功检查与失败诊断分成两阶段。高置信失败先停止机器人，再按重试、重生成轨迹、基于最新异步感知重规划、重新感知后重规划的最小代价顺序升级；primitive 后若对象集合或三维位置超过偏离阈值，则保留高层动作序列并只刷新当前及后续 primitive 参数。该增量支持“能力有界策略加外部恢复外壳”，但不证明基础 VLA 得到提升：RoboCasa 绝对成功率仍低且存在零结果与退化任务，阈值和规则主要手工设定，遮挡、相似物体、接触丰富或不可逆失败仍可能超出恢复范围，论文也未给出定量真实机器人成功率表。", "changed_fields": [], "reason": "compile bundle from source_ddd2f65020c2e556f2b93330", "trigger_source": "source_ddd2f65020c2e556f2b93330", "evidence_added": []}]
change_summary: "compile bundle from source_ddd2f65020c2e556f2b93330"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_ddd2f65020c2e556f2b93330",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。\n\n## 新增来源材料\n\n- `source_ddd2f65020c2e556f2b93330`：ROBOBRIDGE 为基础策略外部的编排边界补充一个控制器无关的五模块运行时：Perceptor 维护对象中心状态，Planner 生成参数化 primitive，Controller 可替换为 VLA、微调适配器或 IK，Robot Interface 吸收具身 API、坐标变换与安全约束，Monitor 则把周期性轻量成功检查与失败诊断分成两阶段。高置信失败先停止机器人，再按重试、重生成轨迹、基于最新异步感知重规划、重新感知后重规划的最小代价顺序升级；primitive 后若对象集合或三维位置超过偏离阈值，则保留高层动作序列并只刷新当前及后续 primitive 参数。该增量支持“能力有界策略加外部恢复外壳”，但不证明基础 VLA 得到提升：RoboCasa 绝对成功率仍低且存在零结果与退化任务，阈值和规则主要手工设定，遮挡、相似物体、接触丰富或不可逆失败仍可能超出恢复范围，论文也未给出定量真实机器人成功率表。",
      "previous_statement": "# 冻结 VLA 的非对称技能编排\n\n把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。\n\n## 新增来源材料\n\n- `source_6b52a51e2b4a3be43c97c386`：RPent 的服务化物理 Agent 外壳把感知、推理、记忆、执行与再观察显式分开，使冻结 VLA 的失败可由上层状态定位、重试和恢复；该增量属于基础设施与记忆闭环，不能等同于底层 VLA 能力提升。\n\n## 新增来源材料\n\n- `source_cc2f2812863ca6751c223b54`：把冻结 VLA 和其他异构策略限定为能力有界的局部专家；高层代理负责分解、路由和恢复，但每次策略切换前还必须用执行记忆估计当前状态与 incoming policy 支持域的兼容性，并在必要时生成受硬安全权限约束的桥接轨迹。正确的技能选择不能替代交接状态验证，稀疏历史也不能证明能力边界。\n\n## 新增来源材料\n\n- `source_40700e61702f4b5a5765e11d`：冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。",
      "reason": "compile bundle from source_ddd2f65020c2e556f2b93330",
      "trigger_source": "source_ddd2f65020c2e556f2b93330"
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
        "candidate:concept_asymmetric_frozen_vla_harness"
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
        "object_updated_at:2026-08-02T19:26:57+08:00",
        "source:source_4bff03c9d5adb3463b34f947 work_sha256:none",
        "source:source_6b52a51e2b4a3be43c97c386 work_sha256:none",
        "source:source_cc2f2812863ca6751c223b54 work_sha256:none",
        "source:source_40700e61702f4b5a5765e11d work_sha256:none",
        "source:source_ddd2f65020c2e556f2b93330 work_sha256:none"
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
        "source:source_6b52a51e2b4a3be43c97c386 record_sha256:ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e",
        "source:source_cc2f2812863ca6751c223b54 record_sha256:9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197",
        "source:source_40700e61702f4b5a5765e11d record_sha256:67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9",
        "source:source_ddd2f65020c2e556f2b93330 record_sha256:3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c"
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
        "source:source_6b52a51e2b4a3be43c97c386 raw_sha256:89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d",
        "source:source_cc2f2812863ca6751c223b54 raw_sha256:5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f",
        "source:source_40700e61702f4b5a5765e11d raw_sha256:a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b",
        "source:source_ddd2f65020c2e556f2b93330 raw_sha256:add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879"
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
        "relation index inspected; 15 related objects found",
        "related:question_skill_compilation_boundary",
        "related:concept_real_robot_deployment_iteration_loop",
        "related:source_4bff03c9d5adb3463b34f947",
        "related:concept_2db7edf95d63ca80702f042e",
        "related:concept_3b83de1641240159d66c23d4"
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
        "distinct_source_ids:5",
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
  "completed_at": "2026-08-02T19:27:19+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "37eb693fe3eb7b2d2bee3db688f1048bf7ca448330deb3bdcb7c358d4d7a0d29",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "ba5b726f050bc771b0206a9a6af7835e12267f4b5bd4f7d2ace6f22ed9877511",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "4c567a89a8a7bd77944c0bd5489fdb82008d08d4c7809a1a57fe2a8834f531bb",
      "incoming_relations_sha256": "dd3c1b5b07ba2c492da2e07d4b27ba46e01849f69ab084e1e65fbb0c486cae36",
      "outgoing_relations_sha256": "4c7925dc3380f59c5247694b6e618f3a9a892f8448152673c8bfc3e4010e89a1"
    },
    "relation_neighborhood_sha256": "4c567a89a8a7bd77944c0bd5489fdb82008d08d4c7809a1a57fe2a8834f531bb",
    "source_record_sha256s": {
      "source_40700e61702f4b5a5765e11d": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9",
      "source_4bff03c9d5adb3463b34f947": "a6a7780edc86abfdd70332084818ef621b983c04e50dbc62556ef48efcb0171a",
      "source_6b52a51e2b4a3be43c97c386": "ee394e8f21ca9a72da08aeb0be8bf02ce88a14dbaa5c3a80b24ba6fee25cc84e",
      "source_cc2f2812863ca6751c223b54": "9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197",
      "source_ddd2f65020c2e556f2b93330": "3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c"
    },
    "source_state_sha256": "93538c461149f21fc7a36f8fb94f634846887b8c5cc423c894cb2e1197c9d707",
    "work_identity_sha256": "5bd8526bb450c446c953267ee34a178c704243b152a1fdd18c01ea7956e04dad"
  },
  "consolidation_id": "consolidation_17d11399e9ea3f4ae47dc1bf",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:27:19+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_17d11399e9ea3f4ae47dc1bf",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_asymmetric_frozen_vla_harness",
  "object_sha256_after": "37eb693fe3eb7b2d2bee3db688f1048bf7ca448330deb3bdcb7c358d4d7a0d29",
  "object_sha256_before": "ff04aac24933c2e22f6e5cc901d5c72591f02cfd010f7b0884a22e7cc1fbb866",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_4bff03c9d5adb3463b34f947",
    "source_6b52a51e2b4a3be43c97c386",
    "source_cc2f2812863ca6751c223b54",
    "source_40700e61702f4b5a5765e11d",
    "source_ddd2f65020c2e556f2b93330"
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
    },
    {
      "raw_content_sha256": "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f",
      "source_id": "source_cc2f2812863ca6751c223b54",
      "source_record_sha256": "9117b333de8370e1e1f07072a372192c870c8436585d3e0d117992425c515197",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b",
      "source_id": "source_40700e61702f4b5a5765e11d",
      "source_record_sha256": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879",
      "source_id": "source_ddd2f65020c2e556f2b93330",
      "source_record_sha256": "3bab0e3fa6e2d667ba1c55aa06c5de940fb0d4a3e7b37925cdb87928723e002c",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "b3f2fe99270f794905525580aa25e37e039eec18e7095aa1c7d0049b42757349",
    "89b60670c1fcc0745ca8b9c37c044c7d98f5e0d731344e2aacfbb21a4bd2ae0d",
    "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f",
    "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b",
    "add5e30c5670b66ac3b696a50a39d6ae8989c46feb119f522dc8c97596d29879"
  ],
  "started_at": "2026-08-02T19:27:18+08:00",
  "status": "complete",
  "title": "Consolidation: 冻结 VLA 的非对称技能编排",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:27:19+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
