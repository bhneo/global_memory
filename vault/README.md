# Vault

## Graph 颜色图例

全局 Graph 默认只展示真实知识对象和显式关系；导航页、阅读视图、Raw、Proposal、Receipt、Exception 与审计页会被过滤，避免它们形成没有语义价值的超级节点。过滤只影响 Obsidian 显示，不影响文件、检索、Context Pack 或 Agent 使用。

- 蓝色：Claim
- 青色：Concept / Work
- 橙色：Question / Tension
- 紫色：Hypothesis / Analogy
- 绿色：Project / Experiment / Opportunity
- 红色：Canonical Knowledge / Frontier / Action

需要审计全图时，可在 Graph 的 Filters 中暂时清空过滤条件；`gm obsidian build` 不会覆盖 `.obsidian/graph.json`。

`raw/` 保存来源与不可变内容；`knowledge/`、`frontier/`、`action/` 保存经批准 canonical 对象；`proposals/` 保存待审修改；`archive/` 保留退出活跃视图的历史。不要手工覆盖 raw，也不要绕过 proposal gate 修改 confirmed 对象。
