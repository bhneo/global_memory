---
id: "proposal_bundle_3b24ac9125b5312ff303"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions"
created_at: "2026-07-27T10:34:38+08:00"
updated_at: "2026-07-27T10:34:39+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_443db75c1157e4ee28fb3ea0"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_68cf6326b6e854fb571fa8e7"
input_sha256: "7a3a0ef7042b710962e0c19389fb9b48d0eb451b43f28b09e7c628a8f73f57af"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_f8a4dfcc3d24b856a7d6335d", "target_path": "vault/knowledge/concepts/concept_f8a4dfcc3d24b856a7d6335d-凸集非集中体积准则-convex-set-non-concentration-volume-criterion.md", "base_sha256": null, "candidate_sha256": "bcc5eea3902bc4786acb9fa42e4fd4d6648b7e9d79e5d31e432fe212ada5585b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3b24ac9125b5312ff303-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md", "working_at": "2026-07-27T10:34:39+08:00"}]
existing_context: [{"id": "input_2157b4467cd4b1295813f202", "type": "input", "title": "[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions", "path": "vault/inputs/input-input_2157b4467cd4b1295813f202.md", "status": "active", "source_ids": ["source_443db75c1157e4ee28fb3ea0"], "snippet": "# [2502.17655] Volume estimates for unions of convex [sets], and the Kakeya set conjecture in three dimensions\n\nInput…", "match_reason": "metadata:title"}, {"id": "input_a541ca45a602bd1db7654686", "type": "input", "title": "[2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities", "path": "vault/inputs/input-input_a541ca45a602bd1db7654686.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# [2411.08871] Restriction [estimates] using decoupling theorems and two-ends Furstenberg inequalities\n\nInput Episode for `source_4ecaaa23ce1d04b17629d3d6`. The…", "match_reason": "metadata:title"}, {"id": "input_696ed17b934899983e8f639c", "type": "input", "title": "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$", "path": "vault/inputs/input-input_696ed17b934899983e8f639c.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "# [1701.07045] Polynomial Wolff axioms and Kakeya-type [estimates] in $\\mathbb{R}^4$\n\nInput Episode for `source_b2c6c3d707b387d0dbad6dbc…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_443db75c1157e4ee28fb3ea0"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "e1721905fcb730c9924cbe96f7bc384bbad089d41f7c1ac7dc878b134e4a3662"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_68cf6326b6e854fb571fa8e7`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_f8a4dfcc3d24b856a7d6335d-凸集非集中体积准则-convex-set-non-concentration-volume-criterion.md
@@ -0,0 +1,20 @@
+---
+id: "concept_f8a4dfcc3d24b856a7d6335d"
+type: "concept"
+status: "proposal"
+title: "凸集非集中体积准则 / convex-set non-concentration volume criterion"
+created_at: "2026-07-27T10:34:38+08:00"
+updated_at: "2026-07-27T10:34:38+08:00"
+aliases: ["convex-set non-concentration", "Kakeya volume estimate", "凸集非集中", "Kakeya 体积估计"]
+tags: []
+domains: ["harmonic-analysis", "geometric-measure-theory", "kakeya"]
+confidence: "medium"
+source_ids: ["source_443db75c1157e4ee28fb3ea0"]
+relations: [{"type": "derived_from", "target_id": "source_443db75c1157e4ee28fb3ea0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2baeb2cc7c9fb6cc84e1614f", "reason": "两者都以近极值管族的几何组织限制 Kakeya 维数；凸集非集中用共同凸集中的管数控制体积，既有概念用近共面与粘连结构描述小体积构型。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_443db75c1157e4ee28fb3ea0"
+reflection_context: {"reflection_ids": ["reflection_2c880abcf8e7c56098a381d4"], "importance": "high", "changed_belief": "我会把 Kakeya 的维数结论与控制管族在凸集内集中程度的中间几何条件一起记录，而不只保留最终维数表述。", "surprising": "", "connections": [{"shared_mechanism": "它与既有近极值 Kakeya 几何结构概念都通过研究小体积或近阈值管族的组织方式来约束维数。", "boundary": "本预印本摘要中的凸集非集中条件及其体积估计需要随论文版本和完整证明一起理解。", "difference": "既有概念强调近共面性和粘连等结构；本文突出的是管族落入共同凸集的计数限制。"}], "open_questions": []}
+---
+
+# 凸集非集中体积准则 / convex-set non-concentration volume criterion
+
+在三维 Kakeya 管族问题中，若一个 delta 管集合满足没有过多管可同时包含于同一凸集的非集中条件，则其管并集可被证明具有近极大的体积。Wang 与 Zahl 的 2025 预印本将这一准则用于宣称三维 Kakeya 集具有满 Minkowski 和 Hausdorff 维数；该概念只描述该论文的条件化证明机制，不把预印本结论提升为无条件的通用分类。
```
