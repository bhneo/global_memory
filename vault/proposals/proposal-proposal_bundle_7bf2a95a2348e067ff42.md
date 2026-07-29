---
id: "proposal_bundle_7bf2a95a2348e067ff42"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T09:42:50+08:00"
updated_at: "2026-07-27T09:42:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_63ea95cc7031bab39a9b7461"]
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
extraction_id: "extraction_22430e73cf44faa6448251fa"
input_sha256: "9ddedc5dda8ceedecf136e8757443d4fca30d7f56c1c19f640b27b36d397fdb1"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_81828ea915bc741846ff9e5d", "target_path": "vault/knowledge/concepts/concept_81828ea915bc741846ff9e5d-加速观察者的模式依赖粒子内容.md", "base_sha256": null, "candidate_sha256": "68bdecfc392bcc0ed0bbcf7a9d7996f490ff2b05e6c9fdc729cf2dc8cdec04e6", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_7bf2a95a2348e067ff42-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_81828ea915bc741846ff9e5d.md", "working_at": "2026-07-27T09:42:51+08:00"}]
existing_context: [{"id": "input_0b5fbfe5c9ecee3146dadce4", "type": "input", "title": "[gr-qc/0209088] Gravity from Spacetime Thermodynamics", "path": "vault/inputs/input-input_0b5fbfe5c9ecee3146dadce4.md", "status": "active", "source_ids": ["source_ad785f5be8067788394ec708"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/0209088] Gravity from Spacetime Thermodynamics\n\n> 原始内容：[vault/raw/objects/sha256/00…", "match_reason": "metadata:title"}, {"id": "input_72936b45ec8a50ec68020711", "type": "input", "title": "[gr-qc/0602001] Non-equilibrium Thermodynamics of Spacetime", "path": "vault/inputs/input-input_72936b45ec8a50ec68020711.md", "status": "active", "source_ids": ["source_086150581c4c39aee0813d57"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/0602001] Non-equilibrium Thermodynamics of Spacetime\n\n> 原始内容：[vault/raw/objects/sha256…", "match_reason": "metadata:title"}, {"id": "input_bfae3de85b84e499b741f875", "type": "input", "title": "[gr-qc/9307038] Black Hole Entropy is Noether Charge", "path": "vault/inputs/input-input_bfae3de85b84e499b741f875.md", "status": "active", "source_ids": ["source_caf9f433fb4cfb10c6466054"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/9307038] Black Hole Entropy is Noether Charge\n\n> 原始内容：[vault/raw/objects…", "match_reason": "metadata:title"}, {"id": "input_57adc74f55821ba73e81d43f", "type": "input", "title": "[gr-qc/9504004] Thermodynamics of Spacetime: The Einstein Equation of State", "path": "vault/inputs/input-input_57adc74f55821ba73e81d43f.md", "status": "active", "source_ids": ["source_4be2cb176dad6fdd8673bd31"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/9504004] Thermodynamics of Spacetime: The Einstein Equation of State\n\n> 原始内容：[vault…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_63ea95cc7031bab39a9b7461"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "f23b6d6e0c73d0de599632840c505aa84a31b37d07843793cbd8205341117dfa"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_22430e73cf44faa6448251fa`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_81828ea915bc741846ff9e5d-加速观察者的模式依赖粒子内容.md
@@ -0,0 +1,20 @@
+---
+id: "concept_81828ea915bc741846ff9e5d"
+type: "concept"
+status: "proposal"
+title: "加速观察者的模式依赖粒子内容"
+created_at: "2026-07-27T09:42:50+08:00"
+updated_at: "2026-07-27T09:42:50+08:00"
+aliases: ["Unruh effect", "observer-dependent particle content", "Unruh 效应", "观察者依赖的粒子内容"]
+tags: []
+domains: ["quantum-field-theory", "relativity"]
+confidence: "high"
+source_ids: ["source_63ea95cc7031bab39a9b7461"]
+relations: [{"type": "derived_from", "target_id": "source_63ea95cc7031bab39a9b7461", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_63ea95cc7031bab39a9b7461"
+reflection_context: {"reflection_ids": ["reflection_d819c914b8a87f998885a364"], "importance": "high", "changed_belief": "我原先可能把热谱表述为加速本身产生粒子的直观故事；现在更重视它依赖于观察者轨迹、真空态和模式分解之间的关系。", "surprising": "", "connections": [], "open_questions": ["在有限时长或非匀加速探测中，哪些可操作观测量仍可与理想 Rindler 热谱稳健对应？"]}
+---
+
+# 加速观察者的模式依赖粒子内容
+
+Unruh 效应的标准表述比较同一 Minkowski 时空中的两种模式分解：惯性观察者以 Minkowski 正能量模式定义真空与粒子，而均匀加速的 Rindler 观察者以自身时间演化定义正能量模式，并将惯性真空关联为热性 Rindler 粒子分布。该表述适用于理想化的均匀加速、Minkowski 真空和相应探测器/模式框架；它不等同于断言加速在任意实验条件下无条件地产生可直接测得的热粒子。
```
