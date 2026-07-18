---
id: "claim_wechat_embodied_data_structure_not_volume_20260716"
title: "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe"
tags: ["embodied-ai", "data-infrastructure", "training-recipe"]
domains: ["robotics", "machine-learning"]
confidence: "low"
applicability: ["Joe Harris 推文引述语境", "部署日志 vs 模型训练数据割裂讨论"]
uncertainty: "为作者观点文；「不缺数据」论断依赖 anecdote，非系统统计。"
evidence: [{"evidence_id": "ev_28", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 28, "span_end": 49, "original_text": "机器人不缺数据，缺的是把数据变成能力的结构", "section": "核心论点", "stance": "supports", "verification_status": "verified", "reason": "文内开篇对问题重定义的表述。"}, {"evidence_id": "ev_120", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 120, "span_end": 156, "original_text": "TB 级传感器日志躺在 S3 里，真正缺的是把这些数据变得可用的基础设施", "section": "Joe Harris", "stance": "supports", "verification_status": "verified", "reason": "文内引述 Joe Harris 对缺基础设施的判断。"}]
type: "claim"
status: "working"
created_at: "2026-07-16T01:19:00+08:00"
updated_at: "2026-07-18T16:03:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "M6 corpus distillation from claim_wechat_embodied_data_structure_not_volume_20260716"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析", "confidence": "low", "created_by": "m6-controlled-distillation-v1", "status": "working"}]
atomicity_status: "atomic"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "low"
publication_gate: "needs_review"
memory_tier: "working"
created_by: "m6-controlled-distillation-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "m6-controlled-distillation-v1"
consolidation_count: 4
last_consolidated_at: "2026-07-18T16:03:00+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_corpus_m6_6078ce0966734a116581"
origin_item_id: "claim-13"
origin_candidate_path: "vault/proposals/candidate-proposal_corpus_m6_6078ce0966734a116581-claim-13-rev-ca0155942939.md"
origin_candidate_sha256: "ca0155942939d34bf42ae69cbe5d1f8e24b18d1453ed56382b03004520c96c7c"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_cf0e7bc0e35bcc3ffbe7db79"
---

# 结构 vs 数量

缺的是把数据变成能力的结构，非单纯缺 TB 日志。
