---
id: "concept_dual_timescale_lifelong_vla_adaptation"
type: "concept"
status: "working"
title: "双时间尺度的持续 VLA 适配"
created_at: "2026-07-21T17:44:57+08:00"
updated_at: "2026-07-26T12:33:48+08:00"
aliases: ["Dual-Timescale Lifelong VLA Adaptation", "LifelongVLA", "Continual VLA Learning", "持续视觉语言动作学习"]
tags: []
domains: ["embodied-ai", "vla", "continual-learning"]
confidence: "medium"
source_ids: ["source_04477c8679bc779d8389a22e"]
relations: [{"type": "derived_from", "target_id": "source_04477c8679bc779d8389a22e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_skill_evolution", "reason": "两者都处理能力随经验累积的稳定更新，但一个发生在模型 adapter 内部，另一个强调外部技能工件与验证。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}]
change_reason: "compile bundle from source_04477c8679bc779d8389a22e"
reflection_context: {"reflection_ids": ["reflection_eca8957906652e0850a7f644"], "importance": "high", "changed_belief": "持续 VLA 的关键接口不仅是保留多少数据，还包括哪些参数承担短期变化、何时合并到长期路径以及任务身份如何被识别。", "surprising": "作者报告相对基线成功率提升超过 13%、遗忘率降低超过 8.2%，真机任务均超过 80%；这些结论仍局限于其增量任务顺序和已知任务门控设置。", "connections": [{"shared_mechanism": "都把经验分成快速适应与稳定保留的不同时间尺度。", "boundary": "LoRA 门控的参数稳定性不等于跨形态技能语义已被正确迁移。", "difference": "技能进化强调外部技能版本和验证；LifelongVLA 在模型参数内部通过双 LoRA 路径和缓存 replay 管理遗忘。"}], "open_questions": ["未知任务边界、相似技能冲突和长序列任务到来时，门控是否仍能正确分配短长期适配？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56sol-readmission-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56sol-readmission-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:48+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_51f63c2258baa5472e5f"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_51f63c2258baa5472e5f-concept-1.md"
origin_candidate_sha256: "d111bf1f3c31501e1d7246cfbb7d4213e94c6ed969b209d2929c6c8f2a3b5eb7"
memory_schema_version: 2
last_consolidation_id: "consolidation_5e59510cd2bd78422910995f"
---

# 双时间尺度的持续 VLA 适配

LifelongVLA 用短期 LoRA adapter 支持新任务可塑性、长期 LoRA adapter 保存稳定能力，并通过任务感知 gate 组合两条路径；缓存高效的随机 replay 在不保留完整轨迹的情况下提供旧技能信号。该机制显式处理 plasticity–stability trade-off，但依赖任务识别、缓存代表性和有限任务序列上的实验验证。
