---
id: "proposal_bundle_63bc57f2fa7fd20f04c2"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence"
created_at: "2026-07-17T12:11:47+08:00"
updated_at: "2026-07-17T12:11:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_deb313c98b03fc4d0b33794a"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_1f11a0062bfea13ba77418dc"
input_sha256: "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_d3c1dc84377e8ab740cf0f2b", "target_path": "vault/knowledge/claims/claim_d3c1dc84377e8ab740cf0f2b-来源原文-2601-03220-from-entropy-to-epiplexity-rethinking-informatio.md", "base_sha256": null, "candidate_sha256": "ac80ce6afe5c10dcbd0dbbc05d47c6f519ee63074f495e45e25922b943900836", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_63bc57f2fa7fd20f04c2-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_d3c1dc84377e8ab740cf0f2b.md", "working_at": "2026-07-17T12:11:48+08:00"}]
existing_context: [{"id": "work_arxiv_2601_03220", "type": "work", "title": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence", "path": "vault/memory/work/work_arxiv_2601_03220.md", "status": "working", "source_ids": ["source_deb313c98b03fc4d0b33794a", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "…Rethinking [Information] for Computationally Bounded Intelligence\n\n## Logical work identity\n\n- arXiv：`2601.03220`\n- Version：`unknown`\n- Captures：`source_deb313c98b03fc4d0b33794a`, `source…", "match_reason": "metadata:title"}, {"id": "claim_wechat_epiplexity_definition_20260715", "type": "claim", "title": "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable", "path": "vault/memory/claim/claim_wechat_epiplexity_definition_20260715.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "For the time-bounded minimum-description-length program P*, the paper defines T-bounded epiplexity S_T(X…", "match_reason": "metadata:tags"}, {"id": "analogy_epiplexity_memory", "type": "analogy", "title": "Epiplexity ↔ 有限上下文记忆压缩", "path": "vault/memory/analogy/analogy_epiplexity_memory.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity] ↔ 有限上下文记忆压缩\n\n共同结构是有限计算预算下保留可复用结构；失效边界是 [Epiplexity] 的正式定义未必直接度量 Agent 记忆效用。", "match_reason": "metadata:title"}, {"id": "concept_epiplexity", "type": "concept", "title": "Epiplexity", "path": "vault/memory/concept/concept_epiplexity.md", "status": "working", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity]\n\n有限计算资源下，观察者能够从数据中提取并复用的结构信息；定义与定理仍需回到原论文核验。", "match_reason": "metadata:title"}, {"id": "hypothesis_epiplexity_memory_compaction", "type": "hypothesis", "title": "Epiplexity 可能帮助评价有限上下文中的记忆压缩", "path": "vault/memory/hypothesis/hypothesis_epiplexity_memory_compaction.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0"], "snippet": "# [Epiplexity] 可能帮助评价有限上下文中的记忆压缩\n\n可复用结构信息或可作为压缩后记忆效用的候选维度，但定义、测量和与任务性能的关系尚未验证。", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_deb313c98b03fc4d0b33794a"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_1f11a0062bfea13ba77418dc`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_d3c1dc84377e8ab740cf0f2b-来源原文-2601-03220-from-entropy-to-epiplexity-rethinking-informatio.md
@@ -0,0 +1,32 @@
+---
+id: "claim_d3c1dc84377e8ab740cf0f2b"
+type: "claim"
+status: "proposal"
+title: "来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa"
+created_at: "2026-07-17T12:11:47+08:00"
+updated_at: "2026-07-17T12:11:47+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_deb313c98b03fc4d0b33794a"]
+relations: [{"type": "derived_from", "target_id": "source_deb313c98b03fc4d0b33794a", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_deb313c98b03fc4d0b33794a"
+evidence: [{"evidence_id": "evidence_c1f2401bf75874bd5ebc", "evidence_kind": "quote", "source_id": "source_deb313c98b03fc4d0b33794a", "content_id": "content_86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09", "extraction_id": "extraction_1f11a0062bfea13ba77418dc", "span_start": 0, "span_end": 104, "original_text": "[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "86024c3a9407b9dfd738a3e6753523d1cd64b802f9b64c9cdf252c3c90b73b09", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: null
+split_reason: null
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 来源原文：[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationa
+
+[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence
```
