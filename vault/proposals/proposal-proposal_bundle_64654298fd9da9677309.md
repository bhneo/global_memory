---
id: "proposal_bundle_64654298fd9da9677309"
type: "proposal"
status: "migrated"
title: "Compile bundle：Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning"
created_at: "2026-07-19T03:23:33+08:00"
updated_at: "2026-07-19T03:23:48+08:00"
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
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_progressive_vla_demonstration_curriculum", "target_path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "base_sha256": "4b233a73f067d1369bda0f87759bc6ace098476c7cc3d97d77b3d4d03828ddc1", "candidate_sha256": "9d2723f9a5d11d8ed27543941d3fa871bbf5740fbe0b8b14f818c2f505e902e9", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_64654298fd9da9677309-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_64654298fd9da9677309-concept-1.md", "working_path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:23:48+08:00"}]
existing_context: [{"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific [demonstrations] 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_91072aa553af99e6ab97c6cd"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
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

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md
+++ candidate:vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md
@@ -1,39 +1,19 @@
 ---
 id: "concept_progressive_vla_demonstration_curriculum"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "由简到繁的 VLA 示范组织"
 created_at: "2026-07-19T03:02:30+08:00"
-updated_at: "2026-07-19T03:06:05+08:00"
-aliases: []
+updated_at: "2026-07-19T03:23:33+08:00"
+aliases: ["simple-to-complex VLA demonstrations", "progressive demonstration curriculum"]
 tags: []
 domains: ["embodied-ai", "vla", "imitation-learning", "data"]
 confidence: "medium"
 source_ids: ["source_91072aa553af99e6ab97c6cd"]
 relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "它把数据闭环中的采集环节细化为具有课程结构的示范组织问题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "示范组织影响 VLA 的学习效率、训练稳定性和长时程泛化。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
-uncertainty: "证据来自双臂抓取排序和毛巾折叠任务，尚不能证明所有任务都受益于同一课程。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-19T03:06:05+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_3602f8a0cb6074cc6b82"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_3602f8a0cb6074cc6b82-concept-1.md"
-origin_candidate_sha256: "0815000a3ef073a4175b5639d07e636ffe38abe2822afd54750fce2dadc5f15d"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_7f2eec512acfc752ebb554b1"
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # 由简到繁的 VLA 示范组织
```
