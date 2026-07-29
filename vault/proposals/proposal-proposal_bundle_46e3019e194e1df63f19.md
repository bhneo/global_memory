---
id: "proposal_bundle_46e3019e194e1df63f19"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-24T18:37:59+08:00"
updated_at: "2026-07-24T18:37:59+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7efe67e4901341dddfe120ff"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_2e131d6431f8a9a32109333a"
input_sha256: "bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_67c66e870e29ca11e24eaa5f", "target_path": "vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md", "base_sha256": "9989cd2612d862454913d40a29aa0fbc1d858ba7b9ff91e8ab070c538fb68deb", "candidate_sha256": "36321f52e4b0876902e213be16e1b65f1ce346a931cbcb6f87f1c2cdad89702b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_46e3019e194e1df63f19-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_46e3019e194e1df63f19-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "reflection_7398559837f1304988c5f5a7", "type": "reflection", "title": "SeededGrasp：语言应先约束接触区域，而非直接承担完整抓取几何", "path": "vault/reflections/reflection-reflection_7398559837f1304988c5f5a7.md", "status": "active", "source_ids": ["source_7efe67e4901341dddfe120ff"], "snippet": "# SeededGrasp：语言应先约束接触区域，而非直接承担完整抓取几何\n\n## Why important\n\nSeededGrasp 将语言语义压缩为场景中的任务相关 seed point，再由轻量抓取生成器处理本体相关姿态；这给多本体抓取提供了一个可分离的语义—几何边界。\n\n## What changed\n\n语言引导抓取不必让 VLM 端到端输出抓取姿态；在杂乱场景中…", "match_reason": "metadata:domains"}, {"id": "concept_67c66e870e29ca11e24eaa5f", "type": "concept", "title": "以语言选择三维抓取种子的多本体抓取分解", "path": "vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md", "status": "working", "source_ids": ["source_7efe67e4901341dddfe120ff"], "snippet": "# 以语言选择三维抓取种子的多本体抓取分解\n\n在杂乱场景的语言引导抓取中，VLM 可先从场景点云选择表征目标对象或功能部位的 seed point，再以该点为条件由轻量抓取生成模型预测本体相关抓取姿态；这种分解把任务语义与接触几何解耦，但其跨本体收益仍取决于目标定位、点云质量和各夹爪的训练覆盖。", "match_reason": "metadata:aliases"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-[Complex] Structured Demonstrations for Vision-Language-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_progressive_vla_demonstration_curriculum", "type": "concept", "title": "由简到繁的 VLA 示范组织", "path": "vault/memory/concept/concept_progressive_vla_demonstration_curriculum.md", "status": "working", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# 由简到繁的 VLA 示范组织\n\n通过子技能分解、环境标准化和任务复杂度递增来组织机器人示范，使策略先掌握基础操作，再学习长时程组合，而不是只收集完整端到端轨迹。", "match_reason": "metadata:aliases"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…Like progressive VLA demonstration curricula, it decomposes [complex] skills into intermediate targets that are easier to learn than…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_7efe67e4901341dddfe120ff"}
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

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_2e131d6431f8a9a32109333a`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md
+++ candidate:vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_67c66e870e29ca11e24eaa5f"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "以语言选择三维抓取种子的多本体抓取分解"
 created_at: "2026-07-24T18:05:50+08:00"
-updated_at: "2026-07-24T18:05:50+08:00"
+updated_at: "2026-07-24T18:37:59+08:00"
 aliases: ["Language-Guided Seeded Grasping", "SeededGrasp", "语言引导三维抓取种子"]
 tags: []
 domains: ["robot-grasping", "vla", "cross-embodiment"]
 confidence: "medium"
 source_ids: ["source_7efe67e4901341dddfe120ff"]
-relations: [{"type": "derived_from", "target_id": "source_7efe67e4901341dddfe120ff", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都以共享语义接口服务多本体行为；本概念将共享部分具体限制为 seed-point 定位，并把抓取姿态保留给本体相关生成器。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_7efe67e4901341dddfe120ff", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都以共享语义接口服务多本体行为；本概念将共享部分具体限制为 seed-point 定位，并把抓取姿态保留给本体相关生成器。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都以共享语义接口服务多本体行为；本概念将共享部分具体限制为 seed-point 定位，并把抓取姿态保留给本体相关生成器。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_7efe67e4901341dddfe120ff"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_7398559837f1304988c5f5a7"], "importance": "high", "changed_belief": "语言引导抓取不必让 VLM 端到端输出抓取姿态；在杂乱场景中，让它指出目标对象或功能部位可把高层意图与低层接触可行性分给不同模块。", "surprising": "", "connections": [{"shared_mechanism": "两者都把跨本体复用建立在共享的高层表示与本体特定控制解码之间。", "boundary": "该连接适用于存在可定位目标区域的抓取任务，不说明单个 seed point 足以表达所有接触序列或灵巧手约束。", "difference": "SeededGrasp 使用显式三维 seed point 作为条件；既有跨本体 VLA 概念描述的是更一般的统一输入输出策略接口。"}], "open_questions": []}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_16a3af460cb0ac5aa877"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_16a3af460cb0ac5aa877-concept-1.md"
-origin_candidate_sha256: "85e5f18aed9035e9057d7677eb8f5baff3bc92207f1d6fde610cb14680427cd9"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 以语言选择三维抓取种子的多本体抓取分解
```
