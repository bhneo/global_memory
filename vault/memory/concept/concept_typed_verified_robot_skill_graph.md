---
id: "concept_typed_verified_robot_skill_graph"
type: "concept"
status: "working"
title: "类型化可验证机器人技能图"
created_at: "2026-07-19T12:18:22+08:00"
updated_at: "2026-07-19T23:49:56+08:00"
aliases: ["typed verified robot skill graph", "Graph-as-Policy", "GaP"]
tags: []
domains: ["embodied-ai", "robotics", "skill-graphs", "agent-execution"]
confidence: "medium"
source_ids: ["source_6fb6f0a30a013fd1ada42b57"]
relations: [{"type": "derived_from", "target_id": "source_6fb6f0a30a013fd1ada42b57", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_skill_evolution", "reason": "GaP 为可审计技能沉淀补充了显式 workflow schema、验证、checkpoint、recovery 和 sim-to-hardware 执行边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该项目给出一种可操作答案：当任务需要跨变化实例持久复用且能通过技能契约和验证门控检查时，可把语言规划固化为外部图。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_adaptive_interleaved_multimodal_planning", "reason": "APIVOT 在模型内部生成视觉未来状态，GaP 把任务结构外化为可执行图；两者分别覆盖内部几何推理与外部可审计执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "tension_internal_reasoning_external_skills", "reason": "GaP 明确选择外部类型化技能与图执行，构成该 tension 的外部可审计一侧。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_6fb6f0a30a013fd1ada42b57"
uncertainty: "来源是 beta 代码仓库说明，API、workflow schema 与 skill interfaces 明示可能变化；项目示例不能替代独立成功率复核。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-19T23:49:56+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_b5617e688da75d78abd3"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b5617e688da75d78abd3-concept-1.md"
origin_candidate_sha256: "ec5963e7c2ed2938187356345abefa3d22b57b44cd0d654d4777b1eb9a3d0c0c"
memory_schema_version: 2
last_consolidation_id: "consolidation_ee18a23eca0800db5622215b"
---

# 类型化可验证机器人技能图

把自然语言任务编译为带类型、检查点和恢复语义的模块化技能计算图，在仿真中验证与改进后执行该图本身，使跨对象几何和姿态变化的持续任务保留可审计控制结构。
