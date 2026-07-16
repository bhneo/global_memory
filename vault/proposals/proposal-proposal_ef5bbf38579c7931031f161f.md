---
id: "proposal_ef5bbf38579c7931031f161f"
type: "proposal"
status: "pending"
title: "模型提议：该文称现代粒子物理中的「粒子」可理解为李群不可约表示空间的基"
created_at: "2026-07-15T21:10:42+08:00"
updated_at: "2026-07-15T21:10:42+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_941321d95232028c233c9433"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_particle_as_representation_basis_20260715"
target_path: "vault/knowledge/claims/claim_wechat_particle_as_representation_basis_20260715-该文称现代粒子物理中的-粒子-可理解为李群不可约表示空间的基.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_ef5bbf38579c7931031f161f.md"
candidate_sha256: "dc1c6fad3238499c04ba7186d6c7e29cbc94a2f4340aac9a1a1928b9d0e769b3"
change_reason: "导入 claim_wechat_particle_as_representation_basis_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_941321d95232028c233c9433", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "uncertainty": "数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称现代粒子物理中的「粒子」可理解为李群不可约表示空间的基

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_941321d95232028c233c9433`
- Input SHA-256：`8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11`
- 不确定性：数学/粒子物理科普；公式符号在 extraction 中有损；非严格证明。
- 提议理由：导入 claim_wechat_particle_as_representation_basis_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_particle_as_representation_basis_20260715-该文称现代粒子物理中的-粒子-可理解为李群不可约表示空间的基.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_particle_as_representation_basis_20260715"
+title: "该文称现代粒子物理中的「粒子」可理解为李群不可约表示空间的基"
+tags: ["particle-physics", "representation-theory", "lie-group"]
+domains: ["physics", "mathematics"]
+confidence: "medium"
+applicability: ["粒子物理概念层解释", "理论赋予实验数据意义的讨论"]
+uncertainty: "为概念性重定义/interpretation，不是实验操作定义；依赖表示论框架。"
+evidence: [{"evidence_id": "ev_201", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 201, "span_end": 264, "original_text": "理论告诉我们实验能看到什么，这当然不是说理论可以瞎编而不用对实验结果负责，应该来说这句话是指只有通过理论才能赋予实验数据意义。", "section": "理论角色", "stance": "supports", "verification_status": "verified", "reason": "文内对理论解释实验数据的说明。"}, {"evidence_id": "ev_290", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 290, "span_end": 310, "original_text": "李群的不可约表示空间的基”这样一个东西。", "section": "粒子定义", "stance": "supports", "verification_status": "verified", "reason": "文内对「粒子」概念的核心表述。"}]
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
+# 粒子即表示基
+
+粒子 = 不可约表示空间基。
```
