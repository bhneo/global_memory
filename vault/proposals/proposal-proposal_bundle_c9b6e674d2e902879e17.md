---
id: "proposal_bundle_c9b6e674d2e902879e17"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-25T18:07:35+08:00"
updated_at: "2026-07-25T18:07:36+08:00"
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
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_f35cd7f55e4108ce45ec35d7", "target_path": "vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md", "base_sha256": "64340fd5c189f6abe1edf9346e5fc184cb83ad4d453bee004fbefa6e237b1f2f", "candidate_sha256": "737d157e8584a82eefeb156a99574a433f46c79d953bc851ca9f98ac4bdbdcaa", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_c9b6e674d2e902879e17-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_c9b6e674d2e902879e17-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The common design question is where [heterogeneous] embodiments should be normalized.\n\n## What changed\n\nA robot foundation-model suite…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_cc2f2812863ca6751c223b54"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
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

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md
+++ candidate:vault/memory/concept/concept_f35cd7f55e4108ce45ec35d7.md
@@ -1,39 +1,20 @@
 ---
 id: "concept_f35cd7f55e4108ce45ec35d7"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "面向异构机器人策略的能力边界路由与记忆交接"
 created_at: "2026-07-25T18:06:31+08:00"
-updated_at: "2026-07-25T18:06:32+08:00"
+updated_at: "2026-07-25T18:07:35+08:00"
 aliases: ["Capability-Aware Policy Routing and Memory Bridge", "RoboHarness", "异构策略记忆桥接"]
 tags: []
 domains: ["robot-planning", "policy-orchestration", "robot-memory"]
 confidence: "medium"
 source_ids: ["source_cc2f2812863ca6751c223b54"]
-relations: [{"type": "derived_from", "target_id": "source_cc2f2812863ca6751c223b54", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都将底层策略的适用范围与上层编排分开表达；RoboHarness 特别处理策略间状态分布交接，而该既有概念侧重把冻结 VLA 限为可重试的局部专家。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_cc2f2812863ca6751c223b54", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都将底层策略的适用范围与上层编排分开表达；RoboHarness 特别处理策略间状态分布交接，而该既有概念侧重把冻结 VLA 限为可重试的局部专家。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都将底层策略的适用范围与上层编排分开表达；RoboHarness 特别处理策略间状态分布交接，而该既有概念侧重把冻结 VLA 限为可重试的局部专家。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_cc2f2812863ca6751c223b54"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_d3da57bd40bcce58fcac3b37"], "importance": "high", "changed_belief": "此前可能把异构策略组合主要理解为高层任务分解；本文强调，分解正确仍不足以保证可执行，跨策略交接必须显式处理状态分布错配。", "surprising": "", "connections": [{"shared_mechanism": "两者都把冻结或独立训练的控制模块置于更高层的适用范围管理与失败恢复接口之下。", "boundary": "该连接适用于存在可辨识子任务、可记录执行状态且能在切换前评估下一策略输入条件的长时程机器人系统。", "difference": "RoboHarness 以执行轨迹检索和空间分布学习来引导交接；既有冻结 VLA 编排概念以原语、验证与重试来约束局部专家。"}], "open_questions": []}
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
-origin_proposal_id: "proposal_bundle_500ee630def1f0608658"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_500ee630def1f0608658-concept-1.md"
-origin_candidate_sha256: "c193110c51dd98d9462d3bfca1f376ac5ce52be7ba414e72158d11868b5b88fe"
-origin_cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 面向异构机器人策略的能力边界路由与记忆交接
```
