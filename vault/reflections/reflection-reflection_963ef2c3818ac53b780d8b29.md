---
id: "reflection_963ef2c3818ac53b780d8b29"
type: "reflection"
status: "active"
title: "Patch Policy：block-causal 掩码保留时序并接入密集视觉 / block-causal masking admits dense vision without losing temporal causality"
created_at: "2026-07-27T18:14:42+08:00"
updated_at: "2026-07-27T18:14:42+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "visual-representations", "control"]
confidence: "medium"
source_ids: ["source_e8651a193623cbe2b86becb0"]
relations: []
target_ids: ["input_ece052248dd2c432913efd3a", "source_e8651a193623cbe2b86becb0"]
input_id: "input_ece052248dd2c432913efd3a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Patch Policy 以 block-causal attention 让轻量 transformer 直接消费预训练 ViT patch tokens，同时维持策略的时间因果性，避免全局池化丢失空间细节或完整 VLM 的推理成本。"
what_changed: "我会把其优势限定为论文的视觉 backbone、掩码、模拟与真实任务设置，而不将相对改进泛化为任何 dense-feature 控制器。"
surprising: ""
connections: [{"shared_mechanism": "两者都保留细粒度视觉表征以支持反应式控制。", "boundary": "本文依赖预训练 ViT patch、block-causal mask 与所报告七个环境套件。", "difference": "大 VLA 借完整 VLM 获得 dense tokens；本文以最小策略扩展避开该骨干计算开销。"}]
conflicts: []
open_questions: ["遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Patch Policy：block-causal 掩码保留时序并接入密集视觉 / block-causal masking admits dense vision without losing temporal causality

## Why important

Patch Policy 以 block-causal attention 让轻量 transformer 直接消费预训练 ViT patch tokens，同时维持策略的时间因果性，避免全局池化丢失空间细节或完整 VLM 的推理成本。

## What changed

我会把其优势限定为论文的视觉 backbone、掩码、模拟与真实任务设置，而不将相对改进泛化为任何 dense-feature 控制器。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都保留细粒度视觉表征以支持反应式控制。
  Boundary: 本文依赖预训练 ViT patch、block-causal mask 与所报告七个环境套件。
  Difference: 大 VLA 借完整 VLM 获得 dense tokens；本文以最小策略扩展避开该骨干计算开销。

## Conflicts

None recorded.

## Open questions

- 遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
