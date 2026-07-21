---
id: "concept_637cf7264723c03955c719e2"
type: "concept"
status: "proposal"
title: "遥操作跟踪偏差作为隐式交互线索"
created_at: "2026-07-20T18:05:38+08:00"
updated_at: "2026-07-20T18:05:38+08:00"
aliases: ["Teleoperation Tracking Discrepancy as Implicit Interaction Cue", "Implicit Force Cue in ACT", "遥操作隐式力线索"]
tags: []
domains: ["embodied-ai", "contact-manipulation", "imitation-learning"]
confidence: "medium"
source_ids: ["source_158b4743a3d4e973913f8bbf"]
relations: [{"type": "derived_from", "target_id": "source_158b4743a3d4e973913f8bbf", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_5b49f7afd60ba18d35ca58e8", "reason": "两者都把接触信息作为纯运动学模仿之外的必要信号，但一个来自机器人遥操作误差，另一个来自人类压力与接触参考。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_158b4743a3d4e973913f8bbf"
reflection_context: {"reflection_ids": ["reflection_91f2ffd2085e86802850ad17"], "importance": "high", "changed_belief": "此前容易将 ACT 的接触能力归因于动作分块架构；这里提示必须区分架构能力与遥操作管线暗中提供的交互线索。", "surprising": "", "connections": [{"shared_mechanism": "两者都试图让策略保留对接触形成、阻力和安全约束敏感的状态。", "boundary": "该连接不假定电机电流或力矩 proxy 等同于真实六维力/力矩测量。", "difference": "触觉对齐的人到机器人接触迁移用显式压力和接触结构作为监督；本文比较遥操作误差这一隐式线索与由机载测量导出的力矩 proxy。"}], "open_questions": ["不同控制器增益、摩擦补偿和传感噪声下，何时力矩 proxy 足以替代遥操作误差信号？"]}
---

# 遥操作跟踪偏差作为隐式交互线索

在 leader–follower 位置控制遥操作中，leader 命令与 follower 执行状态之间的跟踪偏差可与接触起始、外部阻力和约束违反相关；若改为预测未来 follower 状态而移除该偏差，接触关键阶段可能失去该隐式观测，而机载关节力矩或电流 proxy 可作为可显式建模的替代信号。
