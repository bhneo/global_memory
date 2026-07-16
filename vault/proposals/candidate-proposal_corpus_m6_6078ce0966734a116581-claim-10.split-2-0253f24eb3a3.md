---
id: "claim_physo_units_constraints_reduce_search_20260716"
type: "claim"
status: "proposal"
title: "Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间"
created_at: "2026-07-15T18:45:00+08:00"
updated_at: "2026-07-16T19:10:00+08:00"
aliases: []
tags: ["PhySO", "symbolic-regression", "units-constraints"]
domains: ["machine-learning", "physics"]
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "从量子位对 PhySO 单位约束的二手报道拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "proposal"}]
applicability: ["PhySO 的单位一致性生成约束"]
uncertainty: "二手报道证据，等待已捕获 primary PDF 逐字核验。"
evidence: [{"evidence_id": "ev_388", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 388, "span_end": 436, "original_text": "同时将物理条件作为先验知识纳入学习过程中，避免AI搞出没有实际含义的公式，可以大大减少搜索空间。", "section": "物理先验", "stance": "supports", "verification_status": "verified", "reason": "文内对先验约束作用的描述。"}]
atomicity_status: "atomic"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_review"
split_from: "claim_wechat_physo_method_20260715"
split_reason: "将单位约束作用与 RNN/RL 生成方法分开核验"
---

Φ-SO 在生成过程中施加物理单位约束，以排除单位不一致表达式并缩小搜索空间。
