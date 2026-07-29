---
id: "concept_test_time_fast_weight_robot_memory"
type: "concept"
status: "working"
title: "机器人策略的测试时快速权重记忆"
created_at: "2026-07-21T17:41:51+08:00"
updated_at: "2026-07-26T12:34:01+08:00"
aliases: ["Test-Time Fast-Weight Memory for Robot Policies", "RoboTTT", "TTT Robot Policy", "测试时训练机器人策略"]
tags: []
domains: ["embodied-ai", "test-time-training", "long-horizon-manipulation"]
confidence: "medium"
source_ids: ["source_79475aef7849b08664b51a4e"]
relations: [{"type": "derived_from", "target_id": "source_79475aef7849b08664b51a4e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_native_action_aligned_vla_memory", "reason": "两者分别以快速权重和显式原生 token 承载长时历史，形成可比较的记忆接口。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}]
change_reason: "compile bundle from source_79475aef7849b08664b51a4e"
reflection_context: {"reflection_ids": ["reflection_245f74ef295bd04767608b26"], "importance": "high", "changed_belief": "长上下文能力既可通过显式记忆 token 实现，也可通过参数化快速状态实现；两者在可解释性、遗忘和计算成本上有不同风险。", "surprising": "在三项双臂装配任务中作者报告平均完成分 79%，高于单步 GR00T N1.7 的 42% 和 GDN 的 56%；训练使用 16 张 GB200，长上下文收益伴随显著训练成本。", "connections": [{"shared_mechanism": "都保留分钟级历史以改进后续动作。", "boundary": "fast-weight 适应不等于持久跨会话记忆，也不自动保证纠正方向安全。", "difference": "NativeMEM 显式保存动作对齐视觉 token；RoboTTT 通过测试时梯度更新把上下文折叠进快速权重。"}], "open_questions": ["fast weights 遇到错误动作、自生成偏差或任务切换时如何检测并回滚？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56sol-readmission-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56sol-readmission-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:34:01+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0e008d1244eaa3da0c29"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0e008d1244eaa3da0c29-concept-1.md"
origin_candidate_sha256: "0d58a76fa115821d743ca710a4c06dbad4cec0fe79a80619a20b8562ccd913ec"
memory_schema_version: 2
last_consolidation_id: "consolidation_4d4898aea1e942528a0279a0"
---

# 机器人策略的测试时快速权重记忆

RoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮。它把分钟级历史压入参数化在线状态，但需要额外训练计算，并面临错误历史污染、遗忘、回滚和任务切换边界。
