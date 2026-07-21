---
id: "reflection_c3b3e3b0cbbc4d820aa25ce5"
type: "reflection"
status: "active"
title: "CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化"
created_at: "2026-07-20T12:33:40+08:00"
updated_at: "2026-07-20T12:33:40+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "latent-action", "human-video", "contrastive-learning"]
confidence: "medium"
source_ids: ["source_f4bd7390e1b485ab773f1446"]
relations: []
target_ids: ["input_1c16eae7ffda2f7247ec7c34", "source_f4bd7390e1b485ab773f1446"]
input_id: "input_1c16eae7ffda2f7247ec7c34"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "CLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 latent action 被背景变化和外观噪声主导。"
what_changed: "人类视频规模本身不足以保证机器人迁移；若 latent space 没有机器人动作锚点，更多视频可能只增强视觉纠缠。对齐目标应明确表达物理可执行性。"
surprising: "论文把 object generalization 与 fine-tuning 后的知识保持分开处理：CLAP-RF 负责连续低时延动作，Knowledge Matching 约束域适配时不要遗忘预训练语义。"
connections: [{"shared_mechanism": "与 WALA 都把无动作人类视频映射到由机器人数据约束的 latent action 空间。", "boundary": "CLAP 对新物体的已知任务泛化强于仅靠人类视频学习全新任务；人手到平行夹爪的形态差异仍造成不可消除歧义，且当前 extraction 含少量乱码。", "difference": "CLAP 用机器人 VQ 动作词表与对比对齐；WALA 用未来语义和深度变化目标及 world-model 解码监督。"}]
conflicts: ["把人类动作压进机器人 codebook 提高可执行性，却可能丢弃人类视频中超出当前机器人形态的技能结构。"]
open_questions: ["何时应强制对齐到现有机器人动作词表，何时应保留尚不可执行但可用于未来本体的独立 latent？"]
possible_mechanisms: ["对比学习让视觉转移靠近物理动作 token，Knowledge Matching 在连续动作头后训练时约束中间知识不发生灾难性漂移。"]
future_directions: ["统一多阶段训练，并用形态差异分层评测对象泛化、任务泛化与真正跨本体迁移。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化

## Why important

CLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 latent action 被背景变化和外观噪声主导。

## What changed

人类视频规模本身不足以保证机器人迁移；若 latent space 没有机器人动作锚点，更多视频可能只增强视觉纠缠。对齐目标应明确表达物理可执行性。

## Surprising

论文把 object generalization 与 fine-tuning 后的知识保持分开处理：CLAP-RF 负责连续低时延动作，Knowledge Matching 约束域适配时不要遗忘预训练语义。

## Connections

- Shared mechanism: 与 WALA 都把无动作人类视频映射到由机器人数据约束的 latent action 空间。
  Boundary: CLAP 对新物体的已知任务泛化强于仅靠人类视频学习全新任务；人手到平行夹爪的形态差异仍造成不可消除歧义，且当前 extraction 含少量乱码。
  Difference: CLAP 用机器人 VQ 动作词表与对比对齐；WALA 用未来语义和深度变化目标及 world-model 解码监督。

## Conflicts

- 把人类动作压进机器人 codebook 提高可执行性，却可能丢弃人类视频中超出当前机器人形态的技能结构。

## Open questions

- 何时应强制对齐到现有机器人动作词表，何时应保留尚不可执行但可用于未来本体的独立 latent？

## Possible mechanisms

- 对比学习让视觉转移靠近物理动作 token，Knowledge Matching 在连续动作头后训练时约束中间知识不发生灾难性漂移。

## Future directions

- 统一多阶段训练，并用形态差异分层评测对象泛化、任务泛化与真正跨本体迁移。
