---
id: "reflection_62e14da60b1cc35f28689c29"
type: "reflection"
status: "active"
title: "ActionCache：控制时记忆的价值取决于可校验的复用边界"
created_at: "2026-07-19T23:43:39+08:00"
updated_at: "2026-07-19T23:43:39+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vla", "inference-efficiency", "memory"]
confidence: "medium"
source_ids: ["source_291d6174cf92660287138f47"]
relations: []
target_ids: ["input_5cdcb4ea55f4352398dddd8c", "source_291d6174cf92660287138f47"]
input_id: "input_5cdcb4ea55f4352398dddd8c"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "ActionCache 展示了一种不改模型参数的控制时记忆：用多模态上下文键检索过去的中间动作，并保留生成模型的 refinement 作为纠错路径。它把延迟优化转化为记忆命中与安全回退问题。"
what_changed: "此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。"
surprising: "缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。"
connections: [{"shared_mechanism": "都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬", "boundary": "连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解", "difference": "ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合"}]
conflicts: ["上下文键的相似不保证动力学条件相同，错误缓存命中可能在低延迟下放大控制风险"]
open_questions: ["缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？"]
possible_mechanisms: ["相似条件下的生成轨迹位于相邻流形区域，缓存中间动作能缩短从噪声到目标动作的有效路径"]
future_directions: ["把缓存拒绝率、纠错幅度和闭环失败率作为统一的复用安全指标"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# ActionCache：控制时记忆的价值取决于可校验的复用边界

## Why important

ActionCache 展示了一种不改模型参数的控制时记忆：用多模态上下文键检索过去的中间动作，并保留生成模型的 refinement 作为纠错路径。它把延迟优化转化为记忆命中与安全回退问题。

## What changed

此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。

## Surprising

缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。

## Connections

- Shared mechanism: 都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬
  Boundary: 连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解
  Difference: ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合

## Conflicts

- 上下文键的相似不保证动力学条件相同，错误缓存命中可能在低延迟下放大控制风险

## Open questions

- 缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？

## Possible mechanisms

- 相似条件下的生成轨迹位于相邻流形区域，缓存中间动作能缩短从噪声到目标动作的有效路径

## Future directions

- 把缓存拒绝率、纠错幅度和闭环失败率作为统一的复用安全指标
