---
id: "concept_4b29abb8c07d6365b04b97c3"
type: "concept"
status: "proposal"
title: "面向策略学习的可运行交互孪生"
created_at: "2026-07-23T18:06:36+08:00"
updated_at: "2026-07-23T18:06:36+08:00"
aliases: ["Runnable Interaction Twin", "Simulatable Episodic Twin", "可模拟情节孪生"]
tags: []
domains: ["real2sim", "robotics", "world-modeling"]
confidence: "medium"
source_ids: ["source_4ceaa5243dd0d99116547dda"]
relations: [{"type": "derived_from", "target_id": "source_4ceaa5243dd0d99116547dda", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4ceaa5243dd0d99116547dda"
reflection_context: {"reflection_ids": ["reflection_c8a3c97a77f64d38720a8539"], "importance": "high", "changed_belief": "此前容易把 Real2Sim 当成资产重建问题；该来源表明，面向机器人下游使用时，状态、物理和交互轨迹的可执行组合才是关键交付物。", "surprising": "", "connections": [], "open_questions": ["在不同材质、接触和传感噪声条件下，怎样衡量 episodic twin 对真实闭环策略评测的保真度？"]}
---

# 面向策略学习的可运行交互孪生

将真实对象—机器人交互记录组织为可在物理仿真器中重放的 episodic twin：它需要联合保留场景几何、对象状态、推断的物理参数、参与者、相机、位姿和轨迹，使该记录可用于下游策略学习或评测。该概念不保证视觉重建、物理参数估计或跨场景泛化已经充分准确。
