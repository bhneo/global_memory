---
id: "proposal_bundle_3602f8a0cb6074cc6b82"
type: "proposal"
status: "migrated"
title: "Compile bundle：Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning"
created_at: "2026-07-19T03:02:30+08:00"
updated_at: "2026-07-19T03:02:31+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_91072aa553af99e6ab97c6cd"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_74fb6c6c0192fa2278005df3"
input_sha256: "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_progressive_vla_demonstration_curriculum", "target_path": "vault/knowledge/concepts/concept_progressive_vla_demonstration_curriculum-由简到繁的-vla-示范组织.md", "base_sha256": null, "candidate_sha256": "0815000a3ef073a4175b5639d07e636ffe38abe2822afd54750fce2dadc5f15d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3602f8a0cb6074cc6b82-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "working_at": "2026-07-19T03:02:31+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_db4c678a437a315763b8b434", "target_path": "vault/knowledge/claims/claim_db4c678a437a315763b8b434-experimental-results-show-consistent-improvements-in-task-succes.md", "base_sha256": null, "candidate_sha256": "ddea7bbe4faf0286c76d5ec10083fa48da25f946a08406c717c218ef1875d737", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3602f8a0cb6074cc6b82-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_db4c678a437a315763b8b434.md", "working_at": "2026-07-19T03:02:31+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_8477d6342c9553e4d9029bd3", "target_path": "vault/knowledge/claims/claim_8477d6342c9553e4d9029bd3-training-stability-compared-with-the-baseline-method-of-directly.md", "base_sha256": null, "candidate_sha256": "e45373f8840bce55a29e6c978c177fef1e55af9d8e31c03c7734a9fe664cdd12", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3602f8a0cb6074cc6b82-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_8477d6342c9553e4d9029bd3.md", "working_at": "2026-07-19T03:02:31+08:00"}]
existing_context: [{"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific [demonstrations] 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 3, "source_id": "source_91072aa553af99e6ab97c6cd"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 3, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 3, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_74fb6c6c0192fa2278005df3`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_progressive_vla_demonstration_curriculum-由简到繁的-vla-示范组织.md
@@ -0,0 +1,20 @@
+---
+id: "concept_progressive_vla_demonstration_curriculum"
+type: "concept"
+status: "proposal"
+title: "由简到繁的 VLA 示范组织"
+created_at: "2026-07-19T03:02:30+08:00"
+updated_at: "2026-07-19T03:02:30+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "imitation-learning", "data"]
+confidence: "medium"
+source_ids: ["source_91072aa553af99e6ab97c6cd"]
+relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "它把数据闭环中的采集环节细化为具有课程结构的示范组织问题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "示范组织影响 VLA 的学习效率、训练稳定性和长时程泛化。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
+uncertainty: "证据来自双臂抓取排序和毛巾折叠任务，尚不能证明所有任务都受益于同一课程。"
+---
+
+# 由简到繁的 VLA 示范组织
+
+通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_db4c678a437a315763b8b434-experimental-results-show-consistent-improvements-in-task-succes.md
@@ -0,0 +1,32 @@
+---
+id: "claim_db4c678a437a315763b8b434"
+type: "claim"
+status: "proposal"
+title: "Experimental results show consistent improvements in task success rate"
+created_at: "2026-07-19T03:02:30+08:00"
+updated_at: "2026-07-19T03:02:30+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "imitation-learning"]
+confidence: "medium"
+source_ids: ["source_91072aa553af99e6ab97c6cd"]
+relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_embodied_data_loop", "reason": "结果表明数据组织方式而非仅数据规模会影响 VLA 学习效果。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
+applicability: ["reported dual-arm block sorting and towel folding experiments"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_42308c25592c4fa888b5", "evidence_kind": "quote", "source_id": "source_91072aa553af99e6ab97c6cd", "content_id": "content_435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876", "extraction_id": "extraction_74fb6c6c0192fa2278005df3", "span_start": 2146, "span_end": 2216, "original_text": "Experimental results show consistent improvements in task success rate", "interpretation": null, "section": null, "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "Experimental results show consistent improvements in task success rate and training stability compared with the baseline method of directly collecting end-to-end complete task trajectories."
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# Experimental results show consistent improvements in task success rate
+
+Experimental results show consistent improvements in task success rate
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_8477d6342c9553e4d9029bd3-training-stability-compared-with-the-baseline-method-of-directly.md
@@ -0,0 +1,32 @@
+---
+id: "claim_8477d6342c9553e4d9029bd3"
+type: "claim"
+status: "proposal"
+title: "training stability compared with the baseline method of directly collecting end-to-end complete task trajectories."
+created_at: "2026-07-19T03:02:30+08:00"
+updated_at: "2026-07-19T03:02:30+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "imitation-learning"]
+confidence: "medium"
+source_ids: ["source_91072aa553af99e6ab97c6cd"]
+relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_embodied_data_loop", "reason": "结果表明数据组织方式而非仅数据规模会影响 VLA 学习效果。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
+applicability: ["reported dual-arm block sorting and towel folding experiments"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_e6db8606b1ad1d06ede9", "evidence_kind": "quote", "source_id": "source_91072aa553af99e6ab97c6cd", "content_id": "content_435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876", "extraction_id": "extraction_74fb6c6c0192fa2278005df3", "span_start": 2221, "span_end": 2335, "original_text": "training stability compared with the baseline method of directly collecting end-to-end complete task trajectories.", "interpretation": null, "section": null, "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "Experimental results show consistent improvements in task success rate and training stability compared with the baseline method of directly collecting end-to-end complete task trajectories."
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# training stability compared with the baseline method of directly collecting end-to-end complete task trajectories.
+
+training stability compared with the baseline method of directly collecting end-to-end complete task trajectories.
```
