---
id: "proposal_bundle_8dc4786054e13084e46c"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub"
created_at: "2026-07-17T12:11:31+08:00"
updated_at: "2026-07-17T12:11:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_956ae2aa178f0606fb84f943"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_b34fa19bd2435859f3ce9b90"
input_sha256: "69c5df1853a1c0fce766f6ec5f4f2f17c2f96bd45544c0b203667ac62fe19ec3"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_e65d29cd493432e151cd8b45", "target_path": "vault/knowledge/claims/claim_e65d29cd493432e151cd8b45-来源原文-github---xbotics-embodied-ai-club-xbotics-embodied-ai-job-x.md", "base_sha256": null, "candidate_sha256": "eb7541c08c0f994a4e1df18c36786bc515f273d7d8d9be6df7a563857678abc7", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_8dc4786054e13084e46c-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_e65d29cd493432e151cd8b45.md", "working_at": "2026-07-17T12:11:32+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_956ae2aa178f0606fb84f943"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_b34fa19bd2435859f3ce9b90`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_e65d29cd493432e151cd8b45-来源原文-github---xbotics-embodied-ai-club-xbotics-embodied-ai-job-x.md
@@ -0,0 +1,32 @@
+---
+id: "claim_e65d29cd493432e151cd8b45"
+type: "claim"
+status: "proposal"
+title: "来源原文：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 ·"
+created_at: "2026-07-17T12:11:31+08:00"
+updated_at: "2026-07-17T12:11:31+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_956ae2aa178f0606fb84f943"]
+relations: [{"type": "derived_from", "target_id": "source_956ae2aa178f0606fb84f943", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_956ae2aa178f0606fb84f943"
+evidence: [{"evidence_id": "evidence_fcaa3aec1b47015bb254", "evidence_kind": "quote", "source_id": "source_956ae2aa178f0606fb84f943", "content_id": "content_69c5df1853a1c0fce766f6ec5f4f2f17c2f96bd45544c0b203667ac62fe19ec3", "extraction_id": "extraction_b34fa19bd2435859f3ce9b90", "span_start": 0, "span_end": 87, "original_text": "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "69c5df1853a1c0fce766f6ec5f4f2f17c2f96bd45544c0b203667ac62fe19ec3", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
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
+# 来源原文：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 ·
+
+GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-AI-Job: Xbotics具身智能社区全网工作汇总 · GitHub
```
