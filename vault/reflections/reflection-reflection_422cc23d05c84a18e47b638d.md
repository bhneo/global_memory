---
id: "reflection_422cc23d05c84a18e47b638d"
type: "reflection"
status: "active"
title: "PhySO GitHub：复现入口已由一手论文知识对象覆盖"
created_at: "2026-07-21T17:46:50+08:00"
updated_at: "2026-07-21T17:46:50+08:00"
aliases: []
tags: ["reflection", "project"]
domains: ["symbolic-regression", "physics", "open-source"]
confidence: "medium"
source_ids: ["source_a659477a1a8ac8bd6e3c3477"]
relations: []
target_ids: ["input_d79b943efae225d156e447cb", "source_a659477a1a8ac8bd6e3c3477"]
input_id: "input_d79b943efae225d156e447cb"
created_by: "agent"
reflection_kind: "project"
importance: "medium"
why_important: "仓库提供 Physical Symbolic Optimization 的安装、代码和示例，但同一项目的一手论文 arXiv:2303.03192 已有 Work 和 Claim。"
what_changed: "不应从 GitHub 页面再建一个 PhySO 概念；它只补充实现与复现 provenance。"
surprising: "旧 deterministic 对象只复制了 GitHub 标题，而没有复用既有论文 Work，正是本轮需要避免的重复模式。"
connections: [{"shared_mechanism": "论文和代码仓库描述同一符号回归系统。", "boundary": "代码可运行性不独立证明论文实验结论。", "difference": "论文是方法与结果的一手研究来源；GitHub 是实现、版本和使用入口。"}]
conflicts: []
open_questions: ["当前仓库版本是否仍能复现论文固定版本的基准？"]
possible_mechanisms: []
future_directions: ["需要复现时固定 commit 并关联既有 work_arxiv_2303_03192。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# PhySO GitHub：复现入口已由一手论文知识对象覆盖

## Why important

仓库提供 Physical Symbolic Optimization 的安装、代码和示例，但同一项目的一手论文 arXiv:2303.03192 已有 Work 和 Claim。

## What changed

不应从 GitHub 页面再建一个 PhySO 概念；它只补充实现与复现 provenance。

## Surprising

旧 deterministic 对象只复制了 GitHub 标题，而没有复用既有论文 Work，正是本轮需要避免的重复模式。

## Connections

- Shared mechanism: 论文和代码仓库描述同一符号回归系统。
  Boundary: 代码可运行性不独立证明论文实验结论。
  Difference: 论文是方法与结果的一手研究来源；GitHub 是实现、版本和使用入口。

## Conflicts

None recorded.

## Open questions

- 当前仓库版本是否仍能复现论文固定版本的基准？

## Possible mechanisms

None recorded.

## Future directions

- 需要复现时固定 commit 并关联既有 work_arxiv_2303_03192。
