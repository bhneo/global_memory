---
id: "reflection_c5765c32f1c3dd7302da4906"
type: "reflection"
status: "active"
title: "TouchWorld：预测与反应必须处在不同控制时间尺度"
created_at: "2026-07-19T23:43:39+08:00"
updated_at: "2026-07-19T23:43:39+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "tactile", "world-model", "dexterous-manipulation"]
confidence: "medium"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: []
target_ids: ["input_dd10d4b6286ecf52c06c0361", "source_283911da72edc403d1b823fb"]
input_id: "input_dd10d4b6286ecf52c06c0361"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "TouchWorld 把慢速语义规划、中频动作块、触觉子目标预测和高频残差纠错拆开，说明世界模型的价值不只是预测准确，而是为正确时间尺度的控制回路提供目标。"
what_changed: "此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。"
surprising: "触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。"
connections: [{"shared_mechanism": "都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分", "boundary": "连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务", "difference": "TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示"}]
conflicts: ["分层回路提高响应性，但接口误差和跨层目标不一致可能引入新的稳定性问题"]
open_questions: ["预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？"]
possible_mechanisms: ["接触预测提供名义轨迹，高频触觉残差只修正局部偏差，从而降低单一模型同时承担长短时程推理的负担"]
future_directions: ["联合评估预测误差、残差幅度、重规划触发和接触失败之间的因果关系"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# TouchWorld：预测与反应必须处在不同控制时间尺度

## Why important

TouchWorld 把慢速语义规划、中频动作块、触觉子目标预测和高频残差纠错拆开，说明世界模型的价值不只是预测准确，而是为正确时间尺度的控制回路提供目标。

## What changed

此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。

## Surprising

触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。

## Connections

- Shared mechanism: 都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分
  Boundary: 连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务
  Difference: TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示

## Conflicts

- 分层回路提高响应性，但接口误差和跨层目标不一致可能引入新的稳定性问题

## Open questions

- 预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？

## Possible mechanisms

- 接触预测提供名义轨迹，高频触觉残差只修正局部偏差，从而降低单一模型同时承担长短时程推理的负担

## Future directions

- 联合评估预测误差、残差幅度、重规划触发和接触失败之间的因果关系
