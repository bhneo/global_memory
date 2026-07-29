---
id: "concept_f8a4dfcc3d24b856a7d6335d"
type: "concept"
status: "working"
title: "凸集非集中体积准则 / convex-set non-concentration volume criterion"
created_at: "2026-07-27T10:34:38+08:00"
updated_at: "2026-07-27T15:05:35+08:00"
aliases: ["三维 Kakeya 凸集非集中体积估计", "convex Wolff non-concentration for R3 Kakeya"]
tags: []
domains: ["harmonic-analysis", "kakeya"]
confidence: "high"
source_ids: ["source_443db75c1157e4ee28fb3ea0", "source_cf15e6b90aaf4c6584d5efe2"]
relations: [{"type": "derived_from", "target_id": "source_443db75c1157e4ee28fb3ea0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2baeb2cc7c9fb6cc84e1614f", "reason": "两者都以近极值管族的几何组织限制 Kakeya 维数；凸集非集中用共同凸集中的管数控制体积，既有概念用近共面与粘连结构描述小体积构型。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_cf15e6b90aaf4c6584d5efe2"
reflection_context: {"reflection_ids": ["reflection_539106049b68b9810702fe73"], "importance": "high", "changed_belief": "我不会把“R3 Kakeya 集满维”的预印本结论误读为 R3 Kakeya maximal function conjecture 已解决。", "surprising": "", "connections": [{"shared_mechanism": "凸或板状非集中条件都限制高重叠管族并导出体积下界。", "boundary": "本文为预印本，定理针对 delta-tube、shading、Wolff 条件及 epsilon/K 常数。", "difference": "旧概念仅记录摘要级凸集准则；本文增加 D/E 自改进、多尺度 sticky 机制及最大函数仍未解的边界。"}], "open_questions": ["能否将所需非集中条件强化到 K=3，从而处理 R3 Kakeya 最大函数猜想？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-27T15:05:35+08:00"
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
change_type: "refine"
proposed_status: "working"
change_history: [{"change_type": "refine", "previous_statement": "# 凸集非集中体积准则 / convex-set non-concentration volume criterion\n\n在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。", "new_statement": "# 凸集非集中体积准则 / convex-set non-concentration volume criterion\n\n在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。\n\n## 新增来源材料\n\n- `source_cf15e6b90aaf4c6584d5efe2`：对 R3 中满足 Katz--Tao convex 与 Frostman slab Wolff 非集中条件的 delta 管族，Wang 与 Zahl 以 D/E 型体积估计的自改进、多尺度 grains 分解和 sticky-like 结构控制管并集体积，并据此推出每个 R3 Kakeya 集的 Minkowski 与 Hausdorff 维数为 3。该预印本结论不解决 R3 Kakeya maximal-function conjecture 的 K=3 情形。", "changed_fields": [], "reason": "compile bundle from source_cf15e6b90aaf4c6584d5efe2", "trigger_source": "source_cf15e6b90aaf4c6584d5efe2", "evidence_added": []}]
last_consolidation_id: "consolidation_a80c0fb2c0265f440729a1eb"
---

# 凸集非集中体积准则 / convex-set non-concentration volume criterion

在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。

## 新增来源材料

- `source_cf15e6b90aaf4c6584d5efe2`：对 R3 中满足 Katz--Tao convex 与 Frostman slab Wolff 非集中条件的 delta 管族，Wang 与 Zahl 以 D/E 型体积估计的自改进、多尺度 grains 分解和 sticky-like 结构控制管并集体积，并据此推出每个 R3 Kakeya 集的 Minkowski 与 Hausdorff 维数为 3。该预印本结论不解决 R3 Kakeya maximal-function conjecture 的 K=3 情形。
