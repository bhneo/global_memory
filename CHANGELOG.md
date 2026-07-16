# Changelog

## [0.18.0] - 2026-07-16

### Added

- 新增 `gm proposal split-item`：compound bundle item 可拆成至少两个独立 atomic candidates；校验来源边界、原 claim lineage、唯一 target 与候选 schema。
- 原 compound item 保留为 `superseded` 并记录 `split_into`；六个真实子 claim 继续保持 partial evidence 和 proposal gate，未写 canonical。

### Changed

- M6 corpus 当前为 65 个活动 items、26 个 atomic claims、0 个活动 compound claims；另保留 3 个 superseded compound 历史项。

## [0.17.1] - 2026-07-16

### Fixed

- Primary-source locator 现在会清理残缺脚注，并将 arXiv PDF、abstract 与版本 URL 归一为同一稳定任务身份。
- 新增默认 dry-run 的 `gm followup normalize-locators [--apply]`；应用迁移前备份受影响文件，旧 follow-up 保留为 `superseded`，proposal 引用同步去重，重复执行零变更。
- 真实 M6 corpus 的活动 follow-up 从 11 个纠正为 10 个；4 个旧记录迁移到 3 个规范记录，canonical writes 仍为 0。

## [0.17.0] - 2026-07-16

### Added

- M6 quality gate、source lifecycle、atomic claim gate、source-only disposition、typed knowledge objects、bundle review、primary-source follow-ups、epistemic dimensions 和 relation governance。
- `gm quality/source status/source history/review/followups/runs/migrate batch-artifacts/distill corpus` 命令，以及 9 场景 M6 acceptance demo。
- Context Pack 可在显式请求时展开 proposal bundle candidates，并标明 canonical/proposal/source-capture、authority、verification 与 relation/match reason。
- ADR 0020–0028。

### Changed

- `.tmp-batch-import` 经 dry-run、正式 proposal 匹配与备份后清理；临时目录不再是知识真相源。
- 33 个 source 的 143 个 model proposals 受控蒸馏为唯一 62-item corpus bundle；旧 candidate/proposal 历史保留为 superseded，未自动写 canonical。
- Windows CLI 输出固定为 UTF-8，避免包含特殊字符的 evidence/context JSON 编码失败。

### Known limits

- 23 条候选 claim 的 evidence entailment 尚未人工确认，均保持 partial；3 条 compound claim 保持 needs_split。
- 11 个 primary-source follow-up 尚未关闭，跨领域 analogy/synthesis 均只是待审 proposal。

所有重要用户可见变更记录在此。版本遵循语义化版本的意图，但在 `1.0` 前允许小步调整 CLI。

## [0.16.0] - 2026-07-15

### Added

- 新增 `gm capture-wechat` 与微信文章 URL 自动识别：单篇 `mp.weixin.qq.com/s/...` 可用移动端 UA 抓取、解析元数据并以 `source_kind: wechat` 写入 raw vault。
- 新增 `wechat-article-v1` extractor：优先从 `#js_content` 提取正文，改善公众号 HTML 的 `gm extract` 质量。

## [0.15.0] - 2026-07-15

### Added

- M5 第一阶段：新增跨 URL、文件与粘贴入口共享的全局 content-addressed raw object store。
- 新增 `gm raw verify` 与 `gm migrate raw-store --dry-run|--verify`，迁移支持自动 source 备份、本地 journal 续做和幂等重跑。
- Source capture 新增 MIME、原始文件名与建议显示扩展名；URL path 后缀不再决定物理对象类型。
- 新增 `gm extract`：支持文本/Markdown、HTML 正文、PDF 页码边界、中文编码降级、error/stale/rebuild。
- 新增 logical work enrichment proposal，同一 arXiv 的多个 capture 可审计聚合而不覆盖 source。
- Evidence schema 新增 quote、paraphrase、translation、table_value、figure、calculation；quote 可回验 extraction span。
- `gm compile` 升级为检索优先的 Compile Bundle，支持多类型候选、create/update 判定、潜在冲突、provenance report 和 provider-neutral 接口。
- Bundle review 支持 approve all、按 item approve/reject/revise，并用多目标 recovery journal 保证中断可恢复。
- Context Pack 新增 execution/research/exploration profile、组合使用、metadata filters、有限 relation traversal、evidence 视图和截断报告。
- Search 新增分字段加权、type/status/canonical/proposal 过滤与 match reason；`related-content` 准确替代对旧 discover 的 serendipity 表述。
- 新增 provider-neutral external JSON bundle adapter；模型环境只生成本地 JSON，核心继续负责 schema、proposal 和审批。
- 新增 Windows/Linux、Python 3.11–3.13 CI 矩阵及 M5 acceptance demo；本地真实 6 source extraction 已全部 ready。

### Changed

- 现有 6 个 source 已迁移到 5 个唯一 content object，保留旧 raw 文件且未删除 provenance。
- quickstart 验收 fixture 已从活动 vault 清理：source 归档、示例文件删除；`find_document` 与 `gm lint` 可解析归档 source 以维护 proposal 审计链。

## [0.14.0] - 2026-07-15

### Added

- 新增 `provisional` canonical trust level；合格结构化 claim 可经自动门禁发布并立即检索，但不等同人工确认。
- 新增 `gm promote`，由用户把 provisional 显式晋升为 confirmed。
- Search 与 Context Pack 返回知识状态，approval recovery 同时支持 provisional publication。

## [0.13.0] - 2026-07-15

### Changed

- Context Pack 默认排除 `archived` claim 与 synthesis；只被归档 canonical 引用且没有活动 canonical 引用的 source 也默认排除，使无效或测试知识完整退出活动上下文。
- 归档对象仍保留在 Markdown 真相层与索引中，可通过 `search`/`show` 回溯审计历史。
- 支持把需要物理清理的 archived canonical 移入不参与活动索引的 `vault/archive/`，以最小墓碑维持历史 proposal 的 target 审计链。

## [0.12.0] - 2026-07-14

### Added

- 新增 `gm discover <claim-id>`，基于共享来源、标签、关系目标和确定性关键词生成可解释关联候选。
- Discovery proposal 固化 seed/候选 claim hash，审阅期间输入变化会拒绝批准。
- 批准 discovery 仅记录已审阅，不自动写入或修改 canonical relation。

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
