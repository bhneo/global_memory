---
id: "experiment_dataset_trajectory_coverage"
type: "experiment"
status: "working"
title: "比较数据集覆盖与真实部署轨迹覆盖"
created_at: "2026-07-16T16:30:21+08:00"
updated_at: "2026-07-17T18:36:02+08:00"
aliases: []
tags: ["m6-distillation"]
domains: []
confidence: "unknown"
source_ids: ["source_9d39636775b188c87d6a001f", "source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由当前语料蒸馏为待审知识对象", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "applied_in", "target_id": "project_embodied_agent_learning_candidate", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}, {"type": "tested_by", "target_id": "hypothesis_ergodicity_offline_coverage", "reason": "M6 人工可审阅结构连接；不得仅凭关键词确认", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
change_reason: "M6 controlled corpus distillation; requires human review"
memory_tier: "working"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 3
last_consolidated_at: "2026-07-17T18:36:02+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "experiment-60"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-experiment_dataset_trajectory_coverage.md"
origin_candidate_sha256: "d5d0bc86193cad975fdb90d2834e75b54e90fcc06fbe893a8cbdf33a69606e2a"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_c9419cc0eada52692d212290"
---

# 比较数据集覆盖与真实部署轨迹覆盖

记录单个 Agent 的时间轨迹、不可逆失败与恢复，比较其与离线数据集群体覆盖指标的偏差。
