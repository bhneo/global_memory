---
id: "proposal_bundle_e6ae032cba0844c059cc"
type: "proposal"
status: "migrated"
title: "Compile bundle：Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning"
created_at: "2026-07-19T23:48:18+08:00"
updated_at: "2026-07-19T23:48:33+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_91072aa553af99e6ab97c6cd"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-weekly-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_74fb6c6c0192fa2278005df3"
input_sha256: "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_progressive_vla_demonstration_curriculum", "target_path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "base_sha256": "2610df92ad6225aaba3cf64dbe4b63a9e042c9217502b8a6a0a2b6e23151eb6f", "candidate_sha256": "5237d389b51d7a7fe4839cdca8d1e3729903dfea85a083156d32b3d0a0d9af84", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_e6ae032cba0844c059cc-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_e6ae032cba0844c059cc-concept-1.md", "working_path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T23:48:33+08:00"}]
existing_context: [{"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_progressive_vla_demonstration_curriculum", "type": "concept", "title": "由简到繁的 VLA 示范组织", "path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "status": "working", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "match_reason": "metadata:aliases"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific [demonstrations] 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language-Action] Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}]
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

- Provider：`codex-gpt56-m91-real-weekly-v2`
- Extraction：`extraction_74fb6c6c0192fa2278005df3`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md
+++ candidate:vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md
@@ -1,41 +1,20 @@
 ---
 id: "concept_progressive_vla_demonstration_curriculum"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "由简到繁的 VLA 示范组织"
 created_at: "2026-07-19T03:02:30+08:00"
-updated_at: "2026-07-19T03:38:29+08:00"
+updated_at: "2026-07-19T23:48:18+08:00"
 aliases: ["simple-to-complex VLA demonstrations", "progressive demonstration curriculum"]
 tags: []
-domains: ["embodied-ai", "vla", "imitation-learning", "data"]
+domains: ["embodied-ai", "vla", "imitation-learning", "curriculum"]
 confidence: "medium"
 source_ids: ["source_91072aa553af99e6ab97c6cd"]
-relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "它把数据闭环中的采集环节细化为具有课程结构的示范组织问题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "示范组织影响 VLA 的学习效率、训练稳定性和长时程泛化。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_91072aa553af99e6ab97c6cd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_embodied_data_loop", "reason": "它把数据闭环中的采集环节细化为具有课程结构的示范组织问题。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "示范组织影响 VLA 的学习效率、训练稳定性和长时程泛化。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都分解长时程任务，但示范课程组织训练监督，类型化技能图组织部署时调用、验证与恢复。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-weekly-v2", "status": "proposal"}]
 change_reason: "compile bundle from source_91072aa553af99e6ab97c6cd"
-uncertainty: "证据来自双臂抓取排序和毛巾折叠任务，尚不能证明所有任务都受益于同一课程。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 4
-last_consolidated_at: "2026-07-19T03:38:29+08:00"
-last_verified_at: "2026-07-19T03:28:48+08:00"
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
-last_consolidation_id: "consolidation_788608fd42e4145bcb7ed57e"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "new_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_91072aa553af99e6ab97c6cd", "trigger_source": "source_91072aa553af99e6ab97c6cd", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "new_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_91072aa553af99e6ab97c6cd", "trigger_source": "source_91072aa553af99e6ab97c6cd", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "new_statement": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "changed_fields": ["aliases"], "reason": "compile bundle from source_91072aa553af99e6ab97c6cd", "trigger_source": "source_91072aa553af99e6ab97c6cd", "evidence_added": []}]
+change_type: "metadata_only"
+reflection_context: {"reflection_ids": ["reflection_61def8d05e0b6ddfb18b6f75"], "importance": "weekly", "changed_belief": "此前数据闭环更强调覆盖率、质量和回流速度；该材料增加了课程结构这一维度，即相同模型与近似数据规模也可能因示范顺序和组织方式产生不同结果。", "surprising": "研究声称仅改变示范组织就能改善训练稳定性与任务成功率，说明端到端完整轨迹未必是信息最有效的采集单位。", "connections": [{"shared_mechanism": "都通过阶段化结构减少策略一次性学习的组合复杂度", "boundary": "连接限于训练监督组织，不意味着示范课程等同于执行时的技能图或规划层", "difference": "由简到繁示范在数据采集阶段塑造学习分布；技能图在执行阶段显式组织可调用能力"}], "open_questions": ["课程结构带来的收益有多少来自子技能复用，有多少来自降低环境方差？"]}
+proposed_status: "working"
 ---
 
 # 由简到繁的 VLA 示范组织
```
