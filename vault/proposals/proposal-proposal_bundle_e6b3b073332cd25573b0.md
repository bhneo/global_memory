---
id: "proposal_bundle_e6b3b073332cd25573b0"
type: "proposal"
status: "migrated"
title: "Compile bundle：[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning"
created_at: "2026-07-17T12:11:49+08:00"
updated_at: "2026-07-17T12:11:50+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e9ed0a3745aea832b64d7fa7"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e0f10373120f14e21be1ce07"
input_sha256: "cf1e907e553fd236347479442a09db77431de1bffd38c87db6c09a38032c88eb"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_c9385096b06a12f170a42fa0", "target_path": "vault/knowledge/claims/claim_c9385096b06a12f170a42fa0-来源原文-1810-08647-social-influence-as-intrinsic-motivation-for-mul.md", "base_sha256": null, "candidate_sha256": "c81b0c519bdcac798107f26db228942da95d60b19e2fe04aef70a2c3d6d71af5", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_e6b3b073332cd25573b0-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_c9385096b06a12f170a42fa0.md", "working_at": "2026-07-17T12:11:50+08:00"}]
existing_context: [{"id": "work_arxiv_1810_08647", "type": "work", "title": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "path": "vault/memory/work/work_arxiv_1810_08647.md", "status": "working", "source_ids": ["source_e9ed0a3745aea832b64d7fa7", "source_c019c0a492cc659d7858134d"], "snippet": "# [1810.08647] Social Influence as Intrinsic Motivation for [Multi-Agent] Deep Reinforcement Learning\n\n## Logical work identity\n\n- arXiv：`1810…", "match_reason": "metadata:title"}, {"id": "work_arxiv_1811_05931", "type": "work", "title": "[1811.05931] Evolving intrinsic motivations for altruistic behavior", "path": "vault/memory/work/work_arxiv_1811_05931.md", "status": "working", "source_ids": ["source_08e53bb30d37610610477e01", "source_62389152cf0723e2f3a753c1"], "snippet": "# [1811.05931] Evolving intrinsic motivations for altruistic behavior\n\n## Logical work identity\n\n- arXiv：`1811.05931`\n- Version：`unknown`\n- Captures：`source_08e53bb30d37610610477e01`, `source_62389152cf0723e2f3a753c1`\n\n此对象聚合现实世界作品身份，不替代任何 s", "match_reason": "metadata:title"}, {"id": "claim_wechat_im_rl_framework_internal_rewards_20260716", "type": "claim", "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模", "path": "vault/memory/claim/claim_wechat_im_rl_framework_internal_rewards_20260716.md", "status": "working", "source_ids": ["source_91199da18f239c48bbcdd49f"], "snippet": "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e9ed0a3745aea832b64d7fa7"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_e0f10373120f14e21be1ce07`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_c9385096b06a12f170a42fa0-来源原文-1810-08647-social-influence-as-intrinsic-motivation-for-mul.md
@@ -0,0 +1,32 @@
+---
+id: "claim_c9385096b06a12f170a42fa0"
+type: "claim"
+status: "proposal"
+title: "来源原文：[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinf"
+created_at: "2026-07-17T12:11:49+08:00"
+updated_at: "2026-07-17T12:11:49+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_e9ed0a3745aea832b64d7fa7"]
+relations: [{"type": "derived_from", "target_id": "source_e9ed0a3745aea832b64d7fa7", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e9ed0a3745aea832b64d7fa7"
+evidence: [{"evidence_id": "evidence_2ec466339564a95216da", "evidence_kind": "quote", "source_id": "source_e9ed0a3745aea832b64d7fa7", "content_id": "content_cf1e907e553fd236347479442a09db77431de1bffd38c87db6c09a38032c88eb", "extraction_id": "extraction_e0f10373120f14e21be1ce07", "span_start": 0, "span_end": 97, "original_text": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "cf1e907e553fd236347479442a09db77431de1bffd38c87db6c09a38032c88eb", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: null
+split_reason: null
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 来源原文：[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinf
+
+[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning
```
