# ADR 0024：Knowledge Object Classification

- 状态：accepted
- 日期：2026-07-16

## 决策

Compiler 支持 concept、claim、question、tension、hypothesis、analogy、anomaly、intuition、synthesis，并允许 `source_only`。Concept 使用稳定语义身份并增量更新；analogy 必须记录两域、共享结构、失效边界和置信度，默认仅为 proposal；tension 保留双方，不自动裁决。

## 结果

资料不再被统一压缩成孤立 claim，低价值来源也无需制造 canonical 节点。
