---
id: "reflection_743b2d2d30d2f822bf2bfb9f"
type: "reflection"
status: "active"
title: "FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口"
created_at: "2026-07-26T12:18:38+08:00"
updated_at: "2026-07-26T12:18:38+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["vla", "real-time-control", "autonomous-driving"]
confidence: "medium"
source_ids: ["source_d4762e0cf2330ab6ea00a521"]
relations: []
target_ids: ["input_c15fd9c8fb97e78e5e7d9c60", "source_d4762e0cf2330ab6ea00a521"]
input_id: "input_c15fd9c8fb97e78e5e7d9c60"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作把慢速语言与历史聚合、快速当前帧动作预测通过逐层 KV cache 接口解耦，并用随机陈旧性训练匹配异步部署分布；它把实时控制从单纯模型压缩问题改写为时间尺度、缓存一致性与新鲜观测融合的接口问题。"
what_changed: "此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支 token、缓存可增量等价更新且快分支在训练中见过滞后上下文时，异步复用才是可验证的系统契约。"
surprising: "同一 action expert 从 10 Hz 提升到 20 Hz 主要提高路线完成率与减少偏航/超时，而综合 driving score 未同步提高并伴随更多车辆碰撞暴露；控制新鲜度和安全驾驶质量不是同一指标。"
connections: [{"shared_mechanism": "FastSlow-LMDrive 与块内反应式力注入都保留慢速预训练先验，同时用更快、更新鲜的局部观测驱动轻量动作分支。", "boundary": "连接适用于慢上下文在多个控制 tick 内仍有用、快路径可独立读取当前传感且延迟分布可在训练中覆盖的任务。", "difference": "FastSlow-LMDrive 通过逐层视觉语言 KV cache 服务驾驶 waypoint expert；力注入概念通过近期六维力记忆修正接触动作块，安全变量与传感动力学不同。"}]
conflicts: []
open_questions: ["能否用快慢分支分歧和缓存年龄共同触发安全降级，并在长路线密集交通中减少完成率上升带来的碰撞暴露？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口

## Why important

该工作把慢速语言与历史聚合、快速当前帧动作预测通过逐层 KV cache 接口解耦，并用随机陈旧性训练匹配异步部署分布；它把实时控制从单纯模型压缩问题改写为时间尺度、缓存一致性与新鲜观测融合的接口问题。

## What changed

此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支 token、缓存可增量等价更新且快分支在训练中见过滞后上下文时，异步复用才是可验证的系统契约。

## Surprising

同一 action expert 从 10 Hz 提升到 20 Hz 主要提高路线完成率与减少偏航/超时，而综合 driving score 未同步提高并伴随更多车辆碰撞暴露；控制新鲜度和安全驾驶质量不是同一指标。

## Connections

- Shared mechanism: FastSlow-LMDrive 与块内反应式力注入都保留慢速预训练先验，同时用更快、更新鲜的局部观测驱动轻量动作分支。
  Boundary: 连接适用于慢上下文在多个控制 tick 内仍有用、快路径可独立读取当前传感且延迟分布可在训练中覆盖的任务。
  Difference: FastSlow-LMDrive 通过逐层视觉语言 KV cache 服务驾驶 waypoint expert；力注入概念通过近期六维力记忆修正接触动作块，安全变量与传感动力学不同。

## Conflicts

None recorded.

## Open questions

- 能否用快慢分支分歧和缓存年龄共同触发安全降级，并在长路线密集交通中减少完成率上升带来的碰撞暴露？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
