---
id: "concept_f9a9f1d1818632c0380b7942"
type: "concept"
status: "proposal"
title: "VLA 的强化学习读出接口"
created_at: "2026-07-20T11:55:51+08:00"
updated_at: "2026-07-20T11:55:51+08:00"
aliases: ["RL Token", "RLT", "reinforcement-learning readout interface"]
tags: []
domains: ["embodied-ai", "robot-rl", "vla", "representation-learning"]
confidence: "high"
source_ids: ["source_40700e61702f4b5a5765e11d"]
relations: [{"type": "derived_from", "target_id": "source_40700e61702f4b5a5765e11d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_40700e61702f4b5a5765e11d"
reflection_context: {"reflection_ids": ["reflection_5b4f45d757e5b256cdddfcfa"], "importance": "weekly", "changed_belief": "VLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。", "surprising": "收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。", "connections": [{"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}], "open_questions": ["RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？"]}
---

# VLA 的强化学习读出接口

VLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。
