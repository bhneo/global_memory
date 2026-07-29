---
id: "proposal_bundle_c78c1e6ca36dcbe59e9a"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T16:14:39+08:00"
updated_at: "2026-07-27T16:14:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_6b6bf6a9d857d2e74c2037ba"]
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
extraction_id: "extraction_c1cd93c35147a994c4a8b981"
input_sha256: "7d16826a2bd22aa9da063f96af8fa9f2ac8b7736d77dbe98450902556707efeb"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_365bbb2a2d0b113d59b474ff", "target_path": "vault/knowledge/concepts/concept_365bbb2a2d0b113d59b474ff-协变熵界以光片而非空间体积限定熵-covariant-entropy-bound-uses-light-sheets-rathe.md", "base_sha256": null, "candidate_sha256": "ac27a4e03882d29258bd39d2f855b34843058b0570025a0b19b0fcdb4e986fd8", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_c78c1e6ca36dcbe59e9a-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_365bbb2a2d0b113d59b474ff.md", "working_at": "2026-07-27T16:14:41+08:00"}]
existing_context: [{"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "# [hep-th/0603001] [Holographic] Derivation of Entanglement Entropy from AdS/CFT\n\nInput Episode for `source_6c0e05be9fc0c544826d7f9b`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_26ade68b0fee058a5e73c9e7", "type": "input", "title": "[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity", "path": "vault/inputs/input-input_26ade68b0fee058a5e73c9e7.md", "status": "active", "source_ids": ["source_7ab41149787a9cd99bd2fe58"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/9711200] The Large N Limit of Superconformal Field Theories and Supergravity…", "match_reason": "metadata:title"}, {"id": "reflection_110c74eddca156c2211ac7cc", "type": "reflection", "title": "全息纠缠第一定律：线性化 AdS 场方程仍受对偶前提约束 / entanglement first law is conditional holographic gravity", "path": "vault/reflections/reflection-reflection_110c74eddca156c2211ac7cc.md", "status": "active", "source_ids": ["source_62c0eb77c44fc70ee44d7233"], "snippet": "# 全息纠缠第一定律：线性化 AdS 场方程仍受对偶前提约束 / entanglement first law is conditional [holographic] gravity\n\n## Why important\n\n该文把球形区域的 CFT 纠缠熵第一定律映射为半经典全息对偶中的线性化引力方程，说明“从纠缠得引力…", "match_reason": "metadata:title"}, {"id": "reflection_60d6cfa7a6c01410932bc897", "type": "reflection", "title": "纠缠第一定律到线性化 AdS：完整约束需要所有球与所有参考系 / entanglement first law needs all balls and frames", "path": "vault/reflections/reflection-reflection_60d6cfa7a6c01410932bc897.md", "status": "active", "source_ids": ["source_8e0a54f1b7764d6c5f111dcb"], "snippet": "…附近的完整线性化 Einstein 方程。\n\n## What changed\n\n我会把“纠缠得引力”的说法限定在 [holographic] CFT、真空附近、球形区域、弱曲率经典对偶和线性阶，并保留所有区域与参考系这一闭合条件。\n\n## Surprising\n\nNot stated.\n\n## Connections…", "match_reason": "full-text:body"}, {"id": "input_b2abca9f2f8c38b0c2f2bdb7", "type": "input", "title": "[1001.0785] On the Origin of Gravity and the Laws of Newton", "path": "vault/inputs/input-input_b2abca9f2f8c38b0c2f2bdb7.md", "status": "active", "source_ids": ["source_35c0773ed4e8dcc92518936e"], "snippet": "# [1001.0785] On the Origin of Gravity and the Laws of Newton\n\nInput Episode for `source_35c0773ed4e8dcc92518936e`. The immutable Source remains authoritative.\n\n# [1001.0785] On the Origin of Gravity and the Laws of Newton\n\n> 原始内容：[vault/ra", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_6b6bf6a9d857d2e74c2037ba"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "35eb58e7dea2ed07580e4f3a01a85d9db150d19e160fe8309dd847921c47b2ba"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_c1cd93c35147a994c4a8b981`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_365bbb2a2d0b113d59b474ff-协变熵界以光片而非空间体积限定熵-covariant-entropy-bound-uses-light-sheets-rathe.md
@@ -0,0 +1,20 @@
+---
+id: "concept_365bbb2a2d0b113d59b474ff"
+type: "concept"
+status: "proposal"
+title: "协变熵界以光片而非空间体积限定熵 / covariant entropy bound uses light-sheets rather than spatial volumes"
+created_at: "2026-07-27T16:14:39+08:00"
+updated_at: "2026-07-27T16:14:39+08:00"
+aliases: ["Bousso 光片熵界", "Bousso light-sheet entropy bound"]
+tags: []
+domains: ["quantum-gravity", "holography", "entropy-bounds"]
+confidence: "high"
+source_ids: ["source_6b6bf6a9d857d2e74c2037ba"]
+relations: [{"type": "derived_from", "target_id": "source_6b6bf6a9d857d2e74c2037ba", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_6b6bf6a9d857d2e74c2037ba"
+reflection_context: {"reflection_ids": ["reflection_ff32987e56b70f3263c6f761"], "importance": "high", "changed_belief": "我会把全息面积缩放限定为带光片选择、几何近似和能量条件限制的协变构造，而不将其表述为任意区域信息量的已证普适定律。", "surprising": "", "connections": [{"shared_mechanism": "两者都将视界或曲面的面积与可访问信息和熵联系起来。", "boundary": "协变熵界选择正交的非膨胀零光片，并在近经典几何与受控能量条件下讨论。", "difference": "局部 Rindler 热力学以局部热流和 Clausius 关系约束场方程；本文以全局光片构造限制与曲面相关的熵。"}], "open_questions": ["量子涨落、负能量和非半经典时空中，应以何种广义熵和量子光片条件替代经典协变界？"]}
+---
+
+# 协变熵界以光片而非空间体积限定熵 / covariant entropy bound uses light-sheets rather than spatial volumes
+
+协变熵界将与给定曲面相关的熵限制在其正交、非膨胀的零光片上，而非任意被该曲面围住的空间体积；该构造在近经典几何、适当能量条件和光片终止规则下提出，不能作为无条件的普适信息容量定律。
```
