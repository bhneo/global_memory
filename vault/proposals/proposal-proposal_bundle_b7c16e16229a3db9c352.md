---
id: "proposal_bundle_b7c16e16229a3db9c352"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub"
created_at: "2026-07-17T12:11:51+08:00"
updated_at: "2026-07-17T12:11:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ff5ce793c0efda7112e73c86"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a733adf0e37c89d2568fc0fb"
input_sha256: "9d9f5f2ce44b4db45d0cc510847274d1396aebc1ac8cd6f37382d962d3cc2a33"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_a1bf006b4174d98d1d8108c5", "target_path": "vault/knowledge/claims/claim_a1bf006b4174d98d1d8108c5-来源原文-github---xbotics-embodied-ai-club-xbotics-embodied-guide-xb.md", "base_sha256": null, "candidate_sha256": "b40a1391dc5af94d40feceabb4b83cf1abb707064a4a676e3403d318668f032b", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_b7c16e16229a3db9c352-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_a1bf006b4174d98d1d8108c5.md", "working_at": "2026-07-17T12:11:51+08:00"}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ff5ce793c0efda7112e73c86"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_a733adf0e37c89d2568fc0fb`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_a1bf006b4174d98d1d8108c5-来源原文-github---xbotics-embodied-ai-club-xbotics-embodied-guide-xb.md
@@ -0,0 +1,32 @@
+---
+id: "claim_a1bf006b4174d98d1d8108c5"
+type: "claim"
+status: "proposal"
+title: "来源原文：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把"
+created_at: "2026-07-17T12:11:51+08:00"
+updated_at: "2026-07-17T12:11:51+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_ff5ce793c0efda7112e73c86"]
+relations: [{"type": "derived_from", "target_id": "source_ff5ce793c0efda7112e73c86", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_ff5ce793c0efda7112e73c86"
+evidence: [{"evidence_id": "evidence_454c0c2bef74a113937b", "evidence_kind": "quote", "source_id": "source_ff5ce793c0efda7112e73c86", "content_id": "content_9d9f5f2ce44b4db45d0cc510847274d1396aebc1ac8cd6f37382d962d3cc2a33", "extraction_id": "extraction_a733adf0e37c89d2568fc0fb", "span_start": 0, "span_end": 149, "original_text": "GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "9d9f5f2ce44b4db45d0cc510847274d1396aebc1ac8cd6f37382d962d3cc2a33", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
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
+# 来源原文：GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把
+
+GitHub - Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide: Xbotics 社区具身智能学习指南：我们把“具身综述→学习路线→仿真学习→开源实物→人物访谈→公司图谱”串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。 · GitHub
```
