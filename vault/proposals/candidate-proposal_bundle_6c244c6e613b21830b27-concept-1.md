---
id: "concept_16a7c84a59e39784c801e4ff"
type: "concept"
status: "proposal"
title: "非特权开放世界移动操作评测边界"
created_at: "2026-07-22T18:12:25+08:00"
updated_at: "2026-07-22T18:12:25+08:00"
aliases: ["Non-Privileged Open-World Mobile Manipulation Evaluation", "REAL", "REAL-Bench", "非特权移动操作评测"]
tags: []
domains: ["mobile-manipulation", "benchmarking"]
confidence: "medium"
source_ids: ["source_92fed4343c703da77f798f08"]
relations: [{"type": "derived_from", "target_id": "source_92fed4343c703da77f798f08", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_protocol_hri_agent_execution_boundary", "reason": "两者都将语言交互和物理执行分别置于明确协议边界中；REAL 用任务环境检验该边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_92fed4343c703da77f798f08"
reflection_context: {"reflection_ids": ["reflection_f83b07f9aed0e61ac4a066d9"], "importance": "high", "changed_belief": "开放世界评测不能默认对象列表、目标位姿或无歧义指令；这些信息缺口本身构成策略能力与失败来源。", "surprising": "论文报告的实机结果来自特定双臂移动平台与 60 个 episode，说明该评测边界比仅模拟指标更强，但仍不是跨平台保证。", "connections": [], "open_questions": ["如何分解报告探索、澄清、工具执行与物理可达性对每次失败的贡献？"]}
---

# 非特权开放世界移动操作评测边界

面向开放世界移动操作的评测应限制策略使用 RGB 等物理可获得输入，并把主动探索、视觉消歧和人机意图澄清纳入闭环任务；模拟与实机成绩必须连同具体工具、资产、episode 和本体条件解释。
