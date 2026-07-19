---
id: "proposal_bundle_9a3307c0abe27d2f9610"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T03:40:05+08:00"
updated_at: "2026-07-19T03:40:19+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
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
extraction_id: "extraction_b80f55d96258c5cbdae58ac8"
input_sha256: "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_vla_action_evaluation_distillation", "target_path": "vault/memory/concept/concept_vla_action_evaluation_distillation.md", "base_sha256": "1bf1c4af78049fba72313d9fdad959e1f41cbbeb0c970c16dd35962526ac0478", "candidate_sha256": "1752dd5cb683db410aaf1551c4a8be82ad2d8844e7ba73082bf8269feb92fe89", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_9a3307c0abe27d2f9610-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_9a3307c0abe27d2f9610-concept-1.md", "working_path": "vault/memory/concept/concept_vla_action_evaluation_distillation.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:40:19+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ff90ad99bd47043e812cce9e"}
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
- Extraction：`extraction_b80f55d96258c5cbdae58ac8`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_vla_action_evaluation_distillation.md
+++ candidate:vault/memory/concept/concept_vla_action_evaluation_distillation.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_vla_action_evaluation_distillation"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "VLA 动作评估蒸馏"
 created_at: "2026-07-19T03:03:50+08:00"
-updated_at: "2026-07-19T03:26:42+08:00"
-aliases: []
+updated_at: "2026-07-19T03:40:05+08:00"
+aliases: ["VLA action evaluation distillation", "action value distillation", "SVA"]
 tags: []
 domains: ["embodied-ai", "vla", "reinforcement-learning", "planning", "value-function"]
 confidence: "medium"
 source_ids: ["source_ff90ad99bd47043e812cce9e"]
 relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "answers", "target_id": "question_world_model_action_value", "reason": "该方法用仿真回报蒸馏出的动作价值模型把长期后果预测连接到动作选择。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都关注预测结果对策略评价的价值，但这里评价对象是冻结 VLA 产生的候选动作。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "评估器与生成器解耦，目标是在不后训练 VLA 主干的情况下保留通用能力。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
-uncertainty: "树搜索知识来自仿真，Q 评估器的 Sim-to-Real 外推和候选覆盖仍是限制。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-19T03:26:42+08:00"
-last_verified_at: "2026-07-19T03:26:34+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_ec30b88a6f8a07464311"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_ec30b88a6f8a07464311-concept-1.md"
-origin_candidate_sha256: "3542f12e5f8958f0080a14086281120220baef7fb31311e93839bd7346840cf1"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_45aa1991d480b045e0765e10"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "new_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ff90ad99bd47043e812cce9e", "trigger_source": "source_ff90ad99bd47043e812cce9e", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "new_statement": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ff90ad99bd47043e812cce9e", "trigger_source": "source_ff90ad99bd47043e812cce9e", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # VLA 动作评估蒸馏
```
