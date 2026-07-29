---
id: "reflection_d3da57bd40bcce58fcac3b37"
type: "reflection"
status: "active"
title: "RoboHarness：异构策略编排的关键是交接状态而非仅技能目录"
created_at: "2026-07-25T18:06:28+08:00"
updated_at: "2026-07-25T18:06:28+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robot-planning", "policy-orchestration", "robot-memory"]
confidence: "medium"
source_ids: ["source_cc2f2812863ca6751c223b54"]
relations: []
target_ids: ["input_9fe1d68a8a84e597e0f28fd3", "source_cc2f2812863ca6751c223b54"]
input_id: "input_9fe1d68a8a84e597e0f28fd3"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "RoboHarness 将长时程执行失败定位到两类可操作接口：策略在当前状态下的能力边界，以及前一策略终态是否落入下一策略的可行输入分布。这比把多策略系统描述成静态技能库更能指导何处需要观测、路由与恢复。"
what_changed: "此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。"
surprising: ""
connections: [{"shared_mechanism": "两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。", "boundary": "该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。", "difference": "RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# RoboHarness：异构策略编排的关键是交接状态而非仅技能目录

## Why important

RoboHarness 将长时程执行失败定位到两类可操作接口：策略在当前状态下的能力边界，以及前一策略终态是否落入下一策略的可行输入分布。这比把多策略系统描述成静态技能库更能指导何处需要观测、路由与恢复。

## What changed

此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。
  Boundary: 该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。
  Difference: RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
