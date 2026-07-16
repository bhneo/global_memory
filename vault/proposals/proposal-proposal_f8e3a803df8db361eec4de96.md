---
id: "proposal_f8e3a803df8db361eec4de96"
type: "proposal"
status: "pending"
title: "模型提议：该文称数据堂具身智能数据工厂超 8000 平方米、300 组双臂采集设备，计划年产 10 万小时数据"
created_at: "2026-07-16T01:11:55+08:00"
updated_at: "2026-07-16T01:11:55+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_datatang_factory_scale_20260716"
target_path: "vault/knowledge/claims/claim_wechat_datatang_factory_scale_20260716-该文称数据堂具身智能数据工厂超-8000-平方米-300-组双臂采集设备-计划年产-10-万小时数据.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f8e3a803df8db361eec4de96.md"
candidate_sha256: "c35cc63fff788ff30f8233137c94fdb4b089d8ed2de4e076dbaf3ec5391450a7"
change_reason: "导入 claim_wechat_datatang_factory_scale_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_cda5a1b9e036598aff53e5be", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "uncertainty": "行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称数据堂具身智能数据工厂超 8000 平方米、300 组双臂采集设备，计划年产 10 万小时数据

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_cda5a1b9e036598aff53e5be`
- Input SHA-256：`4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5`
- 不确定性：行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。
- 提议理由：导入 claim_wechat_datatang_factory_scale_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_datatang_factory_scale_20260716-该文称数据堂具身智能数据工厂超-8000-平方米-300-组双臂采集设备-计划年产-10-万小时数据.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_datatang_factory_scale_20260716"
+title: "该文称数据堂具身智能数据工厂超 8000 平方米、300 组双臂采集设备，计划年产 10 万小时数据"
+tags: ["datatang", "data-factory", "crowdsourcing"]
+domains: ["robotics", "data-engineering"]
+confidence: "low"
+applicability: ["数据堂场内工厂与 Ego 众包服务宣传", "2026 具身数据产业化叙述"]
+uncertainty: "为厂商软文数字；600 采集员、万小时交付等未独立验证。"
+evidence: [{"evidence_id": "ev_4348", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 4348, "span_end": 4467, "original_text": "8000平方米，搭建高度真实、可灵活配置的物理环境，模拟药店、超市、工厂、家居、厨房等真实复杂场景，涵盖零售、医疗、工业自动化等多个商业化领域。\n\n工厂装配了300组通用双臂灵巧手采集设备，600名经验丰富的采集员。计划今年产出10万小时", "section": "工厂规模", "stance": "supports", "verification_status": "verified", "reason": "文内对数据堂工厂面积与产出计划的说明。"}, {"evidence_id": "ev_4427", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 4427, "span_end": 4447, "original_text": "300组通用双臂灵巧手采集设备，600名", "section": "设备与人员", "stance": "supports", "verification_status": "verified", "reason": "文内对双臂设备与采集员规模的说明。"}]
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
+# 数据堂工厂
+
+8000㎡/300 组设备；10 万小时计划（宣传数字）。
```
