---
id: "proposal_2bb6bb64b38a86a24375d750"
type: "proposal"
status: "pending"
title: "模型提议：该文区分精神病症与超智识：二者皆被主流视为越界，但后者被描述为解放而非痛不欲生"
created_at: "2026-07-15T18:37:56+08:00"
updated_at: "2026-07-15T18:37:56+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_3413634e4482813fa28da48e"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_psychosis_hypersanity_contrast_20260715"
target_path: "vault/knowledge/claims/claim_wechat_psychosis_hypersanity_contrast_20260715-该文区分精神病症与超智识-二者皆被主流视为越界-但后者被描述为解放而非痛不欲生.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_2bb6bb64b38a86a24375d750.md"
candidate_sha256: "96cd77cf60ab6c38db7685edce35cfc5b67207f91af0eb4aaad5b59a004a4b9a"
change_reason: "导入 claim_wechat_psychosis_hypersanity_contrast_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_3413634e4482813fa28da48e", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "uncertainty": "哲学/精神病学文化评论；非临床建议；多处为 Laing/Jung 著作二次转述。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文区分精神病症与超智识：二者皆被主流视为越界，但后者被描述为解放而非痛不欲生

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_3413634e4482813fa28da48e`
- Input SHA-256：`f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7`
- 不确定性：哲学/精神病学文化评论；非临床建议；多处为 Laing/Jung 著作二次转述。
- 提议理由：导入 claim_wechat_psychosis_hypersanity_contrast_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_psychosis_hypersanity_contrast_20260715-该文区分精神病症与超智识-二者皆被主流视为越界-但后者被描述为解放而非痛不欲生.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_psychosis_hypersanity_contrast_20260715"
+title: "该文区分精神病症与超智识：二者皆被主流视为越界，但后者被描述为解放而非痛不欲生"
+tags: ["psychosis", "hypersanity", "philosophy"]
+domains: ["psychology", "philosophy"]
+confidence: "medium"
+applicability: ["Burton 对 psychosis 与 hypersanity 的概念对比", "文化哲学评论语境"]
+uncertainty: "对比为作者规范性论述，非流行病学或诊断标准；不应用于替代临床区分。"
+evidence: [{"evidence_id": "ev_2334", "evidence_kind": "quote", "source_id": "source_3413634e4482813fa28da48e", "content_id": "content_f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "extraction_id": "extraction_95c0d98bd7ac31b847b3caa6", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "span_start": 2334, "span_end": 2385, "original_text": "精神病症（psychosis）和超智识都将我们置身于社会之外，让我们在主流群体眼中看起来像是“疯子”。", "section": "共同社会位置", "stance": "supports", "verification_status": "verified", "reason": "文内对两种状态的共同描述。"}, {"evidence_id": "ev_2408", "evidence_kind": "quote", "source_id": "source_3413634e4482813fa28da48e", "content_id": "content_f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "extraction_id": "extraction_95c0d98bd7ac31b847b3caa6", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "span_start": 2408, "span_end": 2441, "original_text": "但鉴于精神障碍令人痛不欲生且行动不能，超智识往往意味着解放和赋能。", "section": "体验差异", "stance": "supports", "verification_status": "verified", "reason": "文内对两者体验后果的对比。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T18:35:00+08:00"
+updated_at: "2026-07-15T18:35:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入微信哲学评论译文；等待人工核验"
+source_ids: ["source_3413634e4482813fa28da48e"]
+relations: [{"type": "derived_from", "target_id": "source_3413634e4482813fa28da48e", "reason": "由利维坦转载的 Aeon/Neel Burton 哲学评论译文归纳；非临床指南或原始研究"}]
+---
+
+# psychosis vs 超智识
+
+前者被描述为痛苦失能，后者为解放赋能。
```
