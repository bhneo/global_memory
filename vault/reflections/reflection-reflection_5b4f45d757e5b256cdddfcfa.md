---
id: "reflection_5b4f45d757e5b256cdddfcfa"
type: "reflection"
status: "active"
title: "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口"
created_at: "2026-07-20T11:53:47+08:00"
updated_at: "2026-07-20T11:53:47+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-rl", "vla", "online-rl", "representation-learning"]
confidence: "high"
source_ids: ["source_40700e61702f4b5a5765e11d"]
relations: []
target_ids: ["input_69f2cd71c59b17e7d4214346", "source_40700e61702f4b5a5765e11d"]
input_id: "input_69f2cd71c59b17e7d4214346"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 actor-critic 通过紧凑 RL token 在少量真机交互中适应精密阶段。"
what_changed: "VLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。"
surprising: "收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。"
connections: [{"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}]
conflicts: ["压缩表征提高样本效率，却可能丢失在线适应所需的细粒度状态；动作锚定保护先验，也会限制偏离原策略才能发现的行为。"]
open_questions: ["RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？"]
possible_mechanisms: ["紧凑 token 降低 critic 与 actor 的统计和计算负担，VLA 动作锚定使探索围绕已有可行行为展开。"]
future_directions: ["比较 token 容量、读出层位置、历史窗口和动作锚定强度对样本效率与策略偏移的影响。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口

## Why important

它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 actor-critic 通过紧凑 RL token 在少量真机交互中适应精密阶段。

## What changed

VLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。

## Surprising

收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。

## Connections

- Shared mechanism: 与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。
  Boundary: RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。
  Difference: RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。

## Conflicts

- 压缩表征提高样本效率，却可能丢失在线适应所需的细粒度状态；动作锚定保护先验，也会限制偏离原策略才能发现的行为。

## Open questions

- RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？

## Possible mechanisms

- 紧凑 token 降低 critic 与 actor 的统计和计算负担，VLA 动作锚定使探索围绕已有可行行为展开。

## Future directions

- 比较 token 容量、读出层位置、历史窗口和动作锚定强度对样本效率与策略偏移的影响。
