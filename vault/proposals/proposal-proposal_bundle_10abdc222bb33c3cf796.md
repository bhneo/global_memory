---
id: "proposal_bundle_10abdc222bb33c3cf796"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.08436v1.pdf"
created_at: "2026-07-19T22:43:22+08:00"
updated_at: "2026-07-19T22:43:22+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_61f3045b170e78e4adb2422c"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.08436v1.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_1ed8e5ff2c0f461bac3094e9"
input_sha256: "dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_ab253cb9064bc1b550d5e973", "target_path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "base_sha256": "1891b768a336db1da9e10261ed20d4294b3746343b91d763d8920de0956aa100", "candidate_sha256": "4e3369f70e68801b92880f58dd57a72ccc714fbaaf62e24dee087038a179787e", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_10abdc222bb33c3cf796-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_10abdc222bb33c3cf796-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "input_5d285e86b54c2cafe7458888", "type": "input", "title": "2607.08436v1.pdf", "path": "vault/inputs/input-input_5d285e86b54c2cafe7458888.md", "status": "active", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.08436v1.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/dc/da/dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "reflection_0dd383cc873ce81c0afd3d06", "type": "reflection", "title": "EGOWAM：跨本体迁移应优先共享世界变化而不是动作", "path": "vault/reflections/reflection-reflection_0dd383cc873ce81c0afd3d06.md", "status": "active", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "…通用 VLA 侧重统一策略输入输出接口，[EGOWAM] 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式\n\n## Conflicts\n\n- 世界表示越抽象越可能丢失接触级控制细节；3D flow 与 DINO 的优势可能随任务分布变化\n\n## Open questions\n\n- 什么 world target 能同时保留接触动力学…", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "synthesis_77d12a9c578c8e5a6223bff4", "type": "synthesis", "title": "具身泛化中的中间表示、接口解耦与动作落差", "path": "vault/synthesis/synthesis-synthesis_77d12a9c578c8e5a6223bff4.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277", "source_61f3045b170e78e4adb2422c", "source_886372de22c708b28cd11e4b", "source_be9781ec8ca637c5dfd8fabb", "source_d83bb2c45bcaf70906e9ac96"], "snippet": "…并通过跨形态数据支持迁移。\",\n    \"proposed\": \"跨本体泛化应进一步分解为任务相关视觉/世界表示、跨本体共享的中间结构，以及本体特定动作解码与接触执行；注意力或世界表示的迁移证据不能直接推出动作级成功。\",\n    \"reason\": \"[EGOWAM] 将共享监督从动作转向世界变化，Pelican-VLA 区分注意力泛化与动作泛化，SkillPlug 则冻结共享技能并只适应轻量路由和动作头，三者共同要求把表示迁移与执行迁移拆开。\",\n    \"change_type…", "match_reason": "full-text:body"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "claim_6ed5013981fdc75c87eb19c9", "type": "claim", "title": "real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×", "path": "vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# real-[world] environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference…", "match_reason": "metadata:title"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:aliases"}, {"id": "claim_0534c95e4004502bb928fc9e", "type": "claim", "title": "34.43× for representative flow-based VLA models, π0.5", "path": "vault/memory/claim/claim_0534c95e4004502bb928fc9e.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# 34.43× for representative flow-based VLA [models], π0.5\n\n34.43× for representative flow-based VLA [models]…", "match_reason": "metadata:title"}, {"id": "claim_4b17c3d6e1aa3af61a3c70d4", "type": "claim", "title": "These trends indicate that improving VLA models in practice requires a coordinated treatment of data, embodiment,", "path": "vault/memory/claim/claim_4b17c3d6e1aa3af61a3c70d4.md", "status": "working", "source_ids": ["source_233c4bef3a727389ddf81ae2"], "snippet": "# These trends indicate that improving VLA [models] in practice requires a coordinated treatment of data, embodiment,\n\nThese trends…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_61f3045b170e78e4adb2422c"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.08436v1.pdf

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_1ed8e5ff2c0f461bac3094e9`
- 编译前召回已有对象：9
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md
+++ candidate:vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_ab253cb9064bc1b550d5e973"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "跨本体世界监督通道"
 created_at: "2026-07-19T17:16:45+08:00"
-updated_at: "2026-07-19T17:16:45+08:00"
+updated_at: "2026-07-19T22:43:22+08:00"
 aliases: ["Cross-Embodiment World Supervision Channel", "Embodiment-Invariant World Target", "EGOWAM", "World Action Model"]
 tags: []
 domains: ["embodied-ai", "world-model", "cross-embodiment"]
 confidence: "medium"
 source_ids: ["source_61f3045b170e78e4adb2422c"]
-relations: [{"type": "derived_from", "target_id": "source_61f3045b170e78e4adb2422c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它把跨本体通用策略进一步分解为世界监督共享与动作执行对齐两个通道，并明确前者的表示条件。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_61f3045b170e78e4adb2422c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它把跨本体通用策略进一步分解为世界监督共享与动作执行对齐两个通道，并明确前者的表示条件。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "它把跨本体通用策略进一步分解为世界监督共享与动作执行对齐两个通道，并明确前者的表示条件。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_61f3045b170e78e4adb2422c"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_0dd383cc873ce81c0afd3d06"], "importance": "high", "changed_belief": "此前跨本体 VLA 更强调统一动作接口或数据混合；该材料提示应先选择能抽象外观、保持跨本体一致并分离相机运动的 world target，再讨论动作对齐。", "surprising": "该受控比较中像素重建迁移较弱，而 DINO 特征和 3D flow 的收益方向不同，说明“增加世界模型头”本身不够，预测目标的抽象层级决定迁移内容。", "connections": [{"shared_mechanism": "都试图从多形态数据中保留任务语义和物理效果，同时隔离本体特有的执行因素", "boundary": "连接只覆盖跨本体表示共享，不意味着世界监督可以替代机器人动作数据或解决控制精度", "difference": "通用 VLA 侧重统一策略输入输出接口，EGOWAM 侧重用辅助世界预测通道改变共享骨干接收人类数据的方式"}], "open_questions": ["什么 world target 能同时保留接触动力学、分离 ego-motion 并跨不同机器人相机布局迁移？"]}
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
-origin_proposal_id: "proposal_bundle_17351093fa01d5d557d9"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_17351093fa01d5d557d9-concept-1.md"
-origin_candidate_sha256: "9e2142a0223206a27470315708c118b5dac89b7ae370dae8979e36ea60bb3870"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 跨本体世界监督通道
```
