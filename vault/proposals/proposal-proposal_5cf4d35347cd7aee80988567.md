---
id: "proposal_5cf4d35347cd7aee80988567"
type: "proposal"
status: "superseded"
title: "模型提议：该文认为世界模型做评估因「错得起」可能比直接生成动作更易先落地"
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
target_id: "claim_wechat_eval_vs_action_tradeoff_20260715"
target_path: "vault/knowledge/claims/claim_wechat_eval_vs_action_tradeoff_20260715-该文认为世界模型做评估因-错得起-可能比直接生成动作更易先落地.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5cf4d35347cd7aee80988567.md"
candidate_sha256: "f6c885b8738d32d58bf76fbad99652dd833455a8a7b34273d4e3283701241e66"
change_reason: "导入 claim_wechat_eval_vs_action_tradeoff_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "uncertainty": "公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文认为世界模型做评估因「错得起」可能比直接生成动作更易先落地

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_2d4f3a7d3525782c8ff503ee`
- Input SHA-256：`2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e`
- 不确定性：公众号评论文章；多处为对第三方论文/访谈的二次转述，需回原文核验。
- 提议理由：导入 claim_wechat_eval_vs_action_tradeoff_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_eval_vs_action_tradeoff_20260715-该文认为世界模型做评估因-错得起-可能比直接生成动作更易先落地.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_eval_vs_action_tradeoff_20260715"
+title: "该文认为世界模型做评估因「错得起」可能比直接生成动作更易先落地"
+tags: ["world-model", "evaluation", "world-action-model"]
+domains: ["world-models", "robot-learning"]
+confidence: "medium"
+applicability: ["作者对世界模型两条应用路线的对比", "真机代价较高的动作生成场景"]
+uncertainty: "属于作者观点性对比，「先落地」未给出可复现判据或统一 benchmark。"
+evidence: [{"evidence_id": "ev_809", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 809, "span_end": 865, "original_text": "同样是世界模型，直接生成动作那条线要「少犯贵的错」，难在错不起； 而做评估这条线，恰恰因为错得起，反而先落地了。", "section": "路线对比", "stance": "supports", "verification_status": "verified", "reason": "作者对两条路线成本结构的对比。"}, {"evidence_id": "ev_506", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 506, "span_end": 526, "original_text": "世界模型落不了地？没关系，换个思路就行。", "section": "策略转向", "stance": "supports", "verification_status": "verified", "reason": "作者对应用路线切换的表述。"}]
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
+# 评估 vs 动作生成
+
+评估路线因错误成本较低，作者认为更易率先落地。
```
