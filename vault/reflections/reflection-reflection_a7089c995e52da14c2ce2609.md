---
id: "reflection_a7089c995e52da14c2ce2609"
type: "reflection"
status: "active"
title: "主动真机因子评测：把部署鲁棒性估计变成序贯实验设计"
created_at: "2026-07-20T18:05:26+08:00"
updated_at: "2026-07-20T18:05:26+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "robot-evaluation", "active-learning"]
confidence: "medium"
source_ids: ["source_61152ca8210ad3913764a291"]
relations: []
target_ids: ["input_00e38de2e22eb93c2ecd0990", "source_61152ca8210ad3913764a291"]
input_id: "input_00e38de2e22eb93c2ecd0990"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "该工作把有限真机试验预算从固定测试套件转为围绕任务因子空间的信息增益分配，因此将部署评测的核心对象从单一成功率改为对失败区域和性能分布的不确定性估计。"
what_changed: "此前真机评测闭环强调可回放和归因；这里补充了试验选择本身也应由不确定性驱动，不能把少量便利条件下的成功率视为部署就绪度。"
surprising: "在三个任务和三类因子的实机研究中，作者报告主动选择通常比随机测试少用 20–40% 的试验；该结果只支持其评测设计空间和代理模型设置，不构成对所有机器人任务的保证。"
connections: [{"shared_mechanism": "两者都把真机 rollout 组织为可用于下一轮决策的结构化反馈。", "boundary": "连接只涉及评测闭环与试验预算分配，不把记录完整性等同于统计有效性。", "difference": "真机部署评估迭代闭环侧重日志、回放和训练反馈；该论文侧重由概率代理模型选择下一组因子配置。"}]
conflicts: []
open_questions: ["面对相关的相机、物体和初始状态因素时，代理模型的不确定性校准如何在不同机器人和任务之间验证？"]
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 主动真机因子评测：把部署鲁棒性估计变成序贯实验设计

## Why important

该工作把有限真机试验预算从固定测试套件转为围绕任务因子空间的信息增益分配，因此将部署评测的核心对象从单一成功率改为对失败区域和性能分布的不确定性估计。

## What changed

此前真机评测闭环强调可回放和归因；这里补充了试验选择本身也应由不确定性驱动，不能把少量便利条件下的成功率视为部署就绪度。

## Surprising

在三个任务和三类因子的实机研究中，作者报告主动选择通常比随机测试少用 20–40% 的试验；该结果只支持其评测设计空间和代理模型设置，不构成对所有机器人任务的保证。

## Connections

- Shared mechanism: 两者都把真机 rollout 组织为可用于下一轮决策的结构化反馈。
  Boundary: 连接只涉及评测闭环与试验预算分配，不把记录完整性等同于统计有效性。
  Difference: 真机部署评估迭代闭环侧重日志、回放和训练反馈；该论文侧重由概率代理模型选择下一组因子配置。

## Conflicts

None recorded.

## Open questions

- 面对相关的相机、物体和初始状态因素时，代理模型的不确定性校准如何在不同机器人和任务之间验证？

## Possible mechanisms

None recorded.

## Future directions

None recorded.
