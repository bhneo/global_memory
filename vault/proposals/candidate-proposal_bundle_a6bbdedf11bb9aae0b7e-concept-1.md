---
id: "concept_implicit_behavior_coordination"
type: "concept"
status: "proposal"
title: "隐式行为协调"
created_at: "2026-07-19T02:51:51+08:00"
updated_at: "2026-07-19T02:51:51+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "imitation-learning", "reinforcement-learning", "long-horizon-control"]
confidence: "medium"
source_ids: ["source_8aa5e06bac422cb3319b94e6"]
relations: [{"type": "derived_from", "target_id": "source_8aa5e06bac422cb3319b94e6", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_skill_evolution", "reason": "两者都处理可复用行为的形成与选择，但隐式行为协调不要求显式技能对象。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该工作提供一个反例：部分长时程任务可以不先把行为固化为显式技能再协调。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
change_reason: "compile bundle from source_8aa5e06bac422cb3319b94e6"
uncertainty: "证据来自 Habitat rearrangement 设置，不能推出所有长时程机器人任务都不需要显式技能。"
---

# 隐式行为协调

从未标注的子任务示范中学习多模态候选动作块，再由价值函数按当前状态和任务目标选择候选，从而避免显式技能标签、边界和固定切换逻辑。
