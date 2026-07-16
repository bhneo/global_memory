---
id: "proposal_1cc33f823a46a1cdc5265034"
type: "proposal"
status: "superseded"
title: "模型提议：该文称李代数刻画李群局部结构，指数映射仅对紧致连通李群为满射"
created_at: "2026-07-15T21:10:43+08:00"
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
target_id: "claim_wechat_lie_algebra_exponential_map_20260715"
target_path: "vault/knowledge/claims/claim_wechat_lie_algebra_exponential_map_20260715-该文称李代数刻画李群局部结构-指数映射仅对紧致连通李群为满射.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1cc33f823a46a1cdc5265034.md"
candidate_sha256: "adf30eea2cab951377f88b7850bc5fb8e08aa1a974b09d0d95602b000c145d0b"
change_reason: "导入 claim_wechat_lie_algebra_exponential_map_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_941321d95232028c233c9433", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "uncertainty": "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称李代数刻画李群局部结构，指数映射仅对紧致连通李群为满射

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_941321d95232028c233c9433`
- Input SHA-256：`8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11`
- 不确定性：数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。
- 提议理由：导入 claim_wechat_lie_algebra_exponential_map_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_lie_algebra_exponential_map_20260715-该文称李代数刻画李群局部结构-指数映射仅对紧致连通李群为满射.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_lie_algebra_exponential_map_20260715"
+title: "该文称李代数刻画李群局部结构，指数映射仅对紧致连通李群为满射"
+tags: ["lie-algebra", "exponential-map", "lie-group"]
+domains: ["mathematics", "physics"]
+confidence: "medium"
+applicability: ["文内第三节李代数构造与指数映射", "局部-整体关系讨论"]
+uncertainty: "不同李群可共享同一李代数为文内断言，未给出反例；证明被省略。"
+evidence: [{"evidence_id": "ev_2879", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 2879, "span_end": 2956, "original_text": "李代数可以在局部转变为李群元素，因为李代数可以看成是李群单位元上的一个切向量，所以这个切向量可以生成一个局部的流满足解出这个流，我们发现结果是一个指数映射", "section": "指数映射", "stance": "supports", "verification_status": "verified", "reason": "文内对李代数局部生成群元的描述。"}, {"evidence_id": "ev_3032", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 3032, "span_end": 3049, "original_text": "只有紧致连通李群指数映射才是满射。", "section": "满射条件", "stance": "supports", "verification_status": "verified", "reason": "文内对指数映射覆盖范围的限制。"}, {"evidence_id": "ev_3138", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 3138, "span_end": 3201, "original_text": "李代数只能反映李群的局部性质，对于整体性质则无能为力，事实上不同的李群可以有相同的李代数，因此对李群的研究也不能仅借助李代数。", "section": "局部局限", "stance": "supports", "verification_status": "verified", "reason": "文内对李代数无法捕获整体性质的说明。"}]
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
+# 李代数与指数映射
+
+局部线性化；紧致连通时 exp 满射。
```
