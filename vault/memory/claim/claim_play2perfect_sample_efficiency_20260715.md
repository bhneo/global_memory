---
id: "claim_play2perfect_sample_efficiency_20260715"
type: "claim"
status: "working"
title: "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: ["Play2Perfect 33x"]
tags: ["dexterous-manipulation", "reinforcement-learning", "pretraining", "assembly"]
domains: ["robotics", "robot-learning"]
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Play2Perfect：仿真 play 预训练 + 稀疏奖励装配微调", "Tight-Insertion (Fixtured) wall-clock 对比", "Scratch (dense reward) 含 10 waypoint shaping", "22-DoF Sharpa 手 + 7-DoF KUKA iiwa 14"]
uncertainty: "33× 量化来自 Fixtured 任务 dense-scratch 对比；主任务 scratch 24h 无成功 rollout。不能外推为通用加速比。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "We show that our prior is 33x more sample-efficient than RL training from scratch, even when provided with dense, multi-stage rewards.", "stance": "supports", "reason": "摘要直接陈述样本效率倍数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "Scratch (dense reward) requires over 100 hours to reach near-perfect success, while Play2Perfect reaches the same success rate in only 4 hours, yielding a 33× speed-up.", "stance": "supports", "reason": "Fixtured 任务 wall-clock 对比。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "both scratch baselines produce no successful rollouts even after 24 hours", "stance": "context", "reason": "主任务 scratch 失败，限定对比范围。"}]
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
origin_proposal_id: "proposal_757024799e5bc3c541292d99"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_757024799e5bc3c541292d99.md"
origin_candidate_sha256: "d0e5fb70314443e119dd38ed6c3f9cd05006574f4f5d6b99fbef5d3f9047d764"
memory_schema_version: 1
---

# Play2Perfect 在简化插入任务中的训练效率

在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward scratch 需要超过 100 小时达到接近满成功率，而 Play2Perfect 使用 play 先验和 sparse assembly reward 约 4 小时达到相同水平；论文将其概括为 33× speed-up/sample-efficiency improvement。

这个 33× 数字只对应上述简化任务的 wall-clock 对比。四项主要装配任务中，两种 scratch baseline 在 24 小时后都没有成功 rollout，因而没有形成可直接计算的通用倍数；不应把 33× 外推为所有装配任务或所有硬件的加速比。
