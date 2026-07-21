---
id: "reflection_4b63a8834e11b28db3cf2fdc"
type: "reflection"
status: "active"
title: "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心"
created_at: "2026-07-20T12:39:21+08:00"
updated_at: "2026-07-20T12:39:21+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "tactile-control", "whole-arm-manipulation", "mpc", "contact-modeling"]
confidence: "high"
source_ids: ["source_e8cc1290fdb80e80f77ba2c2"]
relations: []
target_ids: ["input_680e14163f51a60d9a5da0fb", "source_e8cc1290fdb80e80f77ba2c2"]
input_id: "input_680e14163f51a60d9a5da0fb"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "TACTIC 不只把触觉追加到 observation，而是让 distributed tactile、proximity map、contact Jacobian sampling 和 hybrid predictive model 共同围绕多链路接触组织 MPC。"
what_changed: "此前触觉控制容易被描述为学习一个 visuotactile policy；该工作提示，在稀疏多接触数据下，可靠控制还需要把分析运动学用于可行性，把学习模型用于接触形成与断裂，并在采样阶段主动偏向能调节接触力的方向。"
surprising: "接触 Jacobian 不只是 cost 项，而被直接用于塑形每个 MPC step 的动作扰动，使探索及时对当前接触法向敏感。"
connections: [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉既用于预测未来接触，也用于即时动作修正。", "boundary": "TACTIC 不提供形式安全保证，真实实验使用 mannequin 和 custom exoskeleton 数据；面向真人护理仍需舒适性、安全栈与受试者验证。", "difference": "多时间尺度触觉世界模型强调分层神经控制回路；TACTIC 用 sampling-based MPC、contact Jacobian 和 learned latent dynamics 形成显式混合规划器。"}]
conflicts: ["分析结构提高物理一致性，但当前 active-contact 假设和局部 Jacobian 仍会在接触拓扑突变时失效。"]
open_questions: ["接触形成/断裂不确定性如何传播到 MPC 风险，而不只以平均预测力进入 cost？"]
possible_mechanisms: ["proximity map 提供接触前预测，tactile 定位当前接触，Jacobian 引导力调节方向，learned dynamics 补足纯运动学无法预测的接触切换。"]
future_directions: ["联动 variable impedance、接触不确定性和独立安全监控，并在真人交互中验证任务与舒适性。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心

## Why important

TACTIC 不只把触觉追加到 observation，而是让 distributed tactile、proximity map、contact Jacobian sampling 和 hybrid predictive model 共同围绕多链路接触组织 MPC。

## What changed

此前触觉控制容易被描述为学习一个 visuotactile policy；该工作提示，在稀疏多接触数据下，可靠控制还需要把分析运动学用于可行性，把学习模型用于接触形成与断裂，并在采样阶段主动偏向能调节接触力的方向。

## Surprising

接触 Jacobian 不只是 cost 项，而被直接用于塑形每个 MPC step 的动作扰动，使探索及时对当前接触法向敏感。

## Connections

- Shared mechanism: 与多时间尺度触觉世界模型控制都把触觉既用于预测未来接触，也用于即时动作修正。
  Boundary: TACTIC 不提供形式安全保证，真实实验使用 mannequin 和 custom exoskeleton 数据；面向真人护理仍需舒适性、安全栈与受试者验证。
  Difference: 多时间尺度触觉世界模型强调分层神经控制回路；TACTIC 用 sampling-based MPC、contact Jacobian 和 learned latent dynamics 形成显式混合规划器。

## Conflicts

- 分析结构提高物理一致性，但当前 active-contact 假设和局部 Jacobian 仍会在接触拓扑突变时失效。

## Open questions

- 接触形成/断裂不确定性如何传播到 MPC 风险，而不只以平均预测力进入 cost？

## Possible mechanisms

- proximity map 提供接触前预测，tactile 定位当前接触，Jacobian 引导力调节方向，learned dynamics 补足纯运动学无法预测的接触切换。

## Future directions

- 联动 variable impedance、接触不确定性和独立安全监控，并在真人交互中验证任务与舒适性。
