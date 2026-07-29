---
id: "reflection_11d7846e1ebfa021b7ef74ac"
type: "reflection"
status: "active"
title: "Retriever：显式时钟把异步机器人闭环变为可复现程序"
created_at: "2026-07-22T18:11:26+08:00"
updated_at: "2026-07-22T18:11:26+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robot-systems", "embodied-ai"]
confidence: "medium"
source_ids: ["source_5260f9244a5030c2143c36e4"]
relations: []
target_ids: ["input_46bc94c55d2d67b754bd7fa5", "source_5260f9244a5030c2143c36e4"]
input_id: "input_46bc94c55d2d67b754bd7fa5"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "Retriever 将感知、信念更新、规划和控制之间常被隐含在回调与消息队列中的时序契约提升为显式图结构，因此为长时程机器人系统提供可检查的延迟、缓冲与重放边界。"
what_changed: "此前容易把异步执行当作部署细节；该工作表明输入消费语义和运行时钟会改变闭环行为，因而必须成为程序接口的一部分。"
surprising: ""
connections: [{"shared_mechanism": "两者都把机器人任务拆成带明确接口与验证点的可组合节点。", "boundary": "该连接只涉及运行时调度与输入同步，不证明任意技能节点的物理正确性。", "difference": "Retriever 定义多速率流和同步策略；技能图关注任务前置条件、验证与恢复语义。"}]
conflicts: []
open_questions: ["对感知延迟或时钟漂移的最小可复现测试集应如何定义？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Retriever：显式时钟把异步机器人闭环变为可复现程序

## Why important

Retriever 将感知、信念更新、规划和控制之间常被隐含在回调与消息队列中的时序契约提升为显式图结构，因此为长时程机器人系统提供可检查的延迟、缓冲与重放边界。

## What changed

此前容易把异步执行当作部署细节；该工作表明输入消费语义和运行时钟会改变闭环行为，因而必须成为程序接口的一部分。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都把机器人任务拆成带明确接口与验证点的可组合节点。
  Boundary: 该连接只涉及运行时调度与输入同步，不证明任意技能节点的物理正确性。
  Difference: Retriever 定义多速率流和同步策略；技能图关注任务前置条件、验证与恢复语义。

## Conflicts

None recorded.

## Open questions

- 对感知延迟或时钟漂移的最小可复现测试集应如何定义？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
