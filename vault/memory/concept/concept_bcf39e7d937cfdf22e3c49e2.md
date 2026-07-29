---
id: "concept_bcf39e7d937cfdf22e3c49e2"
type: "concept"
status: "working"
title: "面向真实零售人形机器人的数据高效 VLA 后训练闭环"
created_at: "2026-07-24T18:05:38+08:00"
updated_at: "2026-07-26T12:33:44+08:00"
aliases: ["Data-Efficient Experience-Driven VLA Post-Training", "DEED", "数据高效经验驱动 VLA 后训练"]
tags: []
domains: ["humanoid-robotics", "vla", "post-training"]
confidence: "medium"
source_ids: ["source_3846f8c1451f8a12e0f87b33"]
relations: [{"type": "derived_from", "target_id": "source_3846f8c1451f8a12e0f87b33", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者均讨论将 VLA 用于异构实体环境；DEED 具体限定部署后的频率、数据和经验接口，而该既有概念描述跨本体策略的一般输入输出接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_3846f8c1451f8a12e0f87b33"
reflection_context: {"reflection_ids": ["reflection_3b2e99de9c8c6dfc2ba8cd5a"], "importance": "high", "changed_belief": "先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上，控制与数据接口的对齐以及对策略自身失败状态的经验回收同样决定能否从朴素微调转为可用行为。", "surprising": "", "connections": [], "open_questions": ["文本 advantage 前缀和视觉语言价值函数在不同零售任务、不同经验比例下何时会避免或加剧自生成 rollout 主导训练分布的退化？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:44+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_9186ea727626fb11fc36"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_9186ea727626fb11fc36-concept-1.md"
origin_candidate_sha256: "f0ac2de44b73215afc46336043a5f819bd82a86cd53feeac2ee2f3c2e7b42c22"
memory_schema_version: 2
last_consolidation_id: "consolidation_a29e9e1022d0fcc95e301f25"
---

# 面向真实零售人形机器人的数据高效 VLA 后训练闭环

在超市场景中部署预训练 VLA 时，可把控制频率对齐、数据筛选、任务相关视觉突出和降低对 VLA 主动作流依赖的后训练配方，与从当前策略失败状态收集的经验驱动细化结合；其目标是缩小实验室到门店的系统失配，而非证明这些组件可独立保证所有人形机器人任务的可靠性。
