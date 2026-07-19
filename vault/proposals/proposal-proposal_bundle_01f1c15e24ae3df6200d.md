---
id: "proposal_bundle_01f1c15e24ae3df6200d"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T03:39:38+08:00"
updated_at: "2026-07-19T03:39:53+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5d8306b5caf7371feeacbc09"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a3199e6daea6b7ca7510b023"
input_sha256: "4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_sensor_conditional_expert_routing", "target_path": "vault/memory/concept/concept_sensor_conditional_expert_routing.md", "base_sha256": "f373d3ed917130644ddb4b615149bbe81732dea0e0ce5d14262f0bcf950926a9", "candidate_sha256": "17a8306756fb448735b2645d371a2530b40a56f251ecb5ed9bafc815c49d626a", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_01f1c15e24ae3df6200d-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_01f1c15e24ae3df6200d-concept-1.md", "working_path": "vault/memory/concept/concept_sensor_conditional_expert_routing.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:39:53+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5d8306b5caf7371feeacbc09"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_a3199e6daea6b7ca7510b023`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_sensor_conditional_expert_routing.md
+++ candidate:vault/memory/concept/concept_sensor_conditional_expert_routing.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_sensor_conditional_expert_routing"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "传感器条件化专家路由"
 created_at: "2026-07-19T03:03:29+08:00"
-updated_at: "2026-07-19T03:30:53+08:00"
-aliases: []
+updated_at: "2026-07-19T03:39:38+08:00"
+aliases: ["sensor-conditional expert routing", "CoRE-VLA"]
 tags: []
 domains: ["embodied-ai", "vla", "mixture-of-experts", "robustness"]
 confidence: "medium"
 source_ids: ["source_5d8306b5caf7371feeacbc09"]
 relations: [{"type": "derived_from", "target_id": "source_5d8306b5caf7371feeacbc09", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它解决跨机器人形态和部署条件下传感器集合不一致这一通用 VLA 难题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_5d8306b5caf7371feeacbc09"
-uncertainty: "论文实验主要以深度为辅助模态，不能直接推出任意传感器组合都能优雅退化。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-19T03:30:53+08:00"
-last_verified_at: "2026-07-19T03:30:45+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_fd46bf9cd0ccdfd3bd16"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_fd46bf9cd0ccdfd3bd16-concept-1.md"
-origin_candidate_sha256: "7387cbd951f7d0161607c61d5a92bfaa22172577086b63d6ac8e3a3ab721d3ba"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_24c90d77d03044a4de6d7229"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "new_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_5d8306b5caf7371feeacbc09", "trigger_source": "source_5d8306b5caf7371feeacbc09", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "new_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_5d8306b5caf7371feeacbc09", "trigger_source": "source_5d8306b5caf7371feeacbc09", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # 传感器条件化专家路由
```
