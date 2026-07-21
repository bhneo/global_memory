---
id: "reflection_bfb923cbbf75ed8a49f9df44"
type: "reflection"
status: "active"
title: "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎"
created_at: "2026-07-20T12:39:11+08:00"
updated_at: "2026-07-20T12:39:11+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "world-model", "data-engine", "multiview-generation", "robot-policy"]
confidence: "medium"
source_ids: ["source_fe986df678d73ef2b6234f0c"]
relations: []
target_ids: ["input_0c37ad2ab47dfef7536c9850", "source_fe986df678d73ef2b6234f0c"]
input_id: "input_0c37ad2ab47dfef7536c9850"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "U0 不把世界基础模型窄化为单一机器人视频预测器，而是联合保持通用图像生成、编辑、多视角具身场景、跨本体 transfer 和具身视频生成，使生成能力能直接扩充策略训练分布。"
what_changed: "此前常把具身 world model 视为预测下一帧或规划 rollout；该工作把 structured multi-view editing 也纳入世界模型接口，强调数据生成与动力学建模可以共享基础模型但需要不同一致性约束。"
surprising: "论文报告用零样本生成的多视角关键帧扩增数据后，π0.5 在所选真机 OOD 条件下成功率从 36.9% 提升到 63.2%，但这证明的是特定增广管线收益，不是生成视频已具备完整物理真实性。"
connections: [{"shared_mechanism": "与双系统 World Action Model 都复用视频生成先验来表示未来交互，并服务下游动作策略。", "boundary": "U0 的场景生成与视频生成仍分离，长 rollout 会累积误差；深度中间表示会引入细节伪影，32K context 也限制长时程。", "difference": "双系统 WAM 关注运行时快慢动作推理；U0 更像多任务具身合成基础模型和可控数据增广引擎。"}]
conflicts: ["保留通用视觉知识提高多样性，但视觉真实感和多视角一致性仍可能掩盖不可执行的接触或动力学。"]
open_questions: ["怎样用几何、接触和策略闭环指标筛掉视觉上合理但控制上有害的合成轨迹？"]
possible_mechanisms: ["通用与具身数据的联合自回归训练减少灾难性遗忘，结构化 transfer 在保持机器人与多视角约束时改变场景因素，从而扩展训练支持集。"]
future_directions: ["把场景与视频联合生成，并在生成数据进入策略训练前增加多视角几何、接触可行性和闭环收益门禁。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎

## Why important

U0 不把世界基础模型窄化为单一机器人视频预测器，而是联合保持通用图像生成、编辑、多视角具身场景、跨本体 transfer 和具身视频生成，使生成能力能直接扩充策略训练分布。

## What changed

此前常把具身 world model 视为预测下一帧或规划 rollout；该工作把 structured multi-view editing 也纳入世界模型接口，强调数据生成与动力学建模可以共享基础模型但需要不同一致性约束。

## Surprising

论文报告用零样本生成的多视角关键帧扩增数据后，π0.5 在所选真机 OOD 条件下成功率从 36.9% 提升到 63.2%，但这证明的是特定增广管线收益，不是生成视频已具备完整物理真实性。

## Connections

- Shared mechanism: 与双系统 World Action Model 都复用视频生成先验来表示未来交互，并服务下游动作策略。
  Boundary: U0 的场景生成与视频生成仍分离，长 rollout 会累积误差；深度中间表示会引入细节伪影，32K context 也限制长时程。
  Difference: 双系统 WAM 关注运行时快慢动作推理；U0 更像多任务具身合成基础模型和可控数据增广引擎。

## Conflicts

- 保留通用视觉知识提高多样性，但视觉真实感和多视角一致性仍可能掩盖不可执行的接触或动力学。

## Open questions

- 怎样用几何、接触和策略闭环指标筛掉视觉上合理但控制上有害的合成轨迹？

## Possible mechanisms

- 通用与具身数据的联合自回归训练减少灾难性遗忘，结构化 transfer 在保持机器人与多视角约束时改变场景因素，从而扩展训练支持集。

## Future directions

- 把场景与视频联合生成，并在生成数据进入策略训练前增加多视角几何、接触可行性和闭环收益门禁。
