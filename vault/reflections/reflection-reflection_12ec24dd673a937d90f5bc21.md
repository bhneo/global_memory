---
id: "reflection_12ec24dd673a937d90f5bc21"
type: "reflection"
status: "active"
title: "Latent Memory Palace：控制中的自适应潜空间推理"
created_at: "2026-07-19T17:16:24+08:00"
updated_at: "2026-07-19T17:16:24+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-control", "latent-reasoning"]
confidence: "medium"
source_ids: ["source_be9781ec8ca637c5dfd8fabb"]
relations: []
target_ids: ["input_209853864d2fbd982e270c61", "source_be9781ec8ca637c5dfd8fabb"]
input_id: "input_209853864d2fbd982e270c61"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。"
what_changed: "此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数。"
surprising: "同一套自回归潜变量框架还可产生可变长度动作 tokenizer，暗示推理长度与动作分段可能由共同的表示机制控制。"
connections: [{"shared_mechanism": "都根据当前状态与任务难度动态分配有限的计算或执行预算", "boundary": "连接只适用于自适应预算分配，不表示内部推理步数与外部动作执行时域等价", "difference": "LMP 调整动作生成前的潜变量推断长度，动态执行时域调整动作生成后的开环执行长度"}]
conflicts: ["潜空间推理的可解释路径不等于可验证的因果推理，长度增加也未必代表任务难度判断正确"]
open_questions: ["潜推理长度能否被校准为任务难度或失败风险的可靠信号？"]
possible_mechanisms: ["带 EOS 的自回归潜变量后验按输入复杂度停止推断"]
future_directions: ["比较内部潜推理长度、动作块执行时域与外部重规划频率的联合分配"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Latent Memory Palace：控制中的自适应潜空间推理

## Why important

它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。

## What changed

此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数。

## Surprising

同一套自回归潜变量框架还可产生可变长度动作 tokenizer，暗示推理长度与动作分段可能由共同的表示机制控制。

## Connections

- Shared mechanism: 都根据当前状态与任务难度动态分配有限的计算或执行预算
  Boundary: 连接只适用于自适应预算分配，不表示内部推理步数与外部动作执行时域等价
  Difference: LMP 调整动作生成前的潜变量推断长度，动态执行时域调整动作生成后的开环执行长度

## Conflicts

- 潜空间推理的可解释路径不等于可验证的因果推理，长度增加也未必代表任务难度判断正确

## Open questions

- 潜推理长度能否被校准为任务难度或失败风险的可靠信号？

## Possible mechanisms

- 带 EOS 的自回归潜变量后验按输入复杂度停止推断

## Future directions

- 比较内部潜推理长度、动作块执行时域与外部重规划频率的联合分配
