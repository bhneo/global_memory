---
id: "proposal_bundle_b43108e78a2a6116b029"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T10:47:14+08:00"
updated_at: "2026-07-27T10:47:15+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9ec7a0dfcdc6c43339383f13"]
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
extraction_id: "extraction_097f4df8f1fd4d9217b1bc96"
input_sha256: "1ed756f5eb8061fe4547cbb219087d47d0cee80c8bde779c189b19879a3955d8"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_d28c0e5c8a5f864e616e2f7a", "target_path": "vault/knowledge/concepts/concept_d28c0e5c8a5f864e616e2f7a-三次-nls-的波动动理学严格极限-rigorous-wave-kinetic-limit-for-cubic-nls.md", "base_sha256": null, "candidate_sha256": "5187efb5f75f79ce8d7758660bf81ea980a482d5f945fe2f2ad3830bb94bd9ac", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b43108e78a2a6116b029-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "working_at": "2026-07-27T10:47:15+08:00"}]
existing_context: [{"id": "concept_end_to_end_embodied_reproducibility", "type": "concept", "title": "端到端具身系统可复现性", "path": "vault/memory/concept/concept_end_to_end_embodied_reproducibility.md", "status": "working", "source_ids": ["source_650f616f1e641912e73115b1"], "snippet": "# 端到端具身系统可复现性\n\n把机械设计与物料清单、低层控制、数据转换、训练配方和推理部署视为同一可复现边界；只开放模型权重或微调代码不足以复现实机具身系统。", "match_reason": "metadata:aliases"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "# [hep-th/0603001] Holographic [Derivation] of Entanglement Entropy from AdS/CFT\n\nInput Episode for `source_6c0e05be9fc0c544826d7f9b`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_b6e3f29e044d376ac9465e43", "type": "input", "title": "[2504.06297] Comment on \"Hilbert's Sixth Problem: Derivation of Fluid Equations via Boltzmann's Kinetic Theory\" by Deng, Hani, and Ma", "path": "vault/inputs/input-input_b6e3f29e044d376ac9465e43.md", "status": "active", "source_ids": ["source_969253c160fba88bdba75603"], "snippet": "…Derivation of Fluid Equations via Boltzmann's [Kinetic] Theory\" by Deng, Hani, and Ma\n\nInput Episode for `source…", "match_reason": "metadata:title"}, {"id": "input_dc842109f2de463e2185e842", "type": "input", "title": "[2207.08358] Rigorous justification of the wave kinetic theory", "path": "vault/inputs/input-input_dc842109f2de463e2185e842.md", "status": "active", "source_ids": ["source_542db9d12c226d58c56b30fd"], "snippet": "# [2207.08358] Rigorous justification of the wave [kinetic] theory\n\nInput Episode for `source_542db9d12c226d58c56b30fd`. The immutable Source remains…", "match_reason": "metadata:title"}, {"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:domains"}, {"id": "concept_972e54ed590f8b093808209f", "type": "concept", "title": "Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit", "path": "vault/memory/concept/concept_972e54ed590f8b093808209f.md", "status": "working", "source_ids": ["source_408691502cdb43e7e2ea5c3b"], "snippet": "# Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit\n\n在满足 Boltzmann--Grad 标度的稀薄硬球系统中，经验密度可在短时收敛到 Boltzmann 方程解；围绕平均的适当缩放涨落可收敛到由线性化…", "match_reason": "metadata:domains"}, {"id": "concept_fb8af053ac360e94db141e7f", "type": "concept", "title": "Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure", "path": "vault/memory/concept/concept_fb8af053ac360e94db141e7f.md", "status": "working", "source_ids": ["source_6c565d5532cc4f2d0020ba4f"], "snippet": "# Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure\n\n对 Boltzmann 方程的 phi-divergence 矩闭合以受约束的 phi-divergence 最小化构造近似分布…", "match_reason": "metadata:domains"}, {"id": "reflection_bd92c5839c8839407acedd26", "type": "reflection", "title": "Hilbert 第六问题综述：不变流形方法把近似层级显式化", "path": "vault/reflections/reflection-reflection_bd92c5839c8839407acedd26.md", "status": "active", "source_ids": ["source_ca2fe79655cb6179fd2f7e6d"], "snippet": "# Hilbert 第六问题综述：不变流形方法把近似层级显式化\n\n## Why important\n\n该综述把从 Boltzmann 型动力学到流体方程的问题表述为分布空间中的慢不变流形，并比较 Chapman-Enskog 展开、直接不变性方程与 Newton 迭代；它提示推导是否可用取决于近似层级和短波边界，而不是只看形式展开是否存在。\n\n## What…", "match_reason": "metadata:domains"}, {"id": "reflection_404ada1db96fcd7ac7c81d9c", "type": "reflection", "title": "Hilbert 第六问题新论断：形式推导与物理适用性须分开审查", "path": "vault/reflections/reflection-reflection_404ada1db96fcd7ac7c81d9c.md", "status": "active", "source_ids": ["source_f0b67fcf01ccaf2e5e2807df"], "snippet": "# Hilbert 第六问题新论断：形式推导与物理适用性须分开审查\n\n## Why important\n\n该文宣称通过 Newton 到 Boltzmann 再到流体方程的组合极限完成 Hilbert 的计划，但库中已存在针对该论断的具体批评来源；它直接说明新颖、醒目的“解决”结论必须与其尺度条件、适用对象和独立反驳分开保存…", "match_reason": "metadata:domains"}, {"id": "reflection_344908985fd536d0a4035c24", "type": "reflection", "title": "Boltzmann--Grad 涨落：典型行为、中心极限与大偏差属于不同层级", "path": "vault/reflections/reflection-reflection_344908985fd536d0a4035c24.md", "status": "active", "source_ids": ["source_408691502cdb43e7e2ea5c3b"], "snippet": "# Boltzmann--Grad 涨落：典型行为、中心极限与大偏差属于不同层级\n\n## Why important\n\n论文在低密度硬球极限下并列给出经验密度的 Boltzmann 大数律、涨落场到带噪线性化 Boltzmann 方程的中心极限，以及短时大偏差泛函；它把从确定性微观动力学到随机有效描述分成可分别检验的三个统计层级。\n\n## What changed\n\n我会避免把…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9ec7a0dfcdc6c43339383f13"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "4451ba8095f3fddeba82a9383e77828628ba8be1be6dd8738784909274a4c30c"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_097f4df8f1fd4d9217b1bc96`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_d28c0e5c8a5f864e616e2f7a-三次-nls-的波动动理学严格极限-rigorous-wave-kinetic-limit-for-cubic-nls.md
@@ -0,0 +1,20 @@
+---
+id: "concept_d28c0e5c8a5f864e616e2f7a"
+type: "concept"
+status: "proposal"
+title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
+created_at: "2026-07-27T10:47:14+08:00"
+updated_at: "2026-07-27T10:47:14+08:00"
+aliases: ["wave kinetic equation", "cubic NLS kinetic limit", "波动动理学方程", "三次 NLS 动理学极限"]
+tags: []
+domains: ["wave-turbulence", "kinetic-theory", "nonlinear-schrodinger-equation"]
+confidence: "high"
+source_ids: ["source_9ec7a0dfcdc6c43339383f13"]
+relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_9ec7a0dfcdc6c43339383f13"
+reflection_context: {"reflection_ids": ["reflection_039e793833ff803621c37f30"], "importance": "high", "changed_belief": "我会把波动动理学方程看作与盒尺度、耦合强度和观察时间共同定义的有效描述，而不是任意弱非线性波的普适长时方程。", "surprising": "", "connections": [{"shared_mechanism": "它与 Boltzmann--Grad 涨落层级都通过协同极限将确定性微观或介观演化连接到统计动理学方程。", "boundary": "该结果针对三次 NLS、d≥3、α∼L⁻¹ 和动理学时间的固定倍数。", "difference": "硬球结果依赖粒子低密度与碰撞半径标度；波动结果依赖大盒极限和弱非线性共振结构。"}], "open_questions": []}
+---
+
+# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS
+
+对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。
```
