# Changelog

所有重要用户可见变更记录在此。版本遵循语义化版本的意图，但在 `1.0` 前允许小步调整 CLI。

## [0.11.0] - 2026-07-14

### Added

- 新增 `gm synthesize <claim-id> ...`，从至少两个 canonical claim 创建可审阅的 synthesis proposal。
- Synthesis 只汇总显式 evidence、范围、不确定性和冲突，不自动推断新事实或解决矛盾。
- Proposal 固化输入 claim hash；审批前任一输入变化都会拒绝批准并要求重新生成综合。

## [0.10.0] - 2026-07-14

### Added

- 新增只读 `gm audit contradictions`，报告 claim 内部 supports/contradicts evidence 并存。
- 同时报告 canonical claim 间显式 `contradicts` relation，并保留双方路径、状态和理由。
- Audit 不裁决冲突、不写入 Markdown/索引，也不修改 confidence 或 status。

## [0.9.0] - 2026-07-14

### Added

- 新增 claim `evidence[]`、`applicability[]` 和 `uncertainty` schema，区分 supports、contradicts 与 context evidence。
- 新规则 compile 生成可回到 raw 的 context evidence；新 model claim 必须提供完整结构化证据字段。
- 增加 confidence/evidence/applicability/uncertainty 的 metadata 校验，同时保持旧 Markdown 兼容读取。

## [0.8.0] - 2026-07-14

### Added

- 新增 `gm model-propose`，导入用户明确提供的外部模型 candidate，而不在仓库内调用任何 provider。
- Model proposal 记录 provider、model、prompt version/hash、输入 source/content hash 与不确定性。
- Model candidate 与现有不可变 candidate、diff、approval recovery 和 lint 审计共用同一治理路径。

## [0.7.0] - 2026-07-14

### Added

- 新增 `gm backup manifest|create|verify|restore`，为整个 `vault/raw/` 生成 SHA-256 manifest 并提供增量本地备份。
- Restore 默认 dry-run；`--apply` 只补齐缺失文件，同路径不同 hash 时拒绝覆盖并停止恢复。
- Backup 覆盖 source Markdown 与 content/blob，恢复后自动重建 SQLite；Git 继续负责 canonical Markdown 与代码历史。

## [0.6.0] - 2026-07-14

### Added

- 新增只读 `gm lint`，检查对象格式、关系/wikilink、claim 来源、raw hash 和 proposal 审阅材料。
- 将断链、哈希或 proposal 不一致作为 error；孤立 canonical 页面和未引用快照作为 warning。
- Lint 覆盖 candidate/base/target、revision lineage 和 source refresh 的来源引用，且不修改真相层或索引。

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
