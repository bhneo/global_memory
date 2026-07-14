# ADR 0005: Immutable candidate revisions

- Status: Accepted
- Date: 2026-07-14

## Context

人工审阅 proposal 时可能需要等待补充证据，或修改 candidate 后再批准。直接编辑已记录哈希的 candidate 会破坏原始 diff、审计证据和可复现性；把暂缓等同于拒绝，则会丢失仍有价值的审阅上下文。Update proposal 还可能在等待期间遇到 canonical 人工修改，旧 base 已不能安全使用。

## Decision

1. `deferred` 是可继续审阅状态，之后仍可 approve、reject 或 revise；暂缓不修改 candidate 或 canonical。
2. Revision 不覆盖原 candidate，而是创建新的不可变 candidate 和 pending proposal。
3. 旧 proposal 标记为 `superseded`，记录 `superseded_by`；新 proposal 记录 `revision_of` 和 typed `supersedes` relation。
4. Revision 必须说明 reason，并保持 target ID、类型、created_at 和 claim provenance。
5. Create revision 继续要求 target 不存在；update revision 在修订时读取 current canonical，并把它保存为新的 base snapshot。
6. Superseded proposal 不可再次批准或拒绝，避免旧 candidate 在新审阅链建立后生效。
7. Source refresh 没有 canonical candidate，不进入 candidate revision 工作流；它仍可 defer、approve 或 reject。

## Consequences

每次人工修订都有独立 hash、diff 和 lineage，旧审阅材料不会被静默改写。Update revision 同时承担显式 rebase，避免继承过期并发令牌。代价是 proposals 目录会保留更多小文件，状态集合增加 `deferred` 和 `superseded`，读取方必须识别这两个状态。

## Rejected alternatives

- 原地编辑 candidate 并更新 hash：会改写已经展示和审计过的提案证据。
- 将 defer 实现为带特殊理由的 reject：无法表达“以后继续审阅”。
- Revision 沿用旧 base：可能在批准时覆盖等待期间的人工 canonical 修改。
- 自动合并 old candidate 与 current：文本合并成功不能证明知识语义没有冲突。
