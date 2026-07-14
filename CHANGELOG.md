# Changelog

所有重要用户可见变更记录在此。版本遵循语义化版本的意图，但在 `1.0` 前允许小步调整 CLI。

## [0.1.0] - 2026-07-14

### Added

- 建立本地优先、模型无关的项目文档、Agent 协议、ADR 与数据 schema。
- 增加 URL、文本、本地文件 capture 和不可变 raw 存储。
- 增加 canonical URL、source identity、content hash 三层去重语义。
- 增加 SQLite FTS5 搜索、来源回溯、typed relation 和可重建索引。
- 增加 compile proposal、内容级 diff、candidate 哈希、approve/reject 审批门。
- 增加 status、doctor、inbox、show、related 等 CLI 命令。
- 增加覆盖 Windows/中文路径、去重、不可变性、审批与失败恢复的自动测试。
