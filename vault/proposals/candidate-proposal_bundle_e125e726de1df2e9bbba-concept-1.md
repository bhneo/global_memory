---
id: "concept_2ce226e08d585158c1dfbb18"
type: "concept"
status: "proposal"
title: "保留视觉语言先验的块内反应式力注入"
created_at: "2026-07-24T18:06:12+08:00"
updated_at: "2026-07-24T18:07:25+08:00"
aliases: ["Late Reactive Force Injection", "LIFT", "反应式力注入 VLA 后训练"]
tags: []
domains: ["vla", "force-control", "contact-rich-manipulation"]
confidence: "medium"
source_ids: ["source_4e06d1b1cdcd0d07eff47909"]
relations: [{"type": "derived_from", "target_id": "source_4e06d1b1cdcd0d07eff47909", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_637cf7264723c03955c719e2", "reason": "两者都使用交互中的附加信号缓解视觉歧义；本概念采用显式力记忆和反应分支，既有概念采用遥操作跟踪偏差这一隐式 proxy。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_637cf7264723c03955c719e2", "reason": "两者都使用交互中的附加信号缓解视觉歧义；本概念采用显式力记忆和反应分支，既有概念采用遥操作跟踪偏差这一隐式 proxy。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4e06d1b1cdcd0d07eff47909"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_1f5ecace3c0b5fd265b9d846"], "importance": "high", "changed_belief": "接触传感并非只能作为全模型重训的额外输入；若初始化时严格保持原动作输出，稀缺的在线力纠正可以针对策略实际访问的接触失败状态进行局部适配。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过补充交互信号来弥补纯视觉在接触状态中的可观测性缺口。", "boundary": "该连接适用于力、力矩或跟踪偏差能可靠反映接触变化的控制系统，不说明任一 proxy 在所有硬件上等价于测得六维力。", "difference": "LIFT 显式编码近期六维末端力并在动作块内反应；既有概念讨论遥操作 leader–follower 的跟踪偏差作为隐式线索。"}], "open_questions": []}
proposed_status: "working"
---

# 保留视觉语言先验的块内反应式力注入

对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。
