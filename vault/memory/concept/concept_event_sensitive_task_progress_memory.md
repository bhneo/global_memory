---
id: "concept_event_sensitive_task_progress_memory"
type: "concept"
status: "working"
title: "事件敏感的任务进度记忆"
created_at: "2026-07-19T12:18:53+08:00"
updated_at: "2026-07-19T12:20:11+08:00"
aliases: ["event-sensitive task-progress memory", "Temporally Conditioned Memory-Fusion Policy", "TFP", "dynamics-aware belief tracking"]
tags: []
domains: ["embodied-ai", "vla", "robot-memory", "visuomotor-control"]
confidence: "medium"
source_ids: ["source_011483b15aae65e849a3772e"]
relations: [{"type": "derived_from", "target_id": "source_011483b15aae65e849a3772e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "DEHP 决定动作块何时重新查询，TFP 用真实经过时间和不规则查询间隔更新任务 belief；两者分别控制外部重规划节奏与内部记忆节奏。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都让快速事件响应与慢速上下文保持共存，但 TFP 跟踪视觉/本体任务进度，后者建模触觉预测与反应控制。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_011483b15aae65e849a3772e"
uncertainty: "循环全量微调代价高，最大实验需 4 张 H200 约 80 小时；真机验证限于桌面单臂，不能直接外推到移动、全身或灵巧手。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:11+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0cb43c03823e232015b6"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0cb43c03823e232015b6-concept-1.md"
origin_candidate_sha256: "67910fd4367e6ea78e0e0cd0582bcb31fe746f415845b0ba1568c82069ba2087"
memory_schema_version: 2
last_consolidation_id: "consolidation_08394fd84fe39072624a10ac"
---

# 事件敏感的任务进度记忆

用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。
