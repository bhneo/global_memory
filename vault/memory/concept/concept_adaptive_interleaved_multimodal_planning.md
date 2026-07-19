---
id: "concept_adaptive_interleaved_multimodal_planning"
type: "concept"
status: "working"
title: "自适应交错多模态规划"
created_at: "2026-07-19T12:18:13+08:00"
updated_at: "2026-07-19T12:20:05+08:00"
aliases: ["adaptive interleaved vision-language planning", "adaptive multimodal planning", "APIVOT"]
tags: []
domains: ["embodied-ai", "robot-planning", "multimodal-reasoning", "long-horizon"]
confidence: "medium"
source_ids: ["source_4ac7cf9f4fce43551683a04b"]
relations: [{"type": "derived_from", "target_id": "source_4ac7cf9f4fce43551683a04b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都区分低频语义结构与几何/动作执行；APIVOT 在单个规划轨迹内交错模态，DSWAM 则在规划器与 WAM 执行器之间分工。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "tension_internal_reasoning_external_skills", "reason": "APIVOT 把几何验证内化为模型的视觉思维，明确落在该 tension 的内部推理一侧，并保留与外部验证式技能图比较的研究边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_4ac7cf9f4fce43551683a04b"
uncertainty: "证据来自 KitchenWorlds 仿真；OOD 物体更密集时下降较大，真实几何与外观泛化尚未验证。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:05+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_5c56317b0a0df19a19fc"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_5c56317b0a0df19a19fc-concept-1.md"
origin_candidate_sha256: "385eec27b29bf7abb766c2f77ca4e6b6ceb82d911b0f0d4479715e2f44b05056"
memory_schema_version: 2
last_consolidation_id: "consolidation_71d56da06bb0a2baab3d8b5c"
---

# 自适应交错多模态规划

长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。
