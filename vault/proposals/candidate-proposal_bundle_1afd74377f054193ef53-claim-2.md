---
id: "claim_6c78036028e3192540cdf5fc"
type: "claim"
status: "proposal"
title: "Specifically, we propose a staged training paradigm with different learning objectives: first, we autoregressively pre-train a VLM backbone on large-scale egoce"
created_at: "2026-07-19T02:51:00+08:00"
updated_at: "2026-07-19T02:51:00+08:00"
aliases: []
tags: []
domains: ["embodied-ai", "vla", "humanoid"]
confidence: "medium"
source_ids: ["source_691f3acc1fe3382639690f59"]
relations: [{"type": "derived_from", "target_id": "source_691f3acc1fe3382639690f59", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "supports", "target_id": "concept_embodied_data_loop", "reason": "论文给出将异构数据按表征学习和机器人控制分阶段使用的具体实例。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
change_reason: "compile bundle from source_691f3acc1fe3382639690f59"
applicability: ["Ψ₀ humanoid loco-manipulation training setup"]
uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
evidence: [{"evidence_id": "evidence_0a57daab0fc4bbb976db", "evidence_kind": "quote", "source_id": "source_691f3acc1fe3382639690f59", "content_id": "content_445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb", "extraction_id": "extraction_89195c64af20a8a1d0967598", "span_start": 1138, "span_end": 1371, "original_text": "Specifically, we propose a staged training paradigm with different learning objectives: first, we autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations", "interpretation": null, "section": null, "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
atomicity_status: "atomic"
evidence_coverage: "full"
split_from: "Specifically, we propose a staged training paradigm with different learning objectives: first, we autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations; then, we post-train a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control."
split_reason: "multiple independently testable clauses"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "unknown"
evidence_entailment: "full"
claim_confidence: "medium"
publication_gate: "needs_review"
---

# Specifically, we propose a staged training paradigm with different learning objectives: first, we autoregressively pre-train a VLM backbone on large-scale egoce

Specifically, we propose a staged training paradigm with different learning objectives: first, we autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations
