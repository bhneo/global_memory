# ADR 0025：Source Bundle Review

- 状态：accepted
- 日期：2026-07-16

## 决策

主要审阅单位升级为 source/source-collection bundle。Bundle 汇总来源权威、质量、对象变更、关系、follow-up、重复、冲突、未提议项和 review cost；支持 high-confidence、指定 items、source-only、defer、reject。批准前验证所有目标、证据、原子性和 item 依赖，再由 recovery journal 原子续做。

## 结果

人工成本由逐条 claim 转向结构化变更包，同时不降低 canonical 门禁。
