---
id: "reflection_c0693ad0e6abf8397dbdfd87"
type: "reflection"
status: "active"
title: "PAC-ACT：动作块既是生成单位，也应成为信用分配与约束单位"
created_at: "2026-07-20T11:53:47+08:00"
updated_at: "2026-07-20T11:53:47+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-rl", "action-chunking", "contact-manipulation", "policy-optimization"]
confidence: "high"
source_ids: ["source_c79f943c818d06054ca5cf92"]
relations: []
target_ids: ["input_29ae46988359dcaa4c2d9fd8", "source_c79f943c818d06054ca5cf92"]
input_id: "input_29ae46988359dcaa4c2d9fd8"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它直接处理动作块策略与逐步奖励之间的结构错位，把 PPO 重写为块级决策过程，并用混合行为先验约束保持预训练 ACT 的低延迟与动作分布。"
what_changed: "动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。"
surprising: "在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。"
connections: [{"shared_mechanism": "与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。", "boundary": "PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。", "difference": "PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。"}]
conflicts: ["更长动作块提高连续性和吞吐，却可能延迟接触异常后的纠正；更强行为先验提高安全性，也可能抑制必要探索。"]
open_questions: ["块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？"]
possible_mechanisms: ["块级优势让奖励反馈与实际策略决策单位对齐，混合 KL 约束同时限制块分布和逐动作偏移。"]
future_directions: ["在同一硬件与数据预算下比较逐步 PPO、固定块 PPO 和风险驱动动态块 PPO。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# PAC-ACT：动作块既是生成单位，也应成为信用分配与约束单位

## Why important

它直接处理动作块策略与逐步奖励之间的结构错位，把 PPO 重写为块级决策过程，并用混合行为先验约束保持预训练 ACT 的低延迟与动作分布。

## What changed

动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。

## Surprising

在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。

## Connections

- Shared mechanism: 与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。
  Boundary: PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。
  Difference: PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。

## Conflicts

- 更长动作块提高连续性和吞吐，却可能延迟接触异常后的纠正；更强行为先验提高安全性，也可能抑制必要探索。

## Open questions

- 块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？

## Possible mechanisms

- 块级优势让奖励反馈与实际策略决策单位对齐，混合 KL 约束同时限制块分布和逐动作偏移。

## Future directions

- 在同一硬件与数据预算下比较逐步 PPO、固定块 PPO 和风险驱动动态块 PPO。
