---
id: "claim_physo_rnn_reinforcement_learning_method_20260716"
type: "claim"
status: "trusted"
title: "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式"
created_at: "2026-07-15T18:45:00+08:00"
updated_at: "2026-07-17T12:02:24+08:00"
aliases: []
tags: ["PhySO", "symbolic-regression", "reinforcement-learning", "rnn"]
domains: ["machine-learning", "physics"]
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"]
relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "从量子位对 PhySO 方法的二手报道拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "working"}, {"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "Primary PhySO PDF states that deep reinforcement learning trains the RNN", "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "working"}]
applicability: ["PhySO 方法结构"]
uncertainty: "已逐字回验 primary PDF；仍需用户审批后才能进入 canonical。"
evidence: [{"evidence_id": "ev_290", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 290, "span_end": 332, "original_text": "Φ-SO背后的技术被叫做“深度符号回归”，使用循环神经网络（RNN）+强化学习实现。", "section": "方法名称", "stance": "supports", "verification_status": "verified", "reason": "文内对技术路线的命名与组件。"}, {"evidence_id": "ev_primary_2e7e308b02a1", "evidence_kind": "quote", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "span_start": 91196, "span_end": 91319, "original_text": "We adopt\nthe very successful deep reinforcement learning strategy\nof Petersen et al. (2021a), which we use to train our RNN", "section": "Conclusion, PDF page 21", "stance": "supports", "verification_status": "verified", "reason": "Primary PhySO PDF states that deep reinforcement learning trains the RNN"}]
atomicity_status: "atomic"
evidence_coverage: "full"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "primary"
evidence_entailment: "full"
claim_confidence: "high"
publication_gate: "needs_review"
split_from: "claim_wechat_physo_method_20260715"
split_reason: "将 RNN/RL 生成方法与单位约束作用分开核验"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "promotion-policy"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-17T12:01:10+08:00"
last_verified_at: null
trust_score: 100
trust_reasons: ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"]
promotion_history: [{"promotion_id": "promotion_5717e51045bf3f2bc96e0e26", "object_id": "claim_physo_rnn_reinforcement_learning_method_20260716", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"], "failed_conditions": [], "supporting_sources": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "contradictions": [], "promoted_at": "2026-07-17T12:02:24+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-10.split-1"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-10.split-1-primary-02a8b5565a84.md"
origin_candidate_sha256: "02a8b5565a847f329f026166d1151e5bdcd7d92047cff276ca0d9a89b1971e6e"
memory_schema_version: 1
---

Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。
