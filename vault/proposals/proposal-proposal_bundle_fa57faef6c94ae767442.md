---
id: "proposal_bundle_fa57faef6c94ae767442"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T12:13:38+08:00"
updated_at: "2026-07-28T12:13:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a195660cb37a44a2e8aa69a0"]
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
extraction_id: "extraction_b335362c9860e3ba02a9efb4"
input_sha256: "36613b93459624ceaf519d4042182713466de2c4e6ed0de9667ea85889fd1fed"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_213bb64d4c68cc5663afe60d", "target_path": "vault/knowledge/concepts/concept_213bb64d4c68cc5663afe60d-静态-newton-引力的热力学表述是等价重释-thermodynamic-formulation-of-static-newt.md", "base_sha256": null, "candidate_sha256": "7f2325288e8f83d8bae9e0acdb899f158f45a7a3d2423f3be98109957fc06298", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_fa57faef6c94ae767442-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_213bb64d4c68cc5663afe60d.md", "working_at": "2026-07-28T12:13:41+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_0b5fbfe5c9ecee3146dadce4", "type": "input", "title": "[gr-qc/0209088] Gravity from Spacetime Thermodynamics", "path": "vault/inputs/input-input_0b5fbfe5c9ecee3146dadce4.md", "status": "active", "source_ids": ["source_ad785f5be8067788394ec708"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/0209088] Gravity from Spacetime Thermodynamics\n\n> 原始内容：[vault/raw/objects/sha256/00…", "match_reason": "metadata:title"}, {"id": "input_72936b45ec8a50ec68020711", "type": "input", "title": "[gr-qc/0602001] Non-equilibrium Thermodynamics of Spacetime", "path": "vault/inputs/input-input_72936b45ec8a50ec68020711.md", "status": "active", "source_ids": ["source_086150581c4c39aee0813d57"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/0602001] Non-equilibrium Thermodynamics of Spacetime\n\n> 原始内容：[vault/raw/objects/sha256…", "match_reason": "metadata:title"}, {"id": "input_bfae3de85b84e499b741f875", "type": "input", "title": "[gr-qc/9307038] Black Hole Entropy is Noether Charge", "path": "vault/inputs/input-input_bfae3de85b84e499b741f875.md", "status": "active", "source_ids": ["source_caf9f433fb4cfb10c6466054"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/9307038] Black Hole Entropy is Noether Charge\n\n> 原始内容：[vault/raw/objects…", "match_reason": "metadata:title"}, {"id": "input_57adc74f55821ba73e81d43f", "type": "input", "title": "[gr-qc/9504004] Thermodynamics of Spacetime: The Einstein Equation of State", "path": "vault/inputs/input-input_57adc74f55821ba73e81d43f.md", "status": "active", "source_ids": ["source_4be2cb176dad6fdd8673bd31"], "snippet": "…The immutable Source remains authoritative.\n\n# [[gr-qc]/9504004] Thermodynamics of Spacetime: The Einstein Equation of State\n\n> 原始内容：[vault…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_a195660cb37a44a2e8aa69a0"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "fca3d2025837e0e856e16b1debfe3b3fd46a281792101eab8bbd36677d0d6957"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_b335362c9860e3ba02a9efb4`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_213bb64d4c68cc5663afe60d-静态-newton-引力的热力学表述是等价重释-thermodynamic-formulation-of-static-newt.md
@@ -0,0 +1,20 @@
+---
+id: "concept_213bb64d4c68cc5663afe60d"
+type: "concept"
+status: "proposal"
+title: "静态 Newton 引力的热力学表述是等价重释 / thermodynamic formulation of static Newtonian gravity is an equivalent reinterpretation"
+created_at: "2026-07-28T12:13:38+08:00"
+updated_at: "2026-07-28T12:13:38+08:00"
+aliases: ["Newtonian entropic gravity equivalence", "thermodynamic reinterpretation of Newtonian gravity", "Newton 熵力等价重述", "静态 Newton 热力学重释"]
+tags: []
+domains: ["gravity", "thermodynamics", "entropic-gravity"]
+confidence: "high"
+source_ids: ["source_a195660cb37a44a2e8aa69a0"]
+relations: [{"type": "derived_from", "target_id": "source_a195660cb37a44a2e8aa69a0", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}]
+change_reason: "compile bundle from source_a195660cb37a44a2e8aa69a0"
+reflection_context: {"reflection_ids": ["reflection_17639fb8c42a103e5d1ad47a"], "importance": "high", "changed_belief": "我会把静态 Newton 情形的熵力语言视为等价重参数化，而不将其本身当作关于 GR 或微观引力起源的证据。", "surprising": "", "connections": [{"shared_mechanism": "两者都以屏幕熵温度量重写 Newton 势力。", "boundary": "本文只论静态 Newton 理论；对 GR 仍有论证缺口。", "difference": "原方案尝试从热力学推出力律；本文还从既有 Newton 理论反向构造该表述。"}], "open_questions": ["哪些不预设 Newton/GR 结构的预测可区分重述与机制？"]}
+---
+
+# 静态 Newton 引力的热力学表述是等价重释 / thermodynamic formulation of static Newtonian gravity is an equivalent reinterpretation
+
+对时间无关的 Newton 引力，Hossenfelder 把 Poisson 方程、测试质量所受的势梯度力，与覆盖空间的非交叠屏幕、屏幕温度和熵变的积分关系作适当识别。借助 Gauss 定律和 Green 恒等式，可以从 Newton 理论构造这种热力学表述，也可以从该表述恢复 Newton 方程；Verlinde 使用的若干额外 bit 数或 equipartition 假设并非完成该等价所必需。双向可逆性表明，在这一静态非相对论范围内，熵力语言本身是 Newton 引力的等价重释，而不是关于微观引力起源的独立证据或新预测。该结论不覆盖广义相对论、引力波、量子叠加源或量子化引力；这些正是需要额外机制才能使热力学描述获得新增解释力的边界。
```
