---
id: "synthesis_6d38cdbcd8bf8ebf9b15b342"
type: "synthesis"
status: "active"
title: "运动控制：动作几何、执行时标与快慢反馈交接"
created_at: "2026-07-29T13:35:12+08:00"
updated_at: "2026-07-29T13:35:12+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["motion-control", "action-representation", "execution-interfaces"]
confidence: "medium"
source_ids: ["source_283911da72edc403d1b823fb", "source_34d6513b0522739d0b25e303", "source_4b25f596c34869693b9b8151"]
relations: []
input_reflections: ["reflection_0078f804e87c7ed12f88876d", "reflection_0db16c2a58084d442087245e", "reflection_c5765c32f1c3dd7302da4906"]
input_concepts: []
emerging_patterns: ["动作接口至少要声明轨迹几何、坐标系、采样频率和执行速度；把它们固定在离散动作块中会掩盖可调控制边界。", "慢速语义或预测通道适合提出名义轨迹与子目标，高频传感和残差控制负责局部物理误差；二者需要明确升级与重规划条件。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "B-spline Policy、TouchWorld 与相对 EEF 都通过显式执行接口减少主策略需要隐式学习的时标或坐标变化。", "boundary": "连续轨迹重定时、触觉残差和跨本体相对动作位于不同控制层，不能互相替代。", "difference": "三者分别解耦轨迹与速度、预测与反应、共享动作语义与本体坐标。"}]
unresolved_tensions: ["更快执行和更长开环复用降低计算成本，却会放大低层跟踪误差和接触切换风险。", "跨本体不变量越强，越可能丢失动力学、形态和硬件安全极限。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["motion-control-execution-interfaces"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_0078f804e87c7ed12f88876d", "primary_direction": "motion-control-execution-interfaces", "secondary_directions": [], "subdirections": ["action-representation-and-coordinate-frames", "trajectories-flows-and-action-chunks"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "B-spline Policy separates trajectory geometry, sampling frequency and execution speed in the action representation."}, {"reflection_id": "reflection_c5765c32f1c3dd7302da4906", "primary_direction": "motion-control-execution-interfaces", "secondary_directions": ["dexterous-contact-manipulation", "world-models-predictive-representations"], "subdirections": ["high-frequency-feedback", "controller-policy-handoff"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "TouchWorld separates slow semantic prediction from high-frequency tactile residual correction."}, {"reflection_id": "reflection_0db16c2a58084d442087245e", "primary_direction": "motion-control-execution-interfaces", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment"], "subdirections": ["action-representation-and-coordinate-frames", "kinematic-and-dynamic-interfaces"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "GR00T uses relative end-effector actions as a cross-embodiment execution interface while retaining embodiment-specific limits."}]
input_syntheses: ["synthesis_fe1750531bf1b2a79846b657"]
---

# 运动控制：动作几何、执行时标与快慢反馈交接

## Emerging patterns

- 动作接口至少要声明轨迹几何、坐标系、采样频率和执行速度；把它们固定在离散动作块中会掩盖可调控制边界。
- 慢速语义或预测通道适合提出名义轨迹与子目标，高频传感和残差控制负责局部物理误差；二者需要明确升级与重规划条件。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "B-spline Policy、TouchWorld 与相对 EEF 都通过显式执行接口减少主策略需要隐式学习的时标或坐标变化。",
    "boundary": "连续轨迹重定时、触觉残差和跨本体相对动作位于不同控制层，不能互相替代。",
    "difference": "三者分别解耦轨迹与速度、预测与反应、共享动作语义与本体坐标。"
  }
]

## Unresolved tensions

- 更快执行和更长开环复用降低计算成本，却会放大低层跟踪误差和接触切换风险。
- 跨本体不变量越强，越可能丢失动力学、形态和硬件安全极限。

## Candidate hypotheses

[]

## Possible experiments

None.
