---
id: "proposal_5c9700513e8a69e5520b393d"
type: "proposal"
status: "pending"
title: "模型提议：该文称等离子体温度跨度很大：低温等离子体可仅几十摄氏度，聚变点火温度可达上亿度"
created_at: "2026-07-15T20:52:19+08:00"
updated_at: "2026-07-15T20:52:19+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_plasma_temperature_range_20260715"
target_path: "vault/knowledge/claims/claim_wechat_plasma_temperature_range_20260715-该文称等离子体温度跨度很大-低温等离子体可仅几十摄氏度-聚变点火温度可达上亿度.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5c9700513e8a69e5520b393d.md"
candidate_sha256: "f21f6be99f1c4aed6fc82acd8c4fbbac6c6a51440e78e8134cf2d2723b5ce53c"
change_reason: "导入 claim_wechat_plasma_temperature_range_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bd3bdfb9a5b1a728c3adf25", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "uncertainty": "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称等离子体温度跨度很大：低温等离子体可仅几十摄氏度，聚变点火温度可达上亿度

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bd3bdfb9a5b1a728c3adf25`
- Input SHA-256：`acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669`
- 不确定性：科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。
- 提议理由：导入 claim_wechat_plasma_temperature_range_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_plasma_temperature_range_20260715-该文称等离子体温度跨度很大-低温等离子体可仅几十摄氏度-聚变点火温度可达上亿度.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_plasma_temperature_range_20260715"
+title: "该文称等离子体温度跨度很大：低温等离子体可仅几十摄氏度，聚变点火温度可达上亿度"
+tags: ["plasma", "fusion", "temperature"]
+domains: ["physics", "plasma-physics"]
+confidence: "medium"
+applicability: ["文内对等离子体电视与太阳核心/聚变点火的对比", "温度数量级科普"]
+uncertainty: "「几乎没有上限」为修辞；50mK 超冷等离子体案例引自 2009 Science 报道但未 capture 原文。"
+evidence: [{"evidence_id": "ev_136", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 136, "span_end": 159, "original_text": "低温等离子体只有几十度，例如等离子体电视屏幕。", "section": "低温等离子体", "stance": "supports", "verification_status": "verified", "reason": "文内低温等离子体例子。"}, {"evidence_id": "ev_179", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 179, "span_end": 216, "original_text": "太阳中心温度高达1500万度，而氢的热核聚变反应的点火温度更是高达上亿度。", "section": "高温等离子体", "stance": "supports", "verification_status": "verified", "reason": "文内对恒星与聚变点火温度的数量级。"}, {"evidence_id": "ev_247", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 247, "span_end": 291, "original_text": "Science就曾报道了一种处在50mK低温的等离子体，它是通过对超冷原子光电离得到的。", "section": "超冷等离子体", "stance": "supports", "verification_status": "verified", "reason": "文内对 2009 人造超冷等离子体的转述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T20:30:00+08:00"
+updated_at: "2026-07-15T20:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入等离子体磁约束科普；等待人工核验"
+source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
+relations: [{"type": "derived_from", "target_id": "source_9bd3bdfb9a5b1a728c3adf25", "reason": "由中科院物理所转载的等离子体/磁约束科普文章归纳；非原始实验论文"}]
+---
+
+# 等离子体温度范围
+
+几十度到上亿度的跨度。
```
