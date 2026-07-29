---
id: "concept_186fc27b4c190ed39889bb9e"
type: "concept"
status: "proposal"
title: "非特权开放世界移动操作的工具化评测契约"
created_at: "2026-07-21T18:09:12+08:00"
updated_at: "2026-07-21T18:09:12+08:00"
aliases: ["Tool-Mediated Evaluation Contract for Non-Privileged Open-World Mobile Manipulation", "REAL", "REAL-Bench", "非特权移动操作评测"]
tags: []
domains: ["embodied-ai", "mobile-manipulation", "benchmarking"]
confidence: "medium"
source_ids: ["source_a5f8ae205338d5f97eea87c7"]
relations: [{"type": "derived_from", "target_id": "source_a5f8ae205338d5f97eea87c7", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都让执行过程显式化并可检查；REAL提供具体工具与episode协议，技能图提供任务节点和恢复语义。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_a5f8ae205338d5f97eea87c7"
reflection_context: {"reflection_ids": ["reflection_e7c85185b496df7cb4ef1b85"], "importance": "high", "changed_belief": "此前容易将MCP理解为模型连接器；该项目表明在移动操作中，工具协议、episode生命周期、任务配置与物理资产前提共同决定评测是否可复现。", "surprising": "", "connections": [{"shared_mechanism": "两者都把机器人决策封装在带检查和恢复边界的工具化执行流程中。", "boundary": "连接不表示REAL仓库已验证任何外部技能图或在缺少Isaac Sim资产时可直接复现实机结果。", "difference": "REAL定义具体仿真MCP工具、241项任务和在线RL/SFT流程；可验证机器人技能图是更抽象的任务编译与验证结构。"}], "open_questions": ["当任务需要澄清意图时，如何分别报告语言澄清、视觉探索、工具执行和物理可达性对最终失败的贡献？"]}
---

# 非特权开放世界移动操作的工具化评测契约

面向开放世界移动操作的评测框架：Agent从原始RGB进行探索，通过导航、感知和操作工具执行动作，并在指令含糊时与模拟用户澄清意图；可复现评测还需绑定任务配置、episode生命周期、兼容场景和物体资产，仓库声明的仿真或真机成功率不应脱离这些前提解释。
