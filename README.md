# Global Memory

## M9.0 research signals

M9.0 adds append-only research annotations, connection feedback, explainable Project/Domain routing, explicit Activation, and local Research Digest/Map views. These signals describe attention, use and research value; they never change Trust, Epistemic Status, Receipt validity or Canonical. See `docs/RESEARCH_SIGNALS.md` and `docs/RESEARCH_ROUTING.md`.

## M9.0.1 quality closure

Routine Weekly maintenance consumes active Working/Trusted memory only. Historical
objects remain auditable but are excluded from routine consolidation. Unmarked web,
PDF and automated captures complete as searchable `source_only` records; only
bounded personal notes may use deterministic paragraph fallback. See ADR 0056.

## M8.1.2 trust boundary

- Receipt v2 fingerprints incoming and outgoing relations; a stale receipt is excluded from strict execution until explicitly re-consolidated.
- Canonical promotion writes a recoverable journal and requires a new `canonical_approved` Receipt v2 for final Canonical bytes.
- Generated Obsidian graph projections remain local/ignored; they are not Git truth-layer artifacts.

Global Memory 是本地优先、用户拥有、模型无关的长期记忆系统。Markdown、不可变 Raw 与治理记录是真相层；SQLite、Context Pack 和 Obsidian 页面都是可删除、可重建的派生层。

当前里程碑是 **M9.0 — Research Signals and Progressive Routing**。它建立在冻结的 M8.1.2 信任边界之上：Working 可以低成本演化；所有 Trusted 变化仍必须有 Receipt v2 与恢复日志；Canonical 仍只允许 Proposal/Exception + 用户明确批准。

## 当前工作流

```text
capture -> immutable Raw + Source
        -> bounded triage / extraction / quality
        -> compile -> Working
        -> real consolidation -> hash-bound Consolidation Receipt
        -> eligible Claim/Concept -> Trusted
        -> promotion card -> explicit user approval -> Canonical
```

新资料命中已有知识时必须声明 `support`、`refine`、`limit`、`contradict`、`supersede` 或 `metadata_only`。Trusted 的语义修改创建 Working Revision；冲突保留原对象和双方证据，标记 `contested` 并创建 Exception；任何降级都产生 Demotion Event。

## 快速开始

要求 Python 3.11–3.13。PowerShell 中 `gm` 可能被解析为 `Get-Member`，本仓库推荐始终使用脚本入口：

```powershell
cd $GM_ROOT
python -m pip install -e ".[test,pdf]"
.\scripts\gm.ps1 doctor
.\scripts\gm.ps1 capture-text --text "待保存材料" --comment "来源说明"
.\scripts\gm.ps1 triage --limit 25
.\scripts\gm.ps1 context "我的问题" --profile research --format markdown --token-budget 1200
```

例行导入默认停在 capture/triage；只有明确选中的材料才深编译：

```powershell
.\scripts\gm.ps1 triage <source-id> --compile-selected
.\scripts\gm.ps1 consolidate object <object-id>
.\scripts\gm.ps1 trust explain <object-id>
.\scripts\gm.ps1 trust requalify <trusted-object-id>
```

显式知识演化：

```powershell
.\scripts\gm.ps1 evolve <object-id> --change-type support --from-file candidate.md --reason "新增独立支持" --trigger-source <source-id>
.\scripts\gm.ps1 evolve <object-id> --change-type refine --from-file candidate.md --reason "适用边界改变"
.\scripts\gm.ps1 evolve <object-id> --change-type contradict --from-file candidate.md --reason "新 Primary Source 冲突"
```

维护与治理：

```powershell
.\scripts\gm.ps1 consolidate daily --limit 25
.\scripts\gm.ps1 consolidate weekly
.\scripts\gm.ps1 weekly
.\scripts\gm.ps1 audit drift
.\scripts\gm.ps1 exceptions
.\scripts\gm.ps1 promotions
.\scripts\gm.ps1 promotion approve <promotion-id> --lock
.\scripts\gm.ps1 recover
```

