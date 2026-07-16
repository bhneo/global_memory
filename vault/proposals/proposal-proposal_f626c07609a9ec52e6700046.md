---
id: "proposal_f626c07609a9ec52e6700046"
type: "proposal"
status: "pending"
title: "模型提议：该文称 Morris-Thorne 可穿越虫洞需要违反类光能量条件的奇异负能物质"
created_at: "2026-07-15T21:48:24+08:00"
updated_at: "2026-07-15T21:48:24+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_647ffb9287507f806c354670"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_traversable_wormhole_exotic_matter_20260715"
target_path: "vault/knowledge/claims/claim_wechat_traversable_wormhole_exotic_matter_20260715-该文称-morris-thorne-可穿越虫洞需要违反类光能量条件的奇异负能物质.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f626c07609a9ec52e6700046.md"
candidate_sha256: "871538a3930bd7cb15fd6aa3b6de898fa1d5608c36bb4c41b0ced941d04fc2a0"
change_reason: "导入 claim_wechat_traversable_wormhole_exotic_matter_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_647ffb9287507f806c354670", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "uncertainty": "理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 Morris-Thorne 可穿越虫洞需要违反类光能量条件的奇异负能物质

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_647ffb9287507f806c354670`
- Input SHA-256：`ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0`
- 不确定性：理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。
- 提议理由：导入 claim_wechat_traversable_wormhole_exotic_matter_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_traversable_wormhole_exotic_matter_20260715-该文称-morris-thorne-可穿越虫洞需要违反类光能量条件的奇异负能物质.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_traversable_wormhole_exotic_matter_20260715"
+title: "该文称 Morris-Thorne 可穿越虫洞需要违反类光能量条件的奇异负能物质"
+tags: ["wormhole", "energy-condition", "general-relativity"]
+domains: ["physics", "general-relativity"]
+confidence: "medium"
+applicability: ["Morris-Thorne 球对称虫洞构造讨论", "Ray-Chaudhuri 方程与测地线汇论证语境"]
+uncertainty: "为科普性转述经典 GR 结论；负能物质量子来源与可工程化尺度未在文中定量给出。"
+evidence: [{"evidence_id": "ev_692", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 692, "span_end": 830, "original_text": "Morris和Thorne考虑反其道⽽⾏之，先给出关于时空结构的限制，然后再通过爱因斯坦场⽅程进⾏物质分布的求解。\n\n最初的计算是在球对称坐标系下进⾏的，他们发现如果要想满⾜特定的⾍洞时空结构，那么所需要的物质分布⼀定是违反能量条件的，通俗地来讲，需要引⼊奇异的负能物质[1]", "section": "Morris-Thorne 方法", "stance": "supports", "verification_status": "verified", "reason": "文内对反求物质分布与负能需求的说明。"}, {"evidence_id": "ev_1146", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 1146, "span_end": 1180, "original_text": "类光能量条件，因此⾍洞的存在⼀定需要在它的喉部引⼊负能量的奇异物质。", "section": "能量条件", "stance": "supports", "verification_status": "verified", "reason": "文内对类光能量条件被破坏的结论。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T21:40:00+08:00"
+updated_at: "2026-07-15T21:40:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入虫洞科普；等待人工核验"
+source_ids: ["source_647ffb9287507f806c354670"]
+relations: [{"type": "derived_from", "target_id": "source_647ffb9287507f806c354670", "reason": "由返朴/中科院物理所转载的虫洞科普文章归纳；引用 Morris-Thorne 等经典论文但未 capture 原文"}]
+---
+
+# 可穿越虫洞与负能物质
+
+喉部需奇异负能物质；违反类光能量条件。
```
