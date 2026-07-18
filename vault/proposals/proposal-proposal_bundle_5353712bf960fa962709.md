---
id: "proposal_bundle_5353712bf960fa962709"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-18T16:30:48+08:00"
updated_at: "2026-07-18T16:30:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e2614742b0c3ee7cf985d616"]
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
extraction_id: "extraction_9b4583595ba685f207389410"
input_sha256: "1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_b93f2824932425f11bf3d80c", "target_path": "vault/knowledge/claims/claim_b93f2824932425f11bf3d80c-2026-7-17-gigaworld-policy-0-5-a-faster.md", "base_sha256": null, "candidate_sha256": "cf755db9f364de74ecd823553a90a9eb9a07a3929014d2a5d84195bfaa3277a3", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_5353712bf960fa962709-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_b93f2824932425f11bf3d80c.md", "working_at": "2026-07-18T16:30:48+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_ece3b21b134d0b944b46b8fd", "target_path": "vault/knowledge/claims/claim_ece3b21b134d0b944b46b8fd-stronger-wam-empowered-by-autoresearch-gigaai-tsinghua-universit.md", "base_sha256": null, "candidate_sha256": "87ce0df6556b7010070a09ce8ba1dfaa8ea483d29b49efd18e34f13868b102b7", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_5353712bf960fa962709-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_ece3b21b134d0b944b46b8fd.md", "working_at": "2026-07-18T16:30:48+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…We observe that the agents incentivized to\ncommunicate via the social inﬂuence reward learn [faster], and\nachieve signiﬁcantly…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_e2614742b0c3ee7cf985d616"}
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
- Extraction：`extraction_9b4583595ba685f207389410`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_b93f2824932425f11bf3d80c-2026-7-17-gigaworld-policy-0-5-a-faster.md
@@ -0,0 +1,32 @@
+---
+id: "claim_b93f2824932425f11bf3d80c"
+type: "claim"
+status: "proposal"
+title: "2026-7-17 GigaWorld-Policy-0.5: A Faster"
+created_at: "2026-07-18T16:30:48+08:00"
+updated_at: "2026-07-18T16:30:48+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_e2614742b0c3ee7cf985d616"]
+relations: [{"type": "derived_from", "target_id": "source_e2614742b0c3ee7cf985d616", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e2614742b0c3ee7cf985d616"
+evidence: [{"evidence_id": "evidence_b7cc8665e26c3e85add3", "evidence_kind": "paraphrase", "source_id": "source_e2614742b0c3ee7cf985d616", "content_id": "content_1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990", "extraction_id": "extraction_9b4583595ba685f207389410", "span_start": -1, "span_end": 39, "original_text": "2026-7-17 GigaWorld-Policy-0.5: A Faster", "interpretation": "2026-7-17 GigaWorld-Policy-0.5: A Faster", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "2026-7-17\nGigaWorld-Policy-0.5: A Faster and Stronger WAM\nEmpowered by AutoResearch\nGigaAI\nTsinghua University\nProject Page: https://open-gigaai.github.io/giga-world-policy/\nAlphabetical Order:Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni, Fangzheng Ye, Guan Huang, Guo Li, Guosheng Zhao,\nHaodong Yan, Hengtao Li, Jiwen Lu, Kai Wang, Mingming Yu, Qitang Hu, Qiuping Deng, Songling Liu, Xiaoyu Tian, Xiaofeng Wang,\nXinyu Zhou, Xiuwei Xu, Xinze Chen, Yang Wang, Yejun Zeng, Yifan Chang, Yun Ye, Zhenyu "
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 2026-7-17 GigaWorld-Policy-0.5: A Faster
+
+2026-7-17 GigaWorld-Policy-0.5: A Faster
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_ece3b21b134d0b944b46b8fd-stronger-wam-empowered-by-autoresearch-gigaai-tsinghua-universit.md
@@ -0,0 +1,32 @@
+---
+id: "claim_ece3b21b134d0b944b46b8fd"
+type: "claim"
+status: "proposal"
+title: "Stronger WAM Empowered by AutoResearch GigaAI Tsinghua University Project Page: https://open-gigaai.github.io/giga-world-policy/ Alphabetical Order:Angen Ye, An"
+created_at: "2026-07-18T16:30:48+08:00"
+updated_at: "2026-07-18T16:30:48+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_e2614742b0c3ee7cf985d616"]
+relations: [{"type": "derived_from", "target_id": "source_e2614742b0c3ee7cf985d616", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e2614742b0c3ee7cf985d616"
+evidence: [{"evidence_id": "evidence_31499c0ec37b786bd09d", "evidence_kind": "paraphrase", "source_id": "source_e2614742b0c3ee7cf985d616", "content_id": "content_1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990", "extraction_id": "extraction_9b4583595ba685f207389410", "span_start": -1, "span_end": 453, "original_text": "Stronger WAM Empowered by AutoResearch GigaAI Tsinghua University Project Page: https://open-gigaai.github.io/giga-world-policy/ Alphabetical Order:Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni, Fangzheng Ye, Guan Huang, Guo Li, Guosheng Zhao, Haodong Yan, Hengtao Li, Jiwen Lu, Kai Wang, Mingming Yu, Qitang Hu, Qiuping Deng, Songling Liu, Xiaoyu Tian, Xiaofeng Wang, Xinyu Zhou, Xiuwei Xu, Xinze Chen, Yang Wang, Yejun Zeng, Yifan Chang, Yun Ye, Zhenyu", "interpretation": "Stronger WAM Empowered by AutoResearch GigaAI Tsinghua University Project Page: https://open-gigaai.github.io/giga-world-policy/ Alphabetical Order:Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni, Fangzheng Ye, Guan Huang, Guo Li, Guosheng Zhao, Haodong Yan, Hengtao Li, Jiwen Lu, Kai Wang, Mingming Yu, Qitang Hu, Qiuping Deng, Songling Liu, Xiaoyu Tian, Xiaofeng Wang, Xinyu Zhou, Xiuwei Xu, Xinze Chen, Yang Wang, Yejun Zeng, Yifan Chang, Yun Ye, Zhenyu", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "1745ce117de5b359f955d1da910a830661d5d80a2781c7dd50cf67fb3fe43990", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "2026-7-17\nGigaWorld-Policy-0.5: A Faster and Stronger WAM\nEmpowered by AutoResearch\nGigaAI\nTsinghua University\nProject Page: https://open-gigaai.github.io/giga-world-policy/\nAlphabetical Order:Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni, Fangzheng Ye, Guan Huang, Guo Li, Guosheng Zhao,\nHaodong Yan, Hengtao Li, Jiwen Lu, Kai Wang, Mingming Yu, Qitang Hu, Qiuping Deng, Songling Liu, Xiaoyu Tian, Xiaofeng Wang,\nXinyu Zhou, Xiuwei Xu, Xinze Chen, Yang Wang, Yejun Zeng, Yifan Chang, Yun Ye, Zhenyu "
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Stronger WAM Empowered by AutoResearch GigaAI Tsinghua University Project Page: https://open-gigaai.github.io/giga-world-policy/ Alphabetical Order:Angen Ye, An
+
+Stronger WAM Empowered by AutoResearch GigaAI Tsinghua University Project Page: https://open-gigaai.github.io/giga-world-policy/ Alphabetical Order:Angen Ye, Angyuan Ma, Boyuan Wang, Chaojun Ni, Fangzheng Ye, Guan Huang, Guo Li, Guosheng Zhao, Haodong Yan, Hengtao Li, Jiwen Lu, Kai Wang, Mingming Yu, Qitang Hu, Qiuping Deng, Songling Liu, Xiaoyu Tian, Xiaofeng Wang, Xinyu Zhou, Xiuwei Xu, Xinze Chen, Yang Wang, Yejun Zeng, Yifan Chang, Yun Ye, Zhenyu
```
