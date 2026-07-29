---
id: "concept_cdbe55276db1fb0eb0aa370a"
type: "concept"
status: "proposal"
title: "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere equilibrium fluctuations"
created_at: "2026-07-27T10:43:06+08:00"
updated_at: "2026-07-27T17:04:23+08:00"
aliases: ["硬球涨落的全高斯长时极限", "full Gaussian long-time limit for hard-sphere fluctuations"]
tags: []
domains: ["kinetic-theory", "boltzmann", "statistical-mechanics"]
confidence: "high"
source_ids: ["source_3851b9ffbfbae3ca166308fd", "source_323f116c3573f26f4af7785d"]
relations: [{"type": "derived_from", "target_id": "source_3851b9ffbfbae3ca166308fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_323f116c3573f26f4af7785d"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_3231f184af64cbede55c5e55"], "importance": "high", "changed_belief": "我会把全时结果限定为平衡、低密度和涨落过程，而不外推为任意初值下非线性 Boltzmann 方程的全时严格导出。", "surprising": "", "connections": [{"shared_mechanism": "两者都以低密度硬球碰撞与再碰撞控制把微观动力学连接到有效动理学。", "boundary": "本文限于平衡 Boltzmann--Grad 缩放、任意长动力学时间和高斯涨落过程。", "difference": "既有对象只记录伴随工作中的全时协方差控制；本文以高阶矩证明完整涨落过程的高斯极限。"}], "open_questions": ["能否在可量化的非平衡初值范围内获得同样的长时完整涨落过程，而非仅协方差或短时结果？"]}
proposed_status: "working"
---

# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere fluctuations

对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann 方程控制。该结果处理的是二阶相关与线性化动力学，不能替代任意初值下非线性 Boltzmann 方程的全时严格导出。

## 新增来源材料

- `source_323f116c3573f26f4af7785d`：在平衡 Boltzmann--Grad 极限的硬球气体中，经验测度的适当缩放涨落过程可在任意长动力学时间收敛为由线性化 Boltzmann 碰撞算子和时空白高斯噪声驱动的高斯过程；这延伸全时协方差控制，但不推出任意初值下非线性 Boltzmann 方程的全时严格导出。
