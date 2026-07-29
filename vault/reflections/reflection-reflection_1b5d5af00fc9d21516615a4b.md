---
id: "reflection_1b5d5af00fc9d21516615a4b"
type: "reflection"
status: "active"
title: "Scaling BFM：行为规模同时取决于 rollout 数量与参考动作多样性"
created_at: "2026-07-21T18:09:01+08:00"
updated_at: "2026-07-21T18:09:01+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["humanoid-robotics", "reinforcement-learning", "behavior-foundation-models"]
confidence: "medium"
source_ids: ["source_46f82af34b1ace2c5c0483af"]
relations: []
target_ids: ["input_3fcb4a20dc48656f262a500a", "source_46f82af34b1ace2c5c0483af"]
input_id: "input_3fcb4a20dc48656f262a500a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该论文将人形行为基础模型的“数据规模”拆开：PPO中的有效样本量由在线rollout决定，参考动作库主要塑造行为分布多样性。这个区分避免把更多动作片段误当作等价的训练规模。"
what_changed: "此前容易按参考动作数量衡量人形预训练规模；这里应分别追踪并调节在线交互数量、参考动作多样性、全局运动跟踪接口和模型表达能力。"
surprising: "论文将全局坐标系整体轨迹跟踪作为减少行为歧义的统一接口，但这并不意味着局部控制或不同根状态估计下必然获得同样优势。"
connections: [{"shared_mechanism": "两者都以共享的行为表示替代每个任务单独设计奖励或控制逻辑。", "boundary": "连接只适用于行为基础模型的训练与控制接口，不把参考运动跟踪等同于真实任务成功。", "difference": "Scaling BFM讨论人形全身运动的rollout数量和参考分布；跨本体VLA两阶段训练讨论状态转换语言和机器人指令对齐。"}]
conflicts: []
open_questions: ["当参考动作覆盖增加但在线rollout预算固定时，如何检测新增多样性是提高泛化还是稀释关键接触和恢复行为？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Scaling BFM：行为规模同时取决于 rollout 数量与参考动作多样性

## Why important

该论文将人形行为基础模型的“数据规模”拆开：PPO中的有效样本量由在线rollout决定，参考动作库主要塑造行为分布多样性。这个区分避免把更多动作片段误当作等价的训练规模。

## What changed

此前容易按参考动作数量衡量人形预训练规模；这里应分别追踪并调节在线交互数量、参考动作多样性、全局运动跟踪接口和模型表达能力。

## Surprising

论文将全局坐标系整体轨迹跟踪作为减少行为歧义的统一接口，但这并不意味着局部控制或不同根状态估计下必然获得同样优势。

## Connections

- Shared mechanism: 两者都以共享的行为表示替代每个任务单独设计奖励或控制逻辑。
  Boundary: 连接只适用于行为基础模型的训练与控制接口，不把参考运动跟踪等同于真实任务成功。
  Difference: Scaling BFM讨论人形全身运动的rollout数量和参考分布；跨本体VLA两阶段训练讨论状态转换语言和机器人指令对齐。

## Conflicts

None recorded.

## Open questions

- 当参考动作覆盖增加但在线rollout预算固定时，如何检测新增多样性是提高泛化还是稀释关键接触和恢复行为？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
