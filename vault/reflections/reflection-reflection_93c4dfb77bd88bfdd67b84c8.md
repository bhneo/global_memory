---
id: "reflection_93c4dfb77bd88bfdd67b84c8"
type: "reflection"
status: "active"
title: "HCPG-Flow：接触阶段门控替代不可靠的 critic 排序 / contact-phase gating replaces weak critic ranking"
created_at: "2026-07-27T18:15:19+08:00"
updated_at: "2026-07-27T18:15:19+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "reinforcement-learning", "flow-policies"]
confidence: "medium"
source_ids: ["source_bee998153a82cd2a92db045b"]
relations: []
target_ids: ["input_ee2a2a06a55912556138f660", "source_bee998153a82cd2a92db045b"]
input_id: "input_ee2a2a06a55912556138f660"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "HCPG-Flow 对 flow policy 的多个动作候选按是否接触切换 TCP 接近或物体任务进度，以一阶距离下降选择软动作，绕开 replay 覆盖不足时 critic 的长程排序误差。"
what_changed: "我会把其收益归于显式对象几何、可用接触信号和任务距离，而不把解析 selector 当成对未知任务或缺少接触感知的普适替代。"
surprising: ""
connections: [{"shared_mechanism": "两者都在执行时利用非参数化的局部物理/几何结构改善生成式策略选择。", "boundary": "本文限于其 contact gate、对象中心距离、K=4 候选和 SAC-Flow 评测设置。", "difference": "critic ranking 依赖学习到的长程价值；HCPG 在接触前后使用分阶段的一阶局部进度。"}]
conflicts: []
open_questions: ["接触判定噪声和任务进度不可由单一距离表示时，selector 如何退化或校准？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# HCPG-Flow：接触阶段门控替代不可靠的 critic 排序 / contact-phase gating replaces weak critic ranking

## Why important

HCPG-Flow 对 flow policy 的多个动作候选按是否接触切换 TCP 接近或物体任务进度，以一阶距离下降选择软动作，绕开 replay 覆盖不足时 critic 的长程排序误差。

## What changed

我会把其收益归于显式对象几何、可用接触信号和任务距离，而不把解析 selector 当成对未知任务或缺少接触感知的普适替代。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都在执行时利用非参数化的局部物理/几何结构改善生成式策略选择。
  Boundary: 本文限于其 contact gate、对象中心距离、K=4 候选和 SAC-Flow 评测设置。
  Difference: critic ranking 依赖学习到的长程价值；HCPG 在接触前后使用分阶段的一阶局部进度。

## Conflicts

None recorded.

## Open questions

- 接触判定噪声和任务进度不可由单一距离表示时，selector 如何退化或校准？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
