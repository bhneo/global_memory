---
id: "reflection_cb246940931502d077f687f5"
type: "reflection"
status: "active"
title: "DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配"
created_at: "2026-07-20T12:27:33+08:00"
updated_at: "2026-07-20T12:27:33+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-rl", "reward-modeling", "failure-data", "credit-assignment"]
confidence: "high"
source_ids: ["source_f9128ff3463cfaa7fa41ee7e"]
relations: []
target_ids: ["input_916597fd1db065ff715631b8", "source_f9128ff3463cfaa7fa41ee7e"]
input_id: "input_916597fd1db065ff715631b8"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "DenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。"
what_changed: "此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。"
surprising: "两帧历史优于一帧，而三帧又略差，提示奖励估计既需要时间上下文，也会受到冗余或噪声历史的影响。"
connections: [{"shared_mechanism": "与 VLA 动作评估蒸馏都学习一个轻量评估信号，为原策略的候选动作或后训练提供长期结果信息。", "boundary": "DenseReward 依赖仿真中的阶段标签和定向扰动，论文只证明其所选操作任务上的奖励预测与下游指导效果；合成失败分布仍可能遗漏真机罕见故障。", "difference": "动作评估蒸馏从仿真树搜索回报学习候选动作 Q 值；DenseReward 从视觉历史和语言预测逐时刻进度，并显式训练多类失败轨迹。"}]
conflicts: ["更密集的模型奖励改善信用分配，但奖励模型偏差也会被策略优化主动利用，形成 reward hacking。"]
open_questions: ["合成失败与真实失败的分布差异应如何检测，并在策略开始利用奖励漏洞前触发人工或真机校准？"]
possible_mechanisms: ["阶段感知标签提供连续任务进度，定向扰动补齐成功示范没有覆盖的错误转移，短历史窗口帮助区分静态相似但趋势不同的状态。"]
future_directions: ["在长时程、工具使用和恢复任务上联合评估失败覆盖、奖励校准、策略收益与 reward hacking。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配

## Why important

DenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。

## What changed

此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。

## Surprising

两帧历史优于一帧，而三帧又略差，提示奖励估计既需要时间上下文，也会受到冗余或噪声历史的影响。

## Connections

- Shared mechanism: 与 VLA 动作评估蒸馏都学习一个轻量评估信号，为原策略的候选动作或后训练提供长期结果信息。
  Boundary: DenseReward 依赖仿真中的阶段标签和定向扰动，论文只证明其所选操作任务上的奖励预测与下游指导效果；合成失败分布仍可能遗漏真机罕见故障。
  Difference: 动作评估蒸馏从仿真树搜索回报学习候选动作 Q 值；DenseReward 从视觉历史和语言预测逐时刻进度，并显式训练多类失败轨迹。

## Conflicts

- 更密集的模型奖励改善信用分配，但奖励模型偏差也会被策略优化主动利用，形成 reward hacking。

## Open questions

- 合成失败与真实失败的分布差异应如何检测，并在策略开始利用奖励漏洞前触发人工或真机校准？

## Possible mechanisms

- 阶段感知标签提供连续任务进度，定向扰动补齐成功示范没有覆盖的错误转移，短历史窗口帮助区分静态相似但趋势不同的状态。

## Future directions

- 在长时程、工具使用和恢复任务上联合评估失败覆盖、奖励校准、策略收益与 reward hacking。
