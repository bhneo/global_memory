# Global Memory Schema v0.17

## M6 knowledge graph extensions

- `source` capture fact remains immutable; processing state is derived from extraction, quality, proposals and events.
- Quality records separate `availability_status`, `content_quality`, `extraction_quality` and `source_authority`.
- Claims add `atomicity_status`, `evidence_coverage`, `quote_verification`, `evidence_entailment`, `claim_confidence` and `publication_gate`.
- Formal knowledge types include concept, claim, question, tension, hypothesis, analogy, anomaly, intuition and synthesis. `source_only` is a successful compile disposition.
- A bundle proposal owns `bundle_items[]`, metrics, follow-ups, duplicate/conflict findings and unresolved items. Candidate Markdown remains immutable; revisions point to new files.
- M6 typed relations require type/target/reason plus confidence, created_by and status on new proposal edges.
- `vault/followups/` stores primary-source and recovery tasks. `system/runs/` and `data/derived/` are rebuildable, non-truth layers.

所有对象是 UTF-8 Markdown，使用 YAML Frontmatter。实现当前输出 JSON-compatible YAML 值，以便零依赖解析；标准 YAML 工具和 Obsidian 仍可读取。

## 基础对象

```yaml
---
id: "concept_example"
type: "concept"
status: "proposal"
title: "示例概念"
created_at: "2026-07-14T00:00:00+08:00"
updated_at: "2026-07-14T00:00:00+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: []
relations: []
superseded_by: null
valid_during: null
change_reason: null
---
```

稳定 ID 不依赖标题或文件位置。对象类型包括：`source`、`work`、`intuition`、`entity`、`concept`、`claim`、`question`、`tension`、`analogy`、`hypothesis`、`project`、`decision`、`experiment`、`failure`、`opportunity`、`synthesis`、`proposal`。

## Derived extraction

Extraction 位于 `data/derived/extractions/`，不进入 canonical 索引。字段至少包括 `extraction_id`、`source_id`、`content_id`、`input_sha256`、`extractor`、`extractor_version`、`extracted_at`、`mime_type`、`language`、`page_count`、`character_count`、`status`、`warnings[]`。状态为 `ready`、`error` 或 `stale`。

## Logical work

Work 使用 `type: work`，保存 `work_type`、`canonical_title`、`authors[]`、`published_at`、`doi`、`arxiv_id`、`repository_url`、`version`、`language`、`aliases[]`、`same_work_as[]` 和 `supersedes_version`。多个 capture 通过 `source_ids` 关联；任何 enrichment 必须先生成 proposal。

## Typed relation

```yaml
relations: [{"type":"derived_from","target_id":"source_abc","reason":"由该来源第 3 节提出"}]
```

允许类型：`supports`、`contradicts`、`refines`、`analogous_to`、`derived_from`、`applied_in`、`raises`、`supersedes`、`related_to`。每条关系必须有目标和简短理由；弱关系宁缺毋滥。

## Source record

Source 除基础字段外必须包含：

- `source_kind`：`web`、`wechat`、`files` 或 `personal-notes`。
- `original_title`、`author`。
- `original_locator`、`canonical_locator`。
- `captured_at`、可空 `published_at`。
- `content_sha256`、`content_id`、`raw_content_path`。对象路径固定由完整内容哈希派生：`vault/raw/objects/sha256/<前2位>/<次2位>/<完整哈希>`。
- `mime_type`、`original_filename`、`display_extension`：只用于解释和显示，不参与 content identity。
- `save_reason`、`import_method`、`processing_status`、`content_type`。
- `source_family_id`：由 source kind 与 canonical locator 派生的版本族 ID。
- `version_number`：族内从 1 开始的连续序号。
- `previous_version_id`：上一版本 ID；v1 为 `null`。

`source record` 与 `raw content` 均通过独占创建写入。所有新 raw bytes 不分入口统一进入全局 object store；旧 `content/`、`blobs/` 仅作为迁移前兼容输入，迁移不自动删除。

## Proposal record

Proposal 额外包含 `proposal_kind`、`processor`、`action`、`target_id`、`target_path`、`reviewed_at`、`review_reason`。状态为 `pending`、`deferred`、`superseded`、`approved` 或 `rejected`。

