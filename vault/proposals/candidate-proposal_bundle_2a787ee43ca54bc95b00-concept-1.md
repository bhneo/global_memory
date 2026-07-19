---
id: "concept_multitimescale_tactile_world_model"
type: "concept"
status: "proposal"
title: "多时间尺度触觉世界模型控制"
created_at: "2026-07-19T03:02:53+08:00"
updated_at: "2026-07-19T03:02:53+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
confidence: "medium"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_283911da72edc403d1b823fb"
uncertainty: "架构和结果局限于论文中的六项长时程接触任务，触觉硬件与标注成本可能影响迁移。"
---

# 多时间尺度触觉世界模型控制

把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。
