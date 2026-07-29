---
id: "concept_8f8ae7b5cac6690d2e341d40"
type: "concept"
status: "proposal"
title: "人形行为基础模型的数量—多样性协同扩展"
created_at: "2026-07-21T18:09:03+08:00"
updated_at: "2026-07-21T18:09:03+08:00"
aliases: ["Quantity-Diversity Co-Scaling for Humanoid Behavior Foundation Models", "Scaling Behavior Foundation Model", "BFM", "人形行为基础模型扩展"]
tags: []
domains: ["humanoid-robotics", "reinforcement-learning", "behavior-foundation-models"]
confidence: "medium"
source_ids: ["source_46f82af34b1ace2c5c0483af"]
relations: [{"type": "derived_from", "target_id": "source_46f82af34b1ace2c5c0483af", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "前者区分训练中产生的数据数量与行为多样性，后者保存部署评估的可回放反馈；二者都需要避免用单一汇总指标掩盖分布覆盖。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_46f82af34b1ace2c5c0483af"
reflection_context: {"reflection_ids": ["reflection_1b5d5af00fc9d21516615a4b"], "importance": "high", "changed_belief": "此前容易按参考动作数量衡量人形预训练规模；这里应分别追踪并调节在线交互数量、参考动作多样性、全局运动跟踪接口和模型表达能力。", "surprising": "论文将全局坐标系整体轨迹跟踪作为减少行为歧义的统一接口，但这并不意味着局部控制或不同根状态估计下必然获得同样优势。", "connections": [{"shared_mechanism": "两者都以共享的行为表示替代每个任务单独设计奖励或控制逻辑。", "boundary": "连接只适用于行为基础模型的训练与控制接口，不把参考运动跟踪等同于真实任务成功。", "difference": "Scaling BFM讨论人形全身运动的rollout数量和参考分布；跨本体VLA两阶段训练讨论状态转换语言和机器人指令对齐。"}], "open_questions": ["当参考动作覆盖增加但在线rollout预算固定时，如何检测新增多样性是提高泛化还是稀释关键接触和恢复行为？"]}
---

# 人形行为基础模型的数量—多样性协同扩展

在人形运动跟踪的强化学习预训练中，在线并行环境与rollout时域主要决定有效交互数据数量，经过筛选的参考动作库主要决定行为分布多样性；两者需与全局全身轨迹接口和可扩展模型架构协同评估，而不能以参考动作数量单独替代训练规模。
