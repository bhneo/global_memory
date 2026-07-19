---
id: "proposal_bundle_0cb43c03823e232015b6"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:18:53+08:00"
updated_at: "2026-07-19T12:18:53+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_011483b15aae65e849a3772e"]
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
extraction_id: "extraction_f29133ba5e9d78ebe32902ab"
input_sha256: "05aded7c8cbc5f5d38322d846307a00a462688faff9c13a3dad650538dff8f78"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_event_sensitive_task_progress_memory", "target_path": "vault/knowledge/concepts/concept_event_sensitive_task_progress_memory-事件敏感的任务进度记忆.md", "base_sha256": null, "candidate_sha256": "67910fd4367e6ea78e0e0cd0582bcb31fe746f415845b0ba1568c82069ba2087", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0cb43c03823e232015b6-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "working_at": "2026-07-19T12:18:53+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_011483b15aae65e849a3772e"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_f29133ba5e9d78ebe32902ab`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_event_sensitive_task_progress_memory-事件敏感的任务进度记忆.md
@@ -0,0 +1,20 @@
+---
+id: "concept_event_sensitive_task_progress_memory"
+type: "concept"
+status: "proposal"
+title: "事件敏感的任务进度记忆"
+created_at: "2026-07-19T12:18:53+08:00"
+updated_at: "2026-07-19T12:18:53+08:00"
+aliases: ["event-sensitive task-progress memory", "Temporally Conditioned Memory-Fusion Policy", "TFP", "dynamics-aware belief tracking"]
+tags: []
+domains: ["embodied-ai", "vla", "robot-memory", "visuomotor-control"]
+confidence: "medium"
+source_ids: ["source_011483b15aae65e849a3772e"]
+relations: [{"type": "derived_from", "target_id": "source_011483b15aae65e849a3772e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "DEHP 决定动作块何时重新查询，TFP 用真实经过时间和不规则查询间隔更新任务 belief；两者分别控制外部重规划节奏与内部记忆节奏。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都让快速事件响应与慢速上下文保持共存，但 TFP 跟踪视觉/本体任务进度，后者建模触觉预测与反应控制。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_011483b15aae65e849a3772e"
+uncertainty: "循环全量微调代价高，最大实验需 4 张 H200 约 80 小时；真机验证限于桌面单臂，不能直接外推到移动、全身或灵巧手。"
+---
+
+# 事件敏感的任务进度记忆
+
+用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。
```
