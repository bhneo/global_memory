---
id: "reflection_bd1bc1b00ef5304ee9d29e9c"
type: "reflection"
status: "active"
title: "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens"
created_at: "2026-07-27T18:19:40+08:00"
updated_at: "2026-07-27T18:19:40+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vision-language-action", "force-sensing"]
confidence: "medium"
source_ids: ["source_1ee2c3fae53a9d05689cd143"]
relations: []
target_ids: ["input_ef85630f475f692df3ccaeb6", "source_1ee2c3fae53a9d05689cd143"]
input_id: "input_ef85630f475f692df3ccaeb6"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "FM-VLA 以预训练 VAE 将高频 wrench 历史压缩为 force-memory tokens，并与短状态历史一起条件化 action expert，从而面向视觉变化微弱的非 Markov 接触任务保留事件历史。"
what_changed: "我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。"
surprising: ""
connections: [{"shared_mechanism": "两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。", "boundary": "本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。", "difference": "视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。"}]
conflicts: []
open_questions: ["传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens

## Why important

FM-VLA 以预训练 VAE 将高频 wrench 历史压缩为 force-memory tokens，并与短状态历史一起条件化 action expert，从而面向视觉变化微弱的非 Markov 接触任务保留事件历史。

## What changed

我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。
  Boundary: 本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。
  Difference: 视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。

## Conflicts

None recorded.

## Open questions

- 传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
