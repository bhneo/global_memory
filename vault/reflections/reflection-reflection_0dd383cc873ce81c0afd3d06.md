---
id: "reflection_0dd383cc873ce81c0afd3d06"
type: "reflection"
status: "active"
title: "EGOWAM：跨本体迁移应优先共享世界变化而不是动作"
created_at: "2026-07-19T17:16:43+08:00"
updated_at: "2026-07-19T17:16:43+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "world-model", "cross-embodiment"]
confidence: "medium"
source_ids: ["source_61f3045b170e78e4adb2422c"]
relations: []
target_ids: ["input_5d285e86b54c2cafe7458888", "source_61f3045b170e78e4adb2422c"]
input_id: "input_5d285e86b54c2cafe7458888"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它把人类第一视角数据到机器人策略的迁移瓶颈定位为监督通道选择：动作标签混入形态和行为风格，而未来场景变化可能承载更本体无关的物理与任务信息。"
what_changed: "此前跨本体 VLA 更强调统一动作接口或数据混合；该材料提示应先选择能抽象外观、保持跨本体一致并分离相机运动的 world target，再讨论动作对齐。"
surprising: "该受控比较中像素重建迁移较弱，而 DINO 特征和 3D flow 的收益方向不同，说明“增加世界模型头”本身不够，预测目标的抽象层级决定迁移内容。"
connections: [{"shared_mechanism": "都试图从多形态数据中保留任务语义和物理效果，同时隔离本体特有的执行因素", "boundary": "连接只覆盖跨本体表示共享，不意味着世界监督可以替代机器人动作数据或解决控制精度", "difference": "通用 VLA 侧重统一策略输入输出接口，EGOWAM 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式"}]
conflicts: ["世界表示越抽象越可能丢失接触级控制细节；3D flow 与 DINO 的优势可能随任务分布变化"]
open_questions: ["什么 world target 能同时保留接触动力学、分离 ego-motion 并跨不同机器人相机布局迁移？"]
possible_mechanisms: ["辅助世界预测头让人类数据通过场景动力学而非不可执行动作更新共享视觉骨干"]
future_directions: ["在相同数据和策略骨干下联合比较 DINO、3D flow、对象状态和接触事件表示"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# EGOWAM：跨本体迁移应优先共享世界变化而不是动作

## Why important

它把人类第一视角数据到机器人策略的迁移瓶颈定位为监督通道选择：动作标签混入形态和行为风格，而未来场景变化可能承载更本体无关的物理与任务信息。

## What changed

此前跨本体 VLA 更强调统一动作接口或数据混合；该材料提示应先选择能抽象外观、保持跨本体一致并分离相机运动的 world target，再讨论动作对齐。

## Surprising

该受控比较中像素重建迁移较弱，而 DINO 特征和 3D flow 的收益方向不同，说明“增加世界模型头”本身不够，预测目标的抽象层级决定迁移内容。

## Connections

- Shared mechanism: 都试图从多形态数据中保留任务语义和物理效果，同时隔离本体特有的执行因素
  Boundary: 连接只覆盖跨本体表示共享，不意味着世界监督可以替代机器人动作数据或解决控制精度
  Difference: 通用 VLA 侧重统一策略输入输出接口，EGOWAM 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式

## Conflicts

- 世界表示越抽象越可能丢失接触级控制细节；3D flow 与 DINO 的优势可能随任务分布变化

## Open questions

- 什么 world target 能同时保留接触动力学、分离 ego-motion 并跨不同机器人相机布局迁移？

## Possible mechanisms

- 辅助世界预测头让人类数据通过场景动力学而非不可执行动作更新共享视觉骨干

## Future directions

- 在相同数据和策略骨干下联合比较 DINO、3D flow、对象状态和接触事件表示
