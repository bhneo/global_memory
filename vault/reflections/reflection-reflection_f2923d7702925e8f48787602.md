---
id: "reflection_f2923d7702925e8f48787602"
type: "reflection"
status: "active"
title: "VLA 推理时多样化应由失败风险触发，而不是持续扰动基础策略"
created_at: "2026-08-02T12:14:36+08:00"
updated_at: "2026-08-02T12:14:36+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vision-language-action", "reinforcement-learning", "test-time-steering"]
confidence: "high"
source_ids: ["source_e504623270d30d733b2cb9e1"]
relations: []
target_ids: ["input_5f3c6ce6e48a86bbc3f26606", "source_e504623270d30d733b2cb9e1"]
input_id: "input_5f3c6ce6e48a86bbc3f26606"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "RL2-VLA 把冻结 VLA、离线 RL 潜表示策略、失败检测器和候选验证器组合为一个条件化推理接口，回答了何时值得用额外动作多样性跨出示范主模态，同时保留基础策略在正常状态下的准确动作。"
what_changed: "此前容易把 test-time scaling 理解为统一增加候选数量；该论文区分成功态与失败态的相反缩放行为，表明多样性干预需要由失败风险门控，否则会损害已经准确的动作。"
surprising: "论文报告组合转向在失败元组上改善动作误差缩放，却在成功元组上属于最差方法之一；适应性不是附加优化，而是避免转向伤害基础策略的核心边界。"
connections: [{"shared_mechanism": "都冻结基础 flow/VLA 先验，并在小于主干的接口上引入奖励或纠正信号。", "boundary": "RL2-VLA 在推理期组合 VLA 与离线 RL 速度场并依赖失败检测和候选验证；RLMM-Flow 在训练期优化初始潜变量，CheckVLA 在动作派发后检测后果偏差并修复后缀。", "difference": "三者分别改变候选分布、生成潜变量和已提交动作后缀，监督来源与干预时机不可互换。"}]
conflicts: []
open_questions: ["失败检测器在新本体、新相机与没有在线失败 rollout 的场景中如何校准，才能避免把门控收益建立在额外任务级数据上？"]
possible_mechanisms: ["VLA action-expert latent 为轻量 RL policy 提供任务相关状态，速度场组合扩展候选分布，失败门控把分布外探索限制在基础策略预计失效的时刻。"]
future_directions: ["用统一调用预算联合报告失败召回、误触发、候选多样性、验证器校准与真实闭环收益。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# VLA 推理时多样化应由失败风险触发，而不是持续扰动基础策略

## Why important

RL2-VLA 把冻结 VLA、离线 RL 潜表示策略、失败检测器和候选验证器组合为一个条件化推理接口，回答了何时值得用额外动作多样性跨出示范主模态，同时保留基础策略在正常状态下的准确动作。

## What changed

此前容易把 test-time scaling 理解为统一增加候选数量；该论文区分成功态与失败态的相反缩放行为，表明多样性干预需要由失败风险门控，否则会损害已经准确的动作。

## Surprising

论文报告组合转向在失败元组上改善动作误差缩放，却在成功元组上属于最差方法之一；适应性不是附加优化，而是避免转向伤害基础策略的核心边界。

## Connections

- Shared mechanism: 都冻结基础 flow/VLA 先验，并在小于主干的接口上引入奖励或纠正信号。
  Boundary: RL2-VLA 在推理期组合 VLA 与离线 RL 速度场并依赖失败检测和候选验证；RLMM-Flow 在训练期优化初始潜变量，CheckVLA 在动作派发后检测后果偏差并修复后缀。
  Difference: 三者分别改变候选分布、生成潜变量和已提交动作后缀，监督来源与干预时机不可互换。

## Conflicts

None recorded.

## Open questions

- 失败检测器在新本体、新相机与没有在线失败 rollout 的场景中如何校准，才能避免把门控收益建立在额外任务级数据上？

## Possible mechanisms

- VLA action-expert latent 为轻量 RL policy 提供任务相关状态，速度场组合扩展候选分布，失败门控把分布外探索限制在基础策略预计失效的时刻。

## Future directions

- 用统一调用预算联合报告失败召回、误触发、候选多样性、验证器校准与真实闭环收益。
