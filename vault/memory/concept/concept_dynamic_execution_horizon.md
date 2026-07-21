---
id: "concept_dynamic_execution_horizon"
type: "concept"
status: "working"
title: "动态动作块执行时域"
created_at: "2026-07-19T12:18:42+08:00"
updated_at: "2026-07-20T13:37:38+08:00"
aliases: ["dynamic execution horizon", "Dynamic Execution Horizon Prediction", "DEHP"]
tags: []
domains: ["embodied-ai", "robot-control", "action-chunking", "reinforcement-learning"]
confidence: "medium"
source_ids: ["source_531bafa56ff63468797ac69e"]
relations: [{"type": "derived_from", "target_id": "source_531bafa56ff63468797ac69e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "part_of", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "动作块执行长度、重查询时机与时延补偿共同属于从策略预测到实际命令的部署调度层。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_vla_action_cache_refinement", "reason": "两者都在不改生成主干的情况下优化动作块推理；缓存方法复用生成中间态，DEHP 调整已生成动作块的执行前缀。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_531bafa56ff63468797ac69e"
uncertainty: "受控实验主要使用 state-based Diffusion Policy；方法声称可黑盒扩展到图像策略，但该扩展尚未由本文实验证实，且能力上限仍由冻结基础策略决定。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 3
last_consolidated_at: "2026-07-20T13:37:38+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_a065541b84dd5bb41857"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_a065541b84dd5bb41857-concept-1.md"
origin_candidate_sha256: "6d4704c2f91d802bd993cf84ef9865a56e5b13bee1484bf013c3b87d7e46e9d8"
memory_schema_version: 2
last_consolidation_id: "consolidation_bb31bf4323ee87ce4298c93c"
---

# 动态动作块执行时域

在保持动作块生成策略冻结的条件下，按当前观测和预测动作块动态决定执行多少步再重规划：自由空间运动使用较长前缀，精细对齐与接触阶段缩短前缀以提高反应性。
