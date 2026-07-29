---
id: "proposal_bundle_7c6f6222e085c52358ae"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-26T12:18:55+08:00"
updated_at: "2026-07-26T12:18:55+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_45c4de28acb4ba36642f1594"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-m91-weekly-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_d0c1f95522acbd043c3f7d2e"
input_sha256: "d0d9e9b8f4c7891b9b3b2b5f2448f72b5d9d4d70d5d284b72292996a17fe1346"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_648a44e346f991eab5956e55", "target_path": "vault/knowledge/concepts/concept_648a44e346f991eab5956e55-不可提升力预算下的语义恢复与快环权限分离.md", "base_sha256": null, "candidate_sha256": "84c515baa850606a9a51a1687e70ef3b32b076dc18c691662d53c0e9832a1f5b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_7c6f6222e085c52358ae-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_648a44e346f991eab5956e55.md", "working_at": "2026-07-26T12:18:55+08:00"}]
existing_context: [{"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…and asynchronous data collection, suggesting that throughput and [recovery] can dominate algorithm labels.\n\n## Connections\n\n- Shared mechanism: Both paths…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…feedback can select parameter adjustment, replanning, or exception [recovery].\n\n## Future directions\n\n- Audit the openJiuwen/jiuwensymbiosis repository and example…", "match_reason": "full-text:body"}, {"id": "input_4bec3f6febe9fd2b5e3f75e5", "type": "input", "title": "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation", "path": "vault/inputs/input-input_4bec3f6febe9fd2b5e3f75e5.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# [2607.15982] Data and Learning Where it Matters for [Contact-Rich] Manipulation\n\nInput Episode for `source_42e52a18cc082f3af087d574`. The…", "match_reason": "metadata:title"}, {"id": "concept_bfba032a868e0f7e1bcbe1d8", "type": "concept", "title": "接触关键段的数据聚焦学习", "path": "vault/memory/concept/concept_bfba032a868e0f7e1bcbe1d8.md", "status": "working", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# 接触关键段的数据聚焦学习\n\n在接触丰富操作中，用规划执行较简单的自由空间运动，并将自主数据采集与离线深度强化学习集中于决定接触成败的关键阶段。该设计的收益依赖于关键段划分、任务分布与采集系统，不能外推为所有操作任务都只需少量数据。", "match_reason": "metadata:aliases"}, {"id": "claim_play2perfect_finetuning_necessary_20260715", "type": "claim", "title": "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要", "path": "vault/memory/claim/claim_play2perfect_finetuning_necessary_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "…Play-only 为 0%。\n\n因此论文支持的结论是：play 预训练提供抓取和重定向先验，但在该 tight/[contact-rich] 装配设置中仍需要任务专用 RL 微调。它不意味着 Play-only 对所有装配任务均无效。", "match_reason": "metadata:tags"}, {"id": "concept_2ce226e08d585158c1dfbb18", "type": "concept", "title": "保留视觉语言先验的块内反应式力注入", "path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "status": "working", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。", "match_reason": "metadata:domains"}, {"id": "reflection_100e9d85ab1ae858496415ca", "type": "reflection", "title": "接触丰富操作：把数据密度限定在关键阶段", "path": "vault/reflections/reflection-reflection_100e9d85ab1ae858496415ca.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# 接触丰富操作：把数据密度限定在关键阶段\n\n## Why important\n\n该工作将高精度操作的数据需求按任务阶段划分：自由空间运动使用传统规划，接触关键段才以自动采集数据和离线强化学习优化，从而把数据预算与主要失败机制对齐。\n\n## What changed\n\n不应把端到端数据规模视作所有阶段同样受益；接触状态转换可能是需要高密度数据的局部瓶颈。\n\n## Surprising\n\n作者在四项实机任务中报告以 2–2.5 小时自主数据获得较高成功率…", "match_reason": "metadata:domains"}, {"id": "reflection_1f5ecace3c0b5fd265b9d846", "type": "reflection", "title": "LIFT：接触反馈可作为保留先验的块内反应接口", "path": "vault/reflections/reflection-reflection_1f5ecace3c0b5fd265b9d846.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "# LIFT：接触反馈可作为保留先验的块内反应接口\n\n## Why important\n\nLIFT 不重训视觉语言主干，而以零初始化残差把延迟对齐的近期六维力记忆注入并行反应分支；它把接触不确定性定位为可在动作块内刷新、且不必破坏预训练先验的接口问题。\n\n## What changed\n\n接触传感并非只能作为全模型重训的额外输入；若初始化时严格保持原动作输出，稀缺的在线力纠正可以针对策略实际访问的接触失败状态进行局部适配。\n\n## Surprising\n\nNot stated.\n\n## Connections…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_45c4de28acb4ba36642f1594"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "7496b4e69979dfc80abc6121b1c8f5e68cd245d00d654caada8eb5124e6839a5"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-m91-weekly-daily-v1`
- Extraction：`extraction_d0c1f95522acbd043c3f7d2e`
- 编译前召回已有对象：8
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_648a44e346f991eab5956e55-不可提升力预算下的语义恢复与快环权限分离.md
@@ -0,0 +1,20 @@
+---
+id: "concept_648a44e346f991eab5956e55"
+type: "concept"
+status: "proposal"
+title: "不可提升力预算下的语义恢复与快环权限分离"
+created_at: "2026-07-26T12:18:55+08:00"
+updated_at: "2026-07-26T12:18:55+08:00"
+aliases: ["Semantic Recovery with Immutable Force Budget and Fast-Loop Authority", "FORGE-plus", "力预算恢复权限分离"]
+tags: []
+domains: ["contact-rich-manipulation", "robot-safety", "failure-recovery"]
+confidence: "medium"
+source_ids: ["source_45c4de28acb4ba36642f1594"]
+relations: [{"type": "derived_from", "target_id": "source_45c4de28acb4ba36642f1594", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都让慢速代理只选择有界恢复原语并保留底层专家；FORGE-plus 进一步把不可提升的力预算和硬控制权限写成显式安全契约。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都使用快速力反馈处理接触失败；FORGE-plus 强调预算与恢复权限，既有概念强调在保留视觉语言先验时注入近期力记忆。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_45c4de28acb4ba36642f1594"
+reflection_context: {"reflection_ids": ["reflection_5eb9ba718b0b143e55d0b020"], "importance": "high", "changed_belief": "此前容易把硬 force clamp 视为足够的安全边界；论文结果表明命令被限制后，阻抗控制与接触瞬态仍可让峰值力超过预算，因此预算设置必须覆盖 overshoot 分布，恢复后下降轨迹也需要单独验证。", "surprising": "读取隐藏破坏阈值的 oracle ceiling 仍因接触 overshoot 破坏约一半脆弱部件，而更保守的身份派生预算在该仿真设置中零破坏；这说明接近真实阈值并不等于更安全。", "connections": [{"shared_mechanism": "FORGE-plus 与冻结 VLA 非对称技能编排都把语义层限制为选择有界原语，并把连续控制与安全权限留在低层可验证机制中。", "boundary": "连接适用于安全量可在快环测量、动作菜单有限且权限不可由语言输出提升的接触任务；当前证据仅来自刚体仿真与注入故障。", "difference": "FORGE-plus 明确冻结力预算并以 force/contact signature 选择恢复；既有编排概念更广泛地处理姿态重置、运输、验证与局部技能适用范围。"}], "open_questions": ["如何把接触 overshoot、恢复后更硬的力包络与部件材料不确定性纳入在线预算，而仍保持语义恢复层不能提高安全上限？"]}
+---
+
+# 不可提升力预算下的语义恢复与快环权限分离
+
+接触丰富装配可让慢速语义模块依据对象身份提出每对象力预算，并在失败时依据紧凑力与接触签名从固定恢复菜单中选择动作；实际命令饱和、全局硬上限和力权限必须留在高频控制环，恢复过程不得提高原始预算。该架构仍需测量命令力与接触峰值之间的 overshoot，并以仿真限定、注入故障和代理 baseline 的边界解释结果，不能把硬 clamp 当作真实接触力保证。
```
