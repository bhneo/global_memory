---
id: "concept_vla_action_cache_refinement"
type: "concept"
status: "proposal"
title: "VLA 动作缓存与上下文复用"
created_at: "2026-07-19T03:02:11+08:00"
updated_at: "2026-07-19T23:47:20+08:00"
aliases: ["VLA action caching and refinement", "ActionCache"]
tags: []
domains: ["embodied-ai", "vla", "inference-efficiency", "memory"]
confidence: "medium"
source_ids: ["source_291d6174cf92660287138f47"]
relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "缓存复用和动作块执行都延长已有中间结果的有效期，因此需要按环境变化和不确定性共同决定何时重新生成。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
change_reason: "compile bundle from source_291d6174cf92660287138f47"
change_type: "metadata_only"
reflection_context: {"reflection_ids": ["reflection_62e14da60b1cc35f28689c29"], "importance": "weekly", "changed_belief": "此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。", "surprising": "缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。", "connections": [{"shared_mechanism": "都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬", "boundary": "连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解", "difference": "ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合"}], "open_questions": ["缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？"]}
proposed_status: "working"
---

# VLA 动作缓存与上下文复用

为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。
