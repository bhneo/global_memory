---
id: "reflection_3ea617cf483f3d85a6aa4d31"
type: "reflection"
status: "active"
title: "Xiaomi-Robotics-1：状态转换语言把可扩展轨迹预训练接到机器人指令"
created_at: "2026-07-21T18:08:33+08:00"
updated_at: "2026-07-21T18:08:33+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "robot-learning"]
confidence: "medium"
source_ids: ["source_5df8ebbcd9bd1afec33d46cc"]
relations: []
target_ids: ["input_04990e3549bb1073a1efb6ff", "source_5df8ebbcd9bd1afec33d46cc"]
input_id: "input_04990e3549bb1073a1efb6ff"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作把大规模 UMI 轨迹的自动状态转换标注与跨本体后训练明确分成两个接口：先学习从观察和目标状态描述生成动作，再对齐真实机器人及人类常用的祈使指令。它为“扩大数据量”提供了可检查的语义桥接，而不是把非机器人轨迹直接等同于可部署机器人示范。"
what_changed: "此前容易把 VLA 扩展理解为只增加遥操作小时数；这里的关键变化是，能扩展的预训练数据需要有与动作结果相连的状态转换语言，且仍需单独处理末端执行器和提示形式的本体差异。"
surprising: "论文报告预训练规模收益会转移到未见环境的后训练真机评估，但这一结果仅适用于其两阶段数据、模型和评测设置，不能替代接触安全或任务特定验证。"
connections: [{"shared_mechanism": "两者都通过结构化数据接口把模型训练连接到可回放的真实机器人评估。", "boundary": "该连接只涉及训练数据语义与评估闭环的衔接，不把一次评测日志变成对跨本体泛化的证据。", "difference": "Xiaomi-Robotics-1处理预训练到后训练的语言和动作本体对齐；真机部署评估闭环强调每次执行的日志、评分和训练反馈。"}]
conflicts: []
open_questions: ["固定长度轨迹的状态转换自动标注在长程任务中何时会丢失对接触前提、失败恢复或子目标顺序的必要约束？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Xiaomi-Robotics-1：状态转换语言把可扩展轨迹预训练接到机器人指令

## Why important

该工作把大规模 UMI 轨迹的自动状态转换标注与跨本体后训练明确分成两个接口：先学习从观察和目标状态描述生成动作，再对齐真实机器人及人类常用的祈使指令。它为“扩大数据量”提供了可检查的语义桥接，而不是把非机器人轨迹直接等同于可部署机器人示范。

## What changed

此前容易把 VLA 扩展理解为只增加遥操作小时数；这里的关键变化是，能扩展的预训练数据需要有与动作结果相连的状态转换语言，且仍需单独处理末端执行器和提示形式的本体差异。

## Surprising

论文报告预训练规模收益会转移到未见环境的后训练真机评估，但这一结果仅适用于其两阶段数据、模型和评测设置，不能替代接触安全或任务特定验证。

## Connections

- Shared mechanism: 两者都通过结构化数据接口把模型训练连接到可回放的真实机器人评估。
  Boundary: 该连接只涉及训练数据语义与评估闭环的衔接，不把一次评测日志变成对跨本体泛化的证据。
  Difference: Xiaomi-Robotics-1处理预训练到后训练的语言和动作本体对齐；真机部署评估闭环强调每次执行的日志、评分和训练反馈。

## Conflicts

None recorded.

## Open questions

- 固定长度轨迹的状态转换自动标注在长程任务中何时会丢失对接触前提、失败恢复或子目标顺序的必要约束？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
