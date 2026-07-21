---
id: "claim_ed202cdc4c79d46f2ac31913"
type: "claim"
status: "working"
title: "该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选"
created_at: "2026-07-19T03:03:50+08:00"
updated_at: "2026-07-19T03:05:44+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "value-function"]
confidence: "medium"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "supports", "target_id": "concept_vla_action_evaluation_distillation", "reason": "候选覆盖显著高于单次选择表现，支持把瓶颈部分归因于动作评价而非纯生成。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_ff90ad99bd47043e812cce9e"
applicability: ["reported diagnostic embodied benchmark settings"]
uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
evidence: [{"evidence_id": "evidence_a0ed7c22bb0d15f4c2cb", "evidence_kind": "paraphrase", "source_id": "source_ff90ad99bd47043e812cce9e", "content_id": "content_fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c", "extraction_id": "extraction_b80f55d96258c5cbdae58ac8", "span_start": -1, "span_end": 188, "original_text": "A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.", "interpretation": "A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
atomicity_status: "atomic"
evidence_coverage: "missing"
split_from: null
split_reason: null
quote_verification: "failed"
extraction_quality: "good"
epistemic_source_authority: "primary"
evidence_entailment: "full"
claim_confidence: "medium"
publication_gate: "needs_review"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T03:05:44+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_ec30b88a6f8a07464311"
origin_item_id: "claim-2"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_ec30b88a6f8a07464311-claim-2.md"
origin_candidate_sha256: "571b26ec5847917f8a9922a9271d099babd4184719fce53de28dabf63288dd20"
memory_schema_version: 2
last_consolidation_id: "consolidation_56ecb37c89765ae7a88e842d"
---

# 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选

A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.
