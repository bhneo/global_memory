---
id: "concept_ca2e18a64c50dab0d08b3f1a"
type: "concept"
status: "proposal"
title: "依赖闭包的组件准入与新鲜作用域恢复 / Dependency-closed component admission and fresh scoped recovery"
created_at: "2026-08-02T18:58:12+08:00"
updated_at: "2026-08-02T18:58:12+08:00"
aliases: ["HALO", "support-closure admission", "one-dispatch token", "依赖闭包运行时准入"]
tags: []
domains: ["agent-safety", "robotics", "runtime-admission", "authorization"]
confidence: "high"
source_ids: ["source_8c84c595f1a48ba498b2074e"]
relations: [{"type": "derived_from", "target_id": "source_8c84c595f1a48ba498b2074e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_protocol_hri_agent_execution_boundary", "reason": "两者都分离 Agent 交互、授权和能力派发；HALO 进一步定义回复组件在支持漂移下的闭包准入、摘要见证与最终门。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都用类型图、依赖和恢复结构约束机器人执行；技能图是长期 workflow，HALO 面向一次回复的运行时最大支持闭包和新鲜授权。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_8c84c595f1a48ba498b2074e"
reflection_context: {"reflection_ids": ["reflection_0c154d1167b819af9040f0f9"], "importance": "high", "changed_belief": "我原先会把部分接受主要理解为 schema 过滤；该工作显示，单个组件即使本身受支持，也可能因依赖的结果、参考或前置条件失效而必须被闭包删除，而且闭包后仍需一次独立的实时授权。", "surprising": "恢复建议本身被建模为无权限 obligation：它能记录作用域、原因和恢复路线，却不能重放旧组件；只有重新生成的新候选通过完整准入后才可执行。", "connections": [{"shared_mechanism": "HALO 与 concept_dual_protocol_hri_agent_execution_boundary 都把 Agent 通信、授权和物理能力派发分层。", "boundary": "协议或准入门都不替代设备控制器的实时稳定性、碰撞避免与下游物理安全。", "difference": "既有节点描述 ACP/MCP 的通信职责，HALO 定义回复组件图在支持漂移下的保留闭包、摘要见证和单次派发 token。"}, {"shared_mechanism": "HALO 与 concept_typed_verified_robot_skill_graph 都以类型化图、依赖和恢复结构约束执行。", "boundary": "HALO 针对一次异构 Agent 回复的运行时准入，不等同于长期技能图的仿真验证和任务编排。", "difference": "技能图外化可复用 workflow；HALO 计算当前支持下的最大依赖闭包，并在最后一刻重新验证授权。"}], "open_questions": ["当支持目录、授权账本和执行适配器分布在多节点时，如何保持最终门的原子消费与当前闭包见证，而不把延迟变成新的竞态窗口？"]}
---

# 依赖闭包的组件准入与新鲜作用域恢复 / Dependency-closed component admission and fresh scoped recovery

当一次 Agent 回复包含文本、建议、动作和恢复等异构组件时，保留与执行必须分成两层。先把回复视为不可信类型化组件图，依据可信能力目录为每个组件计算支持足迹，并迭代删除不受支持或依赖已删除组件的节点，得到当前支持下的最大依赖闭包。随后对保留组件生成确定性的规范摘要与见证，只签发绑定具体组件的一次性派发 token；唯一最终门在调用适配器前重新计算当前闭包、检查依赖处理阶段和摘要、原子消费 token。恢复 obligation 只记录作用域、原因、支持条件与路线，不携带旧动作权限；恢复必须生成新候选并重新经历完整准入。该协议依赖可信目录、支持提供者、授权账本和适配器，不能发现未声明依赖、证明语义真值、提供分布式 exactly-once 或替代下游物理安全。
