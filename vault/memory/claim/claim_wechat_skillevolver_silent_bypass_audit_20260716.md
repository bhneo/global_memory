---
id: "claim_wechat_skillevolver_silent_bypass_audit_20260716"
type: "claim"
status: "trusted"
title: "该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本"
created_at: "2026-07-16T11:16:00+08:00"
updated_at: "2026-07-17T22:40:01+08:00"
aliases: []
tags: ["SkillEvolver", "auditor", "silent-bypass"]
domains: ["agent-systems", "software-engineering"]
confidence: "medium"
source_ids: ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"]
relations: [{"type": "derived_from", "target_id": "source_d01f40e4896de2e186cbbe8a", "reason": "由 SkillEvolver 二手解读的 Auditor 段落拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "working"}, {"type": "derived_from", "target_id": "source_ca1f80f2bf2e7d410ab2459e", "reason": "Primary PDF defines Auditor check 9 as silent-bypass at runtime", "confidence": "high", "created_by": "primary-quote-verification-v1", "status": "working"}]
applicability: ["技能声明正确但可能未被下游 Agent 使用的审计"]
uncertainty: "已逐字回验 primary PDF；仍需用户审批后才能进入 canonical。"
evidence: [{"evidence_id": "ev_7663", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 7663, "span_end": 7793, "original_text": "silent-bypass。这个非常实用：skill 声称有主脚本，但探索轨迹里多数失败运行根本没有 Bash 调用它。也就是说，skill 内容可能是对的，但下游 Agent 没有用。普通静态评审看不出来，只有把 skill 真部署给 fresh agent", "section": "silent-bypass 检查", "stance": "supports", "verification_status": "verified", "reason": "文内对第 9 类 Auditor 检查的描述。"}, {"evidence_id": "ev_primary_cc70d0b65105", "evidence_kind": "quote", "source_id": "source_ca1f80f2bf2e7d410ab2459e", "content_id": "content_4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "extraction_id": "extraction_9bc53d972ae8ac3a7cbb3807", "input_sha256": "4cdf2a8f80f1b49951952e6678a9b11b314171c597757670bd0111f20c3f3185", "span_start": 54205, "span_end": 54384, "original_text": "9 Silent-bypass ⋆ Skill declares aprimary scriptbut ex-\nploration traces contain zero Bash invoca-\ntions of it under majority-fail – a correct\nskill is quietly ignored at runtime.", "section": "Appendix A.2 Table 3, PDF page 15", "stance": "supports", "verification_status": "verified", "reason": "Primary PDF defines Auditor check 9 as silent-bypass at runtime"}]
atomicity_status: "atomic"
evidence_coverage: "full"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "primary"
evidence_entailment: "full"
claim_confidence: "high"
publication_gate: "needs_review"
split_from: "claim_wechat_skillevolver_meta_audit_loop_20260716"
split_reason: "将 Auditor 行为检查与策略探索设置分开核验"
memory_tier: "trusted"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 6
last_consolidated_at: "2026-07-17T22:40:01+08:00"
last_verified_at: null
trust_score: 100
trust_reasons: ["valid consolidation receipt matches current object", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists", "drift audit has no high risk"]
promotion_history: [{"promotion_id": "promotion_e6136711acf3cde5498ae262", "object_id": "claim_wechat_skillevolver_silent_bypass_audit_20260716", "from_status": "working", "to_status": "trusted", "policy_version": "trusted-promotion-v1", "promotion_mode": "automatic", "reasons": ["completed consolidation review", "atomic claim", "full evidence coverage", "full evidence entailment", "good extraction", "primary or official authority", "explicit applicability", "supporting evidence exists"], "failed_conditions": [], "supporting_sources": ["source_d01f40e4896de2e186cbbe8a", "source_ca1f80f2bf2e7d410ab2459e"], "contradictions": [], "promoted_at": "2026-07-17T12:02:58+08:00", "promoted_by": "promotion-policy"}]
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-16.split-2"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-16.split-2-primary-f5cf0a8d70d8.md"
origin_candidate_sha256: "f5cf0a8d70d8c7d7fa874cde4b7814c986300c8724003f88534530ec54e49d6c"
memory_schema_version: 2
legacy_status: "trusted"
epistemic_status: "supported"
last_consolidation_id: "consolidation_86b11868864abff7263e40f5"
needs_policy_requalification: false
trust_policy_version: "trusted-promotion-v3-receipt-v2"
last_policy_qualified_at: "2026-07-17T18:38:24+08:00"
last_valid_receipt_id: null
policy_requalification_failed_conditions: []
---

该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本。
