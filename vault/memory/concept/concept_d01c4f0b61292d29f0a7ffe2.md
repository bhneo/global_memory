---
id: "concept_d01c4f0b61292d29f0a7ffe2"
type: "concept"
status: "working"
title: "动作块级策略优化与动态执行时域"
created_at: "2026-07-20T11:56:00+08:00"
updated_at: "2026-07-20T13:37:36+08:00"
aliases: ["PAC-ACT", "chunk-level PPO", "action-chunk policy optimization"]
tags: []
domains: ["embodied-ai", "robot-rl", "action-chunking", "contact-manipulation"]
confidence: "high"
source_ids: ["source_c79f943c818d06054ca5cf92"]
relations: [{"type": "derived_from", "target_id": "source_c79f943c818d06054ca5cf92", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}]
change_reason: "compile bundle from source_c79f943c818d06054ca5cf92"
reflection_context: {"reflection_ids": ["reflection_c0693ad0e6abf8397dbdfd87"], "importance": "weekly", "changed_belief": "动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。", "surprising": "在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。", "connections": [{"shared_mechanism": "与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。", "boundary": "PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。", "difference": "PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。"}], "open_questions": ["块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
consolidation_count: 2
last_consolidated_at: "2026-07-20T13:37:36+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_63cd1d4cd1ac5e4971d1"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_63cd1d4cd1ac5e4971d1-concept-1.md"
origin_candidate_sha256: "0abbeece325a6ec42b27fbeac3a8881574c4e7069a16d72fd7dbb027a8eae290"
memory_schema_version: 2
last_consolidation_id: "consolidation_b37a36ee83a614dec5a46304"
---

# 动作块级策略优化与动态执行时域

动作块级策略优化要求强化学习的决策、价值、优势和行为先验约束与动作块生成单位对齐；块长同时决定吞吐、时间连续性、信用分配跨度和异常后的纠正延迟，因此应被视为可按风险与阶段调整的控制时域。
