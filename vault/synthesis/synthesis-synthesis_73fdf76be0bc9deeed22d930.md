---
id: "synthesis_73fdf76be0bc9deeed22d930"
type: "synthesis"
status: "active"
title: "价值信号：进度代理、失败覆盖与可优化读出"
created_at: "2026-07-29T13:33:57+08:00"
updated_at: "2026-07-29T13:33:57+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["value-learning", "reward-modeling", "progress-estimation"]
confidence: "medium"
source_ids: ["source_40700e61702f4b5a5765e11d", "source_e326446389e083c6ba9c94c2", "source_f9128ff3463cfaa7fa41ee7e"]
relations: []
input_reflections: ["reflection_052db872e2258b0e016c5ebf", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cb246940931502d077f687f5"]
input_concepts: []
emerging_patterns: ["价值信号的上游质量与估计器容量同样关键：时间标签可能与物理进度错位，训练集也可能缺少碰撞、掉落、漏抓和恢复等失败机制。", "紧凑价值读出提高在线样本效率，却可能隐藏接触状态、历史歧义和阶段切换所需信息。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "UR-VC、RL Token 与 DenseReward 都在策略更新之前治理进度或价值接口。", "boundary": "标签校正、表征读出和奖励模型属于不同层；任一层改进不能证明另两层可靠。", "difference": "UR-VC无训练地校正离线代理，RL Token为 actor-critic 压缩状态，DenseReward从失败覆盖数据学习逐时刻奖励。"}]
unresolved_tensions: ["更稠密的反馈改善信用分配，也为策略利用系统性偏差创造更大空间。", "跨轨迹视觉相似可能不等于相同接触状态，校正后的进度仍需物理验证。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["value-reward-progress-uncertainty"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_052db872e2258b0e016c5ebf", "primary_direction": "value-reward-progress-uncertainty", "secondary_directions": [], "subdirections": ["progress-calibration", "value-estimation"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "UR-VC directly corrects the common but biased assumption that demonstration time equals physical progress."}, {"reflection_id": "reflection_5b4f45d757e5b256cdddfcfa", "primary_direction": "value-reward-progress-uncertainty", "secondary_directions": ["reinforcement-learning-policy-posttraining"], "subdirections": ["value-estimation", "uncertainty-and-confidence"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "medium", "reason": "RL Token exposes a compact state representation to actor-critic value learning, while leaving its information sufficiency open."}, {"reflection_id": "reflection_cb246940931502d077f687f5", "primary_direction": "value-reward-progress-uncertainty", "secondary_directions": ["reinforcement-learning-policy-posttraining"], "subdirections": ["reward-design", "progress-calibration", "quality-and-success-signals"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "DenseReward ties per-timestep progress supervision to explicit physical failure coverage."}]
input_syntheses: ["synthesis_be18972801786224075196eb"]
---

# 价值信号：进度代理、失败覆盖与可优化读出

## Emerging patterns

- 价值信号的上游质量与估计器容量同样关键：时间标签可能与物理进度错位，训练集也可能缺少碰撞、掉落、漏抓和恢复等失败机制。
- 紧凑价值读出提高在线样本效率，却可能隐藏接触状态、历史歧义和阶段切换所需信息。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "UR-VC、RL Token 与 DenseReward 都在策略更新之前治理进度或价值接口。",
    "boundary": "标签校正、表征读出和奖励模型属于不同层；任一层改进不能证明另两层可靠。",
    "difference": "UR-VC无训练地校正离线代理，RL Token为 actor-critic 压缩状态，DenseReward从失败覆盖数据学习逐时刻奖励。"
  }
]

## Unresolved tensions

- 更稠密的反馈改善信用分配，也为策略利用系统性偏差创造更大空间。
- 跨轨迹视觉相似可能不等于相同接触状态，校正后的进度仍需物理验证。

## Candidate hypotheses

[]

## Possible experiments

None.
