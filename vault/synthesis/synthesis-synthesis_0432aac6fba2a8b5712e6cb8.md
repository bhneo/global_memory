---
id: "synthesis_0432aac6fba2a8b5712e6cb8"
type: "synthesis"
status: "active"
title: "VLA：表征泛化、预测监督与可执行动作锚点"
created_at: "2026-07-29T13:26:57+08:00"
updated_at: "2026-07-29T13:26:57+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["vla", "cross-embodiment", "representation-learning"]
confidence: "medium"
source_ids: ["source_2d5d59db178b1a20c9213220", "source_3093a2f57587e962f87d6277", "source_61f3045b170e78e4adb2422c"]
relations: []
input_reflections: ["reflection_051f1a0f00d5131171df1440", "reflection_0dd383cc873ce81c0afd3d06", "reflection_3eda5d913d6a736393b8cd9c"]
input_concepts: []
emerging_patterns: ["VLA 的表征泛化与动作泛化必须分开评估：聚焦正确对象或预测正确世界变化，不自动产生跨本体可执行动作。", "人类视频迁移需要一个由机器人数据锚定的中介；未来语义—几何变化可减少外观纠缠，但仍需动作监督和控制约束。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Pelican、EGOWAM 与 WALA 都在端到端视觉到动作链中隔离任务相关表征和本体相关执行。", "boundary": "注意力、世界预测目标与 latent action 不是可互换模块；其证据任务和失效条件不同。", "difference": "Pelican 诊断注意力到动作的落差，EGOWAM改变人类数据的训练监督，WALA用机器人动作把预测中介锚定到执行。"}]
unresolved_tensions: ["压缩和本体不变性促进迁移，却可能丢失接触、动力学和硬件极限所需细节。", "视觉预测越容易从无动作视频扩展，越需要独立证明其可执行性而非仅重建质量。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["vla-architecture-pretraining-cross-embodiment"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_051f1a0f00d5131171df1440", "primary_direction": "vla-architecture-pretraining-cross-embodiment", "secondary_directions": [], "subdirections": ["backbone-and-multimodal-fusion", "capability-and-scaling-evaluation"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "Pelican separates attention-level representation transfer from action-level generalization."}, {"reflection_id": "reflection_0dd383cc873ce81c0afd3d06", "primary_direction": "vla-architecture-pretraining-cross-embodiment", "secondary_directions": ["world-models-predictive-representations"], "subdirections": ["pretraining-objectives", "embodiment-and-action-space-alignment"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "EGOWAM asks which predictive target best transfers human egocentric data into robot policies."}, {"reflection_id": "reflection_3eda5d913d6a736393b8cd9c", "primary_direction": "vla-architecture-pretraining-cross-embodiment", "secondary_directions": ["world-models-predictive-representations"], "subdirections": ["action-tokenization-and-decoding", "transfer-and-adaptation-interfaces"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "WALA uses future semantic-geometric change plus robot actions to anchor an executable latent action interface."}]
input_syntheses: ["synthesis_77d12a9c578c8e5a6223bff4"]
---

# VLA：表征泛化、预测监督与可执行动作锚点

## Emerging patterns

- VLA 的表征泛化与动作泛化必须分开评估：聚焦正确对象或预测正确世界变化，不自动产生跨本体可执行动作。
- 人类视频迁移需要一个由机器人数据锚定的中介；未来语义—几何变化可减少外观纠缠，但仍需动作监督和控制约束。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Pelican、EGOWAM 与 WALA 都在端到端视觉到动作链中隔离任务相关表征和本体相关执行。",
    "boundary": "注意力、世界预测目标与 latent action 不是可互换模块；其证据任务和失效条件不同。",
    "difference": "Pelican 诊断注意力到动作的落差，EGOWAM改变人类数据的训练监督，WALA用机器人动作把预测中介锚定到执行。"
  }
]

## Unresolved tensions

- 压缩和本体不变性促进迁移，却可能丢失接触、动力学和硬件极限所需细节。
- 视觉预测越容易从无动作视频扩展，越需要独立证明其可执行性而非仅重建质量。

## Candidate hypotheses

[]

## Possible experiments

None.
