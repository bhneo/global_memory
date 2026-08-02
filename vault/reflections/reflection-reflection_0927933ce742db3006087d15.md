---
id: "reflection_0927933ce742db3006087d15"
type: "reflection"
status: "active"
title: "机器人能力演化需要把经验成熟度编译成不同执行层，而不只是持续微调同一策略"
created_at: "2026-08-02T12:14:55+08:00"
updated_at: "2026-08-02T12:14:55+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "embodied-agents", "capability-learning", "policy-orchestration"]
confidence: "high"
source_ids: ["source_d0908c8e9c58809dd2665c1e"]
relations: []
target_ids: ["input_74d991d028e707dbdc21ee6e", "source_d0908c8e9c58809dd2665c1e"]
input_id: "input_74d991d028e707dbdc21ee6e"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "HERO 把零样本启发式执行、一次经验的几何迁移和由重复经验训练出的闭环 visuomotor policy 组织成可演化能力层级，并让同一 orchestrator 同时负责数据积累与部署回退。它将能力成熟度变成可显式调度的系统状态。"
what_changed: "此前能力编排容易被看作对一组静态策略做任务路由；该论文进一步表明，编排器可以把成功经验从昂贵推理逐步转化为可复用轨迹，再编译为低延迟闭环策略，并在部署时反向按成熟度回退。"
surprising: "HERO 的数据演化采用 H→E→R，而部署采用 R→E→H；训练与执行沿同一能力谱反向流动，使快速已学能力优先，同时保留经验迁移和从头推理作为恢复路径。"
connections: [{"shared_mechanism": "都通过高层 orchestrator 在异构机器人能力之间路由，并显式处理失败与交接。", "boundary": "RoboHarness 主要估计静态策略的能力边界与状态分布交接；HERO 还让成功经验随重复使用从启发式执行演化为 exemplar，再训练为 reflexive policy。", "difference": "前者强调未经联合训练策略之间的输入状态可达性，后者强调经验成熟度驱动的能力创建、编译和反向回退。"}]
conflicts: []
open_questions: ["如何在不依赖人工定义 primitive skill space 的前提下发现新能力层，并防止错误的成功判定被编译进 reflexive policy？"]
possible_mechanisms: ["成功执行先进入 exemplar library，经复用扩展覆盖并降低采集成本；高频重复经验经过筛选后训练闭环策略，部署则按 policy 可用性和失败反馈逐级回退。"]
future_directions: ["将能力覆盖、交接可达性、验证误差和编译收益纳入统一的路由置信度与回滚协议。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 机器人能力演化需要把经验成熟度编译成不同执行层，而不只是持续微调同一策略

## Why important

HERO 把零样本启发式执行、一次经验的几何迁移和由重复经验训练出的闭环 visuomotor policy 组织成可演化能力层级，并让同一 orchestrator 同时负责数据积累与部署回退。它将能力成熟度变成可显式调度的系统状态。

## What changed

此前能力编排容易被看作对一组静态策略做任务路由；该论文进一步表明，编排器可以把成功经验从昂贵推理逐步转化为可复用轨迹，再编译为低延迟闭环策略，并在部署时反向按成熟度回退。

## Surprising

HERO 的数据演化采用 H→E→R，而部署采用 R→E→H；训练与执行沿同一能力谱反向流动，使快速已学能力优先，同时保留经验迁移和从头推理作为恢复路径。

## Connections

- Shared mechanism: 都通过高层 orchestrator 在异构机器人能力之间路由，并显式处理失败与交接。
  Boundary: RoboHarness 主要估计静态策略的能力边界与状态分布交接；HERO 还让成功经验随重复使用从启发式执行演化为 exemplar，再训练为 reflexive policy。
  Difference: 前者强调未经联合训练策略之间的输入状态可达性，后者强调经验成熟度驱动的能力创建、编译和反向回退。

## Conflicts

None recorded.

## Open questions

- 如何在不依赖人工定义 primitive skill space 的前提下发现新能力层，并防止错误的成功判定被编译进 reflexive policy？

## Possible mechanisms

- 成功执行先进入 exemplar library，经复用扩展覆盖并降低采集成本；高频重复经验经过筛选后训练闭环策略，部署则按 policy 可用性和失败反馈逐级回退。

## Future directions

- 将能力覆盖、交接可达性、验证误差和编译收益纳入统一的路由置信度与回滚协议。
