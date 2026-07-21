---
id: "concept_09dc6e910b167ba474c89c38"
type: "concept"
status: "proposal"
title: "世界动作模型的激活空间鲁棒性 steering"
created_at: "2026-07-20T18:05:48+08:00"
updated_at: "2026-07-20T18:05:48+08:00"
aliases: ["World-Action Model Activation-Space Robustness Steering", "WA-LQR", "World-Action Linear Quadratic Regulator", "世界动作模型激活引导"]
tags: []
domains: ["world-model", "robot-robustness", "mechanistic-interpretability"]
confidence: "medium"
source_ids: ["source_38cba686373b003398483ab2"]
relations: [{"type": "derived_from", "target_id": "source_38cba686373b003398483ab2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "两者都在冻结基础策略的潜在表示层实施轻量干预，但一个由人类纠正动作导出输入潜变量，另一个由扰动对比激活和局部控制导出内部 steering。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_38cba686373b003398483ab2"
reflection_context: {"reflection_ids": ["reflection_f5a4802aeb05942de18022f0"], "importance": "high", "changed_belief": "此前训练后或提示级的鲁棒性改进常被看作统一手段；这里显示能否从激活中得到可迁移干预方向取决于具体架构和扰动。", "surprising": "", "connections": [{"shared_mechanism": "两者都先诊断内部表示中是否存在与目标行为相关的可用结构，再把诊断结果用于干预。", "boundary": "低维可分离只是在所测模型和扰动上的预测信号，不是因果解释或安全保证。", "difference": "表示对齐触觉 grounding 在训练期把未来接触结果监督到中间层；WAM steering 在不微调模型时，于推理期调节已存在的激活方向。"}], "open_questions": ["在新的相机、夹爪和视觉噪声组合上，线性可分性与闭环 steering 效果的相关性是否仍能校准？"]}
---

# 世界动作模型的激活空间鲁棒性 steering

对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。
