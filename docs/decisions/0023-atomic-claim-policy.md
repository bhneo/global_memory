# ADR 0023：Atomic Claim Policy

- 状态：accepted
- 日期：2026-07-16

## 决策

claim 编译后必须记录 `atomicity_status` 与 `evidence_coverage`。可可靠拆分时产生独立子 claim 和 evidence；不能可靠拆分时标记 `needs_split`。compound、partial/missing evidence 或 degraded extraction 不得直接批准为 confirmed。

## 结果

字符定位不再等同于完整蕴含，未来 support、refine 与 contradict 可以作用于更小断言。
