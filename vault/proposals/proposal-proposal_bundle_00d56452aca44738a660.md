---
id: "proposal_bundle_00d56452aca44738a660"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-24T18:06:44+08:00"
updated_at: "2026-07-24T18:40:19+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_3846f8c1451f8a12e0f87b33"]
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
extraction_id: "extraction_b8b75dd0216071846123cab5"
input_sha256: "a69631b5b009666d4a45cf3fc23092a582b5efab0e2f3db340f66cd986131aab"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_bcf39e7d937cfdf22e3c49e2", "target_path": "vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md", "base_sha256": "8fb2e5a7bc626ccb1843ef7d344e9b308bb30759d1f706efc0345d29cd95484d", "candidate_sha256": "3c6043b866f6999db617aef49b486f0470ce870ea7a83d56f45e6a51e1fbf069", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_00d56452aca44738a660-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_00d56452aca44738a660-concept-1.md", "exception_reasons": ["unclassified incremental change"], "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "concept_bcf39e7d937cfdf22e3c49e2", "type": "concept", "title": "面向真实零售人形机器人的数据高效 VLA 后训练闭环", "path": "vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md", "status": "working", "source_ids": ["source_3846f8c1451f8a12e0f87b33"], "snippet": "# 面向真实零售人形机器人的数据高效 VLA 后训练闭环\n\n在超市场景中部署预训练 VLA 时，可把控制频率对齐、数据筛选、任务相关视觉突出和降低对 VLA 主动作流依赖的后训练配方，与从当前策略失败状态收集的经验驱动细化结合；其目标是缩小实验室到门店的系统失配，而非证明这些组件可独立保证所有人形机器人任务的可靠性。", "match_reason": "metadata:aliases"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…offline iteration and online off-policy VLA [post-training] are distinct paths\n\n## Why important\n\nThe notes separate an…", "match_reason": "metadata:title"}, {"id": "reflection_3b2e99de9c8c6dfc2ba8cd5a", "type": "reflection", "title": "DEED：零售人形 VLA 的可靠性首先是部署系统问题", "path": "vault/reflections/reflection-reflection_3b2e99de9c8c6dfc2ba8cd5a.md", "status": "active", "source_ids": ["source_3846f8c1451f8a12e0f87b33"], "snippet": "# DEED：零售人形 VLA 的可靠性首先是部署系统问题\n\n## Why important\n\nDEED 把零售人形机器人的失效面放在控制频率、数据筛选、视觉重点和部署后经验回收的组合接口上；这为区分基础模型能力不足与系统集成失配提供了更可操作的诊断单位。\n\n## What changed\n\n先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上…", "match_reason": "metadata:domains"}, {"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for Force Accelerating VLA [Post-Training] with Reactive Force Injection Yi Wang 12* , Wendi Chen…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_3846f8c1451f8a12e0f87b33"}
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
- Extraction：`extraction_b8b75dd0216071846123cab5`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md
+++ candidate:vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_bcf39e7d937cfdf22e3c49e2"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "面向真实零售人形机器人的数据高效 VLA 后训练闭环"
 created_at: "2026-07-24T18:05:38+08:00"
-updated_at: "2026-07-24T18:05:39+08:00"
+updated_at: "2026-07-24T18:06:44+08:00"
 aliases: ["Data-Efficient Experience-Driven VLA Post-Training", "DEED", "数据高效经验驱动 VLA 后训练"]
 tags: []
 domains: ["humanoid-robotics", "vla", "post-training"]
 confidence: "medium"
 source_ids: ["source_3846f8c1451f8a12e0f87b33"]
-relations: [{"type": "derived_from", "target_id": "source_3846f8c1451f8a12e0f87b33", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者均讨论将 VLA 用于异构实体环境；DEED 具体限定部署后的频率、数据和经验接口，而该既有概念描述跨本体策略的一般输入输出接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_3846f8c1451f8a12e0f87b33", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者均讨论将 VLA 用于异构实体环境；DEED 具体限定部署后的频率、数据和经验接口，而该既有概念描述跨本体策略的一般输入输出接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者均讨论将 VLA 用于异构实体环境；DEED 具体限定部署后的频率、数据和经验接口，而该既有概念描述跨本体策略的一般输入输出接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_3846f8c1451f8a12e0f87b33"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_3b2e99de9c8c6dfc2ba8cd5a"], "importance": "high", "changed_belief": "先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上，控制与数据接口的对齐以及对策略自身失败状态的经验回收同样决定能否从朴素微调转为可用行为。", "surprising": "", "connections": [], "open_questions": ["文本 advantage 前缀和视觉语言价值函数在不同零售任务、不同经验比例下何时会避免或加剧自生成 rollout 主导训练分布的退化？"]}
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
-origin_proposal_id: "proposal_bundle_9186ea727626fb11fc36"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_9186ea727626fb11fc36-concept-1.md"
-origin_candidate_sha256: "f0ac2de44b73215afc46336043a5f819bd82a86cd53feeac2ee2f3c2e7b42c22"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 面向真实零售人形机器人的数据高效 VLA 后训练闭环
```
