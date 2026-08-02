---
id: "reflection_d4da03127a4726ff3f567d63"
type: "reflection"
status: "active"
title: "World Action Planner：把计划变成可被世界模型反复想象和修正的对象"
created_at: "2026-08-02T18:57:48+08:00"
updated_at: "2026-08-02T18:57:48+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "world-model", "planning", "visual-language-model"]
confidence: "medium"
source_ids: ["source_a54ea0123fbadf6d7012c9fb"]
relations: []
target_ids: ["input_cde49d7c9071270dc3fb8348", "source_a54ea0123fbadf6d7012c9fb"]
input_id: "input_cde49d7c9071270dc3fb8348"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "World Action Planner 将 VLM 产生的高层动作计划视为初稿，并用动作条件世界模型想象结果、再通过搜索迭代修正。这把世界模型从一次性 rollout 或执行后监控器提升为计划空间中的内循环评价器，适合长时组合与避碰问题。"
what_changed: "我原先会把 action-conditioned world model 主要放在候选排序或执行监控；该项目强调在执行前反复修改整份动作计划，而不是只选一个固定候选或报警后修复后缀。"
surprising: "动作条件不是低维控制向量，而是通过正向运动学渲染的机器人关节骨架 pose image；世界模型因此在视觉空间中同时看到场景与名义机器人运动。"
connections: [{"shared_mechanism": "WAP 与 concept_1bc84fc99981d367b712d161 都用动作条件世界模型生成候选未来以支持决策。", "boundary": "项目页没有给出捕获文本中的数值表格，不能从“outperforms”措辞推导具体提升或统计稳健性。", "difference": "DriftWorld 节点强调单次前向 rollout 吞吐量，WAP 强调 VLM 初稿、世界模型想象与计划搜索的迭代闭环。"}, {"shared_mechanism": "WAP 与 concept_2db7edf95d63ca80702f042e 都用动作条件未来验证动作计划。", "boundary": "WAP 在执行前优化计划，CheckVLA 在执行中按观测偏差修复剩余后缀，两者不应合并。", "difference": "WAP 搜索整体计划的想象结果，CheckVLA 监控已提交动作的真实后果并做延迟感知修复。"}]
conflicts: []
open_questions: ["当世界模型在搜索中被反复利用时，如何检测计划对模型误差的投机，并把想象分数与真实闭环成功率校准？"]
possible_mechanisms: ["由 VLM 提出动作计划，把正向运动学生成的机器人 pose image 作为动作条件输入多任务世界模型，再依据想象 rollout 的任务进展和碰撞风险迭代搜索计划。"]
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# World Action Planner：把计划变成可被世界模型反复想象和修正的对象

## Why important

World Action Planner 将 VLM 产生的高层动作计划视为初稿，并用动作条件世界模型想象结果、再通过搜索迭代修正。这把世界模型从一次性 rollout 或执行后监控器提升为计划空间中的内循环评价器，适合长时组合与避碰问题。

## What changed

我原先会把 action-conditioned world model 主要放在候选排序或执行监控；该项目强调在执行前反复修改整份动作计划，而不是只选一个固定候选或报警后修复后缀。

## Surprising

动作条件不是低维控制向量，而是通过正向运动学渲染的机器人关节骨架 pose image；世界模型因此在视觉空间中同时看到场景与名义机器人运动。

## Connections

- Shared mechanism: WAP 与 concept_1bc84fc99981d367b712d161 都用动作条件世界模型生成候选未来以支持决策。
  Boundary: 项目页没有给出捕获文本中的数值表格，不能从“outperforms”措辞推导具体提升或统计稳健性。
  Difference: DriftWorld 节点强调单次前向 rollout 吞吐量，WAP 强调 VLM 初稿、世界模型想象与计划搜索的迭代闭环。
- Shared mechanism: WAP 与 concept_2db7edf95d63ca80702f042e 都用动作条件未来验证动作计划。
  Boundary: WAP 在执行前优化计划，CheckVLA 在执行中按观测偏差修复剩余后缀，两者不应合并。
  Difference: WAP 搜索整体计划的想象结果，CheckVLA 监控已提交动作的真实后果并做延迟感知修复。

## Conflicts

None recorded.

## Open questions

- 当世界模型在搜索中被反复利用时，如何检测计划对模型误差的投机，并把想象分数与真实闭环成功率校准？

## Possible mechanisms

- 由 VLM 提出动作计划，把正向运动学生成的机器人 pose image 作为动作条件输入多任务世界模型，再依据想象 rollout 的任务进展和碰撞风险迭代搜索计划。

## Future directions

None recorded.
