---
id: "concept_latent_space_intervention_adaptation"
type: "concept"
status: "proposal"
title: "生成策略的潜空间干预适应"
created_at: "2026-07-19T12:19:04+08:00"
updated_at: "2026-07-19T12:19:04+08:00"
aliases: ["latent-space intervention adaptation", "noise-space policy adaptation", "FlowDAgger"]
tags: []
domains: ["embodied-ai", "robot-learning", "human-in-the-loop", "generative-policy"]
confidence: "medium"
source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
relations: [{"type": "derived_from", "target_id": "source_9a6e63428ed93e1a99ea4c4d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都冻结生成主干并增加轻量部署模块；动作评估蒸馏负责候选排序，潜空间干预适应则从人类纠正学习如何改变生成噪声。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都保留冻结 VLA 的已有能力；Harness VLA 在外部原语/规划层重组行为，FlowDAgger 在生成潜变量层内转向行为。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "该方法需要部署时捕获状态、人的纠正动作和对应策略执行，以形成可训练的干预对；可记录的真机迭代闭环是其数据入口。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_9a6e63428ed93e1a99ea4c4d"
uncertainty: "适应能力受基础策略动作流形支持范围约束，并依赖人类干预的覆盖与一致性；高度多模态或病态生成动力学会降低反演保真度。"
---

# 生成策略的潜空间干预适应

把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。
