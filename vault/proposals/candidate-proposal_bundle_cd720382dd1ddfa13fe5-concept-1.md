---
id: "concept_5b49f7afd60ba18d35ca58e8"
type: "concept"
status: "proposal"
title: "触觉对齐的人到机器人接触迁移"
created_at: "2026-07-20T12:39:31+08:00"
updated_at: "2026-07-20T12:39:31+08:00"
aliases: ["Tactile-aligned human-to-robot contact transfer", "TactiDex", "TactiSkill", "接触保真迁移"]
tags: []
domains: ["embodied-ai", "dexterous-manipulation", "tactile-transfer", "contact-evaluation"]
confidence: "high"
source_ids: ["source_37fe3c1f9d9fb7daa262fa91"]
relations: [{"type": "derived_from", "target_id": "source_37fe3c1f9d9fb7daa262fa91", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "触觉迁移提供目标接触结构，多时间尺度控制提供运行时预测与快速纠偏，两者覆盖训练 reference 与执行闭环的不同环节。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_37fe3c1f9d9fb7daa262fa91"
reflection_context: {"reflection_ids": ["reflection_e8e62c04da8ad9f420c37be4"], "importance": "high", "changed_belief": "此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。", "surprising": "纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。", "connections": [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。", "boundary": "TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。", "difference": "多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。"}], "open_questions": ["哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？"]}
---

# 触觉对齐的人到机器人接触迁移

在人类示范中同步手部运动学、物体状态和全手压力，把接触形成、接触区域时序、力幅值与安全约束作为独立监督和评测维度。该范式纠正纯运动学模仿的接触缺口，但跨本体时不应假设人类接触分布可无条件照搬。
