---
id: "concept_sensor_conditional_expert_routing"
type: "concept"
status: "working"
title: "传感器条件化专家路由"
created_at: "2026-07-19T03:03:29+08:00"
updated_at: "2026-07-19T03:06:06+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "mixture-of-experts", "robustness"]
confidence: "medium"
source_ids: ["source_5d8306b5caf7371feeacbc09"]
relations: [{"type": "derived_from", "target_id": "source_5d8306b5caf7371feeacbc09", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它解决跨机器人形态和部署条件下传感器集合不一致这一通用 VLA 难题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_5d8306b5caf7371feeacbc09"
uncertainty: "论文实验主要以深度为辅助模态，不能直接推出任意传感器组合都能优雅退化。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:06:06+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_fd46bf9cd0ccdfd3bd16"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_fd46bf9cd0ccdfd3bd16-concept-1.md"
origin_candidate_sha256: "7387cbd951f7d0161607c61d5a92bfaa22172577086b63d6ac8e3a3ab721d3ba"
memory_schema_version: 2
last_consolidation_id: "consolidation_a21d90be87a4f7534493b359"
---

# 传感器条件化专家路由

根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。
