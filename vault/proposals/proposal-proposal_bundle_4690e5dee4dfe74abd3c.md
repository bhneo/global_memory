---
id: "proposal_bundle_4690e5dee4dfe74abd3c"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T10:34:05+08:00"
updated_at: "2026-07-27T10:34:07+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_6c565d5532cc4f2d0020ba4f"]
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
extraction_id: "extraction_cc4b5ede68490d6b7f2714d9"
input_sha256: "4dbe577594e8fcbbca51d8ec391b122c7e3f0cf52e36e2963737339fcf23bd10"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_fb8af053ac360e94db141e7f", "target_path": "vault/knowledge/concepts/concept_fb8af053ac360e94db141e7f-phi-divergence-结构保持矩闭合-phi-divergence-structure-preserving-momen.md", "base_sha256": null, "candidate_sha256": "05abf50175df284ebe073307c502b8960d6cb7efef9d2a1d8faeb1590b96ac86", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_4690e5dee4dfe74abd3c-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_fb8af053ac360e94db141e7f.md", "working_at": "2026-07-27T10:34:07+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_6c565d5532cc4f2d0020ba4f"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "e1721905fcb730c9924cbe96f7bc384bbad089d41f7c1ac7dc878b134e4a3662"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_cc4b5ede68490d6b7f2714d9`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_fb8af053ac360e94db141e7f-phi-divergence-结构保持矩闭合-phi-divergence-structure-preserving-momen.md
@@ -0,0 +1,20 @@
+---
+id: "concept_fb8af053ac360e94db141e7f"
+type: "concept"
+status: "proposal"
+title: "Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure"
+created_at: "2026-07-27T10:34:05+08:00"
+updated_at: "2026-07-27T10:34:05+08:00"
+aliases: ["phi-divergence moment closure", "structure-preserving moment closure", "Phi 散度矩闭合", "结构保持矩闭合"]
+tags: []
+domains: ["kinetic-theory", "boltzmann-equation", "moment-closure"]
+confidence: "high"
+source_ids: ["source_6c565d5532cc4f2d0020ba4f"]
+relations: [{"type": "derived_from", "target_id": "source_6c565d5532cc4f2d0020ba4f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_6c565d5532cc4f2d0020ba4f"
+reflection_context: {"reflection_ids": ["reflection_5f9a7c726064e8ba810e25ec"], "importance": "high", "changed_belief": "我原先把矩闭合主要看成用有限矩逼近分布；这里更清楚地看到，闭合的关键取舍是同时保留哪些动力学结构，以及这些结构在何处失效。", "surprising": "", "connections": [{"shared_mechanism": "本论文与既有 Hilbert 第六问题反思都把从 Boltzmann 方程到宏观方程视为受约束的近似构造，而非自动读取的极限。", "boundary": "本文讨论特定 phi-divergence 闭合的结构性质，不证明一般的流体极限或长时间有效性。", "difference": "不变流形反思关注尺度、稳定性与近似层级；本文给出的是有限矩闭合中选择散度和闭合函数的具体机制。"}], "open_questions": []}
+---
+
+# Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure
+
+对 Boltzmann 方程的 phi-divergence 矩闭合以受约束的 phi-divergence 最小化构造近似分布。该框架包含 Grad 型与相对熵型闭合为特例，并以所选散度与近似指数关系来权衡相空间分布的非负性、对称双曲性、可实现性和通量在局部平衡附近的正则性；这些性质仅在论文声明的闭合阶数、碰撞算子和散度耗散条件下讨论。
```
