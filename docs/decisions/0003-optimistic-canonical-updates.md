# ADR 0003: Optimistic concurrency for canonical updates

- Status: Accepted
- Date: 2026-07-14

## Context

Proposal 创建后到人工批准前，用户或另一个 Agent 可能修改 canonical Markdown。若审批仍直接覆盖 target，会静默丢失人工工作。文件系统没有跨会话事务，Git diff 也不能替代运行时写入前检查。自动三方合并可能把语义冲突伪装成文本合并成功。

## Decision

1. 每个 canonical update proposal 保存提案时 target 的完整不可变 base snapshot，以及完整 candidate。
2. Proposal 记录 `base_sha256` 和 `candidate_sha256`；审批前重新核验两份 snapshot。
3. 审批时计算 current target hash，只有它仍等于 base hash 才允许写 candidate。
4. Current 变化时 proposal 保持 pending，拒绝覆盖，不自动合并。
5. `proposal show` 保留 Base→Candidate diff，并在冲突时动态增加 Base→Current diff。
6. 解决冲突的路径是审阅三方材料、基于 current 生成新 candidate、创建新 proposal。
7. Candidate 必须保持 target 的稳定 ID、类型和 `created_at`；claim 必须保留 provenance。
8. Candidate 用 `status: proposal` 表示尚未生效，可用 `proposed_status` 建议批准后的 canonical 状态。

## Consequences

并发人工修改不会被静默覆盖，proposal 本身保留完整审计材料。代价是冲突必须重新提案，且 base snapshot 会产生少量文件重复。我们接受该成本，优先保证认知治理和可恢复性。

## Rejected alternatives

- 审批时无条件覆盖：会丢失 proposal 创建后的人工修改。
- 只依赖 Git 工作区是否干净：无法证明特定 target 与提案时一致。
- 自动文本三方合并：文本无冲突不代表知识语义无冲突。
- 只存 base hash 不存 snapshot：无法在未来重建完整三方审阅材料。
