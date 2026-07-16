---
id: "proposal_95249f2b68d739991365c37a"
type: "proposal"
status: "superseded"
title: "模型提议：天南具身公园文称近月四篇世界模型相关工作收敛于「拿世界模型去做评估」"
created_at: "2026-07-15T18:11:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_wam_eval_convergence_20260715"
target_path: "vault/knowledge/claims/claim_wechat_wam_eval_convergence_20260715-天南具身公园文称近月四篇世界模型相关工作收敛于-拿世界模型去做评估.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_95249f2b68d739991365c37a.md"
candidate_sha256: "9b659e23066e2a63fab34e3bf15943fc40ef355da24cb2ba0b352c91bc9c948b"
change_reason: "导入 claim_wechat_wam_eval_convergence_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "uncertainty": "公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：天南具身公园文称近月四篇世界模型相关工作收敛于「拿世界模型去做评估」

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_2d4f3a7d3525782c8ff503ee`
- Input SHA-256：`2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e`
- 不确定性：公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。
- 提议理由：导入 claim_wechat_wam_eval_convergence_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_wam_eval_convergence_20260715-天南具身公园文称近月四篇世界模型相关工作收敛于-拿世界模型去做评估.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_wam_eval_convergence_20260715"
+title: "天南具身公园文称近月四篇世界模型相关工作收敛于「拿世界模型去做评估」"
+tags: ["world-model", "evaluation", "embodied-ai"]
+domains: ["robot-learning", "world-models"]
+confidence: "medium"
+applicability: ["2026-07 天南具身公园公众号评论", "作者归纳的智元 τ₀-WM、SC3-Eval、World Value Model、GigaWorld-1 四篇工作"]
+uncertainty: "收敛判断来自作者个人阅读归纳，非系统综述；四篇论文本身未在本仓库 capture，不能将作者归类等同于各论文自述。"
+evidence: [{"evidence_id": "ev_376", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 376, "span_end": 430, "original_text": "四拨人，四个方向，团队肯定没碰过，但他们这一个月放出来的东西，指向的居然是同一件事：\n\n拿世界模型去做评估。", "section": "行业转向", "stance": "supports", "verification_status": "verified", "reason": "作者对四篇工作共同方向的直接归纳。"}, {"evidence_id": "ev_305", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 305, "span_end": 374, "original_text": "一个月之内，我被四篇非常 Solid 的论文轮着轰炸了一遍，分别来自智元罗剑岚、英伟达和 PI、字节，还有极佳（GigaWorld-1）。", "section": "引用范围", "stance": "supports", "verification_status": "verified", "reason": "限定作者所指的四处来源。"}, {"evidence_id": "evp_36296", "evidence_kind": "paraphrase", "source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "section": "来源层级", "interpretation": "公众号评论文章，引用多篇外部论文", "stance": "context", "verification_status": "verified", "reason": "提醒主张层级低于原始论文。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T18:12:00+08:00"
+updated_at: "2026-07-15T18:12:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入微信文章知识；等待人工核验"
+source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
+relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由微信公众号评论文章归纳；非独立 peer-reviewed 论文正文"}]
+---
+
+# 世界模型评估方向收敛
+
+作者认为四篇近期工作共同指向用世界模型做 policy 评估，而非直接生成动作。
```
