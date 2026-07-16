---
id: "proposal_e5265dc12db70a8088f7252f"
type: "proposal"
status: "superseded"
title: "模型提议：该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念"
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
target_id: "claim_wechat_lie_group_continuous_symmetry_20260715"
target_path: "vault/knowledge/claims/claim_wechat_lie_group_continuous_symmetry_20260715-该文称李群用于描述可连续变化的对称性-并可定量处理洛伦兹变换与自旋概念.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e5265dc12db70a8088f7252f.md"
candidate_sha256: "417b5fd072da225a743e088d5db93e387c77c8fb25f2cf4aaba33c022076c20a"
change_reason: "导入 claim_wechat_lie_group_continuous_symmetry_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_941321d95232028c233c9433", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "uncertainty": "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_941321d95232028c233c9433`
- Input SHA-256：`8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11`
- 不确定性：数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。
- 提议理由：导入 claim_wechat_lie_group_continuous_symmetry_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_lie_group_continuous_symmetry_20260715-该文称李群用于描述可连续变化的对称性-并可定量处理洛伦兹变换与自旋概念.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_lie_group_continuous_symmetry_20260715"
+title: "该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念"
+tags: ["lie-group", "symmetry", "lorentz"]
+domains: ["mathematics", "physics"]
+confidence: "medium"
+applicability: ["现代物理对称性/群论入门语境", "洛伦兹对称性与表示论讨论"]
+uncertainty: "为科普性概念介绍，未给出严格定理证明；自旋导出路径被压缩叙述。"
+evidence: [{"evidence_id": "ev_75", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 75, "span_end": 118, "original_text": "物理上经常会遇到一些能连续变化的对称性，为了描述这种连续变化的对称，我们就要借助李群。", "section": "连续对称", "stance": "supports", "verification_status": "verified", "reason": "文内对引入李群动机的说明。"}, {"evidence_id": "ev_118", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 118, "span_end": 178, "original_text": "比如洛伦兹对称性就是这样一种对称性，借助李群（及它的表示论）的概念，我们可以定量地描述洛伦兹变换甚至由此导出自旋的概念。", "section": "洛伦兹与自旋", "stance": "supports", "verification_status": "verified", "reason": "文内对李群在相对论与自旋中作用的表述。"}]
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
+# 李群与连续对称
+
+描述连续对称；洛伦兹变换与自旋。
```
