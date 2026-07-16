---
id: "proposal_d0e21be509a847f917fe8501"
type: "proposal"
status: "superseded"
title: "模型提议：该文称多万亿位 π 计算常用于检验超算性能，且 39 位精度即可把可观测宇宙圆周算到原子尺度"
created_at: "2026-07-15T19:24:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_a86d60369a021d93d1e863aa"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_pi_supercomputer_benchmark_20260715"
target_path: "vault/knowledge/claims/claim_wechat_pi_supercomputer_benchmark_20260715-该文称多万亿位-π-计算常用于检验超算性能-且-39-位精度即可把可观测宇宙圆周算到原子尺度.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_d0e21be509a847f917fe8501.md"
candidate_sha256: "9dd5dbddf61026f8185cb7d5cdc72504234bb1cc8b568a8e9eca2e4220833d1b"
change_reason: "导入 claim_wechat_pi_supercomputer_benchmark_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a86d60369a021d93d1e863aa", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "uncertainty": "科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称多万亿位 π 计算常用于检验超算性能，且 39 位精度即可把可观测宇宙圆周算到原子尺度

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a86d60369a021d93d1e863aa`
- Input SHA-256：`9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295`
- 不确定性：科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。
- 提议理由：导入 claim_wechat_pi_supercomputer_benchmark_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_pi_supercomputer_benchmark_20260715-该文称多万亿位-π-计算常用于检验超算性能-且-39-位精度即可把可观测宇宙圆周算到原子尺度.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_pi_supercomputer_benchmark_20260715"
+title: "该文称多万亿位 π 计算常用于检验超算性能，且 39 位精度即可把可观测宇宙圆周算到原子尺度"
+tags: ["pi", "supercomputer", "benchmark"]
+domains: ["mathematics", "computing"]
+confidence: "medium"
+applicability: ["文内对超算 π 计算用途的说明", "宇宙学精度需求讨论"]
+uncertainty: "39 位与「原子大小」为科普数量级说法，未给出推导来源；2021/2022 纪录为媒体报道需可核对。"
+evidence: [{"evidence_id": "ev_2842", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 2842, "span_end": 2920, "original_text": "事实上，如果从实际测量的角度而言，圆周率π值精确到39位时，就可以将可观测宇宙的圆周计算，精确到一个原子大小，这已经能够满足目前绝大多数宇宙学的计算需求了。", "section": "39 位精度", "stance": "supports", "verification_status": "verified", "reason": "文内对 π 有效精度需求的表述。"}, {"evidence_id": "ev_3016", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 3016, "span_end": 3055, "original_text": "用超级计算机去计算多位π值，是目前用于检验计算机性能和改善计算方法的常用方法。", "section": "超算检验", "stance": "supports", "verification_status": "verified", "reason": "文内对 π 作为超算 benchmark 的说明。"}, {"evidence_id": "ev_2643", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 2643, "span_end": 2707, "original_text": "2021 年8月，瑞士的科学家刷新世界纪录，使用超级计算机，将圆周率计算到了小数点后的 62.8 万亿位，耗时108天零9小时。", "section": "2021 纪录", "stance": "supports", "verification_status": "verified", "reason": "文内对 2021 计算纪录的转述。"}, {"evidence_id": "ev_2734", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 2734, "span_end": 2811, "original_text": "2022 年 3 月， Google Cloud将小数点后的 100 万亿位数都给计算了出来，共计用了不到 158 天的时间，而第100万亿位，恰好是0。", "section": "2022 纪录", "stance": "supports", "verification_status": "verified", "reason": "文内对 2022 Google Cloud 100 万亿位的转述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T19:25:00+08:00"
+updated_at: "2026-07-15T19:25:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入圆周率科普文章；等待人工核验"
+source_ids: ["source_a86d60369a021d93d1e863aa"]
+relations: [{"type": "derived_from", "target_id": "source_a86d60369a021d93d1e863aa", "reason": "由中科院物理所公众号科普文章归纳；非原始研究论文"}]
+---
+
+# 超算与 π
+
+benchmark 用途；39 位宇宙尺度；2021/2022 纪录。
```
