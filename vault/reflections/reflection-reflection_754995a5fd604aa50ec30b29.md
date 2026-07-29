---
id: "reflection_754995a5fd604aa50ec30b29"
type: "reflection"
status: "active"
title: "DriftWorld：世界模型的控制价值受 rollout 吞吐量约束"
created_at: "2026-07-24T18:05:59+08:00"
updated_at: "2026-07-24T18:05:59+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["world-modeling", "robot-planning"]
confidence: "medium"
source_ids: ["source_ce00fba8d7127c890fdcc46e"]
relations: []
target_ids: ["input_9e8df5db2286bbf5351f2dfe", "source_ce00fba8d7127c890fdcc46e"]
input_id: "input_9e8df5db2286bbf5351f2dfe"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "DriftWorld 将动作条件未来帧生成从迭代去噪改为一次前向生成，直接针对候选动作搜索需要大量 rollout 的推理瓶颈；它把世界模型评价从单帧保真扩展到能否支持实时决策。"
what_changed: "世界模型速度不只是工程优化；当采样速度限制候选动作数量时，生成吞吐量会改变规划和离线策略排序是否可实际使用。"
surprising: ""
connections: []
conflicts: []
open_questions: ["单步高速生成在长时程接触、遮挡和分布外动作下的误差累积，何时会抵消其增加候选 rollout 数量带来的决策收益？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# DriftWorld：世界模型的控制价值受 rollout 吞吐量约束

## Why important

DriftWorld 将动作条件未来帧生成从迭代去噪改为一次前向生成，直接针对候选动作搜索需要大量 rollout 的推理瓶颈；它把世界模型评价从单帧保真扩展到能否支持实时决策。

## What changed

世界模型速度不只是工程优化；当采样速度限制候选动作数量时，生成吞吐量会改变规划和离线策略排序是否可实际使用。

## Surprising

Not stated.

## Connections

None recorded.

## Conflicts

None recorded.

## Open questions

- 单步高速生成在长时程接触、遮挡和分布外动作下的误差累积，何时会抵消其增加候选 rollout 数量带来的决策收益？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
