---
id: "proposal_bundle_b414be434cef9482620f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T18:05:38+08:00"
updated_at: "2026-07-20T18:05:39+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_158b4743a3d4e973913f8bbf"]
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
extraction_id: "extraction_7dfda7a59a3d38dfd91d0958"
input_sha256: "39bb8c948872b74c7fe136e31cde65e235308974c5aedec604bcc370f21be425"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_637cf7264723c03955c719e2", "target_path": "vault/knowledge/concepts/concept_637cf7264723c03955c719e2-遥操作跟踪偏差作为隐式交互线索.md", "base_sha256": null, "candidate_sha256": "e005ac78307a23db98ddadec269bc4bc6c7693774f76aaa46c528b9c22800fe9", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b414be434cef9482620f-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_637cf7264723c03955c719e2.md", "working_at": "2026-07-20T18:05:39+08:00"}]
existing_context: [{"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for [Force] Abstract Method Experiments LIFT: Never Too Late for [Force] Accelerating VLA Post-Training…", "match_reason": "metadata:title"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "# TactiDex：人形动作相似不等于接触层面的人类式操作\n\n## Why important\n\nTactiDex 同步记录全手压力、手部运动学、腕部和物体 6D 状态，并把 contact formation、[force] alignment 与安全约束纳入迁移目标和评测，直接暴露纯运动学 imitation…", "match_reason": "full-text:body"}, {"id": "synthesis_be18972801786224075196eb", "type": "synthesis", "title": "灵巧操作、触觉与示范迁移：交互结构、冗余先验和物理可行性", "path": "vault/synthesis/synthesis-synthesis_be18972801786224075196eb.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_951559714c0383331b1b30ac", "source_b7444ef42015f4f3b6f51032", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…在 REGRIND reference 上逐步加入 TactiDex 的 contact timing/[force] 监督，分离空间关系和触觉保真的收益。\n- 为 PAKE 的 partial reference 与 REGRIND…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_158b4743a3d4e973913f8bbf"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_7dfda7a59a3d38dfd91d0958`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_637cf7264723c03955c719e2-遥操作跟踪偏差作为隐式交互线索.md
@@ -0,0 +1,20 @@
+---
+id: "concept_637cf7264723c03955c719e2"
+type: "concept"
+status: "proposal"
+title: "遥操作跟踪偏差作为隐式交互线索"
+created_at: "2026-07-20T18:05:38+08:00"
+updated_at: "2026-07-20T18:05:38+08:00"
+aliases: ["Teleoperation Tracking Discrepancy as Implicit Interaction Cue", "Implicit Force Cue in ACT", "遥操作隐式力线索"]
+tags: []
+domains: ["embodied-ai", "contact-manipulation", "imitation-learning"]
+confidence: "medium"
+source_ids: ["source_158b4743a3d4e973913f8bbf"]
+relations: [{"type": "derived_from", "target_id": "source_158b4743a3d4e973913f8bbf", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_5b49f7afd60ba18d35ca58e8", "reason": "两者都把接触信息作为纯运动学模仿之外的必要信号，但一个来自机器人遥操作误差，另一个来自人类压力与接触参考。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_158b4743a3d4e973913f8bbf"
+reflection_context: {"reflection_ids": ["reflection_91f2ffd2085e86802850ad17"], "importance": "high", "changed_belief": "此前容易将 ACT 的接触能力归因于动作分块架构；这里提示必须区分架构能力与遥操作管线暗中提供的交互线索。", "surprising": "", "connections": [{"shared_mechanism": "两者都试图让策略保留对接触形成、阻力和安全约束敏感的状态。", "boundary": "该连接不假定电机电流或力矩 proxy 等同于真实六维力/力矩测量。", "difference": "触觉对齐的人到机器人接触迁移用显式压力和接触结构作为监督；本文比较遥操作误差这一隐式线索与由机载测量导出的力矩 proxy。"}], "open_questions": ["不同控制器增益、摩擦补偿和传感噪声下，何时力矩 proxy 足以替代遥操作误差信号？"]}
+---
+
+# 遥操作跟踪偏差作为隐式交互线索
+
+在 leader–follower 位置控制遥操作中，leader 命令与 follower 执行状态之间的跟踪偏差可与接触起始、外部阻力和约束违反相关；若改为预测未来 follower 状态而移除该偏差，接触关键阶段可能失去该隐式观测，而机载关节力矩或电流 proxy 可作为可显式建模的替代信号。
```
