---
id: "tension_language_prior_action_control"
type: "tension"
status: "trusted"
title: "语言先验复用 vs 实时动作专用表示"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T22:40:13+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
relations: [{"type": "derived_from", "target_id": "source_f35b44d4bd383fb26ca49165", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
left_view: "复用语言/视觉预训练先验"
right_view: "使用动作专用连续表示"
unresolved: "接口和训练信号如何分工"
validation_method: "延迟、泛化、稳定性联合消融"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 7
last_consolidated_at: "2026-07-17T22:40:13+08:00"
last_verified_at: null
trust_score: 58
trust_reasons: ["valid consolidation receipt matches current object"]
promotion_history: [{"promotion_id": "promotion_85a481f26d392326fc196204", "object_id": "tension_language_prior_action_control", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "tension is durable and source-linked"], "failed_conditions": [], "supporting_sources": ["source_f35b44d4bd383fb26ca49165"], "contradictions": [], "promoted_at": "2026-07-17T12:04:58+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "tension-46"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-tension_language_prior_action_control.md"
origin_candidate_sha256: "3d675784ddc650eb43906213a83d0a415731b19651dbb13b2756ef6383fa373e"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_071780788c9802ca02fe0f93"
needs_policy_requalification: false
trust_policy_version: "trusted-promotion-v3-receipt-v2"
last_policy_qualified_at: "2026-07-17T18:40:41+08:00"
last_valid_receipt_id: null
policy_requalification_failed_conditions: []
---

# 语言先验复用 vs 实时动作专用表示

语言先验有助于泛化和任务理解，但连续控制需要低延迟、高带宽且具身化的动作表示。
