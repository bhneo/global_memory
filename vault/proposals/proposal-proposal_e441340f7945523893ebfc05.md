---
id: "proposal_e441340f7945523893ebfc05"
type: "proposal"
status: "superseded"
title: "模型提议：该文称标准模型是规范理论，其规范群为李群"
created_at: "2026-07-15T21:10:42+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_941321d95232028c233c9433"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_sm_gauge_lie_group_20260715"
target_path: "vault/knowledge/claims/claim_wechat_sm_gauge_lie_group_20260715-该文称标准模型是规范理论-其规范群为李群.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e441340f7945523893ebfc05.md"
candidate_sha256: "7315aea5afb36488bc83fc44dbfa2519c6729ce5f59faf5588fce82066085fdd"
change_reason: "导入 claim_wechat_sm_gauge_lie_group_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_941321d95232028c233c9433", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "uncertainty": "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称标准模型是规范理论，其规范群为李群

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_941321d95232028c233c9433`
- Input SHA-256：`8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11`
- 不确定性：数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。
- 提议理由：导入 claim_wechat_sm_gauge_lie_group_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_sm_gauge_lie_group_20260715-该文称标准模型是规范理论-其规范群为李群.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_sm_gauge_lie_group_20260715"
+title: "该文称标准模型是规范理论，其规范群为李群"
+tags: ["standard-model", "gauge-theory", "lie-group"]
+domains: ["physics", "particle-physics"]
+confidence: "medium"
+applicability: ["标准模型结构的高层科普描述", "规范对称性语境"]
+uncertainty: "未指明具体规范群因子（如 SU(3)×SU(2)×U(1)）；为概述性断言。"
+evidence: [{"evidence_id": "ev_352", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 352, "span_end": 404, "original_text": "目前人类最准确的物理理论——标准模型，它本质是一个规范理论，而这个规范理论的核心要素规范群就是一个李群。", "section": "标准模型规范群", "stance": "supports", "verification_status": "verified", "reason": "文内对标准模型与李群关系的陈述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T21:00:00+08:00"
+updated_at: "2026-07-15T21:00:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入李群李代数科普；等待人工核验"
+source_ids: ["source_941321d95232028c233c9433"]
+relations: [{"type": "derived_from", "target_id": "source_941321d95232028c233c9433", "reason": "由中科院物理所转载的李群李代数科普文章归纳；非教材定理证明"}]
+---
+
+# 标准模型规范群
+
+规范理论；规范群为李群。
```
