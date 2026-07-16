---
id: "proposal_5e9c8f4027bf92eee74bf0b3"
type: "proposal"
status: "superseded"
title: "模型提议：该文称连续对称性在梯度流中对应守恒量，影响隐式偏置与收敛/泛化统计"
created_at: "2026-07-16T00:06:32+08:00"
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
target_id: "claim_wechat_param_symmetry_conserved_quantities_20260716"
target_path: "vault/knowledge/claims/claim_wechat_param_symmetry_conserved_quantities_20260716-该文称连续对称性在梯度流中对应守恒量-影响隐式偏置与收敛-泛化统计.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5e9c8f4027bf92eee74bf0b3.md"
candidate_sha256: "d6335b5e1188b484d3af3823fa6c0414d205c9a2685c75134adec3d06980b342"
change_reason: "导入 claim_wechat_param_symmetry_conserved_quantities_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_6ae6c4bef52010f96ddb3dbf", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "uncertainty": "DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称连续对称性在梯度流中对应守恒量，影响隐式偏置与收敛/泛化统计

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_6ae6c4bef52010f96ddb3dbf`
- Input SHA-256：`1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e`
- 不确定性：DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。
- 提议理由：导入 claim_wechat_param_symmetry_conserved_quantities_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_param_symmetry_conserved_quantities_20260716-该文称连续对称性在梯度流中对应守恒量-影响隐式偏置与收敛-泛化统计.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_param_symmetry_conserved_quantities_20260716"
+title: "该文称连续对称性在梯度流中对应守恒量，影响隐式偏置与收敛/泛化统计"
+tags: ["conserved-quantities", "implicit-bias", "gradient-flow"]
+domains: ["deep-learning", "optimization"]
+confidence: "medium"
+applicability: ["诺特定理类比下的训练动力学讨论", "初始化与守恒量关系"]
+uncertainty: "守恒量例子（Gram 矩阵差等）为科普列举；严格定理条件需回原文。"
+evidence: [{"evidence_id": "ev_1860", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 1860, "span_end": 1898, "original_text": "守恒量（conserved quantities）—— 类似物理中的诺特定理", "section": "对称与守恒", "stance": "supports", "verification_status": "verified", "reason": "文内将对称性与守恒量的物理类比。"}, {"evidence_id": "ev_2009", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 2009, "span_end": 2092, "original_text": "隐式偏置（implicit bias）：\n\n不同的初始化对应不同的守恒量值，进而影响最终的收敛点和泛化性能。也就是说，参数空间的对称结构决定了学习轨迹与结果的统计分布", "section": "隐式偏置", "stance": "supports", "verification_status": "verified", "reason": "文内对守恒量影响收敛与泛化分布的说明。"}]
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
+# 守恒量与隐式偏置
+
+对称结构约束梯度流轨迹与结果分布。
```
