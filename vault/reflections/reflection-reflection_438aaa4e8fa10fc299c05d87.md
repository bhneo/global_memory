---
id: "reflection_438aaa4e8fa10fc299c05d87"
type: "reflection"
status: "active"
title: "BayesContact：接触证据把位姿不确定性保留为后验 / contact evidence preserves pose uncertainty as a posterior"
created_at: "2026-07-27T17:24:06+08:00"
updated_at: "2026-07-27T17:24:06+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "tactile-sensing", "bayesian-inference"]
confidence: "medium"
source_ids: ["source_4757ec1a2e8a0b678a350ee1"]
relations: []
target_ids: ["input_e0631f8a902ae61ca7d8aee9", "source_4757ec1a2e8a0b678a350ee1"]
input_id: "input_e0631f8a902ae61ca7d8aee9"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "BayesContact 在 peg-in-hole 中维持物体位姿粒子 belief，并融合深度与力/力矩接触证据；这将接触丰富操作从单点姿态估计改为可随观测更新的不确定性推断。"
what_changed: "我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。"
surprising: ""
connections: [{"shared_mechanism": "两者都用视觉和接触信息缩小接触操作中的状态不确定性。", "boundary": "本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。", "difference": "深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。"}]
conflicts: []
open_questions: ["接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# BayesContact：接触证据把位姿不确定性保留为后验 / contact evidence preserves pose uncertainty as a posterior

## Why important

BayesContact 在 peg-in-hole 中维持物体位姿粒子 belief，并融合深度与力/力矩接触证据；这将接触丰富操作从单点姿态估计改为可随观测更新的不确定性推断。

## What changed

我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都用视觉和接触信息缩小接触操作中的状态不确定性。
  Boundary: 本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。
  Difference: 深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。

## Conflicts

None recorded.

## Open questions

- 接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
