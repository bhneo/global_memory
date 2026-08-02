---
id: "reflection_f281f91cef2d68101060fe4a"
type: "reflection"
status: "active"
title: "N0-TWAM：把未来触觉从辅助目标提升为三流联合生成"
created_at: "2026-08-02T18:57:06+08:00"
updated_at: "2026-08-02T18:57:06+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "tactile-manipulation", "world-action-model", "mixture-of-transformers"]
confidence: "medium"
source_ids: ["source_d319d5007779569f8f786413"]
relations: []
target_ids: ["input_93da43408df65f059c3d8a5a", "source_d319d5007779569f8f786413"]
input_id: "input_93da43408df65f059c3d8a5a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "N0-TWAM 不再只用未来触觉作为隔离的辅助监督或压缩条件 token，而是用视觉、触觉和动作三个专家在共享注意力下共同生成三种未来。这给触觉原生的 world-action model 一个明确结构，同时保留当前局部触觉到动作分支的部署可用路径。"
what_changed: "我原先把 N0 系列的未来触觉主要理解为动作 expert 的紧凑 grounding；该实现显示另一条边界：未来视觉、触觉和动作可在统一 rectified-flow 目标下协同生成，而动作仍只接受当前局部触觉条件。"
surprising: "未来触觉被表示为相对首帧的全局残差生成目标，而当前局部触觉另经专用 encoder 注入动作 expert；同一模态的预测目标与控制条件采用不同接口。"
connections: [{"shared_mechanism": "N0-TWAM 与 concept_action_centered_joint_world_action_model 都用 Mixture-of-Transformers 联合生成未来视觉和动作。", "boundary": "当前来源是官方实现仓库，不能仅凭代码发布复述论文的全部性能与泛化结论。", "difference": "既有节点聚焦 GigaWorld 的视觉—动作联合模型，N0-TWAM 增加独立触觉 expert、未来触觉生成目标和当前局部触觉条件。"}, {"shared_mechanism": "N0-TWAM 与 concept_c5189a551eabdd0550bacd70 都利用未来触觉监督动作学习。", "boundary": "两者都不应被外推为已验证的在线力安全或任意硬件触觉等价。", "difference": "TacWAM 隔离未来目标以防泄漏，N0-TWAM 让三种未来在共享注意力中协同生成，但动作仅由当前局部触觉条件化。"}]
conflicts: []
open_questions: ["共享注意力中的未来触觉 token 如何避免成为训练时的动作捷径，同时仍允许三流预测真正交换因果相关信息？"]
possible_mechanisms: ["以 WAN2.2 为骨干建立视觉、触觉、动作三个专家，在对齐时间步上用统一 rectified-flow 损失联合生成，并把当前局部触觉经独立路径注入动作 expert。"]
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# N0-TWAM：把未来触觉从辅助目标提升为三流联合生成

## Why important

N0-TWAM 不再只用未来触觉作为隔离的辅助监督或压缩条件 token，而是用视觉、触觉和动作三个专家在共享注意力下共同生成三种未来。这给触觉原生的 world-action model 一个明确结构，同时保留当前局部触觉到动作分支的部署可用路径。

## What changed

我原先把 N0 系列的未来触觉主要理解为动作 expert 的紧凑 grounding；该实现显示另一条边界：未来视觉、触觉和动作可在统一 rectified-flow 目标下协同生成，而动作仍只接受当前局部触觉条件。

## Surprising

未来触觉被表示为相对首帧的全局残差生成目标，而当前局部触觉另经专用 encoder 注入动作 expert；同一模态的预测目标与控制条件采用不同接口。

## Connections

- Shared mechanism: N0-TWAM 与 concept_action_centered_joint_world_action_model 都用 Mixture-of-Transformers 联合生成未来视觉和动作。
  Boundary: 当前来源是官方实现仓库，不能仅凭代码发布复述论文的全部性能与泛化结论。
  Difference: 既有节点聚焦 GigaWorld 的视觉—动作联合模型，N0-TWAM 增加独立触觉 expert、未来触觉生成目标和当前局部触觉条件。
- Shared mechanism: N0-TWAM 与 concept_c5189a551eabdd0550bacd70 都利用未来触觉监督动作学习。
  Boundary: 两者都不应被外推为已验证的在线力安全或任意硬件触觉等价。
  Difference: TacWAM 隔离未来目标以防泄漏，N0-TWAM 让三种未来在共享注意力中协同生成，但动作仅由当前局部触觉条件化。

## Conflicts

None recorded.

## Open questions

- 共享注意力中的未来触觉 token 如何避免成为训练时的动作捷径，同时仍允许三流预测真正交换因果相关信息？

## Possible mechanisms

- 以 WAN2.2 为骨干建立视觉、触觉、动作三个专家，在对齐时间步上用统一 rectified-flow 损失联合生成，并把当前局部触觉经独立路径注入动作 expert。

## Future directions

None recorded.
