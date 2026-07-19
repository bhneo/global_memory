---
id: "proposal_bundle_ec30b88a6f8a07464311"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T03:03:50+08:00"
updated_at: "2026-07-19T03:03:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_b80f55d96258c5cbdae58ac8"
input_sha256: "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_vla_action_evaluation_distillation", "target_path": "vault/knowledge/concepts/concept_vla_action_evaluation_distillation-vla-动作评估蒸馏.md", "base_sha256": null, "candidate_sha256": "3542f12e5f8958f0080a14086281120220baef7fb31311e93839bd7346840cf1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_ec30b88a6f8a07464311-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_vla_action_evaluation_distillation.md", "working_at": "2026-07-19T03:03:51+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_ed202cdc4c79d46f2ac31913", "target_path": "vault/knowledge/claims/claim_ed202cdc4c79d46f2ac31913-该研究的-pass-k-诊断显示冻结-vla-输出中存在大量可行候选.md", "base_sha256": null, "candidate_sha256": "571b26ec5847917f8a9922a9271d099babd4184719fce53de28dabf63288dd20", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "missing", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_ec30b88a6f8a07464311-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_ed202cdc4c79d46f2ac31913.md", "working_at": "2026-07-19T03:03:51+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_ff90ad99bd47043e812cce9e"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_b80f55d96258c5cbdae58ac8`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_vla_action_evaluation_distillation-vla-动作评估蒸馏.md
@@ -0,0 +1,20 @@
+---
+id: "concept_vla_action_evaluation_distillation"
+type: "concept"
+status: "proposal"
+title: "VLA 动作评估蒸馏"
+created_at: "2026-07-19T03:03:50+08:00"
+updated_at: "2026-07-19T03:03:50+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "reinforcement-learning", "planning", "value-function"]
+confidence: "medium"
+source_ids: ["source_ff90ad99bd47043e812cce9e"]
+relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "answers", "target_id": "question_world_model_action_value", "reason": "该方法用仿真回报蒸馏出的动作价值模型把长期后果预测连接到动作选择。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "两者都关注预测结果对策略评价的价值，但这里评价对象是冻结 VLA 产生的候选动作。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "评估器与生成器解耦，目标是在不后训练 VLA 主干的情况下保留通用能力。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
+uncertainty: "树搜索知识来自仿真，Q 评估器的 Sim-to-Real 外推和候选覆盖仍是限制。"
+---
+
+# VLA 动作评估蒸馏
+
+保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_ed202cdc4c79d46f2ac31913-该研究的-pass-k-诊断显示冻结-vla-输出中存在大量可行候选.md
@@ -0,0 +1,32 @@
+---
+id: "claim_ed202cdc4c79d46f2ac31913"
+type: "claim"
+status: "proposal"
+title: "该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选"
+created_at: "2026-07-19T03:03:50+08:00"
+updated_at: "2026-07-19T03:03:50+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "vla", "value-function"]
+confidence: "medium"
+source_ids: ["source_ff90ad99bd47043e812cce9e"]
+relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_vla_action_evaluation_distillation", "reason": "候选覆盖显著高于单次选择表现，支持把瓶颈部分归因于动作评价而非纯生成。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
+applicability: ["reported diagnostic embodied benchmark settings"]
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+evidence: [{"evidence_id": "evidence_a0ed7c22bb0d15f4c2cb", "evidence_kind": "paraphrase", "source_id": "source_ff90ad99bd47043e812cce9e", "content_id": "content_fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c", "extraction_id": "extraction_b80f55d96258c5cbdae58ac8", "span_start": -1, "span_end": 188, "original_text": "A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.", "interpretation": "A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+atomicity_status: "atomic"
+evidence_coverage: "missing"
+split_from: null
+split_reason: null
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "full"
+claim_confidence: "medium"
+publication_gate: "needs_review"
+---
+
+# 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选
+
+A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.
```
