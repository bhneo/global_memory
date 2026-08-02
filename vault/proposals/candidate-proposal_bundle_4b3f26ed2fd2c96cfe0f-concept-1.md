---
id: "concept_61c0ffd089f650a51ec3f00d"
type: "concept"
status: "proposal"
title: "上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions"
created_at: "2026-08-02T18:21:44+08:00"
updated_at: "2026-08-02T18:21:44+08:00"
aliases: ["RedFlow", "context-aware corrective matching", "adaptive redirection objective", "结构化失败数据复用"]
tags: []
domains: ["robotics", "vla", "offline-reinforcement-learning", "flow-policy"]
confidence: "high"
source_ids: ["source_9f9972326eb118a8e4bb5623"]
relations: [{"type": "derived_from", "target_id": "source_9f9972326eb118a8e4bb5623", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都保留 flow 先验并限制外部反馈的干预范围；RedFlow 在动作速度场中使用上下文匹配的离线成败样本，RLMM-Flow 用 critic 在潜变量中分阶段转向整段轨迹。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_9f9972326eb118a8e4bb5623"
reflection_context: {"reflection_ids": ["reflection_4602753df83a62d4799d8e91"], "importance": "high", "changed_belief": "我原先更倾向把失败轨迹视为统一的反偏好信号；该工作把它拆成可被同上下文正样本重定向的失败动作，以及只能安全压制的无匹配失败动作。", "surprising": "修正目标不是人工标注的唯一动作，而是同进度、近似本体上下文中的正样本动作重心；这把多解动作空间中的纠正保持为集合内插值。", "connections": [{"shared_mechanism": "RedFlow 与既有 concept_6a559a41722de87986c350e7 都保留 flow 生成先验，并把外部质量或价值反馈限制在比全模型更新更窄的后训练接口。", "boundary": "该连接只适用于基础 flow policy 已覆盖目标行为邻域的条件；两项工作都不能从先验支持域外凭空恢复动作能力。", "difference": "RedFlow 在动作速度场上用离线成败轨迹与 progress-proprioception 上下文匹配纠偏，RLMM-Flow 在潜变量上用 critic 分阶段转向整段轨迹。"}], "open_questions": ["如何检测 progress-proprioception 上的近邻是否已经越出正样本支持域，并在此时自动退化为仅压制而非重定向？"]}
---

# 上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions

在 mixed-quality 离线 flow-policy 后训练中，先用任务进度把轨迹切到相近阶段，再用本体状态聚类近似局部决策上下文。对能找到同上下文正样本的失败动作，以正动作的加权重心作为集合内纠正端点并重定向 flow 速度；对没有可靠正支持的失败动作只施加有界抑制；同时保留对高质量动作的吸引。这样可分别表达质量保持、失败抑制和可支持的纠正，但其有效性依赖进度奖励、聚类和正样本覆盖；匹配错误会产生伪纠正，支持域外失败不能由该机制恢复正确动作。
