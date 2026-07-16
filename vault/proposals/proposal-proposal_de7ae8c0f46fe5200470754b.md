---
id: "proposal_de7ae8c0f46fe5200470754b"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 ReLU/BatchNorm、线性层/注意力、Softmax 等常见架构具有连续对称性，Transformer 对称性为组件组合"
created_at: "2026-07-16T00:06:31+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_6ae6c4bef52010f96ddb3dbf"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_param_symmetry_architectures_20260716"
target_path: "vault/knowledge/claims/claim_wechat_param_symmetry_architectures_20260716-该文称-relu-batchnorm-线性层-注意力-softmax-等常见架构具有连续对称性-transformer-对称性为.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_de7ae8c0f46fe5200470754b.md"
candidate_sha256: "3aaa010039f8fa8553a12b35d56bade8cf4a022b1f68ad5a73b1fae6280f90cd"
change_reason: "导入 claim_wechat_param_symmetry_architectures_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_6ae6c4bef52010f96ddb3dbf", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "uncertainty": "DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 ReLU/BatchNorm、线性层/注意力、Softmax 等常见架构具有连续对称性，Transformer 对称性为组件组合

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_6ae6c4bef52010f96ddb3dbf`
- Input SHA-256：`1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e`
- 不确定性：DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。
- 提议理由：导入 claim_wechat_param_symmetry_architectures_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_param_symmetry_architectures_20260716-该文称-relu-batchnorm-线性层-注意力-softmax-等常见架构具有连续对称性-transformer-对称性为.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_param_symmetry_architectures_20260716"
+title: "该文称 ReLU/BatchNorm、线性层/注意力、Softmax 等常见架构具有连续对称性，Transformer 对称性为组件组合"
+tags: ["relu", "transformer", "continuous-symmetry"]
+domains: ["deep-learning", "architecture"]
+confidence: "medium"
+applicability: ["常见 NN 架构对称性分类", "多头注意力对称组合讨论"]
+uncertainty: "架构列举为综述性概括；各对称群精确形式需回原文。"
+evidence: [{"evidence_id": "ev_723", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 723, "span_end": 808, "original_text": "ReLU 网络与 BatchNorm / LayerNorm 等归一层具有正缩放对称；\n\n线性层和注意力机制具有一般线性（GL）对称；\n\nSoftmax 函数具有平移对称", "section": "连续对称类型", "stance": "supports", "verification_status": "verified", "reason": "文内对 ReLU/归一化/线性/Softmax 对称的列举。"}, {"evidence_id": "ev_978", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 978, "span_end": 1033, "original_text": "Transformer，其对称性是其各组件对称性的组合。例如，多头注意力机制同时具有每个头内部的广义线性对称性", "section": "Transformer 对称", "stance": "supports", "verification_status": "verified", "reason": "文内对 Transformer 组件对称组合的描述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:06:00+08:00"
+updated_at: "2026-07-16T00:06:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入参数空间对称性科普；等待人工核验"
+source_ids: ["source_6ae6c4bef52010f96ddb3dbf"]
+relations: [{"type": "derived_from", "target_id": "source_6ae6c4bef52010f96ddb3dbf", "reason": "由机器之心对 arXiv:2506.13018 参数空间对称性综述的科普转述归纳；原论文未 capture"}]
+---
+
+# 架构对称性
+
+缩放/GL/平移等连续对称；Transformer 为组合。
```
