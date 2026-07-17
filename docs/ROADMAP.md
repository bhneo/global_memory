# Roadmap

## M8 — Trustworthy Consolidation and Incremental Knowledge Evolution

- P0 six-platform CI, independent diagnostics and artifacts: implemented and publicly green.
- Orthogonal Memory Tier / Epistemic Status, explicit Context mapping and migration: implemented and verified on the real vault.
- Hash-bound Consolidation Receipts and narrow Claim/Concept Promotion: implemented.
- Trusted support, Working Revision, conflict/Exception and explicit Demotion Event: implemented.
- Sequential A→B→C support/contradict acceptance and semantic drift interface: implemented in deterministic fixtures.
- Weekly report and generated metrics: implemented; final real-vault counts are generated, not hand-maintained.
- Milestone close gate: full local acceptance is complete; confirm the six CI jobs on the final commit.

M8 deliberately does not add embeddings, vector/graph databases, new MCP tools, browser ingestion, Web UI or multi-Agent orchestration.

Current handoff (2026-07-17): M7 automatic consolidation and promotion governance is implemented. Routine candidates become Working, policy-backed Weekly may produce Trusted memory and exception/promotion queues, and Canonical remains explicit human confirmation. The legacy pending corpus is migrated only after dry-run, backup and verification. Future work is real usage calibration of trust thresholds and review compression, not per-item approval.

## M6 — Knowledge Distillation and Graph Formation（已完成工程与首轮受控蒸馏）

- P0：batch runs/formal proposal 分离、quality gate、derived source lifecycle。（完成）
- P1：atomic claim、typed object/source-only、bundle review、authority/follow-up、epistemic dimensions、typed relations。（完成）
- P2：33-source corpus distillation，当前 66-item 活动 proposal graph，canonical writes 0。（完成）
- 验收：115 tests、doctor/lint/raw integrity、migration dry-run、M6 nine-scenario demo。（以本轮最终实测为准）
- M6.1：follow-up locator 规范化与 superseded lineage（活动任务 11 → 10）；3 个 compound claims 拆成 6 个 atomic children，原 item 保留为 superseded。（完成）
- 后续：partial-entailment 保持显式证据状态；按价值与可核验性选择性审阅 proposal，并继续导入真实资料。

## M7 — Agent Use and Maintenance（进行中）

- Codex/Cursor/Claude 轻量入口、Context Pack v1、receipt → proposal、Obsidian 可重建视图。（完成）
- Receipt 显式类型块无损编译，避免首句截断与强制人工 revision。（完成）
- 统一维护报告：完整性、积压、receipt、弱证据、陈旧对象和派生视图状态。（当前切片）
- 三个 Agent 各完成一次真实 read → task → receipt → proposal 验收。（Codex、Cursor 已完成；Claude 待真实使用）
- 新资料对已有 concept/claim 的 update/refine/support/contradict 候选，以及项目决策反馈和长期 contradiction 演化。（待实现）
- 知识复用统计与人工认可的跨领域连接验证。（待真实数据验证）

M7 不引入 embedding、图数据库、复杂前端、后台自动调度或自动 canonical 写入。

## M5 — Real Knowledge Compilation（进行中）

- 全局 content-addressed raw store、完整性校验与可恢复迁移。（已完成）
- Derived extraction、logical work、evidence taxonomy。（已完成）
- Bundle compiler、选择性审批与原子 recovery。（已完成）
- Context Pack profiles、metadata filters 与有限关系遍历。（已完成）
- 跨平台 CI 与重建演示。（已完成）
- 本地 20–30 份真实跨领域验证。（样本不足；随正常导入继续，不伪造完成）
- 本地真实跨领域知识复利验证仍随正常导入推进，不以 source 数量代替使用效果。

## M1 — 最小可信闭环（已完成）

- Capture URL、文本、本地文件。
- Raw 不可变、哈希、source/content 去重。
- Markdown source record、FTS5、来源回溯与索引重建。
- 规则 compile、proposal diff、approve/reject gate。
- Windows/中文路径、失败恢复和核心治理测试。

退出条件：`gm doctor` 通过、全量测试通过、真实仓库完成一条 capture → approve → search 演示。

## M2 — 版本与更新安全

- URL refresh 和 source version/changing-content 语义。（已完成）
- Source refresh diff proposal 与人工确认，且不触碰 canonical。（已完成）
- Canonical update proposal、乐观并发 hash、三方 diff。（已完成）
- 跨文件 approve recovery journal 与故障注入测试。（已完成）
- Proposal defer、不可变 candidate revision 与 supersedes 审阅链。（已完成）
- `gm lint`：schema、失效链接、无来源 claim、孤立页面、raw hash。（已完成）
- Raw manifest、增量备份与恢复演练。（已完成）

## M3 — 高质量编译与认知治理

- Provider-neutral model processor（先产 proposal）。（已完成：外部 candidate 导入边界，以及 provisional/confirmed 分级发布）
- Claim 定位、矛盾证据、适用条件和不确定性 schema。（已完成）
- Contradiction audit。（已完成）
- 可审阅 synthesis proposal。（已完成；自动周期调度暂缓）
- serendipity proposal。（已完成：可解释 relation discovery，自动建边暂缓）
- 人工修订 candidate 后创建新 proposal/hash 的明确工作流。（已完成）

## M4 — 渐进式检索

- Context Pack 接口与 token budget。（已完成：只读、可回溯、保守 token 估算）
- 更好的中文全文检索和 relation traversal ranking。
- 可选 embedding/向量索引评估；必须本地可重建且不成为真相源。
- Obsidian 可重建视图与指南。（已完成；插件继续暂缓）

## 明确暂缓

图数据库、复杂前端、浏览器插件、微信全量抓取、多 Agent 框架、自动夜间任务、全库自动重写和复杂本体。
