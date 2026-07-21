---
id: "reflection_91f2ffd2085e86802850ad17"
type: "reflection"
status: "active"
title: "ACT 的隐式力线索：遥操作跟踪误差可能是接触状态的替代观测"
created_at: "2026-07-20T18:05:36+08:00"
updated_at: "2026-07-20T18:05:36+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "contact-manipulation", "imitation-learning"]
confidence: "medium"
source_ids: ["source_158b4743a3d4e973913f8bbf"]
relations: []
target_ids: ["input_034a10c98f14b19b2c4826e7", "source_158b4743a3d4e973913f8bbf"]
input_id: "input_034a10c98f14b19b2c4826e7"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该受控消融指出，leader–follower 遥操作中的命令—执行偏差会泄露接触、阻力和约束违反信息；这使示范采集接口成为策略观测定义的一部分，而非中性的离线数据来源。"
what_changed: "此前容易将 ACT 的接触能力归因于动作分块架构；这里提示必须区分架构能力与遥操作管线暗中提供的交互线索。"
surprising: ""
connections: [{"shared_mechanism": "两者都试图让策略保留对接触形成、阻力和安全约束敏感的状态。", "boundary": "该连接不假定电机电流或力矩 proxy 等同于真实六维力/力矩测量。", "difference": "触觉对齐的人到机器人接触迁移用显式压力和接触结构作为监督；本文比较遥操作误差这一隐式线索与由机载测量导出的力矩 proxy。"}]
conflicts: []
open_questions: ["不同控制器增益、摩擦补偿和传感噪声下，何时力矩 proxy 足以替代遥操作误差信号？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# ACT 的隐式力线索：遥操作跟踪误差可能是接触状态的替代观测

## Why important

该受控消融指出，leader–follower 遥操作中的命令—执行偏差会泄露接触、阻力和约束违反信息；这使示范采集接口成为策略观测定义的一部分，而非中性的离线数据来源。

## What changed

此前容易将 ACT 的接触能力归因于动作分块架构；这里提示必须区分架构能力与遥操作管线暗中提供的交互线索。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都试图让策略保留对接触形成、阻力和安全约束敏感的状态。
  Boundary: 该连接不假定电机电流或力矩 proxy 等同于真实六维力/力矩测量。
  Difference: 触觉对齐的人到机器人接触迁移用显式压力和接触结构作为监督；本文比较遥操作误差这一隐式线索与由机载测量导出的力矩 proxy。

## Conflicts

None recorded.

## Open questions

- 不同控制器增益、摩擦补偿和传感噪声下，何时力矩 proxy 足以替代遥操作误差信号？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
