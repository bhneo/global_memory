---
id: "concept_bb69fa188e0417143c3277cf"
type: "concept"
status: "proposal"
title: "视觉—触觉 simulation-based 位姿后验用于插入 / visuo-tactile simulation-based pose posterior for insertion"
created_at: "2026-07-27T17:24:09+08:00"
updated_at: "2026-07-27T17:24:09+08:00"
aliases: ["BayesContact", "视觉触觉位姿后验", "visuo-tactile pose posterior"]
tags: []
domains: ["robotics", "tactile-sensing", "bayesian-inference"]
confidence: "medium"
source_ids: ["source_4757ec1a2e8a0b678a350ee1"]
relations: [{"type": "derived_from", "target_id": "source_4757ec1a2e8a0b678a350ee1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4757ec1a2e8a0b678a350ee1"
reflection_context: {"reflection_ids": ["reflection_438aaa4e8fa10fc299c05d87"], "importance": "high", "changed_belief": "我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。", "surprising": "", "connections": [{"shared_mechanism": "两者都用视觉和接触信息缩小接触操作中的状态不确定性。", "boundary": "本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。", "difference": "深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。"}], "open_questions": ["接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？"]}
---

# 视觉—触觉 simulation-based 位姿后验用于插入 / visuo-tactile simulation-based pose posterior for insertion

在 peg-in-hole 插入中，可用粒子表示物体位姿 belief，并以深度观测和由力/力矩导出的接触证据通过仿真前向模型进行 simulation-based 更新；该方法输出可随接触更新的后验而非单点位姿。其有效性依赖接触与传感仿真的模型保真度及论文的任务设置，未保证对任意几何、摩擦或环境零样本泛化。
