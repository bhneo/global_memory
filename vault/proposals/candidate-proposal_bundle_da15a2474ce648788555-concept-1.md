---
id: "concept_geometry_grounded_proprioception"
type: "concept"
status: "proposal"
title: "几何落地的本体感觉视觉融合"
created_at: "2026-07-19T12:19:14+08:00"
updated_at: "2026-07-19T12:19:14+08:00"
aliases: ["geometry-grounded proprioception", "proprioception-vision geometric grounding", "GeoProp"]
tags: []
domains: ["embodied-ai", "robot-perception", "proprioception", "visual-grounding"]
confidence: "medium"
source_ids: ["source_b1f4ea371eb10f3bc7a0f532"]
relations: [{"type": "derived_from", "target_id": "source_b1f4ea371eb10f3bc7a0f532", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "GeoProp 为通用 VLA 中常被当作独立向量的本体状态提供显式 3D 到 2D 对齐机制，并在 Diffusion Policy 与 π0 两类架构上测试。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "该对齐依赖已知相机内外参且只投影末端位置；跨相机、灵巧手和全身本体的直接可移植性因此受约束。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "GeoProp 的 predictive kinematic sampling 使用局部运动前视补充当前状态，但它预测的是短时投影位置，不等同于完整未来状态或世界动力学预测。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_b1f4ea371eb10f3bc7a0f532"
uncertainty: "方法在相机标定漂移、投影点被遮挡、急剧转向和接触切换时可能退化；单固定主相机实验不足以证明多视角与移动相机泛化。"
---

# 几何落地的本体感觉视觉融合

把末端位姿投影到图像特征平面，在共定位视觉 token 上采样并注入本体状态，同时用近期运动预测短时前视坐标，使机器人运动学与场景语义形成显式对应。
