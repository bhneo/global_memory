---
id: "concept_staged_cross_embodiment_alignment"
type: "concept"
status: "working"
title: "异构具身数据的分阶段对齐"
created_at: "2026-07-19T02:51:00+08:00"
updated_at: "2026-07-19T03:06:08+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "humanoid", "robot-learning"]
confidence: "medium"
source_ids: ["source_691f3acc1fe3382639690f59"]
relations: [{"type": "derived_from", "target_id": "source_691f3acc1fe3382639690f59", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "该方法把具身数据闭环进一步区分为通用表征数据与本体控制数据两个训练阶段。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "working"}]
change_reason: "compile bundle from source_691f3acc1fe3382639690f59"
uncertainty: "这是对 Ψ₀ 训练配方的概念归纳，尚未证明适用于所有机器人形态。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56terra-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56terra-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:06:08+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_1afd74377f054193ef53"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_1afd74377f054193ef53-concept-1.md"
origin_candidate_sha256: "3069c545e66450d2fe2367eb53178ba1ac408c003b62bbcd242646d2dd4c2549"
memory_schema_version: 2
last_consolidation_id: "consolidation_a40bad0b9df74250a25c9be3"
---

# 异构具身数据的分阶段对齐

把人类视频中的通用视觉—动作表征学习，与机器人本体专属的连续控制学习拆成不同阶段，以减少人类运动学和机器人运动学差异造成的负迁移。
