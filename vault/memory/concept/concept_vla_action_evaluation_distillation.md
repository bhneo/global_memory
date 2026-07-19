---
id: "concept_vla_action_evaluation_distillation"
type: "concept"
status: "working"
title: "VLA 动作评估蒸馏"
created_at: "2026-07-19T03:03:50+08:00"
updated_at: "2026-07-19T12:20:27+08:00"
aliases: ["VLA action evaluation distillation", "action value distillation", "SVA"]
tags: []
domains: ["embodied-ai", "vla", "reinforcement-learning", "planning", "value-function"]
confidence: "medium"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_world_model_action_value", "reason": "该方法用仿真回报蒸馏出的动作价值模型把长期后果预测连接到动作选择。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都关注预测结果对策略评价的价值，但这里评价对象是冻结 VLA 产生的候选动作。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "评估器与生成器解耦，目标是在不后训练 VLA 主干的情况下保留通用能力。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
uncertainty: "树搜索知识来自仿真，Q 评估器的 Sim-to-Real 外推和候选覆盖仍是限制。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 5
last_consolidated_at: "2026-07-19T12:20:27+08:00"
last_verified_at: "2026-07-19T03:26:34+08:00"
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_ec30b88a6f8a07464311"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_ec30b88a6f8a07464311-concept-1.md"
origin_candidate_sha256: "3542f12e5f8958f0080a14086281120220baef7fb31311e93839bd7346840cf1"
memory_schema_version: 2
last_consolidation_id: "consolidation_cccb9426298d45be4e3b42a1"
evidence: []
change_history: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "new_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ff90ad99bd47043e812cce9e", "trigger_source": "source_ff90ad99bd47043e812cce9e", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "new_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ff90ad99bd47043e812cce9e", "trigger_source": "source_ff90ad99bd47043e812cce9e", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "new_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "changed_fields": ["aliases"], "reason": "compile bundle from source_ff90ad99bd47043e812cce9e", "trigger_source": "source_ff90ad99bd47043e812cce9e", "evidence_added": []}]
---

# VLA 动作评估蒸馏

保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。
