# Roadmap

## M5 — Real Knowledge Compilation（进行中）

- 全局 content-addressed raw store、完整性校验与可恢复迁移。（已完成）
- Derived extraction、logical work、evidence taxonomy。（下一步）
- Bundle compiler、选择性审批与原子 recovery。（已完成）
- Context Pack profiles、metadata filters 与有限关系遍历。（进行中）
- 跨平台 CI、重建演示和本地真实跨领域验证。（待实现）

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
- Obsidian 视图指南，但不把插件变成后端。

## 明确暂缓

图数据库、复杂前端、浏览器插件、微信全量抓取、多 Agent 框架、自动夜间任务、全库自动重写和复杂本体。
