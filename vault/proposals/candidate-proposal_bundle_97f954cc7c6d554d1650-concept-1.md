---
id: "concept_1920583cd9c7063491d45a40"
type: "concept"
status: "proposal"
title: "表示对齐的未来触觉 grounding"
created_at: "2026-07-20T18:05:58+08:00"
updated_at: "2026-07-20T18:05:58+08:00"
aliases: ["Representation-Aligned Future Tactile Grounding", "Latent Tactile Predictor", "LTP", "未来触觉表征对齐"]
tags: []
domains: ["embodied-ai", "tactile-manipulation", "vla"]
confidence: "medium"
source_ids: ["source_38651a884fe5c5c73a6e190d"]
relations: [{"type": "derived_from", "target_id": "source_38651a884fe5c5c73a6e190d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都把未来触觉作为控制相关目标，但前者在 VLA 的训练期选择内部 grounding 接口，后者在分层闭环中用触觉子目标与高频残差。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_38651a884fe5c5c73a6e190d"
reflection_context: {"reflection_ids": ["reflection_243a1a3f0cdc9450748cd215"], "importance": "high", "changed_belief": "此前触觉增强常被理解为增加输入模态或辅助损失；这里要求先验证内部接口与目标是否对齐，且多层广泛施加同一损失可能反而造成失配。", "surprising": "", "connections": [{"shared_mechanism": "两者都从动作条件的中间表示预测未来接触相关结果。", "boundary": "连接不表示生成触觉图像的跨传感器保真度已足以作为控制监督。", "difference": "VQ-Touch 面向传感器家族间的触觉图像生成；本文的 LTP 以未来紧凑触觉 latent 在策略内部约束接触控制表示。"}], "open_questions": ["在线传感器漂移或更换触觉皮肤后，如何重新验证被选中的 action-expert 接口仍是未来接触的最佳监督位置？"]}
---

# 表示对齐的未来触觉 grounding

在触觉增强 VLA 中，先以冻结 probe 比较各内部表示对未来触觉状态的可预测性，再将紧凑未来触觉 latent 的预测损失施加到最能表达动作条件接触动力学的中间 action-expert 接口；该训练期约束不同于直接预测噪声较大的原始触觉，也不同于在多个接口无差别叠加损失。
