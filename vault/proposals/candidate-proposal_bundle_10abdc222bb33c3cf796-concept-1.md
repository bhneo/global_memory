---
id: "concept_ab253cb9064bc1b550d5e973"
type: "concept"
status: "proposal"
title: "跨本体世界监督通道"
created_at: "2026-07-19T17:16:45+08:00"
updated_at: "2026-07-19T22:43:22+08:00"
aliases: ["Cross-Embodiment World Supervision Channel", "Embodiment-Invariant World Target", "EGOWAM", "World Action Model"]
tags: []
domains: ["embodied-ai", "world-model", "cross-embodiment"]
confidence: "medium"
source_ids: ["source_61f3045b170e78e4adb2422c"]
relations: [{"type": "derived_from", "target_id": "source_61f3045b170e78e4adb2422c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它把跨本体通用策略进一步分解为世界监督共享与动作执行对齐两个通道，并明确前者的表示条件。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它把跨本体通用策略进一步分解为世界监督共享与动作执行对齐两个通道，并明确前者的表示条件。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_61f3045b170e78e4adb2422c"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_0dd383cc873ce81c0afd3d06"], "importance": "high", "changed_belief": "此前跨本体 VLA 更强调统一动作接口或数据混合；该材料提示应先选择能抽象外观、保持跨本体一致并分离相机运动的 world target，再讨论动作对齐。", "surprising": "该受控比较中像素重建迁移较弱，而 DINO 特征和 3D flow 的收益方向不同，说明“增加世界模型头”本身不够，预测目标的抽象层级决定迁移内容。", "connections": [{"shared_mechanism": "都试图从多形态数据中保留任务语义和物理效果，同时隔离本体特有的执行因素", "boundary": "连接只覆盖跨本体表示共享，不意味着世界监督可以替代机器人动作数据或解决控制精度", "difference": "通用 VLA 侧重统一策略输入输出接口，EGOWAM 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式"}], "open_questions": ["什么 world target 能同时保留接触动力学、分离 ego-motion 并跨不同机器人相机布局迁移？"]}
proposed_status: "working"
---

# 跨本体世界监督通道

在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。
