---
id: "proposal_b7ba9caccc44b875a3ca3535"
type: "proposal"
status: "pending"
title: "模型提议：该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越"
created_at: "2026-07-15T21:48:24+08:00"
updated_at: "2026-07-15T21:48:24+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_647ffb9287507f806c354670"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_double_trace_traversable_20260715"
target_path: "vault/knowledge/claims/claim_wechat_double_trace_traversable_20260715-该文称边界-double-trace-deformation-可引入负能量流-使原本不可穿越的-er-桥变为可穿越.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b7ba9caccc44b875a3ca3535.md"
candidate_sha256: "409eae486f793424992647dd0a4a17008caffd25ed3a0df89a83f7aac31e3f1b"
change_reason: "导入 claim_wechat_double_trace_traversable_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_647ffb9287507f806c354670", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "uncertainty": "理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_647ffb9287507f806c354670`
- Input SHA-256：`ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0`
- 不确定性：理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。
- 提议理由：导入 claim_wechat_double_trace_traversable_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_double_trace_traversable_20260715-该文称边界-double-trace-deformation-可引入负能量流-使原本不可穿越的-er-桥变为可穿越.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_double_trace_traversable_20260715"
+title: "该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越"
+tags: ["traversable-wormhole", "ads-cft", "quantum-teleportation"]
+domains: ["physics", "quantum-gravity"]
+confidence: "low"
+applicability: ["Gao-Jafferis-Wall 可穿越虫洞模型科普", "引力版量子隐形传态图像"]
+uncertainty: "为特定 holographic 模型结论；double trace 操作与实验可 realizability 未讨论；科普转述。"
+evidence: [{"evidence_id": "ev_2945", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 2945, "span_end": 2982, "original_text": "double trace deformation的操作，引⼊如下的算符扰动", "section": "double trace 构造", "stance": "supports", "verification_status": "verified", "reason": "文内对实现可穿越性的模型操作。"}, {"evidence_id": "ev_3121", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 3121, "span_end": 3266, "original_text": "根据ER=EPR的思想，这个过程相当于引⼒版本的量⼦隐形传态，⽽double trace deformation则类似经典信道。在量⼦隐形传态中，似乎量⼦⽐特是通过量⼦纠缠在另⼀个地⽅被重新构造出来的；⽽在引⼒的图像下，它有了⼀个全新的理解，那就是它是通过连接两个地⽅的⾍洞穿越⽽来的[7]", "section": "引力量子隐形传态", "stance": "supports", "verification_status": "verified", "reason": "文内对可穿越虫洞与量子隐形传态类比。"}]
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
+# double trace 可穿越虫洞
+
+负能量流收缩视界；类比量子隐形传态。
```
