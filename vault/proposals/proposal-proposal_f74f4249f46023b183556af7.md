---
id: "proposal_f74f4249f46023b183556af7"
type: "proposal"
status: "pending"
title: "模型提议：该文称 epiplexity（认知复杂度）指在算力约束下观察者能从数据中提取的可复用、可泛化结构信息总量"
created_at: "2026-07-15T23:49:56+08:00"
updated_at: "2026-07-15T23:49:56+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_epiplexity_definition_20260715"
target_path: "vault/knowledge/claims/claim_wechat_epiplexity_definition_20260715-该文称-epiplexity-认知复杂度-指在算力约束下观察者能从数据中提取的可复用-可泛化结构信息总量.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f74f4249f46023b183556af7.md"
candidate_sha256: "9f33dd97d2ce7ab3bbefa436a560390b74e4acd6faaabfcc544ebe87c83e60a8"
change_reason: "导入 claim_wechat_epiplexity_definition_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_494ab02c17c5f495f1ed29d0", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "uncertainty": "信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 epiplexity（认知复杂度）指在算力约束下观察者能从数据中提取的可复用、可泛化结构信息总量

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_494ab02c17c5f495f1ed29d0`
- Input SHA-256：`40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d`
- 不确定性：信息论/AI 科普；原论文 arXiv:2601.03220 未 capture，需回原文核验定理与公式。
- 提议理由：导入 claim_wechat_epiplexity_definition_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_epiplexity_definition_20260715-该文称-epiplexity-认知复杂度-指在算力约束下观察者能从数据中提取的可复用-可泛化结构信息总量.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_epiplexity_definition_20260715"
+title: "该文称 epiplexity（认知复杂度）指在算力约束下观察者能从数据中提取的可复用、可泛化结构信息总量"
+tags: ["epiplexity", "information-theory", "computational-bounds"]
+domains: ["information-theory", "machine-learning"]
+confidence: "medium"
+applicability: ["有限算力观察者视角的信息论", "2026 From Entropy to Epiplexity 论文科普语境"]
+uncertainty: "为第三方科普转述；形式化定义细节需回 arXiv:2601.03220 核验。"
+evidence: [{"evidence_id": "ev_1198", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 1198, "span_end": 1231, "original_text": "算力约束下，观察者能从数据中提取的、可复用、可泛化的结构性信息总量", "section": "核心定义", "stance": "supports", "verification_status": "verified", "reason": "文内对 epiplexity 的第三代范式定义。"}, {"evidence_id": "ev_1348", "evidence_kind": "quote", "source_id": "source_494ab02c17c5f495f1ed29d0", "content_id": "content_40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "extraction_id": "extraction_5281bc038cb077d2d54e9da5", "input_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "span_start": 1348, "span_end": 1404, "original_text": "香农熵解决了「信息能不能传过去」的问题，而 epiplexity 解决了「信息能不能被学会、能不能用来解决新问题", "section": "与香农熵关系", "stance": "supports", "verification_status": "verified", "reason": "文内对比香农熵与 epiplexity 的分工。"}]
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
+# Epiplexity 定义
+
+有限算力下可学习结构信息；拓展经典信息论边界。
```
