---
id: "concept_a858f8d191d3afdd69418471"
type: "concept"
status: "proposal"
title: "陈旧性对齐与上下文分区共同约束异步快慢控制接口"
created_at: "2026-07-26T12:18:41+08:00"
updated_at: "2026-07-27T19:02:43+08:00"
aliases: ["Staleness-Aligned Asynchronous Slow-Context Fast-Control Interface", "FastSlow-LMDrive", "异步快慢 VLA 接口"]
tags: []
domains: ["vla", "real-time-control", "autonomous-driving"]
confidence: "medium"
source_ids: ["source_d4762e0cf2330ab6ea00a521", "source_e67cd99ac31c7017d6f7f7c7"]
relations: [{"type": "derived_from", "target_id": "source_d4762e0cf2330ab6ea00a521", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都在保留慢速预训练表示的同时增加读取新鲜局部传感的快分支；前者面向视觉驾驶缓存，后者面向动作块内力反馈。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都依赖非对称接口使冻结主干可被复用；FastSlow 在单策略内部复用缓存，既有概念在多原语编排中复用冻结局部专家。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_30d85c442682f6afd96c3022", "reason": "两者都复用慢表示并让快路径读取新鲜信息；前者用训练覆盖缓存陈旧性，后者用 static、sliding、dynamic 分区证明部分 KV 复用的正确性，适用边界并不相同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}]
change_reason: "compile bundle from source_e67cd99ac31c7017d6f7f7c7"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_d8d4183ecacf40814756f4c2"], "importance": "weekly", "changed_belief": "我会把实时性归因于缓存有效性与异步执行的系统契约，而不把任何 flow-matching VLA 的缓存复用或论文基准速度泛化为普遍部署保证。", "surprising": "", "connections": [{"shared_mechanism": "两者都以异步执行和复用不随当前采样步变化的计算来减少控制等待。", "boundary": "本文限于其 timestep-invariance 分区、固定输入下的 attention 等价性及 LIBERO/Kinetix 报告设置。", "difference": "一般异步推理只重叠预测与执行；Reflex 还主张通过静态/滑动/动态上下文分区保持增量 KV 缓存的数学正确性。"}], "open_questions": ["感知输入变化、动作反馈和长时闭环分布漂移下，哪些区域仍可安全缓存且保持端到端控制稳定？"]}
proposed_status: "working"
---

# 陈旧性对齐的异步慢上下文—快控制接口

在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。

## 新增来源材料

- `source_e67cd99ac31c7017d6f7f7c7`：在需要高频闭环控制的 VLA 系统中，慢上下文与快动作接口应同时声明缓存内容的时间角色和有效期。FastSlow-LMDrive 用训练时随机截断覆盖部署缓存陈旧性；Reflex 则把 flow-matching 注意力分成 static、sliding 与 dynamic 区域，并仅对去噪步不变的部分做增量 KV 更新。两种机制都要求固定输入下与完整前向的等价性或可检验一致性，但训练时陈旧性对齐不能替代 Reflex 的 timestep-invariance 分区，缓存加速也不能证明长时闭环稳定或部署安全。
