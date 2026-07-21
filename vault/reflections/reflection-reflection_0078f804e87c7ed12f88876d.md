---
id: "reflection_0078f804e87c7ed12f88876d"
type: "reflection"
status: "active"
title: "B-spline Policy：把动作表示与执行速度从固定采样率中解耦"
created_at: "2026-07-20T12:27:49+08:00"
updated_at: "2026-07-20T12:27:49+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "visuomotor-policy", "action-representation", "fast-manipulation", "continuous-control"]
confidence: "high"
source_ids: ["source_4b25f596c34869693b9b8151"]
relations: []
target_ids: ["input_514023badd03fb20a731a56a", "source_4b25f596c34869693b9b8151"]
input_id: "input_514023badd03fb20a731a56a"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "BSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。"
what_changed: "此前动作块加速常被理解为少重规划或少执行几步；BSP 表明，动作表示本身可以把轨迹几何、控制频率和执行时标分离，从而在不为每个速度重训策略的情况下重定时。"
surprising: "在 Table Cleaning 的一个 4× 设置中，完成时间从 23.57 秒降至 11.80 秒且成功次数近似保持；但 Speed Stacking 在 4× 时成功率归零，清楚暴露出表示可重定时不等于硬件可无限加速。"
connections: [{"shared_mechanism": "与动态动作块执行时域都依据执行阶段调整重规划与动作执行之间的时间接口，以兼顾自由空间速度和接触阶段反应性。", "boundary": "BSP 的高倍加速受低层控制器、执行器和接触动态限制；论文结果不能推出任意策略或硬件都能保持几何轨迹后安全重定时。", "difference": "动态执行时域从离散动作块中选择执行前缀长度；BSP 直接改变策略输出为连续曲线，并通过时间缩放和段间对齐实现高速连续控制。"}]
conflicts: ["连续曲线和高频采样减少段间跳变，但更激进的时间缩放会把误差放大到低层控制器和物理约束无法跟踪的区域。"]
open_questions: ["能否依据接触风险、跟踪误差和策略不确定性在线选择 B-spline 时间缩放，而不是预设固定倍速？"]
possible_mechanisms: ["紧凑控制点表示保留轨迹几何，高频采样提供平滑控制命令，段间相位对齐减少异步推理造成的边界不连续。"]
future_directions: ["把时间缩放与动态执行时域、接触检测和控制器跟踪裕度联合起来，建立速度-鲁棒性闭环。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# B-spline Policy：把动作表示与执行速度从固定采样率中解耦

## Why important

BSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。

## What changed

此前动作块加速常被理解为少重规划或少执行几步；BSP 表明，动作表示本身可以把轨迹几何、控制频率和执行时标分离，从而在不为每个速度重训策略的情况下重定时。

## Surprising

在 Table Cleaning 的一个 4× 设置中，完成时间从 23.57 秒降至 11.80 秒且成功次数近似保持；但 Speed Stacking 在 4× 时成功率归零，清楚暴露出表示可重定时不等于硬件可无限加速。

## Connections

- Shared mechanism: 与动态动作块执行时域都依据执行阶段调整重规划与动作执行之间的时间接口，以兼顾自由空间速度和接触阶段反应性。
  Boundary: BSP 的高倍加速受低层控制器、执行器和接触动态限制；论文结果不能推出任意策略或硬件都能保持几何轨迹后安全重定时。
  Difference: 动态执行时域从离散动作块中选择执行前缀长度；BSP 直接改变策略输出为连续曲线，并通过时间缩放和段间对齐实现高速连续控制。

## Conflicts

- 连续曲线和高频采样减少段间跳变，但更激进的时间缩放会把误差放大到低层控制器和物理约束无法跟踪的区域。

## Open questions

- 能否依据接触风险、跟踪误差和策略不确定性在线选择 B-spline 时间缩放，而不是预设固定倍速？

## Possible mechanisms

- 紧凑控制点表示保留轨迹几何，高频采样提供平滑控制命令，段间相位对齐减少异步推理造成的边界不连续。

## Future directions

- 把时间缩放与动态执行时域、接触检测和控制器跟踪裕度联合起来，建立速度-鲁棒性闭环。
