---
id: "proposal_bundle_896076b01406d7be4d12"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-23T18:06:46+08:00"
updated_at: "2026-07-23T18:06:46+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cdce2dfd2021019fc46a9ea7"]
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
extraction_id: "extraction_7403aec3003862569f9c95c8"
input_sha256: "d472f231a0ec73b791ec3ca8b395ea72270bf939907be8b243d3e574974b63dd"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_3363773a8f142fcedd29ce9d", "target_path": "vault/knowledge/concepts/concept_3363773a8f142fcedd29ce9d-训练-模型-部署三分布的操作鲁棒性诊断.md", "base_sha256": null, "candidate_sha256": "8c53cf7a7d976307e0b126d0d3588b482544bef5e7957bdb146de9d0a272ce4b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_896076b01406d7be4d12-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_3363773a8f142fcedd29ce9d.md", "working_at": "2026-07-23T18:06:46+08:00"}]
existing_context: [{"id": "input_4bec3f6febe9fd2b5e3f75e5", "type": "input", "title": "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation", "path": "vault/inputs/input-input_4bec3f6febe9fd2b5e3f75e5.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# [2607.15982] Data and Learning Where it Matters for Contact-Rich [Manipulation]\n\nInput Episode for `source_42e52a18cc082f3af087d574`. The…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-Robot separates navigation, [manipulation], and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation Model for Dexterous [Manipulation]\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "…Vision-Driven Embodied Agents for Open-World Mobile [Manipulation] · GitHub\n\nInput Episode for `source_a5f8ae205338d5f97eea87c7`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_cdce2dfd2021019fc46a9ea7"}
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
- Extraction：`extraction_7403aec3003862569f9c95c8`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_3363773a8f142fcedd29ce9d-训练-模型-部署三分布的操作鲁棒性诊断.md
@@ -0,0 +1,20 @@
+---
+id: "concept_3363773a8f142fcedd29ce9d"
+type: "concept"
+status: "proposal"
+title: "训练—模型—部署三分布的操作鲁棒性诊断"
+created_at: "2026-07-23T18:06:46+08:00"
+updated_at: "2026-07-23T18:06:46+08:00"
+aliases: ["Train-Model-Deployment Distribution Diagnosis", "χ0", "训练模型部署分布诊断"]
+tags: []
+domains: ["robot-learning", "robust-manipulation"]
+confidence: "medium"
+source_ids: ["source_cdce2dfd2021019fc46a9ea7"]
+relations: [{"type": "derived_from", "target_id": "source_cdce2dfd2021019fc46a9ea7", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "两者都要求以实机执行数据定位训练与部署的差异；本概念额外区分模型归纳偏置这一中间边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_cdce2dfd2021019fc46a9ea7"
+reflection_context: {"reflection_ids": ["reflection_1f4ab26f44d5ff91048664cc"], "importance": "high", "changed_belief": "资源规模不是部署鲁棒性的唯一解释变量；同一策略可能在训练数据覆盖、动作采样和执行时延三个边界上分别失配。", "surprising": "", "connections": [{"shared_mechanism": "两者都把实机执行反馈视为训练闭环中需要显式建模的分布来源。", "boundary": "该连接只适用于将训练策略部署到有时延和扰动的物理系统，不证明特定对齐模块可迁移到所有机器人或任务。", "difference": "χ0 将失配细分为训练、模型和部署三种分布；既有实机迭代概念强调采集—训练—验证循环的操作流程。"}], "open_questions": []}
+---
+
+# 训练—模型—部署三分布的操作鲁棒性诊断
+
+在长时程机器人操作中，分别检查专家演示训练分布、策略学习到的归纳偏置和实机执行轨迹分布之间的失配；对齐措施应标明其针对数据覆盖、动作采样还是推理—执行时延。该诊断框架不意味着三个分布可被完全观测或由单一指标消除。
```
