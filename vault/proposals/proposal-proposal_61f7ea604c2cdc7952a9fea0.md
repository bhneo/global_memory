---
id: "proposal_61f7ea604c2cdc7952a9fea0"
type: "proposal"
status: "pending"
title: "模型提议：该文引述 Moravec 悖论：逻辑/数学对计算机易，行走抓取等身体智能难；称当前大模型「缸中之脑」缺乏物理世界感知"
created_at: "2026-07-16T11:12:50+08:00"
updated_at: "2026-07-16T11:12:50+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_6ada1b3b0033883b83a3bf40"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_jiuwen_moravec_embodiment_gap_20260716"
target_path: "vault/knowledge/claims/claim_wechat_jiuwen_moravec_embodiment_gap_20260716-该文引述-moravec-悖论-逻辑-数学对计算机易-行走抓取等身体智能难-称当前大模型-缸中之脑-缺乏物理世界感知.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_61f7ea604c2cdc7952a9fea0.md"
candidate_sha256: "0979407acb65d0633eaea7a9ddd7da266e31778464fd5109dc0bdf479f6cde0a"
change_reason: "导入 claim_wechat_jiuwen_moravec_embodiment_gap_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_6ada1b3b0033883b83a3bf40", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "uncertainty": "量子位/openJiuwen 软文；产品能力与 benchmark 需独立验证，confidence 偏低。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文引述 Moravec 悖论：逻辑/数学对计算机易，行走抓取等身体智能难；称当前大模型「缸中之脑」缺乏物理世界感知

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_6ada1b3b0033883b83a3bf40`
- Input SHA-256：`d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567`
- 不确定性：量子位/openJiuwen 软文；产品能力与 benchmark 需独立验证，confidence 偏低。
- 提议理由：导入 claim_wechat_jiuwen_moravec_embodiment_gap_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_jiuwen_moravec_embodiment_gap_20260716-该文引述-moravec-悖论-逻辑-数学对计算机易-行走抓取等身体智能难-称当前大模型-缸中之脑-缺乏物理世界感知.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_jiuwen_moravec_embodiment_gap_20260716"
+title: "该文引述 Moravec 悖论：逻辑/数学对计算机易，行走抓取等身体智能难；称当前大模型「缸中之脑」缺乏物理世界感知"
+tags: ["Moravec-paradox", "embodied-ai", "physical-ai"]
+domains: ["robotics", "artificial-intelligence"]
+confidence: "medium"
+applicability: ["physical AI 动机论述", "1988 Moravec 引述"]
+uncertainty: "悖论表述为科普常见转述；「最大局限之一」为作者观点。"
+evidence: [{"evidence_id": "ev_424", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 424, "span_end": 503, "original_text": "Moravec悖论：最难的不是高数，而是走路\n\n1988年，机器人学家Hans Moravec提出了后来著名的Moravec's Paradox（莫拉维克悖论", "section": "Moravec 引入", "stance": "supports", "verification_status": "verified", "reason": "文内对 Moravec 悖论名称与提出者的说明。"}, {"evidence_id": "ev_639", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 639, "span_end": 682, "original_text": "缸中之脑”困境：智商200，但没有实体，对真实物理世界的摩擦力、重力和空间几何一无所知", "section": " embodiment 缺口", "stance": "supports", "verification_status": "verified", "reason": "文内对大模型缺乏物理实体知识的比喻。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:10:00+08:00"
+updated_at: "2026-07-16T11:10:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 Jiuwen Symbiosis 宣传文；等待人工核验"
+source_ids: ["source_6ada1b3b0033883b83a3bf40"]
+relations: [{"type": "derived_from", "target_id": "source_6ada1b3b0033883b83a3bf40", "reason": "量子位授权转载 openJiuwen Jiuwen Symbiosis 开源宣传；属 vendor/社区软文"}]
+---
+
+# Moravec / 缸中之脑
+
+Agent 可操作数字世界但难触达物理世界。
```
