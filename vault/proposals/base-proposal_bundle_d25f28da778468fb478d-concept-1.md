---
id: "concept_24de3544824d45b83583c5a5"
type: "concept"
status: "working"
title: "全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity"
created_at: "2026-07-28T01:47:06+08:00"
updated_at: "2026-07-28T01:47:07+08:00"
aliases: ["entanglement first law implies linearized Einstein equations", "all balls and Lorentz frames", "纠缠第一律推出线性化 Einstein 方程", "全息纠缠闭合条件"]
tags: []
domains: ["ads-cft", "quantum-gravity", "entanglement"]
confidence: "high"
source_ids: ["source_8e0a54f1b7764d6c5f111dcb"]
relations: [{"type": "derived_from", "target_id": "source_8e0a54f1b7764d6c5f111dcb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}, {"type": "related_to", "target_id": "concept_4e520f39dde022d5e1042625", "reason": "两者都用纠缠的一阶变分约束 Einstein 方程，但本项依赖 AdS/CFT 与 RT，既有节点使用固定体积小测地球的真空纠缠平衡。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_8e0a54f1b7764d6c5f111dcb"
reflection_context: {"reflection_ids": ["reflection_60d6cfa7a6c01410932bc897"], "importance": "high", "changed_belief": "我会把“纠缠得引力”的说法限定在 holographic CFT、真空附近、球形区域、弱曲率经典对偶和线性阶，并保留所有区域与参考系这一闭合条件。", "surprising": "", "connections": [{"shared_mechanism": "两者都把边界纠缠熵的一阶变化映射为 bulk 几何约束。", "boundary": "本文限于 CFT 真空的小扰动、球形区域和具有 Ryu--Takayanagi 面积解释的半经典全息对偶。", "difference": "既有条目强调从纠缠第一律到线性化场方程的条件化推导；本文特别说明任意 Lorentz 参考系为何是获得全部分量的必要条件。"}], "open_questions": ["离开球形区域、线性阶或全息 CFT 后，哪些可观测量仍能支撑对应的引力约束？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "gpt-5.6-sol-high-daily-v2-readmission"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_e7930e6ede16a1c4169f"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_e7930e6ede16a1c4169f-concept-1.md"
origin_candidate_sha256: "f5e2151e5b2ead6c4a96c953f9c8b4a9f4247300b07e2dad8d42eb3a2190b899"
origin_cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
memory_schema_version: 2
---

# 全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity

对具有半经典 AdS 对偶的 CFT 真空的小扰动，将纠缠第一定律应用于所有球形边界区域，并用 RT 面积关系和边界应力张量--渐近度规字典，可得到纯 AdS 附近的线性化 Einstein 方程。只在一个固定 Lorentz 参考系考察所有球时仅获得部分分量；完整方程需要任意参考系。该结论局限于真空附近、球形区域、线性阶和经典全息度规扇区，不能约束所有额外 bulk 场或直接推广到非线性引力。
