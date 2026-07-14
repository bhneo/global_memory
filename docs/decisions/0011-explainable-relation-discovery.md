# ADR 0011: Explainable relation discovery without automatic edges

- Status: Accepted
- Date: 2026-07-14

## Context

长期记忆需要保留跨领域偶然关联的机会，但自动添加 relation 会把弱相似性伪装为知识结构，并在没有可解释理由时污染图。向量或模型相似度也尚未满足本地可重建、隐私和审计边界。发现候选在审阅期间若输入 claim 变化，旧信号同样会失效。

## Decision

1. `gm discover <claim-id>` 只对 canonical claim 运行，使用共享 source IDs、tags、relation targets 和确定性 title/tag 关键词作为候选信号。
2. 每个候选保存完整 signals、确定性 score、输入 claim path/hash/status；没有任何信号时不创建 proposal。
3. Proposal approval 前重验 seed 与全部候选的 hash；任一变化时拒绝批准并要求重新发现。
4. Discovery proposal 不创建 candidate，不写 canonical，不自动添加 relation。批准只记录人工已审阅。
5. 人工若认为某关系有意义，必须通过独立 `propose-update` 提交 canonical relation diff 和理由。

## Consequences

系统能提出可回溯的意外关联，同时避免把统计重叠误作事实。代价是 relation 采纳需要额外一步，关键词信号也可能较弱或噪声；这些成本换来对关系质量和治理边界的控制。

## Rejected alternatives

- 自动写入 `related_to`：会让弱信号静默污染知识图。
- 黑箱 embedding 近邻：当前不满足可解释、可重建和隐私默认值。
- 只输出候选 ID：审阅者无法判断关联为何出现。
- 输入变化后仍批准：会确认基于过期材料的候选。
