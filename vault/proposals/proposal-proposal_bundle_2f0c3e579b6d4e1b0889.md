---
id: "proposal_bundle_2f0c3e579b6d4e1b0889"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:17:39+08:00"
updated_at: "2026-07-19T12:17:39+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_650f616f1e641912e73115b1"]
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
extraction_id: "extraction_ca52a93bed1b499eeacdbbbd"
input_sha256: "3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_end_to_end_embodied_reproducibility", "target_path": "vault/knowledge/concepts/concept_end_to_end_embodied_reproducibility-端到端具身系统可复现性.md", "base_sha256": null, "candidate_sha256": "cdb20dafd73bbc8161c49ff6d972bbd3bc177c85f4d705503a7d19a5d6561e8b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_2f0c3e579b6d4e1b0889-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_end_to_end_embodied_reproducibility.md", "working_at": "2026-07-19T12:17:39+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_650f616f1e641912e73115b1"}
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
- Extraction：`extraction_ca52a93bed1b499eeacdbbbd`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_end_to_end_embodied_reproducibility-端到端具身系统可复现性.md
@@ -0,0 +1,20 @@
+---
+id: "concept_end_to_end_embodied_reproducibility"
+type: "concept"
+status: "proposal"
+title: "端到端具身系统可复现性"
+created_at: "2026-07-19T12:17:39+08:00"
+updated_at: "2026-07-19T12:17:39+08:00"
+aliases: ["end-to-end embodied-system reproducibility", "embodied AI full-stack reproducibility", "E2E embodied reproducibility"]
+tags: []
+domains: ["embodied-ai", "robotics", "reproducibility", "vla"]
+confidence: "medium"
+source_ids: ["source_650f616f1e641912e73115b1"]
+relations: [{"type": "derived_from", "target_id": "source_650f616f1e641912e73115b1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_embodied_data_loop", "reason": "OpenEAI-Platform 把遥操作采集、统一数据转换、两阶段训练、控制与实机评估实现为一条可复现链路，是具身数据闭环的具体系统实例。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "统一状态与动作接口及 dataset-specific adapters 处理异构数据约定，为跨本体策略提供数据侧对齐机制，但论文实机验证仍集中在其自研机械臂。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_650f616f1e641912e73115b1"
+uncertainty: "论文称代码、布局和模型将在录用后发布；当前材料能支持系统设计与实验报告，不能替代对全部发布资产可复现性的独立验证。"
+---
+
+# 端到端具身系统可复现性
+
+把机械设计与物料清单、低层控制、数据转换、训练配方和推理部署视为同一可复现边界；只开放模型权重或微调代码不足以复现实机具身系统。
```
