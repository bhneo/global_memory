---
id: "claim_physo_units_constraints_reduce_search_20260716"
type: "claim"
status: "trusted"
title: "Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间"
created_at: "2026-07-15T18:45:00+08:00"
updated_at: "2026-07-17T15:23:46+08:00"
aliases: []
tags: ["PhySO", "symbolic-regression", "units-constraints"]
domains: ["machine-learning", "physics"]
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"]
relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "从量子位对 PhySO 单位约束的二手报道拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "working"}, {"type": "derived_from", "target_id": "source_b85c7e35189fedbd359efa94", "reason": "Primary PhySO PDF states that generated solutions are units-consistent by construction", "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "working"}]
applicability: ["PhySO 的单位一致性生成约束"]
uncertainty: "已逐字回验 primary PDF；仍需用户审批后才能进入 canonical。"
evidence: [{"evidence_id": "ev_388", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 388, "span_end": 436, "original_text": "同时将物理条件作为先验知识纳入学习过程中，避免AI搞出没有实际含义的公式，可以大大减少搜索空间。", "section": "物理先验", "stance": "supports", "verification_status": "verified", "reason": "文内对先验约束作用的描述。"}, {"evidence_id": "ev_primary_67f24f6c168a", "evidence_kind": "quote", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "span_start": 1143, "span_end": 1240, "original_text": "from the ground up, to propose solutions where the physical units are consistent by construction.", "section": "Abstract, PDF page 1", "stance": "supports", "verification_status": "verified", "reason": "Primary PhySO PDF states that generated solutions are units-consistent by construction"}, {"evidence_id": "ev_primary_d79ac7b3a44d", "evidence_kind": "quote", "source_id": "source_b85c7e35189fedbd359efa94", "content_id": "content_895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "extraction_id": "extraction_f7743ab92a554c94f10a12cd", "input_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "span_start": 1343, "span_end": 1466, "original_text": "rules of dimensional analysis restrict enormously the freedom of the equation generator, thus vastly\nimproving performance.", "section": "Abstract, PDF page 1", "stance": "supports", "verification_status": "verified", "reason": "Primary PhySO PDF states that dimensional-analysis rules restrict generator freedom"}]
atomicity_status: "atomic"
evidence_coverage: "full"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "primary"
evidence_entailment: "full"
claim_confidence: "high"
publication_gate: "needs_review"
split_from: "claim_wechat_physo_method_20260715"
split_reason: "将单位约束作用与 RNN/RL 生成方法分开核验"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v1"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-17T15:23:46+08:00"
last_verified_at: null
trust_score: 100
trust_reasons: ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"]
promotion_history: [{"promotion_id": "promotion_8c4ed1b7289ce5865a314954", "object_id": "claim_physo_units_constraints_reduce_search_20260716", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"], "failed_conditions": [], "supporting_sources": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "contradictions": [], "promoted_at": "2026-07-17T12:02:31+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-10.split-2"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-10.split-2-primary-56500a927a1c.md"
origin_candidate_sha256: "56500a927a1c126a26835ecf986c44f78e52905531151233eb82fbcdad92fa99"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "supported"
last_consolidation_id: "consolidation_0b45491886bff038a1dbb2ad"
---

Φ-SO 在生成过程中施加物理单位约束，以排除单位不一致表达式并缩小搜索空间。
