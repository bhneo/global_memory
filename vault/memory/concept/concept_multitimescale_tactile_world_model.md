---
id: "concept_multitimescale_tactile_world_model"
type: "concept"
status: "working"
title: "多时间尺度触觉世界模型控制"
created_at: "2026-07-19T03:02:53+08:00"
updated_at: "2026-07-20T13:37:50+08:00"
aliases: ["multi-timescale tactile world model", "TouchWorld"]
tags: []
domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
confidence: "medium"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_283911da72edc403d1b823fb"
uncertainty: "架构和结果局限于论文中的六项长时程接触任务，触觉硬件与标注成本可能影响迁移。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 7
last_consolidated_at: "2026-07-20T13:37:50+08:00"
last_verified_at: "2026-07-19T03:29:27+08:00"
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_2a787ee43ca54bc95b00"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2a787ee43ca54bc95b00-concept-1.md"
origin_candidate_sha256: "e6161d8a748e1a5dd54a5ac7254ede7a78d21d97fc25b7593f1b022e298b82fc"
memory_schema_version: 2
last_consolidation_id: "consolidation_4d1bad043262eae83c5c24a2"
evidence: []
change_history: [{"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["aliases"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": [], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}]
---

# 多时间尺度触觉世界模型控制

把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。
