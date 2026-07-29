---
id: "synthesis_13759d5e46a496e43d0349cc"
type: "synthesis"
status: "active"
title: "精细操作：手—物关系、触觉目标与接触可行性闭环"
created_at: "2026-07-29T13:32:27+08:00"
updated_at: "2026-07-29T13:32:27+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["dexterous-manipulation", "tactile-control", "teleoperation"]
confidence: "medium"
source_ids: ["source_37fe3c1f9d9fb7daa262fa91", "source_570c26541066c02080dd8de5", "source_e8cc1290fdb80e80f77ba2c2"]
relations: []
input_reflections: ["reflection_4b63a8834e11b28db3cf2fdc", "reflection_631ecd2479bd127e62730569", "reflection_e8e62c04da8ad9f420c37be4"]
input_concepts: []
emerging_patterns: ["精细操作可迁移的单位更接近任务相关手—物关系、接触结构和阶段目标，而不是逐帧人手关节姿态。", "触觉既是示范保真目标，也是运行时误差信号；接触形成、力调节和接触断裂需要独立于几何成功率的评价。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "TactiDex、TACTIC 与 TELEDEXTER 都把手—物或接触关系作为中间控制对象。", "boundary": "三者依赖的传感、MoCap、仿真和接触拓扑不同，当前结果不能外推到开放世界灵巧操作。", "difference": "TactiDex定义人机接触保真指标，TACTIC执行 whole-arm 接触中心 MPC，TELEDEXTER用在线手—物子目标驱动低层策略。"}]
unresolved_tensions: ["更强示范先验缩小搜索空间，却可能阻止策略切换到示范之外的接触拓扑。", "复现人类接触有助于解释和迁移，但机器人形态、材料和安全极限不同，完全对齐未必最优。"]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "gpt-5.6-sol-direction-reframe-2026-07-29"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["dexterous-contact-manipulation"]
candidate_window: {"from_date": "2026-07-21", "to_date": "2026-07-29"}
delta_kind: "reframe"
direction_assignments: [{"reflection_id": "reflection_e8e62c04da8ad9f420c37be4", "primary_direction": "dexterous-contact-manipulation", "secondary_directions": [], "subdirections": ["tactile-sensing-and-contact-dynamics", "contact-rich-benchmarks"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "TactiDex makes contact formation, force alignment and safety independent transfer and evaluation targets."}, {"reflection_id": "reflection_4b63a8834e11b28db3cf2fdc", "primary_direction": "dexterous-contact-manipulation", "secondary_directions": ["motion-control-execution-interfaces"], "subdirections": ["tactile-sensing-and-contact-dynamics", "contact-rich-benchmarks"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "TACTIC organizes perception, contact-Jacobian sampling and predictive control around changing whole-arm contact."}, {"reflection_id": "reflection_631ecd2479bd127e62730569", "primary_direction": "dexterous-contact-manipulation", "secondary_directions": [], "subdirections": ["teleoperation-and-retargeting", "demonstration-transfer"], "crosscut_dimensions": ["data-and-demonstrations"], "routing_confidence": "high", "reason": "TELEDEXTER transfers consecutive hand-object subgoals instead of copying every human joint."}]
input_syntheses: ["synthesis_1fdb28cc5ac38aa6f424e5e1"]
---

# 精细操作：手—物关系、触觉目标与接触可行性闭环

## Emerging patterns

- 精细操作可迁移的单位更接近任务相关手—物关系、接触结构和阶段目标，而不是逐帧人手关节姿态。
- 触觉既是示范保真目标，也是运行时误差信号；接触形成、力调节和接触断裂需要独立于几何成功率的评价。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "TactiDex、TACTIC 与 TELEDEXTER 都把手—物或接触关系作为中间控制对象。",
    "boundary": "三者依赖的传感、MoCap、仿真和接触拓扑不同，当前结果不能外推到开放世界灵巧操作。",
    "difference": "TactiDex定义人机接触保真指标，TACTIC执行 whole-arm 接触中心 MPC，TELEDEXTER用在线手—物子目标驱动低层策略。"
  }
]

## Unresolved tensions

- 更强示范先验缩小搜索空间，却可能阻止策略切换到示范之外的接触拓扑。
- 复现人类接触有助于解释和迁移，但机器人形态、材料和安全极限不同，完全对齐未必最优。

## Candidate hypotheses

[]

## Possible experiments

None.
