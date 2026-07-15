# ADR 0016：Source Capture 与 Logical Work 分离

- 状态：accepted
- 日期：2026-07-15

## 决策

Source 永久表达具体捕获事件；work 表达现实作品身份。Work enrichment 通过 proposal 创建或更新，只聚合 `source_ids`，不修改 capture record。第一版只信任显式或可靠解析的 arXiv ID，不按模糊标题自动合并。

## 结果

本地 PDF、PDF URL 和 abstract 页面可以属于一个 work，同时各自 URL、文件名、渠道、时间与保存理由完整保留。无法可靠识别的 source 合法保持无 work 状态。
