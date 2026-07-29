---
id: "reflection_ee2dc3e5679d14ca67d9f5df"
type: "reflection"
status: "active"
title: "SafeRelBench：安全必须在风险动作之前验证关系前置条件"
created_at: "2026-07-21T17:41:59+08:00"
updated_at: "2026-07-21T17:41:59+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-safety", "spatial-reasoning", "evaluation"]
confidence: "medium"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
relations: []
target_ids: ["input_ebc477907cc0b3217e20c03c", "source_b470fe87f9d09df2b7d3b5fd"]
input_id: "input_ebc477907cc0b3217e20c03c"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它把安全评测从最终状态和静态风险识别推进到执行过程：支撑、容纳和邻近关系决定某个普通动作在当前时刻是否安全。"
what_changed: "完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。"
surprising: "七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。"
connections: [{"shared_mechanism": "都用类型化前置条件约束动作序列。", "boundary": "基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。", "difference": "类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。"}]
conflicts: []
open_questions: ["关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？"]
possible_mechanisms: ["把每个安全条件绑定到具体 risk-prone action，可检测动作顺序中的过程失败。"]
future_directions: ["加入不确定关系估计、真实机器人接触风险和可恢复执行的评测。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# SafeRelBench：安全必须在风险动作之前验证关系前置条件

## Why important

它把安全评测从最终状态和静态风险识别推进到执行过程：支撑、容纳和邻近关系决定某个普通动作在当前时刻是否安全。

## What changed

完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。

## Surprising

七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。

## Connections

- Shared mechanism: 都用类型化前置条件约束动作序列。
  Boundary: 基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。
  Difference: 类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。

## Conflicts

None recorded.

## Open questions

- 关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？

## Possible mechanisms

- 把每个安全条件绑定到具体 risk-prone action，可检测动作顺序中的过程失败。

## Future directions

- 加入不确定关系估计、真实机器人接触风险和可恢复执行的评测。
