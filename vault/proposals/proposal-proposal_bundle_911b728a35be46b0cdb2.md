---
id: "proposal_bundle_911b728a35be46b0cdb2"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-17T12:15:10+08:00"
updated_at: "2026-07-17T12:15:10+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_1c0f944bf6b14cf9d1fff939"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_c970040f818d88a47cff99b3"
input_sha256: "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_ad8c28d32a7d55ab2806574d", "target_path": "vault/knowledge/claims/claim_ad8c28d32a7d55ab2806574d-from-entropy-to-epiplexity-rethinking-information-for-computatio.md", "base_sha256": null, "candidate_sha256": "a3a647d0dad2ab9caec8747f104ad154c447cb4972af02371dfbd58b38ae4dcd", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_911b728a35be46b0cdb2-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_ad8c28d32a7d55ab2806574d.md", "working_at": "2026-07-17T12:15:10+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_c7f06719c78cc576410dded2", "target_path": "vault/knowledge/claims/claim_c7f06719c78cc576410dded2-useful-information-be-constructed-from-merely-applying-determini.md", "base_sha256": null, "candidate_sha256": "120790b364170dd0f003d2cd0cff65a2893153dc0633b94556ea956cd84513c3", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_911b728a35be46b0cdb2-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_c7f06719c78cc576410dded2.md", "working_at": "2026-07-17T12:15:10+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…Speaker consistency, is a normalized\nscore∈ [0,1] which assesses the [entropy] ofp(ak|mk) and\n(a) Cleanup…", "match_reason": "full-text:body"}, {"id": "work_arxiv_2601_03220", "type": "work", "title": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence", "path": "vault/memory/work/work_arxiv_2601_03220.md", "status": "working", "source_ids": ["source_deb313c98b03fc4d0b33794a", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "# From Entropy to Epiplexity: [Rethinking] Information for Computationally Bounded Intelligence\n\n## Logical work identity\n\n- arXiv：`2601.03220`\n- Version：`unknown…", "match_reason": "metadata:title"}, {"id": "claim_d3c1dc84377e8ab740cf0f2b", "type": "claim", "title": "来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa", "path": "vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md", "status": "working", "source_ids": ["source_deb313c98b03fc4d0b33794a"], "snippet": "…Entropy to Epiplexity: [Rethinking] Information for Computationa\n\n[2601.03220] From Entropy to Epiplexity: [Rethinking] Information for Computationally Bounded…", "match_reason": "metadata:title"}, {"id": "claim_wechat_epiplexity_definition_20260715", "type": "claim", "title": "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable", "path": "vault/memory/claim/claim_wechat_epiplexity_definition_20260715.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "For the time-bounded minimum-description-length program P*, the paper defines T-bounded [epiplexity] S_T(X…", "match_reason": "metadata:title"}, {"id": "analogy_epiplexity_memory", "type": "analogy", "title": "Epiplexity ↔ 有限上下文记忆压缩", "path": "vault/memory/analogy/analogy_epiplexity_memory.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity] ↔ 有限上下文记忆压缩\n\n共同结构是有限计算预算下保留可复用结构；失效边界是 [Epiplexity] 的正式定义未必直接度量 Agent 记忆效用。", "match_reason": "metadata:title"}, {"id": "concept_epiplexity", "type": "concept", "title": "Epiplexity", "path": "vault/memory/concept/concept_epiplexity.md", "status": "working", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity]\n\n有限计算资源下，观察者能够从数据中提取并复用的结构信息；定义与定理仍需回到原论文核验。", "match_reason": "metadata:title"}, {"id": "hypothesis_epiplexity_memory_compaction", "type": "hypothesis", "title": "Epiplexity 可能帮助评价有限上下文中的记忆压缩", "path": "vault/memory/hypothesis/hypothesis_epiplexity_memory_compaction.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity] 可能帮助评价有限上下文中的记忆压缩\n\n可复用结构信息或可作为压缩后记忆效用的候选维度，但定义、测量和与任务性能的关系尚未验证。", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_1c0f944bf6b14cf9d1fff939"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 2, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 2, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_c970040f818d88a47cff99b3`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_ad8c28d32a7d55ab2806574d-from-entropy-to-epiplexity-rethinking-information-for-computatio.md
@@ -0,0 +1,32 @@
+---
+id: "claim_ad8c28d32a7d55ab2806574d"
+type: "claim"
+status: "proposal"
+title: "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kol"
+created_at: "2026-07-17T12:15:10+08:00"
+updated_at: "2026-07-17T12:15:10+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_1c0f944bf6b14cf9d1fff939"]
+relations: [{"type": "derived_from", "target_id": "source_1c0f944bf6b14cf9d1fff939", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_1c0f944bf6b14cf9d1fff939"
+evidence: [{"evidence_id": "evidence_21e8c945846dd77a8e9c", "evidence_kind": "paraphrase", "source_id": "source_1c0f944bf6b14cf9d1fff939", "content_id": "content_8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extraction_id": "extraction_c970040f818d88a47cff99b3", "span_start": -1, "span_end": 326, "original_text": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kolter1 Andrew Gordon Wilson2 1Carnegie Mellon University 2New York University Abstract Can we learn more from data than existed in the generating process itself? Can new", "interpretation": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kolter1 Andrew Gordon Wilson2 1Carnegie Mellon University 2New York University Abstract Can we learn more from data than existed in the generating process itself? Can new", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "From Entropy to Epiplexity: Rethinking Information for\nComputationally Bounded Intelligence\nMarc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kolter1\nAndrew Gordon Wilson2\n1Carnegie Mellon University 2New York University\nAbstract\nCan we learn more from data than existed in the generating process itself? Can new and useful\ninformation be constructed from merely applying deterministic transformations to existing data?\nCan the learnable content in data be evaluated without considerin"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kol
+
+From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kolter1 Andrew Gordon Wilson2 1Carnegie Mellon University 2New York University Abstract Can we learn more from data than existed in the generating process itself? Can new
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_c7f06719c78cc576410dded2-useful-information-be-constructed-from-merely-applying-determini.md
@@ -0,0 +1,32 @@
+---
+id: "claim_c7f06719c78cc576410dded2"
+type: "claim"
+status: "proposal"
+title: "useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without co"
+created_at: "2026-07-17T12:15:10+08:00"
+updated_at: "2026-07-17T12:15:10+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_1c0f944bf6b14cf9d1fff939"]
+relations: [{"type": "derived_from", "target_id": "source_1c0f944bf6b14cf9d1fff939", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_1c0f944bf6b14cf9d1fff939"
+evidence: [{"evidence_id": "evidence_ca620df6bf1f6237413f", "evidence_kind": "paraphrase", "source_id": "source_1c0f944bf6b14cf9d1fff939", "content_id": "content_8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extraction_id": "extraction_c970040f818d88a47cff99b3", "span_start": -1, "span_end": 167, "original_text": "useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without considerin", "interpretation": "useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without considerin", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "From Entropy to Epiplexity: Rethinking Information for\nComputationally Bounded Intelligence\nMarc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kolter1\nAndrew Gordon Wilson2\n1Carnegie Mellon University 2New York University\nAbstract\nCan we learn more from data than existed in the generating process itself? Can new and useful\ninformation be constructed from merely applying deterministic transformations to existing data?\nCan the learnable content in data be evaluated without considerin"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without co
+
+useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without considerin
```
