# Data Model

## M8 orthogonal state

| Dimension | Values | Question answered |
|---|---|---|
| Memory Tier | working, trusted, canonical, historical | Is this worth stable recall and retention? |
| Epistemic Status | established, supported, provisional, contested, hypothetical, open_question, partially_answered, exploratory_analogy, observed_anomaly, user_intuition, superseded, unknown | What is currently known? |

Examples: `trusted + open_question` is a durable unanswered question; `trusted + exploratory_analogy` is a retained heuristic, not factual equivalence; `trusted + contested` is important but conflicted. `status` remains a compatibility mirror of tier after migration; `legacy_status` preserves the prior value.

| M8 record | Location | Identity / validity |
|---|---|---|
| Consolidation Receipt | `vault/receipts/consolidation/` | object before/after hashes + source/evidence hashes + checks |
| Working Revision | `vault/memory/revisions/` | immutable revision ID, `revision_of`, previous version, change record |
| Version snapshot | `vault/archive/versions/` | SHA-256 of exact previous Markdown |
| Demotion Event | `vault/receipts/demotions/` | object + from/to dimensions + reason + version paths |
| Drift Report | report/CLI output | compared versions + evidence + drift type/severity/action |

## M7 memory lifecycle

| Tier | Location | Meaning | Writer |
|---|---|---|---|
| raw | `vault/raw/` | immutable captured evidence | capture only |
| derived | `data/derived/` | rebuildable extraction/index/assessment | tools |
| working | `vault/memory/` | usable, provenance-preserving, revisable | compiler/consolidator |
| trusted | `vault/memory/` | passed type-specific promotion policy | consolidator or explicit user action |
| canonical | knowledge/frontier/action | scarce stable commitment | promotion approval only |

Working metadata records creator/updater, compiler/model, source and candidate hashes, consolidation count, trust score/reasons, promotion history, locks and schema version. Exception and promotion cards are governance records, not knowledge facts.

## M6 objects and states

| Object | Durable role | Gate |
|---|---|---|
| Source quality | availability/content/extraction/authority derived assessment | blocks compile when invalid |
| Processing state | event/formal-data derived lifecycle | rebuildable, never capture fact |
| Bundle proposal | source-level review unit with metrics and items | pending/deferred/approved/rejected |
| Concept | stable reusable semantic node | create or update, avoid same-name duplicate |
| Claim | atomic testable assertion with evidence | compound/partial/degraded blocked |
| Question/Tension/Hypothesis | unresolved frontier | preserved, not auto-resolved |
| Analogy | cross-domain structural proposal | boundary and confidence required |
| Follow-up | primary-source/recovery task | auditable status history |

New relation edges carry type, target, reason, confidence, created_by and status. Context Pack adds `truth_layer`, `source_authority` and a verification view without changing underlying objects.

## 身份层

| 对象 | 身份来源 | 是否可共享 | 是否可覆盖 |
|---|---|---:|---:|
| Content object | 原始 bytes SHA-256 | 是 | 否 |
| Source record | kind + canonical locator SHA-256 | 否 | 否 |
| Knowledge object | 稳定语义 ID | 不适用 | 经门禁发布或人工批准的 proposal |
| Derived extraction | source + input hash + extractor/version hash | 是 | 是 |
| Logical work | 可靠外部标识或显式用户指定 | 否 | 仅经 enrichment proposal |
| Proposal | source + candidate hash | 同编译结果复用 | 状态可审计变化 |
| SQLite row | 从 Markdown ID 派生 | 不适用 | 可删除重建 |

Source identity 从单层扩展为两层：family 代表 canonical locator，version 代表该 family 在某个捕获时点的不可变证据。v1 保持原有 ID 兼容；v2 起的 ID 包含连续序号与 content hash 前缀。`previous_version_id` 构成可审计时间链，不使用覆盖表达网页变化。

Content object identity 只取决于原始 bytes 的 SHA-256。所有 capture channel 共用 `vault/raw/objects/sha256/<prefix>/<full-hash>`；`content_id` 固定为 `content_<full-hash>`。MIME、原始文件名和显示扩展名属于 source capture metadata，不参与物理对象身份。

Extraction 不是 source 或 raw：它保存抽取文本和页码边界，绑定 `source_id/content_id/input_sha256`，并由 extractor/version 派生稳定 ID。输入变化时旧 extraction 标为 stale；删除后可从 raw 重建。

