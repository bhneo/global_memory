---
id: "concept_generalist_cross_embodiment_vla"
type: "concept"
status: "working"
title: "跨本体通用 VLA 策略"
created_at: "2026-07-19T03:01:52+08:00"
updated_at: "2026-07-19T03:05:59+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "cross-embodiment", "humanoid"]
confidence: "medium"
source_ids: ["source_34d6513b0522739d0b25e303"]
relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "跨本体通用策略需要处理共享表征与本体专属控制之间的对齐。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
uncertainty: "通用性取决于训练数据、动作空间和具体部署支持，不能从项目定位推出任意机器人上的零样本泛化。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:05:59+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_b42edda3bcd8367515cd"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-concept-1.md"
origin_candidate_sha256: "53554fe46394c350e9f4d04c35326fd3a8a97dec6ff9e54c60121411cfe001df"
memory_schema_version: 2
last_consolidation_id: "consolidation_293f11cedb4d9003a326fffc"
---

# 跨本体通用 VLA 策略

以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。
