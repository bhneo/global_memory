---
id: "proposal_5b5b9361b7a9977dba2bb022"
type: "proposal"
status: "superseded"
title: "模型提议：Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%"
created_at: "2026-07-15T12:25:12+08:00"
updated_at: "2026-07-15T14:27:40+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_agentic_vla_cross_task_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_cross_task_20260715-agentic-vla-在-libero-long-训练后无-object-演示的跨任务适应达-31-2-成功率-direct-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_5b5b9361b7a9977dba2bb022.md"
candidate_sha256: "d5188dcbad169fe22a449b1d3837c46be3bf3ccc5415f2171c4d6fedaf211e5a"
change_reason: "Agentic-VLA 跨任务"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_2c21320690e566fbbf80fd75", "input_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:27:40+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_e79a010f0e001d3b10c7e7ed"
---

# 模型提议：Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_2c21320690e566fbbf80fd75`
- Input SHA-256：`8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Agentic-VLA 跨任务
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_cross_task_20260715-agentic-vla-在-libero-long-训练后无-object-演示的跨任务适应达-31-2-成功率-direct-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_agentic_vla_cross_task_20260715"
+type: "claim"
+status: "proposal"
+title: "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["vla", "cross-task", "transfer"]
+domains: ["robot-learning"]
+confidence: "medium"
+source_ids: ["source_2c21320690e566fbbf80fd75"]
+relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Long 训练 → Object 评估", "无 Object task-specific demos", "5 seeds"]
+uncertainty: "31.2% 远低于全监督 96.6%（50 demos）；Progress 68.7%。"
+evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "cross-task transfer from 0% to 31.2% without task-specific demonstrations", "stance": "supports", "reason": "摘要陈述。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Table 3", "excerpt": "Direct Transfer (SFT) 0.0±0.0 ... Agentic-VLA 31.2±2.3", "stance": "supports", "reason": "Table 3。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Section 4.4", "excerpt": "direct transfer to LIBERO-Object achieves 0% success rate", "stance": "context", "reason": "0% 基线条件。"}]
+---
+
+# 跨任务
+
+Table 3。
```
