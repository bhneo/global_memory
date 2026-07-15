---
id: "claim_play2perfect_sample_efficiency_20260715"
type: "claim"
status: "proposal"
title: "Play2Perfect 的 dexterous play 预训练使装配 RL 微调比从零训练（含稠密奖励）样本效率高约 33 倍"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-15T12:20:00+08:00"
aliases: ["Play2Perfect 33x"]
tags: ["dexterous-manipulation", "reinforcement-learning", "pretraining", "assembly"]
domains: ["robotics", "robot-learning"]
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Play2Perfect：仿真 play 预训练 + 稀疏奖励装配微调", "Tight-Insertion (Fixtured) wall-clock 对比", "Scratch (dense reward) 含 10 waypoint shaping", "22-DoF Sharpa 手 + 7-DoF KUKA iiwa 14"]
uncertainty: "33× 量化来自 Fixtured 任务 dense-scratch 对比；主任务 scratch 24h 无成功 rollout。不能外推为通用加速比。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "We show that our prior is 33x more sample-efficient than RL training from scratch, even when provided with dense, multi-stage rewards.", "stance": "supports", "reason": "摘要直接陈述样本效率倍数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "Scratch (dense reward) requires over 100 hours to reach near-perfect success, while Play2Perfect reaches the same success rate in only 4 hours, yielding a 33× speed-up.", "stance": "supports", "reason": "Fixtured 任务 wall-clock 对比。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "both scratch baselines produce no successful rollouts even after 24 hours", "stance": "context", "reason": "主任务 scratch 失败，限定对比范围。"}]
---

# Play2Perfect 33× 样本效率

见 evidence 与 uncertainty。