Candidate revision 创建新的 proposal/candidate，不覆盖原 candidate。新 proposal 使用 `revision_of` 和 `supersedes` relation 指向旧 proposal；旧 proposal 使用 `superseded_by` 指向新 proposal。Update revision 在创建时重新捕获 current canonical 作为 base snapshot。

- `knowledge_compile` 具有 `candidate_path` 与 `candidate_sha256`。Candidate 自身状态必须为 `proposal`；批准后 canonical 状态改为 `confirmed` 并写入 `approved_via`。
- `knowledge_update` 具有 `base_path`、`base_sha256`、`candidate_path`、`candidate_sha256` 和 `change_reason`。审批时 current target hash 必须等于 base hash。
- `source_refresh` 具有 `previous_source_id`、`new_source_id`、旧/新内容哈希和原文 diff。批准只确认来源版本，不写 canonical knowledge。
- `model_candidate` 具有普通 candidate/base 字段和 `model_run`：`provider`、`model`、`prompt_version`、可空 `prompt_sha256`、`input_source_id`、`input_sha256`、`uncertainty`。它由用户显式提供的外部 candidate 生成，CLI 不调用 provider。
- `compile_bundle` 保存 `extraction_id/input_sha256`、编译前 `existing_context`、`bundle_items[]`、`contradiction_candidates`、`unresolved_items` 和 `provenance_validation`。每个 item 保存独立 target/base/candidate/hash、`decision` 与潜在冲突。Item decision 为 `pending/approved/rejected`。

Bundle approve 可以选择 item 子集。选中项先全部通过 candidate/base/current 校验，再由 `system/recovery/bundle-*.json` 以单一 operation roll-forward 写入；未选择项保持 pending。Item revision 不覆盖旧 candidate。

External JSON provider adapter 接受 item 列表或 `{"items": [...]}`。每项至少提供 `object_type/title/body`，可选 `span_start`；所有字段进入与 deterministic provider 相同的 schema、candidate、diff 和 proposal gate。JSON 文件本身不被自动复制到 canonical。

Update candidate 必须保持 target 的 `id`、`type`、`created_at`，并使用 `status: proposal`。可选 `proposed_status` 仅允许 `provisional`、`confirmed`、`contested`、`superseded`、`archived`；省略时保留 base canonical status。

Canonical knowledge 的信任状态分两级：

- `provisional`：来源与结构已通过自动门禁，可检索、可进入 Context Pack，但尚未得到用户人工确认。
- `confirmed`：用户显式核对并确认。`gm promote` 是从 `provisional` 到 `confirmed` 的唯一快捷晋升路径，并写入确认时间、操作者类型与审计事件。

`contested`、`superseded`、`archived` 继续表达争议、替代和归档生命周期。Proposal 的 `published` 表示其 candidate 已发布为 `provisional`；`approved` 只表示人工批准。

## Claim evidence and uncertainty

新建的 claim candidate 使用以下字段；为兼容已有 Markdown，旧 claim 可以暂时缺少这些字段，但一旦存在即由 schema 校验。

```yaml
confidence: "low" # unknown | low | medium | high
applicability: ["适用条件或范围；空列表表示尚未确认"]
uncertainty: "仍不能确认的限制、反例或信息缺口"
evidence:
  - source_id: "source_abc"
    location: "第 3 节，第 2 段"
    excerpt: "可回到 raw source 核验的简短摘录"
    stance: "supports" # supports | contradicts | context
    reason: "此证据为何支持、反对或仅提供背景"
```

每条 evidence 的 `source_id` 必须属于 claim 的 `source_ids`。`supports` 与 `contradicts` 可以同时存在；`context` 表示来源相关但尚不自动构成正反证据。`confidence` 不取代 `uncertainty`：前者是当前判断强度，后者保留未决限制。

