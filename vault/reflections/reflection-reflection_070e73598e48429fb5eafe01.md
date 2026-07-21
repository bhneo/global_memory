---
id: "reflection_070e73598e48429fb5eafe01"
type: "reflection"
status: "active"
title: "PAKE：先学习运动学冗余分布，再让 RL 选择部分参考"
created_at: "2026-07-20T12:39:38+08:00"
updated_at: "2026-07-20T12:39:38+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "whole-body-control", "loco-manipulation", "kinematic-redundancy", "hierarchical-rl"]
confidence: "high"
source_ids: ["source_951559714c0383331b1b30ac"]
relations: []
target_ids: ["input_204a28780631a2ded63e6314", "source_951559714c0383331b1b30ac"]
input_id: "input_204a28780631a2ded63e6314"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "PAKE 把高维全身 loco-manipulation 拆成 Kinematic Normalizing Flow 生成多样可行的 partial reference、高层策略在其 latent 中选择冗余解、低层策略执行动力学可行跟踪。"
what_changed: "全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。"
surprising: "框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。"
connections: [{"shared_mechanism": "与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。", "boundary": "PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。", "difference": "PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。"}]
conflicts: ["运动学 latent 缩小搜索空间，却可能排除依赖动力学、接触或动量的可行解。"]
open_questions: ["怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？"]
possible_mechanisms: ["条件 normalizing flow 表达给定末端目标下的多解分布，高层策略选择有利于协调的 latent，低层 imitation 吸收动力学扰动。"]
future_directions: ["将接触模式、负载和稳定裕度纳入 partial reference latent，并评估分布外目标的失败检测。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# PAKE：先学习运动学冗余分布，再让 RL 选择部分参考

## Why important

PAKE 把高维全身 loco-manipulation 拆成 Kinematic Normalizing Flow 生成多样可行的 partial reference、高层策略在其 latent 中选择冗余解、低层策略执行动力学可行跟踪。

## What changed

全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。

## Surprising

框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。

## Connections

- Shared mechanism: 与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。
  Boundary: PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。
  Difference: PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。

## Conflicts

- 运动学 latent 缩小搜索空间，却可能排除依赖动力学、接触或动量的可行解。

## Open questions

- 怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？

## Possible mechanisms

- 条件 normalizing flow 表达给定末端目标下的多解分布，高层策略选择有利于协调的 latent，低层 imitation 吸收动力学扰动。

## Future directions

- 将接触模式、负载和稳定裕度纳入 partial reference latent，并评估分布外目标的失败检测。
