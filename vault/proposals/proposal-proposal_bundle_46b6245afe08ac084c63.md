---
id: "proposal_bundle_46b6245afe08ac084c63"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-23T18:07:18+08:00"
updated_at: "2026-07-23T18:07:18+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5c29f310c66b0fb5c6cb2758"]
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
extraction_id: "extraction_0340a525c770f5ce73091b7e"
input_sha256: "70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_98b7ebb5d2382b61dd11bab3", "target_path": "vault/knowledge/concepts/concept_98b7ebb5d2382b61dd11bab3-带本体掩码的语义分组跨本体动作空间.md", "base_sha256": null, "candidate_sha256": "d46e55df09eade1640a52381c83f6c31d510c298ae0a72cbe825876545d331e7", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_46b6245afe08ac084c63-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_98b7ebb5d2382b61dd11bab3.md", "working_at": "2026-07-23T18:07:18+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5c29f310c66b0fb5c6cb2758"}
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
- Extraction：`extraction_0340a525c770f5ce73091b7e`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_98b7ebb5d2382b61dd11bab3-带本体掩码的语义分组跨本体动作空间.md
@@ -0,0 +1,20 @@
+---
+id: "concept_98b7ebb5d2382b61dd11bab3"
+type: "concept"
+status: "proposal"
+title: "带本体掩码的语义分组跨本体动作空间"
+created_at: "2026-07-23T18:07:18+08:00"
+updated_at: "2026-07-23T18:07:18+08:00"
+aliases: ["Embodiment-Masked Unified Action Space", "RynnBrain-VLA", "本体掩码统一动作空间"]
+tags: []
+domains: ["cross-embodiment", "vla", "grounding"]
+confidence: "medium"
+source_ids: ["source_5c29f310c66b0fb5c6cb2758"]
+relations: [{"type": "derived_from", "target_id": "source_5c29f310c66b0fb5c6cb2758", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "两者都试图在异构机器人之间建立可训练的共享表示；本概念以动作维度掩码保留控制接口的不兼容边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_5c29f310c66b0fb5c6cb2758"
+reflection_context: {"reflection_ids": ["reflection_a4b214ba9367da2f36ca1c06"], "importance": "high", "changed_belief": "跨本体训练不必强迫不兼容的动作空间逐维对齐；共享语义分组可以与本体特定掩码配合，但仍需要对各平台的真实控制结果单独验证。", "surprising": "", "connections": [], "open_questions": ["身体部位语义分组在接触、灵巧手和全身协调任务中何时会掩盖关键的本体差异？"]}
+---
+
+# 带本体掩码的语义分组跨本体动作空间
+
+跨本体 VLA 可将不同机器人的动作按语义对应的身体部位分组到共享动作空间，并用本体特定掩码仅激活每台机器人可用的维度，以支持联合训练而不要求不兼容控制接口逐维对齐。该设计仍须在具体机器人、任务和控制频率上验证其迁移收益。
```
