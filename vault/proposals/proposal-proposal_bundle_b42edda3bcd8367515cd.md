---
id: "proposal_bundle_b42edda3bcd8367515cd"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub"
created_at: "2026-07-19T03:01:52+08:00"
updated_at: "2026-07-19T03:01:53+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_34d6513b0522739d0b25e303"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_050b3e68335b770d39f1ba85"
input_sha256: "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_generalist_cross_embodiment_vla", "target_path": "vault/knowledge/concepts/concept_generalist_cross_embodiment_vla-跨本体通用-vla-策略.md", "base_sha256": null, "candidate_sha256": "53554fe46394c350e9f4d04c35326fd3a8a97dec6ff9e54c60121411cfe001df", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_generalist_cross_embodiment_vla.md", "working_at": "2026-07-19T03:01:53+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_251ad28e5021bb5fb97a0f2b", "target_path": "vault/knowledge/claims/claim_251ad28e5021bb5fb97a0f2b-the-neural-network-architecture-of-gr00t-n1-7-is-a-combination-o.md", "base_sha256": null, "candidate_sha256": "4cc1fef51f700f3d33a77f58641e8c1b7f74b90a3193174afd8feb736cdc70ad", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_251ad28e5021bb5fb97a0f2b.md", "working_at": "2026-07-19T03:01:53+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_758e87c35e680435e7968bfe", "target_path": "vault/knowledge/claims/claim_758e87c35e680435e7968bfe-diffusion-transformer-head-that-denoises-continuous-actions.md", "base_sha256": null, "candidate_sha256": "5dd4780722f8523b978eb45da6b63d02031a0d0c23460ada775b60cacc6d68b2", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_758e87c35e680435e7968bfe.md", "working_at": "2026-07-19T03:01:53+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 3, "source_id": "source_34d6513b0522739d0b25e303"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 3, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 3, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub

## 编译边界

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_050b3e68335b770d39f1ba85`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_generalist_cross_embodiment_vla-跨本体通用-vla-策略.md
@@ -0,0 +1,20 @@
+---
+id: "concept_generalist_cross_embodiment_vla"
+type: "concept"
+status: "proposal"
+title: "跨本体通用 VLA 策略"
+created_at: "2026-07-19T03:01:52+08:00"
+updated_at: "2026-07-19T03:01:52+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "cross-embodiment", "humanoid"]
+confidence: "medium"
+source_ids: ["source_34d6513b0522739d0b25e303"]
+relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "跨本体通用策略需要处理共享表征与本体专属控制之间的对齐。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
+uncertainty: "通用性取决于训练数据、动作空间和具体部署支持，不能从项目定位推出任意机器人上的零样本泛化。"
+---
+
+# 跨本体通用 VLA 策略
+
+以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_251ad28e5021bb5fb97a0f2b-the-neural-network-architecture-of-gr00t-n1-7-is-a-combination-o.md
@@ -0,0 +1,32 @@
+---
+id: "claim_251ad28e5021bb5fb97a0f2b"
+type: "claim"
+status: "proposal"
+title: "The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model"
+created_at: "2026-07-19T03:01:52+08:00"
+updated_at: "2026-07-19T03:01:52+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "humanoid"]
+confidence: "medium"
+source_ids: ["source_34d6513b0522739d0b25e303"]
+relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "instantiates", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "该架构是跨本体通用 VLA 的具体实现。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
+applicability: ["NVIDIA Isaac GR00T N1.7 repository release"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_9d814f3351cd8e54a857", "evidence_kind": "quote", "source_id": "source_34d6513b0522739d0b25e303", "content_id": "content_033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393", "extraction_id": "extraction_050b3e68335b770d39f1ba85", "span_start": 3256, "span_end": 3354, "original_text": "The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model", "interpretation": null, "section": null, "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model and diffusion transformer head that denoises continuous actions."
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model
+
+The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_758e87c35e680435e7968bfe-diffusion-transformer-head-that-denoises-continuous-actions.md
@@ -0,0 +1,32 @@
+---
+id: "claim_758e87c35e680435e7968bfe"
+type: "claim"
+status: "proposal"
+title: "diffusion transformer head that denoises continuous actions."
+created_at: "2026-07-19T03:01:52+08:00"
+updated_at: "2026-07-19T03:01:52+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "humanoid"]
+confidence: "medium"
+source_ids: ["source_34d6513b0522739d0b25e303"]
+relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "instantiates", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "该架构是跨本体通用 VLA 的具体实现。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_34d6513b0522739d0b25e303"
+applicability: ["NVIDIA Isaac GR00T N1.7 repository release"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_f79885bcfc7715f2cdc7", "evidence_kind": "quote", "source_id": "source_34d6513b0522739d0b25e303", "content_id": "content_033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393", "extraction_id": "extraction_050b3e68335b770d39f1ba85", "span_start": 3359, "span_end": 3419, "original_text": "diffusion transformer head that denoises continuous actions.", "interpretation": null, "section": null, "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model and diffusion transformer head that denoises continuous actions."
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# diffusion transformer head that denoises continuous actions.
+
+diffusion transformer head that denoises continuous actions.
```
