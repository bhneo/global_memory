---
id: "concept_dual_protocol_hri_agent_execution_boundary"
type: "concept"
status: "proposal"
title: "人机客户端与 Agent 执行的双协议边界"
created_at: "2026-07-21T17:44:43+08:00"
updated_at: "2026-07-21T17:44:43+08:00"
aliases: ["Dual-Protocol HRI and Agent Execution Boundary", "ACP-MCP Robot Architecture", "Agent-Client Protocol", "ACP", "人机交互双协议架构"]
tags: []
domains: ["agent-infrastructure", "human-robot-interaction", "mcp"]
confidence: "medium"
source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
relations: [{"type": "derived_from", "target_id": "source_a0c7811ba12c9cf80bfd26c9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "双协议架构定义通信与授权边界，类型化技能图定义可验证执行结构；两者覆盖不同层级。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
change_reason: "compile bundle from source_a0c7811ba12c9cf80bfd26c9"
reflection_context: {"reflection_ids": ["reflection_797e923d7a0e6ef67bb26728"], "importance": "high", "changed_belief": "可插拔 Agent 接入不仅需要工具协议，还需要独立的人机交互协议；否则 UI、授权和中断语义仍会与具体 Agent 实现耦合。", "surprising": "作者把原为编码 Agent 设计的 ACP 移植到机器人 HRI，并只在其原型架构上验证；这证明可行性而非实时安全、互操作成熟度或工业可靠性。", "connections": [{"shared_mechanism": "都把物理能力暴露为结构化服务，并保留高层可观察控制。", "boundary": "协议解耦不替代机器人侧安全控制、时限保证或动作验证。", "difference": "RPent 聚焦物理 Agent 基础设施和共享工作空间；ACP+MCP 架构明确拆分人机客户端、Agent 编排与执行协议。"}], "open_questions": ["ACP 的取消、授权和流式状态语义如何映射到不可瞬时中断的物理动作？"]}
---

# 人机客户端与 Agent 执行的双协议边界

在三层机器人 Agent 架构中，以 Agent-Client Protocol（ACP）连接人类界面与推理 Agent，承载流式可观察性、显式授权和任务中断；以 Model Context Protocol（MCP）连接 Agent 与机器人能力服务。该分层降低 UI、推理器和平台的直接耦合，但协议层可行性不构成实时控制、安全停止或工业互操作保证。
