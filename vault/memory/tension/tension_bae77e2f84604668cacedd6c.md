---
id: "tension_bae77e2f84604668cacedd6c"
type: "tension"
status: "working"
title: "世界预测可解释性与动作对齐安全之间的张力"
created_at: "2026-07-23T18:07:07+08:00"
updated_at: "2026-08-02T19:55:50+08:00"
aliases: ["World-Action Alignment Tension", "BadWAM", "世界动作对齐张力"]
tags: []
domains: ["world-action-model", "robot-safety"]
confidence: "medium"
source_ids: ["source_c2d7b53bd1c40ed0af8ea5cb"]
relations: [{"type": "derived_from", "target_id": "source_c2d7b53bd1c40ed0af8ea5cb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_action_centered_joint_world_action_model", "reason": "两者均涉及动作与未来表征的联合输出；该张力指出联合输出仍需针对二者对齐进行独立验收。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_c2d7b53bd1c40ed0af8ea5cb"
reflection_context: {"reflection_ids": ["reflection_dc9e5944bbe8d789e0935906"], "importance": "high", "changed_belief": "世界动作模型的预测质量与闭环动作正确性必须分别验证；未来画面未明显漂移并不蕴含动作仍与该未来一致。", "surprising": "", "connections": [{"shared_mechanism": "两者都依赖未来表征与动作输出的联合建模。", "boundary": "该连接仅说明联合建模存在需要验证的接口，不说明所有世界动作模型或所有扰动都会发生同类攻击。", "difference": "既有动作中心联合世界—动作模型描述生成架构；BadWAM 聚焦该架构中想象与执行可被脱钩的安全失败模式。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 2
last_consolidated_at: "2026-08-02T19:55:50+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_05dba53c3c9f85990185"
origin_item_id: "tension-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_05dba53c3c9f85990185-tension-1.md"
origin_candidate_sha256: "506193d5a44e7f2d2113fdac56bd0761d24afa094befe32152f230ce9ded790b"
memory_schema_version: 2
last_consolidation_id: "consolidation_9a7d4ecb39674e4a53ad4fff"
---

# 世界预测可解释性与动作对齐安全之间的张力

世界动作模型可用预测未来作为动作后果的可解释表示，但视觉扰动可能使预测未来保持表面合理而动作输出偏离该未来并导致任务失败。因此，未来预测质量不能单独充当动作安全或闭环正确性的充分验收条件。
