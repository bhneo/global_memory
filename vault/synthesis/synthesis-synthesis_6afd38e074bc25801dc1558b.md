---
id: "synthesis_6afd38e074bc25801dc1558b"
type: "synthesis"
status: "active"
title: "世界模型：预测目标、可执行锚点与生成数据门禁"
created_at: "2026-07-29T13:28:56+08:00"
updated_at: "2026-07-29T13:28:56+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["world-models", "predictive-representations", "embodied-generation"]
confidence: "medium"
source_ids: ["source_2d5d59db178b1a20c9213220", "source_61f3045b170e78e4adb2422c", "source_fe986df678d73ef2b6234f0c"]
relations: []
input_reflections: ["reflection_0dd383cc873ce81c0afd3d06", "reflection_3eda5d913d6a736393b8cd9c", "reflection_bfb923cbbf75ed8a49f9df44"]
input_concepts: []
emerging_patterns: ["世界模型至少承担三种不同职责：训练期迁移监督、可执行 latent action 中介、生成式数据引擎；三者的评价门禁不能互换。", "视觉真实或未来变化准确仍不足以证明接触动力学、动作解码和闭环策略收益。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "EGOWAM、WALA 与 U0 都利用未来或生成变化来扩展昂贵机器人动作数据。", "boundary": "共同机制只涉及预测式监督；对控制有益仍需几何、动作、接触和闭环指标逐层验证。", "difference": "EGOWAM比较跨本体 world target，WALA学习可执行 latent action，U0组织多视角生成与数据增广。"}]
unresolved_tensions: ["更抽象的预测目标有利于跨外观迁移，却可能丢失细粒度接触状态。", "更大规模合成数据能扩展覆盖，也可能系统性放大视觉合理但物理错误的轨迹。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["world-models-predictive-representations"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_0dd383cc873ce81c0afd3d06", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment"], "subdirections": ["action-conditioned-prediction", "predictive-model-evaluation-and-failure-detection"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "EGOWAM compares world targets as transfer supervision while holding the policy backbone and data mixture controlled."}, {"reflection_id": "reflection_3eda5d913d6a736393b8cd9c", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment"], "subdirections": ["latent-dynamics", "action-conditioned-prediction"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "WALA learns future semantic and geometric deltas as a latent dynamics target."}, {"reflection_id": "reflection_bfb923cbbf75ed8a49f9df44", "primary_direction": "world-models-predictive-representations", "secondary_directions": [], "subdirections": ["rollout-and-planning-interfaces", "predictive-model-evaluation-and-failure-detection"], "crosscut_dimensions": ["data-and-demonstrations", "system-and-deployment"], "routing_confidence": "high", "reason": "U0 broadens world-model use toward controlled multi-view generation and a synthetic data engine."}]
input_syntheses: ["synthesis_60071a24c6e3071f6731c4e2"]
---

# 世界模型：预测目标、可执行锚点与生成数据门禁

## Emerging patterns

- 世界模型至少承担三种不同职责：训练期迁移监督、可执行 latent action 中介、生成式数据引擎；三者的评价门禁不能互换。
- 视觉真实或未来变化准确仍不足以证明接触动力学、动作解码和闭环策略收益。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "EGOWAM、WALA 与 U0 都利用未来或生成变化来扩展昂贵机器人动作数据。",
    "boundary": "共同机制只涉及预测式监督；对控制有益仍需几何、动作、接触和闭环指标逐层验证。",
    "difference": "EGOWAM比较跨本体 world target，WALA学习可执行 latent action，U0组织多视角生成与数据增广。"
  }
]

## Unresolved tensions

- 更抽象的预测目标有利于跨外观迁移，却可能丢失细粒度接触状态。
- 更大规模合成数据能扩展覆盖，也可能系统性放大视觉合理但物理错误的轨迹。

## Candidate hypotheses

[]

## Possible experiments

None.
