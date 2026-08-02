---
id: "concept_8a7645759329c1444d94a4cf"
type: "concept"
status: "proposal"
title: "同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training"
created_at: "2026-08-02T18:22:04+08:00"
updated_at: "2026-08-02T18:22:04+08:00"
aliases: ["X-NavDP", "GQRM", "Group Q-score Reweighted Matching", "self-bootstrapped action perturbation"]
tags: []
domains: ["robotics", "navigation", "diffusion-policy", "reinforcement-learning", "cross-embodiment"]
confidence: "high"
source_ids: ["source_bdb17eb4583ec8af52f28dfb"]
relations: [{"type": "derived_from", "target_id": "source_bdb17eb4583ec8af52f28dfb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都共享高层策略以迁移不同本体；X-NavDP 仍通过 embodiment FiLM 和各形态低层控制器显式吸收运动学与动力学差异。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都在保留预训练生成先验的前提下用价值信号后训练；X-NavDP 在线更新 score，RLMM-Flow 冻结 flow decoder 并转向生成潜变量。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_bdb17eb4583ec8af52f28dfb"
reflection_context: {"reflection_ids": ["reflection_7991ec84469c68e4271878a4"], "importance": "high", "changed_belief": "我原先把候选动作 Q 值重加权理解为全局优势过滤；该方法显示，在不同状态回报尺度差异大时，应先在同状态候选组内归一化，避免简单状态垄断梯度。", "surprising": "无目标候选并非随机噪声，而是沿带目标预测相对当前策略动作做有符号外推，从而扩大探索又保留动作流形。", "connections": [{"shared_mechanism": "X-NavDP 与 concept_generalist_cross_embodiment_vla 都把不同机器人形态的数据或策略经验汇入共享高层决策模型。", "boundary": "该连接限于高层导航策略共享；X-NavDP 仍依赖每种形态的 embodiment 条件与预训练低层控制器，不能据此推断控制接口无关。", "difference": "通用跨本体 VLA 节点描述广义数据与本体适配框架，X-NavDP 具体以 FiLM 条件化、结构化扩散候选和在线 Q 重加权处理导航。"}, {"shared_mechanism": "X-NavDP 与 concept_6a559a41722de87986c350e7 都保留预训练生成策略的行为先验，并用价值信号集中改进较小的生成接口。", "boundary": "该连接要求基础策略已在候选邻域提供可行行为；critic 排序错误或先验无覆盖时，两者都不保证安全改进。", "difference": "X-NavDP 在线更新 diffusion score matching，RLMM-Flow 冻结 flow decoder 并由 latent actor-critic 转向初始噪声。"}], "open_questions": ["如何在保持同状态相对归一化优点的同时，加入跨状态的风险校准，使困难状态的高相对分数不掩盖绝对安全下界？"]}
---

# 同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training

为在在线 RL 中稳定改进连续扩散导航策略，先从当前策略构造保留动作流形的带目标候选，以及沿带目标预测相对当前动作做有符号外推的无目标候选；再在同一状态的候选组内归一化 Q 分数、强化相对高价值候选，并以重加权 score matching 更新策略。这样困难低回报状态不会因绝对 Q 尺度较低而失去梯度，本体 FiLM 则让共享策略适配不同形态。边界是 critic 必须在组内排序可靠；方法仍依赖每种形态的低层控制器、短期观测记忆和训练场景覆盖，对透明或空心障碍的感知也有限。
