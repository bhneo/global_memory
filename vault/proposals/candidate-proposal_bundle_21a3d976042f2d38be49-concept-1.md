---
id: "concept_a858f8d191d3afdd69418471"
type: "concept"
status: "proposal"
title: "陈旧性对齐的异步慢上下文—快控制接口"
created_at: "2026-07-26T12:18:41+08:00"
updated_at: "2026-07-26T12:18:41+08:00"
aliases: ["Staleness-Aligned Asynchronous Slow-Context Fast-Control Interface", "FastSlow-LMDrive", "异步快慢 VLA 接口"]
tags: []
domains: ["vla", "real-time-control", "autonomous-driving"]
confidence: "medium"
source_ids: ["source_d4762e0cf2330ab6ea00a521"]
relations: [{"type": "derived_from", "target_id": "source_d4762e0cf2330ab6ea00a521", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都在保留慢速预训练表示的同时增加读取新鲜局部传感的快分支；前者面向视觉驾驶缓存，后者面向动作块内力反馈。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都依赖非对称接口使冻结主干可被复用；FastSlow 在单策略内部复用缓存，既有概念在多原语编排中复用冻结局部专家。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_d4762e0cf2330ab6ea00a521"
reflection_context: {"reflection_ids": ["reflection_743b2d2d30d2f822bf2bfb9f"], "importance": "high", "changed_belief": "此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支 token、缓存可增量等价更新且快分支在训练中见过滞后上下文时，异步复用才是可验证的系统契约。", "surprising": "同一 action expert 从 10 Hz 提升到 20 Hz 主要提高路线完成率与减少偏航/超时，而综合 driving score 未同步提高并伴随更多车辆碰撞暴露；控制新鲜度和安全驾驶质量不是同一指标。", "connections": [{"shared_mechanism": "FastSlow-LMDrive 与块内反应式力注入都保留慢速预训练先验，同时用更快、更新鲜的局部观测驱动轻量动作分支。", "boundary": "连接适用于慢上下文在多个控制 tick 内仍有用、快路径可独立读取当前传感且延迟分布可在训练中覆盖的任务。", "difference": "FastSlow-LMDrive 通过逐层视觉语言 KV cache 服务驾驶 waypoint expert；力注入概念通过近期六维力记忆修正接触动作块，安全变量与传感动力学不同。"}], "open_questions": ["能否用快慢分支分歧和缓存年龄共同触发安全降级，并在长路线密集交通中减少完成率上升带来的碰撞暴露？"]}
---

# 陈旧性对齐的异步慢上下文—快控制接口

在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。
