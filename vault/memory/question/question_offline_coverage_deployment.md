---
id: "question_offline_coverage_deployment"
type: "question"
status: "trusted"
title: "离线数据能否代表真实部署轨迹？"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T12:04:12+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "raises", "target_id": "concept_ergodicity", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "promotion-policy"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-17T12:01:11+08:00"
last_verified_at: null
trust_score: 66
trust_reasons: ["completed consolidation review", "question is durable and source-linked"]
promotion_history: [{"promotion_id": "promotion_44d85e02553bd9479da44313", "object_id": "question_offline_coverage_deployment", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "question is durable and source-linked"], "failed_conditions": [], "supporting_sources": ["source_9d39636775b188c87d6a001f"], "contradictions": [], "promoted_at": "2026-07-17T12:04:12+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "question-39"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-question_offline_coverage_deployment.md"
origin_candidate_sha256: "c849ae6cbd2ee5ec2dd255ec306021c2249790337323b7cd3beabe5f84882352"
memory_schema_version: 1
---

# 离线数据能否代表真实部署轨迹？

需要区分数据集群体分布与单个 Agent 随时间经历的状态、风险和不可逆失败。
