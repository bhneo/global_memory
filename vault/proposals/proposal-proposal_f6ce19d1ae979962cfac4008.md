---
id: "proposal_f6ce19d1ae979962cfac4008"
type: "proposal"
status: "superseded"
title: "模型提议：该文称「扩大的黑洞」为静态图错觉，大脑将中央暗区解读为正在进入黑暗环境而非像素变化"
created_at: "2026-07-16T01:40:40+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_38756ea977001ddb8594f144"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_expanding_hole_perceived_darkness_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expanding_hole_perceived_darkness_20260716-该文称-扩大的黑洞-为静态图错觉-大脑将中央暗区解读为正在进入黑暗环境而非像素变化.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f6ce19d1ae979962cfac4008.md"
candidate_sha256: "6673228338e9aba0e58ad3c7d406cab4ac4c60f2ecc0ee948c664a72f4609a0f"
change_reason: "导入 claim_wechat_expanding_hole_perceived_darkness_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_38756ea977001ddb8594f144", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "uncertainty": "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称「扩大的黑洞」为静态图错觉，大脑将中央暗区解读为正在进入黑暗环境而非像素变化

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_38756ea977001ddb8594f144`
- Input SHA-256：`fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86`
- 不确定性：知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。
- 提议理由：导入 claim_wechat_expanding_hole_perceived_darkness_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expanding_hole_perceived_darkness_20260716-该文称-扩大的黑洞-为静态图错觉-大脑将中央暗区解读为正在进入黑暗环境而非像素变化.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expanding_hole_perceived_darkness_20260716"
+title: "该文称「扩大的黑洞」为静态图错觉，大脑将中央暗区解读为正在进入黑暗环境而非像素变化"
+tags: ["expanding-hole", "visual-illusion", "perception"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["Bruno Laeng 等 expanding hole 错觉讨论", "静态图动态感错觉"]
+uncertainty: "为科普转述；Laeng 原论文细节需回 Frontiers 2022 核验。"
+evidence: [{"evidence_id": "ev_104", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 104, "span_end": 124, "original_text": "静态图，上面的每一个像素都没有改变过颜色", "section": "静态错觉", "stance": "supports", "verification_status": "verified", "reason": "文内强调图像像素未变。"}, {"evidence_id": "ev_298", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 298, "span_end": 350, "original_text": "Bruno Laeng）教授和他的同事们发现，当人们盯着图中央的黑洞，大脑会以为人正在走向一片黑暗的环境", "section": "大脑解读", "stance": "supports", "verification_status": "verified", "reason": "文内对 Laeng 团队机制解释的核心表述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:41:00+08:00"
+updated_at: "2026-07-16T01:41:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 expanding hole 视错觉科普；等待人工核验"
+source_ids: ["source_38756ea977001ddb8594f144"]
+relations: [{"type": "derived_from", "target_id": "source_38756ea977001ddb8594f144", "reason": "由环球科学/中科院物理所转载的 expanding hole 研究科普；原论文 Frontiers 2022 未 capture"}]
+---
+
+# 静态 expanding hole
+
+错觉来自大脑对暗区运动/环境的预测。
```
