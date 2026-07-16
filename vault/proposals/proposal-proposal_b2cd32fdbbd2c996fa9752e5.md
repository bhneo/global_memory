---
id: "proposal_b2cd32fdbbd2c996fa9752e5"
type: "proposal"
status: "pending"
title: "模型提议：该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合"
created_at: "2026-07-15T21:10:43+08:00"
updated_at: "2026-07-15T21:10:43+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_941321d95232028c233c9433"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_lie_group_definition_20260715"
target_path: "vault/knowledge/claims/claim_wechat_lie_group_definition_20260715-该文定义李群为同时满足群公理-微分流形结构与运算相容性的集合.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b2cd32fdbbd2c996fa9752e5.md"
candidate_sha256: "a7756cd94721d49ab340cfcc8921d0824b9f8539f2db9ec4fbdc73a11eab5ed9"
change_reason: "导入 claim_wechat_lie_group_definition_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_941321d95232028c233c9433", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "uncertainty": "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_941321d95232028c233c9433`
- Input SHA-256：`8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11`
- 不确定性：数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。
- 提议理由：导入 claim_wechat_lie_group_definition_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_lie_group_definition_20260715-该文定义李群为同时满足群公理-微分流形结构与运算相容性的集合.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_lie_group_definition_20260715"
+title: "该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合"
+tags: ["lie-group", "differential-geometry", "manifold"]
+domains: ["mathematics"]
+confidence: "medium"
+applicability: ["文内第二节李群定义", "圆的对称 vs 离散群对比语境"]
+uncertainty: "提取文本中公式符号有 HTML 丢失；相容性条件未完整呈现数学细节。"
+evidence: [{"evidence_id": "ev_1682", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 1682, "span_end": 1843, "original_text": "当我们说到圆的变换时，我们可以谈圆转了一个无穷小的角度。对于群这个代数结构来说并不能体现“无穷小”这个概念，因为无穷小涉及到极限，而极限的概念依赖于拓扑而非群。所以我们需要同时用到群结构和拓扑结构才可以准确的说明这种变换。在实际应用中，我们通常不仅需要拓扑结构，还需要建立在拓扑上的微分结构，这两者结合就引出了李群的概念。", "section": "连续 vs 离散", "stance": "supports", "verification_status": "verified", "reason": "文内说明圆对称需要拓扑/微分结构。"}, {"evidence_id": "ev_1843", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 1843, "span_end": 1980, "original_text": "定义一个李群为一个集合，满足1.是个群2.是个微分流形3.的群结构和微分结构相容。一般来说我们会将每一个群元对应到流形上一点，并且把单位元置于原点处。相容性条件告诉我们群运算1）可以写成流形上的一个二元映射并且映射是光滑的。2）, 存在  满足。李群同时具有群结构和微分结构", "section": "李群定义", "stance": "supports", "verification_status": "verified", "reason": "文内对李群三重条件的概述。"}]
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
+# 李群定义
+
+群 + 微分流形 + 相容运算。
```
