---
id: "concept_predictive_vla_deployment"
type: "concept"
status: "working"
title: "面向真实部署的预测式 VLA"
created_at: "2026-07-19T02:52:30+08:00"
updated_at: "2026-07-19T12:20:20+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "world-model", "robot-learning"]
confidence: "medium"
source_ids: ["source_233c4bef3a727389ddf81ae2"]
relations: [{"type": "derived_from", "target_id": "source_233c4bef3a727389ddf81ae2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都利用对未来状态或结果的预测，但这里预测被用作 VLA 训练目标而不只是离线评测器。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_embodied_data_loop", "reason": "该方案把跨本体数据规模、动作空间覆盖和预测训练目标共同视为部署能力来源。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}]
change_reason: "compile bundle from source_233c4bef3a727389ddf81ae2"
uncertainty: "未来预测在该工作中是代理训练目标，不等同于完整的环境动力学世界模型。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56terra-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56terra-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-19T12:20:20+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_7e605b3d52b545aadc55"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_7e605b3d52b545aadc55-concept-1.md"
origin_candidate_sha256: "bed1fcdf34d7427958dbeb57c3a6f527d99366aba1947627ad0cb997815c98dd"
memory_schema_version: 2
last_consolidation_id: "consolidation_addb5624a16aa8aa847befd7"
---

# 面向真实部署的预测式 VLA

在 VLA 的视觉—语言—动作映射中加入未来状态或动作后果预测，使策略不仅响应当前观测，还能以语义和几何线索形成面向动态环境的预测表示。
