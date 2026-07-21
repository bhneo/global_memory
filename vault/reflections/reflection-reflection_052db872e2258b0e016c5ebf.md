---
id: "reflection_052db872e2258b0e016c5ebf"
type: "reflection"
status: "active"
title: "UR-VC：先纠正进度代理，再训练价值或优势条件策略"
created_at: "2026-07-20T11:53:47+08:00"
updated_at: "2026-07-20T11:53:47+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "value-learning", "progress-estimation", "offline-data"]
confidence: "high"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: []
target_ids: ["input_3534465a5a2e8ab09b743126", "source_e326446389e083c6ba9c94c2"]
input_id: "input_3534465a5a2e8ab09b743126"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它指出成功示范中的归一化时间并不等于物理进度，尤其接触和可变形物体任务会倒退、停滞或速度不均；错误代理会污染后续价值与优势监督。"
what_changed: "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。"
surprising: "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。"
connections: [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}]
conflicts: ["跨轨迹视觉相似不一定意味着任务状态或接触状态相同，检索偏差可能以另一种形式替代时间偏差。"]
open_questions: ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？"]
possible_mechanisms: ["跨轨迹匹配近似固定物理状态并平均各轨迹的时间扭曲，从而估计该状态通常位于任务的哪个阶段。"]
future_directions: ["把跨轨迹一致性、接触观测和价值不确定性结合为进度标签的置信区间。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# UR-VC：先纠正进度代理，再训练价值或优势条件策略

## Why important

它指出成功示范中的归一化时间并不等于物理进度，尤其接触和可变形物体任务会倒退、停滞或速度不均；错误代理会污染后续价值与优势监督。

## What changed

价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。

## Surprising

UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。

## Connections

- Shared mechanism: 与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。
  Boundary: UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。
  Difference: UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。

## Conflicts

- 跨轨迹视觉相似不一定意味着任务状态或接触状态相同，检索偏差可能以另一种形式替代时间偏差。

## Open questions

- 如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？

## Possible mechanisms

- 跨轨迹匹配近似固定物理状态并平均各轨迹的时间扭曲，从而估计该状态通常位于任务的哪个阶段。

## Future directions

- 把跨轨迹一致性、接触观测和价值不确定性结合为进度标签的置信区间。
