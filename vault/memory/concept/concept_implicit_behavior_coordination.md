---
id: "concept_implicit_behavior_coordination"
type: "concept"
status: "working"
title: "隐式行为协调"
created_at: "2026-07-19T02:51:51+08:00"
updated_at: "2026-07-19T03:06:00+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "imitation-learning", "reinforcement-learning", "long-horizon-control"]
confidence: "medium"
source_ids: ["source_8aa5e06bac422cb3319b94e6"]
relations: [{"type": "derived_from", "target_id": "source_8aa5e06bac422cb3319b94e6", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_skill_evolution", "reason": "两者都处理可复用行为的形成与选择，但隐式行为协调不要求显式技能对象。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该工作提供一个反例：部分长时程任务可以不先把行为固化为显式技能再协调。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}]
change_reason: "compile bundle from source_8aa5e06bac422cb3319b94e6"
uncertainty: "证据来自 Habitat rearrangement 设置，不能推出所有长时程机器人任务都不需要显式技能。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56terra-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56terra-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:06:00+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_a6bbdedf11bb9aae0b7e"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_a6bbdedf11bb9aae0b7e-concept-1.md"
origin_candidate_sha256: "335da603c999232e4a94f5fd0f4395e0ca61871dbec44ab66473e0a28d9650ba"
memory_schema_version: 2
last_consolidation_id: "consolidation_8659bd63c330c2c1c5c860f4"
---

# 隐式行为协调

从未标注的子任务示范中学习多模态候选动作块，再由价值函数按当前状态和任务目标选择候选，从而避免显式技能标签、边界和固定切换逻辑。
