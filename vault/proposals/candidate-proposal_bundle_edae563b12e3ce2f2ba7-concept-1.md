---
id: "concept_a6e832624a3a4b33fb48980a"
type: "concept"
status: "proposal"
title: "稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann"
created_at: "2026-07-28T10:04:28+08:00"
updated_at: "2026-07-28T10:46:45+08:00"
aliases: ["long-time hard-sphere Boltzmann derivation", "arbitrary fixed time Boltzmann-Grad limit", "长时硬球 Boltzmann 极限", "Hilbert sixth problem hard-sphere scope"]
tags: []
domains: ["kinetic-theory", "boltzmann-equation", "mathematical-physics"]
confidence: "medium"
source_ids: ["source_d15eb994dab1398b83534ed1"]
relations: [{"type": "derived_from", "target_id": "source_d15eb994dab1398b83534ed1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_d15eb994dab1398b83534ed1"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_2feea84cb30c4bceb6d8165f"], "importance": "high", "changed_belief": "我会把本文首先读作对特定硬球模型第一动力学极限的作者主张，而不是已独立确证的普遍“Hilbert 第六问题已解决”事实。", "surprising": "", "connections": [{"shared_mechanism": "本文和既有尺度稳定性 Reflection 都把微观动力学到宏观方程视为需要逐段验证的极限链。", "boundary": "本文限于 Boltzmann--Grad 稀薄硬球、Boltzmann 解存在及 companion work 的流体衔接；既有 Reflection 讨论的是近似闭合的尺度和稳定性边界。", "difference": "本文主张长时硬球动力学到 Boltzmann 的控制；既有来源分析 Boltzmann 到流体近似在波数与稳定性边界内的成立条件。"}], "open_questions": ["companion work 的流体极限如何逐项满足本文硬球极限的条件，且哪些环节已有独立复核？"]}
proposed_status: "working"
---

# 稀薄硬球到非线性 Boltzmann 方程的任意固定时间极限 / arbitrary-fixed-time hard-sphere limit to nonlinear Boltzmann

在 d≥2、论文规定的光滑初值、grand-canonical Boltzmann--Grad 稀薄硬球系综以及 Boltzmann 解存在并满足统一 Maxwellian 型界的条件下，作者证明经验分布在任意预先固定的有限终止时间内收敛到非线性 Boltzmann 方程。若 Boltzmann 解全局存在且保持所需统一界，论文还允许终止时间随 epsilon 以 log|log epsilon| 量级缓慢增长。该结论处理稀薄硬球到 Boltzmann 方程的第一动力学极限；论文所称 Hilbert 第六问题的完整链条还依赖 companion work 中的流体极限，并不能外推到光滑势、任意初值、任意模型或无条件无限时间。
