---
id: "concept_e69974f653450465afb2aa3e"
type: "concept"
status: "proposal"
title: "失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering"
created_at: "2026-08-02T12:14:39+08:00"
updated_at: "2026-08-02T12:14:39+08:00"
aliases: ["RL2-VLA", "adaptive RL latent compositional steering", "failure-gated test-time VLA scaling", "失败门控 VLA 转向"]
tags: []
domains: ["robotics", "vision-language-action", "reinforcement-learning", "test-time-steering"]
confidence: "high"
source_ids: ["source_e504623270d30d733b2cb9e1"]
relations: [{"type": "derived_from", "target_id": "source_e504623270d30d733b2cb9e1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都冻结 flow 先验并用离线 RL 改变动作分布；RL2-VLA 在推理期组合速度场并由失败门控，RLMM-Flow 在潜变量训练接口中分阶段优化整段动作。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都依赖候选动作评价来保留冻结 VLA 的通用先验；RL2-VLA 额外改变失败态候选分布，动作评估蒸馏主要负责从既有候选中选择。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都用失败信号决定是否干预；RL2-VLA 在动作派发前扩展并选择候选，CheckVLA 在派发后按动作后果偏差修复可部署后缀。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_e504623270d30d733b2cb9e1"
reflection_context: {"reflection_ids": ["reflection_f2923d7702925e8f48787602"], "importance": "high", "changed_belief": "此前容易把 test-time scaling 理解为统一增加候选数量；该论文区分成功态与失败态的相反缩放行为，表明多样性干预需要由失败风险门控，否则会损害已经准确的动作。", "surprising": "论文报告组合转向在失败元组上改善动作误差缩放，却在成功元组上属于最差方法之一；适应性不是附加优化，而是避免转向伤害基础策略的核心边界。", "connections": [{"shared_mechanism": "都冻结基础 flow/VLA 先验，并在小于主干的接口上引入奖励或纠正信号。", "boundary": "RL2-VLA 在推理期组合 VLA 与离线 RL 速度场并依赖失败检测和候选验证；RLMM-Flow 在训练期优化初始潜变量，CheckVLA 在动作派发后检测后果偏差并修复后缀。", "difference": "三者分别改变候选分布、生成潜变量和已提交动作后缀，监督来源与干预时机不可互换。"}], "open_questions": ["失败检测器在新本体、新相机与没有在线失败 rollout 的场景中如何校准，才能避免把门控收益建立在额外任务级数据上？"]}
---

# 失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering

从冻结 VLA 的 action-expert latent 训练轻量离线 RL flow policy，并在推理时对 VLA 与 RL 的速度场做加权组合以生成偏离示范主模态的候选；失败检测器仅在基础策略预计失效时启用组合转向，成功状态退回基础 VLA，最后由外部 verifier 选择动作。该接口把多样性放在失败态而非全时段：论文的 scaling analysis 显示组合转向可改善失败元组，却会扰动已准确的成功元组。它不同于优化初始噪声的 RLMM-Flow，也不同于派发后检测并修复后缀的 CheckVLA。适用性仍受离线数据支持域、失败检测校准、候选 verifier 质量与额外任务级 rollout 需求约束；论文的 SIMPLER、PolaRiS 和 PiperX 结果不能直接推出无校准跨本体泛化。
