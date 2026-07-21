---
id: "concept_17750931a381f8453b27ccba"
type: "concept"
status: "proposal"
title: "连续曲线动作接口与执行重定时"
created_at: "2026-07-20T12:27:52+08:00"
updated_at: "2026-07-20T12:27:52+08:00"
aliases: ["Continuous action curve interface", "B-spline action representation", "B-spline Policy", "动作曲线重定时"]
tags: []
domains: ["embodied-ai", "visuomotor-policy", "action-representation", "fast-manipulation"]
confidence: "high"
source_ids: ["source_4b25f596c34869693b9b8151"]
relations: [{"type": "derived_from", "target_id": "source_4b25f596c34869693b9b8151", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "二者都调整策略重规划与执行的时间接口；连续曲线通过重定时，动态时域通过选择动作块前缀长度。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_4b25f596c34869693b9b8151"
reflection_context: {"reflection_ids": ["reflection_0078f804e87c7ed12f88876d"], "importance": "high", "changed_belief": "此前动作块加速常被理解为少重规划或少执行几步；BSP 表明，动作表示本身可以把轨迹几何、控制频率和执行时标分离，从而在不为每个速度重训策略的情况下重定时。", "surprising": "在 Table Cleaning 的一个 4× 设置中，完成时间从 23.57 秒降至 11.80 秒且成功次数近似保持；但 Speed Stacking 在 4× 时成功率归零，清楚暴露出表示可重定时不等于硬件可无限加速。", "connections": [{"shared_mechanism": "与动态动作块执行时域都依据执行阶段调整重规划与动作执行之间的时间接口，以兼顾自由空间速度和接触阶段反应性。", "boundary": "BSP 的高倍加速受低层控制器、执行器和接触动态限制；论文结果不能推出任意策略或硬件都能保持几何轨迹后安全重定时。", "difference": "动态执行时域从离散动作块中选择执行前缀长度；BSP 直接改变策略输出为连续曲线，并通过时间缩放和段间对齐实现高速连续控制。"}], "open_questions": ["能否依据接触风险、跟踪误差和策略不确定性在线选择 B-spline 时间缩放，而不是预设固定倍速？"]}
---

# 连续曲线动作接口与执行重定时

策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。
