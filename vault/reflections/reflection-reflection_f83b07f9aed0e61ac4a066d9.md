---
id: "reflection_f83b07f9aed0e61ac4a066d9"
type: "reflection"
status: "active"
title: "REAL：非特权感知与意图澄清须进入部署评测"
created_at: "2026-07-22T18:12:22+08:00"
updated_at: "2026-07-22T18:12:22+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["mobile-manipulation", "benchmarking"]
confidence: "medium"
source_ids: ["source_92fed4343c703da77f798f08"]
relations: []
target_ids: ["input_7ee0bdd883c221ff9e62625a", "source_92fed4343c703da77f798f08"]
input_id: "input_7ee0bdd883c221ff9e62625a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "REAL 同时移除模拟器的特权感知 API，并将主动视觉探索和动态用户澄清纳入移动操作任务，因而使部署可行性不再只是离线成功率。"
what_changed: "开放世界评测不能默认对象列表、目标位姿或无歧义指令；这些信息缺口本身构成策略能力与失败来源。"
surprising: "论文报告的实机结果来自特定双臂移动平台与 60 个 episode，说明该评测边界比仅模拟指标更强，但仍不是跨平台保证。"
connections: []
conflicts: []
open_questions: ["如何分解报告探索、澄清、工具执行与物理可达性对每次失败的贡献？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# REAL：非特权感知与意图澄清须进入部署评测

## Why important

REAL 同时移除模拟器的特权感知 API，并将主动视觉探索和动态用户澄清纳入移动操作任务，因而使部署可行性不再只是离线成功率。

## What changed

开放世界评测不能默认对象列表、目标位姿或无歧义指令；这些信息缺口本身构成策略能力与失败来源。

## Surprising

论文报告的实机结果来自特定双臂移动平台与 60 个 episode，说明该评测边界比仅模拟指标更强，但仍不是跨平台保证。

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 如何分解报告探索、澄清、工具执行与物理可达性对每次失败的贡献？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
