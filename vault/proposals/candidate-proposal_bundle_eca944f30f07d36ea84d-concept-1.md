---
id: "concept_dual_system_world_action_model"
type: "concept"
status: "proposal"
title: "双系统 World Action Model"
created_at: "2026-07-19T03:03:07+08:00"
updated_at: "2026-07-19T03:30:06+08:00"
aliases: ["dual-system world-action model", "DSWAM"]
tags: []
domains: ["embodied-ai", "world-action-model", "vla", "planning"]
confidence: "medium"
source_ids: ["source_ba057c2c11df2a5eba107870"]
relations: [{"type": "derived_from", "target_id": "source_ba057c2c11df2a5eba107870", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都将预测性世界表征接入动作系统，但 DSWAM 以 WAM 执行为默认路径。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两种架构都用双速或多速层级分离语义规划与动作执行。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "raises", "target_id": "tension_world_model_eval_action", "reason": "DSWAM 直接比较 WAM 与 VLA 执行路径，触及世界模型应作为评估器还是动作生成器的边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_ba057c2c11df2a5eba107870"
change_type: "metadata_only"
proposed_status: "working"
---

# 双系统 World Action Model

默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。
