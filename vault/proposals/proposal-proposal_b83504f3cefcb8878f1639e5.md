---
id: "proposal_b83504f3cefcb8878f1639e5"
type: "proposal"
status: "pending"
title: "模型提议：该文称反色「白洞」图使被试瞳孔由扩大转为缩小，大脑或解读为走向明亮环境"
created_at: "2026-07-16T01:40:40+08:00"
updated_at: "2026-07-16T01:40:40+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_38756ea977001ddb8594f144"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_expanding_hole_white_hole_constriction_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expanding_hole_white_hole_constriction_20260716-该文称反色-白洞-图使被试瞳孔由扩大转为缩小-大脑或解读为走向明亮环境.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b83504f3cefcb8878f1639e5.md"
candidate_sha256: "4abb3ebead30eb4b98cacb53a5e21a9d8bccb9637632436b312d409dc5aaeb72"
change_reason: "导入 claim_wechat_expanding_hole_white_hole_constriction_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_38756ea977001ddb8594f144", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "uncertainty": "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称反色「白洞」图使被试瞳孔由扩大转为缩小，大脑或解读为走向明亮环境

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_38756ea977001ddb8594f144`
- Input SHA-256：`fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86`
- 不确定性：知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。
- 提议理由：导入 claim_wechat_expanding_hole_white_hole_constriction_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expanding_hole_white_hole_constriction_20260716-该文称反色-白洞-图使被试瞳孔由扩大转为缩小-大脑或解读为走向明亮环境.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expanding_hole_white_hole_constriction_20260716"
+title: "该文称反色「白洞」图使被试瞳孔由扩大转为缩小，大脑或解读为走向明亮环境"
+tags: ["expanding-hole", "pupil", "aftereffect"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["黑底白洞反色条件讨论", "明暗方向性瞳孔响应"]
+uncertainty: "反色实验细节在科普中被压缩；效应量未给出。"
+evidence: [{"evidence_id": "ev_1154", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 1154, "span_end": 1169, "original_text": "反色处理，变成黑色背景的“白洞", "section": "反色刺激", "stance": "supports", "verification_status": "verified", "reason": "文内对反色图条件的说明。"}, {"evidence_id": "ev_1188", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 1188, "span_end": 1200, "original_text": "不再是逐渐放大，而是缩小", "section": "瞳孔缩小", "stance": "supports", "verification_status": "verified", "reason": "文内对白洞条件下瞳孔缩小的叙述。"}]
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
+# 白洞反色
+
+白洞条件瞳孔缩小；与黑洞条件对照。
```
