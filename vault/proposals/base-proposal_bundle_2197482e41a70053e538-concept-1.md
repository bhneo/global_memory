---
id: "concept_d28c0e5c8a5f864e616e2f7a"
type: "concept"
status: "working"
title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
created_at: "2026-07-27T10:47:14+08:00"
updated_at: "2026-07-27T11:18:58+08:00"
aliases: ["rigorous long-time wave-kinetic limit for cubic NLS", "long-time justification of wave turbulence theory", "三次 NLS 长时波动动理学严格极限", "长时波湍流理论严格证明"]
tags: []
domains: ["wave-turbulence", "kinetic-theory", "nonlinear-schrodinger-equation"]
confidence: "high"
source_ids: ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e"]
relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_ebf287b4d71ccdc41101466e"
reflection_context: {"reflection_ids": ["reflection_46d4dcf890fae70ce354f2d4"], "importance": "high", "changed_belief": "我会把三次 NLS 的波动动理学极限理解为可覆盖 WKE 全部存活区间的条件性长时结论，而不是“只要弱非线性就能无限延长”的普适近似。", "surprising": "证明的关键不是把 Duhamel 展开机械追溯到初始时刻：对每个时间层的二点相关应以当前 WKE 谱近似并保留高阶累积量的历史结构，才能消除表面同阶的伪主项。", "connections": [{"shared_mechanism": "它与既有三次 NLS 波动动理学概念都通过大盒与弱非线性协同极限，把随机 NLS 的统计量连接到 WKE。", "boundary": "定理针对 d≥3、随机 Schwartz 初值、α=L^-γ（γ∈(0,1)，端点另有几何条件）且 τ*<τmax；WKE 可有限时爆破，近似不声称跨越该点。", "difference": "既有条目概括早期的固定动理学窗口；本文用分层累积量、正向时间结构与二点相关闭合，将窗口推进至 WKE 的整个存活区间。"}], "open_questions": ["若 WKE 全局有界，τ* 随 L 增长的最优速率是什么；在 WKE 爆破后应以何种弱解或可观测量修改近似？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-27T11:18:58+08:00"
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
change_type: "refine"
proposed_status: "working"
change_history: [{"change_type": "refine", "previous_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。", "new_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。", "changed_fields": [], "reason": "compile bundle from source_ebf287b4d71ccdc41101466e", "trigger_source": "source_ebf287b4d71ccdc41101466e", "evidence_added": []}]
last_consolidation_id: "consolidation_d604a80266cdc304b710d4f4"
---

# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS

对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。

## 新增来源材料

- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。
