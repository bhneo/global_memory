---
id: "claim_wechat_param_symmetry_conserved_quantities_20260716"
title: "该文称连续对称性在梯度流中对应守恒量，影响隐式偏置与收敛/泛化统计"
tags: ["conserved-quantities", "implicit-bias", "gradient-flow"]
domains: ["deep-learning", "optimization"]
confidence: "medium"
applicability: ["诺特定理类比下的训练动力学讨论", "初始化与守恒量关系"]
uncertainty: "守恒量例子（Gram 矩阵差等）为科普列举；严格定理条件需回原文。"
evidence: [{"evidence_id": "ev_1860", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 1860, "span_end": 1898, "original_text": "守恒量（conserved quantities）—— 类似物理中的诺特定理", "section": "对称与守恒", "stance": "supports", "verification_status": "verified", "reason": "文内将对称性与守恒量的物理类比。"}, {"evidence_id": "ev_2009", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 2009, "span_end": 2092, "original_text": "隐式偏置（implicit bias）：\n\n不同的初始化对应不同的守恒量值，进而影响最终的收敛点和泛化性能。也就是说，参数空间的对称结构决定了学习轨迹与结果的统计分布", "section": "隐式偏置", "stance": "supports", "verification_status": "verified", "reason": "文内对守恒量影响收敛与泛化分布的说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T00:06:00+08:00"
updated_at: "2026-07-16T16:30:21+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "M6 corpus distillation from claim_wechat_param_symmetry_conserved_quantities_20260716"
source_ids: ["source_6ae6c4bef52010f96ddb3dbf"]
relations: [{"type": "derived_from", "target_id": "source_6ae6c4bef52010f96ddb3dbf", "reason": "由机器之心对 arXiv:2506.13018 参数空间对称性综述的科普转述归纳；原论文未 capture", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "proposal"}]
atomicity_status: "atomic"
evidence_coverage: "missing"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_review"
---

# 守恒量与隐式偏置

对称结构约束梯度流轨迹与结果分布。
