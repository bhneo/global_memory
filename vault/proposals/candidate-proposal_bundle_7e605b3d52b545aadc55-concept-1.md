---
id: "concept_predictive_vla_deployment"
type: "concept"
status: "proposal"
title: "面向真实部署的预测式 VLA"
created_at: "2026-07-19T02:52:30+08:00"
updated_at: "2026-07-19T02:52:30+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "world-model", "robot-learning"]
confidence: "medium"
source_ids: ["source_233c4bef3a727389ddf81ae2"]
relations: [{"type": "derived_from", "target_id": "source_233c4bef3a727389ddf81ae2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都利用对未来状态或结果的预测，但这里预测被用作 VLA 训练目标而不只是离线评测器。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_embodied_data_loop", "reason": "该方案把跨本体数据规模、动作空间覆盖和预测训练目标共同视为部署能力来源。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
change_reason: "compile bundle from source_233c4bef3a727389ddf81ae2"
uncertainty: "未来预测在该工作中是代理训练目标，不等同于完整的环境动力学世界模型。"
---

# 面向真实部署的预测式 VLA

在 VLA 的视觉—语言—动作映射中加入未来状态或动作后果预测，使策略不仅响应当前观测，还能以语义和几何线索形成面向动态环境的预测表示。
