---
id: "concept_0c7884679bf6d4e1287ce225"
type: "concept"
status: "proposal"
title: "控制策略的自适应潜空间推理"
created_at: "2026-07-19T17:16:26+08:00"
updated_at: "2026-07-19T22:43:05+08:00"
aliases: ["Adaptive Latent Reasoning for Control", "自适应潜推理控制", "Latent Memory Palace", "LMP"]
tags: []
domains: ["embodied-ai", "robot-control", "latent-reasoning"]
confidence: "medium"
source_ids: ["source_be9781ec8ca637c5dfd8fabb"]
relations: [{"type": "derived_from", "target_id": "source_be9781ec8ca637c5dfd8fabb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者分别在动作前内部推理和动作后执行阶段自适应分配预算，构成不同控制层的可变计算时域。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者分别在动作前内部推理和动作后执行阶段自适应分配预算，构成不同控制层的可变计算时域。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_be9781ec8ca637c5dfd8fabb"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_12ec24dd673a937d90f5bc21"], "importance": "high", "changed_belief": "此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数。", "surprising": "同一套自回归潜变量框架还可产生可变长度动作 tokenizer，暗示推理长度与动作分段可能由共同的表示机制控制。", "connections": [{"shared_mechanism": "都根据当前状态与任务难度动态分配有限的计算或执行预算", "boundary": "连接只适用于自适应预算分配，不表示内部推理步数与外部动作执行时域等价", "difference": "LMP 调整动作生成前的潜变量推断长度，动态执行时域调整动作生成后的开环执行长度"}], "open_questions": ["潜推理长度能否被校准为任务难度或失败风险的可靠信号？"]}
proposed_status: "working"
---

# 控制策略的自适应潜空间推理

控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。
