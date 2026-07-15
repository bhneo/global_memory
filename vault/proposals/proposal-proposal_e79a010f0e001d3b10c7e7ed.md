---
id: "proposal_e79a010f0e001d3b10c7e7ed"
type: "proposal"
status: "pending"
title: "修订：模型提议：Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%"
created_at: "2026-07-15T14:27:40+08:00"
updated_at: "2026-07-15T14:27:40+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "supersedes", "target_id": "proposal_5b5b9361b7a9977dba2bb022", "reason": "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"}]
proposal_kind: "knowledge_revision"
processor: "human-candidate-revision-v1"
action: "create"
target_id: "claim_agentic_vla_cross_task_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_cross_task_20260715-agentic-vla-在-libero-long-训练后无-object-演示的跨任务适应达-31-2-成功率-direct-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e79a010f0e001d3b10c7e7ed.md"
candidate_sha256: "87717e14de3cbc85d9220f0da744526d54b5c2c6aff2e116d70f2d634a974a63"
change_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
revision_of: "proposal_5b5b9361b7a9977dba2bb022"
reviewed_at: null
review_reason: null
---

# 修订：模型提议：Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%

## 修订说明

- 被替代 proposal：`proposal_5b5b9361b7a9977dba2bb022`
- 修订理由：人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份
- 建议操作：`create` `vault/knowledge/claims/claim_agentic_vla_cross_task_20260715-agentic-vla-在-libero-long-训练后无-object-演示的跨任务适应达-31-2-成功率-direct-.md`
- 原 candidate 保持不可变；本 proposal 使用新的 candidate。

## Base → Revised Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_cross_task_20260715-agentic-vla-在-libero-long-训练后无-object-演示的跨任务适应达-31-2-成功率-direct-.md
@@ -0,0 +1,26 @@
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
+# Agentic-VLA 的跨任务适应结果
+
+论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT) 的成功率为 `0.0±0.0%`，EVOLVE-VLA 为 `20.8±2.7%`，Agentic-VLA 通过在线适应达到 `31.2±2.3%`；对应任务进度为 `68.7±3.1%`。
+
+该结果说明在线适应在论文设定中产生了非零跨任务成功率，但 31.2% 仍远低于使用 50 条 demonstrations 的全监督结果 96.6%，不能表述为已经解决跨任务泛化。
```
