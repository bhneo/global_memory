---
id: "proposal_bundle_dc149423c36ffaf926af"
type: "proposal"
status: "migrated"
title: "Compile bundle：[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity"
created_at: "2026-07-27T10:42:44+08:00"
updated_at: "2026-07-27T10:42:45+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7ab41149787a9cd99bd2fe58"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_8bae06f25d952755087315ab"
input_sha256: "0511c7f253575668911d1fdf7f571ddc0ba51395f605f8ebc7efdef384794e86"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_fffdce69b79728a7844d0e69", "target_path": "vault/knowledge/concepts/concept_fffdce69b79728a7844d0e69-大-n-去耦极限中的-ads-cft-对偶-ads-cft-duality-in-the-large-n-decoupling-.md", "base_sha256": null, "candidate_sha256": "d8dda680407f18de84ccbde62b82217162285d10646a17a5bd73df3f255c9ef3", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_dc149423c36ffaf926af-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_fffdce69b79728a7844d0e69.md", "working_at": "2026-07-27T10:42:45+08:00"}]
existing_context: [{"id": "input_26ade68b0fee058a5e73c9e7", "type": "input", "title": "[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity", "path": "vault/inputs/input-input_26ade68b0fee058a5e73c9e7.md", "status": "active", "source_ids": ["source_7ab41149787a9cd99bd2fe58"], "snippet": "# [hep-th/9711200] The Large N Limit of Superconformal [Field] Theories and Supergravity\n\nInput Episode for `source_7ab41149787a9cd99bd2fe58…", "match_reason": "metadata:title"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT\n\n> 原始内容：[vault…", "match_reason": "metadata:title"}, {"id": "input_904a46149f3859dfe84fd1da", "type": "input", "title": "[0903.1254] Entropy density of spacetime and thermodynamic interpretation of field equations of gravity in any diffeomorphism invariant theory", "path": "vault/inputs/input-input_904a46149f3859dfe84fd1da.md", "status": "active", "source_ids": ["source_a7883246b297470ec1c413b8"], "snippet": "# [0903.1254] Entropy density of spacetime and thermodynamic interpretation of [field] equations of gravity in any diffeomorphism invariant…", "match_reason": "metadata:title"}, {"id": "concept_81828ea915bc741846ff9e5d", "type": "concept", "title": "加速观察者的模式依赖粒子内容", "path": "vault/memory/concept/concept_81828ea915bc741846ff9e5d.md", "status": "working", "source_ids": ["source_63ea95cc7031bab39a9b7461"], "snippet": "# 加速观察者的模式依赖粒子内容\n\nUnruh 效应的标准表述比较同一 Minkowski 时空中的两种模式分解：惯性观察者以 Minkowski 正能量模式定义真空与粒子，而均匀加速的 Rindler 观察者以自身时间演化定义正能量模式，并将惯性真空关联为热性 Rindler 粒子分布。该表述适用于理想化的均匀加速、Minkowski 真空和相应探测器/模式框架…", "match_reason": "metadata:domains"}, {"id": "reflection_d819c914b8a87f998885a364", "type": "reflection", "title": "Unruh 综述：粒子内容依赖观测者的模式定义", "path": "vault/reflections/reflection-reflection_d819c914b8a87f998885a364.md", "status": "active", "source_ids": ["source_63ea95cc7031bab39a9b7461"], "snippet": "# Unruh 综述：粒子内容依赖观测者的模式定义\n\n## Why important\n\n这篇综述将 Unruh 效应的核心限定为：均匀加速观察者与惯性观察者采用不同的正能量模式和粒子概念；它避免把“观察者依赖”误简化成对同一局部测量的任意主观解释。\n\n## What changed\n\n我原先可能把热谱表述为加速本身产生粒子的直观故事；现在更重视它依赖于观察者轨迹、真空态和模式分解之间的关系。\n\n## Surprising…", "match_reason": "metadata:domains"}, {"id": "reflection_3e4ed414d26049974df374c2", "type": "reflection", "title": "Wald 熵：从微分同胚对称性导出广义引力熵候选", "path": "vault/reflections/reflection-reflection_3e4ed414d26049974df374c2.md", "status": "active", "source_ids": ["source_d211d7e773bf278ce50a7ac8"], "snippet": "# Wald 熵：从微分同胚对称性导出广义引力熵候选\n\n## Why important\n\nWald 的构造把一般微分同胚不变拉格朗日引力理论中的定常黑洞第一定律，与在分叉 Killing 视界截面上计算的 Noether charge 联系起来；它给出比面积类比更可迁移的条件化定义。\n\n## What changed\n\n我原先容易把黑洞熵只记作面积项；本文使我把面积公式视为特定理论中的结果…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_7ab41149787a9cd99bd2fe58"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "b585c65433a6bca8db5c4f1df558d2ce2cb99124252c5be9a629c81ce3317ae7"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_8bae06f25d952755087315ab`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_fffdce69b79728a7844d0e69-大-n-去耦极限中的-ads-cft-对偶-ads-cft-duality-in-the-large-n-decoupling-.md
@@ -0,0 +1,20 @@
+---
+id: "concept_fffdce69b79728a7844d0e69"
+type: "concept"
+status: "proposal"
+title: "大 N 去耦极限中的 AdS/CFT 对偶 / AdS/CFT duality in the large-N decoupling limit"
+created_at: "2026-07-27T10:42:44+08:00"
+updated_at: "2026-07-27T10:42:44+08:00"
+aliases: ["AdS/CFT correspondence", "gauge/gravity duality", "大 N AdS/CFT 对偶", "规范/引力对偶"]
+tags: []
+domains: ["quantum-gravity", "string-theory", "quantum-field-theory"]
+confidence: "high"
+source_ids: ["source_7ab41149787a9cd99bd2fe58"]
+relations: [{"type": "derived_from", "target_id": "source_7ab41149787a9cd99bd2fe58", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_7ab41149787a9cd99bd2fe58"
+reflection_context: {"reflection_ids": ["reflection_36f58c6bf72d9d492aabd4dd"], "importance": "high", "changed_belief": "我会把 AdS/CFT 记作在明确 large-N、共形点和近地平线条件下提出的对偶框架，而不是无边界的“引力等于量子场论”。", "surprising": "", "connections": [], "open_questions": ["哪些有限 N、有限耦合或非共形形变保留可控的几何对偶描述，哪些只保留形式类比？"]}
+---
+
+# 大 N 去耦极限中的 AdS/CFT 对偶 / AdS/CFT duality in the large-N decoupling limit
+
+Maldacena 的原始 AdS/CFT 提案从某些膜构型的低能去耦极限出发：在 large N 下，近地平线的 AdS、球面及紧致流形几何可由相应超共形场论 Hilbert 空间中的扇区描述。该表述依赖所指定的 large-N、共形点、紧化与近地平线条件；它不是对任意量子场论与任意引力背景的无条件等同。
```
