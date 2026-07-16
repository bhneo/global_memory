---
id: "proposal_618369856dc605b77d9881d6"
type: "proposal"
status: "superseded"
title: "模型提议：该文称过去两年数据采集经历真机遥操→UMI 手持夹爪→第一人称 Ego 视频三次迭代"
created_at: "2026-07-16T01:11:55+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_embodied_data_three_waves_20260716"
target_path: "vault/knowledge/claims/claim_wechat_embodied_data_three_waves_20260716-该文称过去两年数据采集经历真机遥操-umi-手持夹爪-第一人称-ego-视频三次迭代.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_618369856dc605b77d9881d6.md"
candidate_sha256: "537eb2aa5c3b80e2cef6bd601dc9d9550984b4e80a520687aebbfc0f5b1d5a29"
change_reason: "导入 claim_wechat_embodied_data_three_waves_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_cda5a1b9e036598aff53e5be", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "uncertainty": "行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称过去两年数据采集经历真机遥操→UMI 手持夹爪→第一人称 Ego 视频三次迭代

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_cda5a1b9e036598aff53e5be`
- Input SHA-256：`4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5`
- 不确定性：行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。
- 提议理由：导入 claim_wechat_embodied_data_three_waves_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodied_data_three_waves_20260716-该文称过去两年数据采集经历真机遥操-umi-手持夹爪-第一人称-ego-视频三次迭代.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodied_data_three_waves_20260716"
+title: "该文称过去两年数据采集经历真机遥操→UMI 手持夹爪→第一人称 Ego 视频三次迭代"
+tags: ["umi", "ego-centric", "teleoperation"]
+domains: ["robotics", "data-engineering"]
+confidence: "medium"
+applicability: ["具身数据采集范式演进科普", "UMI/Ego 优缺点对照"]
+uncertainty: "三次迭代划分为主观框架；各路线缺陷列举来自软文而非系统评测。"
+evidence: [{"evidence_id": "ev_414", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 414, "span_end": 457, "original_text": "真机遥操」到「手持夹爪UMI」，再到今年爆发的「第一人称人类视频Ego Centric", "section": "三次迭代", "stance": "supports", "verification_status": "verified", "reason": "文内对三种采集范式的时序划分。"}, {"evidence_id": "ev_467", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 467, "span_end": 504, "original_text": "解放对采集人的束缚」，虽然扩大了产能，降低采集成本，但也损失了精细控制数据", "section": "迭代权衡", "stance": "supports", "verification_status": "verified", "reason": "文内对产能扩大与精细控制损失的说明。"}]
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
+# 三次迭代
+
+遥操→UMI→Ego；成本↓但精细控制数据↓。
```
