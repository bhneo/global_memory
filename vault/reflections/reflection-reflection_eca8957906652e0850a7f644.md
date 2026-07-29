---
id: "reflection_eca8957906652e0850a7f644"
type: "reflection"
status: "active"
title: "LifelongVLA：用双时间尺度适配显式管理可塑性—稳定性"
created_at: "2026-07-21T17:44:55+08:00"
updated_at: "2026-07-21T17:44:55+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "continual-learning"]
confidence: "medium"
source_ids: ["source_04477c8679bc779d8389a22e"]
relations: []
target_ids: ["input_aa07b64b8d7408c682aac2fc", "source_04477c8679bc779d8389a22e"]
input_id: "input_aa07b64b8d7408c682aac2fc"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它没有把持续学习简化为扩大 replay，而是用短期与长期 LoRA 路径及任务门控明确分配新技能适应和旧技能巩固。"
what_changed: "持续 VLA 的关键接口不仅是保留多少数据，还包括哪些参数承担短期变化、何时合并到长期路径以及任务身份如何被识别。"
surprising: "作者报告相对基线成功率提升超过 13%、遗忘率降低超过 8.2%，真机任务均超过 80%；这些结论仍局限于其增量任务顺序和已知任务门控设置。"
connections: [{"shared_mechanism": "都把经验分成快速适应与稳定保留的不同时间尺度。", "boundary": "LoRA 门控的参数稳定性不等于跨形态技能语义已被正确迁移。", "difference": "技能进化强调外部技能版本和验证；LifelongVLA 在模型参数内部通过双 LoRA 路径和缓存 replay 管理遗忘。"}]
conflicts: []
open_questions: ["未知任务边界、相似技能冲突和长序列任务到来时，门控是否仍能正确分配短长期适配？"]
possible_mechanisms: ["短期 adapter 吸收新任务梯度，长期 adapter 与平衡 replay 保存跨任务稳定表征。"]
future_directions: ["在无任务 ID、非平稳场景和更长任务序列上测试遗忘、迁移与缓存偏差。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# LifelongVLA：用双时间尺度适配显式管理可塑性—稳定性

## Why important

它没有把持续学习简化为扩大 replay，而是用短期与长期 LoRA 路径及任务门控明确分配新技能适应和旧技能巩固。

## What changed

持续 VLA 的关键接口不仅是保留多少数据，还包括哪些参数承担短期变化、何时合并到长期路径以及任务身份如何被识别。

## Surprising

作者报告相对基线成功率提升超过 13%、遗忘率降低超过 8.2%，真机任务均超过 80%；这些结论仍局限于其增量任务顺序和已知任务门控设置。

## Connections

- Shared mechanism: 都把经验分成快速适应与稳定保留的不同时间尺度。
  Boundary: LoRA 门控的参数稳定性不等于跨形态技能语义已被正确迁移。
  Difference: 技能进化强调外部技能版本和验证；LifelongVLA 在模型参数内部通过双 LoRA 路径和缓存 replay 管理遗忘。

## Conflicts

None recorded.

## Open questions

- 未知任务边界、相似技能冲突和长序列任务到来时，门控是否仍能正确分配短长期适配？

## Possible mechanisms

- 短期 adapter 吸收新任务梯度，长期 adapter 与平衡 replay 保存跨任务稳定表征。

## Future directions

- 在无任务 ID、非平稳场景和更长任务序列上测试遗忘、迁移与缓存偏差。
