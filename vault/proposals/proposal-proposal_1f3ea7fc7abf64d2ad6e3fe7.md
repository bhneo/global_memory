---
id: "proposal_1f3ea7fc7abf64d2ad6e3fe7"
type: "proposal"
status: "superseded"
title: "模型提议：该文称模式连通性与模型融合部分源于对称性，离散置换对称使极小值副本数随宽度阶乘增长"
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
target_id: "claim_wechat_param_symmetry_mode_connectivity_20260716"
target_path: "vault/knowledge/claims/claim_wechat_param_symmetry_mode_connectivity_20260716-该文称模式连通性与模型融合部分源于对称性-离散置换对称使极小值副本数随宽度阶乘增长.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1f3ea7fc7abf64d2ad6e3fe7.md"
candidate_sha256: "1ab6423c3d483c8bcdb9f9f647c6f40d9f39c91e69a9141a895750fa4b41987a"
change_reason: "导入 claim_wechat_param_symmetry_mode_connectivity_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_6ae6c4bef52010f96ddb3dbf", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "uncertainty": "DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称模式连通性与模型融合部分源于对称性，离散置换对称使极小值副本数随宽度阶乘增长

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_6ae6c4bef52010f96ddb3dbf`
- Input SHA-256：`1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e`
- 不确定性：DL 理论科普；原综述 arXiv:2506.13018 未 capture，需回原文核验定理与实验。
- 提议理由：导入 claim_wechat_param_symmetry_mode_connectivity_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_param_symmetry_mode_connectivity_20260716-该文称模式连通性与模型融合部分源于对称性-离散置换对称使极小值副本数随宽度阶乘增长.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_param_symmetry_mode_connectivity_20260716"
+title: "该文称模式连通性与模型融合部分源于对称性，离散置换对称使极小值副本数随宽度阶乘增长"
+tags: ["mode-connectivity", "permutation-symmetry", "model-fusion"]
+domains: ["deep-learning", "optimization"]
+confidence: "medium"
+applicability: ["独立训练模型低损耗路径连接讨论", "宽度与极小值数量关系科普"]
+uncertainty: "「部分源于」为综述性解释；阶乘增长为定性表述。"
+evidence: [{"evidence_id": "ev_1073", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 1073, "span_end": 1330, "original_text": "模式连通性：对称性如何塑造损失地形\n\n对称性让优化空间既复杂又有规律。\n\n连续对称性（如缩放）会将一个孤立的极小值点 “拉伸” 成一个连续、平坦的极小值流形。沿着这个流形移动，损失值保持不变。这意味着网络的许多平坦方向并非来自更好的泛化，而是由结构对称性决定的。因此，传统用平坦度衡量泛化能力的指标需要谨慎解读。\n\n另外，实践中观察到的 “模式连通性”—— 即独立训练得到的模型往往能通过低损耗路径连接 —— 其背后也部分源于连续对称性。对称性天然地在参数空间中创造出连接功能等价参数的连续路径，从而解释了模型融合", "section": "模式连通性", "stance": "supports", "verification_status": "verified", "reason": "文内将模式连通性与对称性、模型融合关联。"}, {"evidence_id": "ev_1419", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 1419, "span_end": 1494, "original_text": "离散对称性（如神经元置换）则会在参数空间的不同位置复制出大量功能完全相同的极小值 “副本”。这使损失地形更加复杂，其极小值的数量随网络宽度呈阶乘级增长", "section": "置换副本", "stance": "supports", "verification_status": "verified", "reason": "文内对离散对称复制极小值的说明。"}]
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
+# 模式连通性
+
+对称性提供连接路径；置换使极小值副本爆炸。
```
