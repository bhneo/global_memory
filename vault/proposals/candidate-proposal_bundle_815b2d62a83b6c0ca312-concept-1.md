---
id: "concept_latent_space_intervention_adaptation"
type: "concept"
status: "proposal"
title: "生成策略的潜空间干预适应"
created_at: "2026-07-19T12:19:04+08:00"
updated_at: "2026-07-20T11:56:10+08:00"
aliases: ["FlowDAgger", "latent-space intervention adaptation", "noise-space policy adaptation"]
tags: []
domains: ["embodied-ai", "vla", "human-in-the-loop", "generative-policy"]
confidence: "high"
source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
relations: [{"type": "derived_from", "target_id": "source_9a6e63428ed93e1a99ea4c4d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都冻结生成主干并增加轻量部署模块；动作评估蒸馏负责候选排序，潜空间干预适应则从人类纠正学习如何改变生成噪声。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都保留冻结 VLA 的已有能力；Harness VLA 在外部原语/规划层重组行为，FlowDAgger 在生成潜变量层内转向行为。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "该方法需要部署时捕获状态、人的纠正动作和对应策略执行，以形成可训练的干预对；可记录的真机迭代闭环是其数据入口。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_9a6e63428ed93e1a99ea4c4d"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_cd269bee56819aafec2fd5a3"], "importance": "weekly", "changed_belief": "人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。", "surprising": "人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger 风格干预能够训练潜空间控制器。", "connections": [{"shared_mechanism": "与 RL Token 都把大模型保持为稳定行为先验，只训练小型中间接口。", "boundary": "FlowDAgger 限于可执行动作反演的流匹配或扩散生成策略，并依赖人类在分布偏移处提供纠正。", "difference": "FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 actor-critic；两者的信息来源和安全成本不同。"}], "open_questions": ["动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？"]}
proposed_status: "working"
---

# 生成策略的潜空间干预适应

把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。
