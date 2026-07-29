---
id: "reflection_e7c85185b496df7cb4ef1b85"
type: "reflection"
status: "active"
title: "REAL：把开放世界移动操作的非特权交互装进可部署评测契约"
created_at: "2026-07-21T18:09:11+08:00"
updated_at: "2026-07-21T18:09:11+08:00"
aliases: []
tags: ["reflection", "project"]
domains: ["embodied-ai", "mobile-manipulation", "benchmarking"]
confidence: "medium"
source_ids: ["source_a5f8ae205338d5f97eea87c7"]
relations: []
target_ids: ["input_41c7203faaf98b68b319eebc", "source_a5f8ae205338d5f97eea87c7"]
input_id: "input_41c7203faaf98b68b319eebc"
created_by: "agent"
reflection_kind: "project"
importance: "high"
why_important: "REAL公开仓库把原始RGB探索、用户澄清、导航与操作工具、任务YAML和模拟验证放到同一评测接口中，令“开放世界可部署”可以沿资产、工具协议和测试边界追溯，而不是只由摘要中的成功率表述。"
what_changed: "此前容易将MCP理解为模型连接器；该项目表明在移动操作中，工具协议、episode生命周期、任务配置与物理资产前提共同决定评测是否可复现。"
surprising: ""
connections: [{"shared_mechanism": "两者都把机器人决策封装在带检查和恢复边界的工具化执行流程中。", "boundary": "连接不表示REAL仓库已验证任何外部技能图或在缺少Isaac Sim资产时可直接复现实机结果。", "difference": "REAL定义具体仿真MCP工具、241项任务和在线RL/SFT流程；可验证机器人技能图是更抽象的任务编译与验证结构。"}]
conflicts: []
open_questions: ["当任务需要澄清意图时，如何分别报告语言澄清、视觉探索、工具执行和物理可达性对最终失败的贡献？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# REAL：把开放世界移动操作的非特权交互装进可部署评测契约

## Why important

REAL公开仓库把原始RGB探索、用户澄清、导航与操作工具、任务YAML和模拟验证放到同一评测接口中，令“开放世界可部署”可以沿资产、工具协议和测试边界追溯，而不是只由摘要中的成功率表述。

## What changed

此前容易将MCP理解为模型连接器；该项目表明在移动操作中，工具协议、episode生命周期、任务配置与物理资产前提共同决定评测是否可复现。

## Surprising

Not stated.

## Connections

- Shared mechanism: 两者都把机器人决策封装在带检查和恢复边界的工具化执行流程中。
  Boundary: 连接不表示REAL仓库已验证任何外部技能图或在缺少Isaac Sim资产时可直接复现实机结果。
  Difference: REAL定义具体仿真MCP工具、241项任务和在线RL/SFT流程；可验证机器人技能图是更抽象的任务编译与验证结构。

## Conflicts

None recorded.

## Open questions

- 当任务需要澄清意图时，如何分别报告语言澄清、视觉探索、工具执行和物理可达性对最终失败的贡献？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
