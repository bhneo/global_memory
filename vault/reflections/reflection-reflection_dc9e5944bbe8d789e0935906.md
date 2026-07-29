---
id: "reflection_dc9e5944bbe8d789e0935906"
type: "reflection"
status: "active"
title: "BadWAM：合理的未来想象不能单独证明动作安全"
created_at: "2026-07-23T18:07:05+08:00"
updated_at: "2026-07-23T18:07:05+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["world-action-model", "robot-safety", "adversarial-robustness"]
confidence: "medium"
source_ids: ["source_c2d7b53bd1c40ed0af8ea5cb"]
relations: []
target_ids: ["input_97348f953ed6aff15f2aac9a", "source_c2d7b53bd1c40ed0af8ea5cb"]
input_id: "input_97348f953ed6aff15f2aac9a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "BadWAM 显示小视觉扰动可在保持预测未来看似合理时诱导失败动作，暴露世界预测与动作输出之间可被攻击的对齐接口；这限制了把 imagined future 当作充分安全证据的做法。"
what_changed: "世界动作模型的预测质量与闭环动作正确性必须分别验证；未来画面未明显漂移并不蕴含动作仍与该未来一致。"
surprising: ""
connections: [{"shared_mechanism": "两者都依赖未来表征与动作输出的联合建模。", "boundary": "该连接仅说明联合建模存在需要验证的接口，不说明所有世界动作模型或所有扰动都会发生同类攻击。", "difference": "既有动作中心联合世界—动作模型描述生成架构；BadWAM 聚焦该架构中想象与执行可被脱钩的安全失败模式。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# BadWAM：合理的未来想象不能单独证明动作安全

## Why important

BadWAM 显示小视觉扰动可在保持预测未来看似合理时诱导失败动作，暴露世界预测与动作输出之间可被攻击的对齐接口；这限制了把 imagined future 当作充分安全证据的做法。

## What changed

世界动作模型的预测质量与闭环动作正确性必须分别验证；未来画面未明显漂移并不蕴含动作仍与该未来一致。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都依赖未来表征与动作输出的联合建模。
  Boundary: 该连接仅说明联合建模存在需要验证的接口，不说明所有世界动作模型或所有扰动都会发生同类攻击。
  Difference: 既有动作中心联合世界—动作模型描述生成架构；BadWAM 聚焦该架构中想象与执行可被脱钩的安全失败模式。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
