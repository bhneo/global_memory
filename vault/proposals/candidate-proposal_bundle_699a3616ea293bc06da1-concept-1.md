---
id: "concept_e41100353a87ecb775dd5c71"
type: "concept"
status: "proposal"
title: "局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state"
created_at: "2026-07-27T15:07:14+08:00"
updated_at: "2026-07-27T15:41:39+08:00"
aliases: ["非平衡局部视界热力学", "non-equilibrium local-horizon thermodynamics"]
tags: []
domains: ["gravity", "thermodynamics", "non-equilibrium"]
confidence: "high"
source_ids: ["source_4be2cb176dad6fdd8673bd31", "source_bd59f7e9cadcd7af4910d1e9", "source_086150581c4c39aee0813d57"]
relations: [{"type": "derived_from", "target_id": "source_4be2cb176dad6fdd8673bd31", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_7960d38d3965156bf98d11b2", "reason": "两者都以局部视界和熵能关系处理引力；Jacobson 是带 Clausius 前提的场方程导出，既有概念是 on-shell 作用量重释。", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_086150581c4c39aee0813d57"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_fdab66c14e1214c1e3d543b7"], "importance": "high", "changed_belief": "我会把高曲率或修正熵下的局部热力学写成可能含内部熵产生的非平衡闭合，而不是将 dS=dQ/T 机械外推。", "surprising": "", "connections": [{"shared_mechanism": "两者都以局部加速视界的热流、Unruh 温度和熵变约束引力方程。", "boundary": "本文具体处理多项式 Ricci-scalar 熵修正，并依赖熵平衡和守恒条件。", "difference": "原始 Jacobson 论证使用面积熵和平衡 Clausius 关系；本文加入 bulk/shear viscosity 型内部熵产生。"}], "open_questions": ["更一般的高阶曲率熵泛函需要哪些非平衡变量，才能维持局部能量守恒？"]}
proposed_status: "working"
---

# 局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state

在假定视界熵与面积成正比、并要求每个时空点的所有局部 Rindler 因果视界均满足 deltaQ=T dS（deltaQ 为加速观察者所见能量通量，T 为 Unruh 温度）时，Jacobson 将 Einstein 方程导出为状态方程。该论证受热力学和局部视界假设约束，未确定引力微观自由度，也不支持把场方程视作无前提地由热力学推出。

## 新增来源材料

- `source_bd59f7e9cadcd7af4910d1e9`：将局部 Clausius 关系推广到高阶曲率引力时，需要熵密度对近似局部 Killing 向量具有 Noether-charge 型依赖，并满足视界切片与可积性限制；该路线可约束由度规和 Riemann 张量代数构成的拉格朗日量，但似乎不自然容纳曲率导数项。

## 新增来源材料

- `source_086150581c4c39aee0813d57`：当局部视界熵含 Ricci-scalar 曲率修正时，平衡 Clausius 关系须扩展为 dS=dQ/T+dSi，其中 dSi 是由能量动量守恒约束的 bulk-viscosity 型内部熵产生；纯 Einstein 情形也可在允许视界 shear viscosity 时纳入熵产生。该非平衡形式不自动适用于任意高阶曲率熵泛函。
