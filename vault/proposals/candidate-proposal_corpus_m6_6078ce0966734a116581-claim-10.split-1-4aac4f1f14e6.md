---
id: "claim_physo_rnn_reinforcement_learning_method_20260716"
type: "claim"
status: "proposal"
title: "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式"
created_at: "2026-07-15T18:45:00+08:00"
updated_at: "2026-07-16T19:10:00+08:00"
aliases: []
tags: ["PhySO", "symbolic-regression", "reinforcement-learning", "rnn"]
domains: ["machine-learning", "physics"]
confidence: "medium"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "从量子位对 PhySO 方法的二手报道拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "proposal"}]
applicability: ["PhySO 方法结构"]
uncertainty: "二手报道证据，等待已捕获 primary PDF 逐字核验。"
evidence: [{"evidence_id": "ev_290", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 290, "span_end": 332, "original_text": "Φ-SO背后的技术被叫做“深度符号回归”，使用循环神经网络（RNN）+强化学习实现。", "section": "方法名称", "stance": "supports", "verification_status": "verified", "reason": "文内对技术路线的命名与组件。"}]
atomicity_status: "atomic"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_review"
split_from: "claim_wechat_physo_method_20260715"
split_reason: "将 RNN/RL 生成方法与单位约束作用分开核验"
---

Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。
