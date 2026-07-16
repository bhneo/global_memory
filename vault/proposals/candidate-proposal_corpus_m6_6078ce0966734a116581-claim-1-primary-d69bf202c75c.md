---
id: "claim_wechat_epiplexity_definition_20260715"
type: "claim"
status: "proposal"
title: "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable"
created_at: "2026-07-15T23:50:00+08:00"
updated_at: "2026-07-16T19:43:26+08:00"
aliases: []
tags: ["epiplexity", "information-theory", "computational-bounds", "minimum-description-length"]
domains: ["information-theory", "machine-learning"]
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"]
relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "Secondary interpretation retained for provenance; formal wording corrected from the primary paper", "confidence": "low", "created_by": "m6.1-primary-scope-correction", "status": "proposal"}, {"type": "derived_from", "target_id": "source_1c0f944bf6b14cf9d1fff939", "reason": "Primary paper formally defines epiplexity as the program-length component of the compute-bounded minimum two-part code", "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "proposal"}]
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
---

For the time-bounded minimum-description-length program P*, the paper defines T-bounded epiplexity S_T(X) as the program length |P*|. It interprets this as structure and regularity visible at compute level T, without guaranteeing usefulness for a particular downstream task.
