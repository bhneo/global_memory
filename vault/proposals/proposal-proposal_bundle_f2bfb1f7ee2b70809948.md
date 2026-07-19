---
id: "proposal_bundle_f2bfb1f7ee2b70809948"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub"
created_at: "2026-07-19T03:37:31+08:00"
updated_at: "2026-07-19T03:37:46+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_34d6513b0522739d0b25e303"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_050b3e68335b770d39f1ba85"
input_sha256: "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_generalist_cross_embodiment_vla", "target_path": "vault/memory/concept/concept_generalist_cross_embodiment_vla.md", "base_sha256": "0b6a4da45fc7bda2b15232f5bf9071202c29530104108af98839c010ed0bcf3c", "candidate_sha256": "66ec8fcef93200be9be0f264007795c987c23d210ec6e307b87dee00a02026c2", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_f2bfb1f7ee2b70809948-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_f2bfb1f7ee2b70809948-concept-1.md", "working_path": "vault/memory/concept/concept_generalist_cross_embodiment_vla.md", "evolution_action": "metadata_only", "exception_id": null, "working_at": "2026-07-19T03:37:46+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_34d6513b0522739d0b25e303"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_050b3e68335b770d39f1ba85`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_generalist_cross_embodiment_vla.md
+++ candidate:vault/memory/concept/concept_generalist_cross_embodiment_vla.md
@@ -1,41 +1,19 @@
 ---
 id: "concept_generalist_cross_embodiment_vla"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "跨本体通用 VLA 策略"
 created_at: "2026-07-19T03:01:52+08:00"
-updated_at: "2026-07-19T03:27:40+08:00"
-aliases: []
+updated_at: "2026-07-19T03:37:31+08:00"
+aliases: ["generalist cross-embodiment VLA", "cross-embodiment policy"]
 tags: []
 domains: ["embodied-ai", "vla", "cross-embodiment", "humanoid"]
 confidence: "medium"
 source_ids: ["source_34d6513b0522739d0b25e303"]
 relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "跨本体通用策略需要处理共享表征与本体专属控制之间的对齐。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
 change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
-uncertainty: "通用性取决于训练数据、动作空间和具体部署支持，不能从项目定位推出任意机器人上的零样本泛化。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 3
-last_consolidated_at: "2026-07-19T03:27:40+08:00"
-last_verified_at: "2026-07-19T03:27:33+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_b42edda3bcd8367515cd"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-concept-1.md"
-origin_candidate_sha256: "53554fe46394c350e9f4d04c35326fd3a8a97dec6ff9e54c60121411cfe001df"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_1f175087ae575d6539485e63"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_34d6513b0522739d0b25e303", "trigger_source": "source_34d6513b0522739d0b25e303", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_34d6513b0522739d0b25e303", "trigger_source": "source_34d6513b0522739d0b25e303", "evidence_added": []}]
+change_type: "metadata_only"
+proposed_status: "working"
 ---
 
 # 跨本体通用 VLA 策略
```
