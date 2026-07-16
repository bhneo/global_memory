---
id: "proposal_cc325814828aad58bb047f96"
type: "proposal"
status: "superseded"
title: "模型提议：该文引 Laing 称「正常人」在过去约 50 年杀害约一亿同胞"
created_at: "2026-07-15T18:37:56+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_3413634e4482813fa28da48e"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_laing_normal_violence_20260715"
target_path: "vault/knowledge/claims/claim_wechat_laing_normal_violence_20260715-该文引-laing-称-正常人-在过去约-50-年杀害约一亿同胞.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_cc325814828aad58bb047f96.md"
candidate_sha256: "72d366a42242006fc05b0eea698c451803ce74289087c884810aeed154b87bf4"
change_reason: "导入 claim_wechat_laing_normal_violence_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_3413634e4482813fa28da48e", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "uncertainty": "哲学/精神病学文化评论；非临床建议；多处为 Laing/Jung 著作二次转述。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文引 Laing 称「正常人」在过去约 50 年杀害约一亿同胞

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_3413634e4482813fa28da48e`
- Input SHA-256：`f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7`
- 不确定性：哲学/精神病学文化评论；非临床建议；多处为 Laing/Jung 著作二次转述。
- 提议理由：导入 claim_wechat_laing_normal_violence_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_laing_normal_violence_20260715-该文引-laing-称-正常人-在过去约-50-年杀害约一亿同胞.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_laing_normal_violence_20260715"
+title: "该文引 Laing 称「正常人」在过去约 50 年杀害约一亿同胞"
+tags: ["laing", "social-critique", "violence"]
+domains: ["philosophy", "psychology"]
+confidence: "low"
+applicability: ["Laing《经验政治》(1967) 引文", "编者注限定为 1967 前半个世纪"]
+uncertainty: "数字为 Laing 1967 年书中的修辞性论断；编者注称 WWII 直接死亡约七千万，与「一亿」口径不同；属哲学社会批判非历史统计。"
+evidence: [{"evidence_id": "ev_2711", "evidence_kind": "quote", "source_id": "source_3413634e4482813fa28da48e", "content_id": "content_f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "extraction_id": "extraction_95c0d98bd7ac31b847b3caa6", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "span_start": 2711, "span_end": 2747, "original_text": "在过去的50年，“正常人”大概杀害了100,000,000个他们的同胞。", "section": "Laing 引文", "stance": "supports", "verification_status": "verified", "reason": "文内直接引述 Laing 数字。"}, {"evidence_id": "ev_2747", "evidence_kind": "quote", "source_id": "source_3413634e4482813fa28da48e", "content_id": "content_f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "extraction_id": "extraction_95c0d98bd7ac31b847b3caa6", "input_sha256": "f5fb1a70caddd9fb2df74a41980d639e096f0723369fd67429571aa6074ccfa7", "span_start": 2747, "span_end": 2813, "original_text": "（编者注：此处应考虑到莱恩此书的书写年份，即1967年之前的半个世纪。仅二战期间，直接死于战争及与战争相关原因的人约为7,000万）", "section": "编者注", "stance": "supports", "verification_status": "verified", "reason": "文内对引文时间范围与数量的限定说明。"}]
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
+# Laing 正常人暴力论
+
+1967 前半个世纪约一亿杀害的引述。
```
