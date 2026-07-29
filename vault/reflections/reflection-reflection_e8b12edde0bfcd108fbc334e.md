---
id: "reflection_e8b12edde0bfcd108fbc334e"
type: "reflection"
status: "active"
title: "Agentic Real2Sim：episode twin 的价值取决于可运行的物理接口而非视觉外观"
created_at: "2026-07-26T12:18:25+08:00"
updated_at: "2026-07-26T12:18:25+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["real2sim", "robot-simulation", "embodied-ai"]
confidence: "medium"
source_ids: ["source_4f709a2f26b6_v0002_cb9f3e56f3e6"]
relations: []
target_ids: ["input_bbbfd5548c15d7accd857172", "source_4f709a2f26b6_v0002_cb9f3e56f3e6"]
input_id: "input_bbbfd5548c15d7accd857172"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "完整论文把真实交互录像到仿真资产的转换写成统一 episode contract，要求几何、演员、对象状态、物理参数、相机、轨迹、回放指标与修复接口共同可运行；这使 Real2Sim 的评价对象从静态资产质量变成可查询、可重放的物理交互单元。"
what_changed: "此前已有 Working Concept 已经覆盖可运行交互孪生，因此新版本不需要重复概念；完整 reader 进一步限定了当前证据：DROID-100 的刚体回放成功率仍低于一半，deformable 与 humanoid 仅作定性压力测试，下游策略学习仍是目标而非已完成验证。"
surprising: "在固定流程下，开源 31B VLM 的观察到的回放成功数不低于三种专有后端，但所有后端的绝对成功率都低于 50%，说明上游视觉与仿真组件可能比 VLM 选择更限制当前系统。"
connections: []
conflicts: []
open_questions: ["如何用真实闭环策略的行为误差而非 VLM 回放评分，验证 episodic twin 对策略学习与评测的任务保真度？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Agentic Real2Sim：episode twin 的价值取决于可运行的物理接口而非视觉外观

## Why important

完整论文把真实交互录像到仿真资产的转换写成统一 episode contract，要求几何、演员、对象状态、物理参数、相机、轨迹、回放指标与修复接口共同可运行；这使 Real2Sim 的评价对象从静态资产质量变成可查询、可重放的物理交互单元。

## What changed

此前已有 Working Concept 已经覆盖可运行交互孪生，因此新版本不需要重复概念；完整 reader 进一步限定了当前证据：DROID-100 的刚体回放成功率仍低于一半，deformable 与 humanoid 仅作定性压力测试，下游策略学习仍是目标而非已完成验证。

## Surprising

在固定流程下，开源 31B VLM 的观察到的回放成功数不低于三种专有后端，但所有后端的绝对成功率都低于 50%，说明上游视觉与仿真组件可能比 VLM 选择更限制当前系统。

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 如何用真实闭环策略的行为误差而非 VLM 回放评分，验证 episodic twin 对策略学习与评测的任务保真度？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
