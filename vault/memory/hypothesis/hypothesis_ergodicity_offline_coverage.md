---
id: "hypothesis_ergodicity_offline_coverage"
type: "hypothesis"
status: "trusted"
title: "遍历性指标可能预测离线数据对部署轨迹的覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T12:03:28+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "low"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "depends_on", "target_id": "concept_ergodicity", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "answers", "target_id": "question_offline_coverage_deployment", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
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
trust_reasons: ["completed consolidation review", "hypothesis is durable and source-linked"]
promotion_history: [{"promotion_id": "promotion_3d461f591b6ae98e993ba314", "object_id": "hypothesis_ergodicity_offline_coverage", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "hypothesis is durable and source-linked"], "failed_conditions": [], "supporting_sources": ["source_9d39636775b188c87d6a001f"], "contradictions": [], "promoted_at": "2026-07-17T12:03:28+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "hypothesis-48"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-hypothesis_ergodicity_offline_coverage.md"
origin_candidate_sha256: "0ef0cdf2f6e23e94ef8db8602835ca6f259480b6b63a929919ca06e8bda7ceac"
memory_schema_version: 1
---

# 遍历性指标可能预测离线数据对部署轨迹的覆盖

若任务具有强路径依赖和不可逆失败，群体分布覆盖可能高估单个 Agent 的时间轨迹覆盖；需要部署日志验证。
