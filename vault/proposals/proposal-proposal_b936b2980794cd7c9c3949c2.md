---
id: "proposal_b936b2980794cd7c9c3949c2"
type: "proposal"
status: "pending"
title: "模型提议：该文将模型合并/参数算术与线性模式连接作为不同训练模型共享潜在流形的证据"
created_at: "2026-07-16T00:29:35+08:00"
updated_at: "2026-07-16T00:29:35+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_model_merge_linear_connectivity_20260716"
target_path: "vault/knowledge/claims/claim_wechat_model_merge_linear_connectivity_20260716-该文将模型合并-参数算术与线性模式连接作为不同训练模型共享潜在流形的证据.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b936b2980794cd7c9c3949c2.md"
candidate_sha256: "d5682757171e8bc65d0f4b819920337beda5e5af2d85f2e6115d3ef4b4086870"
change_reason: "导入 claim_wechat_model_merge_linear_connectivity_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_f35b44d4bd383fb26ca49165", "input_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "uncertainty": "观点性科普；多处哲学推断；vec2vec/Anthropic/PRH 原文未 capture，需回引文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文将模型合并/参数算术与线性模式连接作为不同训练模型共享潜在流形的证据

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_f35b44d4bd383fb26ca49165`
- Input SHA-256：`0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0`
- 不确定性：观点性科普；多处哲学推断；vec2vec/Anthropic/PRH 原文未 capture，需回引文核验。
- 提议理由：导入 claim_wechat_model_merge_linear_connectivity_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_model_merge_linear_connectivity_20260716-该文将模型合并-参数算术与线性模式连接作为不同训练模型共享潜在流形的证据.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_model_merge_linear_connectivity_20260716"
+title: "该文将模型合并/参数算术与线性模式连接作为不同训练模型共享潜在流形的证据"
+tags: ["model-merging", "mode-connectivity", "weight-space"]
+domains: ["machine-learning", "optimization"]
+confidence: "low"
+applicability: ["模型合并与权重插值讨论", "线性模式连接作为共享结构证据的科普语境"]
+uncertainty: "从合并成功推断共享流形为哲学性跳跃；[8] 未 capture，与参数对称性等因素未区分。"
+evidence: [{"evidence_id": "ev_1592", "evidence_kind": "quote", "source_id": "source_f35b44d4bd383fb26ca49165", "content_id": "content_0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "extraction_id": "extraction_5175d74685def36cf73e75c3", "input_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "span_start": 1592, "span_end": 1614, "original_text": "两个模型相加，从而获得一个能同时胜任两种任务", "section": "模型合并", "stance": "supports", "verification_status": "verified", "reason": "文内对参数级模型合并可行性的表述。"}, {"evidence_id": "ev_1772", "evidence_kind": "quote", "source_id": "source_f35b44d4bd383fb26ca49165", "content_id": "content_0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "extraction_id": "extraction_5175d74685def36cf73e75c3", "input_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "span_start": 1772, "span_end": 1836, "original_text": "线性模式连接的存在——即在不同微调模型的权重之间存在一条损失保持不变的路径——是另一个关键证据，它指向了一个连贯的、潜在智能图景", "section": "模式连接", "stance": "supports", "verification_status": "verified", "reason": "文内将线性模式连接作为共享结构证据。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:26:00+08:00"
+updated_at: "2026-07-16T00:26:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 LLM 表征趋同观点文；等待人工核验"
+source_ids: ["source_f35b44d4bd383fb26ca49165"]
+relations: [{"type": "derived_from", "target_id": "source_f35b44d4bd383fb26ca49165", "reason": "由智能情报所转载 Lukas Nel 2025-07 观点文归纳；vec2vec/柏拉图表征等原论文未 capture"}]
+---
+
+# 模型合并与模式连接
+
+合并/连接被解释为共享流形；推断性强。
```
