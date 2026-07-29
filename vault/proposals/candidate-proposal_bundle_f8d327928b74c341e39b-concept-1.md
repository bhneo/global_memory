---
id: "concept_e41100353a87ecb775dd5c71"
type: "concept"
status: "proposal"
title: "局部 Rindler Clausius 关系中的 Einstein 状态方程 / Einstein equation of state from local-Rindler Clausius relations"
created_at: "2026-07-27T15:07:14+08:00"
updated_at: "2026-07-28T11:34:56+08:00"
aliases: ["Einstein equation of state", "Jacobson local horizon thermodynamics", "局部视界 Clausius 推导", "Einstein 方程热力学状态方程"]
tags: []
domains: ["gravity", "thermodynamics", "rindler-horizons"]
confidence: "high"
source_ids: ["source_4be2cb176dad6fdd8673bd31", "source_bd59f7e9cadcd7af4910d1e9", "source_086150581c4c39aee0813d57", "source_057e50214c8825e0185c4a81"]
relations: [{"type": "derived_from", "target_id": "source_4be2cb176dad6fdd8673bd31", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_7960d38d3965156bf98d11b2", "reason": "两者都以局部视界和熵能关系处理引力；Jacobson 是带 Clausius 前提的场方程导出，既有概念是 on-shell 作用量重释。", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_057e50214c8825e0185c4a81"
change_type: "support"
reflection_context: {"reflection_ids": ["reflection_ae7589ae5a41e7354d0782e1"], "importance": "high", "changed_belief": "我会把“Einstein 方程是状态方程”限定为上述局部平衡假设下的推导，而不外推为关于时空本体的无条件结论。", "surprising": "", "connections": [{"shared_mechanism": "它与既有局部 Rindler Clausius 概念都用视界热流、熵变和 Raychaudhuri 聚焦约束场方程。", "boundary": "论证假定熵与面积成正比、视界在点处瞬时平衡，并忽略热力学极限外的涨落。", "difference": "本文是面积熵下的原始 Einstein 情形；既有节点还记录高阶曲率需可积性条件或非平衡内部熵产生的扩展边界。"}], "open_questions": ["当局部平衡或面积熵失效时，哪些额外熵产生或自由度可维持一致的场方程闭合？"]}
proposed_status: "working"
---

# 局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state

在假定视界熵与面积成正比、并要求每个时空点的所有局部 Rindler 因果视界均满足 deltaQ=T dS（deltaQ 为加速观察者所见能量通量，T 为 Unruh 温度）时，Jacobson 将 Einstein 方程导出为状态方程。该论证受热力学和局部视界假设约束，未确定引力微观自由度，也不支持把场方程视作无前提地由热力学推出。

## 新增来源材料

- `source_bd59f7e9cadcd7af4910d1e9`：将局部 Clausius 关系推广到高阶曲率引力时，需要熵密度对近似局部 Killing 向量具有 Noether-charge 型依赖，并满足视界切片与可积性限制；该路线可约束由度规和 Riemann 张量代数构成的拉格朗日量，但似乎不自然容纳曲率导数项。

## 新增来源材料

- `source_086150581c4c39aee0813d57`：当局部视界熵含 Ricci-scalar 曲率修正时，平衡 Clausius 关系须扩展为 dS=dQ/T+dSi，其中 dSi 是由能量动量守恒约束的 bulk-viscosity 型内部熵产生；纯 Einstein 情形也可在允许视界 shear viscosity 时纳入熵产生。该非平衡形式不自动适用于任意高阶曲率熵泛函。

## 新增来源材料

- `source_057e50214c8825e0185c4a81`：Jacobson 的原始论证要求：穿过每个时空点的所有局部 Rindler 因果视界都满足 delta Q=T dS，其中 delta Q 是加速观察者测得的跨视界能流，T 是 Unruh 温度，且视界熵与截面积成正比。为使用平衡 Clausius 关系，视界生成元在所选点的膨胀和剪切被取为零；Raychaudhuri 方程随后把面积变化连接到 Ricci 曲率，配合能动量守恒得到 Einstein 方程，宇宙学常数作为未定积分常数出现。该结论属于热力学极限中的状态方程：它不识别引力的微观自由度，也不把场方程本身的正则量子化确立为基本量子引力理论；离开面积熵或局部平衡时需要额外的非平衡熵产生或其他闭合条件。
