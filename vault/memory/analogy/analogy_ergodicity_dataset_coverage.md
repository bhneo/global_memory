---
id: "analogy_ergodicity_dataset_coverage"
type: "analogy"
status: "trusted"
title: "遍历性 ↔ 离线数据对部署轨迹的覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T12:01:36+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "analogous_to", "target_id": "concept_ergodicity", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "analogous_to", "target_id": "concept_embodied_data_loop", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
source_domain: "stochastic processes"
target_domain: "offline embodied learning"
shared_structure: "ensemble coverage may differ from temporal trajectory coverage"
where_it_breaks: "部署策略和环境会共同改变分布"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "promotion-policy"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-17T12:01:10+08:00"
last_verified_at: null
trust_score: 66
trust_reasons: ["completed consolidation review", "analogy records shared structure and break boundary"]
promotion_history: [{"promotion_id": "promotion_ea72aafda1f82ee4033f8abb", "object_id": "analogy_ergodicity_dataset_coverage", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "analogy records shared structure and break boundary"], "failed_conditions": [], "supporting_sources": ["source_9d39636775b188c87d6a001f"], "contradictions": [], "promoted_at": "2026-07-17T12:01:36+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "analogy-55"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-analogy_ergodicity_dataset_coverage.md"
origin_candidate_sha256: "9e909acf5e852cc0c6be3eaba40416d6f8b37bc609d50970b39d4486bbe71004"
memory_schema_version: 1
---

# 遍历性 ↔ 离线数据对部署轨迹的覆盖

共同结构是群体样本与单个主体时间经历可能不等价；失效边界是 Agent 环境分布并非严格物理遍历过程。
