---
id: "proposal_bundle_2742a626a6fa72800ce5"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-17T12:17:09+08:00"
updated_at: "2026-07-17T12:17:10+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ca1f80f2bf2e7d410ab2459e"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_9bc53d972ae8ac3a7cbb3807"
input_sha256: "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_499470a2d077fe16b177bd1e", "target_path": "vault/knowledge/claims/claim_499470a2d077fe16b177bd1e-preprint-skillevolver-skilllearning-as-ameta-skill-genrui-zhang2.md", "base_sha256": null, "candidate_sha256": "b87185bb69c70a0c9b2c1b3bb05390fa04c30487d93ee99c15802debcd07edef", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_2742a626a6fa72800ce5-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_499470a2d077fe16b177bd1e.md", "working_at": "2026-07-17T12:17:10+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_080bdc5349e0e08fa8882e97", "target_path": "vault/knowledge/claims/claim_080bdc5349e0e08fa8882e97-then-consumed-unchanged-with-no-mechanism-to-improve-from-real-u.md", "base_sha256": null, "candidate_sha256": "e2591c4916eba7aed061e49a38542fc7fb8a83aaa6f5550b247ac4939354136d", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_2742a626a6fa72800ce5-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_080bdc5349e0e08fa8882e97.md", "working_at": "2026-07-17T12:17:10+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…Measuring collaborative emergent behav-\nior in multi-agent reinforcement learning.arXiv [preprint]\narXiv:1807.08663, 2018.\nBogin, B…", "match_reason": "full-text:body"}, {"id": "claim_wechat_skillevolver_k4_strategy_exploration_20260716", "type": "claim", "title": "该文称 SkillEvolver 每轮显式生成 K=4 个覆盖不同高层决策轴的策略", "path": "vault/memory/claim/claim_wechat_skillevolver_k4_strategy_exploration_20260716.md", "status": "trusted", "source_ids": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "该文称 [SkillEvolver] 每轮显式生成 K=4 个覆盖不同高层决策轴的策略。", "match_reason": "metadata:title"}, {"id": "claim_wechat_skillevolver_silent_bypass_audit_20260716", "type": "claim", "title": "该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本", "path": "vault/memory/claim/claim_wechat_skillevolver_silent_bypass_audit_20260716.md", "status": "trusted", "source_ids": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "该文称 [SkillEvolver] 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本。", "match_reason": "metadata:title"}, {"id": "claim_4766d041f4bbb95d5823e5dd", "type": "claim", "title": "来源原文：[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill", "path": "vault/memory/claim/claim_4766d041f4bbb95d5823e5dd.md", "status": "working", "source_ids": ["source_0214d3d2f8cddf30a1140f8a"], "snippet": "# 来源原文：[2605.10500] [SkillEvolver]: Skill Learning as a Meta-Skill\n\n[2605.10500] [SkillEvolver]: Skill Learning as a Meta…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2605_10500", "type": "work", "title": "[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill", "path": "vault/memory/work/work_arxiv_2605_10500.md", "status": "working", "source_ids": ["source_0214d3d2f8cddf30a1140f8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "# [2605.10500] [SkillEvolver]: Skill Learning as a Meta-Skill\n\n## Logical work identity\n\n- arXiv：`2605.10500`\n- Version：`unknown`\n- Captures…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_ca1f80f2bf2e7d410ab2459e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 2, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 2, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_9bc53d972ae8ac3a7cbb3807`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_499470a2d077fe16b177bd1e-preprint-skillevolver-skilllearning-as-ameta-skill-genrui-zhang2.md
@@ -0,0 +1,32 @@
+---
+id: "claim_499470a2d077fe16b177bd1e"
+type: "claim"
+status: "proposal"
+title: "Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong"
+created_at: "2026-07-17T12:17:09+08:00"
+updated_at: "2026-07-17T12:17:09+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_ca1f80f2bf2e7d410ab2459e"]
+relations: [{"type": "derived_from", "target_id": "source_ca1f80f2bf2e7d410ab2459e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ca1f80f2bf2e7d410ab2459e"
+evidence: [{"evidence_id": "evidence_66c305d8ef8ae5dbaeb5", "evidence_kind": "paraphrase", "source_id": "source_ca1f80f2bf2e7d410ab2459e", "content_id": "content_4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "extraction_id": "extraction_9bc53d972ae8ac3a7cbb3807", "span_start": -1, "span_end": 304, "original_text": "Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong University ABSTRACT Agent skills today arestatic artifacts: authored once – by human curation or one- shot generation from parametric knowledge –", "interpretation": "Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong University ABSTRACT Agent skills today arestatic artifacts: authored once – by human curation or one- shot generation from parametric knowledge –", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "Preprint.\nSKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL\nGenrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1†\n1Tsinghua University 2Beijing Jiaotong University\nABSTRACT\nAgent skills today arestatic artifacts: authored once – by human curation or one-\nshot generation from parametric knowledge – and then consumed unchanged, with\nno mechanism to improve from real use. We proposeSkillEvolver, a lightweight,\nplug-and-play solution foronline skill learning, in which a singlemeta-skilliter-\n"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong
+
+Preprint. SKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL Genrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1† 1Tsinghua University 2Beijing Jiaotong University ABSTRACT Agent skills today arestatic artifacts: authored once – by human curation or one- shot generation from parametric knowledge –
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_080bdc5349e0e08fa8882e97-then-consumed-unchanged-with-no-mechanism-to-improve-from-real-u.md
@@ -0,0 +1,32 @@
+---
+id: "claim_080bdc5349e0e08fa8882e97"
+type: "claim"
+status: "proposal"
+title: "then consumed unchanged, with no mechanism to improve from real use. We proposeSkillEvolver, a lightweight, plug-and-play solution foronline skill learning, in"
+created_at: "2026-07-17T12:17:09+08:00"
+updated_at: "2026-07-17T12:17:09+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_ca1f80f2bf2e7d410ab2459e"]
+relations: [{"type": "derived_from", "target_id": "source_ca1f80f2bf2e7d410ab2459e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ca1f80f2bf2e7d410ab2459e"
+evidence: [{"evidence_id": "evidence_444679d5b6b22361ed50", "evidence_kind": "paraphrase", "source_id": "source_ca1f80f2bf2e7d410ab2459e", "content_id": "content_4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "extraction_id": "extraction_9bc53d972ae8ac3a7cbb3807", "span_start": -1, "span_end": 188, "original_text": "then consumed unchanged, with no mechanism to improve from real use. We proposeSkillEvolver, a lightweight, plug-and-play solution foronline skill learning, in which a singlemeta-skilliter-", "interpretation": "then consumed unchanged, with no mechanism to improve from real use. We proposeSkillEvolver, a lightweight, plug-and-play solution foronline skill learning, in which a singlemeta-skilliter-", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "Preprint.\nSKILLEVOLVER: SKILLLEARNING AS AMETA-SKILL\nGenrui Zhang2∗ Erle Zhu1∗ Jinfeng Zhou1 Caiyan Jia2 Hongning Wang1†\n1Tsinghua University 2Beijing Jiaotong University\nABSTRACT\nAgent skills today arestatic artifacts: authored once – by human curation or one-\nshot generation from parametric knowledge – and then consumed unchanged, with\nno mechanism to improve from real use. We proposeSkillEvolver, a lightweight,\nplug-and-play solution foronline skill learning, in which a singlemeta-skilliter-\n"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# then consumed unchanged, with no mechanism to improve from real use. We proposeSkillEvolver, a lightweight, plug-and-play solution foronline skill learning, in
+
+then consumed unchanged, with no mechanism to improve from real use. We proposeSkillEvolver, a lightweight, plug-and-play solution foronline skill learning, in which a singlemeta-skilliter-
```
