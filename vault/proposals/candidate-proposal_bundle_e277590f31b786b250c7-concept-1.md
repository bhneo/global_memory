---
id: "concept_1bc84fc99981d367b712d161"
type: "concept"
status: "proposal"
title: "单次前向动作条件世界模型的 rollout 吞吐量接口"
created_at: "2026-07-24T18:06:01+08:00"
updated_at: "2026-07-24T18:07:12+08:00"
aliases: ["Single-Pass Drifting World Model", "DriftWorld", "单次前向漂移世界模型"]
tags: []
domains: ["world-modeling", "robot-planning"]
confidence: "medium"
source_ids: ["source_ce00fba8d7127c890fdcc46e"]
relations: [{"type": "derived_from", "target_id": "source_ce00fba8d7127c890fdcc46e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都把预测模型置于动作决策接口中；本概念聚焦候选 rollout 的生成吞吐量，而既有概念聚焦高频动作与低频语义规划的职责分离。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "两者都把预测模型置于动作决策接口中；本概念聚焦候选 rollout 的生成吞吐量，而既有概念聚焦高频动作与低频语义规划的职责分离。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_ce00fba8d7127c890fdcc46e"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_754995a5fd604aa50ec30b29"], "importance": "high", "changed_belief": "世界模型速度不只是工程优化；当采样速度限制候选动作数量时，生成吞吐量会改变规划和离线策略排序是否可实际使用。", "surprising": "", "connections": [], "open_questions": ["单步高速生成在长时程接触、遮挡和分布外动作下的误差累积，何时会抵消其增加候选 rollout 数量带来的决策收益？"]}
proposed_status: "working"
---

# 单次前向动作条件世界模型的 rollout 吞吐量接口

动作条件世界模型若在训练中学习从先验到未来帧的漂移映射，可在推理时以单次前向生成候选动作序列的 rollout，从而为在线动作搜索或离线策略排序释放采样预算；其控制价值仍需分别验证预测保真、长时程误差和候选排序与真实结果的一致性。
