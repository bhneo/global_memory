# Changelog

所有重要用户可见变更记录在此。版本遵循语义化版本的意图，但在 `1.0` 前允许小步调整 CLI。

## [0.5.0] - 2026-07-14

### Added

- 新增 `gm proposal defer`；暂缓状态不会修改 candidate/canonical，之后仍可继续审阅。
- 新增 `gm proposal revise`；修订创建新的不可变 candidate/proposal，并用 supersedes lineage 保留旧审阅材料。
- Update revision 以 current canonical 重新建立 base snapshot，继续执行乐观并发保护。
- `status` 与 proposal 列表支持 `deferred`、`superseded` 状态。
- 修正文档中 recovery journal 仍属未来工作的过期描述。

## [0.4.0] - 2026-07-14

### Added

- 增加 canonical approval recovery journal 与阶段化 roll-forward。
- 增加 `gm recover`，幂等补齐 target、proposal、audit 和派生索引。
- Audit event 使用 operation ID 去重，重复 recovery 不重复写事件。
- `gm doctor` 和 `gm status` 显示 pending recovery journal。
- 增加 prepared、target、proposal、audit/index 失败及 create/update 故障注入测试。
- 第三状态和 journal payload 篡改会被阻断，不覆盖人工修改。

## [0.3.0] - 2026-07-14

### Added

- 增加 `gm propose-update`，从显式 Markdown candidate 创建 canonical update proposal。
- Update proposal 保存不可变 base/candidate snapshot 和 SHA-256。
- Approval 使用乐观并发检查，target 在审阅期间变化时拒绝覆盖。
- `proposal show` 在冲突时动态展示 Base→Candidate 与 Base→Current。
- 支持重新基于 current 提案，并验证 ID、类型、created_at、状态和 claim provenance。
- 原有 knowledge compile 的 update 分支也纳入同一基线保护。

## [0.2.0] - 2026-07-14

### Added

- 增加显式 `gm capture <url> --refresh`，普通 capture 行为保持不变。
- 增加 source family、连续 version、previous-version 链和内容回退历史。
- 增加 `source_refresh` proposal、旧/新原文 diff 和独立审批语义。
- `doctor` 检查版本号重复、previous 缺失、链不连续和 locator 不一致。
- 增加 refresh 未变化、变化、重复、回退、审批隔离和 CLI 抓取测试。

## [0.1.0] - 2026-07-14

### Added

- 建立本地优先、模型无关的项目文档、Agent 协议、ADR 与数据 schema。
- 增加 URL、文本、本地文件 capture 和不可变 raw 存储。
- 增加 canonical URL、source identity、content hash 三层去重语义。
- 增加 SQLite FTS5 搜索、来源回溯、typed relation 和可重建索引。
- 增加 compile proposal、内容级 diff、candidate 哈希、approve/reject 审批门。
- 增加 status、doctor、inbox、show、related 等 CLI 命令。
- 增加覆盖 Windows/中文路径、去重、不可变性、审批与失败恢复的自动测试。
