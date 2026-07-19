# Global Memory Schema v0.26

## M9.1 Cognitive Objects

`vault/inputs/` stores Input Episodes linked to immutable Sources.
`vault/reflections/` stores `truth_layer: reflection` interpretations with no
Memory Tier or Epistemic Status. `vault/synthesis/` stores
`truth_layer: cognitive_synthesis` Weekly pattern records, also without Memory
Tier. Neither layer is Evidence or execution-safe.

Reflection connections require `shared_mechanism`, `boundary`, and `difference`.
Candidate hypotheses require supporting Reflection/Source IDs,
counterarguments, a falsifier, and a possible experiment; their status remains
`hypothetical`. Full schemas are in `docs/COGNITIVE_CONSOLIDATION.md`.

## M9.0 Research Annotation

```yaml
id: annotation_<stable-hash>
type: annotation
status: active
annotation_kind: capture_intent # capture_intent | connection_feedback | research_note
target_ids: []
unresolved_target_ids: []
created_at:
created_by: user
user_authored: true
truth_layer: user_annotation
why_saved:
what_surprised_me:
possible_connections: []
research_projects: []
domains: []
personal_salience: unknown # low | medium | high | unknown
note:
feedback_label: null # obvious | forced | interesting | actionable
feedback_note:
supersedes_annotation_id: null
agent_interpretation: null
```

Annotation 是 append-only 用户信号，不参与 Trusted/Canonical Promotion，也不进入 Consolidation Receipt 指纹。修正必须创建新文件并引用旧 ID。

## M9.0 Activation Event

```yaml
event_id: activation_<stable-hash>
object_id:
event_kind: used # selected | opened | used | cited | coactivated
project_id:
query_hash:
context_pack_id:
reason:
created_at:
source: cli # cli | user | context_pack
coactivated_ids: []
```

事件位于本地 `system/logs/activation-events.jsonl`；SQLite `activation_events` 和 `activation_aggregates` 可重建。Activation 不改变知识 Markdown、Trust、Epistemic Status 或 Receipt。

## M9.0 Route Trace

Context Pack 增加 `route_trace`：`explicit_project`、`selected_project`、`project_candidates`、`selected_domains`、`seed_objects`、`relation_expansions`、`annotation_matches`、`fallback_used`、`raw_opened` 和 `selection_reasons`。它是只读解释信息，不是知识对象。

M9.0.1 中，Annotation 的 supersession 链保留全部 Markdown 历史，但默认消费 `active()` 返回的当前叶节点。Context 中的 Annotation payload 必须标为 `truth_layer: user_annotation`、`execution_safe: false` 和 `receipt_state: not_applicable`。

`source_only` 是 terminal compile disposition：它保留 Source/Raw/Extraction，不创建受治理知识对象，也不表示导入失败。

所有真相层对象是 UTF-8 Markdown + YAML Frontmatter。实现输出 JSON-compatible YAML；稳定 ID 不依赖标题或路径。

## 基础字段

```yaml
id: concept_example
type: concept
status: working
title: 示例概念
created_at: 2026-07-17T12:00:00+08:00
updated_at: 2026-07-17T12:00:00+08:00
aliases: []
tags: []
domains: []
confidence: unknown
source_ids: []
relations: []
```

`status` 保留为兼容字段；M8 知识对象的正式语义由以下正交维度表达：

```yaml
memory_tier: working # working | trusted | canonical | historical
epistemic_status: unknown # established | supported | provisional | contested |
                           # hypothetical | open_question | partially_answered |
                           # exploratory_analogy | observed_anomaly | user_intuition |
                           # superseded | unknown
```

活动 memory 还包含：`created_by`、`updated_by`、`consolidation_count`、`last_consolidated_at`、`last_consolidation_id`、`promotion_history`、`trust_score`、`trust_reasons` 与 `memory_schema_version`。

## Source 与 Raw

Source 是不可变捕获事实，至少包含 `source_kind`、original/canonical locator、captured/published time、`content_sha256`、`content_id`、`raw_content_path`、mime/import/save fields、source family/version chain。原始 bytes 位于：

```text
vault/raw/objects/sha256/<2>/<2>/<full-sha256>
```

相同 bytes 可被不同 Source 记录引用；Source provenance 不合并。Logical Work 通过稳定 `work_id` 聚合现实中的同一作品；独立性按 Work 而非 URL 数量计算。

## Claim Evidence

Claim 的晋升相关字段包括：

