---
id: "proposal_bundle_29c6e1c518cb204dd879"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T01:55:12+08:00"
updated_at: "2026-07-28T01:55:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_aa1393c9b110562ca3f37509"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "degraded"
extraction_quality: "degraded"
extraction_id: "extraction_9d74f12f1022041d3c7fe878"
input_sha256: "c7d228e79c2e13255dbcef7b919eb62eabb56c93a57f24d5c69021a64cf04c0f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_972e54ed590f8b093808209f", "target_path": "vault/memory/concept/concept_972e54ed590f8b093808209f.md", "base_sha256": "ccbcdd72f156e9bed77a783e625b02b2a32e35b814496d7d0feff2f6ea16b004", "candidate_sha256": "c15c182c495e12e3e85e61eb3e5461b6019d37a3e760ae646da30fd3a1336f6f", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_29c6e1c518cb204dd879-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_29c6e1c518cb204dd879-concept-1.md", "working_path": "vault/memory/concept/concept_972e54ed590f8b093808209f.md", "evolution_action": "support", "exception_id": null, "working_at": "2026-07-28T01:55:48+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_8f16a3ad954bd05b1a2a7752", "type": "input", "title": "[2012.03813] Long-time correlations for a hard-sphere gas at equilibrium", "path": "vault/inputs/input-input_8f16a3ad954bd05b1a2a7752.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "…Thierry Bodineau , Isabelle Gallagher (UPD7, DMA), Laure [Saint-Raymond] , Sergio Simonella View a PDF of the paper titled…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_aa1393c9b110562ca3f37509"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "degraded", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "74927bba664f8936f712388db40fbf90903bc1bc7af83c4c48962b7c0c03db90"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_9d74f12f1022041d3c7fe878`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_972e54ed590f8b093808209f.md
+++ candidate:vault/memory/concept/concept_972e54ed590f8b093808209f.md
@@ -1,42 +1,26 @@
 ---
 id: "concept_972e54ed590f8b093808209f"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit"
 created_at: "2026-07-27T10:46:52+08:00"
-updated_at: "2026-07-27T19:06:43+08:00"
-aliases: ["Boltzmann-Grad fluctuations", "fluctuating Boltzmann equation", "Boltzmann--Grad 涨落", "涨落 Boltzmann 方程"]
+updated_at: "2026-07-28T01:55:12+08:00"
+aliases: ["Lanford short-time limit", "Newton to Boltzmann derivation", "牛顿粒子到 Boltzmann 方程", "Boltzmann--Grad 短时收敛"]
 tags: []
-domains: ["kinetic-theory", "statistical-mechanics", "large-deviations"]
+domains: ["kinetic-theory", "statistical-mechanics", "boltzmann-equation"]
 confidence: "high"
-source_ids: ["source_408691502cdb43e7e2ea5c3b"]
+source_ids: ["source_408691502cdb43e7e2ea5c3b", "source_aa1393c9b110562ca3f37509"]
 relations: [{"type": "derived_from", "target_id": "source_408691502cdb43e7e2ea5c3b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_408691502cdb43e7e2ea5c3b"
-reflection_context: {"reflection_ids": ["reflection_344908985fd536d0a4035c24"], "importance": "high", "changed_belief": "我会避免把“Boltzmann 方程有效”概括成单一结论：平均行为、小涨落和罕见路径需要不同的极限陈述。", "surprising": "", "connections": [{"shared_mechanism": "它与已有硬球长时相关概念都用低密度硬球微观动力学导出线性化 Boltzmann 层面的涨落控制。", "boundary": "本文对非平衡涨落、中心极限和大偏差的陈述限于其短时与正则性假设。", "difference": "已有概念处理平衡协方差的全时控制；本文把非平衡经验密度的典型、小涨落与罕见事件分层。"}], "open_questions": []}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 1
-last_consolidated_at: "2026-07-27T19:06:43+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_70ef165d78f84bfaaf82"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_70ef165d78f84bfaaf82-concept-1.md"
-origin_candidate_sha256: "58f389335d14989f18be9a9d33f80466255160e3fc9c31a2afd1880a2b8f6ed2"
-origin_cognitive_artifact_sha256: "4451ba8095f3fddeba82a9383e77828628ba8be1be6dd8738784909274a4c30c"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_ef3b08ecd79d927819a45bf7"
+change_reason: "compile bundle from source_aa1393c9b110562ca3f37509"
+change_type: "support"
+reflection_context: {"reflection_ids": ["reflection_6f883dfba279d1a3c9fe11f7"], "importance": "high", "changed_belief": "我不会把从 N 粒子牛顿动力学到 Boltzmann 方程理解为无条件的极限，而会先检查标度、初始相关和有效时间是否被证明覆盖。", "surprising": "", "connections": [{"shared_mechanism": "它与已有关于 Hilbert 第六问题的反思同样强调宏观或动理学导出需要可说明的近似层级和适用边界。", "boundary": "本文只在其声明的低密度 Boltzmann--Grad 情形及有限有效时间内讨论收敛。", "difference": "该论文处理粒子系统到 Boltzmann 方程；既有反思还涉及 Boltzmann 方程向流体方程的闭合与解释问题。"}], "open_questions": []}
+proposed_status: "working"
 ---
 
 # Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit
 
 在满足 Boltzmann--Grad 标度的稀薄硬球系统中，经验密度可在短时收敛到 Boltzmann 方程解；围绕平均的适当缩放涨落可收敛到由线性化 Boltzmann 算子和高斯噪声描述的过程，并可在额外正则性条件下讨论路径大偏差。三个结论分别对应典型行为、小涨落和罕见事件，不能相互替代。
+
+## 新增来源材料
+
+- `source_aa1393c9b110562ca3f37509`：对直径或作用程为 ε 的硬球及满足论文条件的短程排斥势粒子，在 Nε^(d-1)=1 的 Boltzmann--Grad 标度、近独立初始数据和有限有效时间内，一粒子边缘分布可在可观测量意义下收敛到相应 Boltzmann 方程；证明通过层级展开和对再碰撞病态轨迹的控制建立传播混沌。有效时间只是平均首次碰撞时间的一部分，不能据此主张任意长时收敛。
```
