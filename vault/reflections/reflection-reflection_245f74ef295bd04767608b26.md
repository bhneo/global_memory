---
id: "reflection_245f74ef295bd04767608b26"
type: "reflection"
status: "active"
title: "RoboTTT：把长序列经验写入策略 fast weights"
created_at: "2026-07-21T17:41:49+08:00"
updated_at: "2026-07-21T17:41:49+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "test-time-training", "long-horizon-manipulation"]
confidence: "medium"
source_ids: ["source_79475aef7849b08664b51a4e"]
relations: []
target_ids: ["input_60b32d4869a86abdba7f0396", "source_79475aef7849b08664b51a4e"]
input_id: "input_60b32d4869a86abdba7f0396"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它不是简单增加历史帧，而是在推理过程中用 TTT 层的 fast weights 吸收序列，试图把示范、纠正和自身执行历史变成在线适应状态。"
what_changed: "长上下文能力既可通过显式记忆 token 实现，也可通过参数化快速状态实现；两者在可解释性、遗忘和计算成本上有不同风险。"
surprising: "在三项双臂装配任务中作者报告平均完成分 79%，高于单步 GR00T N1.7 的 42% 和 GDN 的 56%；训练使用 16 张 GB200，长上下文收益伴随显著训练成本。"
connections: [{"shared_mechanism": "都保留分钟级历史以改进后续动作。", "boundary": "fast-weight 适应不等于持久跨会话记忆，也不自动保证纠正方向安全。", "difference": "NativeMEM 显式保存动作对齐视觉 token；RoboTTT 通过测试时梯度更新把上下文折叠进快速权重。"}]
conflicts: []
open_questions: ["fast weights 遇到错误动作、自生成偏差或任务切换时如何检测并回滚？"]
possible_mechanisms: ["序列训练让 fast-weight 更新学习吸收人类纠正和历史动作，从而在测试时在线改变策略。"]
future_directions: ["比较显式 token 记忆、递归状态和 fast weights 在干扰、回滚、延迟及跨任务切换上的表现。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# RoboTTT：把长序列经验写入策略 fast weights

## Why important

它不是简单增加历史帧，而是在推理过程中用 TTT 层的 fast weights 吸收序列，试图把示范、纠正和自身执行历史变成在线适应状态。

## What changed

长上下文能力既可通过显式记忆 token 实现，也可通过参数化快速状态实现；两者在可解释性、遗忘和计算成本上有不同风险。

## Surprising

在三项双臂装配任务中作者报告平均完成分 79%，高于单步 GR00T N1.7 的 42% 和 GDN 的 56%；训练使用 16 张 GB200，长上下文收益伴随显著训练成本。

## Connections

- Shared mechanism: 都保留分钟级历史以改进后续动作。
  Boundary: fast-weight 适应不等于持久跨会话记忆，也不自动保证纠正方向安全。
  Difference: NativeMEM 显式保存动作对齐视觉 token；RoboTTT 通过测试时梯度更新把上下文折叠进快速权重。

## Conflicts

None recorded.

## Open questions

- fast weights 遇到错误动作、自生成偏差或任务切换时如何检测并回滚？

## Possible mechanisms

- 序列训练让 fast-weight 更新学习吸收人类纠正和历史动作，从而在测试时在线改变策略。

## Future directions

- 比较显式 token 记忆、递归状态和 fast weights 在干扰、回滚、延迟及跨任务切换上的表现。
