---
id: "reflection_9e08fb71dc807c22fb1b8bf5"
type: "reflection"
status: "active"
title: "冻结技能之上的验证恢复闭环可以释放推理能力，但不会提高底层技能上限"
created_at: "2026-07-28T18:38:38+08:00"
updated_at: "2026-07-28T18:38:38+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "vision-language-action", "orchestration", "verification", "recovery"]
confidence: "high"
source_ids: ["source_38375a0f6ddc91f3bfde47d3"]
relations: []
target_ids: ["input_e876fbfe2c39e1892dfaa802", "source_38375a0f6ddc91f3bfde47d3"]
input_id: "input_e876fbfe2c39e1892dfaa802"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Pigey 用前沿视觉语言模型在冻结 TAMP 与 VLA 技能之上执行感知、规划、调用、验证和恢复，显示大量任务级失败来自编排与状态更新，而不是必须重训底层策略。这为现有 asymmetric frozen VLA harness 提供了直接的同构实例。"
what_changed: "冻结 VLA 的性能评估必须把低层技能能力和高层编排能力分开；加入验证、重感知和双向升级后，任务成功率可大幅变化，但这不意味着底层策略本身变强。"
surprising: "论文报告的主要增益集中在推理受限任务，同时明确显示低层技能不支持的任务仍构成不可跨越的上限。"
connections: [{"shared_mechanism": "现有 asymmetric frozen VLA harness 已定义冻结局部技能与高层语义重绑定、规划、验证和恢复的非对称分工。", "boundary": "Pigey 是该概念的具体系统和实证实例，而不是新的独立抽象。", "difference": "本文补充了 verify-before-place、完成前 fresh Perceive 和有类型失败升级的操作细节。"}]
conflicts: ["正文声称覆盖七种推理模型，而相应表格列出九种；这不影响所有列出模型均较基线提升的方向性结论，但限制精确计数的可信度。"]
open_questions: ["如何降低多次视觉语言模型调用的分钟级延迟和成本，同时控制验证器误报与部分可观测性？"]
possible_mechanisms: ["确定性抓取检查、腕部视觉验证、放置前验证和完成前重新感知，把一次性语言计划变成受环境反馈约束的状态机。"]
future_directions: ["用学习型但可校准的验证器和更低延迟的局部推理替代部分昂贵的前沿模型调用。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 冻结技能之上的验证恢复闭环可以释放推理能力，但不会提高底层技能上限

## Why important

Pigey 用前沿视觉语言模型在冻结 TAMP 与 VLA 技能之上执行感知、规划、调用、验证和恢复，显示大量任务级失败来自编排与状态更新，而不是必须重训底层策略。这为现有 asymmetric frozen VLA harness 提供了直接的同构实例。

## What changed

冻结 VLA 的性能评估必须把低层技能能力和高层编排能力分开；加入验证、重感知和双向升级后，任务成功率可大幅变化，但这不意味着底层策略本身变强。

## Surprising

论文报告的主要增益集中在推理受限任务，同时明确显示低层技能不支持的任务仍构成不可跨越的上限。

## Connections

- Shared mechanism: 现有 asymmetric frozen VLA harness 已定义冻结局部技能与高层语义重绑定、规划、验证和恢复的非对称分工。
  Boundary: Pigey 是该概念的具体系统和实证实例，而不是新的独立抽象。
  Difference: 本文补充了 verify-before-place、完成前 fresh Perceive 和有类型失败升级的操作细节。

## Conflicts

- 正文声称覆盖七种推理模型，而相应表格列出九种；这不影响所有列出模型均较基线提升的方向性结论，但限制精确计数的可信度。

## Open questions

- 如何降低多次视觉语言模型调用的分钟级延迟和成本，同时控制验证器误报与部分可观测性？

## Possible mechanisms

- 确定性抓取检查、腕部视觉验证、放置前验证和完成前重新感知，把一次性语言计划变成受环境反馈约束的状态机。

## Future directions

- 用学习型但可校准的验证器和更低延迟的局部推理替代部分昂贵的前沿模型调用。
