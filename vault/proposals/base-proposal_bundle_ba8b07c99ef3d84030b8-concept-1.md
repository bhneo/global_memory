---
id: "concept_f8a4dfcc3d24b856a7d6335d"
type: "concept"
status: "working"
title: "凸集非集中体积准则 / convex-set non-concentration volume criterion"
created_at: "2026-07-27T10:34:38+08:00"
updated_at: "2026-07-27T10:34:39+08:00"
aliases: ["convex-set non-concentration", "Kakeya volume estimate", "凸集非集中", "Kakeya 体积估计"]
tags: []
domains: ["harmonic-analysis", "geometric-measure-theory", "kakeya"]
confidence: "medium"
source_ids: ["source_443db75c1157e4ee28fb3ea0"]
relations: [{"type": "derived_from", "target_id": "source_443db75c1157e4ee28fb3ea0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2baeb2cc7c9fb6cc84e1614f", "reason": "两者都以近极值管族的几何组织限制 Kakeya 维数；凸集非集中用共同凸集中的管数控制体积，既有概念用近共面与粘连结构描述小体积构型。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_443db75c1157e4ee28fb3ea0"
reflection_context: {"reflection_ids": ["reflection_2c880abcf8e7c56098a381d4"], "importance": "high", "changed_belief": "我会把 Kakeya 的维数结论与控制管族在凸集内集中程度的中间几何条件一起记录，而不只保留最终维数表述。", "surprising": "", "connections": [{"shared_mechanism": "它与既有近极值 Kakeya 几何结构概念都通过研究小体积或近阈值管族的组织方式来约束维数。", "boundary": "本预印本摘要中的凸集非集中条件及其体积估计需要随论文版本和完整证明一起理解。", "difference": "既有概念强调近共面性和粘连等结构；本文突出的是管族落入共同凸集的计数限制。"}], "open_questions": []}
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
origin_proposal_id: "proposal_bundle_3b24ac9125b5312ff303"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_3b24ac9125b5312ff303-concept-1.md"
origin_candidate_sha256: "bcc5eea3902bc4786acb9fa42e4fd4d6648b7e9d79e5d31e432fe212ada5585b"
origin_cognitive_artifact_sha256: "e1721905fcb730c9924cbe96f7bc384bbad089d41f7c1ac7dc878b134e4a3662"
memory_schema_version: 2
---

# 凸集非集中体积准则 / convex-set non-concentration volume criterion

在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。
