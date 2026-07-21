---
id: "reflection_f5a4802aeb05942de18022f0"
type: "reflection"
status: "active"
title: "WAM 鲁棒性干预：可分离激活是可操控性的诊断而非普适保证"
created_at: "2026-07-20T18:05:46+08:00"
updated_at: "2026-07-20T18:05:46+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["world-model", "robot-robustness", "mechanistic-interpretability"]
confidence: "medium"
source_ids: ["source_38cba686373b003398483ab2"]
relations: []
target_ids: ["input_35fb42270b48cd7cab723f0e", "source_38cba686373b003398483ab2"]
input_id: "input_35fb42270b48cd7cab723f0e"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作将分布外鲁棒性的模型内诊断与推理时控制相连：先检查扰动相关激活是否低维线性可分，再在该子空间中做受约束闭环 steering。"
what_changed: "此前训练后或提示级的鲁棒性改进常被看作统一手段；这里显示能否从激活中得到可迁移干预方向取决于具体架构和扰动。"
surprising: ""
connections: [{"shared_mechanism": "两者都先诊断内部表示中是否存在与目标行为相关的可用结构，再把诊断结果用于干预。", "boundary": "低维可分离只是在所测模型和扰动上的预测信号，不是因果解释或安全保证。", "difference": "表示对齐触觉 grounding 在训练期把未来接触结果监督到中间层；WAM steering 在不微调模型时，于推理期调节已存在的激活方向。"}]
conflicts: []
open_questions: ["在新的相机、夹爪和视觉噪声组合上，线性可分性与闭环 steering 效果的相关性是否仍能校准？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# WAM 鲁棒性干预：可分离激活是可操控性的诊断而非普适保证

## Why important

该工作将分布外鲁棒性的模型内诊断与推理时控制相连：先检查扰动相关激活是否低维线性可分，再在该子空间中做受约束闭环 steering。

## What changed

此前训练后或提示级的鲁棒性改进常被看作统一手段；这里显示能否从激活中得到可迁移干预方向取决于具体架构和扰动。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都先诊断内部表示中是否存在与目标行为相关的可用结构，再把诊断结果用于干预。
  Boundary: 低维可分离只是在所测模型和扰动上的预测信号，不是因果解释或安全保证。
  Difference: 表示对齐触觉 grounding 在训练期把未来接触结果监督到中间层；WAM steering 在不微调模型时，于推理期调节已存在的激活方向。

## Conflicts

None recorded.

## Open questions

- 在新的相机、夹爪和视觉噪声组合上，线性可分性与闭环 steering 效果的相关性是否仍能校准？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
