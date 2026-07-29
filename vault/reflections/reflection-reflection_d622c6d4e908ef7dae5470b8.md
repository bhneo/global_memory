---
id: "reflection_d622c6d4e908ef7dae5470b8"
type: "reflection"
status: "active"
title: "Hy-Embodied-VLM：动作中心能力分类约束数据配方，而非直接输出控制"
created_at: "2026-07-21T17:45:08+08:00"
updated_at: "2026-07-21T17:45:08+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["embodied-ai", "vision-language-model", "action-reasoning"]
confidence: "medium"
source_ids: ["source_bd08e368730960f4f6ce19ca"]
relations: []
target_ids: ["input_e69b286ace68f56c81ab185b", "source_bd08e368730960f4f6ce19ca"]
input_id: "input_e69b286ace68f56c81ab185b"
created_by: "agent"
reflection_kind: "article"
importance: "medium"
why_important: "该模型用动作相关状态理解、动作转移推理、序列与自适应推理三个维度组织预训练和后训练数据，补充了具身 VLM 与闭环 VLA 之间的能力边界。"
what_changed: "具身 VLM 的价值可体现在动作前的状态与转移推理，但 benchmark 排名不能证明机器人闭环执行能力。"
surprising: "论文摘要和项目页报告约 30B 总参数、每 token 激活约 3B，并在 38 个具身相关 benchmark 中 19 项第一；当前抓取的论文来源只有 arXiv 摘要页，细节主要由配套仓库补充。"
connections: [{"shared_mechanism": "都以动作相关信息组织视觉语言表示。", "boundary": "具身 VLM benchmark 不等于连续动作生成、低层控制或真实安全验证。", "difference": "Hy-Embodied-VLM 输出状态与动作推理表征；VLA 概念进一步要求将观察和语言映射为可执行动作。"}]
conflicts: []
open_questions: ["动作中心 taxonomy 的每一维对下游真实机器人成功率分别贡献多少？"]
possible_mechanisms: ["按动作相关层次筛选数据可减少通用 VLM 表征与具身决策需求的错配。"]
future_directions: ["用冻结 probe、控制微调和真机闭环分别验证三类能力的迁移。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Hy-Embodied-VLM：动作中心能力分类约束数据配方，而非直接输出控制

## Why important

该模型用动作相关状态理解、动作转移推理、序列与自适应推理三个维度组织预训练和后训练数据，补充了具身 VLM 与闭环 VLA 之间的能力边界。

## What changed

具身 VLM 的价值可体现在动作前的状态与转移推理，但 benchmark 排名不能证明机器人闭环执行能力。

## Surprising

论文摘要和项目页报告约 30B 总参数、每 token 激活约 3B，并在 38 个具身相关 benchmark 中 19 项第一；当前抓取的论文来源只有 arXiv 摘要页，细节主要由配套仓库补充。

## Connections

- Shared mechanism: 都以动作相关信息组织视觉语言表示。
  Boundary: 具身 VLM benchmark 不等于连续动作生成、低层控制或真实安全验证。
  Difference: Hy-Embodied-VLM 输出状态与动作推理表征；VLA 概念进一步要求将观察和语言映射为可执行动作。

## Conflicts

None recorded.

## Open questions

- 动作中心 taxonomy 的每一维对下游真实机器人成功率分别贡献多少？

## Possible mechanisms

- 按动作相关层次筛选数据可减少通用 VLM 表征与具身决策需求的错配。

## Future directions

- 用冻结 probe、控制微调和真机闭环分别验证三类能力的迁移。
