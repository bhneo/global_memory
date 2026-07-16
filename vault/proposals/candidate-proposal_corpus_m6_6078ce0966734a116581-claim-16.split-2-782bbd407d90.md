---
id: "claim_wechat_skillevolver_silent_bypass_audit_20260716"
type: "claim"
status: "proposal"
title: "该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本"
created_at: "2026-07-16T11:16:00+08:00"
updated_at: "2026-07-16T18:00:00+08:00"
aliases: []
tags: ["SkillEvolver", "auditor", "silent-bypass"]
domains: ["agent-systems", "software-engineering"]
confidence: "medium"
source_ids: ["source_d01f40e4896de2e186cbbe8a"]
relations: [{"type": "derived_from", "target_id": "source_d01f40e4896de2e186cbbe8a", "reason": "由 SkillEvolver 二手解读的 Auditor 段落拆分", "confidence": "low", "created_by": "m6.1-human-directed-split", "status": "proposal"}]
applicability: ["技能声明正确但可能未被下游 Agent 使用的审计"]
uncertainty: "Auditor 检查类别来自二手材料转述，需回 arXiv:2605.10500 核验。"
evidence: [{"evidence_id": "ev_7663", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 7663, "span_end": 7793, "original_text": "silent-bypass。这个非常实用：skill 声称有主脚本，但探索轨迹里多数失败运行根本没有 Bash 调用它。也就是说，skill 内容可能是对的，但下游 Agent 没有用。普通静态评审看不出来，只有把 skill 真部署给 fresh agent", "section": "silent-bypass 检查", "stance": "supports", "verification_status": "verified", "reason": "文内对第 9 类 Auditor 检查的描述。"}]
atomicity_status: "atomic"
evidence_coverage: "partial"
quote_verification: "exact"
extraction_quality: "good"
epistemic_source_authority: "secondary"
evidence_entailment: "partial"
claim_confidence: "medium"
publication_gate: "needs_review"
split_from: "claim_wechat_skillevolver_meta_audit_loop_20260716"
split_reason: "将 Auditor 行为检查与策略探索设置分开核验"
---

该文称 SkillEvolver 的 silent-bypass 审计检查下游 Agent 是否实际调用技能脚本。
