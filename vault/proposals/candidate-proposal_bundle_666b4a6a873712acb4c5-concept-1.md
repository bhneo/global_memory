---
id: "concept_23e7d830d5080b6725168c6e"
type: "concept"
status: "proposal"
title: "由追加式交互历史约束的可执行程序世界模型"
created_at: "2026-07-26T12:18:26+08:00"
updated_at: "2026-07-26T12:18:26+08:00"
aliases: ["Executable Program World Model Constrained by Append-Only History", "Schema harness", "追加式历史约束的程序世界模型"]
tags: []
domains: ["world-models", "mechanism-discovery", "agent-harness"]
confidence: "medium"
source_ids: ["source_d90b4e9bf278dfc5e68d1bb5"]
relations: [{"type": "derived_from", "target_id": "source_d90b4e9bf278dfc5e68d1bb5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_action_centered_joint_world_action_model", "reason": "两者都联合表达环境演化与动作选择；Schema 使用可读、可重放的离散程序并以完整历史检验，既有概念使用 latent 世界—动作监督且不因此自动获得可规划性。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}]
change_reason: "compile bundle from source_d90b4e9bf278dfc5e68d1bb5"
reflection_context: {"reflection_ids": ["reflection_dc9b1c4fbde4b505081c875b"], "importance": "high", "changed_belief": "此前容易把可执行世界模型理解为只需提供可搜索的 transition function；该来源表明，搜索只对当前表示下的图完备，真正的发现成本在于用区分性实验暴露遗漏对象、状态变量或转移边。", "surprising": "同一 harness 下模型差异主要体现在何时质疑表示并选择区分性实验，而不是最终能否写出同一种规则；但文中接近满分的 Public-set 结果为自报且不能外推到 Semi-private。", "connections": [{"shared_mechanism": "Schema 与 Global Memory 都把不可改写的观察历史和可修订的模型解释分层，并用可重放记录约束后续推理。", "boundary": "该连接适用于需要从交互反例修订显式模型的系统；ARC 的离散、完全可记录环境不等同于开放世界机器人或知识治理。", "difference": "Schema 的程序直接用于 BFS 规划和环境动作；Global Memory 的 Reflection 与 Synthesis 明确不是执行模型，也不能成为 Execution Evidence。"}], "open_questions": ["在连续、部分可观测且含传感噪声的机器人环境中，怎样把精确 backtest 改写为保留不确定性的模型检验而不把误差都归因于规则错误？"]}
---

# 由追加式交互历史约束的可执行程序世界模型

一种机制发现接口可以把当前状态表示、转移规则与目标条件写成可编辑程序，同时把真实观察和已执行动作保存在不可改写的时间线上；候选程序在用于搜索或提交动作前，需要对全部可检查历史重放验证，预测失配则使当前计划失效并触发对状态表示或转移规则的显式修订。该接口只能证明程序与已记录交互的一致性，不能保证未观测状态中的规则正确，也不能把自报的公开基准成绩外推为持出集或现实环境能力。
