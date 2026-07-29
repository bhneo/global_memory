---
id: "concept_d28c0e5c8a5f864e616e2f7a"
type: "concept"
status: "working"
title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
created_at: "2026-07-27T10:47:14+08:00"
updated_at: "2026-07-27T10:47:15+08:00"
aliases: ["wave kinetic equation", "cubic NLS kinetic limit", "波动动理学方程", "三次 NLS 动理学极限"]
tags: []
domains: ["wave-turbulence", "kinetic-theory", "nonlinear-schrodinger-equation"]
confidence: "high"
source_ids: ["source_9ec7a0dfcdc6c43339383f13"]
relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_9ec7a0dfcdc6c43339383f13"
reflection_context: {"reflection_ids": ["reflection_039e793833ff803621c37f30"], "importance": "high", "changed_belief": "我会把波动动理学方程看作与盒尺度、耦合强度和观察时间共同定义的有效描述，而不是任意弱非线性波的普适长时方程。", "surprising": "", "connections": [{"shared_mechanism": "它与 Boltzmann--Grad 涨落层级都通过协同极限将确定性微观或介观演化连接到统计动理学方程。", "boundary": "该结果针对三次 NLS、d≥3、α∼L⁻¹ 和动理学时间的固定倍数。", "difference": "硬球结果依赖粒子低密度与碰撞半径标度；波动结果依赖大盒极限和弱非线性共振结构。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_b43108e78a2a6116b029"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b43108e78a2a6116b029-concept-1.md"
origin_candidate_sha256: "5187efb5f75f79ce8d7758660bf81ea980a482d5f945fe2f2ad3830bb94bd9ac"
origin_cognitive_artifact_sha256: "4451ba8095f3fddeba82a9383e77828628ba8be1be6dd8738784909274a4c30c"
memory_schema_version: 2
---

# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS

对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。
