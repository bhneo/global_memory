---
id: "claim_wechat_lie_group_definition_20260715"
title: "该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合"
tags: ["lie-group", "differential-geometry", "manifold"]
domains: ["mathematics"]
confidence: "medium"
applicability: ["文内第二节李群定义", "圆的对称 vs 离散群对比语境"]
uncertainty: "提取文本中公式符号有 HTML 丢失；相容性条件未完整呈现数学细节。"
evidence: [{"evidence_id": "ev_1682", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 1682, "span_end": 1843, "original_text": "当我们说到圆的变换时，我们可以谈圆转了一个无穷小的角度。对于群这个代数结构来说并不能体现“无穷小”这个概念，因为无穷小涉及到极限，而极限的概念依赖于拓扑而非群。所以我们需要同时用到群结构和拓扑结构才可以准确的说明这种变换。在实际应用中，我们通常不仅需要拓扑结构，还需要建立在拓扑上的微分结构，这两者结合就引出了李群的概念。", "section": "连续 vs 离散", "stance": "supports", "verification_status": "verified", "reason": "文内说明圆对称需要拓扑/微分结构。"}, {"evidence_id": "ev_1843", "evidence_kind": "quote", "source_id": "source_941321d95232028c233c9433", "content_id": "content_8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "extraction_id": "extraction_c4f0793e6fac8c18c8ed3a6f", "input_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "span_start": 1843, "span_end": 1980, "original_text": "定义一个李群为一个集合，满足1.是个群2.是个微分流形3.的群结构和微分结构相容。一般来说我们会将每一个群元对应到流形上一点，并且把单位元置于原点处。相容性条件告诉我们群运算1）可以写成流形上的一个二元映射并且映射是光滑的。2）, 存在  满足。李群同时具有群结构和微分结构", "section": "李群定义", "stance": "supports", "verification_status": "verified", "reason": "文内对李群三重条件的概述。"}]
type: "claim"
status: "working"
created_at: "2026-07-15T21:00:00+08:00"
updated_at: "2026-07-17T18:35:48+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "M6 corpus distillation from claim_wechat_lie_group_definition_20260715"
source_ids: ["source_941321d95232028c233c9433"]
relations: [{"type": "derived_from", "target_id": "source_941321d95232028c233c9433", "reason": "由中科院物理所转载的李群李代数科普文章归纳；非教材定理证明", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
atomicity_status: "atomic"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_review"
memory_tier: "working"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 3
last_consolidated_at: "2026-07-17T18:35:48+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-5"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-5-rev-9faa2d5d305d.md"
origin_candidate_sha256: "9faa2d5d305dd4cf9af7116e14578b08b2aa16fcf789feb1a8e35e9337b7ee73"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_1a43d39c3e1d556e9076863b"
---

# 李群定义

群 + 微分流形 + 相容运算。
