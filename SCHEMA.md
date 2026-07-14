# Global Memory Schema v0.1

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

`source record` 与 `raw content` 均通过独占创建写入。文本内容按 hash 存在 `content/`；二进制在 `blobs/`，默认不提交 Git。

## Proposal record

Proposal 额外包含 `processor`、`action`、`target_id`、`target_path`、`candidate_path`、`candidate_sha256`、`reviewed_at`、`review_reason`。状态为 `pending`、`approved` 或 `rejected`。Candidate 自身状态必须为 `proposal`；批准后 canonical 状态改为 `confirmed` 并写入 `approved_via`。

## 去重语义

- source identity：`source_kind + canonical_locator` 的 SHA-256 派生稳定 ID。
- content identity：原始 bytes 的 SHA-256；不同来源可共享 content object。
- URL canonicalization：scheme/host 小写、默认端口移除、fragment 移除、query 排序、常见 tracking 参数移除。
- 重复 source 不创建第二份记录；不同 source 的相同内容保留两份 source record。

## 真相层与派生层

`vault/` 和 raw content 是真相层。`data/indexes/global_memory.sqlite3` 中的 documents、relations 和 FTS5 均由 Markdown/raw 重建，不允许成为唯一数据载体。
