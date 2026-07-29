---
id: "reflection_63063bb66f27ff296bc9d7d2"
type: "reflection"
status: "active"
title: "Action QFormer：动作接口也是表征更新边界"
created_at: "2026-07-22T18:12:05+08:00"
updated_at: "2026-07-22T18:12:05+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["vla", "representation-learning"]
confidence: "medium"
source_ids: ["source_9b0d550203c4d7bd7acf8a36"]
relations: []
target_ids: ["input_5242bae9e71b14b53f2fbe8a", "source_9b0d550203c4d7bd7acf8a36"]
input_id: "input_5242bae9e71b14b53f2fbe8a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作指出动作监督不仅训练动作头，也会重塑继承的多模态表征；查询式中间接口提供一个可设计的梯度与信息组织边界。"
what_changed: "动作接口不只是从表征读取控制量的末端模块，它还决定动作损失如何回写视觉语言通路。"
surprising: ""
connections: [{"shared_mechanism": "两者都通过显式中间接口约束高层表示如何影响动作。", "boundary": "该连接不说明接口设计可替代障碍规避、规划或真实接触验证。", "difference": "Action QFormer 是训练时查询接口；现有分类概念描述的是具身 VLM 的功能组织。"}]
conflicts: []
open_questions: ["查询接口在接触操作和长时程重规划中是否仍能避免语言侧表征退化？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Action QFormer：动作接口也是表征更新边界

## Why important

该工作指出动作监督不仅训练动作头，也会重塑继承的多模态表征；查询式中间接口提供一个可设计的梯度与信息组织边界。

## What changed

动作接口不只是从表征读取控制量的末端模块，它还决定动作损失如何回写视觉语言通路。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都通过显式中间接口约束高层表示如何影响动作。
  Boundary: 该连接不说明接口设计可替代障碍规避、规划或真实接触验证。
  Difference: Action QFormer 是训练时查询接口；现有分类概念描述的是具身 VLM 的功能组织。

## Conflicts

None recorded.

## Open questions

- 查询接口在接触操作和长时程重规划中是否仍能避免语言侧表征退化？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
