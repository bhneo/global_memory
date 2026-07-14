# ADR 0001: Local-first, model-independent truth layer

- Status: Accepted
- Date: 2026-07-14

## Context

个人长期记忆的寿命应超过任何模型、应用、插件或云服务。聊天上下文难以完整导出；向量索引和数据库 schema 会变化；模型生成解释可能不准确。系统仍需要检索性能和未来模型能力，但不能把它们变成不可替代核心。

## Decision

1. UTF-8 Markdown、相对 raw content 和 Git 审计构成长期真相层。
2. Raw source 只追加，content object 以 SHA-256 定址，不允许普通流程覆盖。
3. SQLite FTS5 是可删除、可全量重建的派生索引。
4. 模型与规则处理器只生成 proposal；人工批准后才写 canonical knowledge。
5. Obsidian、Codex、Claude 和未来界面通过开放文件协议协作，不拥有核心状态。

## Consequences

好处是可迁移、可审计、可离线、可回溯，也降低单一供应商锁定。代价是文件系统跨对象事务较弱、批量查询不如专用图数据库直接、审批增加操作成本。我们接受这些代价，并优先通过原子文件写、恢复 journal、派生索引和渐进式检索改善体验。

## Rejected alternatives

- 以模型记忆或聊天历史为真相源：不可完整控制、导出和长期验证。
- 以 SQLite/向量数据库为唯一存储：降低人类可读性和迁移能力。
- 首期引入图数据库：在关系语义尚未稳定前增加运维和迁移成本。
- Processor 自动写 canonical：无法满足来源治理、认知演化和人工授权要求。
