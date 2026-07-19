---
id: "concept_asymmetric_frozen_vla_harness"
type: "concept"
status: "working"
title: "冻结 VLA 的非对称技能编排"
created_at: "2026-07-19T12:18:32+08:00"
updated_at: "2026-07-19T12:20:06+08:00"
aliases: ["asymmetric frozen-VLA harness", "VLA-as-a-primitive", "Harness VLA"]
tags: []
domains: ["embodied-ai", "vla", "robot-agents", "long-horizon-manipulation"]
confidence: "medium"
source_ids: ["source_4bff03c9d5adb3463b34f947"]
relations: [{"type": "derived_from", "target_id": "source_4bff03c9d5adb3463b34f947", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都把长程任务外化为可审计原语组合；Harness VLA 特别保留一个冻结 VLA 作为接触原语，GaP 则执行更一般的类型化技能图。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该框架显示不必持续扩张技能库：可先固定小型原语集合，通过执行记忆学习调用范围，仅在重复组合暴露缺失抽象时再考虑新技能。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都采用非对称分工；Harness VLA 把接触控制交给 VLA、非接触结构交给代理，而 DSWAM 把高频动作交给 WAM、粗粒度分解交给规划器。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_4bff03c9d5adb3463b34f947"
uncertainty: "高层规划器与低层 VLA 仍是开放反馈环，且缺少联合奖励/偏好微调；拥挤长程场景的结构推理受图像描述能力限制。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:06+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_84924618ed7bb77a5704"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_84924618ed7bb77a5704-concept-1.md"
origin_candidate_sha256: "ca740123df7e1d552efc8343f658d1a9ead0389bf71134ba9696bb6be738e466"
memory_schema_version: 2
last_consolidation_id: "consolidation_314019a3a8e7261df3f7bd23"
---

# 冻结 VLA 的非对称技能编排

把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。
