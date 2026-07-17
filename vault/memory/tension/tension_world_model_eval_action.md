---
id: "tension_world_model_eval_action"
type: "tension"
status: "trusted"
title: "更好的世界模型评价 vs 直接优化动作结果"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T22:40:14+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
left_view: "改进世界模型评价"
right_view: "直接优化真实动作结果"
unresolved: "评价与动作收益的稳定相关性"
validation_method: "跨任务前瞻相关性与干预实验"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 7
last_consolidated_at: "2026-07-17T22:40:14+08:00"
last_verified_at: null
trust_score: 58
trust_reasons: ["valid consolidation receipt matches current object"]
promotion_history: [{"promotion_id": "promotion_6e5021a695be419135d4f1e6", "object_id": "tension_world_model_eval_action", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "tension is durable and source-linked"], "failed_conditions": [], "supporting_sources": ["source_2d4f3a7d3525782c8ff503ee"], "contradictions": [], "promoted_at": "2026-07-17T12:05:07+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "tension-45"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-tension_world_model_eval_action.md"
origin_candidate_sha256: "f9842dd588e05f7d45a20033b0c7d7c5359a41f2d0c4a117918327555539bf87"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_7232c1c7516f64452c851379"
needs_policy_requalification: false
trust_policy_version: "trusted-promotion-v3-receipt-v2"
last_policy_qualified_at: "2026-07-17T18:40:55+08:00"
last_valid_receipt_id: null
policy_requalification_failed_conditions: []
---

# 更好的世界模型评价 vs 直接优化动作结果

代理评价可降低真实试验成本，但评价与动作收益可能脱钩；直接优化动作又可能缺少可诊断中间信号。
