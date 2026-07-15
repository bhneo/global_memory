---
id: "proposal_693109a0dbdbce6e04f9ffaa"
type: "proposal"
status: "pending"
title: "模型提议：该文称英伟达与 PI 的 SC3-Eval 与真机相关性达 0.929 且能复现真机失败"
created_at: "2026-07-15T18:11:29+08:00"
updated_at: "2026-07-15T18:11:29+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_sc3_eval_correlation_20260715"
target_path: "vault/knowledge/claims/claim_wechat_sc3_eval_correlation_20260715-该文称英伟达与-pi-的-sc3-eval-与真机相关性达-0-929-且能复现真机失败.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_693109a0dbdbce6e04f9ffaa.md"
candidate_sha256: "569f14b9009943b10c347b1c2afff87d4b2cc19b8c5d9784c49bf21ac602e568"
change_reason: "导入 claim_wechat_sc3_eval_correlation_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "uncertainty": "公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称英伟达与 PI 的 SC3-Eval 与真机相关性达 0.929 且能复现真机失败

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_2d4f3a7d3525782c8ff503ee`
- Input SHA-256：`2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e`
- 不确定性：公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。
- 提议理由：导入 claim_wechat_sc3_eval_correlation_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_sc3_eval_correlation_20260715-该文称英伟达与-pi-的-sc3-eval-与真机相关性达-0-929-且能复现真机失败.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_sc3_eval_correlation_20260715"
+title: "该文称英伟达与 PI 的 SC3-Eval 与真机相关性达 0.929 且能复现真机失败"
+tags: ["world-model", "evaluation", "sc3-eval"]
+domains: ["world-models", "robotics"]
+confidence: "low"
+applicability: ["作者对 SC3-Eval 论文结果的转述", "视频模型用于 rollout 评估的设定"]
+uncertainty: "0.929 与失败复现能力均经公众号二次转述；SC3-Eval 原文未 capture；未说明相关性指标定义与样本量。"
+evidence: [{"evidence_id": "ev_1241", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 1241, "span_end": 1352, "original_text": "SC3-Eval解的是另一个事：视频模型拿来评估，最怕它一本正经地胡说八道，画面顺、物理假。他们逼模型「自己跟自己对账」，正着生成画面、反着从画面倒推动作，俩一旦对不上，就说明它在瞎编了，直接把这条 rollout 掐掉。", "section": "SC3-Eval 方法", "stance": "supports", "verification_status": "verified", "reason": "作者对 SC3-Eval 机制的描述。"}, {"evidence_id": "ev_1354", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 1354, "span_end": 1395, "original_text": "做到了跟真机 0.929 的相关性，更狠的是能把真机上真实出现过的失败给复现出来。", "section": "SC3-Eval 结果", "stance": "supports", "verification_status": "verified", "reason": "作者转述的相关性与失败复现表述。"}]
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
+# SC3-Eval 转述
+
+作者称 SC3-Eval 与真机相关性 0.929。
```
