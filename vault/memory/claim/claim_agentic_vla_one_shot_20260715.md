---
id: "claim_agentic_vla_one_shot_20260715"
type: "claim"
status: "working"
title: "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: []
tags: ["vla", "one-shot", "libero"]
domains: ["robot-learning"]
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["每任务 1 demo SFT 预训练", "LIBERO 四套件"]
uncertainty: "摘要 +28.5% 与 Table 2 +26.9% 不一致，批准时以 Table 2 为准。"
evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7-8 页 Table 2", "excerpt": "Agentic-VLA 70.5 ... OpenVLA-OFT 43.6 ... Δ vs. SFT +26.9", "stance": "supports", "reason": "Table 2 one-shot 对比。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Section 4.3", "excerpt": "only a single demonstration per task is available for SFT pre-training", "stance": "context", "reason": "one-shot 协议。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "+28.5% in 1-shot learning", "stance": "context", "reason": "与 Table 2 数字差异，待核对。"}]
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
origin_proposal_id: "proposal_ed15e3a6bc9d3a320d6ce246"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_ed15e3a6bc9d3a320d6ce246.md"
origin_candidate_sha256: "f969f6b79b1e9749ccb64e7842db6338815162da3433ea7950efdf382495b19c"
memory_schema_version: 1
---

# Agentic-VLA 的 one-shot 结果

在每个任务仅使用一条 demonstration 做 SFT pre-training 的设定下，Agentic-VLA 在 LIBERO 四套件上的平均成功率为 70.5%，OpenVLA-OFT 为 43.6%，Table 2 给出的差值是 26.9 个百分点；相对 EVOLVE-VLA 的 61.3% 提高 9.2 个百分点。

论文摘要同时写作 `+28.5% in 1-shot learning`，与 Table 2 的 26.9 个百分点不一致。当前主张采用可直接复算的 Table 2 数字，并保留摘要差异等待作者版本更新或进一步解释。
