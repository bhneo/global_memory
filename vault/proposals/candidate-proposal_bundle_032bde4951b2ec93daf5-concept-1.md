---
id: "concept_a13a20254f749ae9c5484c6b"
type: "concept"
status: "proposal"
title: "生成器状态监督的当前态预测控制接口 / Current-only predictive control interface supervised by generator states"
created_at: "2026-08-01T18:22:35+08:00"
updated_at: "2026-08-01T18:22:35+08:00"
aliases: ["Enfold", "generator-to-representation learning", "G2R predictive representation", "生成器中间状态蒸馏控制表征"]
tags: []
domains: ["robotics", "world-models", "predictive-representation", "vision-language-action"]
confidence: "high"
source_ids: ["source_029a4fa602a118a1ead1bbf4"]
relations: [{"type": "derived_from", "target_id": "source_029a4fa602a118a1ead1bbf4", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "Enfold 用生成质量、控制读出和干预案例分别测试 representation；这落实了世界模型必须用动作、规划和失败恢复而非仅视频相似度评价的原则。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_029a4fa602a118a1ead1bbf4"
reflection_context: {"reflection_ids": ["reflection_964f606aa97843d429045b0b"], "importance": "high", "changed_belief": "此前容易把世界模型的价值定位在显式 rollout 或 action-time latent context；本文显示未来条件的生成计算可以只在训练时充当监督，并由 current-only representation 以受限方式内化。", "surprising": "作者的理论边界明确指出 representation 是当前输入的确定函数，因此不可能获得给定当前输入之外的样本特定未来信息；R2G 的提升只能说明它重新组织了当前上下文中已有的可预测结构。", "connections": [{"shared_mechanism": "都要求世界模型通过动作、规划或失败恢复等闭环用途验证，而不能只看视频质量。", "boundary": "既有世界模型评价概念是评价原则；Enfold 是把生成器内部状态转化为 current-only 控制接口的具体训练机制。", "difference": "评价原则不规定表示如何学习，Enfold 通过 G2R、R2G 与 stop-gradient task readout 隔离信息来源和使用路径。"}], "open_questions": ["在接触动力学、遮挡和更大分布偏移下，generator-state supervision 是否仍保留控制需要的细粒度状态，而不是只学习可预测的平均结构？"]}
---

# 生成器状态监督的当前态预测控制接口 / Current-only predictive control interface supervised by generator states

训练时让世界生成器在教师强制的真实未来上暴露多个深度和腐蚀时刻的中间状态，由 timestep-conditioned prediction head 监督只读取当前视觉上下文与语言指令的 encoder；同一 representation 以 stop-gradient 条件化未来生成器并供动作头读取，使任务梯度不直接塑造 encoder。部署控制只执行 encoder 与动作头，生成器仅在显式想象未来时运行。该接口学习的是当前条件下可预测的生成结构，而不是样本特定的未知未来；它可抑制生成噪声和外观扰动，也可能过滤无法从当前状态唯一预测却对接触控制重要的信息。论文的控制、视频和表征结果支持该接口，但 RoboTwin 小差异缺少不确定性估计，人工干预只构成定性重规划证据。
