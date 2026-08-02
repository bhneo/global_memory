---
id: "reflection_1ca77990ff946c0288b7704c"
type: "reflection"
status: "active"
title: "FA-RDP：让控制频率随任务歧义与接触阶段切换"
created_at: "2026-08-02T18:56:44+08:00"
updated_at: "2026-08-02T18:56:44+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "diffusion-policy", "force-control", "multi-rate-control"]
confidence: "high"
source_ids: ["source_1fa826244c5f3d4ea7f41541"]
relations: []
target_ids: ["input_88d51045aa7c71bb2fbb6205", "source_1fa826244c5f3d4ea7f41541"]
input_id: "input_88d51045aa7c71bb2fbb6205"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "FA-RDP 把扩散控制中的频率、预测时域和采样成本绑定到任务阶段：接触前用低频多步扩散保留多模态计划，接触后用高频单步蒸馏及时响应力反馈。这比固定频率或只缩短执行前缀更明确地处理了歧义消退与反馈带宽之间的冲突。"
what_changed: "我原先把高频控制主要理解为更频繁地重规划；该工作表明，频率切换还必须同步改变预测序列长度和采样器，否则高频多步扩散的计算预算会失控。"
surprising: "频率门由低频视觉 token 学习，而高频阶段每步刷新力输入并复用缓存的慢速上下文；快速反馈并不要求重算全部视觉语义。"
connections: [{"shared_mechanism": "FA-RDP 与 concept_dynamic_execution_horizon 都按任务阶段改变开环承诺长度，以平衡吞吐和反馈反应。", "boundary": "连接限于执行调度；两者都不保证基础策略支持域外的恢复或力安全。", "difference": "动态执行时域改变一个已生成动作块执行多少步，FA-RDP 同时切换 10/30 Hz、16/48 步预测和多步/单步生成器。"}, {"shared_mechanism": "FA-RDP 与 concept_multitimescale_tactile_world_model 都把慢速语义上下文和快速接触反馈分层。", "boundary": "FA-RDP 使用视觉与六维力，不能直接外推到触觉图像、长时任务分解或跨硬件触觉语义。", "difference": "既有概念以触觉子目标和残差控制组织多时间尺度，FA-RDP 以阶段歧义门切换扩散采样频率。"}]
conflicts: []
open_questions: ["当视觉歧义在接触后重新出现，或力信号在接触前已经关键时，二阶段门应如何校准和回退？"]
possible_mechanisms: ["从慢速视觉 token 预测多模态歧义状态，接触前执行低频多步扩散，歧义消退后切换到缓存语义上下文下的高频一步蒸馏。"]
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# FA-RDP：让控制频率随任务歧义与接触阶段切换

## Why important

FA-RDP 把扩散控制中的频率、预测时域和采样成本绑定到任务阶段：接触前用低频多步扩散保留多模态计划，接触后用高频单步蒸馏及时响应力反馈。这比固定频率或只缩短执行前缀更明确地处理了歧义消退与反馈带宽之间的冲突。

## What changed

我原先把高频控制主要理解为更频繁地重规划；该工作表明，频率切换还必须同步改变预测序列长度和采样器，否则高频多步扩散的计算预算会失控。

## Surprising

频率门由低频视觉 token 学习，而高频阶段每步刷新力输入并复用缓存的慢速上下文；快速反馈并不要求重算全部视觉语义。

## Connections

- Shared mechanism: FA-RDP 与 concept_dynamic_execution_horizon 都按任务阶段改变开环承诺长度，以平衡吞吐和反馈反应。
  Boundary: 连接限于执行调度；两者都不保证基础策略支持域外的恢复或力安全。
  Difference: 动态执行时域改变一个已生成动作块执行多少步，FA-RDP 同时切换 10/30 Hz、16/48 步预测和多步/单步生成器。
- Shared mechanism: FA-RDP 与 concept_multitimescale_tactile_world_model 都把慢速语义上下文和快速接触反馈分层。
  Boundary: FA-RDP 使用视觉与六维力，不能直接外推到触觉图像、长时任务分解或跨硬件触觉语义。
  Difference: 既有概念以触觉子目标和残差控制组织多时间尺度，FA-RDP 以阶段歧义门切换扩散采样频率。

## Conflicts

None recorded.

## Open questions

- 当视觉歧义在接触后重新出现，或力信号在接触前已经关键时，二阶段门应如何校准和回退？

## Possible mechanisms

- 从慢速视觉 token 预测多模态歧义状态，接触前执行低频多步扩散，歧义消退后切换到缓存语义上下文下的高频一步蒸馏。

## Future directions

None recorded.
