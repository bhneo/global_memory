---
id: "proposal_db216ece4bf90421ac4a8220"
type: "proposal"
status: "superseded"
title: "模型提议：Agentic-VLA 在 LIBERO-Long 上达到 90% 成功率所需迭代约为 EVOLVE-VLA 的 2.4 倍更少（700 vs 1680）"
created_at: "2026-07-15T12:25:13+08:00"
updated_at: "2026-07-15T14:27:52+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_agentic_vla_training_efficiency_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_training_efficiency_20260715-agentic-vla-在-libero-long-上达到-90-成功率所需迭代约为-evolve-vla-的-2-4-倍更少-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_db216ece4bf90421ac4a8220.md"
candidate_sha256: "19275be1a822d7c9c6f8798514b2cef5f05d970b5cdca3c19a2772dde5721c7c"
change_reason: "Agentic-VLA 效率"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_2c21320690e566fbbf80fd75", "input_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:27:52+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_0e1b5b493ea68c0127447da6"
---

# 模型提议：Agentic-VLA 在 LIBERO-Long 上达到 90% 成功率所需迭代约为 EVOLVE-VLA 的 2.4 倍更少（700 vs 1680）

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_2c21320690e566fbbf80fd75`
- Input SHA-256：`8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Agentic-VLA 效率
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_training_efficiency_20260715-agentic-vla-在-libero-long-上达到-90-成功率所需迭代约为-evolve-vla-的-2-4-倍更少-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_agentic_vla_training_efficiency_20260715"
+type: "claim"
+status: "proposal"
+title: "Agentic-VLA 在 LIBERO-Long 上达到 90% 成功率所需迭代约为 EVOLVE-VLA 的 2.4 倍更少（700 vs 1680）"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["vla", "training-efficiency"]
+domains: ["robot-learning"]
+confidence: "medium"
+source_ids: ["source_2c21320690e566fbbf80fd75"]
+relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["LIBERO-Long", "90% SR 收敛阈值", "Table 4 对比 SimpleVLA-RL / EVOLVE-VLA"]
+uncertainty: "90% 为论文自定义阈值；wall-clock 未量化。"
+evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "2.4× faster convergence compared to existing online adaptation methods", "stance": "supports", "reason": "摘要加速比。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8-9 页 Table 4", "excerpt": "EVOLVE-VLA 1,680 ... Agentic-VLA 700 ... 2.4×", "stance": "supports", "reason": "Table 4 迭代与 speedup。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 9 页 Section 4.5", "excerpt": "only 22.4k rollouts to achieve target performance, compared to 53.8k for EVOLVE-VLA", "stance": "supports", "reason": "rollout 规模。"}]
+---
+
+# 训练效率
+
+Table 4。
```