新 evidence 使用 `evidence_id` 和 `evidence_kind`，允许：`quote`、`paraphrase`、`translation`、`table_value`、`figure`、`calculation`。共同 provenance 字段包括 `source_id`、可选 `work_id/content_id/extraction_id`、`page/section/span_start/span_end`、`verification_status`、`input_sha256`、`extractor/extractor_version`。Quote 必须逐字匹配 extraction span；paraphrase 不能标为 verbatim；translation 必须同时有 `original_text`、`translated_text` 和目标语言；table_value 必须保留单位；calculation 必须引用同一 claim 内存在的输入 evidence ID，并记录方法与结果。

`gm audit contradictions` 以 `evidence[].stance` 中同一 claim 的 `supports` 与 `contradicts` 并存、以及 claim `relations` 中类型为 `contradicts` 的边为输入。它是只读报告，不新增冲突字段，也不自动变更 claim status。

## Synthesis proposal

`synthesis` 是 canonical knowledge 对象类型。`deterministic_synthesis` proposal 必须具有至少两个 `input_claims` 条目；每项保存输入 claim 的 `id`、仓库相对 `path`、完整 Markdown `sha256` 与生成时 `status`。Candidate 的 `source_ids` 是全部输入 claim 来源的去重并集，并以 `related_to` relation 指向每个输入 claim。审批前会重验每个输入路径、ID、类型和 hash；变化时必须重新生成 proposal。

## Relation discovery proposal

`relation_discovery` 是无 candidate 的审阅 proposal，不写入 canonical。它保存 `discovery_inputs`（seed 与全部候选 claim 的 `id`、`path`、`sha256`）和 `discovery_candidates`。每个候选包含可解释 `signals`：`shared_source_ids`、`shared_tags`、`shared_relation_targets`、`shared_keywords`，以及由这些信号确定性计算的 `score`。批准前重验输入 hash；批准仅记录审阅结果，不自动添加 relation。

## 去重语义

- source family identity：`source_kind + canonical_locator` 的 SHA-256 派生稳定 ID。
- source version identity：族 ID、连续版本号与该次 content hash 共同构成；内容回退仍形成新版本。
- content identity：原始 bytes 的 SHA-256；不同来源可共享 content object。
- URL canonicalization：scheme/host 小写、默认端口移除、fragment 移除、query 排序、常见 tracking 参数移除。
- 重复 source 不创建第二份记录；不同 source 的相同内容保留两份 source record。
- 普通 capture 不刷新；显式 refresh 内容未变时复用最新版本，变化时只追加新版本。

## 真相层与派生层

`vault/` 和 raw content 是真相层。`data/indexes/global_memory.sqlite3` 中的 documents、relations 和 FTS5 均由 Markdown/raw 重建，不允许成为唯一数据载体。

SQLite documents 派生索引保存 title、aliases、tags、domains、body、type、status、source kind 与 provenance；FTS 对 metadata 字段赋予高于 body 的权重。`search` 结果必须返回 status 和 `match_reason`，关系扩展结果注明 depth、relation type 和起点。

## Operational recovery journal

`system/recovery/approve-<proposal-id>.json` 是审批中的本地事务材料，不是知识对象。字段包括 `journal_version`、`operation_id`、`phase`、target/proposal path、写前/写后 SHA-256、预期写后完整文本和 audit payload。Phase 依次为 `prepared`、`target_written`、`proposal_written`、`audit_written`、`index_rebuilt`。成功后删除；未完成时 `doctor` 必须报告。

## Lint contract

`gm lint` 只读取真相层和 proposal 材料。它校验 metadata、`source_ids`、typed relation、Obsidian-style wikilink、source raw hash、proposal candidate/base/target/hash 与 revision lineage。`errors` 代表失效或不一致，命令返回非零；孤立 canonical 页面和未引用的 candidate/base snapshot 是 `warnings`，不代表仓库损坏。

## Raw backup manifest

Raw manifest 是 UTF-8 JSON，当前 `manifest_version` 为 `1`，作用域固定为 `vault/raw`。每个条目含仓库相对 `path`、字节数 `bytes` 和内容 `sha256`。它覆盖 source Markdown 与 raw content/blob，但不覆盖 SQLite、日志、recovery journal 或 canonical Markdown。备份目录内 manifest 文件名固定为 `global-memory-raw-manifest.json`；恢复只接受该作用域内的条目，并拒绝路径越界、重复路径、大小或哈希不匹配。
