---
id: "concept_39512575bdcd8ac68d340b03"
type: "concept"
status: "proposal"
title: "状态转换语言驱动的跨本体 VLA 两阶段训练"
created_at: "2026-07-21T18:08:34+08:00"
updated_at: "2026-07-21T18:08:34+08:00"
aliases: ["State-Transition Language Driven Cross-Embodiment VLA Training", "Xiaomi-Robotics-1", "状态转换语言跨本体训练"]
tags: []
domains: ["embodied-ai", "vla", "robot-learning"]
confidence: "medium"
source_ids: ["source_5df8ebbcd9bd1afec33d46cc"]
relations: [{"type": "derived_from", "target_id": "source_5df8ebbcd9bd1afec33d46cc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "前者定义训练数据如何跨本体对齐，后者定义对齐后的策略如何被真实执行记录和评估；两者共同需要保留任务与本体边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_5df8ebbcd9bd1afec33d46cc"
reflection_context: {"reflection_ids": ["reflection_3ea617cf483f3d85a6aa4d31"], "importance": "high", "changed_belief": "此前容易把 VLA 扩展理解为只增加遥操作小时数；这里的关键变化是，能扩展的预训练数据需要有与动作结果相连的状态转换语言，且仍需单独处理末端执行器和提示形式的本体差异。", "surprising": "论文报告预训练规模收益会转移到未见环境的后训练真机评估，但这一结果仅适用于其两阶段数据、模型和评测设置，不能替代接触安全或任务特定验证。", "connections": [{"shared_mechanism": "两者都通过结构化数据接口把模型训练连接到可回放的真实机器人评估。", "boundary": "该连接只涉及训练数据语义与评估闭环的衔接，不把一次评测日志变成对跨本体泛化的证据。", "difference": "Xiaomi-Robotics-1处理预训练到后训练的语言和动作本体对齐；真机部署评估闭环强调每次执行的日志、评分和训练反馈。"}], "open_questions": ["固定长度轨迹的状态转换自动标注在长程任务中何时会丢失对接触前提、失败恢复或子目标顺序的必要约束？"]}
---

# 状态转换语言驱动的跨本体 VLA 两阶段训练

先用大规模轨迹中自动生成的场景状态转换语言训练观察和语言到动作块的映射，再用跨本体机器人数据把该能力对齐到机器人动作空间与祈使任务指令的 VLA 训练配方；其跨本体收益应按目标本体、任务和真机评测分别验证。
