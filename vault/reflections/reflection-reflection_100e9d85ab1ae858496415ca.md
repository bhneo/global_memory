---
id: "reflection_100e9d85ab1ae858496415ca"
type: "reflection"
status: "active"
title: "接触丰富操作：把数据密度限定在关键阶段"
created_at: "2026-07-22T18:11:47+08:00"
updated_at: "2026-07-22T18:11:47+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["contact-rich-manipulation", "robot-learning"]
confidence: "medium"
source_ids: ["source_42e52a18cc082f3af087d574"]
relations: []
target_ids: ["input_4bec3f6febe9fd2b5e3f75e5", "source_42e52a18cc082f3af087d574"]
input_id: "input_4bec3f6febe9fd2b5e3f75e5"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作将高精度操作的数据需求按任务阶段划分：自由空间运动使用传统规划，接触关键段才以自动采集数据和离线强化学习优化，从而把数据预算与主要失败机制对齐。"
what_changed: "不应把端到端数据规模视作所有阶段同样受益；接触状态转换可能是需要高密度数据的局部瓶颈。"
surprising: "作者在四项实机任务中报告以 2–2.5 小时自主数据获得较高成功率，但这一结果受其任务、自动采集方案和离线 RL 设置约束。"
connections: []
conflicts: []
open_questions: ["关键接触段在未建模的新任务中能否可靠识别，而不遗漏决定成功的过渡状态？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 接触丰富操作：把数据密度限定在关键阶段

## Why important

该工作将高精度操作的数据需求按任务阶段划分：自由空间运动使用传统规划，接触关键段才以自动采集数据和离线强化学习优化，从而把数据预算与主要失败机制对齐。

## What changed

不应把端到端数据规模视作所有阶段同样受益；接触状态转换可能是需要高密度数据的局部瓶颈。

## Surprising

作者在四项实机任务中报告以 2–2.5 小时自主数据获得较高成功率，但这一结果受其任务、自动采集方案和离线 RL 设置约束。

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 关键接触段在未建模的新任务中能否可靠识别，而不遗漏决定成功的过渡状态？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
