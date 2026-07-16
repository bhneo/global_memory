# ADR 0023：Atomic Claim Policy

- 状态：accepted
- 日期：2026-07-16

## 决策

claim 编译后必须记录 `atomicity_status` 与 `evidence_coverage`。可可靠拆分时产生独立子 claim 和 evidence；不能可靠拆分时标记 `needs_split`。compound、partial/missing evidence 或 degraded extraction 不得直接批准为 confirmed。

Bundle 内的可靠拆分使用显式 `split-item`：每个 child 必须是 atomic proposal claim、保留 `split_from`、且不得引入 parent 之外的 source。Parent 不删除，改为 `superseded` 并记录 `split_into`；child 仍分别经过 evidence 与 approval gate。拆分时不得把没有被分配 evidence 支持的原措辞复制到 child。

Primary-source 核验必须绑定已捕获 source、ready extraction、逐字匹配 span 和 section/page。通过核验只创建新的不可变 candidate revision，并可把该原子 claim 的 evidence coverage/entailment 提升为 full；它不等于用户批准，也不自动写 canonical。

## 结果

字符定位不再等同于完整蕴含，未来 support、refine 与 contradict 可以作用于更小断言。
