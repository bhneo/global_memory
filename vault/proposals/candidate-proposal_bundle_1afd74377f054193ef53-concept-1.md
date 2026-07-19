---
id: "concept_staged_cross_embodiment_alignment"
type: "concept"
status: "proposal"
title: "异构具身数据的分阶段对齐"
created_at: "2026-07-19T02:51:00+08:00"
updated_at: "2026-07-19T02:51:00+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "humanoid", "robot-learning"]
confidence: "medium"
source_ids: ["source_691f3acc1fe3382639690f59"]
relations: [{"type": "derived_from", "target_id": "source_691f3acc1fe3382639690f59", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "该方法把具身数据闭环进一步区分为通用表征数据与本体控制数据两个训练阶段。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
change_reason: "compile bundle from source_691f3acc1fe3382639690f59"
uncertainty: "这是对 Ψ₀ 训练配方的概念归纳，尚未证明适用于所有机器人形态。"
---

# 异构具身数据的分阶段对齐

把人类视频中的通用视觉—动作表征学习，与机器人本体专属的连续控制学习拆成不同阶段，以减少人类运动学和机器人运动学差异造成的负迁移。
