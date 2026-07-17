---
id: "claim_agentic_vla_cross_task_20260715"
type: "claim"
status: "working"
title: "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: []
tags: ["vla", "cross-task", "transfer"]
domains: ["robot-learning"]
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Long 训练 → Object 评估", "无 Object task-specific demos", "5 seeds"]
uncertainty: "31.2% 远低于全监督 96.6%（50 demos）；Progress 68.7%。"
evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "cross-task transfer from 0% to 31.2% without task-specific demonstrations", "stance": "supports", "reason": "摘要陈述。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Table 3", "excerpt": "Direct Transfer (SFT) 0.0±0.0 ... Agentic-VLA 31.2±2.3", "stance": "supports", "reason": "Table 3。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Section 4.4", "excerpt": "direct transfer to LIBERO-Object achieves 0% success rate", "stance": "context", "reason": "0% 基线条件。"}]
memory_tier: "working"
created_by: "human-candidate-revision-v1"
updated_by: "weekly-consolidation-v1"
model_provider: null
model_version: null
compiler_version: "human-candidate-revision-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-17T12:01:10+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_e79a010f0e001d3b10c7e7ed"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_e79a010f0e001d3b10c7e7ed.md"
origin_candidate_sha256: "87717e14de3cbc85d9220f0da744526d54b5c2c6aff2e116d70f2d634a974a63"
memory_schema_version: 1
---

# Agentic-VLA 的跨任务适应结果

论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT) 的成功率为 `0.0±0.0%`，EVOLVE-VLA 为 `20.8±2.7%`，Agentic-VLA 通过在线适应达到 `31.2±2.3%`；对应任务进度为 `68.7±3.1%`。

该结果说明在线适应在论文设定中产生了非零跨任务成功率，但 31.2% 仍远低于使用 50 条 demonstrations 的全监督结果 96.6%，不能表述为已经解决跨任务泛化。
