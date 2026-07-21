---
id: "reflection_a74b334857543499d8111c64"
type: "reflection"
status: "active"
title: "FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口"
created_at: "2026-07-20T12:32:53+08:00"
updated_at: "2026-07-20T12:32:53+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "world-action-model", "optical-flow", "action-representation", "video-pretraining"]
confidence: "high"
source_ids: ["source_ef80ef223077ef0855660839"]
relations: []
target_ids: ["input_5f966e5ff15622edf0829255", "source_ef80ef223077ef0855660839"]
input_id: "input_5f966e5ff15622edf0829255"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "FlowWAM 把 optical flow 从辅助视觉信号提升为主要动作表示：它既与预训练视频生成器的输入格式兼容，又保留逐像素跨帧运动，并可解码回机器人动作。"
what_changed: "此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。"
surprising: "跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。"
connections: [{"shared_mechanism": "与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。", "boundary": "光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。", "difference": "双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。"}]
conflicts: ["视频原生表示利于利用无标签视频，但二维像素运动可能把相机运动、物体运动与机器人本体运动混合，并丢失力和深度约束。"]
open_questions: ["在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？"]
possible_mechanisms: ["双流扩散在共享视频先验中耦合 RGB 与光流，光流计划提供稠密运动轨迹，动作解码器再把可见运动映射到控制空间。"]
future_directions: ["联合深度、相机运动补偿与接触信号，验证光流动作接口在长时程和跨本体条件下的可解码边界。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口

## Why important

FlowWAM 把 optical flow 从辅助视觉信号提升为主要动作表示：它既与预训练视频生成器的输入格式兼容，又保留逐像素跨帧运动，并可解码回机器人动作。

## What changed

此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。

## Surprising

跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。

## Connections

- Shared mechanism: 与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。
  Boundary: 光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。
  Difference: 双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。

## Conflicts

- 视频原生表示利于利用无标签视频，但二维像素运动可能把相机运动、物体运动与机器人本体运动混合，并丢失力和深度约束。

## Open questions

- 在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？

## Possible mechanisms

- 双流扩散在共享视频先验中耦合 RGB 与光流，光流计划提供稠密运动轨迹，动作解码器再把可见运动映射到控制空间。

## Future directions

- 联合深度、相机运动补偿与接触信号，验证光流动作接口在长时程和跨本体条件下的可解码边界。
