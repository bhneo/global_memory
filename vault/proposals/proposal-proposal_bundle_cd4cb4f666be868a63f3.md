---
id: "proposal_bundle_cd4cb4f666be868a63f3"
type: "proposal"
status: "migrated"
title: "Compile bundle：[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$"
created_at: "2026-07-28T10:17:54+08:00"
updated_at: "2026-07-28T10:17:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b2c6c3d707b387d0dbad6dbc"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e5b07cd2ccd80e4caf9af5d4"
input_sha256: "4163e7e82a70698bf8ee765df720b8b5b0c2b96ee5ab64e50bcacc5f4121f354"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_2de4832c73aa726ac94ca956", "target_path": "vault/knowledge/concepts/concept_2de4832c73aa726ac94ca956-r4-polynomial-wolff-公理下的条件化管并集体积界-conditional-tube-union-bounds-.md", "base_sha256": null, "candidate_sha256": "eab9efddc523e1dbd1739390699f3188dc9b73aa3cc781789095fa972aa6a5c1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_cd4cb4f666be868a63f3-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_2de4832c73aa726ac94ca956.md", "working_at": "2026-07-28T10:17:57+08:00"}]
existing_context: [{"id": "input_696ed17b934899983e8f639c", "type": "input", "title": "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$", "path": "vault/inputs/input-input_696ed17b934899983e8f639c.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "# [1701.07045] Polynomial Wolff axioms and Kakeya-type [estimates] in $\\mathbb{R}^4$\n\nInput Episode for `source_b2c6c3d707b387d0dbad6dbc…", "match_reason": "metadata:title"}, {"id": "concept_9ba11c3fe75d6cae3c970ff4", "type": "concept", "title": "高维 Kakeya 的递归多尺度 polynomial Wolff 机制 / recursive multiscale polynomial-Wolff mechanism for higher-dimensional Kakeya", "path": "vault/memory/concept/concept_9ba11c3fe75d6cae3c970ff4.md", "status": "working", "source_ids": ["source_e480d57998401d152443b4ad"], "snippet": "…型 polynomial partitioning 写成递归算法，使归纳过程中暴露的不同尺度几何信息不被压缩掉，并将其组织为多尺度 polynomial Wolff [axioms]。论文摘要报告该机制改进 n=5 或 n≥7 的 Kakeya maximal…", "match_reason": "metadata:aliases"}, {"id": "reflection_8bed5c9d4ce32f9a4412f334", "type": "reflection", "title": "R4 polynomial Wolff 条件：条件化体积界不能替代 Kakeya 猜想 / polynomial Wolff bounds remain conditional", "path": "vault/reflections/reflection-reflection_8bed5c9d4ce32f9a4412f334.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "…conditional\n\n## Why important\n\n该文的 R4 管并集体积和多线性界依赖 polynomial Wolff [axioms]，并明确把“每个 Kakeya 集满足该条件”留作未证猜想；条件化估计不能被读成 R4 Kakeya 猜想已解…", "match_reason": "full-text:body"}, {"id": "reflection_3161177e53e4d63befa4efbe", "type": "reflection", "title": "R4 polynomial Wolff 公理：条件化管界不等于 Kakeya 解决 / conditional tube bounds do not solve R4 Kakeya", "path": "vault/reflections/reflection-reflection_3161177e53e4d63befa4efbe.md", "status": "active", "source_ids": ["source_8e3ad66feb25889d1f2a8103"], "snippet": "…本文处理 R4 的 delta 管，并额外假定 polynomial Wolff [axioms]，三线性结果还要求交管三元组方向独立。\n  Difference: 既有对象讨论同一论文的条件性界；当前 PDF 只是同一工作可读版本的重复来源，而非独立验证。\n\n## Conflicts\n\nNone…", "match_reason": "full-text:body"}, {"id": "reflection_0a086695ae3406f8c7c543a1", "type": "reflection", "title": "多项式分割的 restriction 改进：明确指数不是完整猜想 / polynomial partitioning gives a bounded restriction improvement", "path": "vault/reflections/reflection-reflection_0a086695ae3406f8c7c543a1.md", "status": "active", "source_ids": ["source_b6d55666cda69c2a1c407986"], "snippet": "# 多项式分割的 restriction 改进：明确指数不是完整猜想 / [polynomial] partitioning gives a bounded restriction improvement\n\n## Why important\n\nGuth 将多项式分割用于振荡积分的波包组织，在严格正第二基本形式这一几何边界下把 R3 的线性…", "match_reason": "metadata:title"}, {"id": "reflection_a6bfe02e241eb2369adb8f8a", "type": "reflection", "title": "高维 Kakeya 的递归多尺度界：同一工作 PDF 只补证明细节 / duplicate PDF only supplements multiscale proof detail", "path": "vault/reflections/reflection-reflection_a6bfe02e241eb2369adb8f8a.md", "status": "active", "source_ids": ["source_58d4a745ceb904073c47f2b3"], "snippet": "…两者都用递归多尺度几何信息和 polynomial [Wolff] 控制方向分离管族。\n  Boundary: 结果针对 n=5 或 n>=7 的最大函数改进及选定维数的集合界。\n  Difference: 既有反思已记录同一工作的范围与机制；当前 PDF 只是同一论文的完整版本。\n\n## Conflicts…", "match_reason": "full-text:body"}, {"id": "concept_0ea689b9ff94e453dd23b64b", "type": "concept", "title": "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements", "path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "status": "working", "source_ids": ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986", "source_f366554c5c3887de7c6ad29b"], "snippet": "…source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 [polynomial] partitioning 控制 extension 波包，证明 L2(S) 到 Lp…", "match_reason": "metadata:domains"}, {"id": "concept_c0e590dd716efa867bc34cbd", "type": "concept", "title": "多线性 restriction 与 Kakeya 中的横截性控制", "path": "vault/memory/concept/concept_c0e590dd716efa867bc34cbd.md", "status": "working", "source_ids": ["source_84c8c0edd41364ae0542b7ca", "source_2a85810f575207c9c115a466"], "snippet": "…新增来源材料\n\n- `source_2a85810f575207c9c115a466`：当 n 类圆柱管的方向向量具有统一正的行列式下界时，Guth 以 [polynomial] ham-sandwich 方法证明 Bennett--Carbery--Tao 多线性 Kakeya 猜想的端点估计…", "match_reason": "metadata:domains"}, {"id": "reflection_3d3296633fe4d9256a88672c", "type": "reflection", "title": "R3 restriction 的 broom 线索：指数改进须与证明机制和适用范数绑定 / broom-based R3 restriction needs scoped exponents", "path": "vault/reflections/reflection-reflection_3d3296633fe4d9256a88672c.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "…该摘要把具体 p>3+3/13 界与 two-ends、[polynomial] partitioning 并列，提示 restriction 进展应按精确指数、输入范数与几何分解机制保存，而非归入笼统的 Kakeya 标签…", "match_reason": "metadata:domains"}, {"id": "reflection_539106049b68b9810702fe73", "type": "reflection", "title": "三维 Kakeya 的全维主张：体积估计、Wolff 非集中与最大函数猜想需分开 / R3 Kakeya full dimension needs scoped claims", "path": "vault/reflections/reflection-reflection_539106049b68b9810702fe73.md", "status": "active", "source_ids": ["source_cf15e6b90aaf4c6584d5efe2"], "snippet": "# 三维 Kakeya 的全维主张：体积估计、[Wolff] 非集中与最大函数猜想需分开 / R3 Kakeya full dimension needs scoped claims\n\n## Why important\n\n该 PDF 给出了既存概念未记录的证明中介和未解决边界…", "match_reason": "metadata:title"}, {"id": "reflection_69a40cf16b9785b5d6678ef3", "type": "reflection", "title": "Wang--Zahl 后的三维 Kakeya：凸 Wolff 公理把重叠归因于凸聚集", "path": "vault/reflections/reflection-reflection_69a40cf16b9785b5d6678ef3.md", "status": "active", "source_ids": ["source_6663eabaf2e8d72079fead7a"], "snippet": "# Wang--Zahl 后的三维 Kakeya：凸 [Wolff] 公理把重叠归因于凸聚集\n\n## Why important\n\n该综述把三维满维结论组织为凸 [Wolff] 公理下的典型重数控制，并把多尺度分析作为从最坏管族到矛盾的主线；它补足了只记录“维数为 3”时会丢失的证明中介。\n\n## What…", "match_reason": "metadata:title"}, {"id": "concept_f8a4dfcc3d24b856a7d6335d", "type": "concept", "title": "凸集非集中体积准则 / convex-set non-concentration volume criterion", "path": "vault/memory/concept/concept_f8a4dfcc3d24b856a7d6335d.md", "status": "working", "source_ids": ["source_443db75c1157e4ee28fb3ea0", "source_cf15e6b90aaf4c6584d5efe2"], "snippet": "…R3 中满足 Katz--Tao convex 与 Frostman slab [Wolff] 非集中条件的 delta 管族，Wang 与 Zahl 以 D/E…", "match_reason": "metadata:aliases"}, {"id": "reflection_54ac9c11b0aadf6dcc93710a", "type": "reflection", "title": "高维 Kakeya：递归归纳暴露多尺度几何信息", "path": "vault/reflections/reflection-reflection_54ac9c11b0aadf6dcc93710a.md", "status": "active", "source_ids": ["source_e480d57998401d152443b4ad"], "snippet": "# 高维 Kakeya：递归归纳暴露多尺度几何信息\n\n## Why important\n\n该文把多项式划分的归纳证明写成递归算法，以提取方向分离管族在不同尺度上的几何信息，并据此建立多尺度 polynomial Wolff [axioms]；它将改进估计的关键放在跨尺度约束，而非单尺度覆盖计数。\n\n## What changed\n\n我会把高维 Kakeya 改进视为需要保存并传递尺度间结构的归纳过程…", "match_reason": "full-text:body"}, {"id": "input_a541ca45a602bd1db7654686", "type": "input", "title": "[2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities", "path": "vault/inputs/input-input_a541ca45a602bd1db7654686.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# [2411.08871] Restriction [estimates] using decoupling theorems and two-ends Furstenberg inequalities\n\nInput Episode for `source_4ecaaa23ce1d04b17629d3d6`. The…", "match_reason": "metadata:title"}, {"id": "input_2157b4467cd4b1295813f202", "type": "input", "title": "[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions", "path": "vault/inputs/input-input_2157b4467cd4b1295813f202.md", "status": "active", "source_ids": ["source_443db75c1157e4ee28fb3ea0"], "snippet": "# [2502.17655] Volume [estimates] for unions of convex sets, and the Kakeya set conjecture in three dimensions\n\nInput…", "match_reason": "metadata:title"}, {"id": "reflection_b41efeb649d24f9777603cfc", "type": "reflection", "title": "Kac 计划：混沌传播需要函数估计与适用边界 / Kac propagation of chaos needs scoped functional estimates", "path": "vault/reflections/reflection-reflection_b41efeb649d24f9777603cfc.md", "status": "active", "source_ids": ["source_8b084d508aceb97e2df2ff16"], "snippet": "# Kac 计划：混沌传播需要函数估计与适用边界 / Kac propagation of chaos needs scoped functional [estimates]\n\n## Why important\n\n论文以生成元一致性估计和非线性极限流的稳定性估计来建立碰撞多粒子系统到 Boltzmann 型平均场极限的定量混沌传播，说明“平均场极限…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b2c6c3d707b387d0dbad6dbc"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "9b6a8aa5a8d338acdaaf8576596d9c08d385a9ec57e259e24f1d4264aa0c82c3"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\mathbb{R}^4$

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_e5b07cd2ccd80e4caf9af5d4`
- 编译前召回已有对象：16
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_2de4832c73aa726ac94ca956-r4-polynomial-wolff-公理下的条件化管并集体积界-conditional-tube-union-bounds-.md
@@ -0,0 +1,20 @@
+---
+id: "concept_2de4832c73aa726ac94ca956"
+type: "concept"
+status: "proposal"
+title: "R4 polynomial Wolff 公理下的条件化管并集体积界 / conditional tube-union bounds under polynomial Wolff axioms in R4"
+created_at: "2026-07-28T10:17:54+08:00"
+updated_at: "2026-07-28T10:17:54+08:00"
+aliases: ["R4 polynomial Wolff axioms", "delta one minus one over forty tube bound", "四维 polynomial Wolff 体积界", "R4 Kakeya 条件化估计"]
+tags: []
+domains: ["harmonic-analysis", "kakeya", "polynomial-method"]
+confidence: "medium"
+source_ids: ["source_b2c6c3d707b387d0dbad6dbc"]
+relations: [{"type": "derived_from", "target_id": "source_b2c6c3d707b387d0dbad6dbc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}]
+change_reason: "compile bundle from source_b2c6c3d707b387d0dbad6dbc"
+reflection_context: {"reflection_ids": ["reflection_8bed5c9d4ce32f9a4412f334"], "importance": "high", "changed_belief": "我会将代数簇非集中公理视为可检验的中介假设，而非方向分离本身自动满足的性质。", "surprising": "", "connections": [], "open_questions": ["如何从一般 Kakeya 管族导出 polynomial Wolff axioms，或构造其失效的近极值结构？"]}
+---
+
+# R4 polynomial Wolff 公理下的条件化管并集体积界 / conditional tube-union bounds under polynomial Wolff axioms in R4
+
+对 R4 中 delta^-3 个 delta 管，polynomial Wolff axioms 要求低次数代数簇的 delta 邻域不能容纳过多管。论文 v3 摘要声称：在该公理下，管并集体积至少为 delta^(1-1/40)，并得到对应于维数 3+1/40 的最大函数型估计；若多数相交管三元组指向三个线性独立方向，则并集体积至少为 delta^(3/4)，对应更强的多线性横截情形。作者明确没有证明每个 R4 Kakeya 集都满足 polynomial Wolff axioms，因此这些是条件化界，不是 R4 Kakeya 集或最大函数猜想的无条件解决。
```