```yaml
atomicity_status: atomic # atomic | compound | uncertain
evidence_coverage: full  # full | partial | missing
evidence_entailment: full # full | partial | indirect | conflicting | none
extraction_quality: good # good | degraded | failed
epistemic_source_authority: primary # primary | official | peer_reviewed | secondary | commentary | anecdotal | unknown
claim_confidence: medium
applicability: [明确适用条件]
uncertainty: 仍未解决的限制
evidence:
  - evidence_id: evidence_...
    evidence_kind: quote
    source_id: source_...
    stance: supports # supports | contradicts | context
    verification_status: verified
    input_sha256: ...
```

Typed evidence 支持 quote、paraphrase、translation、table_value、figure、calculation。Quote 必须回到 extraction span；translation 不得伪装 verbatim；calculation 必须引用同 Claim 内已有 evidence IDs。

## Consolidation Receipt

Receipt v2 `relation_fingerprint` contains incoming, outgoing and full-neighborhood SHA-256 values. A direct contradiction in either direction invalidates a current receipt. Per-check details record `execution_status`, `validation_outcome`, and `semantic_recheck_performed`: metadata inspection is not semantic revalidation.

Canonical promotion journals live under `system/recovery/canonical-promotion-*.json`. They retain exact Trusted/Card pre-images and may roll forward only when a complete `canonical_approved` Receipt v2 matches the final Canonical bytes; otherwise recovery restores the bytes exactly.

Receipt 位于 `vault/receipts/consolidation/`，不可变并绑定对象前后哈希：

```yaml
consolidation_id: consolidation_...
object_id: claim_...
object_version_before: 1
object_sha256_before: ...
object_sha256_after: ...
source_ids: []
source_sha256s: []
evidence_ids: []
started_at: ...
completed_at: ...
consolidator: deterministic
consolidator_version: trustworthy-consolidation-v1
model_provider: none
model_version: none
checks:
  schema_validated: true
  raw_available: true
  provenance_revalidated: true
  evidence_revalidated: true
  evidence_entailment_rechecked: true
  duplicate_search_completed: true
  related_object_search_completed: true
  contradiction_search_completed: true
  freshness_checked: true
  source_independence_checked: true
  drift_checked: true
result: unchanged # unchanged | supported | refined | limited | contradicted |
                  # merged | superseded | demoted | promotion_candidate |
                  # needs_review | failed
changes: []
change_summary: No semantic change.
warnings: []
exceptions_created: []
promotion_recommendation: evaluate
```

只有所有规定 checks 为 true、Receipt 为 complete 且 `object_sha256_after` 等于当前文件哈希时，Promotion 才承认它有效。

## Change Record、Revision 与 Demotion

```yaml
change_type: support # support | refine | limit | contradict | supersede | metadata_only
previous_statement: ...
new_statement: ...
changed_fields: []
reason: ...
trigger_source: source_...
evidence_added: []
```

Trusted/Canonical 的 refine、limit、supersede 创建 `vault/memory/revisions/` 下的 Working Revision，包含 `revision_of`、`previous_version`、`needs_revalidation: true`。旧版本快照保存在 `vault/archive/versions/<object-id>/`。

显式降级记录位于 `vault/receipts/demotions/`：

```yaml
demotion_id: demotion_...
object_id: ...
from_tier: trusted
to_tier: working
from_epistemic_status: supported
to_epistemic_status: supported
trigger_source_ids: []
reason: ...
previous_version: ...
new_revision: ...
created_at: ...
created_by: user
exception_id: null
```

Canonical 不能自动降级。

## Context Pack v1

每个 item 至少显示 `truth_layer`、`memory_tier`、`epistemic_status`、confidence、source authority、evidence coverage/entailment、`unresolved_contradictions`、`last_consolidated_at`、路径、文件哈希、来源链和 selection reason。未知 legacy 状态映射为 Unknown，绝不回退到 Canonical。

## Drift Report

```yaml
drift_report_id: drift_...
object_id: ...
object_versions_compared: []
source_evidence_ids: []
drift_type: uncertainty-erasure
severity: high
original_statement: ...
current_statement: ...
evidence_summary: ...
reason: ...
recommended_action: create_exception
```

Drift Audit 是只读分析；High severity 通过 Exception 进入人工处理，不直接改写 Trusted/Canonical。

## 派生层与恢复

SQLite/FTS、Context Pack、Obsidian views、metrics 和 reports 可由 Markdown/Raw 重建。Approval recovery journals 位于 `system/recovery/`；迁移备份位于 `data/backups/`。派生层不能成为唯一真相源。
