---
id: "reflection_1f5ecace3c0b5fd265b9d846"
type: "reflection"
status: "active"
title: "LIFT：接触反馈可作为保留先验的块内反应接口"
created_at: "2026-07-24T18:06:10+08:00"
updated_at: "2026-07-24T18:06:10+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["vla", "force-control", "contact-rich-manipulation"]
confidence: "medium"
source_ids: ["source_4e06d1b1cdcd0d07eff47909"]
relations: []
target_ids: ["input_9f6dd11d13abf277fa0e162d", "source_4e06d1b1cdcd0d07eff47909"]
input_id: "input_9f6dd11d13abf277fa0e162d"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "LIFT 不重训视觉语言主干，而以零初始化残差把延迟对齐的近期六维力记忆注入并行反应分支；它把接触不确定性定位为可在动作块内刷新、且不必破坏预训练先验的接口问题。"
what_changed: "接触传感并非只能作为全模型重训的额外输入；若初始化时严格保持原动作输出，稀缺的在线力纠正可以针对策略实际访问的接触失败状态进行局部适配。"
surprising: ""
connections: [{"shared_mechanism": "两者都通过补充交互信号来弥补纯视觉在接触状态中的可观测性缺口。", "boundary": "该连接适用于力、力矩或跟踪偏差能可靠反映接触变化的控制系统，不说明任一 proxy 在所有硬件上等价于测得六维力。", "difference": "LIFT 显式编码近期六维末端力并在动作块内反应；既有概念讨论遥操作 leader–follower 的跟踪偏差作为隐式线索。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# LIFT：接触反馈可作为保留先验的块内反应接口

## Why important

LIFT 不重训视觉语言主干，而以零初始化残差把延迟对齐的近期六维力记忆注入并行反应分支；它把接触不确定性定位为可在动作块内刷新、且不必破坏预训练先验的接口问题。

## What changed

接触传感并非只能作为全模型重训的额外输入；若初始化时严格保持原动作输出，稀缺的在线力纠正可以针对策略实际访问的接触失败状态进行局部适配。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都通过补充交互信号来弥补纯视觉在接触状态中的可观测性缺口。
  Boundary: 该连接适用于力、力矩或跟踪偏差能可靠反映接触变化的控制系统，不说明任一 proxy 在所有硬件上等价于测得六维力。
  Difference: LIFT 显式编码近期六维末端力并在动作块内反应；既有概念讨论遥操作 leader–follower 的跟踪偏差作为隐式线索。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
