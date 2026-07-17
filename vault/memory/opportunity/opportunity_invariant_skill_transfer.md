---
id: "opportunity_invariant_skill_transfer"
type: "opportunity"
status: "working"
title: "以不变量约束技能跨形态迁移"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T18:36:06+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_941321d95232028c233c9433", "source_6ae6c4bef52010f96ddb3dbf"]
relations: [{"type": "derived_from", "target_id": "source_941321d95232028c233c9433", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "derived_from", "target_id": "source_6ae6c4bef52010f96ddb3dbf", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "applied_in", "target_id": "project_embodied_agent_learning_candidate", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "depends_on", "target_id": "hypothesis_invariants_skill_transfer", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
memory_tier: "working"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 3
last_consolidated_at: "2026-07-17T18:36:06+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "opportunity-62"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-opportunity_invariant_skill_transfer.md"
origin_candidate_sha256: "5dadaa7f722d4a7d557755ce661a3d493d9c536305e66ecb21d8973ed739d9ad"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_c5cc3e28bc3350c438ba174e"
---

# 以不变量约束技能跨形态迁移

探索用几何不变量和等变表示减少不同机器人形态之间的技能重学成本；先作为低置信度机会而非架构决策。
