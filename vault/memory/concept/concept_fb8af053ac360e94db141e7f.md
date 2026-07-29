---
id: "concept_fb8af053ac360e94db141e7f"
type: "concept"
status: "working"
title: "Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure"
created_at: "2026-07-27T10:34:05+08:00"
updated_at: "2026-07-27T19:06:58+08:00"
aliases: ["phi-divergence moment closure", "structure-preserving moment closure", "Phi 散度矩闭合", "结构保持矩闭合"]
tags: []
domains: ["kinetic-theory", "boltzmann-equation", "moment-closure"]
confidence: "high"
source_ids: ["source_6c565d5532cc4f2d0020ba4f"]
relations: [{"type": "derived_from", "target_id": "source_6c565d5532cc4f2d0020ba4f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_6c565d5532cc4f2d0020ba4f"
reflection_context: {"reflection_ids": ["reflection_5f9a7c726064e8ba810e25ec"], "importance": "high", "changed_belief": "我原先把矩闭合主要看成用有限矩逼近分布；这里更清楚地看到，闭合的关键取舍是同时保留哪些动力学结构，以及这些结构在何处失效。", "surprising": "", "connections": [{"shared_mechanism": "本论文与既有 Hilbert 第六问题反思都把从 Boltzmann 方程到宏观方程视为受约束的近似构造，而非自动读取的极限。", "boundary": "本文讨论特定 phi-divergence 闭合的结构性质，不证明一般的流体极限或长时间有效性。", "difference": "不变流形反思关注尺度、稳定性与近似层级；本文给出的是有限矩闭合中选择散度和闭合函数的具体机制。"}], "open_questions": []}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-27T19:06:58+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_4690e5dee4dfe74abd3c"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_4690e5dee4dfe74abd3c-concept-1.md"
origin_candidate_sha256: "05abf50175df284ebe073307c502b8960d6cb7efef9d2a1d8faeb1590b96ac86"
origin_cognitive_artifact_sha256: "e1721905fcb730c9924cbe96f7bc384bbad089d41f7c1ac7dc878b134e4a3662"
memory_schema_version: 2
last_consolidation_id: "consolidation_76c8fc502f0ab8e1534a5d7f"
---

# Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure

对 Boltzmann 方程的 phi-divergence 矩闭合以受约束的 phi-divergence 最小化构造近似分布。该框架包含 Grad 型与相对熵型闭合为特例，并以所选散度与近似指数关系来权衡相空间分布的非负性、对称双曲性、可实现性和通量在局部平衡附近的正则性；这些性质仅在论文声明的闭合阶数、碰撞算子和散度耗散条件下讨论。
