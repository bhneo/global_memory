---
id: "concept_24de3544824d45b83583c5a5"
type: "concept"
status: "proposal"
title: "全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity"
created_at: "2026-07-28T01:47:06+08:00"
updated_at: "2026-07-28T10:18:43+08:00"
aliases: ["gravitation from entanglement", "entanglement first law linearized AdS", "纠缠第一律导出线性化引力", "球形区域全息引力约束"]
tags: []
domains: ["ads-cft", "quantum-gravity", "entanglement"]
confidence: "high"
source_ids: ["source_8e0a54f1b7764d6c5f111dcb", "source_62c0eb77c44fc70ee44d7233"]
relations: [{"type": "derived_from", "target_id": "source_8e0a54f1b7764d6c5f111dcb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}, {"type": "related_to", "target_id": "concept_4e520f39dde022d5e1042625", "reason": "两者都用纠缠的一阶变分约束 Einstein 方程，但本项依赖 AdS/CFT 与 RT，既有节点使用固定体积小测地球的真空纠缠平衡。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_62c0eb77c44fc70ee44d7233"
change_type: "support"
reflection_context: {"reflection_ids": ["reflection_110c74eddca156c2211ac7cc"], "importance": "high", "changed_belief": "我会把纠缠--几何联系限定为具有半经典 holographic dual、真空小扰动与球形区域的命题。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过纠缠量与几何或引力约束建立跨描述层的对应。", "boundary": "本文限于 CFT 的半经典全息对偶、真空附近小扰动和球形区域。", "difference": "既有纠缠--时空条目概述连通性线索；本文给出纠缠第一律到线性化场方程的具体约束。"}], "open_questions": ["如何从线性化、球形区域的约束推广到非线性、一般区域或非全息量子系统？"]}
proposed_status: "working"
---

# 全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity

对具有半经典 AdS 对偶的 CFT 真空的小扰动，将纠缠第一定律应用于所有球形边界区域，并用 RT 面积关系和边界应力张量--渐近度规字典，可得到纯 AdS 附近的线性化 Einstein 方程。只在一个固定 Lorentz 参考系考察所有球时仅获得部分分量；完整方程需要任意参考系。该结论局限于真空附近、球形区域、线性阶和经典全息度规扇区，不能约束所有额外 bulk 场或直接推广到非线性引力。

## 新增来源材料

- `source_62c0eb77c44fc70ee44d7233`：原始论文证明，在具有半经典全息对偶的 CFT 中，对真空态的小扰动和所有球形空间区域施加纠缠第一律，与 dual geometry 满足纯 AdS 附近的线性化引力方程等价。若纠缠熵由 Ryu--Takayanagi 面积给出，得到线性化 Einstein 方程；若由更一般 Wald 泛函给出，则得到相应高曲率引力理论的线性化方程。其讨论同时限制了外推：论证使用全局 AdS-Rindler 区域且只达线性阶，有限扰动提供的是相对熵不等式，通常不足以单独确定完整非线性方程或依赖具体 CFT 的额外 bulk 场。
