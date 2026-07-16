---
id: "claim_wechat_physo_method_20260715"
title: "该文称 Φ-SO 使用 RNN+强化学习的深度符号回归，并纳入物理先验约束搜索空间"
tags: ["symbolic-regression", "reinforcement-learning", "rnn"]
domains: ["machine-learning", "physics"]
confidence: "medium"
applicability: ["量子位对 PhySO 方法栈的概述", "深度符号回归 + 物理条件先验"]
uncertainty: "方法描述为媒体压缩版；RL 奖励设计等细节需回论文；不等同于独立方法评估。"
evidence: [{"evidence_id": "ev_290", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 290, "span_end": 332, "original_text": "Φ-SO背后的技术被叫做“深度符号回归”，使用循环神经网络（RNN）+强化学习实现。", "section": "方法名称", "stance": "supports", "verification_status": "verified", "reason": "文内对技术路线的命名与组件。"}, {"evidence_id": "ev_388", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 388, "span_end": 436, "original_text": "同时将物理条件作为先验知识纳入学习过程中，避免AI搞出没有实际含义的公式，可以大大减少搜索空间。", "section": "物理先验", "stance": "supports", "verification_status": "verified", "reason": "文内对先验约束作用的描述。"}, {"evidence_id": "ev_528", "evidence_kind": "quote", "source_id": "source_ef99e322cc662cffb7eb5c8f", "content_id": "content_fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "extraction_id": "extraction_a9bbb7d4b3a1e278c955120f", "input_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "span_start": 528, "span_end": 584, "original_text": "于是强化学习的规则被设计成，只对找出前5%的候选公式做奖励，找出另外95%也不做惩罚，鼓励模型充分探索搜索空间。", "section": "RL 奖励", "stance": "supports", "verification_status": "verified", "reason": "文内对符号回归 RL 奖励设计的描述。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-15T18:45:00+08:00"
updated_at: "2026-07-16T19:00:47+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "M6 corpus distillation from claim_wechat_physo_method_20260715"
source_ids: ["source_ef99e322cc662cffb7eb5c8f"]
relations: [{"type": "derived_from", "target_id": "source_ef99e322cc662cffb7eb5c8f", "reason": "由量子位公众号对 PhySO/Φ-SO 论文报道归纳；非 arXiv 原文 capture", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
atomicity_status: "compound"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_split"
---

# 方法栈

RNN + RL 深度符号回归，带物理先验。
