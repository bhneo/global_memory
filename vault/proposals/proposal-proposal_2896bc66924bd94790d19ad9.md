---
id: "proposal_2896bc66924bd94790d19ad9"
type: "proposal"
status: "superseded"
title: "模型提议：该文称数据顺序可显著影响 epiplexity 与时间有界熵，挑战「顺序无关」经典假设"
created_at: "2026-07-15T23:49:56+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_epiplexity_order_matters_20260715"
target_path: "vault/knowledge/claims/claim_wechat_epiplexity_order_matters_20260715-该文称数据顺序可显著影响-epiplexity-与时间有界熵-挑战-顺序无关-经典假设.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_2896bc66924bd94790d19ad9.md"
candidate_sha256: "586f3d65c3f9a62999be08cd1fd15258e3fc942972cb7e31040065c19b1a92e4"
change_reason: "导入 claim_wechat_epiplexity_order_matters_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_494ab02c17c5f495f1ed29d0", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "uncertainty": "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称数据顺序可显著影响 epiplexity 与时间有界熵，挑战「顺序无关」经典假设

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_494ab02c17c5f495f1ed29d0`
- Input SHA-256：`40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d`
- 不确定性：信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。
- 提议理由：导入 claim_wechat_epiplexity_order_matters_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_epiplexity_order_matters_20260715-该文称数据顺序可显著影响-epiplexity-与时间有界熵-挑战-顺序无关-经典假设.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_epiplexity_order_matters_20260715"
+title: "该文称数据顺序可显著影响 epiplexity 与时间有界熵，挑战「顺序无关」经典假设"
+tags: ["epiplexity", "data-order", "time-bounded-entropy"]
+domains: ["information-theory", "machine-learning"]
+confidence: "medium"
+applicability: ["定理 3 与单向置换 f 的正反向建模讨论", "课程学习/数据排序语境"]
+uncertainty: "超对数级差距为科普性表述；具体构造需回原文。"
+evidence: [{"evidence_id": "ev_2389", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 2389, "span_end": 2530, "original_text": "定理 3  数据顺序直接决定了认知复杂度和时间有界熵的量级\n\n对于单向置换 f，正向建模（X→f (X)）与反向建模（f (X)→X）的时间有界熵与 epiplexity 存在超对数级的差距。定理从数学上证明了「数据顺序决定信息价值」，顺序不是无关紧要的细节，而是解锁信息价值的钥匙", "section": "定理 3", "stance": "supports", "verification_status": "verified", "reason": "文内对顺序决定信息价值的结论。"}, {"evidence_id": "ev_2422", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 2422, "span_end": 2481, "original_text": "单向置换 f，正向建模（X→f (X)）与反向建模（f (X)→X）的时间有界熵与 epiplexity 存在超对数级", "section": "正反向建模", "stance": "supports", "verification_status": "verified", "reason": "文内对 X→f(X) 与 f(X)→X 差距的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T23:50:00+08:00"
+updated_at: "2026-07-15T23:50:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 epiplexity 科普；等待人工核验"
+source_ids: ["source_494ab02c17c5f495f1ed29d0"]
+relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "由伊芝冰对 arXiv:2601.03220 epiplexity 论文的科普解读归纳；原论文未 capture"}]
+---
+
+# 数据顺序
+
+顺序影响 epiplexity；非无关紧要细节。
```
