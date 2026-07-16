---
id: "proposal_42cce1b31419d16a28efb9b7"
type: "proposal"
status: "superseded"
title: "模型提议：该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动"
created_at: "2026-07-15T20:52:19+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_magnetic_bottle_constraint_20260715"
target_path: "vault/knowledge/claims/claim_wechat_magnetic_bottle_constraint_20260715-该文称不均匀-磁瓶-磁镜-磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_42cce1b31419d16a28efb9b7.md"
candidate_sha256: "f1f075e6d14615ea5fbb6e5c69142de79f702e38e30d7da35b0ccd3ad7e6181f"
change_reason: "导入 claim_wechat_magnetic_bottle_constraint_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bd3bdfb9a5b1a728c3adf25", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "uncertainty": "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bd3bdfb9a5b1a728c3adf25`
- Input SHA-256：`acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669`
- 不确定性：科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。
- 提议理由：导入 claim_wechat_magnetic_bottle_constraint_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_magnetic_bottle_constraint_20260715-该文称不均匀-磁瓶-磁镜-磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_magnetic_bottle_constraint_20260715"
+title: "该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动"
+tags: ["magnetic-confinement", "magnetic-mirror", "plasma"]
+domains: ["physics", "plasma-physics"]
+confidence: "medium"
+applicability: ["高中/大学物理磁约束概念介绍", "两头强中间弱的不均匀磁场结构"]
+uncertainty: "为科普化推导，文内自述「不容易但可以证明」磁矩守恒；高速纵向粒子仍可能从磁瓶端逃逸。"
+evidence: [{"evidence_id": "ev_1184", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 1184, "span_end": 1282, "original_text": "当不均匀的磁场呈现两头强中间弱时，就会对带电粒子产生一种约束，使其只能在一定的空间范围内运动。\n\n由于带电粒子被限制在磁场内部，磁场看起来就像一个看不见的瓶子，因此这种磁场结构被形象的称作为磁瓶。", "section": "磁瓶结构", "stance": "supports", "verification_status": "verified", "reason": "文内对磁瓶命名的物理图像。"}, {"evidence_id": "ev_1609", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 1609, "span_end": 1655, "original_text": "粒子的纵向和横向的运动都受到限制，即带电粒子们被磁场约束起来了，这就是“磁约束”一词的由来！", "section": "磁约束结论", "stance": "supports", "verification_status": "verified", "reason": "文内对纵向/横向运动受限的总结。"}, {"evidence_id": "ev_1733", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 1733, "span_end": 1772, "original_text": "然而，磁瓶并不完美。对那些纵向速度  比较大的粒子，还是有可能从磁瓶两端逃逸。", "section": "磁镜泄漏", "stance": "supports", "verification_status": "verified", "reason": "文内对高纵向速度粒子逃逸的限制说明。"}]
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
+# 磁瓶约束
+
+磁矩近似守恒限制粒子；高速粒子可逃逸。
```
