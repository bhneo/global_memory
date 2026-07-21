---
id: "reflection_7952be977c24d5dfe1da2072"
type: "reflection"
status: "active"
title: "图式 Agent Memory：生命周期完整不等于证据闭环完整"
created_at: "2026-07-20T12:27:17+08:00"
updated_at: "2026-07-20T12:27:17+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["agent-memory", "knowledge-graph", "memory-evolution", "evaluation", "global-memory"]
confidence: "medium"
source_ids: ["source_01ed2f19e91bb0eb1ec3ee92"]
relations: []
target_ids: ["input_9e35f15e22a7b1c0359635c3", "source_01ed2f19e91bb0eb1ec3ee92"]
input_id: "input_9e35f15e22a7b1c0359635c3"
created_by: "agent"
reflection_kind: "article"
importance: "high"
why_important: "这份综述把 Agent Memory 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测；它为检查 Global Memory 的认知链条是否缺环提供了外部分类框架。"
what_changed: "此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。"
surprising: "综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。"
connections: [{"shared_mechanism": "综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。", "boundary": "综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。", "difference": "综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。"}]
conflicts: ["图结构有利于关系推理，但无限积累和高连接度也会放大检索噪声、错误传播和隐私推断风险。"]
open_questions: ["怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？"]
possible_mechanisms: ["显式关系、时间与有效性元数据让更新和矛盾可定位；环境反馈则为仅靠内部一致性无法判断的真实性提供外部校验。"]
future_directions: ["把综述列出的 benchmark 缺口映射到 Global Memory 的 Context、Receipt、Exception 与 Activation 指标，形成不改写知识的评测清单。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 图式 Agent Memory：生命周期完整不等于证据闭环完整

## Why important

这份综述把 Agent Memory 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测；它为检查 Global Memory 的认知链条是否缺环提供了外部分类框架。

## What changed

此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。

## Surprising

综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。

## Connections

- Shared mechanism: 综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。
  Boundary: 综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。
  Difference: 综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。

## Conflicts

- 图结构有利于关系推理，但无限积累和高连接度也会放大检索噪声、错误传播和隐私推断风险。

## Open questions

- 怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？

## Possible mechanisms

- 显式关系、时间与有效性元数据让更新和矛盾可定位；环境反馈则为仅靠内部一致性无法判断的真实性提供外部校验。

## Future directions

- 把综述列出的 benchmark 缺口映射到 Global Memory 的 Context、Receipt、Exception 与 Activation 指标，形成不改写知识的评测清单。
