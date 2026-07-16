---
id: "proposal_0aa86dc6117efd96f6378197"
type: "proposal"
status: "superseded"
title: "模型提议：该文称连续对称性将孤立极小值拉伸为平坦极小值流形，平坦方向未必反映更好泛化"
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
target_id: "claim_wechat_param_symmetry_flat_minima_20260716"
target_path: "vault/knowledge/claims/claim_wechat_param_symmetry_flat_minima_20260716-该文称连续对称性将孤立极小值拉伸为平坦极小值流形-平坦方向未必反映更好泛化.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_0aa86dc6117efd96f6378197.md"
candidate_sha256: "5f70a10dc2e2949e9b40aca84160eab5b2416f0d3e102f0bc15d52a24c1123e6"
change_reason: "导入 claim_wechat_param_symmetry_flat_minima_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_6ae6c4bef52010f96ddb3dbf", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "uncertainty": "DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称连续对称性将孤立极小值拉伸为平坦极小值流形，平坦方向未必反映更好泛化

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_6ae6c4bef52010f96ddb3dbf`
- Input SHA-256：`1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e`
- 不确定性：DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。
- 提议理由：导入 claim_wechat_param_symmetry_flat_minima_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_param_symmetry_flat_minima_20260716-该文称连续对称性将孤立极小值拉伸为平坦极小值流形-平坦方向未必反映更好泛化.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_param_symmetry_flat_minima_20260716"
+title: "该文称连续对称性将孤立极小值拉伸为平坦极小值流形，平坦方向未必反映更好泛化"
+tags: ["flat-minima", "generalization", "symmetry"]
+domains: ["deep-learning", "optimization"]
+confidence: "medium"
+applicability: ["用平坦度解释泛化的谨慎解读", "对称性塑造损失地形讨论"]
+uncertainty: "因果表述为科普归纳；与泛化关系的定量结论需回综述原文。"
+evidence: [{"evidence_id": "ev_715", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 715, "span_end": 1151, "original_text": "连续对称性：\n\nReLU 网络与 BatchNorm / LayerNorm 等归一层具有正缩放对称；\n\n线性层和注意力机制具有一般线性（GL）对称；\n\nSoftmax 函数具有平移对称；\n\n其他结构（如径向激活函数、RBF 网络）也呈现出旋转或尺度类对称。\n\n图 2 （左）ReLU 的缩放对称：对输入权重与偏置按对角矩阵 g 缩放，同时将输出权重乘以 g 的逆矩阵，函数保持不变。（右）自注意力的一般线性对称：键 (WK) 与查询 (WQ) 的线性变换 g 可以互相抵消，输出结果不变。\n\n更重要的是，复杂的现代架构，如 Transformer，其对称性是其各组件对称性的组合。例如，多头注意力机制同时具有每个头内部的广义线性对称性、头之间的排列对称性，以及与输出投影层相关的另一组线性对称性。\n\n从平坦极小值到模式连通性：对称性如何塑造损失地形\n\n对称性让优化空间既复杂又有规律。\n\n连续对称性（如缩放）会将一个孤立的极小值点 “拉伸” 成一个连续、平坦的极小值流形", "section": "平坦流形", "stance": "supports", "verification_status": "verified", "reason": "文内对连续对称性产生平坦极小值流形的说明。"}, {"evidence_id": "ev_1178", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 1178, "span_end": 1228, "original_text": "平坦方向并非来自更好的泛化，而是由结构对称性决定的。因此，传统用平坦度衡量泛化能力的指标需要谨慎解读", "section": "平坦度解读", "stance": "supports", "verification_status": "verified", "reason": "文内对平坦度作为泛化指标的限定。"}]
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
+# 平坦极小值
+
+对称性产生平坦方向；不等于泛化优势。
```
