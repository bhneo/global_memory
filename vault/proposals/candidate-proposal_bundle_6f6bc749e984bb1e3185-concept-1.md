---
id: "concept_e41100353a87ecb775dd5c71"
type: "concept"
status: "proposal"
title: "局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state"
created_at: "2026-07-27T15:07:14+08:00"
updated_at: "2026-07-27T15:07:14+08:00"
aliases: ["Jacobson Einstein equation of state", "局部 Rindler 视界 Clausius 推导", "local Rindler horizon thermodynamics"]
tags: []
domains: ["gravity", "thermodynamics", "general-relativity"]
confidence: "high"
source_ids: ["source_4be2cb176dad6fdd8673bd31"]
relations: [{"type": "derived_from", "target_id": "source_4be2cb176dad6fdd8673bd31", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_7960d38d3965156bf98d11b2", "reason": "两者都以局部视界和熵能关系处理引力；Jacobson 是带 Clausius 前提的场方程导出，既有概念是 on-shell 作用量重释。", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4be2cb176dad6fdd8673bd31"
reflection_context: {"reflection_ids": ["reflection_88da128593d6adeb3fda7549"], "importance": "high", "changed_belief": "我不再把 Einstein 方程是状态方程理解为免前提的证明，或理解为已决定引力的微观自由度。", "surprising": "", "connections": [{"shared_mechanism": "两者都以局部视界和熵--能量关系重释引力结构。", "boundary": "都依赖局部 Rindler 与熵、温度假设，未指定微观自由度。", "difference": "Jacobson 要求所有局部视界满足 Clausius 关系以导出场方程；既有概念处理作用量的 on-shell 重释。"}], "open_questions": ["面积熵比例与局部 Clausius 条件在高阶曲率引力或非平衡情形如何修改？"]}
---

# 局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state

在假定视界熵与面积成正比、并要求每个时空点的所有局部 Rindler 因果视界均满足 deltaQ=T dS（deltaQ 为加速观察者所见能量通量，T 为 Unruh 温度）时，Jacobson 将 Einstein 方程导出为状态方程。该论证受热力学和局部视界假设约束，未确定引力微观自由度，也不支持把场方程视作无前提地由热力学推出。
