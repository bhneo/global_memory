---
id: "proposal_bundle_f2f284ebec42eb596d26"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation"
created_at: "2026-07-22T18:11:50+08:00"
updated_at: "2026-07-22T18:11:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_42e52a18cc082f3af087d574"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_34a921c7eece9c798e3fb7fa"
input_sha256: "ece48cdf146f8397f4877b5f4fe1c97c28046ebebb3ea6376e6601d752eefd45"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_bfba032a868e0f7e1bcbe1d8", "target_path": "vault/knowledge/concepts/concept_bfba032a868e0f7e1bcbe1d8-接触关键段的数据聚焦学习.md", "base_sha256": null, "candidate_sha256": "c888b084b8bc6b3657551d83ee169c235a68a48001802937e3768a0f19fb439c", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_f2f284ebec42eb596d26-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_bfba032a868e0f7e1bcbe1d8.md", "working_at": "2026-07-22T18:11:51+08:00"}]
existing_context: [{"id": "input_4bec3f6febe9fd2b5e3f75e5", "type": "input", "title": "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation", "path": "vault/inputs/input-input_4bec3f6febe9fd2b5e3f75e5.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# [2607.15982] Data and Learning Where it Matters for [Contact-Rich] Manipulation\n\nInput Episode for `source_42e52a18cc082f3af087d574`. The…", "match_reason": "metadata:title"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2606_26428", "type": "work", "title": "Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?", "path": "vault/memory/work/work_arxiv_2606_26428.md", "status": "working", "source_ids": ["source_05d8a9da9e0b53b94872f2a7", "source_ea5eb55121fccd1ed14a40b0"], "snippet": "…What [Matters] in Dexterous Play Pretraining for Precise Assembly?\n\n## Logical work identity\n\n- arXiv：`2606.26428`\n- Version：`unknown`\n- Captures…", "match_reason": "metadata:title"}, {"id": "claim_play2perfect_finetuning_necessary_20260715", "type": "claim", "title": "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要", "path": "vault/memory/claim/claim_play2perfect_finetuning_necessary_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "…Play-only 为 0%。\n\n因此论文支持的结论是：play 预训练提供抓取和重定向先验，但在该 tight/[contact-rich] 装配设置中仍需要任务专用 RL 微调。它不意味着 Play-only 对所有装配任务均无效。", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_42e52a18cc082f3af087d574"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_34a921c7eece9c798e3fb7fa`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_bfba032a868e0f7e1bcbe1d8-接触关键段的数据聚焦学习.md
@@ -0,0 +1,20 @@
+---
+id: "concept_bfba032a868e0f7e1bcbe1d8"
+type: "concept"
+status: "proposal"
+title: "接触关键段的数据聚焦学习"
+created_at: "2026-07-22T18:11:50+08:00"
+updated_at: "2026-07-22T18:11:50+08:00"
+aliases: ["Data and Learning Where it Matters for Contact-Rich Manipulation", "Contact-Critical Data Focusing", "接触关键段学习"]
+tags: []
+domains: ["contact-rich-manipulation", "robot-learning"]
+confidence: "medium"
+source_ids: ["source_42e52a18cc082f3af087d574"]
+relations: [{"type": "derived_from", "target_id": "source_42e52a18cc082f3af087d574", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "两者都将实机执行数据视为受边界约束的反馈；前者规定数据应集中在哪个任务阶段。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_42e52a18cc082f3af087d574"
+reflection_context: {"reflection_ids": ["reflection_100e9d85ab1ae858496415ca"], "importance": "high", "changed_belief": "不应把端到端数据规模视作所有阶段同样受益；接触状态转换可能是需要高密度数据的局部瓶颈。", "surprising": "作者在四项实机任务中报告以 2–2.5 小时自主数据获得较高成功率，但这一结果受其任务、自动采集方案和离线 RL 设置约束。", "connections": [], "open_questions": ["关键接触段在未建模的新任务中能否可靠识别，而不遗漏决定成功的过渡状态？"]}
+---
+
+# 接触关键段的数据聚焦学习
+
+在接触丰富操作中，用规划执行较简单的自由空间运动，并将自主数据采集与离线深度强化学习集中于决定接触成败的关键阶段。该设计的收益依赖于关键段划分、任务分布与采集系统，不能外推为所有操作任务都只需少量数据。
```
