---
id: "proposal_bundle_6c486356999239c562b4"
type: "proposal"
status: "migrated"
title: "Compile bundle：[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms"
created_at: "2026-07-28T10:05:00+08:00"
updated_at: "2026-07-28T10:05:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_f366554c5c3887de7c6ad29b"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_1def99e271950a5e4fc11939"
input_sha256: "85a841cb6f3d607ee6f1b68803fcc61767fd7b3432c8c59aa1edc45e17517111"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_0ea689b9ff94e453dd23b64b", "target_path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "base_sha256": "9898e67ea59e5dd8aa953c21e8028fe76a41ad313ecb0145e84a4c6639fffb8d", "candidate_sha256": "3ce4210c8cabf2855831790df7cd4a3e4455e9b854fe386a5ce62e26f6ffa803", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_6c486356999239c562b4-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_6c486356999239c562b4-concept-1.md", "working_path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-28T10:05:57+08:00"}]
existing_context: [{"id": "input_4846565da5dc1656c16a439a", "type": "input", "title": "[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms", "path": "vault/inputs/input-input_4846565da5dc1656c16a439a.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using [brooms]\n\nInput Episode for `source_f366554c5c3887de7c6ad29b`. The immutable…", "match_reason": "metadata:title"}, {"id": "concept_0ea689b9ff94e453dd23b64b", "type": "concept", "title": "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements", "path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "status": "working", "source_ids": ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986"], "snippet": "…证明 L2(S) 到 Lp(R3) 的 restriction [estimate] 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3…", "match_reason": "full-text:body"}, {"id": "reflection_0a086695ae3406f8c7c543a1", "type": "reflection", "title": "多项式分割的 restriction 改进：明确指数不是完整猜想 / polynomial partitioning gives a bounded restriction improvement", "path": "vault/reflections/reflection-reflection_0a086695ae3406f8c7c543a1.md", "status": "active", "source_ids": ["source_b6d55666cda69c2a1c407986"], "snippet": "# 多项式分割的 [restriction] 改进：明确指数不是完整猜想 / polynomial partitioning gives a bounded [restriction] improvement\n\n## Why important\n\nGuth 将多项式分割用于振荡积分的波包组织，在严格正第二基本形式这一几何边界下把 R3 的线性…", "match_reason": "metadata:title"}, {"id": "reflection_3d3296633fe4d9256a88672c", "type": "reflection", "title": "R3 restriction 的 broom 线索：指数改进须与证明机制和适用范数绑定 / broom-based R3 restriction needs scoped exponents", "path": "vault/reflections/reflection-reflection_3d3296633fe4d9256a88672c.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "…本源只断言截断抛物面上的 L∞→Lp 估计及 p>3+3/13；摘要没有定义 [brooms] 的完整机制。\n  Difference: 既有概念是多线性横截性的一般框架；本文是单一线性 R3 的定量界，并结合 two…", "match_reason": "full-text:body"}, {"id": "reflection_ffdae9cc698b6452d03746f4", "type": "reflection", "title": "多线性 restriction：横截性可替代线性理论中的曲率要求", "path": "vault/reflections/reflection-reflection_ffdae9cc698b6452d03746f4.md", "status": "active", "source_ids": ["source_84c8c0edd41364ae0542b7ca"], "snippet": "# 多线性 [restriction]：横截性可替代线性理论中的曲率要求\n\n## Why important\n\n论文将 [restriction] 和 Kakeya 问题置于多线性设置，强调当多个子流形法向量满足统一张成条件时，估计可依赖横截性而不要求各个曲面具有非零高斯曲率。\n\n## What changed\n\n我原先会把曲率当作 [restriction] 估计的普遍核心条件；本文使我看到在…", "match_reason": "metadata:title"}, {"id": "reflection_388f8044ad3edf589c5d59a4", "type": "reflection", "title": "三维 restriction：Kakeya 关联与精细解耦带来具体指数改进", "path": "vault/reflections/reflection-reflection_388f8044ad3edf589c5d59a4.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# 三维 [restriction]：Kakeya 关联与精细解耦带来具体指数改进\n\n## Why important\n\n该论文把 Kakeya 型关联估计与 refined decoupling 直接接到 R3 中一个定量的线性 [restriction] 指数改进，说明相关几何工具不仅服务于多线性横截性框架。\n\n## What…", "match_reason": "metadata:title"}, {"id": "reflection_a9447d06fedc3128baa4679d", "type": "reflection", "title": "two-ends restriction 摘要：HTML 重复载体不增加证据 / duplicate HTML does not add evidence", "path": "vault/reflections/reflection-reflection_a9447d06fedc3128baa4679d.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# two-ends [restriction] 摘要：HTML 重复载体不增加证据 / duplicate HTML does not add evidence\n\n## Why important\n\n该 HTML 摘要重述 two…", "match_reason": "metadata:title"}, {"id": "reflection_5460516a2a5ca0cf00b1b350", "type": "reflection", "title": "R3 restriction 指数改进：同一论文 PDF 只补充细节，不重复计数 / duplicate PDF adds no new theory", "path": "vault/reflections/reflection-reflection_5460516a2a5ca0cf00b1b350.md", "status": "active", "source_ids": ["source_7d5e22dd2d2cf4588150dce9"], "snippet": "# R3 [restriction] 指数改进：同一论文 PDF 只补充细节，不重复计数 / duplicate PDF adds no new theory\n\n## Why important\n\n该 PDF 详细说明…", "match_reason": "metadata:title"}, {"id": "reflection_fc19fe9e4356fd03fa55740b", "type": "reflection", "title": "R3 broom restriction 的完整证明：重复载体只补几何机制 / full broom proof only supplements the geometric mechanism", "path": "vault/reflections/reflection-reflection_fc19fe9e4356fd03fa55740b.md", "status": "active", "source_ids": ["source_f2d57589a87b572303c23459"], "snippet": "# R3 broom [restriction] 的完整证明：重复载体只补几何机制 / full broom proof only supplements the geometric mechanism\n\n## Why important\n\nHong Wang 的完整证明把截断抛物面上的…", "match_reason": "metadata:title"}, {"id": "input_3b2d4a128c5dcd00c6d756b5", "type": "input", "title": "[2210.03878] An improved restriction estimate in $\\mathbb{R}^3$", "path": "vault/inputs/input-input_3b2d4a128c5dcd00c6d756b5.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# [2210.03878] An improved restriction estimate in $\\[mathbb]{R}^3$\n\nInput Episode for `source_299adfe6dd42f97b6f75b777`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_696ed17b934899983e8f639c", "type": "input", "title": "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$", "path": "vault/inputs/input-input_696ed17b934899983e8f639c.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "# [1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\[mathbb]{R}^4$\n\nInput Episode for `source_b2c6c3d707b387d0dbad6dbc…", "match_reason": "metadata:title"}, {"id": "input_a541ca45a602bd1db7654686", "type": "input", "title": "[2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities", "path": "vault/inputs/input-input_a541ca45a602bd1db7654686.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# [2411.08871] Restriction estimates [using] decoupling theorems and two-ends Furstenberg inequalities\n\nInput Episode for `source_4ecaaa23ce1d04b17629d3d6`. The…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_f366554c5c3887de7c6ad29b"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "282e3a3fa513c853ee2951555889f101d9c1b8517a4b65c9e87831e97ed507a9"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[1802.04312] A restriction estimate in $\mathbb{R}^3$ using brooms

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_1def99e271950a5e4fc11939`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md
+++ candidate:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md
@@ -1,43 +1,20 @@
 ---
 id: "concept_0ea689b9ff94e453dd23b64b"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements"
 created_at: "2026-07-27T11:02:49+08:00"
-updated_at: "2026-07-27T16:02:00+08:00"
-aliases: ["多项式分割 restriction 改进", "polynomial-partitioning restriction improvement"]
+updated_at: "2026-07-28T10:05:00+08:00"
+aliases: ["broom restriction estimate", "p greater than 3 plus 3 over 13", "扫帚结构 restriction", "R3 截断抛物面估计"]
 tags: []
-domains: ["harmonic-analysis", "restriction", "polynomial-partitioning"]
-confidence: "high"
-source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986"]
+domains: ["harmonic-analysis", "restriction-theory", "polynomial-partitioning"]
+confidence: "medium"
+source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986", "source_f366554c5c3887de7c6ad29b"]
 relations: [{"type": "derived_from", "target_id": "source_299adfe6dd42f97b6f75b777", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c0e590dd716efa867bc34cbd", "reason": "两者都连接 Kakeya 型几何控制与 restriction 估计；既有概念处理多线性横截性，本文记录线性 R3 中经 incidence/decoupling 得到的特定指数改进。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_b6d55666cda69c2a1c407986"
-reflection_context: {"reflection_ids": ["reflection_0a086695ae3406f8c7c543a1"], "importance": "high", "changed_belief": "我会把该成果表述为带曲率、范数和指数门槛的 R3 线性估计，而不把它泛化为任意曲面或完整 restriction conjecture。", "surprising": "", "connections": [{"shared_mechanism": "两者都用管状波包的几何组织来控制 restriction 或 Kakeya 型重叠。", "boundary": "本文限于 R3 中紧致光滑且第二基本形式严格正的曲面，以及 L2(S) 到 Lp(R3) 的 p>3.25 估计。", "difference": "本文以多项式分割和 cell/零集二分推进线性 restriction；既有条目以 Kakeya incidence 与 refined decoupling 得到另一指数改进。"}], "open_questions": ["多项式分割中的 broad/cell--surface 分解还需要何种新控制，才能在该类曲面上达到预期的 p>3？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-27T16:02:00+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_24f4c0b1bcacc47a5232"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_24f4c0b1bcacc47a5232-concept-1.md"
-origin_candidate_sha256: "c7e0b9dcd9cab866057ab51d0e5c59449a8d5ca436500a021b416bd676cf0d18"
-origin_cognitive_artifact_sha256: "3d6618ddad3b8349b6d3f6141dd600b00846246ffb5ebeb268e9ecf7148c44ed"
-memory_schema_version: 2
+change_reason: "compile bundle from source_f366554c5c3887de7c6ad29b"
 change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_3d3296633fe4d9256a88672c"], "importance": "high", "changed_belief": "我会把这项结果与后续 p>3+3/14 的摘要级改进并列而不合并，也不会从摘要把 brooms 推广为通用波包分类。", "surprising": "", "connections": [{"shared_mechanism": "本文与既有多线性 restriction/Kakeya 概念都用管或波包几何组织对 extension 叠加的控制。", "boundary": "本源只断言截断抛物面上的 L∞→Lp 估计及 p>3+3/13；摘要没有定义 brooms 的完整机制。", "difference": "既有概念是多线性横截性的一般框架；本文是单一线性 R3 的定量界，并结合 two-ends 与多项式划分。"}], "open_questions": ["broom 结构在完整证明中如何限制波包聚集，并与后续 refined-decoupling 路线形成何种可比较的几何不变量？"]}
 proposed_status: "working"
-change_history: [{"change_type": "refine", "previous_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。", "new_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。\n\n## 新增来源材料\n\n- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。", "changed_fields": [], "reason": "compile bundle from source_b6d55666cda69c2a1c407986", "trigger_source": "source_b6d55666cda69c2a1c407986", "evidence_added": []}]
-last_consolidation_id: "consolidation_75dd27da822c28b08c8cc7d1"
 ---
 
 # 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3
@@ -47,3 +24,7 @@
 ## 新增来源材料
 
 - `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。
+
+## 新增来源材料
+
+- `source_f366554c5c3887de7c6ad29b`：在后续 p>3+3/14 的 Kakeya incidence 与 refined-decoupling 改进之前，Wang 的论文摘要对 R3 截断抛物面给出 L∞ 到 Lp restriction 估计的 p>3+3/13 范围，并把证明路线标记为 polynomial partitioning、two-ends reduction 和 brooms。该来源仅为摘要，因而这里只保存精确指数、范数和方法标签；不能据此把 broom 解释扩展为一般波包聚集定理，也不能把该界与后续更强指数合并。
```
