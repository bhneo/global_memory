---
id: "proposal_b3058b215f825eb358e1bde7"
type: "proposal"
status: "pending"
title: "模型提议：该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关"
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
target_id: "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716-该文称瞳孔调节可能依据大脑对光的感知而非实际照度-主观扩张感与瞳孔幅度正相关.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b3058b215f825eb358e1bde7.md"
candidate_sha256: "c4ae13753f6c6c33e52785c1771479b28144d5e9674c6496a794c8b0be9f4d42"
change_reason: "导入 claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_38756ea977001ddb8594f144", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "uncertainty": "知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_38756ea977001ddb8594f144`
- Input SHA-256：`fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86`
- 不确定性：知觉科普；n=50 与瞳孔 mm 数据需回 Frontiers 2022 原文核验。
- 提议理由：导入 claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716-该文称瞳孔调节可能依据大脑对光的感知而非实际照度-主观扩张感与瞳孔幅度正相关.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"
+title: "该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关"
+tags: ["pupil", "perceived-luminance", "illusion"]
+domains: ["neuroscience", "psychology"]
+confidence: "medium"
+applicability: ["感知驱动瞳孔 vs 物理光照不变语境", "洋红背景扩张更明显"]
+uncertainty: "「推测」性表述；因果机制在科普中被简化。"
+evidence: [{"evidence_id": "ev_980", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 980, "span_end": 1013, "original_text": "并不是根据实际的光照多少，来调节瞳孔的大小，而是根据大脑对光的感知", "section": "感知驱动", "stance": "supports", "verification_status": "verified", "reason": "文内对瞳孔调节依据的推测。"}, {"evidence_id": "ev_569", "evidence_kind": "quote", "source_id": "source_38756ea977001ddb8594f144", "content_id": "content_fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "extraction_id": "extraction_185ffd5cd427923efa0d9edb", "input_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "span_start": 569, "span_end": 969, "original_text": "主观感受到的“黑洞”扩张有多剧烈，也利用眼动仪来检测瞳孔直径在人们凝视图像的过程中有没有变大或变小。\n\n图片来源：原论文\n\n只不过在这项实验当中，被试者观看的“黑洞”图不光是白色背景的这一张，还有许多其他颜色背景的“黑洞”图。\n\n主观问卷的结果显示，50人当中有43人报告说自己看到了“黑洞”变大的景象；而另外7个人，有的感觉“黑洞”没怎么扩张，也有的完全没看出扩张。\n\n瞳孔数据则表明，人们凝视“黑洞”的时候，瞳孔直径会随着时间推移而增大：观看“黑洞”0.5秒时，被试者的瞳孔直径平均约为4.1毫米，而在注视“黑洞”8秒之后，他们的瞳孔直径平均约有4.9毫米。\n\n另外，图中背景颜色不同，观察者的瞳孔放大程度也不同，当“黑洞”放在洋红色/紫红色背景之上，瞳孔扩大最明显。\n\n总体看来，人们在主观感受到黑洞扩张的同时，他们的瞳孔也在扩大。并且，主观感受“黑洞蔓延”越剧烈的被试者，瞳孔扩张的幅度也越大", "section": "主观-瞳孔相关", "stance": "supports", "verification_status": "verified", "reason": "文内对主观扩张与瞳孔扩张相关的说明。"}]
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
+# 感知 vs 照度
+
+瞳孔可能随感知暗化而扩大，非仅物理光强。
```
