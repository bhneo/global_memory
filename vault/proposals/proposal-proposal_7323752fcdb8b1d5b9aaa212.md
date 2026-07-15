---
id: "proposal_7323752fcdb8b1d5b9aaa212"
type: "proposal"
status: "pending"
title: "模型提议：Robo-ValueRL 项目页称使用约 240 小时离线演示与 3000+ 在线 rollout，并报告 chip/block 离线预训练增益 +26% / +34%"
created_at: "2026-07-15T17:34:06+08:00"
updated_at: "2026-07-15T17:34:06+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_robo_valuerl_data_scale_20260715"
target_path: "vault/knowledge/claims/claim_robo_valuerl_data_scale_20260715-robo-valuerl-项目页称使用约-240-小时离线演示与-3000-在线-rollout-并报告-chip-block-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_7323752fcdb8b1d5b9aaa212.md"
candidate_sha256: "b19a75cec3f21689c209844b9fc8ad2a8cdbbabb562eade7042f4e568c55b033"
change_reason: "导入 claim_robo_valuerl_data_scale_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_7b278ba348f2a8bb94cce1fc", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "uncertainty": "项目页数字与协议未完整披露；非 peer-reviewed 正文。"}
reviewed_at: null
review_reason: null
---

# 模型提议：Robo-ValueRL 项目页称使用约 240 小时离线演示与 3000+ 在线 rollout，并报告 chip/block 离线预训练增益 +26% / +34%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_7b278ba348f2a8bb94cce1fc`
- Input SHA-256：`1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9`
- 不确定性：项目页数字与协议未完整披露；非 peer-reviewed 正文。
- 提议理由：导入 claim_robo_valuerl_data_scale_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_robo_valuerl_data_scale_20260715-robo-valuerl-项目页称使用约-240-小时离线演示与-3000-在线-rollout-并报告-chip-block-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_robo_valuerl_data_scale_20260715"
+title: "Robo-ValueRL 项目页称使用约 240 小时离线演示与 3000+ 在线 rollout，并报告 chip/block 离线预训练增益 +26% / +34%"
+tags: ["offline-to-online-rl", "data-scale"]
+domains: ["robot-learning"]
+confidence: "low"
+applicability: ["项目页 Results 区块", "240h offline demonstrations", "3000+ online rollout trajectories"]
+uncertainty: "+26%/+34% 的基线与计算方式在项目页未定义；240h/3000+ 为项目自述规模，未经第三方核验；arXiv 未 release。"
+evidence: [{"evidence_id": "ev_2942", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 2942, "span_end": 3122, "original_text": "Across 240 hours of offline demonstrations and over 3,000 online rollout trajectories, reliable value estimates support stronger offline scaling and more stable online improvement.", "section": "Results", "stance": "supports", "verification_status": "verified", "reason": "规模与价值估计作用的综合陈述。"}, {"evidence_id": "ev_3191", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 3191, "span_end": 3195, "original_text": "+26%", "section": "Results / chip offline gain", "stance": "supports", "verification_status": "verified", "reason": "项目页 chip 离线增益 headline。"}, {"evidence_id": "ev_3216", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 3216, "span_end": 3220, "original_text": "+34%", "section": "Results / block offline gain", "stance": "supports", "verification_status": "verified", "reason": "项目页 block 离线增益 headline。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T17:30:00+08:00"
+updated_at: "2026-07-15T17:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入项目页知识；等待人工核验"
+source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
+relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 Robo-ValueRL 官方项目页归纳；非独立 peer-reviewed 论文正文"}]
+---
+
+# 数据规模与离线增益
+
+项目页 headline 数字。
```
