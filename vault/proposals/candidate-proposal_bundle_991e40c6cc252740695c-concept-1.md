---
id: "concept_59f92bcb786f695ddcd47f7f"
type: "concept"
status: "proposal"
title: "视频原生的光流动作接口"
created_at: "2026-07-20T12:32:57+08:00"
updated_at: "2026-07-20T12:33:53+08:00"
aliases: ["Video-native optical-flow action interface", "FlowWAM", "光流动作表示"]
tags: []
domains: ["embodied-ai", "world-action-model", "optical-flow", "action-representation"]
confidence: "high"
source_ids: ["source_ef80ef223077ef0855660839"]
relations: [{"type": "derived_from", "target_id": "source_ef80ef223077ef0855660839", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "二者都统一动作生成与未来状态建模；光流接口规定共享的运动表征，双系统 WAM 规定快慢推理分工。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "二者都统一动作生成与未来状态建模；光流接口规定共享的运动表征，双系统 WAM 规定快慢推理分工。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_ef80ef223077ef0855660839"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_a74b334857543499d8111c64"], "importance": "high", "changed_belief": "此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。", "surprising": "跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。", "connections": [{"shared_mechanism": "与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。", "boundary": "光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。", "difference": "双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。"}], "open_questions": ["在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？"]}
proposed_status: "working"
---

# 视频原生的光流动作接口

用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。
