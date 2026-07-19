---
id: "reflection_051f1a0f00d5131171df1440"
type: "reflection"
status: "active"
title: "Pelican-VLA 0.5：注意力泛化先于动作泛化"
created_at: "2026-07-19T17:16:52+08:00"
updated_at: "2026-07-19T17:16:52+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "generalization"]
confidence: "medium"
source_ids: ["source_3093a2f57587e962f87d6277"]
relations: []
target_ids: ["input_68161acb3826b9546d640de1", "source_3093a2f57587e962f87d6277"]
input_id: "input_68161acb3826b9546d640de1"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它提供了诊断 VLA 泛化的新分层：模型可能已经跨场景和本体聚焦正确对象与接触区域，却仍不能把该表示稳定映射为成功动作，因此注意力命中不能直接当作零样本控制能力。"
what_changed: "此前常把任务相关视觉表示和动作泛化合并评价；该材料要求分别测量 attention-level generalization 与 attention-to-action transfer。"
surprising: "紧凑 Bottleneck Tokens 在没有对象标注、分割或注意力监督时形成操作相关注意力，而且微调前后注意模式相似，暗示微调主要强化表示到动作的映射。"
connections: [{"shared_mechanism": "都追求跨对象、场景、任务与本体共享任务相关视觉表示", "boundary": "连接只说明视觉表征可迁移，不表示统一动作空间或跨本体动力学已经解决", "difference": "通用 VLA 概念描述端到端跨本体策略目标，Pelican 的结果把其中的注意力表示能力与最终执行能力拆开评估"}]
conflicts: ["可视化注意力可能不是因果解释；操作相关区域聚焦也可能与动作成功无关"]
open_questions: ["如何设计干预实验验证 Bottleneck Tokens 的注意力是否因果改善跨本体动作泛化？"]
possible_mechanisms: ["紧凑瓶颈迫使感知到动作通路压缩并路由任务相关对象与接触区域"]
future_directions: ["同时报告注意力定位、动作可达性、接触成功和跨本体动力学误差"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Pelican-VLA 0.5：注意力泛化先于动作泛化

## Why important

它提供了诊断 VLA 泛化的新分层：模型可能已经跨场景和本体聚焦正确对象与接触区域，却仍不能把该表示稳定映射为成功动作，因此注意力命中不能直接当作零样本控制能力。

## What changed

此前常把任务相关视觉表示和动作泛化合并评价；该材料要求分别测量 attention-level generalization 与 attention-to-action transfer。

## Surprising

紧凑 Bottleneck Tokens 在没有对象标注、分割或注意力监督时形成操作相关注意力，而且微调前后注意模式相似，暗示微调主要强化表示到动作的映射。

## Connections

- Shared mechanism: 都追求跨对象、场景、任务与本体共享任务相关视觉表示
  Boundary: 连接只说明视觉表征可迁移，不表示统一动作空间或跨本体动力学已经解决
  Difference: 通用 VLA 概念描述端到端跨本体策略目标，Pelican 的结果把其中的注意力表示能力与最终执行能力拆开评估

## Conflicts

- 可视化注意力可能不是因果解释；操作相关区域聚焦也可能与动作成功无关

## Open questions

- 如何设计干预实验验证 Bottleneck Tokens 的注意力是否因果改善跨本体动作泛化？

## Possible mechanisms

- 紧凑瓶颈迫使感知到动作通路压缩并路由任务相关对象与接触区域

## Future directions

- 同时报告注意力定位、动作可达性、接触成功和跨本体动力学误差
