---
id: "reflection_5eb9ba718b0b143e55d0b020"
type: "reflection"
status: "active"
title: "FORGE-plus：语义恢复可以选动作，但不能拥有力权限"
created_at: "2026-07-26T12:18:52+08:00"
updated_at: "2026-07-26T12:18:52+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["contact-rich-manipulation", "robot-safety", "failure-recovery"]
confidence: "medium"
source_ids: ["source_45c4de28acb4ba36642f1594"]
relations: []
target_ids: ["input_d600ca44e11764aca6684b48", "source_45c4de28acb4ba36642f1594"]
input_id: "input_d600ca44e11764aca6684b48"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "FORGE-plus 把对象级力预算、力特征驱动的失败分类、固定恢复菜单与高频控制硬约束分开，显示慢速 LLM 可以参与恢复选择而不成为安全执行器；同时它用接触力 overshoot 暴露了命令上限与物理接触上限之间的差距。"
what_changed: "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。"
surprising: "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。"
connections: [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}]
conflicts: []
open_questions: ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# FORGE-plus：语义恢复可以选动作，但不能拥有力权限

## Why important

FORGE-plus 把对象级力预算、力特征驱动的失败分类、固定恢复菜单与高频控制硬约束分开，显示慢速 LLM 可以参与恢复选择而不成为安全执行器；同时它用接触力 overshoot 暴露了命令上限与物理接触上限之间的差距。

## What changed

此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。

## Surprising

读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。

## Connections

- Shared mechanism: FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。
  Boundary: 连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。
  Difference: FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。

## Conflicts

None recorded.

## Open questions

- 如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
