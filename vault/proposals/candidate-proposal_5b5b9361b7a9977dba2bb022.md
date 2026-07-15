---
id: "claim_agentic_vla_cross_task_20260715"
type: "claim"
status: "proposal"
title: "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-15T12:20:00+08:00"
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
---

# 跨任务

Table 3。
