---
id: "reflection_96809e9d9bffed57b211681f"
type: "reflection"
status: "active"
title: "JITOMA：场景记忆的成本控制应发生在构图时而非检索后"
created_at: "2026-07-25T18:08:55+08:00"
updated_at: "2026-07-25T18:08:55+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["scene-graphs", "robot-memory", "long-horizon-robotics"]
confidence: "medium"
source_ids: ["source_e8650c5afb7548268f649fb8"]
relations: []
target_ids: ["input_b6609528f21fa222b673f048", "source_e8650c5afb7548268f649fb8"]
input_id: "input_b6609528f21fa222b673f048"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "JITOMA 将长时程场景图的瓶颈表述为感知饱和：先构建全部细粒度语义再过滤会同时扩大延迟和推理噪声。它提出以低成本休眠锚点保留全局线索，仅在任务意图激活局部子图时生成高成本描述与功能推断。"
what_changed: "此前可能把场景图的任务相关性理解为构建完成后的查询或筛选问题；本文使我更重视资源分配时序本身，即哪些信息应只保留可唤醒索引，哪些信息值得在尚无任务需求时立即语义化。"
surprising: ""
connections: [{"shared_mechanism": "两者都要求把机器人内部结构组织成可按任务激活、且能保留验证边界的局部图。", "boundary": "该连接适用于长时程机器人在有限计算预算下维护结构化环境或技能状态的设计讨论，不证明 JITOMA 已在所有硬件和场景中带来端到端执行收益。", "difference": "JITOMA 管理的是场景观察到 3D 子图的感知与描述成本；既有技能图概念管理的是任务原语、检查点和恢复语义。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# JITOMA：场景记忆的成本控制应发生在构图时而非检索后

## Why important

JITOMA 将长时程场景图的瓶颈表述为感知饱和：先构建全部细粒度语义再过滤会同时扩大延迟和推理噪声。它提出以低成本休眠锚点保留全局线索，仅在任务意图激活局部子图时生成高成本描述与功能推断。

## What changed

此前可能把场景图的任务相关性理解为构建完成后的查询或筛选问题；本文使我更重视资源分配时序本身，即哪些信息应只保留可唤醒索引，哪些信息值得在尚无任务需求时立即语义化。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都要求把机器人内部结构组织成可按任务激活、且能保留验证边界的局部图。
  Boundary: 该连接适用于长时程机器人在有限计算预算下维护结构化环境或技能状态的设计讨论，不证明 JITOMA 已在所有硬件和场景中带来端到端执行收益。
  Difference: JITOMA 管理的是场景观察到 3D 子图的感知与描述成本；既有技能图概念管理的是任务原语、检查点和恢复语义。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
