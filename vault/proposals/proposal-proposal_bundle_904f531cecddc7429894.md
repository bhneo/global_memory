---
id: "proposal_bundle_904f531cecddc7429894"
type: "proposal"
status: "migrated"
title: "Compile bundle：Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement"
created_at: "2026-07-19T23:47:20+08:00"
updated_at: "2026-07-19T23:47:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_291d6174cf92660287138f47"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-weekly-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_fc44714a9855c8d489024b01"
input_sha256: "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_vla_action_cache_refinement", "target_path": "vault/memory/concept/concept_vla_action_cache_refinement.md", "base_sha256": "438b6982d7d63ec5827e891849d91cff97a3ef352c4ba6a748f64182b54bcae6", "candidate_sha256": "c6b9334efb58e1b46a625bf436bea5f3ebdb83daa48a3a38fa0127637d23595a", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_904f531cecddc7429894-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_904f531cecddc7429894-concept-1.md", "working_path": "vault/memory/concept/concept_vla_action_cache_refinement.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T23:47:48+08:00"}]
existing_context: [{"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-Action [Models] with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language-Action] Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}]
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

- Provider：`codex-gpt56-m91-real-weekly-v2`
- Extraction：`extraction_fc44714a9855c8d489024b01`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_vla_action_cache_refinement.md
+++ candidate:vault/memory/concept/concept_vla_action_cache_refinement.md
@@ -1,41 +1,20 @@
 ---
 id: "concept_vla_action_cache_refinement"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "VLA 动作缓存与上下文复用"
 created_at: "2026-07-19T03:02:11+08:00"
-updated_at: "2026-07-19T12:20:26+08:00"
+updated_at: "2026-07-19T23:47:20+08:00"
 aliases: ["VLA action caching and refinement", "ActionCache"]
 tags: []
-domains: ["embodied-ai", "vla", "inference-efficiency"]
+domains: ["embodied-ai", "vla", "inference-efficiency", "memory"]
 confidence: "medium"
 source_ids: ["source_291d6174cf92660287138f47"]
-relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_291d6174cf92660287138f47", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它在不改变通用 VLA 主干的情况下优化连续动作头的实时执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都面向真实部署的时延与闭环执行，但缓存复用不等同于未来动力学预测。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "缓存复用和动作块执行都延长已有中间结果的有效期，因此需要按环境变化和不确定性共同决定何时重新生成。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
 change_reason: "compile bundle from source_291d6174cf92660287138f47"
-uncertainty: "复用安全性依赖上下文相似度和 refinement 能否修正陈旧动作。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 5
-last_consolidated_at: "2026-07-19T12:20:26+08:00"
-last_verified_at: "2026-07-19T03:28:10+08:00"
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
-last_consolidation_id: "consolidation_129dac2d7286fa5c70b89ac8"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["aliases"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}]
+change_type: "metadata_only"
+reflection_context: {"reflection_ids": ["reflection_62e14da60b1cc35f28689c29"], "importance": "weekly", "changed_belief": "此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。", "surprising": "缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。", "connections": [{"shared_mechanism": "都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬", "boundary": "连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解", "difference": "ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合"}], "open_questions": ["缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？"]}
+proposed_status: "working"
 ---
 
 # VLA 动作缓存与上下文复用
```
