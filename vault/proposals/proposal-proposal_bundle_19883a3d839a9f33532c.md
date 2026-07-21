---
id: "proposal_bundle_19883a3d839a9f33532c"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T13:07:25+08:00"
updated_at: "2026-07-20T13:07:25+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_570c26541066c02080dd8de5"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-d-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_005be52e7c6fdbc7ba461e2b"
input_sha256: "ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_64c23c660c9017a5bf73d012", "target_path": "vault/memory/concept/concept_64c23c660c9017a5bf73d012.md", "base_sha256": "35843e55d53e4d5bac1d001609ab374b5a50e5cc4bbc2c3ffecfab572fd8098f", "candidate_sha256": "08d8be3b617ae2c41d1cdbfe94f19d3cf7979ebc0fee127f8f95212c0752c29f", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_19883a3d839a9f33532c-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_19883a3d839a9f33532c-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "work_arxiv_2606_26428", "type": "work", "title": "Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?", "path": "vault/memory/work/work_arxiv_2606_26428.md", "status": "working", "source_ids": ["source_05d8a9da9e0b53b94872f2a7", "source_ea5eb55121fccd1ed14a40b0"], "snippet": "…What Matters in [Dexterous] Play Pretraining for Precise Assembly?\n\n## Logical work identity\n\n- arXiv：`2606.26428`\n- Version：`unknown`\n- Captures…", "match_reason": "metadata:title"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…dexterous [teleoperation] through consecutive hand-object subgoals\n\n## Why important\n\nTELEDEXTER represents operator intent as consecutive hand-object co…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation Model for [Dexterous] Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "claim_play2perfect_realworld_tight_insertion_20260715", "type": "claim", "title": "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10", "path": "vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 的真实世界紧配合插入结果\n\n论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 real-world finetuning…", "match_reason": "metadata:tags"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:tags"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "…alignment 与安全约束纳入迁移目标和评测，直接暴露纯运动学 imitation 的物理缺口。\n\n## What changed\n\n此前人到机器人 [dexterous] transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。\n\n## Surprising\n\n纯运动学 baseline 的…", "match_reason": "metadata:domains"}, {"id": "concept_64c23c660c9017a5bf73d012", "type": "concept", "title": "Consecutive hand-object subgoal teleoperation", "path": "vault/memory/concept/concept_64c23c660c9017a5bf73d012.md", "status": "working", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "# Consecutive hand-object subgoal [teleoperation]\n\nTranslate live human intent into consecutive hand-object co-tracking subgoals, then let…", "match_reason": "metadata:title"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:tags"}, {"id": "reflection_65fb6fe12e2291077f28900c", "type": "reflection", "title": "DemoBridge: single-view demonstration transfer needs simulator-in-the-loop feasibility", "path": "vault/reflections/reflection-reflection_65fb6fe12e2291077f28900c.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…TELEDEXTER is live hand-object [teleoperation] with an RL contact controller; DemoBridge is offline single-view trajectory reconstruction…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_570c26541066c02080dd8de5"}
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

- Provider：`codex-gpt56-m91-daily-batch-d-20260720`
- Extraction：`extraction_005be52e7c6fdbc7ba461e2b`
- 编译前召回已有对象：9
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_64c23c660c9017a5bf73d012.md
+++ candidate:vault/memory/concept/concept_64c23c660c9017a5bf73d012.md
@@ -1,10 +1,10 @@
 ---
 id: "concept_64c23c660c9017a5bf73d012"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "Consecutive hand-object subgoal teleoperation"
 created_at: "2026-07-20T12:47:59+08:00"
-updated_at: "2026-07-20T12:47:59+08:00"
+updated_at: "2026-07-20T13:07:25+08:00"
 aliases: []
 tags: []
 domains: []
@@ -12,27 +12,9 @@
 source_ids: ["source_570c26541066c02080dd8de5"]
 relations: [{"type": "derived_from", "target_id": "source_570c26541066c02080dd8de5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-d-20260720", "status": "working"}]
 change_reason: "compile bundle from source_570c26541066c02080dd8de5"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_631ecd2479bd127e62730569"], "importance": "high", "changed_belief": "A teleoperation interface need not copy every human joint. Sparse joint hand-object targets can preserve task intent while leaving the robot freedom to reorganize contacts, perform finger gaiting, and satisfy embodiment constraints.", "surprising": "One co-tracking controller supports real-time teleoperation across two dexterous hands and seven tasks, and the collected demonstrations train autonomous policies; however, autonomous evaluation uses simplified task subsets.", "connections": [{"shared_mechanism": "Like progressive VLA demonstration curricula, it decomposes complex skills into intermediate targets that are easier to learn than a complete end-to-end trajectory.", "boundary": "The system depends on reliable MoCap estimates of hand and object pose, and simulation does not cover all tool-environment interactions. Contact jams, stalls, and out-of-distribution disturbances remain failure modes.", "difference": "A curriculum organizes data and task difficulty, whereas TELEDEXTER's consecutive subgoals are a live control interface executed by a low-level reinforcement-learning policy."}], "open_questions": ["How should subgoal tolerance encode completion, operator intent, and contact safety simultaneously?"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-daily-batch-d-20260720"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-daily-batch-d-20260720"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_0e0c7318a4fb8fb5bf1f"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0e0c7318a4fb8fb5bf1f-concept-1.md"
-origin_candidate_sha256: "9a04f819b32b8f63d6e093cd780ec6d5e0c94ba5566a08e37f51a01b43b5da62"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # Consecutive hand-object subgoal teleoperation
```
