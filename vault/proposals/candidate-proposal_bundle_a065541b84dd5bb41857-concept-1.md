---
id: "concept_dynamic_execution_horizon"
type: "concept"
status: "proposal"
title: "动态动作块执行时域"
created_at: "2026-07-19T12:18:42+08:00"
updated_at: "2026-07-19T12:18:42+08:00"
aliases: ["dynamic execution horizon", "Dynamic Execution Horizon Prediction", "DEHP"]
tags: []
domains: ["embodied-ai", "robot-control", "action-chunking", "reinforcement-learning"]
confidence: "medium"
source_ids: ["source_531bafa56ff63468797ac69e"]
relations: [{"type": "derived_from", "target_id": "source_531bafa56ff63468797ac69e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "part_of", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "动作块执行长度、重查询时机与时延补偿共同属于从策略预测到实际命令的部署调度层。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_cache_refinement", "reason": "两者都在不改生成主干的情况下优化动作块推理；缓存方法复用生成中间态，DEHP 调整已生成动作块的执行前缀。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_531bafa56ff63468797ac69e"
uncertainty: "受控实验主要使用 state-based Diffusion Policy；方法声称可黑盒扩展到图像策略，但该扩展尚未由本文实验证实，且能力上限仍由冻结基础策略决定。"
---

# 动态动作块执行时域

在保持动作块生成策略冻结的条件下，按当前观测和预测动作块动态决定执行多少步再重规划：自由空间运动使用较长前缀，精细对齐与接触阶段缩短前缀以提高反应性。
