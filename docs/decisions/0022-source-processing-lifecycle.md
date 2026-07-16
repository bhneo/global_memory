# ADR 0022：Source Processing Lifecycle

- 状态：accepted
- 日期：2026-07-16

## 决策

capture fact 保持不可变；processing state 从 extraction、质量、proposal、review 与事件派生为 captured、extracted、quality_checked、compile_pending、compiled、awaiting_review、partially_approved、completed、failed、deferred。Markdown 是事实/正式对象，event log 是审计轨迹，SQLite 是可重建索引。

## 结果

`gm status`、`gm inbox` 与 `gm source status/history` 不再把已有 proposal 的来源误报为 inbox。
