---
id: "proposal_bundle_999dbeaa03e05fb33b32"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T22:43:32+08:00"
updated_at: "2026-07-19T22:43:32+08:00"
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
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_90d52ab5e62d9847f9529875", "target_path": "vault/memory/concept/concept_90d52ab5e62d9847f9529875.md", "base_sha256": "fde11452a318aef36e58f78fa41dcac69557eed3a49c57b1d58a6a2f9a69ea11", "candidate_sha256": "92fafaf1c72a6ee3840ee4327c8e0b492931d2cf157643387282adee864c96f9", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_999dbeaa03e05fb33b32-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_999dbeaa03e05fb33b32-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "reflection_051f1a0f00d5131171df1440", "type": "reflection", "title": "Pelican-VLA 0.5：注意力泛化先于动作泛化", "path": "vault/reflections/reflection-reflection_051f1a0f00d5131171df1440.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277"], "snippet": "# [Pelican-VLA] 0.5：注意力泛化先于动作泛化\n\n## Why important\n\n它提供了诊断 VLA 泛化的新分层：模型可能已经跨场景和本体聚焦正确对象与接触区域，却仍不能把该表示稳定映射为成功动作，因此注意力命中不能直接当作零样本控制能力。\n\n## What changed\n\n此前常把任务相关视觉表示和动作泛化合并评价；该材料要求分别测量 attention…", "match_reason": "metadata:title"}, {"id": "concept_90d52ab5e62d9847f9529875", "type": "concept", "title": "VLA 注意力泛化—动作泛化缺口", "path": "vault/memory/concept/concept_90d52ab5e62d9847f9529875.md", "status": "working", "source_ids": ["source_3093a2f57587e962f87d6277"], "snippet": "# VLA 注意力泛化—动作泛化缺口\n\nVLA 可以在未见场景或本体中形成面向操作对象与接触区域的可迁移注意力，却仍缺少把这些区域稳定映射为可执行动作的能力；因此视觉注意力泛化与动作级成功必须分开评价。", "match_reason": "metadata:aliases"}, {"id": "synthesis_77d12a9c578c8e5a6223bff4", "type": "synthesis", "title": "具身泛化中的中间表示、接口解耦与动作落差", "path": "vault/synthesis/synthesis-synthesis_77d12a9c578c8e5a6223bff4.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277", "source_61f3045b170e78e4adb2422c", "source_886372de22c708b28cd11e4b", "source_be9781ec8ca637c5dfd8fabb", "source_d83bb2c45bcaf70906e9ac96"], "snippet": "…跨本体泛化应进一步分解为任务相关视觉/世界表示、跨本体共享的中间结构，以及本体特定动作解码与接触执行；注意力或世界表示的迁移证据不能直接推出动作级成功。\",\n    \"reason\": \"EGOWAM 将共享监督从动作转向世界变化，[Pelican-VLA] 区分注意力泛化与动作泛化，SkillPlug 则冻结共享技能并只适应轻量路由和动作头，三者共同要求把表示迁移与执行迁移拆开。\",\n    \"change_type\": \"refine\",\n    \"supporting…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_3093a2f57587e962f87d6277"}
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
- Extraction：`extraction_3ded34fd20e3c8744e9d32a9`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_90d52ab5e62d9847f9529875.md
+++ candidate:vault/memory/concept/concept_90d52ab5e62d9847f9529875.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_90d52ab5e62d9847f9529875"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "VLA 注意力泛化—动作泛化缺口"
 created_at: "2026-07-19T17:16:55+08:00"
-updated_at: "2026-07-19T17:16:55+08:00"
+updated_at: "2026-07-19T22:43:32+08:00"
 aliases: ["VLA Attention-to-Action Generalization Gap", "Attention-Level Generalization", "注意力到动作缺口", "Pelican-VLA"]
 tags: []
 domains: ["embodied-ai", "vla", "generalization"]
 confidence: "medium"
 source_ids: ["source_3093a2f57587e962f87d6277"]
-relations: [{"type": "derived_from", "target_id": "source_3093a2f57587e962f87d6277", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它指出跨本体视觉关注可先于可执行动作迁移，限制了仅凭表征或注意力证据声称通用策略成立。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_3093a2f57587e962f87d6277", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它指出跨本体视觉关注可先于可执行动作迁移，限制了仅凭表征或注意力证据声称通用策略成立。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它指出跨本体视觉关注可先于可执行动作迁移，限制了仅凭表征或注意力证据声称通用策略成立。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_3093a2f57587e962f87d6277"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_051f1a0f00d5131171df1440"], "importance": "high", "changed_belief": "此前常把任务相关视觉表示和动作泛化合并评价；该材料要求分别测量 attention-level generalization 与 attention-to-action transfer。", "surprising": "紧凑 Bottleneck Tokens 在没有对象标注、分割或注意力监督时形成操作相关注意力，而且微调前后注意模式相似，暗示微调主要强化表示到动作的映射。", "connections": [{"shared_mechanism": "都追求跨对象、场景、任务与本体共享任务相关视觉表示", "boundary": "连接只说明视觉表征可迁移，不表示统一动作空间或跨本体动力学已经解决", "difference": "通用 VLA 概念描述端到端跨本体策略目标，Pelican 的结果把其中的注意力表示能力与最终执行能力拆开评估"}], "open_questions": ["如何设计干预实验验证 Bottleneck Tokens 的注意力是否因果改善跨本体动作泛化？"]}
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
-origin_proposal_id: "proposal_bundle_0a0618dad0138fd4ccab"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0a0618dad0138fd4ccab-concept-1.md"
-origin_candidate_sha256: "18d0c78ff12508ac4f047669725613af7fadec3db353c84121f09a1ba504ab36"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # VLA 注意力泛化—动作泛化缺口
```
