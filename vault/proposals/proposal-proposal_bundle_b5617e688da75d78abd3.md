---
id: "proposal_bundle_b5617e688da75d78abd3"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - graph-robots/graph-as-policy: gap — graph as policy: compile language instructions into typed, verified robot skill graphs and execute them on simulators or real robots · GitHub"
created_at: "2026-07-19T12:18:22+08:00"
updated_at: "2026-07-19T12:18:23+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_6fb6f0a30a013fd1ada42b57"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - graph-robots/graph-as-policy: gap — graph as policy: compile language instructions into typed, verified robot skill graphs and execute them on simulators or real robots · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a3e7b623386921fd615dae06"
input_sha256: "d386342126ca523c0cc2e040e6e78befa390123e5f540c26db2e4575b43da99c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_typed_verified_robot_skill_graph", "target_path": "vault/knowledge/concepts/concept_typed_verified_robot_skill_graph-类型化可验证机器人技能图.md", "base_sha256": null, "candidate_sha256": "ec5963e7c2ed2938187356345abefa3d22b57b44cd0d654d4777b1eb9a3d0c0c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b5617e688da75d78abd3-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_typed_verified_robot_skill_graph.md", "working_at": "2026-07-19T12:18:23+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_6fb6f0a30a013fd1ada42b57"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - graph-robots/graph-as-policy: gap — graph as policy: compile language instructions into typed, verified robot skill graphs and execute them on simulators or real robots · GitHub

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_a3e7b623386921fd615dae06`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_typed_verified_robot_skill_graph-类型化可验证机器人技能图.md
@@ -0,0 +1,20 @@
+---
+id: "concept_typed_verified_robot_skill_graph"
+type: "concept"
+status: "proposal"
+title: "类型化可验证机器人技能图"
+created_at: "2026-07-19T12:18:22+08:00"
+updated_at: "2026-07-19T12:18:22+08:00"
+aliases: ["typed verified robot skill graph", "Graph-as-Policy", "GaP"]
+tags: []
+domains: ["embodied-ai", "robotics", "skill-graphs", "agent-execution"]
+confidence: "medium"
+source_ids: ["source_6fb6f0a30a013fd1ada42b57"]
+relations: [{"type": "derived_from", "target_id": "source_6fb6f0a30a013fd1ada42b57", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_skill_evolution", "reason": "GaP 为可审计技能沉淀补充了显式 workflow schema、验证、checkpoint、recovery 和 sim-to-hardware 执行边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "该项目给出一种可操作答案：当任务需要跨变化实例持久复用且能通过技能契约和验证门控检查时，可把语言规划固化为外部图。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_adaptive_interleaved_multimodal_planning", "reason": "APIVOT 在模型内部生成视觉未来状态，GaP 把任务结构外化为可执行图；两者分别覆盖内部几何推理与外部可审计执行。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "tension_internal_reasoning_external_skills", "reason": "GaP 明确选择外部类型化技能与图执行，构成该 tension 的外部可审计一侧。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_6fb6f0a30a013fd1ada42b57"
+uncertainty: "来源是 beta 代码仓库说明，API、workflow schema 与 skill interfaces 明示可能变化；项目示例不能替代独立成功率复核。"
+---
+
+# 类型化可验证机器人技能图
+
+把自然语言任务编译为带类型、检查点和恢复语义的模块化技能计算图，在仿真中验证与改进后执行该图本身，使跨对象几何和姿态变化的持续任务保留可审计控制结构。
```
