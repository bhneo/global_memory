---
id: "reflection_ff2ab4bfb8e8d08d5e0ab7df"
type: "reflection"
status: "active"
title: "冻结 flow 先验上的奖励转向需要先稳定价值接口，再扩展潜空间自由度"
created_at: "2026-08-01T18:21:33+08:00"
updated_at: "2026-08-01T18:21:33+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "mobile-manipulation", "flow-policy", "offline-reinforcement-learning"]
confidence: "high"
source_ids: ["source_98bb68f21232969a79d77918"]
relations: []
target_ids: ["input_014809f51af455a868b68e92", "source_98bb68f21232969a79d77918"]
input_id: "input_014809f51af455a868b68e92"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "RLMM-Flow 把移动操作的奖励后训练限制在冻结 flow policy 的初始噪声接口，并把高维整段潜变量优化拆成 action critic 预热与由粗到细的时间残差开放。这使“保留生成先验”和“按任务奖励改进整身轨迹”成为可分解、可审计的训练接口。"
what_changed: "此前容易把潜空间 RL 的稳定性归因于潜变量比动作更低维；本文显示即使保持生成器冻结，高维全时域潜变量仍会因 action critic、latent critic 与 actor 的共同移动目标而失稳，需要先稳定价值蒸馏目标并逐步开放时间自由度。"
surprising: "论文中的 coarse 阶段仍输出与完整时域同形状的张量，但所有时间位置共享同一潜向量，因此有效搜索维度下降而不破坏 base-to-arm 的特征分解。"
connections: [{"shared_mechanism": "都冻结生成式基础策略，并通过更小的中间接口改变部署行为。", "boundary": "RLMM-Flow 使用离线奖励、整段轨迹 critic 和移动操作几何奖励；既有 FlowDAgger 概念使用人类纠正反演潜变量，RL-token 概念使用模型内部特征读出。", "difference": "三者的监督来源、信用分配单位和可达支持域不同，不能合并为同一适配机制。"}]
conflicts: []
open_questions: ["当奖励模型、碰撞几何或真实动力学有系统偏差时，冻结生成先验上的 latent steering 会把错误集中到哪些时域与 base-arm 子空间？"]
possible_mechanisms: ["action critic 预热降低 latent critic 的早期目标漂移，horizon-shared latent 先学习全局运动模式，后续残差再承担局部避障、终端精度和光滑性修正。"]
future_directions: ["在包含在线分布漂移和真实接触误差的评测中分别测量 critic 校准、先验偏离与闭环恢复。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 冻结 flow 先验上的奖励转向需要先稳定价值接口，再扩展潜空间自由度

## Why important

RLMM-Flow 把移动操作的奖励后训练限制在冻结 flow policy 的初始噪声接口，并把高维整段潜变量优化拆成 action critic 预热与由粗到细的时间残差开放。这使“保留生成先验”和“按任务奖励改进整身轨迹”成为可分解、可审计的训练接口。

## What changed

此前容易把潜空间 RL 的稳定性归因于潜变量比动作更低维；本文显示即使保持生成器冻结，高维全时域潜变量仍会因 action critic、latent critic 与 actor 的共同移动目标而失稳，需要先稳定价值蒸馏目标并逐步开放时间自由度。

## Surprising

论文中的 coarse 阶段仍输出与完整时域同形状的张量，但所有时间位置共享同一潜向量，因此有效搜索维度下降而不破坏 base-to-arm 的特征分解。

## Connections

- Shared mechanism: 都冻结生成式基础策略，并通过更小的中间接口改变部署行为。
  Boundary: RLMM-Flow 使用离线奖励、整段轨迹 critic 和移动操作几何奖励；既有 FlowDAgger 概念使用人类纠正反演潜变量，RL-token 概念使用模型内部特征读出。
  Difference: 三者的监督来源、信用分配单位和可达支持域不同，不能合并为同一适配机制。

## Conflicts

None recorded.

## Open questions

- 当奖励模型、碰撞几何或真实动力学有系统偏差时，冻结生成先验上的 latent steering 会把错误集中到哪些时域与 base-arm 子空间？

## Possible mechanisms

- action critic 预热降低 latent critic 的早期目标漂移，horizon-shared latent 先学习全局运动模式，后续残差再承担局部避障、终端精度和光滑性修正。

## Future directions

- 在包含在线分布漂移和真实接触误差的评测中分别测量 critic 校准、先验偏离与闭环恢复。
