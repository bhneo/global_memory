---
id: "hypothesis_invariants_skill_transfer"
type: "hypothesis"
status: "working"
title: "显式不变量可能提高技能跨形态迁移"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T17:04:22+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "low"
source_ids: ["source_941321d95232028c233c9433", "source_6ae6c4bef52010f96ddb3dbf"]
relations: [{"type": "derived_from", "target_id": "source_941321d95232028c233c9433", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "derived_from", "target_id": "source_6ae6c4bef52010f96ddb3dbf", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_lie_group", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_parameter_symmetry", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
memory_tier: "working"
created_by: "m6-controlled-distillation-v1"
updated_by: "trusted-promotion-v3-receipt-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-17T15:24:08+08:00"
last_verified_at: null
trust_score: 66
trust_reasons: ["completed consolidation review", "hypothesis is durable and source-linked"]
promotion_history: [{"promotion_id": "promotion_41c03ff0b707f25af87c8ee2", "object_id": "hypothesis_invariants_skill_transfer", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "hypothesis is durable and source-linked"], "failed_conditions": [], "supporting_sources": ["source_941321d95232028c233c9433", "source_6ae6c4bef52010f96ddb3dbf"], "contradictions": [], "promoted_at": "2026-07-17T12:03:43+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "hypothesis-49"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-hypothesis_invariants_skill_transfer.md"
origin_candidate_sha256: "61eeff5045ad8e0b4473b459cca07856348a78bebc5085b92a45bbced57eb6af"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "hypothetical"
last_consolidation_id: "consolidation_626d41ac7a03dc811f708a45"
needs_revalidation: true
---

# 显式不变量可能提高技能跨形态迁移

将连续对称性和不变量用于技能表示，可能降低形态变化带来的重新学习成本；尚无当前语料中的直接实验支持。
