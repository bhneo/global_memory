---
id: "reflection_a4b214ba9367da2f36ca1c06"
type: "reflection"
status: "active"
title: "RynnBrain 1.1：跨本体共享动作空间仍需保留可用维度边界"
created_at: "2026-07-23T18:07:15+08:00"
updated_at: "2026-07-23T18:07:15+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["cross-embodiment", "vla", "grounding"]
confidence: "medium"
source_ids: ["source_5c29f310c66b0fb5c6cb2758"]
relations: []
target_ids: ["input_99ca8c0b2d899e5a8f1d8aa0", "source_5c29f310c66b0fb5c6cb2758"]
input_id: "input_99ca8c0b2d899e5a8f1d8aa0"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "RynnBrain 1.1 把接触点预测与 3D grounding 加入具身预训练，并以语义对齐的身体部位分组和本体掩码训练跨本体 VLA；它把共享表征与各机器人可执行控制维度之间的边界显式化。"
what_changed: "跨本体训练不必强迫不兼容的动作空间逐维对齐；共享语义分组可以与本体特定掩码配合，但仍需要对各平台的真实控制结果单独验证。"
surprising: ""
connections: []
conflicts: []
open_questions: ["身体部位语义分组在接触、灵巧手和全身协调任务中何时会掩盖关键的本体差异？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# RynnBrain 1.1：跨本体共享动作空间仍需保留可用维度边界

## Why important

RynnBrain 1.1 把接触点预测与 3D grounding 加入具身预训练，并以语义对齐的身体部位分组和本体掩码训练跨本体 VLA；它把共享表征与各机器人可执行控制维度之间的边界显式化。

## What changed

跨本体训练不必强迫不兼容的动作空间逐维对齐；共享语义分组可以与本体特定掩码配合，但仍需要对各平台的真实控制结果单独验证。

## Surprising

Not stated.

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 身体部位语义分组在接触、灵巧手和全身协调任务中何时会掩盖关键的本体差异？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
