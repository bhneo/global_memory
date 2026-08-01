---
id: "concept_6a559a41722de87986c350e7"
type: "concept"
status: "proposal"
title: "冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior"
created_at: "2026-08-01T18:21:36+08:00"
updated_at: "2026-08-01T18:21:36+08:00"
aliases: ["RLMM-Flow", "staged latent steering", "coarse-to-fine latent-space RL", "冻结流策略潜空间强化学习"]
tags: []
domains: ["robotics", "mobile-manipulation", "flow-policy", "offline-reinforcement-learning"]
confidence: "high"
source_ids: ["source_98bb68f21232969a79d77918"]
relations: [{"type": "derived_from", "target_id": "source_98bb68f21232969a79d77918", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "两者都冻结生成策略并在输入潜空间转向行为；RLMM-Flow 由离线奖励和 critic 驱动，既有概念由人类纠正动作反演驱动。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f9a9f1d1818632c0380b7942", "reason": "两者都把 RL 适配限制在基础策略之外的小接口；RLMM-Flow 优化生成噪声并保留 flow decoder，RL-token 从内部特征训练 actor-critic 读出。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_98bb68f21232969a79d77918"
reflection_context: {"reflection_ids": ["reflection_ff2ab4bfb8e8d08d5e0ab7df"], "importance": "high", "changed_belief": "此前容易把潜空间 RL 的稳定性归因于潜变量比动作更低维；本文显示即使保持生成器冻结，高维全时域潜变量仍会因 action critic、latent critic 与 actor 的共同移动目标而失稳，需要先稳定价值蒸馏目标并逐步开放时间自由度。", "surprising": "论文中的 coarse 阶段仍输出与完整时域同形状的张量，但所有时间位置共享同一潜向量，因此有效搜索维度下降而不破坏 base-to-arm 的特征分解。", "connections": [{"shared_mechanism": "都冻结生成式基础策略，并通过更小的中间接口改变部署行为。", "boundary": "RLMM-Flow 使用离线奖励、整段轨迹 critic 和移动操作几何奖励；既有 FlowDAgger 概念使用人类纠正反演潜变量，RL-token 概念使用模型内部特征读出。", "difference": "三者的监督来源、信用分配单位和可达支持域不同，不能合并为同一适配机制。"}], "open_questions": ["当奖励模型、碰撞几何或真实动力学有系统偏差时，冻结生成先验上的 latent steering 会把错误集中到哪些时域与 base-arm 子空间？"]}
---

# 冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior

先用专家轨迹预训练并冻结整身 flow policy，再以 action-space critic 评价解码动作块、把其价值蒸馏给 latent critic，并由 latent actor 转向初始噪声。为避免 action critic、latent critic 和 actor 同时学习造成移动目标，先单独预热 action critic；为避免直接搜索 H×d 的全时域潜空间，先把 horizon-shared latent 重复到完整形状以学习全局 base-arm 运动模式，再开放均值中心化的时间残差修正局部避障、终端精度、关节约束和光滑性。论文证据限于其离线奖励、PhyScene 数据、共享 MPC 和零样本真实部署，机制仍受基础 flow policy 支持域、奖励/几何误差及真实动力学偏差约束。
