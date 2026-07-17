---
id: "proposal_bundle_7b369a05f01115b8bba9"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub"
created_at: "2026-07-17T12:11:33+08:00"
updated_at: "2026-07-17T12:11:33+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a659477a1a8ac8bd6e3c3477"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_68666a9a65711a49a7b4d7c8"
input_sha256: "b24426d2824cc7c2bbb58a3f1cbc718b925001f8c806cf20f66d246d9776f0c5"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_a13acc3bcafaf6b69954a0c9", "target_path": "vault/knowledge/claims/claim_a13acc3bcafaf6b69954a0c9-来源原文-github---wassimtenachi-physo-physical-symbolic-optimization.md", "base_sha256": null, "candidate_sha256": "93cfd722707b3dfa88b86b794d4170a2cdc6fca0db6bac4242a817b39029bdc5", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7b369a05f01115b8bba9-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_a13acc3bcafaf6b69954a0c9.md", "working_at": "2026-07-17T12:11:33+08:00"}]
existing_context: [{"id": "claim_physo_units_constraints_reduce_search_20260716", "type": "claim", "title": "Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间", "path": "vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 在生成过程中施加物理单位约束，以排除单位不一致表达式并缩小搜索空间。", "match_reason": "metadata:tags"}, {"id": "claim_physo_rnn_reinforcement_learning_method_20260716", "type": "claim", "title": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式", "path": "vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。", "match_reason": "metadata:tags"}, {"id": "work_arxiv_2303_03192", "type": "work", "title": "[2303.03192] Deep symbolic regression for physics guided by units constraints: toward the automated discovery of physical laws", "path": "vault/memory/work/work_arxiv_2303_03192.md", "status": "working", "source_ids": ["source_7800c747533d774786595ef7", "source_b85c7e35189fedbd359efa94"], "snippet": "# [2303.03192] Deep [symbolic] regression for physics guided by units constraints: toward the automated discovery of physical laws…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_a659477a1a8ac8bd6e3c3477"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_68666a9a65711a49a7b4d7c8`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_a13acc3bcafaf6b69954a0c9-来源原文-github---wassimtenachi-physo-physical-symbolic-optimization.md
@@ -0,0 +1,32 @@
+---
+id: "claim_a13acc3bcafaf6b69954a0c9"
+type: "claim"
+status: "proposal"
+title: "来源原文：GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub"
+created_at: "2026-07-17T12:11:33+08:00"
+updated_at: "2026-07-17T12:11:33+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_a659477a1a8ac8bd6e3c3477"]
+relations: [{"type": "derived_from", "target_id": "source_a659477a1a8ac8bd6e3c3477", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_a659477a1a8ac8bd6e3c3477"
+evidence: [{"evidence_id": "evidence_fb3547042a960fe13b17", "evidence_kind": "quote", "source_id": "source_a659477a1a8ac8bd6e3c3477", "content_id": "content_b24426d2824cc7c2bbb58a3f1cbc718b925001f8c806cf20f66d246d9776f0c5", "extraction_id": "extraction_68666a9a65711a49a7b4d7c8", "span_start": 0, "span_end": 69, "original_text": "GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "b24426d2824cc7c2bbb58a3f1cbc718b925001f8c806cf20f66d246d9776f0c5", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
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
+# 来源原文：GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub
+
+GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub
```
