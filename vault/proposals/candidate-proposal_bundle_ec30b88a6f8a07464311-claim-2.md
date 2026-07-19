---
id: "claim_ed202cdc4c79d46f2ac31913"
type: "claim"
status: "proposal"
title: "该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选"
created_at: "2026-07-19T03:03:50+08:00"
updated_at: "2026-07-19T03:03:50+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "value-function"]
confidence: "medium"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
relations: [{"type": "derived_from", "target_id": "source_ff90ad99bd47043e812cce9e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_vla_action_evaluation_distillation", "reason": "候选覆盖显著高于单次选择表现，支持把瓶颈部分归因于动作评价而非纯生成。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
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
---

# 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选

A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32.
