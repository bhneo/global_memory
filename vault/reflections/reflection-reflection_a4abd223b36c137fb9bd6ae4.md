---
id: "reflection_a4abd223b36c137fb9bd6ae4"
type: "reflection"
status: "active"
title: "Mixture of Frames：动作分布复杂度部分来自坐标系选择"
created_at: "2026-07-20T12:33:06+08:00"
updated_at: "2026-07-20T12:33:06+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "diffusion-policy", "coordinate-frames", "bimanual-manipulation", "action-representation"]
confidence: "high"
source_ids: ["source_4df1017326dd7cc4786f4218"]
relations: []
target_ids: ["input_1b684ef1c9db92527f799f74", "source_4df1017326dd7cc4786f4218"]
input_id: "input_1b684ef1c9db92527f799f74"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "MoF 说明同一操作动作在夹爪、基座或相对轨迹坐标系中具有不同统计复杂度，且最合适坐标系会随任务阶段变化；策略可以并行去噪多个 frame 专家而非固定一个表示。"
what_changed: "此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture axis，表明动作模型难度有一部分是参数化造成的，而非任务本身不可约复杂度。"
surprising: "MoF 在部分任务上超过按整项任务选择最佳单 frame 的 oracle；路由权重随阶段变化较大的任务收益更高，论文报告两者具有正相关。"
connections: [{"shared_mechanism": "与跨本体通用 VLA 都需要把不同运动学参考系映射到统一的可执行动作接口。", "boundary": "MoF 依赖预先给定的候选 frame 和准确的 proprioceptive frame transform，当前证据集中于双臂移动操作，不能直接推出未知本体上的 frame 自动发现。", "difference": "跨本体通用 VLA 追求不同机器人共享输入输出协议；MoF 在单个机器人内部同时维护多个坐标系专家，并在同一扩散轨迹上融合噪声预测。"}]
conflicts: ["增加 frame 专家降低每个动作分布的建模难度，却提高参数量、路由误差和标定依赖。"]
open_questions: ["能否从数据中发现任务相关 frame，并把 frame transform 不确定性传播进扩散去噪与执行风险？"]
possible_mechanisms: ["共享 canonical diffusion state 保持专家同步，各专家在本地 frame 中建模更紧凑的动作分布，路由器按阶段融合其预测。"]
future_directions: ["比较人工 frame 集、可学习 frame 和不确定 frame 图，并测量收益是否来自阶段切换而非仅参数扩容。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Mixture of Frames：动作分布复杂度部分来自坐标系选择

## Why important

MoF 说明同一操作动作在夹爪、基座或相对轨迹坐标系中具有不同统计复杂度，且最合适坐标系会随任务阶段变化；策略可以并行去噪多个 frame 专家而非固定一个表示。

## What changed

此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture axis，表明动作模型难度有一部分是参数化造成的，而非任务本身不可约复杂度。

## Surprising

MoF 在部分任务上超过按整项任务选择最佳单 frame 的 oracle；路由权重随阶段变化较大的任务收益更高，论文报告两者具有正相关。

## Connections

- Shared mechanism: 与跨本体通用 VLA 都需要把不同运动学参考系映射到统一的可执行动作接口。
  Boundary: MoF 依赖预先给定的候选 frame 和准确的 proprioceptive frame transform，当前证据集中于双臂移动操作，不能直接推出未知本体上的 frame 自动发现。
  Difference: 跨本体通用 VLA 追求不同机器人共享输入输出协议；MoF 在单个机器人内部同时维护多个坐标系专家，并在同一扩散轨迹上融合噪声预测。

## Conflicts

- 增加 frame 专家降低每个动作分布的建模难度，却提高参数量、路由误差和标定依赖。

## Open questions

- 能否从数据中发现任务相关 frame，并把 frame transform 不确定性传播进扩散去噪与执行风险？

## Possible mechanisms

- 共享 canonical diffusion state 保持专家同步，各专家在本地 frame 中建模更紧凑的动作分布，路由器按阶段融合其预测。

## Future directions

- 比较人工 frame 集、可学习 frame 和不确定 frame 图，并测量收益是否来自阶段切换而非仅参数扩容。
