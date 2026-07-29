---
id: "proposal_bundle_ba8b07c99ef3d84030b8"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T15:05:17+08:00"
updated_at: "2026-07-27T15:05:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cf15e6b90aaf4c6584d5efe2"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_615e75f5fb25c79e6de30855"
input_sha256: "631e8b2118e3d03ded2d5fe79f9acdf74353877d143e9887a3c31278cd13ed01"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_f8a4dfcc3d24b856a7d6335d", "target_path": "vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md", "base_sha256": "b9ae03e25b04646752d2a770a5a265b637692fc818813350d135f1e2cc6a0c9e", "candidate_sha256": "db37f65c396de328e32e72ea66ab211e1eb1589ee641b0c803232e6e3f68dcce", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_ba8b07c99ef3d84030b8-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_ba8b07c99ef3d84030b8-concept-1.md", "working_path": "vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-27T15:05:57+08:00"}]
existing_context: [{"id": "concept_f8a4dfcc3d24b856a7d6335d", "type": "concept", "title": "凸集非集中体积准则 / convex-set non-concentration volume criterion", "path": "vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md", "status": "working", "source_ids": ["source_443db75c1157e4ee28fb3ea0"], "snippet": "# 凸集非集中体积准则 / [convex]-set non-concentration volume criterion\n\n在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的…", "match_reason": "metadata:title"}, {"id": "input_2157b4467cd4b1295813f202", "type": "input", "title": "[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions", "path": "vault/inputs/input-input_2157b4467cd4b1295813f202.md", "status": "active", "source_ids": ["source_443db75c1157e4ee28fb3ea0"], "snippet": "# [2502.17655] Volume estimates for unions of [convex] sets, and the Kakeya set conjecture in three dimensions\n\nInput…", "match_reason": "metadata:title"}, {"id": "input_a541ca45a602bd1db7654686", "type": "input", "title": "[2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities", "path": "vault/inputs/input-input_a541ca45a602bd1db7654686.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# [2411.08871] Restriction [estimates] using decoupling theorems and two-ends Furstenberg inequalities\n\nInput Episode for `source_4ecaaa23ce1d04b17629d3d6`. The…", "match_reason": "metadata:title"}, {"id": "input_696ed17b934899983e8f639c", "type": "input", "title": "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$", "path": "vault/inputs/input-input_696ed17b934899983e8f639c.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "# [1701.07045] Polynomial Wolff axioms and Kakeya-type [estimates] in $\\mathbb{R}^4$\n\nInput Episode for `source_b2c6c3d707b387d0dbad6dbc…", "match_reason": "metadata:title"}, {"id": "concept_0ea689b9ff94e453dd23b64b", "type": "concept", "title": "三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3", "path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "status": "working", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "…估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence [estimates] 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_cf15e6b90aaf4c6584d5efe2"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "173530db46f12e1188d5d797dd896ba02254838a63916c49e7ae0ec450189e65"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_615e75f5fb25c79e6de30855`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md
+++ candidate:vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_f8a4dfcc3d24b856a7d6335d"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "凸集非集中体积准则 / convex-set non-concentration volume criterion"
 created_at: "2026-07-27T10:34:38+08:00"
-updated_at: "2026-07-27T10:34:39+08:00"
-aliases: ["convex-set non-concentration", "Kakeya volume estimate", "凸集非集中", "Kakeya 体积估计"]
+updated_at: "2026-07-27T15:05:17+08:00"
+aliases: ["三维 Kakeya 凸集非集中体积估计", "convex Wolff non-concentration for R3 Kakeya"]
 tags: []
-domains: ["harmonic-analysis", "geometric-measure-theory", "kakeya"]
-confidence: "medium"
-source_ids: ["source_443db75c1157e4ee28fb3ea0"]
+domains: ["harmonic-analysis", "kakeya"]
+confidence: "high"
+source_ids: ["source_443db75c1157e4ee28fb3ea0", "source_cf15e6b90aaf4c6584d5efe2"]
 relations: [{"type": "derived_from", "target_id": "source_443db75c1157e4ee28fb3ea0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_2baeb2cc7c9fb6cc84e1614f", "reason": "两者都以近极值管族的几何组织限制 Kakeya 维数；凸集非集中用共同凸集中的管数控制体积，既有概念用近共面与粘连结构描述小体积构型。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_443db75c1157e4ee28fb3ea0"
-reflection_context: {"reflection_ids": ["reflection_2c880abcf8e7c56098a381d4"], "importance": "high", "changed_belief": "我会把 Kakeya 的维数结论与控制管族在凸集内集中程度的中间几何条件一起记录，而不只保留最终维数表述。", "surprising": "", "connections": [{"shared_mechanism": "它与既有近极值 Kakeya 几何结构概念都通过研究小体积或近阈值管族的组织方式来约束维数。", "boundary": "本预印本摘要中的凸集非集中条件及其体积估计需要随论文版本和完整证明一起理解。", "difference": "既有概念强调近共面性和粘连等结构；本文突出的是管族落入共同凸集的计数限制。"}], "open_questions": []}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_3b24ac9125b5312ff303"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_3b24ac9125b5312ff303-concept-1.md"
-origin_candidate_sha256: "bcc5eea3902bc4786acb9fa42e4fd4d6648b7e9d79e5d31e432fe212ada5585b"
-origin_cognitive_artifact_sha256: "e1721905fcb730c9924cbe96f7bc384bbad089d41f7c1ac7dc878b134e4a3662"
-memory_schema_version: 2
+change_reason: "compile bundle from source_cf15e6b90aaf4c6584d5efe2"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_539106049b68b9810702fe73"], "importance": "high", "changed_belief": "我不会把“R3 Kakeya 集满维”的预印本结论误读为 R3 Kakeya maximal function conjecture 已解决。", "surprising": "", "connections": [{"shared_mechanism": "凸或板状非集中条件都限制高重叠管族并导出体积下界。", "boundary": "本文为预印本，定理针对 delta-tube、shading、Wolff 条件及 epsilon/K 常数。", "difference": "旧概念仅记录摘要级凸集准则；本文增加 D/E 自改进、多尺度 sticky 机制及最大函数仍未解的边界。"}], "open_questions": ["能否将所需非集中条件强化到 K=3，从而处理 R3 Kakeya 最大函数猜想？"]}
+proposed_status: "working"
 ---
 
 # 凸集非集中体积准则 / convex-set non-concentration volume criterion
 
 在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。
+
+## 新增来源材料
+
+- `source_cf15e6b90aaf4c6584d5efe2`：对 R3 中满足 Katz--Tao convex 与 Frostman slab Wolff 非集中条件的 delta 管族，Wang 与 Zahl 以 D/E 型体积估计的自改进、多尺度 grains 分解和 sticky-like 结构控制管并集体积，并据此推出每个 R3 Kakeya 集的 Minkowski 与 Hausdorff 维数为 3。该预印本结论不解决 R3 Kakeya maximal-function conjecture 的 K=3 情形。
```
