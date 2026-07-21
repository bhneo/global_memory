---
id: "proposal_bundle_5fb31f3b84fd4a7f4a66"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T13:34:33+08:00"
updated_at: "2026-07-20T13:34:52+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4b25f596c34869693b9b8151"]
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
extraction_id: "extraction_e4434d4c771a07ac28174166"
input_sha256: "95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_17750931a381f8453b27ccba", "target_path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "base_sha256": "3b42da0c3f4062d2fa8ac03ebbb97fcfcad90419bfce91e42ee8654331d048f4", "candidate_sha256": "e3a068daa48bbe20864c1161f91802b6cd0f366273601dc582a382e8369c1925", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_5fb31f3b84fd4a7f4a66-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_5fb31f3b84fd4a7f4a66-concept-1.md", "working_path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-20T13:34:52+08:00"}]
existing_context: [{"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline [Policy]：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:title"}, {"id": "concept_17750931a381f8453b27ccba", "type": "concept", "title": "连续曲线动作接口与执行重定时", "path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "status": "working", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "match_reason": "metadata:aliases"}, {"id": "synthesis_60071a24c6e3071f6731c4e2", "type": "synthesis", "title": "VLA 后训练、动作观察接口与世界模型：分布、表示、反馈和可执行性", "path": "vault/synthesis/synthesis-synthesis_60071a24c6e3071f6731c4e2.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220", "source_4b25f596c34869693b9b8151", "source_4df1017326dd7cc4786f4218", "source_5b8c57a9bef3348109f3b7bb", "source_8b41a014bee47c4239a2fa81", "source_b64b4a539b8c17d0cfe662ba", "source_e6608d8f849ad472bbd95143", "source_ef80ef223077ef0855660839", "source_f4bd7390e1b485ab773f1446", "source_f9128ff3463cfaa7fa41ee7e", "source_fe986df678d73ef2b6234f0c"], "snippet": "…连续 [B-spline] 曲线把轨迹几何、控制频率和执行时标解耦。\",\n    \"proposed\": \"连续曲线重定时与 PAC-ACT 的动作块信用分配位于同一时间接口的不同侧：前者定义执行轨迹，后者定义优化决策单位；两者都必须受接触风险和纠正延迟约束。\",\n    \"reason\": \"[B-spline] Policy 的表示重定时为既有…", "match_reason": "full-text:body"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…offline iteration and online off-[policy] VLA post-training are distinct paths\n\n## Why important\n\nThe notes separate an…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-Robot separates navigation, [manipulation], and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation Model for Dexterous [Manipulation]\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4b25f596c34869693b9b8151"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_e4434d4c771a07ac28174166`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_17750931a381f8453b27ccba.md
+++ candidate:vault/memory/concept/concept_17750931a381f8453b27ccba.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_17750931a381f8453b27ccba"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "连续曲线动作接口与执行重定时"
 created_at: "2026-07-20T12:27:52+08:00"
-updated_at: "2026-07-20T12:27:53+08:00"
+updated_at: "2026-07-20T13:34:33+08:00"
 aliases: ["Continuous action curve interface", "B-spline action representation", "B-spline Policy", "动作曲线重定时"]
 tags: []
 domains: ["embodied-ai", "visuomotor-policy", "action-representation", "fast-manipulation"]
 confidence: "high"
 source_ids: ["source_4b25f596c34869693b9b8151"]
-relations: [{"type": "derived_from", "target_id": "source_4b25f596c34869693b9b8151", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "二者都调整策略重规划与执行的时间接口；连续曲线通过重定时，动态时域通过选择动作块前缀长度。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_4b25f596c34869693b9b8151", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "二者都调整策略重规划与执行的时间接口；连续曲线通过重定时，动态时域通过选择动作块前缀长度。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "reason": "B-spline Policy 解耦轨迹几何与执行时标，PAC-ACT 对齐动作块生成与价值/优势时间单位；二者分别解决执行表示与后训练信用分配。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_4b25f596c34869693b9b8151"
-reflection_context: {"reflection_ids": ["reflection_0078f804e87c7ed12f88876d"], "importance": "high", "changed_belief": "此前动作块加速常被理解为少重规划或少执行几步；BSP 表明，动作表示本身可以把轨迹几何、控制频率和执行时标分离，从而在不为每个速度重训策略的情况下重定时。", "surprising": "在 Table Cleaning 的一个 4× 设置中，完成时间从 23.57 秒降至 11.80 秒且成功次数近似保持；但 Speed Stacking 在 4× 时成功率归零，清楚暴露出表示可重定时不等于硬件可无限加速。", "connections": [{"shared_mechanism": "与动态动作块执行时域都依据执行阶段调整重规划与动作执行之间的时间接口，以兼顾自由空间速度和接触阶段反应性。", "boundary": "BSP 的高倍加速受低层控制器、执行器和接触动态限制；论文结果不能推出任意策略或硬件都能保持几何轨迹后安全重定时。", "difference": "动态执行时域从离散动作块中选择执行前缀长度；BSP 直接改变策略输出为连续曲线，并通过时间缩放和段间对齐实现高速连续控制。"}], "open_questions": ["能否依据接触风险、跟踪误差和策略不确定性在线选择 B-spline 时间缩放，而不是预设固定倍速？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-daily-batch-a-20260720"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-daily-batch-a-20260720"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_d9174a0dee6839b15e85"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_d9174a0dee6839b15e85-concept-1.md"
-origin_candidate_sha256: "3220cbffa7e3e6839d98150bfd2d1e72fe4a6ebf1e8f5552622a617d34473bbf"
-memory_schema_version: 2
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_0078f804e87c7ed12f88876d"], "importance": "weekly", "changed_belief": "此前动作块加速常被理解为少重规划或少执行几步；BSP 表明，动作表示本身可以把轨迹几何、控制频率和执行时标分离，从而在不为每个速度重训策略的情况下重定时。", "surprising": "在 Table Cleaning 的一个 4× 设置中，完成时间从 23.57 秒降至 11.80 秒且成功次数近似保持；但 Speed Stacking 在 4× 时成功率归零，清楚暴露出表示可重定时不等于硬件可无限加速。", "connections": [{"shared_mechanism": "与动态动作块执行时域都依据执行阶段调整重规划与动作执行之间的时间接口，以兼顾自由空间速度和接触阶段反应性。", "boundary": "BSP 的高倍加速受低层控制器、执行器和接触动态限制；论文结果不能推出任意策略或硬件都能保持几何轨迹后安全重定时。", "difference": "动态执行时域从离散动作块中选择执行前缀长度；BSP 直接改变策略输出为连续曲线，并通过时间缩放和段间对齐实现高速连续控制。"}], "open_questions": ["能否依据接触风险、跟踪误差和策略不确定性在线选择 B-spline 时间缩放，而不是预设固定倍速？"]}
+proposed_status: "working"
 ---
 
 # 连续曲线动作接口与执行重定时
```
