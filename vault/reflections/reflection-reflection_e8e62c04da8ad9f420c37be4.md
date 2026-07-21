---
id: "reflection_e8e62c04da8ad9f420c37be4"
type: "reflection"
status: "active"
title: "TactiDex：人形动作相似不等于接触层面的人类式操作"
created_at: "2026-07-20T12:39:30+08:00"
updated_at: "2026-07-20T12:39:30+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "dexterous-manipulation", "tactile-transfer", "human-demonstration", "contact-evaluation"]
confidence: "high"
source_ids: ["source_37fe3c1f9d9fb7daa262fa91"]
relations: []
target_ids: ["input_0b9fff59c58a65307b65bb23", "source_37fe3c1f9d9fb7daa262fa91"]
input_id: "input_0b9fff59c58a65307b65bb23"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "TactiDex 同步记录全手压力、手部运动学、腕部和物体 6D 状态，并把 contact formation、force alignment 与安全约束纳入迁移目标和评测，直接暴露纯运动学 imitation 的物理缺口。"
what_changed: "此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。"
surprising: "纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。"
connections: [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。", "boundary": "TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。", "difference": "多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。"}]
conflicts: ["严格复现人类接触分布可提高人类相似性，但机器人形态、材料与安全极限不同，完全对齐未必是最优目标。"]
open_questions: ["哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？"]
possible_mechanisms: ["contact guidance 防止悬空模仿，alignment 对齐接触时空结构，force constraint 抑制通过过大压力投机完成任务。"]
future_directions: ["引入真机触觉闭环与 on-robot adaptation，并把人类相似性和机器人最优接触分开报告。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# TactiDex：人形动作相似不等于接触层面的人类式操作

## Why important

TactiDex 同步记录全手压力、手部运动学、腕部和物体 6D 状态，并把 contact formation、force alignment 与安全约束纳入迁移目标和评测，直接暴露纯运动学 imitation 的物理缺口。

## What changed

此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。

## Surprising

纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。

## Connections

- Shared mechanism: 与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。
  Boundary: TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。
  Difference: 多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。

## Conflicts

- 严格复现人类接触分布可提高人类相似性，但机器人形态、材料与安全极限不同，完全对齐未必是最优目标。

## Open questions

- 哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？

## Possible mechanisms

- contact guidance 防止悬空模仿，alignment 对齐接触时空结构，force constraint 抑制通过过大压力投机完成任务。

## Future directions

- 引入真机触觉闭环与 on-robot adaptation，并把人类相似性和机器人最优接触分开报告。