`consolidate weekly` first performs a bounded Daily admission catch-up (25
sources by default), so recently captured and triaged material is not silently
omitted when a Daily run was missed. Use `--admit-limit N` to change the bound,
or `--skip-daily-admission` for a review-only run. The catch-up may write
Working memory but never writes Canonical.

外部 provider 更新既有对象时必须返回 `action: "update"`、稳定 `target_id` 和明确 `change_type`。标题只用于展示，不再作为更新身份。Canonical 的 `support`、`metadata_only`、`refine`、`limit`、`contradict`、`supersede` 全部只生成 update Proposal；不会原地修改 Canonical。

`consolidation_count += 1` 不构成有效复核。Promotion 只承认检查完整、与当前对象 SHA-256 相符的 Consolidation Receipt。Question、Tension、Hypothesis、Analogy、Anomaly、Intuition 和 Synthesis 默认暂停自动 Trusted 晋升。

## Memory Tier 与 Epistemic Status

两个维度正交：

- `memory_tier`: `working | trusted | canonical | historical`
- `epistemic_status`: `established | supported | provisional | contested | hypothetical | open_question | partially_answered | exploratory_analogy | observed_anomaly | user_intuition | superseded | unknown`

例如 `trusted + open_question` 表示值得长期追踪但仍未回答；`trusted + contested` 表示值得保留但存在直接冲突。未知旧状态迁移为 `working + unknown`，绝不默认升级为 Canonical。

## Context Pack

```powershell
.\scripts\gm.ps1 context "问题" --profile execution --format markdown
.\scripts\gm.ps1 context "问题" --profile research --format markdown
.\scripts\gm.ps1 context "问题" --profile exploration --format markdown
```

每项显示 `memory_tier`、`epistemic_status`、confidence、source authority、evidence coverage/entailment、未解决冲突和最近 Consolidation。Execution 默认排除 hypothetical、exploratory analogy、unknown、低置信 Working Claim 与 degraded evidence；Research/Exploration 可以显式读取探索材料，但不会把它们改写成事实。

## 迁移、指标与重建

```powershell
.\scripts\gm.ps1 migrate epistemic-status --dry-run
.\scripts\gm.ps1 migrate epistemic-status
.\scripts\gm.ps1 migrate epistemic-status --verify
.\scripts\gm.ps1 metrics
.\scripts\gm.ps1 metrics --write-project-state
.\scripts\gm.ps1 status --machine-readable
.\scripts\gm.ps1 maintain --rebuild-derived
```

迁移在 `data/backups/` 自动备份，保留 `legacy_status`，可幂等重跑。指标由真实 Vault 计算，不在 README 手工维护活动数量。

## 验证

```powershell
python -m pytest
.\scripts\gm.ps1 doctor
.\scripts\gm.ps1 lint
.\scripts\gm.ps1 raw verify
python scripts\ci_acceptance.py setup --root .ci-vault --output artifacts\fixture.json
```

GitHub Actions 固定覆盖 Ubuntu/Windows × Python 3.11/3.12/3.13，并独立运行 pytest、doctor、schema/state/raw、migration、promotion、weekly、provider-driven incremental A→B→C、drift 和 Context truth-layer / strict-execution 验收。

## 安全边界

- 不可变 Raw 和 Source 不覆盖。
- Trusted 语义变化不直接覆盖原版本。
- Canonical 不自动降级；冲突只标记 contested 并进入 Canonical Exception。
- Drift Audit 可生成报告和 Exception，不自动重写 Trusted/Canonical。
- 当前不引入 embedding、向量库、图数据库、新写入 MCP、浏览器插件、Web UI 或多 Agent 框架。

从 [PROJECT_STATE.md](PROJECT_STATE.md) 查看当前快照；数据结构见 [SCHEMA.md](SCHEMA.md)；Consolidation 规则见 [docs/MEMORY_CONSOLIDATION.md](docs/MEMORY_CONSOLIDATION.md)；Agent 入口见 [docs/AGENT_INTEGRATION.md](docs/AGENT_INTEGRATION.md)。
