---
id: "proposal_c1713621678fdb624c389e7f"
type: "proposal"
status: "pending"
title: "模型提议：该文称 epiplexity 支持从模型中心转向数据中心主义，并指出文本模态认知复杂度通常高于图像/视频"
created_at: "2026-07-15T23:49:56+08:00"
updated_at: "2026-07-15T23:49:56+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_epiplexity_data_center_ai_20260715"
target_path: "vault/knowledge/claims/claim_wechat_epiplexity_data_center_ai_20260715-该文称-epiplexity-支持从模型中心转向数据中心主义-并指出文本模态认知复杂度通常高于图像-视频.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_c1713621678fdb624c389e7f.md"
candidate_sha256: "1a5f42b5ffd0eefc110fd973d298129ed4dd4304d1db8037b8dd1730a0947b02"
change_reason: "导入 claim_wechat_epiplexity_data_center_ai_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_494ab02c17c5f495f1ed29d0", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "uncertainty": "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 epiplexity 支持从模型中心转向数据中心主义，并指出文本模态认知复杂度通常高于图像/视频

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_494ab02c17c5f495f1ed29d0`
- Input SHA-256：`40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d`
- 不确定性：信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。
- 提议理由：导入 claim_wechat_epiplexity_data_center_ai_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_epiplexity_data_center_ai_20260715-该文称-epiplexity-支持从模型中心转向数据中心主义-并指出文本模态认知复杂度通常高于图像-视频.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_epiplexity_data_center_ai_20260715"
+title: "该文称 epiplexity 支持从模型中心转向数据中心主义，并指出文本模态认知复杂度通常高于图像/视频"
+tags: ["data-centric-ai", "epiplexity", "pretraining"]
+domains: ["machine-learning", "data-engineering"]
+confidence: "low"
+applicability: ["预训练数据筛选与课程学习讨论", "模态间 epiplexity 比较科普"]
+uncertainty: "文本>图像/视频为科普归纳，未给出统一 benchmark；工程模块为作者框架性主张。"
+evidence: [{"evidence_id": "ev_2968", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 2968, "span_end": 2993, "original_text": "数据中心主义」，让数据治理从经验直觉升级为严谨科学", "section": "工程转向", "stance": "supports", "verification_status": "verified", "reason": "文内对 AI 范式从模型到数据的转向。"}, {"evidence_id": "ev_3058", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 3058, "span_end": 3091, "original_text": "文本模态认知复杂度远超图像、视频的核心原因，为数据选择提供精准依据", "section": "模态差异", "stance": "supports", "verification_status": "verified", "reason": "文内对文本相对图像/视频 epiplexity 的表述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T23:50:00+08:00"
+updated_at: "2026-07-15T23:50:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 epiplexity 科普；等待人工核验"
+source_ids: ["source_494ab02c17c5f495f1ed29d0"]
+relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "由伊芝冰对 arXiv:2601.03220 epiplexity 论文的科普解读归纳；原论文未 capture"}]
+---
+
+# 数据中心 AI
+
+数据 epiplexity 决定泛化上限；文本常更高。
```