Work 是 canonical metadata object，聚合多个 capture 的现实世界作品身份。它用 `source_ids` 和 `derived_from` 保留所有 capture，不反向改写 source。Work enrichment 继续走 proposal、diff、乐观并发和 approval recovery。

Compile Bundle 是一个 proposal 内的 item 集合。每项保存 `item_id/object_type/action/target/base/candidate/hash/decision/potential_conflicts`。Candidate 与 base 不可变；item revision 写新 candidate 并保留 revision history。一次批准选择的所有 item 共用 bundle recovery operation，避免部分成功被误认为完整提交。

Canonical update proposal 将 target 在提案时的完整 Markdown 复制为 base snapshot。Base 不是新的 canonical 版本，而是乐观并发令牌和审计证据；candidate 是建议结果，current 是审批时实际文件。只有 `hash(current) == hash(base)` 才允许 candidate 进入 canonical。

Approval recovery journal 不进入知识图，也不进入 Git。它是短生命周期的本地事务记录，保存已授权审批的确定输出和阶段。Knowledge/proposal Markdown 与 audit event 完成后，journal 可安全删除；存在 journal 表示审批尚未达到完整终态。

## 领域对象

- `knowledge/`：entity、concept、claim、pattern、comparison、synthesis。它们表达已确认的解释结构。
- `frontier/`：intuition、question、tension、analogy、hypothesis、anomaly。它们允许模糊、冲突和未证实内容长期存在。
- `action/`：project、decision、experiment、failure、opportunity。它们连接认识与行动。
- `proposal/`：Agent 或规则处理器提出的增量修改，不属于 canonical。

人的原始直觉首先作为 `personal-notes` raw source 原样保存。后续可以 proposal 形式创建 intuition，但不得覆盖原始文字；Agent interpretation、later reflection 和 open question 必须分节或分对象表达。

## Claim provenance

Claim 至少通过 `source_ids` 指向来源。新 claim 使用结构化 `evidence[]` 保存每条证据的 `source_id`、`location`、`excerpt`、`stance`（`supports` / `contradicts` / `context`）和理由；`applicability[]` 保存适用范围，`confidence` 表达当前判断强度，`uncertainty` 保留未决限制。旧 Markdown 可继续读取，新增或修改的 claim 应逐步补齐这些字段。`supports` 与 `contradicts` 可以并存，不允许用新证据静默抹掉旧主张。

`gm audit contradictions` 只读取 canonical claim：同一 claim 同时拥有 `supports` 和 `contradicts` evidence 时输出内部冲突；claim relation 的 `contradicts` 边输出跨 claim 冲突。审计结果不是真相层对象，也不改变任何状态。

Synthesis 是可批准的 canonical knowledge 对象，不是 audit 缓存。它从至少两个 claim 的显式材料生成，保存输入 claim ID/path/hash/status、聚合后的 `source_ids`，并以 `related_to` relation 保留输入边。输入 hash 在 approval 前重新验证，因此综合不会基于已改变的 claim 静默落库。

Relation discovery 是 proposal 元数据，不是知识图自动写入。它把 seed 与候选 claim 的可解释重叠信号和 hash 记录下来，供人决定是否另行创建关系更新 proposal。批准 relation discovery 不增加或删除任何 typed relation。

## 状态演化

典型状态：`proposal → provisional → confirmed → contested → superseded|archived`。`provisional` 已可检索但尚未人工确认；`confirmed` 表示用户显式确认，仍不代表客观真理。状态不是置信度。变化必须更新 `updated_at`、`change_reason`，必要时设置 `superseded_by` 和 `valid_during`。

## Context Pack

Context Pack 不是新的 knowledge object，也不进入 proposal/canonical 状态机。它是由明确 query、token budget 与当前本地索引临时生成的读取视图；每个入选项保留对象路径、文档 SHA-256、`source_ids`、内容片段和选择理由。它可以为 Agent 提供工作上下文，但不能替代检索、来源链或人工审批，也不得把命中内容解释为新增事实。

Profile、filters、relation depth 和 truncation report 都属于 Context Pack 请求/响应，不写入 truth layer。Evidence 以紧凑可定位视图随 claim 返回并计入预算。Relation expansion 只接受 depth 0..3、nodes 1..100，防止无边界遍历。

## 文件位置

位置表达职责，不表达永久身份。ID 在移动文件后保持不变。文件名包含 ID 以利于无索引检索；标题变化不应改变 ID。
