---
id: "synthesis_2cb5cbca9beef026f0c2b54e"
type: "synthesis"
status: "active"
title: "强化学习后训练：探索分布、信用时标与先验保持接口"
created_at: "2026-07-29T13:30:46+08:00"
updated_at: "2026-07-29T13:30:46+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["reinforcement-learning", "vla-posttraining", "robot-learning"]
confidence: "medium"
source_ids: ["source_5b8c57a9bef3348109f3b7bb", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_f9128ff3463cfaa7fa41ee7e"]
relations: []
input_reflections: ["reflection_305130038ee9fd3cb9e18ec4", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_cb246940931502d077f687f5", "reflection_cd269bee56819aafec2fd5a3"]
input_concepts: []
emerging_patterns: ["VLA-RL 的样本效率由至少三个接口共同决定：探索看见哪些行为模式，奖励怎样表示进展与失败，信用分配是否与策略的一次决策单位对齐。", "保留预训练先验可以通过条件 token、块级 KL 或生成潜变量实现，但所有方式都受基础策略支持域限制。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "ExToken、PAC-ACT 与 FlowDAgger 都把在线适配压力限制在小于基础策略的接口。", "boundary": "示范 token、动作块 actor-critic 和人类纠正 latent 的监督来源与时间尺度不同，不能直接拼接或按同一指标比较。", "difference": "三者分别改变 rollout 分布、块级优化单位和部署纠正位置。"}]
unresolved_tensions: ["强先验减少危险探索，也可能阻止策略跨出原支持集寻找必要的新行为。", "稠密模型奖励改善信用分配，同时扩大 reward hacking 与合成失败覆盖偏差的风险。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["reinforcement-learning-policy-posttraining"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_305130038ee9fd3cb9e18ec4", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": [], "subdirections": ["exploration", "support-domain-constraints"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "ExToken changes the rollout distribution using discrete behavior priors derived from demonstrations."}, {"reflection_id": "reflection_cb246940931502d077f687f5", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": ["value-reward-progress-uncertainty"], "subdirections": ["online-and-real-robot-rl", "safety-and-support-domain-constraints"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "DenseReward changes RL credit through per-timestep progress trained on synthesized physical failures."}, {"reflection_id": "reflection_c0693ad0e6abf8397dbdfd87", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": ["motion-control-execution-interfaces"], "subdirections": ["actor-critic-or-token-level-adaptation", "safety-and-support-domain-constraints"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "PAC-ACT aligns actor-critic credit and behavior constraints with action-chunk decisions."}, {"reflection_id": "reflection_cd269bee56819aafec2fd5a3", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": [], "subdirections": ["residual-and-parameter-efficient-updates", "support-domain-constraints"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "FlowDAgger places human correction in a low-dimensional latent interface around a frozen generative policy."}]
input_syntheses: ["synthesis_1e641e385fe894f21693e284"]
---

# 强化学习后训练：探索分布、信用时标与先验保持接口

## Emerging patterns

- VLA-RL 的样本效率由至少三个接口共同决定：探索看见哪些行为模式，奖励怎样表示进展与失败，信用分配是否与策略的一次决策单位对齐。
- 保留预训练先验可以通过条件 token、块级 KL 或生成潜变量实现，但所有方式都受基础策略支持域限制。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "ExToken、PAC-ACT 与 FlowDAgger 都把在线适配压力限制在小于基础策略的接口。",
    "boundary": "示范 token、动作块 actor-critic 和人类纠正 latent 的监督来源与时间尺度不同，不能直接拼接或按同一指标比较。",
    "difference": "三者分别改变 rollout 分布、块级优化单位和部署纠正位置。"
  }
]

## Unresolved tensions

- 强先验减少危险探索，也可能阻止策略跨出原支持集寻找必要的新行为。
- 稠密模型奖励改善信用分配，同时扩大 reward hacking 与合成失败覆盖偏差的风险。

## Candidate hypotheses

[]

## Possible experiments

None.
