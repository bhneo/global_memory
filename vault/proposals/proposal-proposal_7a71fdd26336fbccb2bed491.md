---
id: "proposal_7a71fdd26336fbccb2bed491"
type: "proposal"
status: "superseded"
title: "模型提议：该文称莱布尼茨级数项次足够多时可逼近 π，但收敛很慢，约 500,000 项才到第五位小数"
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
target_id: "claim_wechat_pi_leibniz_convergence_20260715"
target_path: "vault/knowledge/claims/claim_wechat_pi_leibniz_convergence_20260715-该文称莱布尼茨级数项次足够多时可逼近-π-但收敛很慢-约-500-000-项才到第五位小数.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_7a71fdd26336fbccb2bed491.md"
candidate_sha256: "995b2ddb91a6dade9f097cda6a3958269f45178bd676c0d868e7bb46d26fb977"
change_reason: "导入 claim_wechat_pi_leibniz_convergence_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a86d60369a021d93d1e863aa", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "uncertainty": "科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称莱布尼茨级数项次足够多时可逼近 π，但收敛很慢，约 500,000 项才到第五位小数

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a86d60369a021d93d1e863aa`
- Input SHA-256：`9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295`
- 不确定性：科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。
- 提议理由：导入 claim_wechat_pi_leibniz_convergence_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_pi_leibniz_convergence_20260715-该文称莱布尼茨级数项次足够多时可逼近-π-但收敛很慢-约-500-000-项才到第五位小数.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_pi_leibniz_convergence_20260715"
+title: "该文称莱布尼茨级数项次足够多时可逼近 π，但收敛很慢，约 500,000 项才到第五位小数"
+tags: ["pi", "leibniz-formula", "series"]
+domains: ["mathematics"]
+confidence: "medium"
+applicability: ["文内对 π 的莱布尼茨公式收敛性的科普描述", "大学微积分语境"]
+uncertainty: "500,000 项到第五小数为文内单点说法，未给出误差界推导；级数收敛性本身为经典结果。"
+evidence: [{"evidence_id": "ev_757", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 757, "span_end": 790, "original_text": "毕竟，这是π的莱布尼茨公式，只要项次足够多，总和一定会慢慢接近π。", "section": "莱布尼茨公式", "stance": "supports", "verification_status": "verified", "reason": "文内对级数收敛性的描述。"}, {"evidence_id": "ev_792", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 792, "span_end": 834, "original_text": "虽然，这个数列的收敛速度很慢，要到500,000项之后，才能精确到π的第五小数...", "section": "收敛速度", "stance": "supports", "verification_status": "verified", "reason": "文内对所需项次的数量级说明。"}]
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
+# 莱布尼茨级数
+
+收敛极慢；约 50 万项到第五位小数。
```
