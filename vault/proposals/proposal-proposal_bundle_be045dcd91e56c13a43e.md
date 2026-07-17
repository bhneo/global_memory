---
id: "proposal_bundle_be045dcd91e56c13a43e"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-17T12:17:01+08:00"
updated_at: "2026-07-17T12:17:01+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_30d6af4423a7ecb5e51c4a08"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a052ee853af7bae9742a71b3"
input_sha256: "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_e2f86d4a5a367ae1dc8a5e1f", "target_path": "vault/knowledge/claims/claim_e2f86d4a5a367ae1dc8a5e1f-2026-7-14-embodiskill-skill-aware-reflection-for-self-evolving-e.md", "base_sha256": null, "candidate_sha256": "e5f7d8dd72a4637eed63aae5d658d9d48fb04b9547d026798cc5e0f0b5c16d44", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_be045dcd91e56c13a43e-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_e2f86d4a5a367ae1dc8a5e1f.md", "working_at": "2026-07-17T12:17:01+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_0b690c465600b65a6f2a3652", "target_path": "vault/knowledge/claims/claim_0b690c465600b65a6f2a3652-technology-3-university-of-science.md", "base_sha256": null, "candidate_sha256": "44473bf5c11b23276196ccf469ef517e113af0958d976795ee3adc56bda1942a", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_be045dcd91e56c13a43e-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_0b690c465600b65a6f2a3652.md", "working_at": "2026-07-17T12:17:01+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_d9476033c30cbb2c7b1f3f51", "target_path": "vault/knowledge/claims/claim_d9476033c30cbb2c7b1f3f51-technology-of-china-4-microsoft-research-5-institute-for-ai-indu.md", "base_sha256": null, "candidate_sha256": "d6e5707b4c0569b0a09e0b3274c51ee78b147d27576069e8b9c8d4433f464cac", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_be045dcd91e56c13a43e-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_d9476033c30cbb2c7b1f3f51.md", "working_at": "2026-07-17T12:17:01+08:00"}]
existing_context: [{"id": "claim_e5379e4b954671b9e870a05b", "type": "claim", "title": "来源原文：[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agen", "path": "vault/memory/claim/claim_e5379e4b954671b9e870a05b.md", "status": "working", "source_ids": ["source_b30214d3f75e366c385725a9"], "snippet": "…Skill-Aware Reflection for [Self-Evolving] Embodied Agen\n\n[2605.10332] EmbodiSkill: Skill-Aware Reflection for [Self-Evolving] Embodied…", "match_reason": "metadata:title"}, {"id": "work_arxiv_2605_10332", "type": "work", "title": "[2605.10332] EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents", "path": "vault/memory/work/work_arxiv_2605_10332.md", "status": "working", "source_ids": ["source_b30214d3f75e366c385725a9", "source_30d6af4423a7ecb5e51c4a08"], "snippet": "…Skill-Aware Reflection for [Self-Evolving] Embodied Agents\n\n## Logical work identity\n\n- arXiv：`2605.10332`\n- Version：`unknown`\n- Captures：`source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 3, "source_id": "source_30d6af4423a7ecb5e51c4a08"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 3, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 3, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_a052ee853af7bae9742a71b3`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_e2f86d4a5a367ae1dc8a5e1f-2026-7-14-embodiskill-skill-aware-reflection-for-self-evolving-e.md
@@ -0,0 +1,32 @@
+---
+id: "claim_e2f86d4a5a367ae1dc8a5e1f"
+type: "claim"
+status: "proposal"
+title: "2026-7-14 EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents Ruofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Z"
+created_at: "2026-07-17T12:17:01+08:00"
+updated_at: "2026-07-17T12:17:01+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_30d6af4423a7ecb5e51c4a08"]
+relations: [{"type": "derived_from", "target_id": "source_30d6af4423a7ecb5e51c4a08", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_30d6af4423a7ecb5e51c4a08"
+evidence: [{"evidence_id": "evidence_072cd6e33ffa64542877", "evidence_kind": "paraphrase", "source_id": "source_30d6af4423a7ecb5e51c4a08", "content_id": "content_0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extraction_id": "extraction_a052ee853af7bae9742a71b3", "span_start": -1, "span_end": 306, "original_text": "2026-7-14 EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents Ruofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4 Hao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡ 1 Nanjing University 2 Huazhong University of Science", "interpretation": "2026-7-14 EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents Ruofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4 Hao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡ 1 Nanjing University 2 Huazhong University of Science", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "2026-7-14\nEmbodiSkill: Skill-Aware Reflection for\nSelf-Evolving Embodied Agents\nRuofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4\nHao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡\n1 Nanjing University 2 Huazhong University of Science and Technology 3 University of Science and Technology of China\n4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University\nEmbodied agents can benefit from skills that"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 2026-7-14 EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents Ruofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Z
+
+2026-7-14 EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents Ruofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4 Hao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡ 1 Nanjing University 2 Huazhong University of Science
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_0b690c465600b65a6f2a3652-technology-3-university-of-science.md
@@ -0,0 +1,32 @@
+---
+id: "claim_0b690c465600b65a6f2a3652"
+type: "claim"
+status: "proposal"
+title: "Technology 3 University of Science"
+created_at: "2026-07-17T12:17:01+08:00"
+updated_at: "2026-07-17T12:17:01+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_30d6af4423a7ecb5e51c4a08"]
+relations: [{"type": "derived_from", "target_id": "source_30d6af4423a7ecb5e51c4a08", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_30d6af4423a7ecb5e51c4a08"
+evidence: [{"evidence_id": "evidence_8bf6abb3b14efa201760", "evidence_kind": "quote", "source_id": "source_30d6af4423a7ecb5e51c4a08", "content_id": "content_0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extraction_id": "extraction_a052ee853af7bae9742a71b3", "span_start": 330, "span_end": 364, "original_text": "Technology 3 University of Science", "interpretation": null, "section": null, "page": 1, "stance": "context", "verification_status": "verified", "input_sha256": "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "2026-7-14\nEmbodiSkill: Skill-Aware Reflection for\nSelf-Evolving Embodied Agents\nRuofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4\nHao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡\n1 Nanjing University 2 Huazhong University of Science and Technology 3 University of Science and Technology of China\n4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University\nEmbodied agents can benefit from skills that"
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Technology 3 University of Science
+
+Technology 3 University of Science
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_d9476033c30cbb2c7b1f3f51-technology-of-china-4-microsoft-research-5-institute-for-ai-indu.md
@@ -0,0 +1,32 @@
+---
+id: "claim_d9476033c30cbb2c7b1f3f51"
+type: "claim"
+status: "proposal"
+title: "Technology of China 4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University Embodied agents can benefit from skills that"
+created_at: "2026-07-17T12:17:01+08:00"
+updated_at: "2026-07-17T12:17:01+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_30d6af4423a7ecb5e51c4a08"]
+relations: [{"type": "derived_from", "target_id": "source_30d6af4423a7ecb5e51c4a08", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_30d6af4423a7ecb5e51c4a08"
+evidence: [{"evidence_id": "evidence_af6ae68fe3fe22ebb53f", "evidence_kind": "paraphrase", "source_id": "source_30d6af4423a7ecb5e51c4a08", "content_id": "content_0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extraction_id": "extraction_a052ee853af7bae9742a71b3", "span_start": -1, "span_end": 148, "original_text": "Technology of China 4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University Embodied agents can benefit from skills that", "interpretation": "Technology of China 4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University Embodied agents can benefit from skills that", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "2026-7-14\nEmbodiSkill: Skill-Aware Reflection for\nSelf-Evolving Embodied Agents\nRuofei Ju1∗† Xinrui Wang2∗† Xin Ding3‡ Yifan Yang4 Hao Wu1 Shiqi Jiang4 Qianxi Zhang4\nHao Wen5 Xiangyu Li5 Weijun Wang5 Kun Li5 Yunxin Liu5 Haipeng Dai1 Wei Wang1 Ting Cao5‡\n1 Nanjing University 2 Huazhong University of Science and Technology 3 University of Science and Technology of China\n4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University\nEmbodied agents can benefit from skills that"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Technology of China 4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University Embodied agents can benefit from skills that
+
+Technology of China 4 Microsoft Research 5 Institute for AI Industry Research (AIR), Tsinghua University Embodied agents can benefit from skills that
```
