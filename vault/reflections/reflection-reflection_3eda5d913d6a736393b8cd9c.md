---
id: "reflection_3eda5d913d6a736393b8cd9c"
type: "reflection"
status: "active"
title: "WALA：用未来语义与几何变化约束可执行 latent action"
created_at: "2026-07-20T12:33:29+08:00"
updated_at: "2026-07-20T12:33:29+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "latent-action", "human-video", "future-dynamics"]
confidence: "high"
source_ids: ["source_2d5d59db178b1a20c9213220"]
relations: []
target_ids: ["input_4c84f520cc9c484797bde729", "source_2d5d59db178b1a20c9213220"]
input_id: "input_4c84f520cc9c484797bde729"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "WALA 不从原始像素重建 latent action，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta 提供语义—几何动力学监督，并用机器人动作标签把 latent 绑定到可执行控制。"
what_changed: "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。"
surprising: "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。"
connections: [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}]
conflicts: ["未来变化监督降低动作标签依赖，但相似视觉变化可能对应不同接触力、机器人姿态或可行控制。"]
open_questions: ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？"]
possible_mechanisms: ["冻结 encoder 提供稳定的未来变化目标，训练 decoder 充当 latent world model，机器人 action loss 再约束 policy latent 落到控制空间。"]
future_directions: ["在更多零样本任务和形态差异更大的人机视频上测量 latent 可执行性，而不仅是检索相似度或平均成功率。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# WALA：用未来语义与几何变化约束可执行 latent action

## Why important

WALA 不从原始像素重建 latent action，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta 提供语义—几何动力学监督，并用机器人动作标签把 latent 绑定到可执行控制。

## What changed

此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。

## Surprising

论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。

## Connections

- Shared mechanism: 与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。
  Boundary: WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。
  Difference: 跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。

## Conflicts

- 未来变化监督降低动作标签依赖，但相似视觉变化可能对应不同接触力、机器人姿态或可行控制。

## Open questions

- 未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？

## Possible mechanisms

- 冻结 encoder 提供稳定的未来变化目标，训练 decoder 充当 latent world model，机器人 action loss 再约束 policy latent 落到控制空间。

## Future directions

- 在更多零样本任务和形态差异更大的人机视频上测量 latent 可执行性，而不仅是检索相似度或平均成功率。
