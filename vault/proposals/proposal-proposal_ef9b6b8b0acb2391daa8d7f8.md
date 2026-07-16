---
id: "proposal_ef9b6b8b0acb2391daa8d7f8"
type: "proposal"
status: "pending"
title: "模型提议：该文称祖冲之在公元 462 年给出 355/113 作为 π 近似值，并在近 800 年内为最高精度"
created_at: "2026-07-15T19:24:29+08:00"
updated_at: "2026-07-15T19:24:29+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_a86d60369a021d93d1e863aa"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_zu_chongzhi_355_113_20260715"
target_path: "vault/knowledge/claims/claim_wechat_zu_chongzhi_355_113_20260715-该文称祖冲之在公元-462-年给出-355-113-作为-π-近似值-并在近-800-年内为最高精度.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_ef9b6b8b0acb2391daa8d7f8.md"
candidate_sha256: "85066bae30bc9b0e0f7390fa45653f0368f15443a78b37a8c7d336a73b2c33b7"
change_reason: "导入 claim_wechat_zu_chongzhi_355_113_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a86d60369a021d93d1e863aa", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "uncertainty": "科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称祖冲之在公元 462 年给出 355/113 作为 π 近似值，并在近 800 年内为最高精度

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a86d60369a021d93d1e863aa`
- Input SHA-256：`9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295`
- 不确定性：科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。
- 提议理由：导入 claim_wechat_zu_chongzhi_355_113_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_zu_chongzhi_355_113_20260715-该文称祖冲之在公元-462-年给出-355-113-作为-π-近似值-并在近-800-年内为最高精度.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_zu_chongzhi_355_113_20260715"
+title: "该文称祖冲之在公元 462 年给出 355/113 作为 π 近似值，并在近 800 年内为最高精度"
+tags: ["pi", "history-of-mathematics", "zu-chongzhi"]
+domains: ["mathematics", "history"]
+confidence: "medium"
+applicability: ["文内对中国古代圆周率史的叙述", "355/113 历史近似值讨论"]
+uncertainty: "800 年「最高精度」为科普表述，需与史学文献交叉验证；误差示例（直径 10000 米差 3 毫米）为文内推算。"
+evidence: [{"evidence_id": "ev_1424", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 1424, "span_end": 1487, "original_text": "公元462年，祖冲之在《缀术》中记载了他计算得出的圆周率近似值355/113，其展开成小数的值是3.1415929203...", "section": "355/113 记载", "stance": "supports", "verification_status": "verified", "reason": "文内对祖冲之近似值与展开小数的描述。"}, {"evidence_id": "ev_1494", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 1494, "span_end": 1521, "original_text": "在之后近800年的时间内，这都是准确度最高的π估算值。", "section": "历史精度", "stance": "supports", "verification_status": "verified", "reason": "文内对 355/113 保持领先时间的断言。"}, {"evidence_id": "ev_1690", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 1690, "span_end": 1732, "original_text": "假设一个圆的直径是10000米，那用它计算出的圆周长与真值相比，仅仅多了不到3毫米！", "section": "误差示例", "stance": "supports", "verification_status": "verified", "reason": "文内用 355/113 计算的精度直观例子。"}]
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
+# 祖冲之 355/113
+
+历史高精度近似与误差示例。
```
