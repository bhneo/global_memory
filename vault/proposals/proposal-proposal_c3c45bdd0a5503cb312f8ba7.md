---
id: "proposal_c3c45bdd0a5503cb312f8ba7"
type: "proposal"
status: "pending"
title: "模型提议：该文模拟 10 万人 200 轮硬币博弈：100% 全押几乎全灭，37.5% 凯利下注多数人稳健增值"
created_at: "2026-07-16T00:35:53+08:00"
updated_at: "2026-07-16T00:35:53+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_kelly_simulation_survival_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kelly_simulation_survival_20260716-该文模拟-10-万人-200-轮硬币博弈-100-全押几乎全灭-37-5-凯利下注多数人稳健增值.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_c3c45bdd0a5503cb312f8ba7.md"
candidate_sha256: "70a49ad309b041bf3c59bc6184c7ed9dd6d3acff359d1f13952e36a217052ef0"
change_reason: "导入 claim_wechat_kelly_simulation_survival_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9d39636775b188c87d6a001f", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "uncertainty": "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文模拟 10 万人 200 轮硬币博弈：100% 全押几乎全灭，37.5% 凯利下注多数人稳健增值

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9d39636775b188c87d6a001f`
- Input SHA-256：`0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33`
- 不确定性：概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。
- 提议理由：导入 claim_wechat_kelly_simulation_survival_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kelly_simulation_survival_20260716-该文模拟-10-万人-200-轮硬币博弈-100-全押几乎全灭-37-5-凯利下注多数人稳健增值.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kelly_simulation_survival_20260716"
+title: "该文模拟 10 万人 200 轮硬币博弈：100% 全押几乎全灭，37.5% 凯利下注多数人稳健增值"
+tags: ["simulation", "kelly-criterion", "bankruptcy"]
+domains: ["probability", "behavioral-economics"]
+confidence: "low"
+applicability: ["作者自研 10 万人×200 轮模拟叙述", "100%/65%/37.5%/10% 策略对比"]
+uncertainty: "模拟为文内自述未附代码/数据；幂律分布等结论需复现验证。"
+evidence: [{"evidence_id": "ev_2693", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 2693, "span_end": 2706, "original_text": "100%下注的玩家几乎全灭", "section": "全押结果", "stance": "supports", "verification_status": "verified", "reason": "文内对 100% 下注策略模拟结果的说明。"}, {"evidence_id": "ev_2908", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 2908, "span_end": 2968, "original_text": "37.5% 下注（凯利公式）：财富稳定增长\n\n凯利下注策略下，资产分布明显右移，多数人资产增长且分布集中，是最优财富积累", "section": "凯利模拟", "stance": "supports", "verification_status": "verified", "reason": "文内对 37.5% 策略分布特征的描述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:36:00+08:00"
+updated_at: "2026-07-16T00:36:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入非遍历性/凯利公式科普；等待人工核验"
+source_ids: ["source_9d39636775b188c87d6a001f"]
+relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由 DataCafe/雪鹅经中科院物理所转载的非遍历性与凯利公式科普归纳；Thorp 等原书未 capture"}]
+---
+
+# 下注策略模拟
+
+全押≈全灭；凯利兼顾生存与增值（文内模拟）。
```
