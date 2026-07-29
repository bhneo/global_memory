---
id: "proposal_bundle_d25f28da778468fb478d"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T10:18:43+08:00"
updated_at: "2026-07-28T10:20:08+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_62c0eb77c44fc70ee44d7233"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_acc03a148da29f780a7dcd12"
input_sha256: "0048d573ffb2efd0e1d335c89b54acb24e00787a82f60acc888835fe5f17a577"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_24de3544824d45b83583c5a5", "target_path": "vault/memory/concept/concept_24de3544824d45b83583c5a5.md", "base_sha256": "f6a9a54c297ad3a8477679eeafc0481fdc7d78e2644aebdc53d9f03b22c27589", "candidate_sha256": "3ba60b51714c18e5f89aef6d2faa9117562f2f3a5c6b7cd3dd30d5e9e6618d4f", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_d25f28da778468fb478d-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_d25f28da778468fb478d-concept-1.md", "working_path": "vault/memory/concept/concept_24de3544824d45b83583c5a5.md", "evolution_action": "support", "exception_id": null, "working_at": "2026-07-28T10:20:08+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT\n\n> 原始内容：[vault…", "match_reason": "metadata:title"}, {"id": "input_26ade68b0fee058a5e73c9e7", "type": "input", "title": "[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity", "path": "vault/inputs/input-input_26ade68b0fee058a5e73c9e7.md", "status": "active", "source_ids": ["source_7ab41149787a9cd99bd2fe58"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/9711200] The Large N Limit of Superconformal Field Theories and Supergravity…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_62c0eb77c44fc70ee44d7233"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "9b6a8aa5a8d338acdaaf8576596d9c08d385a9ec57e259e24f1d4264aa0c82c3"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_acc03a148da29f780a7dcd12`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_24de3544824d45b83583c5a5.md
+++ candidate:vault/memory/concept/concept_24de3544824d45b83583c5a5.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_24de3544824d45b83583c5a5"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity"
 created_at: "2026-07-28T01:47:06+08:00"
-updated_at: "2026-07-28T01:47:07+08:00"
-aliases: ["entanglement first law implies linearized Einstein equations", "all balls and Lorentz frames", "纠缠第一律推出线性化 Einstein 方程", "全息纠缠闭合条件"]
+updated_at: "2026-07-28T10:18:43+08:00"
+aliases: ["gravitation from entanglement", "entanglement first law linearized AdS", "纠缠第一律导出线性化引力", "球形区域全息引力约束"]
 tags: []
 domains: ["ads-cft", "quantum-gravity", "entanglement"]
 confidence: "high"
-source_ids: ["source_8e0a54f1b7764d6c5f111dcb"]
+source_ids: ["source_8e0a54f1b7764d6c5f111dcb", "source_62c0eb77c44fc70ee44d7233"]
 relations: [{"type": "derived_from", "target_id": "source_8e0a54f1b7764d6c5f111dcb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}, {"type": "related_to", "target_id": "concept_4e520f39dde022d5e1042625", "reason": "两者都用纠缠的一阶变分约束 Einstein 方程，但本项依赖 AdS/CFT 与 RT，既有节点使用固定体积小测地球的真空纠缠平衡。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
-change_reason: "compile bundle from source_8e0a54f1b7764d6c5f111dcb"
-reflection_context: {"reflection_ids": ["reflection_60d6cfa7a6c01410932bc897"], "importance": "high", "changed_belief": "我会把“纠缠得引力”的说法限定在 holographic CFT、真空附近、球形区域、弱曲率经典对偶和线性阶，并保留所有区域与参考系这一闭合条件。", "surprising": "", "connections": [{"shared_mechanism": "两者都把边界纠缠熵的一阶变化映射为 bulk 几何约束。", "boundary": "本文限于 CFT 真空的小扰动、球形区域和具有 Ryu--Takayanagi 面积解释的半经典全息对偶。", "difference": "既有条目强调从纠缠第一律到线性化场方程的条件化推导；本文特别说明任意 Lorentz 参考系为何是获得全部分量的必要条件。"}], "open_questions": ["离开球形区域、线性阶或全息 CFT 后，哪些可观测量仍能支撑对应的引力约束？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "gpt-5.6-sol-high-daily-v2-readmission"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_e7930e6ede16a1c4169f"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_e7930e6ede16a1c4169f-concept-1.md"
-origin_candidate_sha256: "f5e2151e5b2ead6c4a96c953f9c8b4a9f4247300b07e2dad8d42eb3a2190b899"
-origin_cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
-memory_schema_version: 2
+change_reason: "compile bundle from source_62c0eb77c44fc70ee44d7233"
+change_type: "support"
+reflection_context: {"reflection_ids": ["reflection_110c74eddca156c2211ac7cc"], "importance": "high", "changed_belief": "我会把纠缠--几何联系限定为具有半经典 holographic dual、真空小扰动与球形区域的命题。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过纠缠量与几何或引力约束建立跨描述层的对应。", "boundary": "本文限于 CFT 的半经典全息对偶、真空附近小扰动和球形区域。", "difference": "既有纠缠--时空条目概述连通性线索；本文给出纠缠第一律到线性化场方程的具体约束。"}], "open_questions": ["如何从线性化、球形区域的约束推广到非线性、一般区域或非全息量子系统？"]}
+proposed_status: "working"
 ---
 
 # 全息纠缠第一律对线性化 AdS 引力的闭合条件 / closure conditions from the holographic entanglement first law to linearized AdS gravity
 
 对具有半经典 AdS 对偶的 CFT 真空的小扰动，将纠缠第一定律应用于所有球形边界区域，并用 RT 面积关系和边界应力张量--渐近度规字典，可得到纯 AdS 附近的线性化 Einstein 方程。只在一个固定 Lorentz 参考系考察所有球时仅获得部分分量；完整方程需要任意参考系。该结论局限于真空附近、球形区域、线性阶和经典全息度规扇区，不能约束所有额外 bulk 场或直接推广到非线性引力。
+
+## 新增来源材料
+
+- `source_62c0eb77c44fc70ee44d7233`：原始论文证明，在具有半经典全息对偶的 CFT 中，对真空态的小扰动和所有球形空间区域施加纠缠第一律，与 dual geometry 满足纯 AdS 附近的线性化引力方程等价。若纠缠熵由 Ryu--Takayanagi 面积给出，得到线性化 Einstein 方程；若由更一般 Wald 泛函给出，则得到相应高曲率引力理论的线性化方程。其讨论同时限制了外推：论证使用全局 AdS-Rindler 区域且只达线性阶，有限扰动提供的是相对熵不等式，通常不足以单独确定完整非线性方程或依赖具体 CFT 的额外 bulk 场。
```
