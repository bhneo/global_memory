---
id: "concept_f67f822ee20789d74d7b75e3"
type: "concept"
status: "proposal"
title: "物理失败合成驱动的稠密机器人奖励建模"
created_at: "2026-07-20T12:27:36+08:00"
updated_at: "2026-07-20T12:27:36+08:00"
aliases: ["Failure-synthesis dense reward modeling", "DenseReward", "失败感知稠密奖励"]
tags: []
domains: ["embodied-ai", "robot-rl", "reward-modeling", "failure-data"]
confidence: "high"
source_ids: ["source_f9128ff3463cfaa7fa41ee7e"]
relations: [{"type": "derived_from", "target_id": "source_f9128ff3463cfaa7fa41ee7e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "二者都把结果知识压缩为轻量评估接口；一个输出逐时刻进度奖励，另一个输出候选动作的长期 Q 值。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_f9128ff3463cfaa7fa41ee7e"
reflection_context: {"reflection_ids": ["reflection_cb246940931502d077f687f5"], "importance": "high", "changed_belief": "此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。", "surprising": "两帧历史优于一帧，而三帧又略差，提示奖励估计既需要时间上下文，也会受到冗余或噪声历史的影响。", "connections": [{"shared_mechanism": "与 VLA 动作评估蒸馏都学习一个轻量评估信号，为原策略的候选动作或后训练提供长期结果信息。", "boundary": "DenseReward 依赖仿真中的阶段标签和定向扰动，论文只证明其所选操作任务上的奖励预测与下游指导效果；合成失败分布仍可能遗漏真机罕见故障。", "difference": "动作评估蒸馏从仿真树搜索回报学习候选动作 Q 值；DenseReward 从视觉历史和语言预测逐时刻进度，并显式训练多类失败轨迹。"}], "open_questions": ["合成失败与真实失败的分布差异应如何检测，并在策略开始利用奖励漏洞前触发人工或真机校准？"]}
---

# 物理失败合成驱动的稠密机器人奖励建模

通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。
