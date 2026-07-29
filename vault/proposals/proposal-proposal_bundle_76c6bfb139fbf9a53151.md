---
id: "proposal_bundle_76c6bfb139fbf9a53151"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-25T18:08:58+08:00"
updated_at: "2026-07-25T18:08:59+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e8650c5afb7548268f649fb8"]
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
extraction_id: "extraction_b0923ded365e3783f9810e75"
input_sha256: "c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_ebafde4b9db7a2ebd19c6bc6", "target_path": "vault/knowledge/concepts/concept_ebafde4b9db7a2ebd19c6bc6-以休眠锚点和意图激活驱动的即时场景图生长.md", "base_sha256": null, "candidate_sha256": "6b7b9a52cdaafaf397e7826a19d56fbc3d864939325ed9ebb058f8509a011b55", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_76c6bfb139fbf9a53151-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_ebafde4b9db7a2ebd19c6bc6.md", "working_at": "2026-07-25T18:08:59+08:00"}]
existing_context: [{"id": "concept_typed_verified_robot_skill_graph", "type": "concept", "title": "类型化可验证机器人技能图", "path": "vault/memory/concept/concept_typed_verified_robot_skill_graph.md", "status": "working", "source_ids": ["source_6fb6f0a30a013fd1ada42b57"], "snippet": "# 类型化可验证机器人技能图\n\n把自然语言任务编译为带类型、检查点和恢复语义的模块化技能计算图，在仿真中验证与改进后执行该图本身，使跨对象几何和姿态变化的持续任务保留可审计控制结构。", "match_reason": "metadata:aliases"}, {"id": "reflection_7952be977c24d5dfe1da2072", "type": "reflection", "title": "图式 Agent Memory：生命周期完整不等于证据闭环完整", "path": "vault/reflections/reflection-reflection_7952be977c24d5dfe1da2072.md", "status": "active", "source_ids": ["source_01ed2f19e91bb0eb1ec3ee92"], "snippet": "# 图式 Agent Memory：生命周期完整不等于证据闭环完整\n\n## Why important\n\n这份综述把 Agent Memory 统一为 extraction、storage、retrieval、evolution 四阶段，并指出长期系统的难点已从单纯召回扩展到冲突更新、外部验证、隐私与可归因评测…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e8650c5afb7548268f649fb8"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_b0923ded365e3783f9810e75`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_ebafde4b9db7a2ebd19c6bc6-以休眠锚点和意图激活驱动的即时场景图生长.md
@@ -0,0 +1,20 @@
+---
+id: "concept_ebafde4b9db7a2ebd19c6bc6"
+type: "concept"
+status: "proposal"
+title: "以休眠锚点和意图激活驱动的即时场景图生长"
+created_at: "2026-07-25T18:08:58+08:00"
+updated_at: "2026-07-25T18:08:58+08:00"
+aliases: ["Just-In-Time Scene Graph Growth", "JITOMA", "即时按需场景图增长"]
+tags: []
+domains: ["scene-graphs", "robot-memory", "long-horizon-robotics"]
+confidence: "medium"
+source_ids: ["source_e8650c5afb7548268f649fb8"]
+relations: [{"type": "derived_from", "target_id": "source_e8650c5afb7548268f649fb8", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都用结构化图承载长时程机器人任务；JITOMA 按意图选择何时增长环境子图，而该既有概念用类型、检查点和恢复语义组织可执行技能图。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e8650c5afb7548268f649fb8"
+reflection_context: {"reflection_ids": ["reflection_96809e9d9bffed57b211681f"], "importance": "high", "changed_belief": "此前可能把场景图的任务相关性理解为构建完成后的查询或筛选问题；本文使我更重视资源分配时序本身，即哪些信息应只保留可唤醒索引，哪些信息值得在尚无任务需求时立即语义化。", "surprising": "", "connections": [{"shared_mechanism": "两者都要求把机器人内部结构组织成可按任务激活、且能保留验证边界的局部图。", "boundary": "该连接适用于长时程机器人在有限计算预算下维护结构化环境或技能状态的设计讨论，不证明 JITOMA 已在所有硬件和场景中带来端到端执行收益。", "difference": "JITOMA 管理的是场景观察到 3D 子图的感知与描述成本；既有技能图概念管理的是任务原语、检查点和恢复语义。"}], "open_questions": []}
+---
+
+# 以休眠锚点和意图激活驱动的即时场景图生长
+
+JITOMA 不在进入环境时为全部观测建立高成本的稠密三维语义图，而是先从连续观测维护低成本全局休眠锚点；当任务查询出现时，系统解析机器人意图，唤醒相关局部锚点，并只在该子图内执行节点描述、功能推断等高成本操作。该设计旨在减少长期任务切换中的活动图规模、描述延迟和无关语义噪声，其收益受任务热图质量、锚点覆盖和遗漏关键细节风险约束。
```
