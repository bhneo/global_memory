---
id: "concept_fc70bfc09ac7d9473592f09c"
type: "concept"
status: "working"
title: "全身冗余的部分运动学嵌入"
created_at: "2026-07-20T12:39:41+08:00"
updated_at: "2026-07-20T13:37:44+08:00"
aliases: ["Partial kinematic embedding", "PAKE", "Kinematic Normalizing Flow", "全身运动学冗余 Latent"]
tags: []
domains: ["embodied-ai", "whole-body-control", "loco-manipulation", "kinematic-redundancy"]
confidence: "high"
source_ids: ["source_951559714c0383331b1b30ac"]
relations: [{"type": "derived_from", "target_id": "source_951559714c0383331b1b30ac", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "working"}]
change_reason: "compile bundle from source_951559714c0383331b1b30ac"
reflection_context: {"reflection_ids": ["reflection_070e73598e48429fb5eafe01"], "importance": "high", "changed_belief": "全身控制的冗余不必由单一 end-to-end RL 在原始关节空间从头搜索；可以先把运动学可行解分布编码成可导航 latent，再把动力学和稳定性留给低层。", "surprising": "框架把躯干高度、roll、pitch 当作额外手臂自由度来扩大工作空间，同时仍要求底盘速度跟踪，明确利用而非压制浮动基座冗余。", "connections": [{"shared_mechanism": "与 REGRIND 都先构造结构化参考/先验，再用 RL 学习闭环残差或选择。", "boundary": "PAKE 的硬件证据来自带六自由度机械臂的四足平台，8 个任务共 24 回合；不能外推到任意人形、本体或高冲击接触。", "difference": "PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。"}], "open_questions": ["怎样检测目标任务所需解落在 KNF 支持集之外，并安全扩展 reference 分布？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-daily-batch-c-20260720"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-daily-batch-c-20260720"
consolidation_count: 1
last_consolidated_at: "2026-07-20T13:37:44+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_94b5aa1f8680bdf9f780"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_94b5aa1f8680bdf9f780-concept-1.md"
origin_candidate_sha256: "732fb52eb94b16c20b85408ca34112fb468576da8ec3252c172241928d9c4ecf"
memory_schema_version: 2
last_consolidation_id: "consolidation_b8640e036010ed17330d53e8"
---

# 全身冗余的部分运动学嵌入

学习给定末端目标下的可行 partial reference 分布，把全身运动学冗余压缩为高层可导航 latent，再由低层 imitation controller 保证动力学可行执行。它利用浮动基座和躯干自由度扩大工作空间，但支持集受运动学数据覆盖约束。
