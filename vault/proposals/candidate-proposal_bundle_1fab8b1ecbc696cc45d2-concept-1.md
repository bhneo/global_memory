---
id: "concept_action_centered_joint_world_action_model"
type: "concept"
status: "proposal"
title: "动作中心的联合世界—动作模型"
created_at: "2026-07-21T17:41:29+08:00"
updated_at: "2026-07-21T17:41:29+08:00"
aliases: ["Action-Centered Joint World-Action Model", "GigaWorld-Policy-0.5", "动作中心 WAM"]
tags: []
domains: ["embodied-ai", "world-action-model", "vla"]
confidence: "medium"
source_ids: ["source_e2614742b0c3ee7cf985d616"]
relations: [{"type": "derived_from", "target_id": "source_e2614742b0c3ee7cf985d616", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "联合预测架构需要以未来预测质量、闭环控制收益和计算成本分别验收。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
change_reason: "compile bundle from source_e2614742b0c3ee7cf985d616"
reflection_context: {"reflection_ids": ["reflection_aeafd32447e03d5456e70a02"], "importance": "high", "changed_belief": "联合未来视觉损失不能直接视为世界模型能力；必须分别检查动作成功率、预测质量、延迟和自动搜索选择的可复现性。", "surprising": "作者报告六类水果采摘平均成功率 0.85、三项长程任务平均 0.80，以及特定设置下 17.5% 推理加速，但贡献拆分依赖论文内部消融。", "connections": [{"shared_mechanism": "都用未来状态或结果预测约束动作表示。", "boundary": "联合预测损失不等于具有可规划、因果一致的完整世界模型。", "difference": "该工作端到端联合生成动作与视觉；世界模型评测概念要求把预测质量与闭环控制收益分开验证。"}], "open_questions": ["AutoResearch 选出的配方在不同机器人、数据规模和延迟预算下是否稳定？"]}
---

# 动作中心的联合世界—动作模型

GigaWorld-Policy-0.5 以视觉专家和动作专家构成 Mixture-of-Transformers，在因果注意力约束下从当前多视角观察、机器人状态和语言同时预测动作块与未来视觉 token，并配合 KV cache 等推理加速。它提供的是特定系统中联合世界—动作监督与闭环表现的关联证据，不能单凭未来帧损失推断可规划性或因果世界模型能力。
