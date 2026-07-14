# ADR 0009: Read-only contradiction audit

- Status: Accepted
- Date: 2026-07-14

## Context

结构化 evidence 允许同一 claim 保留支持和反对材料，typed relation 也允许 claim 显式互相矛盾。若系统自动降低置信度、修改 status 或试图选择“赢家”，会把证据冲突误当作可由规则解决的事实裁决，并违反人工审批与认知演化原则。

## Decision

1. 新增 `gm audit contradictions`，只扫描 canonical claim，不扫描或改变 pending proposal。
2. Audit 报告两类显式信号：同一 claim 的 `supports` 与 `contradicts` evidence 并存；claim 间 typed `contradicts` relation。
3. 输出保留 evidence 条目、claim 路径、状态和 relation 理由，使审阅者可以沿 source/provenance 回溯。
4. Audit 始终只读：不改写 Markdown、SQLite、confidence、status 或 relation，也不创建 proposal。
5. Audit 不推断隐含矛盾、不做自然语言语义裁决；更高阶的 synthesis 必须另行作为 proposal 设计。

## Consequences

冲突变为可见、可检索、可审阅的治理输入，而不会被系统静默清除。代价是输出可能含多个方向相反但均合理的材料；用户需要使用 source、适用条件和后续 proposal 做判断。

## Rejected alternatives

- 自动把有冲突的 claim 标为 contested：状态变化本身是知识修改，应经过 proposal 审阅。
- 按 evidence 数量投票：证据数量不代表质量、适用范围或来源可靠性。
- 让模型直接解决冲突：模型结论也必须以 proposal 形式接受人工审阅。
- 扫描纯文本自动猜测矛盾：会制造难以解释的误报，且不具备稳定 provenance。
