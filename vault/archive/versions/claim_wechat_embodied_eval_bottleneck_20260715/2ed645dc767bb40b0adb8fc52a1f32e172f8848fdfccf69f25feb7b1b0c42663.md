---
id: "claim_wechat_embodied_eval_bottleneck_20260715"
title: "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住"
tags: ["real-robot", "evaluation", "vla"]
domains: ["robotics", "robot-learning"]
confidence: "medium"
applicability: ["作者描述的具身 VLA 真机评测流程", "需要排队、人工摆场、逐次记录的场景"]
uncertainty: "来自作者基于行业经验的论断，未给出量化对比实验；「一两天出分」为顺利情况下的经验描述。"
evidence: [{"evidence_id": "ev_597", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 597, "span_end": 677, "original_text": "具身的 VLA 训完一版，想知道行不行，得提交给真机评测团队，先排队，再由人一件件把测试道具摆到场地上，守着机器人一遍遍跑、一次次记，顺利的话一两天后才出个分。", "section": "真机评测流程", "stance": "supports", "verification_status": "verified", "reason": "作者对评估流程耗时的具体描述。"}, {"evidence_id": "ev_692", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 692, "span_end": 718, "original_text": "迭代速度，很多时候不是被训练卡住的，是被评估卡住的。", "section": "瓶颈判断", "stance": "supports", "verification_status": "verified", "reason": "作者对瓶颈来源的判断句。"}]
type: "claim"
status: "working"
created_at: "2026-07-15T18:12:00+08:00"
updated_at: "2026-07-19T12:19:58+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "M6 corpus distillation from claim_wechat_embodied_eval_bottleneck_20260715"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由微信公众号评论文章归纳；非独立 peer-reviewed 论文正文", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
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
consolidation_count: 5
last_consolidated_at: "2026-07-19T12:19:58+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-15"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-15-rev-858705a479c1.md"
origin_candidate_sha256: "858705a479c17f917d0201a933aa80915a26b20bdf5dda2ba6de478e9940c4ee"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_e08882418699e8ec03567bd8"
---

# 评估瓶颈

真机评测排队与人工摆场使迭代受评估而非训练限制。
