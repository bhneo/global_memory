---
id: "reflection_3b2e99de9c8c6dfc2ba8cd5a"
type: "reflection"
status: "active"
title: "DEED：零售人形 VLA 的可靠性首先是部署系统问题"
created_at: "2026-07-24T18:05:35+08:00"
updated_at: "2026-07-24T18:05:35+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["humanoid-robotics", "vla", "post-training"]
confidence: "medium"
source_ids: ["source_3846f8c1451f8a12e0f87b33"]
relations: []
target_ids: ["input_0099dd755223f11535e0d061", "source_3846f8c1451f8a12e0f87b33"]
input_id: "input_0099dd755223f11535e0d061"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "DEED 把零售人形机器人的失效面放在控制频率、数据筛选、视觉重点和部署后经验回收的组合接口上；这为区分基础模型能力不足与系统集成失配提供了更可操作的诊断单位。"
what_changed: "先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上，控制与数据接口的对齐以及对策略自身失败状态的经验回收同样决定能否从朴素微调转为可用行为。"
surprising: ""
connections: []
conflicts: []
open_questions: ["文本 advantage 前缀和视觉语言价值函数在不同零售任务、不同经验比例下何时会避免或加剧自生成 rollout 主导训练分布的退化？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# DEED：零售人形 VLA 的可靠性首先是部署系统问题

## Why important

DEED 把零售人形机器人的失效面放在控制频率、数据筛选、视觉重点和部署后经验回收的组合接口上；这为区分基础模型能力不足与系统集成失配提供了更可操作的诊断单位。

## What changed

先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上，控制与数据接口的对齐以及对策略自身失败状态的经验回收同样决定能否从朴素微调转为可用行为。

## Surprising

Not stated.

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 文本 advantage 前缀和视觉语言价值函数在不同零售任务、不同经验比例下何时会避免或加剧自生成 rollout 主导训练分布的退化？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
