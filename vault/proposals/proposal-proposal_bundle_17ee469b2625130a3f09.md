---
id: "proposal_bundle_17ee469b2625130a3f09"
type: "proposal"
status: "migrated"
title: "Compile bundle：[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents"
created_at: "2026-07-17T12:11:35+08:00"
updated_at: "2026-07-17T12:11:35+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b30214d3f75e366c385725a9"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_f72457bb201b78a69f3fde95"
input_sha256: "8fd4d6f822e18c22bb0572a9627b7c330e2e13a17ed8875c501a4190619021cb"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_e5379e4b954671b9e870a05b", "target_path": "vault/knowledge/claims/claim_e5379e4b954671b9e870a05b-来源原文-2605-10332-embodiskill-skill-aware-reflection-for-self-evol.md", "base_sha256": null, "candidate_sha256": "0f727fd112788797b3db757d092a5b15584ad4f8e5ba9ab29102d19e9aeddb97", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_17ee469b2625130a3f09-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_e5379e4b954671b9e870a05b.md", "working_at": "2026-07-17T12:11:35+08:00"}]
existing_context: [{"id": "work_arxiv_2605_10332", "type": "work", "title": "[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents", "path": "vault/memory/work/work_arxiv_2605_10332.md", "status": "working", "source_ids": ["source_b30214d3f75e366c385725a9", "source_30d6af4423a7ecb5e51c4a08"], "snippet": "…Skill-Aware Reflection for Self-Evolving [Embodied] Agents\n\n## Logical work identity\n\n- arXiv：`2605.10332`\n- Version：`unknown`\n- Captures：`source…", "match_reason": "metadata:title"}, {"id": "claim_wechat_embodied_data_structure_not_volume_20260716", "type": "claim", "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe", "path": "vault/memory/claim/claim_wechat_embodied_data_structure_not_volume_20260716.md", "status": "working", "source_ids": ["source_0a113baae7ce4d1ab78da1a3"], "snippet": "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。", "match_reason": "metadata:tags"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:tags"}, {"id": "claim_wechat_kairos_sim2real_training_20260716", "type": "claim", "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期", "path": "vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md", "status": "working", "source_ids": ["source_a20c5fb22d91216503d413e1"], "snippet": "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b30214d3f75e366c385725a9"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_f72457bb201b78a69f3fde95`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_e5379e4b954671b9e870a05b-来源原文-2605-10332-embodiskill-skill-aware-reflection-for-self-evol.md
@@ -0,0 +1,32 @@
+---
+id: "claim_e5379e4b954671b9e870a05b"
+type: "claim"
+status: "proposal"
+title: "来源原文：[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agen"
+created_at: "2026-07-17T12:11:35+08:00"
+updated_at: "2026-07-17T12:11:35+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b30214d3f75e366c385725a9"]
+relations: [{"type": "derived_from", "target_id": "source_b30214d3f75e366c385725a9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b30214d3f75e366c385725a9"
+evidence: [{"evidence_id": "evidence_b658f03f9ccda3abafe5", "evidence_kind": "quote", "source_id": "source_b30214d3f75e366c385725a9", "content_id": "content_8fd4d6f822e18c22bb0572a9627b7c330e2e13a17ed8875c501a4190619021cb", "extraction_id": "extraction_f72457bb201b78a69f3fde95", "span_start": 0, "span_end": 82, "original_text": "[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "8fd4d6f822e18c22bb0572a9627b7c330e2e13a17ed8875c501a4190619021cb", "extractor": "html-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
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
+# 来源原文：[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agen
+
+[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents
```
