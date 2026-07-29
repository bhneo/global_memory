---
id: "concept_4b29abb8c07d6365b04b97c3"
type: "concept"
status: "working"
title: "面向策略学习的可运行交互孪生"
created_at: "2026-07-23T18:06:36+08:00"
updated_at: "2026-07-26T12:33:33+08:00"
aliases: ["Runnable Interaction Twin", "Simulatable Episodic Twin", "可模拟情节孪生"]
tags: []
domains: ["real2sim", "robotics", "world-modeling"]
confidence: "medium"
source_ids: ["source_4ceaa5243dd0d99116547dda"]
relations: [{"type": "derived_from", "target_id": "source_4ceaa5243dd0d99116547dda", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_4ceaa5243dd0d99116547dda"
reflection_context: {"reflection_ids": ["reflection_c8a3c97a77f64d38720a8539"], "importance": "high", "changed_belief": "此前容易把 Real2Sim 当成资产重建问题；该来源表明，面向机器人下游使用时，状态、物理和交互轨迹的可执行组合才是关键交付物。", "surprising": "", "connections": [], "open_questions": ["在不同材质、接触和传感噪声条件下，怎样衡量 episodic twin 对真实闭环策略评测的保真度？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:33+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_a9bf9e1ceeb1499c44c2"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_a9bf9e1ceeb1499c44c2-concept-1.md"
origin_candidate_sha256: "a653682330de05b7c5dbca0278f06ec582f184fde76d4563c7fee81edd2e13ff"
memory_schema_version: 2
last_consolidation_id: "consolidation_af554051e4bddfc5629cf5cd"
---

# 面向策略学习的可运行交互孪生

将真实对象—机器人交互记录组织为可在物理仿真器中重放的 episodic twin：它需要联合保留场景几何、对象状态、推断的物理参数、参与者、相机、位姿和轨迹，使该记录可用于下游策略学习或评测。该概念不保证视觉重建、物理参数估计或跨场景泛化已经充分准确。
