---
id: "proposal_bundle_6c244c6e613b21830b27"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.13653v1.pdf"
created_at: "2026-07-22T18:12:25+08:00"
updated_at: "2026-07-22T18:12:26+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_92fed4343c703da77f798f08"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.13653v1.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a59ea00a719f7763eb498457"
input_sha256: "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_16a7c84a59e39784c801e4ff", "target_path": "vault/knowledge/concepts/concept_16a7c84a59e39784c801e4ff-非特权开放世界移动操作评测边界.md", "base_sha256": null, "candidate_sha256": "f40605c1bbbc446e9367dda3356e52792cd558f9f511cf188ab3cb231b140684", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_6c244c6e613b21830b27-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_16a7c84a59e39784c801e4ff.md", "working_at": "2026-07-22T18:12:26+08:00"}]
existing_context: [{"id": "input_7ee0bdd883c221ff9e62625a", "type": "input", "title": "2607.13653v1.pdf", "path": "vault/inputs/input-input_7ee0bdd883c221ff9e62625a.md", "status": "active", "source_ids": ["source_92fed4343c703da77f798f08"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.13653v1.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/96/59/9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "…source repository for REAL——Exploratory, Communicative, and Deployable: [Vision-Driven] Embodied Agents for Open-World Mobile Manipulation · GitHub…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_92fed4343c703da77f798f08"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.13653v1.pdf

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_a59ea00a719f7763eb498457`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_16a7c84a59e39784c801e4ff-非特权开放世界移动操作评测边界.md
@@ -0,0 +1,20 @@
+---
+id: "concept_16a7c84a59e39784c801e4ff"
+type: "concept"
+status: "proposal"
+title: "非特权开放世界移动操作评测边界"
+created_at: "2026-07-22T18:12:25+08:00"
+updated_at: "2026-07-22T18:12:25+08:00"
+aliases: ["Non-Privileged Open-World Mobile Manipulation Evaluation", "REAL", "REAL-Bench", "非特权移动操作评测"]
+tags: []
+domains: ["mobile-manipulation", "benchmarking"]
+confidence: "medium"
+source_ids: ["source_92fed4343c703da77f798f08"]
+relations: [{"type": "derived_from", "target_id": "source_92fed4343c703da77f798f08", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_protocol_hri_agent_execution_boundary", "reason": "两者都将语言交互和物理执行分别置于明确协议边界中；REAL 用任务环境检验该边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_92fed4343c703da77f798f08"
+reflection_context: {"reflection_ids": ["reflection_f83b07f9aed0e61ac4a066d9"], "importance": "high", "changed_belief": "开放世界评测不能默认对象列表、目标位姿或无歧义指令；这些信息缺口本身构成策略能力与失败来源。", "surprising": "论文报告的实机结果来自特定双臂移动平台与 60 个 episode，说明该评测边界比仅模拟指标更强，但仍不是跨平台保证。", "connections": [], "open_questions": ["如何分解报告探索、澄清、工具执行与物理可达性对每次失败的贡献？"]}
+---
+
+# 非特权开放世界移动操作评测边界
+
+面向开放世界移动操作的评测应限制策略使用 RGB 等物理可获得输入，并把主动探索、视觉消歧和人机意图澄清纳入闭环任务；模拟与实机成绩必须连同具体工具、资产、episode 和本体条件解释。
```
