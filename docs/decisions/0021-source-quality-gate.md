# ADR 0021：Source Availability 与 Content Quality Gate

- 状态：accepted
- 日期：2026-07-16

## 决策

编译前分别评估 `availability_status` 与 `content_quality`。deleted、login、anti-bot、boilerplate-only、too-short、corrupted、extraction-failed 默认禁止生成知识 proposal，但保留 immutable capture、质量派生记录和 recovery follow-up。质量结论是可重建派生数据，不回写 source fact。

## 结果

失效页面不会污染知识层，来源为何未编译仍可审计。
