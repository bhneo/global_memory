---
id: "proposal_50eb3103b0613e9eedd2fa30"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 π 是无理数，不能表示为两整数之比，且为无限不循环小数"
created_at: "2026-07-15T19:24:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "high"
source_ids: ["source_a86d60369a021d93d1e863aa"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_pi_irrational_20260715"
target_path: "vault/knowledge/claims/claim_wechat_pi_irrational_20260715-该文称-π-是无理数-不能表示为两整数之比-且为无限不循环小数.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_50eb3103b0613e9eedd2fa30.md"
candidate_sha256: "4ab835fa1c7ee2a2aa59adb6c1823d651d44151b6dadd6d3c3f119e59034aa64"
change_reason: "导入 claim_wechat_pi_irrational_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a86d60369a021d93d1e863aa", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "uncertainty": "科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 π 是无理数，不能表示为两整数之比，且为无限不循环小数

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a86d60369a021d93d1e863aa`
- Input SHA-256：`9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295`
- 不确定性：科普文章；超算纪录与历史断言需独立核对；部分为经典数学结论。
- 提议理由：导入 claim_wechat_pi_irrational_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_pi_irrational_20260715-该文称-π-是无理数-不能表示为两整数之比-且为无限不循环小数.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_pi_irrational_20260715"
+title: "该文称 π 是无理数，不能表示为两整数之比，且为无限不循环小数"
+tags: ["pi", "irrational-number", "mathematics"]
+domains: ["mathematics"]
+confidence: "high"
+applicability: ["科普文章对 π 基本性质的陈述", "小学/大学数学常识语境"]
+uncertainty: "无理数性质为数学定论；文章同时称 π 是超越数，该句亦在文中出现但未单独成 claim。"
+evidence: [{"evidence_id": "ev_937", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 937, "span_end": 1015, "original_text": "题干中，之所以要强调“近似等式”，是因为π是无理数，并不能表示成两个整数之比的形式，虽然我们常用形如22/7的分数去近似表示π，但实际上π是无限不循环小数。", "section": "无理数定义", "stance": "supports", "verification_status": "verified", "reason": "文内对 π 不能写成整数比与无限不循环的描述。"}, {"evidence_id": "ev_4011", "evidence_kind": "quote", "source_id": "source_a86d60369a021d93d1e863aa", "content_id": "content_9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "extraction_id": "extraction_59d5676353f0e4b5a43e38ec", "input_sha256": "9143ea8d31cc8d7534db5de546450b2be5f4dd4d90eb7b8c94b337e8cf7c3295", "span_start": 4011, "span_end": 4049, "original_text": "它是无理数，无限不循环；\n\n它还是超越数，不是任何一个有理数系数多项式的根。", "section": "超越数", "stance": "supports", "verification_status": "verified", "reason": "文内对 π 为超越数的补充说明。"}]
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
+# π 的无理性
+
+不能表为整数比；无限不循环；超越数。
```
