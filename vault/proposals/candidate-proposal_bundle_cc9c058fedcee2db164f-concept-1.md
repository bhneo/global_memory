---
id: "concept_5495a66616b2989c1ce38a5f"
type: "concept"
status: "proposal"
title: "经验成熟度驱动的机器人能力编译与回退 / Experience-maturity-driven robotic capability compilation"
created_at: "2026-08-02T12:14:58+08:00"
updated_at: "2026-08-02T12:14:58+08:00"
aliases: ["HERO capability evolution", "heuristic-exemplar-reflexive hierarchy", "H2E2R capability compilation", "机器人经验到肌肉记忆编译"]
tags: []
domains: ["robotics", "embodied-agents", "capability-learning", "policy-orchestration"]
confidence: "high"
source_ids: ["source_d0908c8e9c58809dd2665c1e"]
relations: [{"type": "derived_from", "target_id": "source_d0908c8e9c58809dd2665c1e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f35cd7f55e4108ce45ec35d7", "reason": "两者都由 orchestrator 路由异构能力并处理失败；RoboHarness 关注静态策略的能力边界与状态分布交接，HERO 关注经验成熟度驱动的能力创建、编译和反向回退。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "能力编译需要把真实执行、成功判定、经验筛选和重新训练闭合为可回放迭代；部署迭代闭环提供数据入口，但不自动保证验证或能力演化正确。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_d0908c8e9c58809dd2665c1e"
reflection_context: {"reflection_ids": ["reflection_0927933ce742db3006087d15"], "importance": "high", "changed_belief": "此前能力编排容易被看作对一组静态策略做任务路由；该论文进一步表明，编排器可以把成功经验从昂贵推理逐步转化为可复用轨迹，再编译为低延迟闭环策略，并在部署时反向按成熟度回退。", "surprising": "HERO 的数据演化采用 H→E→R，而部署采用 R→E→H；训练与执行沿同一能力谱反向流动，使快速已学能力优先，同时保留经验迁移和从头推理作为恢复路径。", "connections": [{"shared_mechanism": "都通过高层 orchestrator 在异构机器人能力之间路由，并显式处理失败与交接。", "boundary": "RoboHarness 主要估计静态策略的能力边界与状态分布交接；HERO 还让成功经验随重复使用从启发式执行演化为 exemplar，再训练为 reflexive policy。", "difference": "前者强调未经联合训练策略之间的输入状态可达性，后者强调经验成熟度驱动的能力创建、编译和反向回退。"}], "open_questions": ["如何在不依赖人工定义 primitive skill space 的前提下发现新能力层，并防止错误的成功判定被编译进 reflexive policy？"]}
---

# 经验成熟度驱动的机器人能力编译与回退 / Experience-maturity-driven robotic capability compilation

把机器人能力按经验成熟度组织为三个可演化执行层：启发式 bootstrapper 用 VLM 和几何原语处理无经验任务，exemplar accelerator 对成功轨迹做对象点云配准与几何迁移，reflexive policy 则把重复且通过筛选的经验训练为闭环 visuomotor 控制。数据演化沿 H→E→R 把昂贵推理逐步编译为快速策略，部署沿 R→E→H 优先使用已内化能力，并在 policy 不可用或失败时退回轨迹复用和从头推理。该机制不同于只路由静态策略的能力编排：orchestrator 同时改变能力库存的生命周期。它仍依赖成功验证器、深度/点云质量、人工定义 primitive skill space、每任务训练和可恢复场景；错误成功判定可能污染 exemplar 与下游 policy，不能把少量真实任务结果外推为开放世界自主学习保证。
