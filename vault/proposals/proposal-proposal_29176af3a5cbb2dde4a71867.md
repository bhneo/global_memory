---
id: "proposal_29176af3a5cbb2dde4a71867"
type: "proposal"
status: "superseded"
title: "模型提议：该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线"
created_at: "2026-07-16T01:11:54+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_embodied_data_quality_cost_tradeoff_20260716"
target_path: "vault/knowledge/claims/claim_wechat_embodied_data_quality_cost_tradeoff_20260716-该文称具身数据采集存在质量与成本难以兼得的矛盾-并以特斯拉重资产遥操对比-openai-低成本众包路线.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_29176af3a5cbb2dde4a71867.md"
candidate_sha256: "02be59f7ae5a6c03bc22b8eccd80592df880e4dfdfae28b67936d84c7185896d"
change_reason: "导入 claim_wechat_embodied_data_quality_cost_tradeoff_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_cda5a1b9e036598aff53e5be", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "uncertainty": "行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_cda5a1b9e036598aff53e5be`
- Input SHA-256：`4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5`
- 不确定性：行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。
- 提议理由：导入 claim_wechat_embodied_data_quality_cost_tradeoff_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodied_data_quality_cost_tradeoff_20260716-该文称具身数据采集存在质量与成本难以兼得的矛盾-并以特斯拉重资产遥操对比-openai-低成本众包路线.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodied_data_quality_cost_tradeoff_20260716"
+title: "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线"
+tags: ["embodied-ai", "data-collection", "teleoperation"]
+domains: ["robotics", "machine-learning"]
+confidence: "low"
+applicability: ["2024 特斯拉 vs OpenAI 数据采集路线对比叙述", "Physical AI 数据瓶颈讨论"]
+uncertainty: "为行业评论/软文；两家公司实际策略细节未 capture 原文，「遇挫」等判断属编辑性表述。"
+evidence: [{"evidence_id": "ev_266", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 266, "span_end": 339, "original_text": "特斯拉选择重资产路线，利用动作捕捉服和虚拟现实头显，用昂贵的遥操作设备采集高精度数据；OpenAI则押注低成本机械臂，试图通过众包方式获取海量数据", "section": "两条路线", "stance": "supports", "verification_status": "verified", "reason": "文内对特斯拉与 OpenAI 采集路线对比。"}, {"evidence_id": "ev_21", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 21, "span_end": 31, "original_text": "质量和成本只能二选一", "section": "质量成本矛盾", "stance": "supports", "verification_status": "verified", "reason": "文内对质量与成本不可兼得的点题。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:11:00+08:00"
+updated_at: "2026-07-16T01:11:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入具身数据采集软文；等待人工核验"
+source_ids: ["source_cda5a1b9e036598aff53e5be"]
+relations: [{"type": "derived_from", "target_id": "source_cda5a1b9e036598aff53e5be", "reason": "由新智元对数据堂具身数据采集框架的软文归纳；特斯拉/OpenAI 路线为二手引述"}]
+---
+
+# 质量 vs 成本
+
+遥操高精度 vs 众包低成本；难以兼得（文内观点）。
```
