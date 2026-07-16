# ADR 0020：Batch Run Artifacts 与正式 Proposal 分离

- 状态：accepted
- 日期：2026-07-16

## 决策

正式知识路径固定为 raw/source/extraction → `vault/proposals/` → canonical。`system/runs/<run-id>/` 只保存可删除、可重建的 manifest、摘要、编译输出、校验、错误和指标；不得保存唯一 candidate。`.tmp-*` 不进入 Git。迁移必须先 dry-run、再备份、按对象 ID/哈希验证正式副本，最后才清理临时目录。

## 结果

运行现场不再成为第二真相源；proposal 审计链仍完整，run 可独立清理和重建。
