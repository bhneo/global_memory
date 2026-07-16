---
id: "claim_wechat_epiplexity_definition_20260715"
type: "claim"
status: "proposal"
title: "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable"
created_at: "2026-07-15T23:50:00+08:00"
updated_at: "2026-07-16T19:45:00+08:00"
aliases: []
tags: ["epiplexity", "information-theory", "computational-bounds", "minimum-description-length"]
domains: ["information-theory", "machine-learning"]
confidence: "medium"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
relations: [{"type": "derived_from", "target_id": "source_494ab02c17c5f495f1ed29d0", "reason": "Secondary interpretation retained for provenance; formal wording corrected from the primary paper", "confidence": "low", "created_by": "m6.1-primary-scope-correction", "status": "proposal"}]
applicability: ["Definition 8 of arXiv:2601.03220 for a random variable and compute bound T"]
uncertainty: "Epiplexity captures structure visible at a compute level; the paper explicitly states that it does not guarantee relevance to a specific downstream task or OOD generalization."
evidence: []
atomicity_status: "atomic"
evidence_coverage: "missing"
quote_verification: "not_applicable"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "none"
claim_confidence: "medium"
publication_gate: "needs_evidence"
---

For the time-bounded minimum-description-length program P*, the paper defines T-bounded epiplexity S_T(X) as the program length |P*|. It interprets this as structure and regularity visible at compute level T, without guaranteeing usefulness for a particular downstream task.
