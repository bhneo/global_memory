# ADR 0008: Structured claim evidence and uncertainty

- Status: Accepted
- Date: 2026-07-14

## Context

仅靠 `source_ids` 和正文段落无法清楚表达证据在何处、它是支持还是反对、主张适用于什么条件，以及当前还缺少什么。把这些信息压缩为单一 `confidence` 或 canonical status 会把“判断强度”“证据方向”“适用范围”和“不确定性”混为一谈，并诱使后来的材料静默覆盖早期冲突。

## Decision

1. Claim 新增可选但受校验的 `evidence[]`、`applicability[]` 和 `uncertainty`；旧 Markdown 不强制迁移。
2. Evidence 的每条记录保存 `source_id`、位置、摘录、方向和理由，且 source 必须出现在 claim `source_ids` 中。
3. Evidence direction 只允许 `supports`、`contradicts`、`context`。正反证据可以并存，`context` 不构成自动事实判断。
4. `confidence` 只允许 `unknown`、`low`、`medium`、`high`；它表达当前判断强度，不能取代 `uncertainty`。
5. 规则 compile 只生成 `context` evidence；model claim 在导入时必须提交完整 evidence/applicability/uncertainty，以便人工审阅。

## Consequences

claim 可以逐条回到 raw，且冲突、范围与未知项保持可见，为后续 contradiction audit 和 synthesis 提供稳定输入。代价是新 claim candidate 的 frontmatter 更长，模型导入者需要提供更完整的结构化材料；我们以旧 Markdown 的兼容读取换取渐进迁移。

## Rejected alternatives

- 只把来源位置写进正文：机器无法可靠检查或审计。
- 用 `confidence` 表示冲突与例外：会掩盖不同证据方向和适用范围。
- 自动把最新证据标为 supports：规则/模型无法替代人工的语义判断。
- 立即迁移所有已有 claim：会造成未经审批的 canonical 批量修改。
