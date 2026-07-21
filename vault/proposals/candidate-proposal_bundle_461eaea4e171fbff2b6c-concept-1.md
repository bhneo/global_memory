---
id: "concept_multitimescale_tactile_world_model"
type: "concept"
status: "proposal"
title: "多时间尺度触觉世界模型控制"
created_at: "2026-07-19T03:02:53+08:00"
updated_at: "2026-07-19T23:47:57+08:00"
aliases: ["multi-timescale tactile world model", "TouchWorld"]
tags: []
domains: ["embodied-ai", "vla", "world-model", "tactile"]
confidence: "medium"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "limits", "target_id": "concept_vla_action_cache_refinement", "reason": "接触状态快速变化时，历史动作即使视觉上下文相似也可能陈旧，高频触觉反馈构成动作缓存安全复用的边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
change_reason: "compile bundle from source_283911da72edc403d1b823fb"
change_type: "metadata_only"
reflection_context: {"reflection_ids": ["reflection_c5765c32f1c3dd7302da4906"], "importance": "weekly", "changed_belief": "此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。", "surprising": "触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。", "connections": [{"shared_mechanism": "都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分", "boundary": "连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务", "difference": "TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示"}], "open_questions": ["预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？"]}
proposed_status: "working"
---

# 多时间尺度触觉世界模型控制

把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。
