---
id: "proposal_71fb7be4e9d3a681722f77f9"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 ER=EPR 猜想表明虫洞/爱因斯坦-罗森桥与量子纠缠存在本质联系"
created_at: "2026-07-15T21:48:24+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_647ffb9287507f806c354670"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_er_epr_entanglement_20260715"
target_path: "vault/knowledge/claims/claim_wechat_er_epr_entanglement_20260715-该文称-er-epr-猜想表明虫洞-爱因斯坦-罗森桥与量子纠缠存在本质联系.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_71fb7be4e9d3a681722f77f9.md"
candidate_sha256: "deb82edc89f875a8b6671f5846a1d93edf11b4c441db39020adcf959c7de2d18"
change_reason: "导入 claim_wechat_er_epr_entanglement_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_647ffb9287507f806c354670", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "uncertainty": "理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 ER=EPR 猜想表明虫洞/爱因斯坦-罗森桥与量子纠缠存在本质联系

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_647ffb9287507f806c354670`
- Input SHA-256：`ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0`
- 不确定性：理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。
- 提议理由：导入 claim_wechat_er_epr_entanglement_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_er_epr_entanglement_20260715-该文称-er-epr-猜想表明虫洞-爱因斯坦-罗森桥与量子纠缠存在本质联系.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_er_epr_entanglement_20260715"
+title: "该文称 ER=EPR 猜想表明虫洞/爱因斯坦-罗森桥与量子纠缠存在本质联系"
+tags: ["er-epr", "quantum-entanglement", "holography"]
+domains: ["physics", "quantum-gravity"]
+confidence: "medium"
+applicability: ["AdS/CFT 与 TFD 态对应讨论", "Raamsdonk、Susskind-Maldacena 工作科普"]
+uncertainty: "ER=EPR 仍为猜想而非实验确立事实；TFD-AdS 虫洞对应为特定理论设定。"
+evidence: [{"evidence_id": "ev_2053", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 2053, "span_end": 2076, "original_text": "ER=EPR猜想[5]。(ER=EPR这个名号", "section": "ER=EPR 提出", "stance": "supports", "verification_status": "verified", "reason": "文内对 ER=EPR 猜想来源的说明。"}, {"evidence_id": "ev_2129", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 2129, "span_end": 2207, "original_text": "ER指代爱因斯坦-罗森桥，它是连接两个⿊洞之间的区域，可以看作是⾍洞研究的前⾝。不过它是不可穿越的，任何穿越爱因斯坦-罗森桥的举动，都不可避免的落⼊⿊洞奇点", "section": "ER 不可穿越", "stance": "supports", "verification_status": "verified", "reason": "文内对爱因斯坦-罗森桥性质的限制。"}, {"evidence_id": "ev_2623", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 2623, "span_end": 2640, "original_text": "深刻的联系，甚⾄于说它们本质上即是", "section": "纠缠-虫洞关联", "stance": "supports", "verification_status": "verified", "reason": "文内对纠缠与虫洞等价的表述。"}]
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
+# ER=EPR
+
+虫洞与量子纠缠深层关联；标准 ER 不可穿越。
```
