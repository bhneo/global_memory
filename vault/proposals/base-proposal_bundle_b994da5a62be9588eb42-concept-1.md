---
id: "concept_d28c0e5c8a5f864e616e2f7a"
type: "concept"
status: "working"
title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
created_at: "2026-07-27T10:47:14+08:00"
updated_at: "2026-07-27T15:06:40+08:00"
aliases: ["全标度三次 NLS 波动动理学导出", "full-range scaling wave kinetic derivation"]
tags: []
domains: ["wave-turbulence", "kinetic-theory"]
confidence: "high"
source_ids: ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e", "source_3c493939fefd8cf6ca2e4ba2"]
relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_3c493939fefd8cf6ca2e4ba2"
reflection_context: {"reflection_ids": ["reflection_2aa4c5bf8a7b1c9211cfb86e"], "importance": "high", "changed_belief": "我会把标度覆盖与时间覆盖视为两条独立的定理维度。", "surprising": "", "connections": [{"shared_mechanism": "大盒--弱非线性协同极限将随机 NLS 二点统计连接到 WKE。", "boundary": "结论限于 d≥3、随机 Schwartz 初值、gamma∈(0,1)及小固定 Tkin 倍数。", "difference": "既有长时结果可至 tau*<taumax；本文主要解决完整标度与图展开收敛。"}], "open_questions": ["覆盖全标度的图相消方法能否与长时迭代结合，而不越过 WKE 的存在边界？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-27T15:06:40+08:00"
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
change_history: [{"change_type": "refine", "previous_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。", "new_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。", "changed_fields": [], "reason": "compile bundle from source_ebf287b4d71ccdc41101466e", "trigger_source": "source_ebf287b4d71ccdc41101466e", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。", "new_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。\n\n## 新增来源材料\n\n- `source_3c493939fefd8cf6ca2e4ba2`：在 d≥3 的任意周期矩形盒上，若三次 NLS 取随机 Schwartz 初值并满足 alpha=L^-gamma（gamma∈(0,1)），Deng 与 Hani 在 L→∞ 时将二点统计与 WKE 的近似严格覆盖到动理学时间 Tkin 的固定小倍数；该结果依赖随机初值、标度和有限窗口，不能替代至 WKE 最大寿命的长时结论。", "changed_fields": [], "reason": "compile bundle from source_3c493939fefd8cf6ca2e4ba2", "trigger_source": "source_3c493939fefd8cf6ca2e4ba2", "evidence_added": []}]
last_consolidation_id: "consolidation_a011c23624aee356ecab9dc4"
---

# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS

对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。

## 新增来源材料

- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。

## 新增来源材料

- `source_3c493939fefd8cf6ca2e4ba2`：在 d≥3 的任意周期矩形盒上，若三次 NLS 取随机 Schwartz 初值并满足 alpha=L^-gamma（gamma∈(0,1)），Deng 与 Hani 在 L→∞ 时将二点统计与 WKE 的近似严格覆盖到动理学时间 Tkin 的固定小倍数；该结果依赖随机初值、标度和有限窗口，不能替代至 WKE 最大寿命的长时结论。
