---
id: "claim_wechat_epiplexity_definition_20260715"
type: "claim"
status: "trusted"
title: "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable"
created_at: "2026-07-15T23:50:00+08:00"
updated_at: "2026-07-17T22:40:00+08:00"
aliases: []
tags: ["epiplexity", "information-theory", "computational-bounds", "minimum-description-length"]
domains: ["information-theory", "machine-learning"]
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"]
relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "Secondary interpretation retained for provenance; formal wording corrected from the primary paper", "confidence": "low", "created_by": "m6.1-primary-scope-correction", "status": "working"}, {"type": "derived_from", "target_id": "source_1c0f944bf6b14cf9d1fff939", "reason": "Primary paper formally defines epiplexity as the program-length component of the compute-bounded minimum two-part code", "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "working"}]
applicability: ["Definition 8 of arXiv:2601.03220 for a random variable and compute bound T"]
uncertainty: "已逐字回验 primary PDF；仍需用户审批后才能进入 canonical。"
evidence: [{"evidence_id": "ev_primary_f7df8420e167", "evidence_kind": "quote", "source_id": "source_1c0f944bf6b14cf9d1fff939", "content_id": "content_8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extraction_id": "extraction_c970040f818d88a47cff99b3", "input_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "span_start": 34703, "span_end": 34827, "original_text": "We define theT-boundedepiplexityS T andentropyH T of the random variable\nXas\nST (X) :=|P ⋆|,andH T (X) :=E[log 1/P ⋆(X)].(4)", "section": "Definition 8, PDF page 10", "stance": "supports", "verification_status": "verified", "reason": "Primary paper formally defines epiplexity as the program-length component of the compute-bounded minimum two-part code"}, {"evidence_id": "ev_primary_749ece9a1660", "evidence_kind": "quote", "source_id": "source_1c0f944bf6b14cf9d1fff939", "content_id": "content_8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "extraction_id": "extraction_c970040f818d88a47cff99b3", "input_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "span_start": 13254, "span_end": 13376, "original_text": "We emphasize,\nhowever, that epiplexity is a measure of information,nota guarantee of OOD generalization to\nspecific tasks.", "section": "Introduction, PDF page 4", "stance": "supports", "verification_status": "verified", "reason": "Primary paper explicitly limits epiplexity: it is not a guarantee of OOD generalization to a specific task"}]
atomicity_status: "atomic"
evidence_coverage: "full"
quote_verification: "not_applicable"
extraction_quality: "good"
epistemic_source_authority: "primary"
evidence_entailment: "full"
claim_confidence: "high"
publication_gate: "needs_review"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 6
last_consolidated_at: "2026-07-17T22:40:00+08:00"
last_verified_at: null
trust_score: 100
trust_reasons: ["valid consolidation receipt matches current object", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists", "drift audit has no high risk"]
promotion_history: [{"promotion_id": "promotion_74391a77b586f380ee7305f3", "object_id": "claim_wechat_epiplexity_definition_20260715", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"], "failed_conditions": [], "supporting_sources": ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"], "contradictions": [], "promoted_at": "2026-07-17T12:02:41+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-1"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-1-primary-d69bf202c75c.md"
origin_candidate_sha256: "d69bf202c75c20f3ef7b6dba0fbabe42742c382b8e681fd25bedc227ccf89cfa"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "supported"
last_consolidation_id: "consolidation_accffa7ead2e0318ab55d561"
needs_policy_requalification: false
trust_policy_version: "trusted-promotion-v3-receipt-v2"
last_policy_qualified_at: "2026-07-17T18:38:07+08:00"
last_valid_receipt_id: null
policy_requalification_failed_conditions: []
---

For the time-bounded minimum-description-length program P*, the paper defines T-bounded epiplexity S_T(X) as the program length |P*|. It interprets this as structure and regularity visible at compute level T, without guaranteeing usefulness for a particular downstream task.
