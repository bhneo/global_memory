---
id: "proposal_bundle_a0829fbbfadd33fc47cf"
type: "proposal"
status: "migrated"
title: "Compile bundle：Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement"
created_at: "2026-07-19T03:28:10+08:00"
updated_at: "2026-07-19T03:28:24+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_291d6174cf92660287138f47"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_fc44714a9855c8d489024b01"
input_sha256: "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_vla_action_cache_refinement", "target_path": "vault/memory/concept/concept_vla_action_cache_refinement.md", "base_sha256": "3e1ff6e99be160c44cc7c5070e20fa19bd73a228d9baa6b06e2b2c64dfe8a069", "candidate_sha256": "7c9cbf6dfaa3ef4c45d3199747e09d3bbcc668fbf5f2281a540961836c0c8476", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_a0829fbbfadd33fc47cf-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_a0829fbbfadd33fc47cf-concept-1.md", "working_path": "vault/memory/concept/concept_vla_action_cache_refinement.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:28:24+08:00"}]
existing_context: [{"id": "claim_6ed5013981fdc75c87eb19c9", "type": "claim", "title": "real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×", "path": "vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "…rates in a low-latency regime, achieving inference [acceleration] of up to 11.75×\n\nreal-world environments demonstrate…", "match_reason": "metadata:title"}, {"id": "claim_0534c95e4004502bb928fc9e", "type": "claim", "title": "34.43× for representative flow-based VLA models, π0.5", "path": "vault/memory/claim/claim_0534c95e4004502bb928fc9e.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# 34.43× for representative flow-based VLA [models], π0.5\n\n34.43× for representative flow-based VLA [models]…", "match_reason": "metadata:title"}, {"id": "claim_4b17c3d6e1aa3af61a3c70d4", "type": "claim", "title": "These trends indicate that improving VLA models in practice requires a coordinated treatment of data, embodiment,", "path": "vault/memory/claim/claim_4b17c3d6e1aa3af61a3c70d4.md", "status": "working", "source_ids": ["source_233c4bef3a727389ddf81ae2"], "snippet": "# These trends indicate that improving VLA [models] in practice requires a coordinated treatment of data, embodiment,\n\nThese trends…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_291d6174cf92660287138f47"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_fc44714a9855c8d489024b01`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_vla_action_cache_refinement.md
+++ candidate:vault/memory/concept/concept_vla_action_cache_refinement.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_vla_action_cache_refinement"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "VLA 动作缓存与上下文复用"
 created_at: "2026-07-19T03:02:11+08:00"
-updated_at: "2026-07-19T03:23:11+08:00"
-aliases: []
+updated_at: "2026-07-19T03:28:10+08:00"
+aliases: ["VLA action caching and refinement", "ActionCache"]
 tags: []
 domains: ["embodied-ai", "vla", "inference-efficiency"]
 confidence: "medium"
 source_ids: ["source_291d6174cf92660287138f47"]
 relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_291d6174cf92660287138f47"
-uncertainty: "复用安全性依赖上下文相似度和 refinement 能否修正陈旧动作。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 2
-last_consolidated_at: "2026-07-19T03:23:11+08:00"
-last_verified_at: "2026-07-19T03:23:03+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_1f08ff1c3ffeadc964e2"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_1f08ff1c3ffeadc964e2-concept-1.md"
-origin_candidate_sha256: "c6afce9c6035a67c01e1ee3156231b1f0032c611ee2d640c18f1780d2e9a48be"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_60f18fd4d9c2b299a12a5c6e"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # VLA 动作缓存与上下文复用
```
