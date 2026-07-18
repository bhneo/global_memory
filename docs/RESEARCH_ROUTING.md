# Research Routing

`ResearchRouterService` 为 Context Pack 提供可解释的渐进式路由。顺序是：显式 Project、显式 Domain、Project/Goal/Question 匹配、Annotation 项目/领域信号、全局 FTS、有限 typed relation 扩展、按需打开 Evidence/Raw。

路由默认不扫描整个 Vault；relation depth 限制为 0–2。没有可靠 Project 时保留 Global Route，不为了形式强行选择项目。自动路由不创建或修改 Project。

Route Trace 至少包括：

```yaml
explicit_project:
selected_project:
project_candidates: []
selected_domains: []
seed_objects: []
relation_expansions: []
annotation_matches: []
fallback_used:
raw_opened: []
selection_reasons: []
```

```powershell
.\scripts\gm.ps1 research route "技能何时应该固化" --project embodied-agent
.\scripts\gm.ps1 context "技能何时应该固化" --profile research --project embodied-agent --route-trace --format markdown
```

`research route` 只输出计划，不生成 Context Pack、不写 Activation、不创建知识对象。Context 默认只读；只有 `--record-use` 才显式记录选中事件。
