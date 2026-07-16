---
id: "proposal_8fb0cc460c15e1ce57d9e275"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 replica trick 计算霍金辐射精确熵时需考虑连通「拷贝虫洞」构型，与岛屿公式及幺正性恢复相关"
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
target_id: "claim_wechat_replica_wormhole_island_20260715"
target_path: "vault/knowledge/claims/claim_wechat_replica_wormhole_island_20260715-该文称-replica-trick-计算霍金辐射精确熵时需考虑连通-拷贝虫洞-构型-与岛屿公式及幺正性恢复相关.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_8fb0cc460c15e1ce57d9e275.md"
candidate_sha256: "18a3a779291b5f28942368771979b1e9c757fab84466c86901d6ce1b509f37e1"
change_reason: "导入 claim_wechat_replica_wormhole_island_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_647ffb9287507f806c354670", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "uncertainty": "理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 replica trick 计算霍金辐射精确熵时需考虑连通「拷贝虫洞」构型，与岛屿公式及幺正性恢复相关

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_647ffb9287507f806c354670`
- Input SHA-256：`ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0`
- 不确定性：理论物理科普；ER=EPR 为猜想；经典论文未 capture，需回原文核验。
- 提议理由：导入 claim_wechat_replica_wormhole_island_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_replica_wormhole_island_20260715-该文称-replica-trick-计算霍金辐射精确熵时需考虑连通-拷贝虫洞-构型-与岛屿公式及幺正性恢复相关.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_replica_wormhole_island_20260715"
+title: "该文称 replica trick 计算霍金辐射精确熵时需考虑连通「拷贝虫洞」构型，与岛屿公式及幺正性恢复相关"
+tags: ["replica-wormhole", "black-hole-information", "island-formula"]
+domains: ["physics", "quantum-gravity"]
+confidence: "medium"
+applicability: ["欧式路径积分与 replica trick 熵计算", "2019–2020 岛屿/replica wormhole 研究科普"]
+uncertainty: "拷贝虫洞物理含义文内称「仍有待澄清」；岛屿公式与全连通构型关系为科普概述。"
+evidence: [{"evidence_id": "ev_3922", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 3922, "span_end": 3927, "original_text": "岛屿公式。", "section": "岛屿公式", "stance": "supports", "verification_status": "verified", "reason": "文内对精确熵计算方法的引入。"}, {"evidence_id": "ev_4527", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 4527, "span_end": 4684, "original_text": "连通的构型。\n\n⼀个简单的⽰意图：左侧来⾃辐射密度矩阵形成的边界条件（实线代表做了求迹之后的⿊洞边界，虚线代表辐射），右侧代表计算所需要的引⼒构型。第⼀个图是⾮连通的构型，第⼆个图代表连通的拷贝⾍洞构型。图⽚来：arXiv: 1911.11977\n\n当不考虑连通构型之时，可以得到和霍⾦最初的计算相符的熵，此时违反", "section": "拷贝虫洞与幺正性", "stance": "supports", "verification_status": "verified", "reason": "文内对比非连通与连通构型对熵/幺正性的影响。"}, {"evidence_id": "ev_4845", "evidence_kind": "quote", "source_id": "source_647ffb9287507f806c354670", "content_id": "content_ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "extraction_id": "extraction_5ed8cc221c9d9bcce0c53950", "input_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "span_start": 4845, "span_end": 4884, "original_text": "洛伦兹型的⾍洞对应的物理却⼤不相同，⽽它具体的物理含义仍然有待更多的理解和澄清", "section": "物理含义未定", "stance": "supports", "verification_status": "verified", "reason": "文内对欧几里得拷贝虫洞与洛伦兹虫洞差异的限定。"}]
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
+# 拷贝虫洞
+
+replica 连通构型参与精确熵；关联 Page 曲线/幺正性。
```
