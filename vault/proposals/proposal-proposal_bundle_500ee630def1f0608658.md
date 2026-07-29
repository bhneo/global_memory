---
id: "proposal_bundle_500ee630def1f0608658"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-25T18:06:31+08:00"
updated_at: "2026-07-25T18:06:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cc2f2812863ca6751c223b54"]
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
extraction_id: "extraction_fc1abc70524e79cc98092de2"
input_sha256: "5dbc9f88177d0d795eb9f880582fbf68281cb94c354334750e58f56e752bfb0f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_f35cd7f55e4108ce45ec35d7", "target_path": "vault/knowledge/concepts/concept_f35cd7f55e4108ce45ec35d7-面向异构机器人策略的能力边界路由与记忆交接.md", "base_sha256": null, "candidate_sha256": "c193110c51dd98d9462d3bfca1f376ac5ce52be7ba414e72158d11868b5b88fe", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_500ee630def1f0608658-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "working_at": "2026-07-25T18:06:32+08:00"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The common design question is where [heterogeneous] embodiments should be normalized.\n\n## What changed\n\nA robot foundation-model suite…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_cc2f2812863ca6751c223b54"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_fc1abc70524e79cc98092de2`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_f35cd7f55e4108ce45ec35d7-面向异构机器人策略的能力边界路由与记忆交接.md
@@ -0,0 +1,20 @@
+---
+id: "concept_f35cd7f55e4108ce45ec35d7"
+type: "concept"
+status: "proposal"
+title: "面向异构机器人策略的能力边界路由与记忆交接"
+created_at: "2026-07-25T18:06:31+08:00"
+updated_at: "2026-07-25T18:06:31+08:00"
+aliases: ["Capability-Aware Policy Routing and Memory Bridge", "RoboHarness", "异构策略记忆桥接"]
+tags: []
+domains: ["robot-planning", "policy-orchestration", "robot-memory"]
+confidence: "medium"
+source_ids: ["source_cc2f2812863ca6751c223b54"]
+relations: [{"type": "derived_from", "target_id": "source_cc2f2812863ca6751c223b54", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都将底层策略的适用范围与上层编排分开表达；RoboHarness 特别处理策略间状态分布交接，而该既有概念侧重把冻结 VLA 限为可重试的局部专家。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_cc2f2812863ca6751c223b54"
+reflection_context: {"reflection_ids": ["reflection_d3da57bd40bcce58fcac3b37"], "importance": "high", "changed_belief": "此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。", "surprising": "", "connections": [{"shared_mechanism": "两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。", "boundary": "该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。", "difference": "RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。"}], "open_questions": []}
+---
+
+# 面向异构机器人策略的能力边界路由与记忆交接
+
+RoboHarness 将独立开发的 VLA、强化学习和任务运动规划控制器封装为可路由模块，并用多模态执行记忆和在线证据估计各策略在当前子任务中的适用边界；在策略切换前，其 Memory Bridge 检索与下一策略相关的执行轨迹、估计该策略的分布内状态区域，并引导机器人接近该区域，以降低未经联合训练的控制器之间的状态分布错配。该机制的效果仍取决于能力估计、状态表示和检索轨迹对实际交接条件的覆盖。
```
