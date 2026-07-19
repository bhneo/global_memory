---
id: "proposal_bundle_0915ce93560b0b1f72b5"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T02:52:10+08:00"
updated_at: "2026-07-19T02:52:10+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_54c9a7922f348a245d17efaf"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56terra-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_ae71d8454de8760daabd9fa1"
input_sha256: "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_validation_gated_skill_optimization", "target_path": "vault/knowledge/concepts/concept_validation_gated_skill_optimization-验证门控的技能文本优化.md", "base_sha256": null, "candidate_sha256": "197dfdb4455c478dd5e9e7191077b9d4d4d4edcab2d3ac37e35265b4cc9fd8ae", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0915ce93560b0b1f72b5-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_validation_gated_skill_optimization.md", "working_at": "2026-07-19T02:52:10+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_b912102d1da06715a0c97c77", "target_path": "vault/knowledge/claims/claim_b912102d1da06715a0c97c77-a-separate-optimizer-model-turns-scored-rollouts-into-bounded-ad.md", "base_sha256": null, "candidate_sha256": "a89e9a458d703d2311ed855080daa64f23162b049bc99197d36e2c8953a71e68", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_0915ce93560b0b1f72b5-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_b912102d1da06715a0c97c77.md", "working_at": "2026-07-19T02:52:10+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_bddbfc583594cb06ab113d17", "target_path": "vault/knowledge/claims/claim_bddbfc583594cb06ab113d17-an-edit-is-accepted-only-when-it-strictly-improves-a-held-out-va.md", "base_sha256": null, "candidate_sha256": "8e91a587271569361db72cb780a5163b0d14289539d303570071ecfbf9a8eb3c", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_0915ce93560b0b1f72b5-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_bddbfc583594cb06ab113d17.md", "working_at": "2026-07-19T02:52:10+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…However, here we also present an alternative [strategy] for\nassessing the overall collective outcomes: weighting the total\ncollective…", "match_reason": "full-text:body"}, {"id": "claim_wechat_skillevolver_k4_strategy_exploration_20260716", "type": "claim", "title": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略", "path": "vault/memory/claim/claim_wechat_skillevolver_k4_strategy_exploration_20260716.md", "status": "trusted", "source_ids": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略。", "match_reason": "metadata:tags"}, {"id": "work_arxiv_2605_10332", "type": "work", "title": "[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents", "path": "vault/memory/work/work_arxiv_2605_10332.md", "status": "working", "source_ids": ["source_b30214d3f75e366c385725a9", "source_30d6af4423a7ecb5e51c4a08"], "snippet": "…Skill-Aware Reflection for [Self-Evolving] Embodied Agents\n\n## Logical work identity\n\n- arXiv：`2605.10332`\n- Version：`unknown`\n- Captures：`source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 3, "source_id": "source_54c9a7922f348a245d17efaf"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 3, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 3, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-daily-gpt56terra-v1`
- Extraction：`extraction_ae71d8454de8760daabd9fa1`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_validation_gated_skill_optimization-验证门控的技能文本优化.md
@@ -0,0 +1,20 @@
+---
+id: "concept_validation_gated_skill_optimization"
+type: "concept"
+status: "proposal"
+title: "验证门控的技能文本优化"
+created_at: "2026-07-19T02:52:10+08:00"
+updated_at: "2026-07-19T02:52:10+08:00"
+aliases: []
+tags: []
+domains: ["agent-skills", "agent-learning", "evaluation"]
+confidence: "medium"
+source_ids: ["source_54c9a7922f348a245d17efaf"]
+relations: [{"type": "derived_from", "target_id": "source_54c9a7922f348a245d17efaf", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_skill_evolution", "reason": "该方法为技能演化增加了编辑预算、验证门控、拒绝缓冲和慢速更新等可控机制。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_54c9a7922f348a245d17efaf"
+uncertainty: "验证门控降低回归风险，但效果仍取决于验证集代表性和评分可靠性。"
+---
+
+# 验证门控的技能文本优化
+
+把 Agent 技能文档视作可训练的外部状态：根据执行轨迹提出有界增删改，并仅在独立验证集指标严格改善时接受新版本，同时保留拒绝编辑作为后续负反馈。
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_b912102d1da06715a0c97c77-a-separate-optimizer-model-turns-scored-rollouts-into-bounded-ad.md
@@ -0,0 +1,32 @@
+---
+id: "claim_b912102d1da06715a0c97c77"
+type: "claim"
+status: "proposal"
+title: "a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document,"
+created_at: "2026-07-19T02:52:10+08:00"
+updated_at: "2026-07-19T02:52:10+08:00"
+aliases: []
+tags: []
+domains: ["agent-skills", "agent-learning"]
+confidence: "medium"
+source_ids: ["source_54c9a7922f348a245d17efaf"]
+relations: [{"type": "derived_from", "target_id": "source_54c9a7922f348a245d17efaf", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "它给出将过程性经验固化为技能时的一种可检验接受标准。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_54c9a7922f348a245d17efaf"
+applicability: ["text-based skills evaluated on held-out task instances"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_a3dec3ea5dba6748c4cf", "evidence_kind": "paraphrase", "source_id": "source_54c9a7922f348a245d17efaf", "content_id": "content_87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3", "extraction_id": "extraction_ae71d8454de8760daabd9fa1", "span_start": -1, "span_end": 113, "original_text": "a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document,", "interpretation": "a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document,", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score."
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document,
+
+a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document,
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_bddbfc583594cb06ab113d17-an-edit-is-accepted-only-when-it-strictly-improves-a-held-out-va.md
@@ -0,0 +1,32 @@
+---
+id: "claim_bddbfc583594cb06ab113d17"
+type: "claim"
+status: "proposal"
+title: "an edit is accepted only when it strictly improves a held-out validation score."
+created_at: "2026-07-19T02:52:10+08:00"
+updated_at: "2026-07-19T02:52:10+08:00"
+aliases: []
+tags: []
+domains: ["agent-skills", "agent-learning"]
+confidence: "medium"
+source_ids: ["source_54c9a7922f348a245d17efaf"]
+relations: [{"type": "derived_from", "target_id": "source_54c9a7922f348a245d17efaf", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_skill_compilation_boundary", "reason": "它给出将过程性经验固化为技能时的一种可检验接受标准。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_54c9a7922f348a245d17efaf"
+applicability: ["text-based skills evaluated on held-out task instances"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_2641831bfdc5d23523c7", "evidence_kind": "paraphrase", "source_id": "source_54c9a7922f348a245d17efaf", "content_id": "content_87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3", "extraction_id": "extraction_ae71d8454de8760daabd9fa1", "span_start": -1, "span_end": 78, "original_text": "an edit is accepted only when it strictly improves a held-out validation score.", "interpretation": "an edit is accepted only when it strictly improves a held-out validation score.", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score."
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# an edit is accepted only when it strictly improves a held-out validation score.
+
+an edit is accepted only when it strictly improves a held-out validation score.
```
