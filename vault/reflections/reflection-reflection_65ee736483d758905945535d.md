---
id: "reflection_65ee736483d758905945535d"
type: "reflection"
status: "active"
title: "NativeMEM：让记忆表征服从冻结 VLA 的动作接口"
created_at: "2026-07-21T17:40:37+08:00"
updated_at: "2026-07-21T17:40:37+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "agent-memory", "long-horizon-manipulation"]
confidence: "medium"
source_ids: ["source_748cef2215ddc958568e6368"]
relations: []
target_ids: ["input_006e6583a9db3471eff61a27", "source_748cef2215ddc958568e6368"]
input_id: "input_006e6583a9db3471eff61a27"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它把长时记忆的瓶颈从外部存储容量转为与既有动作策略的表示兼容性：每个帧—视角只保留一个 token，但用冻结 VLA 的原动作损失训练该 token。"
what_changed: "长时视觉记忆不一定需要独立记忆模型；在该设定中，冻结策略反而构成迫使压缩分支保留动作相关信息的训练约束。"
surprising: "作者报告单 token/帧仍可在 32GB 内保留 5000 帧，并在所测任务中把模拟平均成功率由 Mem-0 的 32.4% 提至 84.0%；这是特定 π0.5、任务和复现基线下的结果。"
connections: [{"shared_mechanism": "都通过冻结基础 VLA 限定新增模块的职责。", "boundary": "这里只比较能力扩展接口，不把记忆 token 等同于高层技能编排。", "difference": "NativeMEM 把历史观测压入 VLA 原生 token；非对称技能编排在 VLA 外部管理重试、验证和运输。"}]
conflicts: []
open_questions: ["单 token 压缩在遮挡、多对象身份交换和失败恢复中会丢失哪些不可恢复信息？"]
possible_mechanisms: ["冻结动作头使梯度只能把历史中有助于动作预测的线索写入记忆 token。"]
future_directions: ["在跨机器人、不同 VLA token 空间和真实长时干扰下测试记忆容量与失真。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# NativeMEM：让记忆表征服从冻结 VLA 的动作接口

## Why important

它把长时记忆的瓶颈从外部存储容量转为与既有动作策略的表示兼容性：每个帧—视角只保留一个 token，但用冻结 VLA 的原动作损失训练该 token。

## What changed

长时视觉记忆不一定需要独立记忆模型；在该设定中，冻结策略反而构成迫使压缩分支保留动作相关信息的训练约束。

## Surprising

作者报告单 token/帧仍可在 32GB 内保留 5000 帧，并在所测任务中把模拟平均成功率由 Mem-0 的 32.4% 提至 84.0%；这是特定 π0.5、任务和复现基线下的结果。

## Connections

- Shared mechanism: 都通过冻结基础 VLA 限定新增模块的职责。
  Boundary: 这里只比较能力扩展接口，不把记忆 token 等同于高层技能编排。
  Difference: NativeMEM 把历史观测压入 VLA 原生 token；非对称技能编排在 VLA 外部管理重试、验证和运输。

## Conflicts

None recorded.

## Open questions

- 单 token 压缩在遮挡、多对象身份交换和失败恢复中会丢失哪些不可恢复信息？

## Possible mechanisms

- 冻结动作头使梯度只能把历史中有助于动作预测的线索写入记忆 token。

## Future directions

- 在跨机器人、不同 VLA token 空间和真实长时干扰下测试记忆容量与失真。
