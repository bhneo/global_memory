# Global Memory Agent Protocol

## M8 non-negotiable trust protocol

- Treat `memory_tier` and `epistemic_status` as independent. A Trusted Question remains `open_question`; a Trusted Analogy remains `exploratory_analogy`; `contested` is never a synonym for Canonical.
- Unknown legacy status is `working + unknown`. Never use an unknown-to-canonical fallback in retrieval, migration, rendering, or reasoning.
- `consolidation_count` is diagnostic only. Trusted Promotion requires a complete Receipt v2 whose `object_sha256_after` and full `consolidation_fingerprint` still match the current object. Receipt v1 remains audit history only.
- New evidence must declare `support`, `refine`, `limit`, `contradict`, `supersede`, or `metadata_only`. Unknown classification is `needs_review`, never implicit support. A contradiction needs source-linked contrary evidence, excerpt, and reason.
- Supporting evidence may update Trusted without resetting trust. Semantic changes create a Working Revision and preserve the old version. Conflict marks the object contested, retains both evidence sides, and creates an Exception.
- Every Trusted demotion requires a Demotion Event. Canonical never auto-demotes; create a Canonical Exception instead.
- Execution Context excludes hypothetical, exploratory analogy, unknown, degraded evidence and unverified Working Claims unless explicitly requested. Research/Exploration may include them with labels intact.
- Weekly must distinguish completed Receipts from scans and failures. Drift analysis may recommend action but must not rewrite Trusted or Canonical.

## Lightweight agent entry (M7)

- Codex, Cursor, and Claude use this same repository as one shared memory; tool-local instructions are adapters, not separate truth stores.
- Start from `vault/INDEX.md`, then request a bounded Context Pack with `gm context "<question>" --format markdown --token-budget 1200`. Do not scan the whole vault by default.
- Preserve each selected item's truth layer, status, evidence, source IDs, uncertainty, path, and selection reason. Follow raw/source links when a claim needs verification.
- `vault/views/` and Context Packs are rebuildable views. Canonical Markdown and immutable raw remain the durable truth layers.
- For durable write-back, create a concise session receipt with `gm receipt create --agent codex ...`, compile it, and let validated candidates enter Working memory. A proposal is audit material; it is no longer routine human homework.
- Receipt content should contain durable decisions, verified observations, changed assumptions, open questions, and sources—not transcript filler, secrets, or unsupported conclusions.
- Obsidian opens `vault/`; rebuild its navigation with `gm obsidian build`. See `docs/AGENT_INTEGRATION.md` and ADR 0029.
- Use `gm maintain` for a read-only maintenance check. `gm maintain --rebuild-derived` may refresh SQLite/Obsidian views only; neither mode authorizes canonical edits.
- On Windows PowerShell use `.\\scripts\\gm.ps1`; the bare name `gm` may resolve to the built-in `Get-Member` alias.
- Routine article import is capture-first. `triage` remains the cheapest source preparation step; `consolidate daily` automatically compiles prepared material into Working memory. Do not request per-article approval.
- Run `.\\scripts\\gm.ps1 consolidate weekly` for policy-backed Working review, Trusted promotion, drift audit, exceptions and canonical recommendations. Weekly never writes canonical automatically.
- Only `gm promotion approve <promotion-id>` may normally move Trusted memory into Canonical. `promote --to canonical` merely creates a review card.
- External assistants should use the read-only MCP tools documented in `docs/MCP_INTEGRATION.md`. MCP retrieval never grants capture, proposal, approval, rebuild, deletion, or canonical-write authority.

## M6 operating rules

- 每次 compile 前先过 source availability/content quality gate；无效来源保留 capture 并创建 follow-up，不制造知识。
- 不把所有材料压成 claim。先判断 concept/claim/question/tension/hypothesis/analogy/anomaly/intuition/synthesis 或 source-only。
- Claim 必须经过 atomicity 与 evidence coverage 检查；compound、partial/missing evidence、degraded extraction 不可直接 confirmed。
- 优先检索已有 concept/claim/question/tension/project，再选择 create/update/refine/support/contradict/supersede/link/defer/source-only。
- Bundle 是编译与审计单位；合格 item 可自动进入 Working，任何对象写 canonical 仍须 promotion gate。Analogy 必须保留 where_it_breaks。
- quote exact、extraction quality、source authority、evidence entailment 与 claim confidence 是不同维度，不得互相替代。
- `.tmp-*` 与 `system/runs/` 不是知识层；正式 candidate 只在 `vault/proposals/`。

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
- Agent 可创建 proposal 审计材料并自动物化 Working；未经用户明确批准 promotion card，不得修改 canonical knowledge。
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

允许写 canonical 的常规路径只有一种：Trusted 对象先生成 promotion card，再由用户执行 `gm promotion approve` 明确确认。自动 compile、daily、weekly、migration、drift audit 都不得写 canonical。修复 schema 或迁移 canonical 数据也必须先取得明确授权并提供可检查 diff。
