# ADR 0004: Roll-forward recovery for canonical approval

- Status: Accepted
- Date: 2026-07-14

## Context

Canonical approval 需要依次修改 target、proposal、audit log 和派生索引。文件系统无法提供跨这些对象的原子事务；进程可能在任一步骤退出。仅靠 `doctor` 能发现不一致，却不能确定授权过的最终内容，也不能安全判断该回滚还是继续。

## Decision

1. 在写 canonical target 前，原子创建单个本地 recovery journal。
2. Journal 保存 target/proposal 的写前 hash、确定的写后完整文本与 hash、proposal ID、audit payload 和 operation ID。
3. 执行阶段固定为 target → proposal → audit → index；每阶段完成后原子更新 journal phase。
4. Recovery 采用 roll forward，因为 journal 只在用户明确批准并通过全部 candidate/concurrency 校验后创建。
5. 当前文件等于写前状态时执行写入，等于写后状态时跳过；第三种状态一律 blocked。
6. Audit 通过 operation ID 检测是否已写，防止恢复重试产生重复事件。
7. 索引可重建，因此恢复最后重建；全部步骤成功后删除 journal。
8. Journal 只保存在本地 `system/recovery/` 并排除 Git；它可能含私人候选正文。

## Consequences

审批不再依赖一次进程完整运行，跨文件部分失败可以确定性续做；中断后的人工作业不会被恢复器静默覆盖。代价是 journal 暂时重复 target/candidate 内容，并且 blocked 状态仍需要人工决定如何处理第三种状态。

## Rejected alternatives

- 无 journal，依赖人工看 diff 修复：无法可靠重建批准时的确定输出。
- 自动回滚 target：可能抹掉审批后产生的合法人工修改，且 audit/index 未必可逆。
- 把事务放入 SQLite：SQLite 不能原子提交 Markdown 文件，且不能成为真相源。
- 遇到第三种状态仍强制 roll forward：会违反并发保护并覆盖人工工作。
