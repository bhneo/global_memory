# Vault

## Graph 颜色图例

全局 Graph 默认展示 `views/graph/` 下可重建的人类语义图：节点名称来自标题，边来自真实对象的 `relations` 与 `source_ids`。它不会改写知识对象；Raw、Proposal、Receipt 与审计页也不会成为噪声节点。该派生图只影响 Obsidian 显示，不影响检索、Context Pack 或 Agent 使用。

- 蓝色：Claim
- 青色：Concept / Work
- 橙色：Question / Tension
- 紫色：Hypothesis / Analogy
- 绿色：Project / Experiment / Opportunity
- 灰色：Source

需要审计原始全图时，可在 Graph 的 Filters 中暂时清空过滤条件；每次 `gm obsidian build` 会随知识和来源变化同步重建语义图节点与边，但不会覆盖 `.obsidian/graph.json`。

`raw/` 保存来源与不可变内容；`knowledge/`、`frontier/`、`action/` 保存经批准 canonical 对象；`proposals/` 保存待审修改；`archive/` 保留退出活跃视图的历史。不要手工覆盖 raw，也不要绕过 proposal gate 修改 confirmed 对象。
