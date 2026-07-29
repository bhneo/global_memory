---
id: "reflection_dc9b1c4fbde4b505081c875b"
type: "reflection"
status: "active"
title: "Schema：反例必须能够同时推翻状态表示与转移规则"
created_at: "2026-07-26T12:18:25+08:00"
updated_at: "2026-07-26T12:18:25+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["world-models", "mechanism-discovery", "agent-harness"]
confidence: "medium"
source_ids: ["source_d90b4e9bf278dfc5e68d1bb5"]
relations: []
target_ids: ["input_bf6f63ea23391740118ba725", "source_d90b4e9bf278dfc5e68d1bb5"]
input_id: "input_bf6f63ea23391740118ba725"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Schema 把隐式推理外化为可编辑的状态程序、转移程序和 append-only Timeline，并要求规划前对完整真实交互历史逐步 backtest；其关键不是单纯使用代码，而是让预测失败可以定位到状态表示或机制规则中的具体缺口。"
what_changed: "此前容易把可执行世界模型理解为只需提供可搜索的 transition function；该来源表明，搜索只对当前表示下的图完备，真正的发现成本在于用区分性实验暴露遗漏对象、状态变量或转移边。"
surprising: "同一 harness 下模型差异主要体现在何时质疑表示并选择区分性实验，而不是最终能否写出同一种规则；但文中接近满分的 Public-set 结果为自报且不能外推到 Semi-private。"
connections: [{"shared_mechanism": "Schema 与 Global Memory 都把不可改写的观察历史和可修订的模型解释分层，并用可重放记录约束后续推理。", "boundary": "该连接适用于需要从交互反例修订显式模型的系统；ARC 的离散、完全可记录环境不等同于开放世界机器人或知识治理。", "difference": "Schema 的程序直接用于 BFS 规划和环境动作；Global Memory 的 Reflection 与 Synthesis 明确不是执行模型，也不能成为 Execution Evidence。"}]
conflicts: []
open_questions: ["在连续、部分可观测且含传感噪声的机器人环境中，怎样把精确 backtest 改写为保留不确定性的模型检验而不把误差都归因于规则错误？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Schema：反例必须能够同时推翻状态表示与转移规则

## Why important

Schema 把隐式推理外化为可编辑的状态程序、转移程序和 append-only Timeline，并要求规划前对完整真实交互历史逐步 backtest；其关键不是单纯使用代码，而是让预测失败可以定位到状态表示或机制规则中的具体缺口。

## What changed

此前容易把可执行世界模型理解为只需提供可搜索的 transition function；该来源表明，搜索只对当前表示下的图完备，真正的发现成本在于用区分性实验暴露遗漏对象、状态变量或转移边。

## Surprising

同一 harness 下模型差异主要体现在何时质疑表示并选择区分性实验，而不是最终能否写出同一种规则；但文中接近满分的 Public-set 结果为自报且不能外推到 Semi-private。

## Connections

- Shared mechanism: Schema 与 Global Memory 都把不可改写的观察历史和可修订的模型解释分层，并用可重放记录约束后续推理。
  Boundary: 该连接适用于需要从交互反例修订显式模型的系统；ARC 的离散、完全可记录环境不等同于开放世界机器人或知识治理。
  Difference: Schema 的程序直接用于 BFS 规划和环境动作；Global Memory 的 Reflection 与 Synthesis 明确不是执行模型，也不能成为 Execution Evidence。

## Conflicts

None recorded.

## Open questions

- 在连续、部分可观测且含传感噪声的机器人环境中，怎样把精确 backtest 改写为保留不确定性的模型检验而不把误差都归因于规则错误？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
