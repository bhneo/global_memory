---
id: "proposal_5bc4a3d28508f15a49b0c648"
type: "proposal"
status: "pending"
title: "模型提议：该文报告 50 名被试凝视「黑洞」图时瞳孔随时间扩大（约 4.1mm→4.9mm），86% 主观感到扩张"
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
target_id: "claim_wechat_expanding_hole_pupil_dilation_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expanding_hole_pupil_dilation_20260716-该文报告-50-名被试凝视-黑洞-图时瞳孔随时间扩大-约-4-1mm-4-9mm-86-主观感到扩张.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5bc4a3d28508f15a49b0c648.md"
candidate_sha256: "ba8cf0d85c20197e2aaa8bb1e76e09817effde5f8a597810775e7a38af5e4e54"
change_reason: "导入 claim_wechat_expanding_hole_pupil_dilation_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_38756ea977001ddb8594f144", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "uncertainty": "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文报告 50 名被试凝视「黑洞」图时瞳孔随时间扩大（约 4.1mm→4.9mm），86% 主观感到扩张

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_38756ea977001ddb8594f144`
- Input SHA-256：`fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86`
- 不确定性：知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。
- 提议理由：导入 claim_wechat_expanding_hole_pupil_dilation_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expanding_hole_pupil_dilation_20260716-该文报告-50-名被试凝视-黑洞-图时瞳孔随时间扩大-约-4-1mm-4-9mm-86-主观感到扩张.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expanding_hole_pupil_dilation_20260716"
+title: "该文报告 50 名被试凝视「黑洞」图时瞳孔随时间扩大（约 4.1mm→4.9mm），86% 主观感到扩张"
+tags: ["pupil-response", "psychophysics", "expanding-hole"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["n=50 眼动实验科普叙述", "0.5s vs 8s 瞳孔直径对比"]
+uncertainty: "数值来自科普转述；43/50 比例与 mm 数据需回原文核验。"
+evidence: [{"evidence_id": "ev_546", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 546, "span_end": 703, "original_text": "50位视力正常的成年男女，不止调查这些人看图时主观感受到的“黑洞”扩张有多剧烈，也利用眼动仪来检测瞳孔直径在人们凝视图像的过程中有没有变大或变小。\n\n图片来源：原论文\n\n只不过在这项实验当中，被试者观看的“黑洞”图不光是白色背景的这一张，还有许多其他颜色背景的“黑洞”图。\n\n主观问卷的结果显示，50人当中有43人", "section": "样本与主观报告", "stance": "supports", "verification_status": "verified", "reason": "文内对被试数量与主观扩张报告比例。"}, {"evidence_id": "ev_814", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 814, "span_end": 849, "original_text": "4.1毫米，而在注视“黑洞”8秒之后，他们的瞳孔直径平均约有4.9毫米", "section": "瞳孔直径", "stance": "supports", "verification_status": "verified", "reason": "文内对 0.5s 与 8s 瞳孔直径的叙述。"}]
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
+# 瞳孔扩大
+
+凝视黑洞图瞳孔随时间增大；多数被试主观感到扩张。
```
