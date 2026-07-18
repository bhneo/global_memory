---
id: "proposal_bundle_0928c1fad754f02feeab"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-18T16:30:44+08:00"
updated_at: "2026-07-18T16:30:45+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
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
extraction_id: "extraction_e98976f6b17c4f967f55c0f7"
input_sha256: "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_ce6495dab9cd14e0068546af", "target_path": "vault/knowledge/claims/claim_ce6495dab9cd14e0068546af-saferelbench-a-spatial-relation-aware-benchmark-for-process-leve.md", "base_sha256": null, "candidate_sha256": "c472ab605e75eba829681ceb63b5d81ae78fbfd5d8156cb5647c52c1af454a01", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_0928c1fad754f02feeab-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_ce6495dab9cd14e0068546af.md", "working_at": "2026-07-18T16:30:45+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_3d3342246519ef132c0d22f7", "target_path": "vault/knowledge/claims/claim_3d3342246519ef132c0d22f7-telecommunications-beijing-china-2state-key-laboratory-of-genera.md", "base_sha256": null, "candidate_sha256": "9a419abb59cf8e45c0003aed94c949ac8669565ca5dcafcbb18c6167393aed6a", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_0928c1fad754f02feeab-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_3d3342246519ef132c0d22f7.md", "working_at": "2026-07-18T16:30:45+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…In theHarvest MARL\n\n<!-- [page]: 4 -->\n\nSocial Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL\nsetting, it is…", "match_reason": "full-text:body"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "…个百分点；相对 EVOLVE-VLA，平均提高 2.0 个百分点。\n\n这些结果来自 LIBERO 仿真 [benchmark]，论文对自行运行的方法报告 5 个独立种子的 mean±std；它们不能直接外推为真实机器人成功率。", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_b470fe87f9d09df2b7d3b5fd"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 2, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 2, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_e98976f6b17c4f967f55c0f7`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_ce6495dab9cd14e0068546af-saferelbench-a-spatial-relation-aware-benchmark-for-process-leve.md
@@ -0,0 +1,32 @@
+---
+id: "claim_ce6495dab9cd14e0068546af"
+type: "claim"
+status: "proposal"
+title: "SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents Huaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang"
+created_at: "2026-07-18T16:30:44+08:00"
+updated_at: "2026-07-18T16:30:44+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
+relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
+evidence: [{"evidence_id": "evidence_057b86baec27230cada2", "evidence_kind": "paraphrase", "source_id": "source_b470fe87f9d09df2b7d3b5fd", "content_id": "content_f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11", "extraction_id": "extraction_e98976f6b17c4f967f55c0f7", "span_start": -1, "span_end": 212, "original_text": "SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents Huaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang Zhang 2, Zhaofeng He 1, 1Beijing University of Posts", "interpretation": "SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents Huaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang Zhang 2, Zhaofeng He 1, 1Beijing University of Posts", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level\nSafety in VLM-Driven Embodied Agents\nHuaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang Zhang 2, Zhaofeng He 1,\n1Beijing University of Posts and Telecommunications, Beijing, China\n2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China\nCorrespondence:daibo@bigai.ai, zhaofenghe@bupt.edu.cn\nAbstract\nVision-language models (VLMs) are increas-\ningly used as the reasoning backbone of em-\nbodied agents, en"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents Huaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang
+
+SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents Huaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang Zhang 2, Zhaofeng He 1, 1Beijing University of Posts
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_3d3342246519ef132c0d22f7-telecommunications-beijing-china-2state-key-laboratory-of-genera.md
@@ -0,0 +1,32 @@
+---
+id: "claim_3d3342246519ef132c0d22f7"
+type: "claim"
+status: "proposal"
+title: "Telecommunications, Beijing, China 2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China Correspondence:daibo@bigai.ai, zhaofenghe@bup"
+created_at: "2026-07-18T16:30:44+08:00"
+updated_at: "2026-07-18T16:30:44+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
+relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
+evidence: [{"evidence_id": "evidence_4c5b3e2f789ecfe17345", "evidence_kind": "paraphrase", "source_id": "source_b470fe87f9d09df2b7d3b5fd", "content_id": "content_f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11", "extraction_id": "extraction_e98976f6b17c4f967f55c0f7", "span_start": -1, "span_end": 281, "original_text": "Telecommunications, Beijing, China 2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China Correspondence:daibo@bigai.ai, zhaofenghe@bupt.edu.cn Abstract Vision-language models (VLMs) are increas- ingly used as the reasoning backbone of em- bodied agents, en", "interpretation": "Telecommunications, Beijing, China 2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China Correspondence:daibo@bigai.ai, zhaofenghe@bupt.edu.cn Abstract Vision-language models (VLMs) are increas- ingly used as the reasoning backbone of em- bodied agents, en", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "SAFERELBENCH: A Spatial-Relation-Aware Benchmark for Process-Level\nSafety in VLM-Driven Embodied Agents\nHuaigang Yang1,2, Ya Li1, Min Ren 1, Bo Dai 2, Zhenliang Zhang 2, Zhaofeng He 1,\n1Beijing University of Posts and Telecommunications, Beijing, China\n2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China\nCorrespondence:daibo@bigai.ai, zhaofenghe@bupt.edu.cn\nAbstract\nVision-language models (VLMs) are increas-\ningly used as the reasoning backbone of em-\nbodied agents, en"
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Telecommunications, Beijing, China 2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China Correspondence:daibo@bigai.ai, zhaofenghe@bup
+
+Telecommunications, Beijing, China 2State Key Laboratory of General Artificial Intelligence, BIGAI, Beijing, China Correspondence:daibo@bigai.ai, zhaofenghe@bupt.edu.cn Abstract Vision-language models (VLMs) are increas- ingly used as the reasoning backbone of em- bodied agents, en
```
