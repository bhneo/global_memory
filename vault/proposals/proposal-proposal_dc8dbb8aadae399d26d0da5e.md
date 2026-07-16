---
id: "proposal_dc8dbb8aadae399d26d0da5e"
type: "proposal"
status: "superseded"
title: "模型提议：该文称全球约有 60 台托克马克与 10 台仿星器运行，且两者在保温与稳定性上各有优劣"
created_at: "2026-07-15T20:52:19+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_stellarator_vs_tokamak_20260715"
target_path: "vault/knowledge/claims/claim_wechat_stellarator_vs_tokamak_20260715-该文称全球约有-60-台托克马克与-10-台仿星器运行-且两者在保温与稳定性上各有优劣.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_dc8dbb8aadae399d26d0da5e.md"
candidate_sha256: "744c1a31591dfe15135e3c8e98ad484c175418908da40935439b92c578214916"
change_reason: "导入 claim_wechat_stellarator_vs_tokamak_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bd3bdfb9a5b1a728c3adf25", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "uncertainty": "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称全球约有 60 台托克马克与 10 台仿星器运行，且两者在保温与稳定性上各有优劣

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bd3bdfb9a5b1a728c3adf25`
- Input SHA-256：`acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669`
- 不确定性：科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。
- 提议理由：导入 claim_wechat_stellarator_vs_tokamak_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_stellarator_vs_tokamak_20260715-该文称全球约有-60-台托克马克与-10-台仿星器运行-且两者在保温与稳定性上各有优劣.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_stellarator_vs_tokamak_20260715"
+title: "该文称全球约有 60 台托克马克与 10 台仿星器运行，且两者在保温与稳定性上各有优劣"
+tags: ["stellarator", "tokamak", "fusion"]
+domains: ["physics", "energy"]
+confidence: "low"
+applicability: ["2022 科普文对全球聚变装置数量的概述", "仿星器扭转螺旋磁场的约束思路"]
+uncertainty: "60/10 台数量为文内单点统计，随新建/退役装置变化；优劣对比为概括性说法。"
+evidence: [{"evidence_id": "ev_2221", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2221, "span_end": 2277, "original_text": "基于以上这种扭转磁场的装置被称作仿星器（stellarator），是未来核聚变电站的一种重要的反应堆设备候选者。", "section": "仿星器定义", "stance": "supports", "verification_status": "verified", "reason": "文内对 stellarator 的命名与定位。"}, {"evidence_id": "ev_2775", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2775, "span_end": 2816, "original_text": "目前世界上约有60台托克马克和10台仿星器在运行。\n\n这两种反应器都有一定的优点。", "section": "全球数量", "stance": "supports", "verification_status": "verified", "reason": "文内对运行中装置数量的表述。"}, {"evidence_id": "ev_2816", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2816, "span_end": 2888, "original_text": "托克马克能更好地保持等离子体的高温，而仿星器能更好地维持等离子体的稳定。尽管托克马克目前很流行，仿星器仍有可能有一天成为未来聚变能源工厂的首选。", "section": "装置对比", "stance": "supports", "verification_status": "verified", "reason": "文内对两类装置优缺点的对比总结。"}]
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
+# 托卡马克 vs 仿星器
+
+约 60 vs 10 台；保温 vs 稳定性权衡。
```
