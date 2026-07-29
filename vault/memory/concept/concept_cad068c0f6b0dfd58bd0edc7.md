---
id: "concept_cad068c0f6b0dfd58bd0edc7"
type: "concept"
status: "working"
title: "静态 AdS/CFT 的 Ryu--Takayanagi 极小面处方 / Ryu--Takayanagi minimal-surface prescription in static AdS/CFT"
created_at: "2026-07-28T01:46:26+08:00"
updated_at: "2026-07-28T16:33:56+08:00"
aliases: ["Ryu--Takayanagi formula", "RT formula", "全息纠缠熵极小面处方", "RT 极小面公式"]
tags: []
domains: ["ads-cft", "entanglement", "quantum-gravity"]
confidence: "high"
source_ids: ["source_13265cd7e3182e8896b41a2a"]
relations: [{"type": "derived_from", "target_id": "source_13265cd7e3182e8896b41a2a", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}, {"type": "depends_on", "target_id": "concept_fffdce69b79728a7844d0e69", "reason": "RT 处方依赖受 large-N、去耦和半经典几何条件约束的 AdS/CFT 对偶框架。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_13265cd7e3182e8896b41a2a"
reflection_context: {"reflection_ids": ["reflection_084289f7f003434aaf525dca"], "importance": "high", "changed_belief": "我会将 RT 公式限定为静态半经典 AdS/CFT 处方，并区分其对 2D CFT 的检验、对特定 N=4 SYM 情形的比较与一般动态情形。", "surprising": "", "connections": [{"shared_mechanism": "两者都将边界子系统的纠缠量映射为 bulk 中由边界锚定的几何面积。", "boundary": "本文的原始处方处理静态极小面及 AdS/CFT 中的 CFT 区域。", "difference": "既有纠缠第一律条目从 RT 面积解释推出线性化动力学约束；本文给出该面积处方本身及其静态适用边界。"}], "open_questions": ["在时间依赖或量子修正显著的情形，何种广义熵和极值面条件取代静态极小面公式？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "gpt-5.6-sol-high-daily-v2-readmission"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
consolidation_count: 1
last_consolidated_at: "2026-07-28T16:33:56+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_d1efa8e505643c29cc0b"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_d1efa8e505643c29cc0b-concept-1.md"
origin_candidate_sha256: "a991b2e6d3b412218641f4895d92575592eded16f39434843dee341adfb7c318"
origin_cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
memory_schema_version: 2
last_consolidation_id: "consolidation_19896aff57ed01c088be5a19"
---

# 静态 AdS/CFT 的 Ryu--Takayanagi 极小面处方 / Ryu--Takayanagi minimal-surface prescription in static AdS/CFT

在具有半经典引力对偶的静态 AdS/CFT 设置中，边界 CFT 空间区域 A 的纠缠熵由锚定于 A 的边界且与 A 同调的 bulk 极小曲面面积除以 4G_N 给出。原始工作在 AdS3/CFT2 中复现已知结果，并在 AdS5×S5 与自由 N=4 SYM 之间作比较；该处方不能无条件外推到时间依赖背景或量子引力修正显著的区域。
