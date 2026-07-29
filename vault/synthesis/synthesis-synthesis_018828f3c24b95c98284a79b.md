---
id: "synthesis_018828f3c24b95c98284a79b"
type: "synthesis"
status: "active"
title: "可执行世界表示：历史反例、状态程序与 episode twin 保真度"
created_at: "2026-07-29T13:41:44+08:00"
updated_at: "2026-07-29T13:41:44+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["world-models", "executable-representations", "real2sim"]
confidence: "medium"
source_ids: ["source_4f709a2f26b6_v0002_cb9f3e56f3e6", "source_d90b4e9bf278dfc5e68d1bb5"]
relations: []
input_reflections: ["reflection_dc9b1c4fbde4b505081c875b", "reflection_e8b12edde0bfcd108fbc334e"]
input_concepts: []
emerging_patterns: ["可执行世界表示至少有两种不同验证任务：离散状态/转移程序必须重放全部交互历史，物理 episode twin 必须让场景、相机、对象状态、动力学和轨迹共同可运行。", "可搜索、可重放和可预测都不能单独证明真实机器人闭环有效；验证标准必须绑定表示的预期用途。"]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Schema 与 Agentic Real2Sim 都把观察历史转换成可运行、可由失败结果检验的环境表示。", "boundary": "ARC 的离散程序 backtest 与机器人仿真的重建误差、物理参数和传感噪声具有不同保真度标准。", "difference": "Schema用区分性实验修订状态变量和转移规则，Agentic Real2Sim用几何、物理、参与者、相机与轨迹构造 episode twin。"}]
unresolved_tensions: ["更强可执行性提高可检验性，也可能把表示错误直接传播到规划与训练。", "仿真回放分数仍不能代替真实闭环策略的行为误差和安全结果。"]
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
direction_assignments: [{"reflection_id": "reflection_dc9b1c4fbde4b505081c875b", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["agent-autonomous-systems"], "subdirections": ["state-abstraction", "rollout-and-planning-interfaces"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "Schema makes state and transition programs executable and requires every revision to backtest against append-only interaction history."}, {"reflection_id": "reflection_e8b12edde0bfcd108fbc334e", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["agent-autonomous-systems"], "subdirections": ["rollout-and-planning-interfaces", "predictive-model-evaluation-and-failure-detection"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "Agentic Real2Sim evaluates an episode twin as a runnable physical interaction unit rather than a visually plausible asset."}]
input_syntheses: ["synthesis_180dbd6bb5b146e333818008"]
---

# 可执行世界表示：历史反例、状态程序与 episode twin 保真度

## Emerging patterns

- 可执行世界表示至少有两种不同验证任务：离散状态/转移程序必须重放全部交互历史，物理 episode twin 必须让场景、相机、对象状态、动力学和轨迹共同可运行。
- 可搜索、可重放和可预测都不能单独证明真实机器人闭环有效；验证标准必须绑定表示的预期用途。

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Schema 与 Agentic Real2Sim 都把观察历史转换成可运行、可由失败结果检验的环境表示。",
    "boundary": "ARC 的离散程序 backtest 与机器人仿真的重建误差、物理参数和传感噪声具有不同保真度标准。",
    "difference": "Schema用区分性实验修订状态变量和转移规则，Agentic Real2Sim用几何、物理、参与者、相机与轨迹构造 episode twin。"
  }
]

## Unresolved tensions

- 更强可执行性提高可检验性，也可能把表示错误直接传播到规划与训练。
- 仿真回放分数仍不能代替真实闭环策略的行为误差和安全结果。

## Candidate hypotheses

[]

## Possible experiments

None.
