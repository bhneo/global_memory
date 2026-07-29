---
id: "reflection_d8d4183ecacf40814756f4c2"
type: "reflection"
status: "active"
title: "Reflex 流式 VLA：缓存正确性来自上下文分区 / Reflex streaming VLA preserves caching through context partitioning"
created_at: "2026-07-27T17:19:51+08:00"
updated_at: "2026-07-27T17:19:51+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vision-language-action", "systems"]
confidence: "medium"
source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
relations: []
target_ids: ["input_db9ee752c6786f61cb66b6b1", "source_e67cd99ac31c7017d6f7f7c7"]
input_id: "input_db9ee752c6786f61cb66b6b1"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Reflex 将 flow-matching VLA 的上下文分为 static、sliding 与 dynamic 区域，利用感知编码器对去噪循环的独立性实现增量 KV 更新；其 50Hz 与加速结果仍依赖固定输入下的等价性、AdaRMSNorm 和所报告基准。"
what_changed: "我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。"
surprising: ""
connections: [{"shared_mechanism": "两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。", "boundary": "本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。", "difference": "一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。"}]
conflicts: []
open_questions: ["感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Reflex 流式 VLA：缓存正确性来自上下文分区 / Reflex streaming VLA preserves caching through context partitioning

## Why important

Reflex 将 flow-matching VLA 的上下文分为 static、sliding 与 dynamic 区域，利用感知编码器对去噪循环的独立性实现增量 KV 更新；其 50Hz 与加速结果仍依赖固定输入下的等价性、AdaRMSNorm 和所报告基准。

## What changed

我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。
  Boundary: 本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。
  Difference: 一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。

## Conflicts

None recorded.

## Open questions

- 感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
