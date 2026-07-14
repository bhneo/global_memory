# ADR 0006: Raw manifest and conflict-safe local backup

- Status: Accepted
- Date: 2026-07-14

## Context

`vault/raw/` 是 Global Memory 的不可变证据层。文本 raw 与 source Markdown 通常可由 Git 追踪，但二进制 blob 被 `.gitignore` 排除，且仅依赖 Git 不能证明外部备份是否完整。备份工具如果静默覆盖同路径不同内容，会破坏 raw append-only 约束；恢复工具如果直接写入，也可能覆盖恢复期间产生的本地内容。

## Decision

1. Manifest 覆盖 `vault/raw/` 的所有文件，包括 source Markdown、文本 content 与二进制 blob；每条记录仓库相对路径、字节数和 SHA-256。
2. `gm backup create` 只接受用户明确指定的仓库外本地目录。相同 hash 文件跳过；同路径不同 hash 是 conflict，不覆盖且不发布新 manifest。
3. 备份目录使用固定 `global-memory-raw-manifest.json`，`gm backup verify` 先校验其版本、作用域、路径边界、大小和 hash。
4. `gm backup restore` 默认 dry-run；只有 `--apply` 才写入，并且只恢复本地缺失文件。
5. 恢复发现任一同路径不同 hash 的本地文件时，不写入任何文件。成功恢复后从 Markdown/raw 重建 SQLite 索引。
6. 该机制只保护 raw truth layer；canonical Markdown、proposal、代码和 Git 历史仍由 Git 或独立仓库备份负责。

## Consequences

raw payload 可以从可验证的外部本地副本恢复，同时不会被备份或恢复过程静默改写。代价是用户要选择和维护外部备份位置；备份不包含加密、压缩、远端同步或 Git LFS 策略，这些在实际容量与隐私需求明确后再单独设计。

## Rejected alternatives

- 只备份 blob：丢失 source record 会破坏来源版本链与 provenance。
- 备份时直接覆盖目标：无法区分旧备份损坏与外部人工修改。
- 恢复默认立即写入：意外命令或错误路径可能扩大损失。
- 将备份目录放在仓库内：容易被误提交、递归包含或与真相层混淆。
