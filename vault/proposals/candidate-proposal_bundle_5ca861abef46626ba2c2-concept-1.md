---
id: "concept_474b5f9742996e9fc68609b6"
type: "concept"
status: "proposal"
title: "部署可用的机器人分解式视觉动作接口 / Deployment-available robot-factored visual action interface"
created_at: "2026-07-28T18:36:05+08:00"
updated_at: "2026-07-28T18:36:05+08:00"
aliases: ["Robot-Factored World Models", "robot-factored visual world-model interface", "nominal trajectory rendering", "机器人分解式世界模型接口"]
tags: []
domains: ["robotics", "world-models", "action-representation", "embodied-ai"]
confidence: "high"
source_ids: ["source_e81925f355a0e0d30a13439a"]
relations: [{"type": "derived_from", "target_id": "source_e81925f355a0e0d30a13439a", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "视觉动作接口隔离了动作实现与场景响应，但其真实价值仍需通过动作选择、规划和失败恢复等闭环指标验证，而不能只依赖像素相似度。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_e81925f355a0e0d30a13439a"
reflection_context: {"reflection_ids": ["reflection_52b043d688d780a74db9a1c7"], "importance": "high", "changed_belief": "此前容易把动作条件世界模型的改进归因于更强的视频骨干；本文的同骨干比较表明，动作表示本身可以决定模型是否必须同时学习本体特定的动作实现和场景动力学。", "surprising": "名义轨迹并不需要预知真实接触结果；即便存在抓取失败、滑移等偏差，部署时可计算的机器人侧渲染仍优于向量或位姿注入。", "connections": [{"shared_mechanism": "都把世界模型用于动作条件的未来预测。", "boundary": "现有 action-centered joint world-action model 强调联合预测，而本文贡献是把机器人侧动作实现显式外置为可渲染接口。", "difference": "前者是预测架构概念，后者是部署可用的条件接口，不应合并。"}], "open_questions": ["当真实系统只有部分相机标定、柔性机构或接触丰富的工具时，名义渲染接口的收益会在何处失效？"]}
---

# 部署可用的机器人分解式视觉动作接口 / Deployment-available robot-factored visual action interface

先把控制命令经机器人控制器或运动学展开为部署时可计算的名义轨迹，再用已知 URDF 与相机标定渲染机器人网格 RGB，并以末端执行器深度补充空间消歧；视频世界模型据此预测场景响应，而无需同时重新学习本体特定的动作实现。论文在 DROID 与 RoboCasa 的同骨干比较中报告该接口优于向量或位姿条件，并显示名义渲染加深度的增益；适用边界包括需要可靠的机器人模型和标定、动态相机场景信息可能不完整，以及成功轨迹不足以覆盖滑移、接触误差和失败。
