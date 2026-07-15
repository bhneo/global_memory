# Global Memory Agent Protocol

## Source of truth

本地仓库、Markdown 知识对象和不可变 raw source 是项目真相源。聊天上下文、模型记忆、SQLite、缓存和外部服务都不是最终真相源。

每次开始任务前必须依次读取：

1. `AGENTS.md`
2. `docs/VISION.md`
3. `docs/PRINCIPLES.md`
4. `docs/ARCHITECTURE.md`
5. `PROJECT_STATE.md`
6. 与当前任务相关的 `docs/decisions/` ADR

## Working method

- 先检查环境、仓库状态和未提交修改，再更新实施计划。
- 开始写操作前运行或检查 `gm doctor`；存在 approval recovery journal 时先用 `gm recover` 续做或报告 blocked，不得绕过 journal 继续修改同一 target。
- 每次完成一个清晰的纵向功能；保持小步、可测试、可回滚。
- 修改行为时同步修改测试；运行相关测试和全量测试后才能声称完成。
- 不默认扫描整个 vault；先读 `INDEX.md`、`SCHEMA.md`，再检索少量候选。
- 知识回答必须能回到 `source_ids` 和 raw content；AI 摘要不得替代来源。
- 逐字引用必须标为 `quote` 并回验 extraction span；转述、翻译、表格值、图示解释和计算不得伪装成原文 quote。
- Agent 只能创建 proposal。未经用户明确授权，不得直接修改 canonical knowledge。
- 任务结束更新 `PROJECT_STATE.md`；用户可见行为改变时更新 `CHANGELOG.md`。
- 重要且难以逆转的选择写 ADR；不为假想需求构建复杂抽象。
- 有意义的知识编译必须保留 source、文件 diff、claim、relation、冲突与理由。

## Safety boundaries

- 不得删除、覆盖或静默改写 `vault/raw/` 中的 source record 和 raw content。物理内容对象只能写入由完整 SHA-256 决定的 `vault/raw/objects/sha256/` 路径；capture kind 不得参与对象身份。
- 不得把模型生成内容伪装为用户原始判断。
- 不得未经审批修改 `vault/knowledge/`、`vault/frontier/` 或 `vault/action/` 中已确认对象。
- 不得将推测静默升级为事实；保留 `confidence`、适用条件和冲突证据。
- 不得未经用户明确授权访问仓库外私人目录或向外部服务发送私人资料。
- 不得无备份、无回滚方案执行破坏性数据库迁移。
- 不得在用户不知情时批量修改十个以上知识页面。
- 观点变化优先使用 `contested`、`superseded`、`archived`、`superseded_by` 和 `change_reason`，不得抹掉历史。

## Canonical write gate

允许写 canonical 的常规路径只有两种：合格 claim 经显式自动门禁发布为带 `published_via` 的 provisional；或 pending proposal 经人工查看 diff 后明确 approve，写入带 `approved_via` 的 confirmed/其他审阅状态。两者都必须记录 audit 并重建索引。修复 schema 或迁移 canonical 数据也必须先取得明确授权并提供可检查 diff。
