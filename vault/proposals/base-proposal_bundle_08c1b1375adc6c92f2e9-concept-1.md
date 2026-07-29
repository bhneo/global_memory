---
id: "concept_relation_triggered_process_safety"
type: "concept"
status: "working"
title: "关系触发的具身过程安全"
created_at: "2026-07-21T17:42:01+08:00"
updated_at: "2026-07-21T17:42:02+08:00"
aliases: ["Relation-Triggered Embodied Process Safety", "SafeRelBench", "Spatial-Relation-Aware Process Safety", "空间关系过程安全"]
tags: []
domains: ["embodied-ai", "robot-safety", "spatial-reasoning"]
confidence: "medium"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都要求在动作执行前检查类型化前置条件；该基准提供过程安全评测，而技能图提供执行结构。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}]
change_reason: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
reflection_context: {"reflection_ids": ["reflection_ee2dc3e5679d14ca67d9f5df"], "importance": "high", "changed_belief": "完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。", "surprising": "七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。", "connections": [{"shared_mechanism": "都用类型化前置条件约束动作序列。", "boundary": "基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。", "difference": "类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。"}], "open_questions": ["关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56sol-readmission-v1"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56sol-readmission-v1"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_3d280267fd5befffee7d"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_3d280267fd5befffee7d-concept-1.md"
origin_candidate_sha256: "64f1d6e27809397688bd00a33be5810f286e16e371c88a8bc1c55b6401f8defe"
memory_schema_version: 2
---

# 关系触发的具身过程安全

将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。
