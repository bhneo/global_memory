---
id: "reflection_1f4ab26f44d5ff91048664cc"
type: "reflection"
status: "active"
title: "χ0：长时程鲁棒性需要区分训练、模型与部署分布"
created_at: "2026-07-23T18:06:44+08:00"
updated_at: "2026-07-23T18:06:44+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robot-learning", "robust-manipulation"]
confidence: "medium"
source_ids: ["source_cdce2dfd2021019fc46a9ea7"]
relations: []
target_ids: ["input_838840aa96c39450e2eabd67", "source_cdce2dfd2021019fc46a9ea7"]
input_id: "input_838840aa96c39450e2eabd67"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该论文把长时程操作的失稳归为演示训练分布、策略归纳偏置和实际执行轨迹之间的不同失配，并分别提出权重合并、阶段优势和训练—部署对齐；它为诊断失败提供了比单一成功率更具体的分层位置。"
what_changed: "资源规模不是部署鲁棒性的唯一解释变量；同一策略可能在训练数据覆盖、动作采样和执行时延三个边界上分别失配。"
surprising: ""
connections: [{"shared_mechanism": "两者都把实机执行反馈视为训练闭环中需要显式建模的分布来源。", "boundary": "该连接只适用于将训练策略部署到有时延和扰动的物理系统，不证明特定对齐模块可迁移到所有机器人或任务。", "difference": "χ0 将失配细分为训练、模型和部署三种分布；既有实机迭代概念强调采集—训练—验证循环的操作流程。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# χ0：长时程鲁棒性需要区分训练、模型与部署分布

## Why important

该论文把长时程操作的失稳归为演示训练分布、策略归纳偏置和实际执行轨迹之间的不同失配，并分别提出权重合并、阶段优势和训练—部署对齐；它为诊断失败提供了比单一成功率更具体的分层位置。

## What changed

资源规模不是部署鲁棒性的唯一解释变量；同一策略可能在训练数据覆盖、动作采样和执行时延三个边界上分别失配。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都把实机执行反馈视为训练闭环中需要显式建模的分布来源。
  Boundary: 该连接只适用于将训练策略部署到有时延和扰动的物理系统，不证明特定对齐模块可迁移到所有机器人或任务。
  Difference: χ0 将失配细分为训练、模型和部署三种分布；既有实机迭代概念强调采集—训练—验证循环的操作流程。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
