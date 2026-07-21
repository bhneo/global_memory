---
id: "concept_2d8e08b8d8ace05431e064a0"
type: "concept"
status: "proposal"
title: "接触中心的混合预测控制"
created_at: "2026-07-20T12:39:23+08:00"
updated_at: "2026-07-20T12:39:23+08:00"
aliases: ["Contact-centric hybrid predictive control", "TACTIC", "whole-arm contact MPC"]
tags: []
domains: ["embodied-ai", "tactile-control", "whole-arm-manipulation", "mpc"]
confidence: "high"
source_ids: ["source_e8cc1290fdb80e80f77ba2c2"]
relations: [{"type": "derived_from", "target_id": "source_e8cc1290fdb80e80f77ba2c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "二者都分开处理未来接触预测与快速触觉修正；TACTIC 采用混合 MPC，后者采用分层神经控制。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_e8cc1290fdb80e80f77ba2c2"
reflection_context: {"reflection_ids": ["reflection_4b63a8834e11b28db3cf2fdc"], "importance": "high", "changed_belief": "此前触觉控制容易被描述为学习一个 visuotactile policy；该工作提示，在稀疏多接触数据下，可靠控制还需要把分析运动学用于可行性，把学习模型用于接触形成与断裂，并在采样阶段主动偏向能调节接触力的方向。", "surprising": "接触 Jacobian 不只是 cost 项，而被直接用于塑形每个 MPC step 的动作扰动，使探索及时对当前接触法向敏感。", "connections": [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉既用于预测未来接触，也用于即时动作修正。", "boundary": "TACTIC 不提供形式安全保证，真实实验使用 mannequin 和 custom exoskeleton 数据；面向真人护理仍需舒适性、安全栈与受试者验证。", "difference": "多时间尺度触觉世界模型强调分层神经控制回路；TACTIC 用 sampling-based MPC、contact Jacobian 和 learned latent dynamics 形成显式混合规划器。"}], "open_questions": ["接触形成/断裂不确定性如何传播到 MPC 风险，而不只以平均预测力进入 cost？"]}
---

# 接触中心的混合预测控制

把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics 预测接触形成与力演化。它降低稀疏多接触数据下的物理不一致，但不构成形式安全保证。
