# Global Memory Schema v0.6

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

稳定 ID 不依赖标题或文件位置。第一版对象类型：`source`、`intuition`、`entity`、`concept`、`claim`、`question`、`tension`、`analogy`、`hypothesis`、`project`、`decision`、`experiment`、`failure`、`opportunity`、`proposal`。

## Typed relation

```yaml
relations: [{"type":"derived_from","target_id":"source_abc","reason":"由该来源第 3 节提出"}]
```

允许类型：`supports`、`contradicts`、`refines`、`analogous_to`、`derived_from`、`applied_in`、`raises`、`supersedes`、`related_to`。每条关系必须有目标和简短理由；弱关系宁缺毋滥。

## Source record

Source 除基础字段外必须包含：

- `source_kind`：`web`、`files` 或 `personal-notes`。
- `original_title`、`author`。
- `original_locator`、`canonical_locator`。
- `captured_at`、可空 `published_at`。
- `content_sha256`、`content_id`、`raw_content_path`。
- `save_reason`、`import_method`、`processing_status`、`content_type`。
- `source_family_id`：由 source kind 与 canonical locator 派生的版本族 ID。
- `version_number`：族内从 1 开始的连续序号。
- `previous_version_id`：上一版本 ID；v1 为 `null`。

`source record` 与 `raw content` 均通过独占创建写入。文本内容按 hash 存在 `content/`；二进制在 `blobs/`，默认不提交 Git。

## Proposal record

Proposal 额外包含 `proposal_kind`、`processor`、`action`、`target_id`、`target_path`、`reviewed_at`、`review_reason`。状态为 `pending`、`deferred`、`superseded`、`approved` 或 `rejected`。

Candidate revision 创建新的 proposal/candidate，不覆盖原 candidate。新 proposal 使用 `revision_of` 和 `supersedes` relation 指向旧 proposal；旧 proposal 使用 `superseded_by` 指向新 proposal。Update revision 在创建时重新捕获 current canonical 作为 base snapshot。

- `knowledge_compile` 具有 `candidate_path` 与 `candidate_sha256`。Candidate 自身状态必须为 `proposal`；批准后 canonical 状态改为 `confirmed` 并写入 `approved_via`。
- `knowledge_update` 具有 `base_path`、`base_sha256`、`candidate_path`、`candidate_sha256` 和 `change_reason`。审批时 current target hash 必须等于 base hash。
- `source_refresh` 具有 `previous_source_id`、`new_source_id`、旧/新内容哈希和原文 diff。批准只确认来源版本，不写 canonical knowledge。

Update candidate 必须保持 target 的 `id`、`type`、`created_at`，并使用 `status: proposal`。可选 `proposed_status` 仅允许 `confirmed`、`contested`、`superseded`、`archived`；省略时保留 base canonical status。

## 去重语义

- source family identity：`source_kind + canonical_locator` 的 SHA-256 派生稳定 ID。
- source version identity：族 ID、连续版本号与该次 content hash 共同构成；内容回退仍形成新版本。
- content identity：原始 bytes 的 SHA-256；不同来源可共享 content object。
- URL canonicalization：scheme/host 小写、默认端口移除、fragment 移除、query 排序、常见 tracking 参数移除。
- 重复 source 不创建第二份记录；不同 source 的相同内容保留两份 source record。
- 普通 capture 不刷新；显式 refresh 内容未变时复用最新版本，变化时只追加新版本。

## 真相层与派生层

`vault/` 和 raw content 是真相层。`data/indexes/global_memory.sqlite3` 中的 documents、relations 和 FTS5 均由 Markdown/raw 重建，不允许成为唯一数据载体。

## Operational recovery journal

`system/recovery/approve-<proposal-id>.json` 是审批中的本地事务材料，不是知识对象。字段包括 `journal_version`、`operation_id`、`phase`、target/proposal path、写前/写后 SHA-256、预期写后完整文本和 audit payload。Phase 依次为 `prepared`、`target_written`、`proposal_written`、`audit_written`、`index_rebuilt`。成功后删除；未完成时 `doctor` 必须报告。

## Lint contract

`gm lint` 只读取真相层和 proposal 材料。它校验 metadata、`source_ids`、typed relation、Obsidian-style wikilink、source raw hash、proposal candidate/base/target/hash 与 revision lineage。`errors` 代表失效或不一致，命令返回非零；孤立 canonical 页面和未引用的 candidate/base snapshot 是 `warnings`，不代表仓库损坏。
