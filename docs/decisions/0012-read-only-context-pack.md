# ADR 0012: Read-only Context Pack with provenance and token budget

- Status: Accepted
- Date: 2026-07-14

## Context

长期记忆需要向具体 Agent 任务交付少量相关材料，但若把“交付上下文”做成新的 canonical 对象、自动摘要或隐藏缓存，就会混淆检索结果、派生视图与真相层。Context Pack 还必须在没有 tokenizer、embedding 或外部模型依赖的前提下可预测地控制大小。

## Decision

1. `gm context <query> --token-budget <n>` 是纯读取命令；不得写入 Markdown、SQLite、审计日志或 proposal。
2. 它只在当前检索命中中选择 `source`、`claim` 与 `synthesis`，以检索名次和对象类型作确定性排序，并在预算不足时裁剪内容或报告 omitted 项。直接入选的 source 默认只保留每个 append-only family 的最新版本；历史版本仍属于真相层，可由 `search`/`show` 显式回溯。
3. 每项必须输出相对路径、文档 SHA-256、显式 `source_ids`、内容片段、保守 token 估算和选择理由；source 还输出 raw content hash。
4. token 采用本地的中英文混合保守估算，不声称与任一模型 tokenizer 精确相同。
5. Context Pack 不能替代搜索、来源链、人工审批或事实判断；命中内容不会自动改变任何 canonical 状态。

## Consequences

系统获得一个可直接供 Agent 使用的上下文接口，同时仍可从每一项回到本地原文和 canonical 页面。代价是当前排序只有关键词检索与简单类型优先级；中文召回、source version 选择和关系排序将先通过真实语料验收，再决定是否扩展派生检索层。

## Rejected alternatives

- 把 Context Pack 保存为 canonical synthesis：会把一次任务的临时视图误写为长期知识。
- 自动模型摘要：会增加外部依赖，并把未审批解释混入读取路径。
- 无预算地返回所有命中：不能作为稳定、可控的 Agent 工作上下文。
