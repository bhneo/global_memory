---
id: "proposal_bundle_317a7a8582c434ca655f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T16:01:39+08:00"
updated_at: "2026-07-27T16:02:17+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b6d55666cda69c2a1c407986"]
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
extraction_id: "extraction_8cf1548142b0c69e47876532"
input_sha256: "4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_0ea689b9ff94e453dd23b64b", "target_path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "base_sha256": "90ef9726e7b4f629ba3704ec418deba146151c852fdfec0d19777df64543d111", "candidate_sha256": "400a3b0b2d07c2fd915b6c84d0a99eab7e9e19ab96f54fb9ab1ed924863be273", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_317a7a8582c434ca655f-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_317a7a8582c434ca655f-concept-1.md", "working_path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-27T16:02:17+08:00"}]
existing_context: [{"id": "concept_0ea689b9ff94e453dd23b64b", "type": "concept", "title": "三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3", "path": "vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md", "status": "working", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代", "match_reason": "metadata:aliases"}, {"id": "concept_c0e590dd716efa867bc34cbd", "type": "concept", "title": "多线性 restriction 与 Kakeya 中的横截性控制", "path": "vault/memory/concept/concept_c0e590dd716efa867bc34cbd.md", "status": "working", "source_ids": ["source_84c8c0edd41364ae0542b7ca"], "snippet": "# 多线性 [restriction] 与 Kakeya 中的横截性控制\n\n多线性 [restriction]/Kakeya 框架考虑 d 个扩张算子或管族：当相应子流形的法向量在参数域上一致张成 Rd，并满足规定的光滑性界时，可建立多线性估计而不对每个单独子流形施加高斯曲率条件。横截性在此控制不同输入的几何独立性；该结论不直接给出完整的线性 [restriction]…", "match_reason": "metadata:title"}, {"id": "reflection_3d3296633fe4d9256a88672c", "type": "reflection", "title": "R3 restriction 的 broom 线索：指数改进须与证明机制和适用范数绑定 / broom-based R3 restriction needs scoped exponents", "path": "vault/reflections/reflection-reflection_3d3296633fe4d9256a88672c.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "# R3 [restriction] 的 broom 线索：指数改进须与证明机制和适用范数绑定 / broom-based R3 [restriction] needs scoped exponents\n\n## Why important\n\n该摘要把具体 p>3…", "match_reason": "metadata:title"}, {"id": "reflection_ffdae9cc698b6452d03746f4", "type": "reflection", "title": "多线性 restriction：横截性可替代线性理论中的曲率要求", "path": "vault/reflections/reflection-reflection_ffdae9cc698b6452d03746f4.md", "status": "active", "source_ids": ["source_84c8c0edd41364ae0542b7ca"], "snippet": "# 多线性 [restriction]：横截性可替代线性理论中的曲率要求\n\n## Why important\n\n论文将 [restriction] 和 Kakeya 问题置于多线性设置，强调当多个子流形法向量满足统一张成条件时，估计可依赖横截性而不要求各个曲面具有非零高斯曲率。\n\n## What changed\n\n我原先会把曲率当作 [restriction] 估计的普遍核心条件；本文使我看到在…", "match_reason": "metadata:title"}, {"id": "reflection_388f8044ad3edf589c5d59a4", "type": "reflection", "title": "三维 restriction：Kakeya 关联与精细解耦带来具体指数改进", "path": "vault/reflections/reflection-reflection_388f8044ad3edf589c5d59a4.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# 三维 [restriction]：Kakeya 关联与精细解耦带来具体指数改进\n\n## Why important\n\n该论文把 Kakeya 型关联估计与 refined decoupling 直接接到 R3 中一个定量的线性 [restriction] 指数改进，说明相关几何工具不仅服务于多线性横截性框架。\n\n## What…", "match_reason": "metadata:title"}, {"id": "reflection_5460516a2a5ca0cf00b1b350", "type": "reflection", "title": "R3 restriction 指数改进：同一论文 PDF 只补充细节，不重复计数 / duplicate PDF adds no new theory", "path": "vault/reflections/reflection-reflection_5460516a2a5ca0cf00b1b350.md", "status": "active", "source_ids": ["source_7d5e22dd2d2cf4588150dce9"], "snippet": "# R3 [restriction] 指数改进：同一论文 PDF 只补充细节，不重复计数 / duplicate PDF adds no new theory\n\n## Why important\n\n该 PDF 详细说明…", "match_reason": "metadata:title"}, {"id": "input_a541ca45a602bd1db7654686", "type": "input", "title": "[2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities", "path": "vault/inputs/input-input_a541ca45a602bd1db7654686.md", "status": "active", "source_ids": ["source_4ecaaa23ce1d04b17629d3d6"], "snippet": "# [2411.08871] Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities\n\nInput Episode for `source_4ecaaa23ce1d04b17629d3d6`. The immutable Source remains authoritative.\n\n# [2411.08871] Restriction estimates usi", "match_reason": "metadata:title"}, {"id": "input_2157b4467cd4b1295813f202", "type": "input", "title": "[2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions", "path": "vault/inputs/input-input_2157b4467cd4b1295813f202.md", "status": "active", "source_ids": ["source_443db75c1157e4ee28fb3ea0"], "snippet": "# [2502.17655] Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions\n\nInput Episode for `source_443db75c1157e4ee28fb3ea0`. The immutable Source remains authoritative.\n\n# [2502.17655] Volume estimates ", "match_reason": "metadata:title"}, {"id": "input_3b2d4a128c5dcd00c6d756b5", "type": "input", "title": "[2210.03878] An improved restriction estimate in $\\mathbb{R}^3$", "path": "vault/inputs/input-input_3b2d4a128c5dcd00c6d756b5.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\nInput Episode for `source_299adfe6dd42f97b6f75b777`. The immutable Source remains authoritative.\n\n# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\n> 原始内容：[", "match_reason": "metadata:title"}, {"id": "input_4846565da5dc1656c16a439a", "type": "input", "title": "[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms", "path": "vault/inputs/input-input_4846565da5dc1656c16a439a.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\nInput Episode for `source_f366554c5c3887de7c6ad29b`. The immutable Source remains authoritative.\n\n# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\n> ", "match_reason": "metadata:title"}, {"id": "input_696ed17b934899983e8f639c", "type": "input", "title": "[1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$", "path": "vault/inputs/input-input_696ed17b934899983e8f639c.md", "status": "active", "source_ids": ["source_b2c6c3d707b387d0dbad6dbc"], "snippet": "# [1701.07045] Polynomial Wolff axioms and Kakeya-type estimates in $\\mathbb{R}^4$\n\nInput Episode for `source_b2c6c3d707b387d0dbad6dbc`. The immutable Source remains authoritative.\n\n# [1701.07045] Polynomial Wolff axioms and Kakeya-type est", "match_reason": "metadata:title"}, {"id": "input_bb9068321957f044c9f1310a", "type": "input", "title": "Robo-ValueRL", "path": "vault/inputs/input-input_bb9068321957f044c9f1310a.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# Robo-ValueRL\n\nInput Episode for `source_7b278ba348f2a8bb94cce1fc`. The immutable Source remains authoritative.\n\n# Robo-ValueRL\n\n> 原始内容：[vault/raw/objects/sha256/1c/85/1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9](../ob", "match_reason": "full-text:body"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b6d55666cda69c2a1c407986"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "324d3c3b272977f5085fe368bed7c5f424d8c37e73e8da368f57efae7af0f9c8"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_8cf1548142b0c69e47876532`
- 编译前召回已有对象：13
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md
+++ candidate:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_0ea689b9ff94e453dd23b64b"
 type: "concept"
-status: "working"
-title: "三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3"
+status: "proposal"
+title: "R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements"
 created_at: "2026-07-27T11:02:49+08:00"
-updated_at: "2026-07-27T11:02:50+08:00"
-aliases: ["R3 restriction estimate", "three-dimensional restriction estimate", "Kakeya incidence estimates", "refined decoupling", "三维 restriction 估计", "Kakeya 型关联估计", "精细解耦"]
+updated_at: "2026-07-27T16:01:39+08:00"
+aliases: ["多项式分割 restriction 改进", "polynomial-partitioning restriction improvement"]
 tags: []
-domains: ["harmonic-analysis", "restriction-theory", "kakeya"]
-confidence: "medium"
-source_ids: ["source_299adfe6dd42f97b6f75b777"]
+domains: ["harmonic-analysis", "restriction", "polynomial-partitioning"]
+confidence: "high"
+source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986"]
 relations: [{"type": "derived_from", "target_id": "source_299adfe6dd42f97b6f75b777", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c0e590dd716efa867bc34cbd", "reason": "两者都连接 Kakeya 型几何控制与 restriction 估计；既有概念处理多线性横截性，本文记录线性 R3 中经 incidence/decoupling 得到的特定指数改进。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_299adfe6dd42f97b6f75b777"
-reflection_context: {"reflection_ids": ["reflection_388f8044ad3edf589c5d59a4"], "importance": "high", "changed_belief": "我会把 Kakeya/restriction 的联系区分为具体可量化的线性估计进展，而不是笼统地把所有 Kakeya 技术等同于解决线性 restriction。", "surprising": "", "connections": [{"shared_mechanism": "两者都以管或波包的几何组织限制频率局部片段的叠加。", "boundary": "本文只声称 R3 中 p>3+3/14 的 Lp→Lp 改进，所见来源为摘要级方法信息。", "difference": "既有概念是多线性横截性的一般框架；本文记录线性 R3 的特定指数改进。"}], "open_questions": []}
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
-origin_proposal_id: "proposal_bundle_24f4c0b1bcacc47a5232"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_24f4c0b1bcacc47a5232-concept-1.md"
-origin_candidate_sha256: "c7e0b9dcd9cab866057ab51d0e5c59449a8d5ca436500a021b416bd676cf0d18"
-origin_cognitive_artifact_sha256: "3d6618ddad3b8349b6d3f6141dd600b00846246ffb5ebeb268e9ecf7148c44ed"
-memory_schema_version: 2
+change_reason: "compile bundle from source_b6d55666cda69c2a1c407986"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_0a086695ae3406f8c7c543a1"], "importance": "high", "changed_belief": "我会把该成果表述为带曲率、范数和指数门槛的 R3 线性估计，而不把它泛化为任意曲面或完整 restriction conjecture。", "surprising": "", "connections": [{"shared_mechanism": "两者都用管状波包的几何组织来控制 restriction 或 Kakeya 型重叠。", "boundary": "本文限于 R3 中紧致光滑且第二基本形式严格正的曲面，以及 L2(S) 到 Lp(R3) 的 p>3.25 估计。", "difference": "本文以多项式分割和 cell/零集二分推进线性 restriction；既有条目以 Kakeya incidence 与 refined decoupling 得到另一指数改进。"}], "open_questions": ["多项式分割中的 broad/cell--surface 分解还需要何种新控制，才能在该类曲面上达到预期的 p>3？"]}
+proposed_status: "working"
 ---
 
 # 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3
 
 Wang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。
+
+## 新增来源材料
+
+- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。
```
