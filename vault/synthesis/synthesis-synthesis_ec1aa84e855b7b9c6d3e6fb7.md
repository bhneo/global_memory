---
id: "synthesis_ec1aa84e855b7b9c6d3e6fb7"
type: "synthesis"
status: "active"
title: "Agent 系统：记忆演化、外化状态与物理执行恢复边界"
created_at: "2026-07-29T13:22:24+08:00"
updated_at: "2026-07-29T13:22:24+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["agent-memory", "embodied-agents", "system-infrastructure"]
confidence: "medium"
source_ids: ["source_01ed2f19e91bb0eb1ec3ee92", "source_6b52a51e2b4a3be43c97c386"]
relations: []
input_reflections: ["reflection_4430cc70fe95425f717c1e71", "reflection_7952be977c24d5dfe1da2072"]
input_concepts: []
emerging_patterns: ["Agent Memory 的图结构价值不止是多跳检索；只有选择性写入、冲突演化、环境反馈和可归因评测连成闭环，关系结构才成为长期认知机制。", "冻结 VLA 外壳的增量位于规划、记忆选择、服务编排和失败恢复，必须与基础策略本身的能力分开评测。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "图式记忆生命周期与物理 Agent 外壳都把历史状态用于改变后续选择。", "boundary": "图式记忆综述是领域分类，RPent Source 是官方仓库接口；两者都不能单独证明任务成功率或可靠性提升。", "difference": "前者关注记忆内容的抽取、组织、召回和演化，后者关注感知、推理、记忆、执行服务如何围绕冻结策略递归编排。"}]
unresolved_tensions: ["外化共享状态改善故障归因，同时增加一致性、隐私、时延和错误传播面。", "记忆与反思可能补偿局部失败，也可能把一次误判放大为长链执行错误。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["agent-autonomous-systems"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_4430cc70fe95425f717c1e71", "primary_direction": "agent-autonomous-systems", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment"], "subdirections": ["reflection-and-recovery", "tool-use-and-environment-interaction"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "RPent is primarily an agent infrastructure and recovery architecture around heterogeneous physical capabilities."}, {"reflection_id": "reflection_7952be977c24d5dfe1da2072", "primary_direction": "agent-autonomous-systems", "secondary_directions": [], "subdirections": ["memory-and-continual-learning", "evaluation-and-safety-boundaries"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "The survey reflection changes how long-term agent memory is evaluated across extraction, storage, retrieval and evolution."}]
input_syntheses: ["synthesis_7084bca907043e3cba4afb7e"]
---

# Agent 系统：记忆演化、外化状态与物理执行恢复边界

## Emerging patterns

- Agent Memory 的图结构价值不止是多跳检索；只有选择性写入、冲突演化、环境反馈和可归因评测连成闭环，关系结构才成为长期认知机制。
- 冻结 VLA 外壳的增量位于规划、记忆选择、服务编排和失败恢复，必须与基础策略本身的能力分开评测。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "图式记忆生命周期与物理 Agent 外壳都把历史状态用于改变后续选择。",
    "boundary": "图式记忆综述是领域分类，RPent Source 是官方仓库接口；两者都不能单独证明任务成功率或可靠性提升。",
    "difference": "前者关注记忆内容的抽取、组织、召回和演化，后者关注感知、推理、记忆、执行服务如何围绕冻结策略递归编排。"
  }
]

## Unresolved tensions

- 外化共享状态改善故障归因，同时增加一致性、隐私、时延和错误传播面。
- 记忆与反思可能补偿局部失败，也可能把一次误判放大为长链执行错误。

## Candidate hypotheses

[]

## Possible experiments

None.
