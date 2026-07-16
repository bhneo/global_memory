---
id: "proposal_bf3e32b99ca9d572db69861e"
type: "proposal"
status: "pending"
title: "模型提议：该文称等离子体为物质第四态，且在宇宙可见物质中占比超过 99.9%"
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
target_id: "claim_wechat_plasma_universe_fraction_20260715"
target_path: "vault/knowledge/claims/claim_wechat_plasma_universe_fraction_20260715-该文称等离子体为物质第四态-且在宇宙可见物质中占比超过-99-9.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_bf3e32b99ca9d572db69861e.md"
candidate_sha256: "a0bf3bd7cecee53fb6d0a9b649434477c9bd1bda1254a581553e0c88db96c9b7"
change_reason: "导入 claim_wechat_plasma_universe_fraction_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bd3bdfb9a5b1a728c3adf25", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "uncertainty": "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称等离子体为物质第四态，且在宇宙可见物质中占比超过 99.9%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bd3bdfb9a5b1a728c3adf25`
- Input SHA-256：`acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669`
- 不确定性：科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。
- 提议理由：导入 claim_wechat_plasma_universe_fraction_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_plasma_universe_fraction_20260715-该文称等离子体为物质第四态-且在宇宙可见物质中占比超过-99-9.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_plasma_universe_fraction_20260715"
+title: "该文称等离子体为物质第四态，且在宇宙可见物质中占比超过 99.9%"
+tags: ["plasma", "astrophysics", "fourth-state"]
+domains: ["physics", "plasma-physics"]
+confidence: "medium"
+applicability: ["大学物理学/中科院物理所科普语境", "可见宇宙物质组成的一般性描述"]
+uncertainty: "99.9% 为科普常用数量级表述，精确比例依测量与定义边界而异；非 peer-reviewed 原文。"
+evidence: [{"evidence_id": "ev_0", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 0, "span_end": 84, "original_text": "作为物质的第四态，等离子体物质是部分或完全电离的气态物质，由大量自由电子、阳离子和中性原子及分子组成。在宇宙可见物质中，等离子物质占比超过99.9%，典型的如恒星物质。", "section": "等离子体定义", "stance": "supports", "verification_status": "verified", "reason": "文内对等离子体组成与宇宙占比的描述。"}]
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
+# 等离子体占比
+
+第四态；可见宇宙物质 >99.9% 为等离子体。
```
