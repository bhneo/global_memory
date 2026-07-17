---
id: "proposal_bundle_7e9e9ea5035dd1e5ce4e"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-17T12:17:07+08:00"
updated_at: "2026-07-17T12:17:07+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b85c7e35189fedbd359efa94"]
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
extraction_id: "extraction_f7743ab92a554c94f10a12cd"
input_sha256: "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_b035b6de75ccf5819d0e89fa", "target_path": "vault/knowledge/claims/claim_b035b6de75ccf5819d0e89fa-draft-version-october-10-2023-typeset-using-latex-twocolumn-styl.md", "base_sha256": null, "candidate_sha256": "546ff9225184643c50c2985466be9f6c12b0109d42965814f9f4063863536695", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7e9e9ea5035dd1e5ce4e-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_b035b6de75ccf5819d0e89fa.md", "working_at": "2026-07-17T12:17:07+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_a78ba4a2ebc88876f4393ad0", "target_path": "vault/knowledge/claims/claim_a78ba4a2ebc88876f4393ad0-foivos-i-diakogiannis-2-1universit-e-de-strasbourg-cnrs-observat.md", "base_sha256": null, "candidate_sha256": "39c5426a02c2e2f199929125279ef8676b6eebcbd542e3cdc8dd71e3be7cdf36", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7e9e9ea5035dd1e5ce4e-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_a78ba4a2ebc88876f4393ad0.md", "working_at": "2026-07-17T12:17:07+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_45e2c33254979ebece6a7502", "target_path": "vault/knowledge/claims/claim_45e2c33254979ebece6a7502-revised-october-06-2023.md", "base_sha256": null, "candidate_sha256": "2e855709c39debb8460b01bd13393ebdd3980939b52a9e10b6353f7e1c3b6237", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7e9e9ea5035dd1e5ce4e-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_45e2c33254979ebece6a7502.md", "working_at": "2026-07-17T12:17:07+08:00"}, {"item_id": "claim-4", "object_type": "claim", "action": "create", "target_id": "claim_54cac5c21565eb6d274a5383", "target_path": "vault/knowledge/claims/claim_54cac5c21565eb6d274a5383-accepted-october-06-2023-s.md", "base_sha256": null, "candidate_sha256": "e8a46b19cf4b4e3ccff1797e0446a83a81d53018ca56f8307d2f3f78f3117b70", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7e9e9ea5035dd1e5ce4e-claim-4.md", "base_path": null, "working_path": "vault/memory/claim/claim_54cac5c21565eb6d274a5383.md", "working_at": "2026-07-17T12:17:07+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 4, "source_id": "source_b85c7e35189fedbd359efa94"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 4, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 4, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_f7743ab92a554c94f10a12cd`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_b035b6de75ccf5819d0e89fa-draft-version-october-10-2023-typeset-using-latex-twocolumn-styl.md
@@ -0,0 +1,32 @@
+---
+id: "claim_b035b6de75ccf5819d0e89fa"
+type: "claim"
+status: "proposal"
+title: "Draft version October 10, 2023 Typeset using LATEX twocolumn style in AASTeX63 Deep symbolic regression for physics guided by units constraints: toward the auto"
+created_at: "2026-07-17T12:17:07+08:00"
+updated_at: "2026-07-17T12:17:07+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b85c7e35189fedbd359efa94"]
+relations: [{"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b85c7e35189fedbd359efa94"
+evidence: [{"evidence_id": "evidence_688e410d95a16945e942", "evidence_kind": "paraphrase", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "span_start": -1, "span_end": 227, "original_text": "Draft version October 10, 2023 Typeset using LATEX twocolumn style in AASTeX63 Deep symbolic regression for physics guided by units constraints: toward the automated discovery of physical laws W assim Tenachi ,1 Rodrigo Ibata ,1", "interpretation": "Draft version October 10, 2023 Typeset using LATEX twocolumn style in AASTeX63 Deep symbolic regression for physics guided by units constraints: toward the automated discovery of physical laws W assim Tenachi ,1 Rodrigo Ibata ,1", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "Draft version October 10, 2023\nTypeset using LATEX twocolumn style in AASTeX63\nDeep symbolic regression for physics guided by units constraints:\ntoward the automated discovery of physical laws\nW assim Tenachi\n ,1 Rodrigo Ibata\n ,1 and Foivos I. Diakogiannis\n 2\n1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France\n2Data61, CSIRO, Kensington, WA 6155, Australia\n(Received March 03, 2023; Revised October 06 2023; Accepted October 06, 2023)\nS"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Draft version October 10, 2023 Typeset using LATEX twocolumn style in AASTeX63 Deep symbolic regression for physics guided by units constraints: toward the auto
+
+Draft version October 10, 2023 Typeset using LATEX twocolumn style in AASTeX63 Deep symbolic regression for physics guided by units constraints: toward the automated discovery of physical laws W assim Tenachi ,1 Rodrigo Ibata ,1
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_a78ba4a2ebc88876f4393ad0-foivos-i-diakogiannis-2-1universit-e-de-strasbourg-cnrs-observat.md
@@ -0,0 +1,32 @@
+---
+id: "claim_a78ba4a2ebc88876f4393ad0"
+type: "claim"
+status: "proposal"
+title: "Foivos I. Diakogiannis 2 1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France 2Data61, CSIRO, Kensin"
+created_at: "2026-07-17T12:17:07+08:00"
+updated_at: "2026-07-17T12:17:07+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b85c7e35189fedbd359efa94"]
+relations: [{"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b85c7e35189fedbd359efa94"
+evidence: [{"evidence_id": "evidence_9cdc1ea25f68e2cde12e", "evidence_kind": "paraphrase", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "span_start": -1, "span_end": 208, "original_text": "Foivos I. Diakogiannis 2 1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France 2Data61, CSIRO, Kensington, WA 6155, Australia (Received March 03, 2023", "interpretation": "Foivos I. Diakogiannis 2 1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France 2Data61, CSIRO, Kensington, WA 6155, Australia (Received March 03, 2023", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "Draft version October 10, 2023\nTypeset using LATEX twocolumn style in AASTeX63\nDeep symbolic regression for physics guided by units constraints:\ntoward the automated discovery of physical laws\nW assim Tenachi\n ,1 Rodrigo Ibata\n ,1 and Foivos I. Diakogiannis\n 2\n1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France\n2Data61, CSIRO, Kensington, WA 6155, Australia\n(Received March 03, 2023; Revised October 06 2023; Accepted October 06, 2023)\nS"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Foivos I. Diakogiannis 2 1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France 2Data61, CSIRO, Kensin
+
+Foivos I. Diakogiannis 2 1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France 2Data61, CSIRO, Kensington, WA 6155, Australia (Received March 03, 2023
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_45e2c33254979ebece6a7502-revised-october-06-2023.md
@@ -0,0 +1,32 @@
+---
+id: "claim_45e2c33254979ebece6a7502"
+type: "claim"
+status: "proposal"
+title: "Revised October 06 2023"
+created_at: "2026-07-17T12:17:07+08:00"
+updated_at: "2026-07-17T12:17:07+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b85c7e35189fedbd359efa94"]
+relations: [{"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b85c7e35189fedbd359efa94"
+evidence: [{"evidence_id": "evidence_afa1e980c232c38b25bd", "evidence_kind": "quote", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "span_start": 465, "span_end": 488, "original_text": "Revised October 06 2023", "interpretation": null, "section": null, "page": 1, "stance": "context", "verification_status": "verified", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "Draft version October 10, 2023\nTypeset using LATEX twocolumn style in AASTeX63\nDeep symbolic regression for physics guided by units constraints:\ntoward the automated discovery of physical laws\nW assim Tenachi\n ,1 Rodrigo Ibata\n ,1 and Foivos I. Diakogiannis\n 2\n1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France\n2Data61, CSIRO, Kensington, WA 6155, Australia\n(Received March 03, 2023; Revised October 06 2023; Accepted October 06, 2023)\nS"
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Revised October 06 2023
+
+Revised October 06 2023
```

### claim-4 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_54cac5c21565eb6d274a5383-accepted-october-06-2023-s.md
@@ -0,0 +1,32 @@
+---
+id: "claim_54cac5c21565eb6d274a5383"
+type: "claim"
+status: "proposal"
+title: "Accepted October 06, 2023) S"
+created_at: "2026-07-17T12:17:07+08:00"
+updated_at: "2026-07-17T12:17:07+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b85c7e35189fedbd359efa94"]
+relations: [{"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b85c7e35189fedbd359efa94"
+evidence: [{"evidence_id": "evidence_887c253c384e4923c392", "evidence_kind": "paraphrase", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "span_start": -1, "span_end": 27, "original_text": "Accepted October 06, 2023) S", "interpretation": "Accepted October 06, 2023) S", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "Draft version October 10, 2023\nTypeset using LATEX twocolumn style in AASTeX63\nDeep symbolic regression for physics guided by units constraints:\ntoward the automated discovery of physical laws\nW assim Tenachi\n ,1 Rodrigo Ibata\n ,1 and Foivos I. Diakogiannis\n 2\n1Universit´ e de Strasbourg, CNRS, Observatoire astronomique de Strasbourg, UMR 7550, F-67000 Strasbourg, France\n2Data61, CSIRO, Kensington, WA 6155, Australia\n(Received March 03, 2023; Revised October 06 2023; Accepted October 06, 2023)\nS"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Accepted October 06, 2023) S
+
+Accepted October 06, 2023) S
```
