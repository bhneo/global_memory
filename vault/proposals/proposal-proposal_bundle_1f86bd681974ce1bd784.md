---
id: "proposal_bundle_1f86bd681974ce1bd784"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T01:46:46+08:00"
updated_at: "2026-07-28T01:46:47+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9fee54df131233b62661cd0c"]
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
extraction_id: "extraction_95e651e3dc11e2161725734a"
input_sha256: "a9d4b20ab378a75c72fb843df95302c00fb41b40bd71f558d676682f212c5bd6"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_03d939da38791049f0689422", "target_path": "vault/knowledge/concepts/concept_03d939da38791049f0689422-ads-cft-的边界生成泛函字典-boundary-generating-functional-dictionary-in-a.md", "base_sha256": null, "candidate_sha256": "f6040bd1fefa86e99409a8ad78be8398d2a38b65ef739a84263e88d4c18c0b44", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_1f86bd681974ce1bd784-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_03d939da38791049f0689422.md", "working_at": "2026-07-28T01:46:47+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT\n\n> 原始内容：[vault…", "match_reason": "metadata:title"}, {"id": "input_26ade68b0fee058a5e73c9e7", "type": "input", "title": "[hep-th/9711200] The Large N Limit of Superconformal Field Theories and Supergravity", "path": "vault/inputs/input-input_26ade68b0fee058a5e73c9e7.md", "status": "active", "source_ids": ["source_7ab41149787a9cd99bd2fe58"], "snippet": "…The immutable Source remains authoritative.\n\n# [[hep-th]/9711200] The Large N Limit of Superconformal Field Theories and Supergravity…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9fee54df131233b62661cd0c"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_95e651e3dc11e2161725734a`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_03d939da38791049f0689422-ads-cft-的边界生成泛函字典-boundary-generating-functional-dictionary-in-a.md
@@ -0,0 +1,20 @@
+---
+id: "concept_03d939da38791049f0689422"
+type: "concept"
+status: "proposal"
+title: "AdS/CFT 的边界生成泛函字典 / boundary generating-functional dictionary in AdS/CFT"
+created_at: "2026-07-28T01:46:46+08:00"
+updated_at: "2026-07-28T01:46:46+08:00"
+aliases: ["GKPW dictionary", "Witten prescription", "AdS/CFT generating functional", "全息边界字典", "质量--维数关系"]
+tags: []
+domains: ["quantum-gravity", "string-theory", "conformal-field-theory"]
+confidence: "high"
+source_ids: ["source_9fee54df131233b62661cd0c"]
+relations: [{"type": "derived_from", "target_id": "source_9fee54df131233b62661cd0c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}, {"type": "defines", "target_id": "concept_fffdce69b79728a7844d0e69", "reason": "边界生成泛函和质量--维数关系给出 large-N AdS/CFT 对偶的可计算字典。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}]
+change_reason: "compile bundle from source_9fee54df131233b62661cd0c"
+reflection_context: {"reflection_ids": ["reflection_23e87ee0d8bc631aaf644cc0"], "importance": "high", "changed_belief": "我会把 AdS/CFT 的“对偶”分解为受近似控制的相关函数计算规则、谱映射和边界条件，而不是把它留作抽象口号。", "surprising": "", "connections": [{"shared_mechanism": "它与已有大 N 去耦极限 AdS/CFT 概念都以大 N、AdS 几何与共形场论的对应为基础。", "boundary": "本文的超引力树图计算适用于 AdS 长度尺度远大于弦和 Planck 尺度的参数区间。", "difference": "原始提案建立近地平线去耦路径；本文给出从边界渐近数据计算 CFT 相关函数的更明确字典。"}], "open_questions": []}
+---
+
+# AdS/CFT 的边界生成泛函字典 / boundary generating-functional dictionary in AdS/CFT
+
+在 AdS 尺度远大于弦长和 Planck 长、因而经典超引力近似可用的参数区间，边界 CFT 的相关函数可由 bulk 场在指定无穷远边界数据下的在壳超引力作用量对边界源求变分得到；对应算符的共形维数同时受 bulk 场质量控制。该字典是受近似条件约束的计算规则，不是任意耦合、有限 N 或任意边界条件下的无条件等式。
```
