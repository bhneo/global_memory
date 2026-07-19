---
id: "concept_vla_action_evaluation_distillation"
type: "concept"
status: "proposal"
title: "VLA 动作评估蒸馏"
created_at: "2026-07-19T03:03:50+08:00"
updated_at: "2026-07-19T03:26:34+08:00"
aliases: ["VLA action evaluation distillation", "action value distillation", "SVA"]
tags: []
domains: ["embodied-ai", "vla", "reinforcement-learning", "planning", "value-function"]
confidence: "medium"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_world_model_action_value", "reason": "该方法用仿真回报蒸馏出的动作价值模型把长期后果预测连接到动作选择。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都关注预测结果对策略评价的价值，但这里评价对象是冻结 VLA 产生的候选动作。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "评估器与生成器解耦，目标是在不后训练 VLA 主干的情况下保留通用能力。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
change_type: "metadata_only"
proposed_status: "working"
---

# VLA 动作评估蒸馏

保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。
