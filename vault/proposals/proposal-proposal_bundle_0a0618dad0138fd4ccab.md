---
id: "proposal_bundle_0a0618dad0138fd4ccab"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T17:16:55+08:00"
updated_at: "2026-07-19T17:16:55+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_3093a2f57587e962f87d6277"]
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
extraction_id: "extraction_3ded34fd20e3c8744e9d32a9"
input_sha256: "0cc9e6e229a225d3e2abc51f84e24397902379210c94f432ac0854896d8677ad"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_90d52ab5e62d9847f9529875", "target_path": "vault/knowledge/concepts/concept_90d52ab5e62d9847f9529875-vla-注意力泛化-动作泛化缺口.md", "base_sha256": null, "candidate_sha256": "18d0c78ff12508ac4f047669725613af7fadec3db353c84121f09a1ba504ab36", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0a0618dad0138fd4ccab-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_90d52ab5e62d9847f9529875.md", "working_at": "2026-07-19T17:16:55+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_3093a2f57587e962f87d6277"}
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
- Extraction：`extraction_3ded34fd20e3c8744e9d32a9`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_90d52ab5e62d9847f9529875-vla-注意力泛化-动作泛化缺口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_90d52ab5e62d9847f9529875"
+type: "concept"
+status: "proposal"
+title: "VLA 注意力泛化—动作泛化缺口"
+created_at: "2026-07-19T17:16:55+08:00"
+updated_at: "2026-07-19T17:16:55+08:00"
+aliases: ["VLA Attention-to-Action Generalization Gap", "Attention-Level Generalization", "注意力到动作缺口", "Pelican-VLA"]
+tags: []
+domains: ["embodied-ai", "vla", "generalization"]
+confidence: "medium"
+source_ids: ["source_3093a2f57587e962f87d6277"]
+relations: [{"type": "derived_from", "target_id": "source_3093a2f57587e962f87d6277", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它指出跨本体视觉关注可先于可执行动作迁移，限制了仅凭表征或注意力证据声称通用策略成立。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_3093a2f57587e962f87d6277"
+reflection_context: {"reflection_ids": ["reflection_051f1a0f00d5131171df1440"], "importance": "high", "changed_belief": "此前常把任务相关视觉表示和动作泛化合并评价；该材料要求分别测量 attention-level generalization 与 attention-to-action transfer。", "surprising": "紧凑 Bottleneck Tokens 在没有对象标注、分割或注意力监督时形成操作相关注意力，而且微调前后注意模式相似，暗示微调主要强化表示到动作的映射。", "connections": [{"shared_mechanism": "都追求跨对象、场景、任务与本体共享任务相关视觉表示", "boundary": "连接只说明视觉表征可迁移，不表示统一动作空间或跨本体动力学已经解决", "difference": "通用 VLA 概念描述端到端跨本体策略目标，Pelican 的结果把其中的注意力表示能力与最终执行能力拆开评估"}], "open_questions": ["如何设计干预实验验证 Bottleneck Tokens 的注意力是否因果改善跨本体动作泛化？"]}
+---
+
+# VLA 注意力泛化—动作泛化缺口
+
+VLA 可以在未见场景或本体中形成面向操作对象与接触区域的可迁移注意力，却仍缺少把这些区域稳定映射为可执行动作的能力；因此视觉注意力泛化与动作级成功必须分开评价。
```
