---
id: "proposal_53bcd8117e16272c52d22212"
type: "proposal"
status: "pending"
title: "模型提议：该文报告 G0.5 零样本 DROID Franka 成功率 82.5%，PP Bench 指令跟随 65.6%→84.4%（50h 后训练）；BEHAVIOR-1K 1 epoch 29.0% 超 π0.5 四 epoch 26.3%"
created_at: "2026-07-16T11:07:21+08:00"
updated_at: "2026-07-16T11:07:21+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e6608d8f849ad472bbd95143"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_g05_reported_benchmarks_20260716"
target_path: "vault/knowledge/claims/claim_wechat_g05_reported_benchmarks_20260716-该文报告-g0-5-零样本-droid-franka-成功率-82-5-pp-bench-指令跟随-65-6-84-4-50h-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_53bcd8117e16272c52d22212.md"
candidate_sha256: "b71b6e286556e4222a1913df54ef9ca4e3b88bb8db328323a2ee58ef985f31f5"
change_reason: "导入 claim_wechat_g05_reported_benchmarks_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_e6608d8f849ad472bbd95143", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "uncertainty": "自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文报告 G0.5 零样本 DROID Franka 成功率 82.5%，PP Bench 指令跟随 65.6%→84.4%（50h 后训练）；BEHAVIOR-1K 1 epoch 29.0% 超 π0.5 四 epoch 26.3%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_e6608d8f849ad472bbd95143`
- Input SHA-256：`4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228`
- 不确定性：自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。
- 提议理由：导入 claim_wechat_g05_reported_benchmarks_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_g05_reported_benchmarks_20260716-该文报告-g0-5-零样本-droid-franka-成功率-82-5-pp-bench-指令跟随-65-6-84-4-50h-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_g05_reported_benchmarks_20260716"
+title: "该文报告 G0.5 零样本 DROID Franka 成功率 82.5%，PP Bench 指令跟随 65.6%→84.4%（50h 后训练）；BEHAVIOR-1K 1 epoch 29.0% 超 π0.5 四 epoch 26.3%"
+tags: ["benchmark", "Galaxea-G0.5", "zero-shot"]
+domains: ["robotics", "evaluation"]
+confidence: "low"
+applicability: ["vs π0.5/GR00T 对比叙述", "prompt 副词微调行为 +15%/+10%"]
+uncertainty: "全部为自媒体转述 G0.5 报告数字；非独立复现，宜标 contested/low 待回原文。"
+evidence: [{"evidence_id": "ev_4463", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 4463, "span_end": 4501, "original_text": "82.5% 的成功率，全面压制了针对该数据集专门训练的 π0.5-DROID", "section": "DROID 零样本", "stance": "supports", "verification_status": "verified", "reason": "文内对 DROID Franka 零样本成功率叙述。"}, {"evidence_id": "ev_4997", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 4997, "span_end": 5134, "original_text": "BEHAVIOR-1K)原生COT的检验：在 BEHAVIOR-1K 这个包含 50 个复杂长程家务、平均单次演示长达 6.6 分钟的挑战赛中，G0.5 仅仅使用 1 个 Epoch 的后训练，就超越了使用 4 个 Epoch 训练的 π0.5（29.0% vs 26.3%", "section": "长程家务", "stance": "supports", "verification_status": "verified", "reason": "文内对 BEHAVIOR-1K epoch 对比数据。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:08:00+08:00"
+updated_at: "2026-07-16T11:08:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 G0.5 vs PI flow matching 解读；等待人工核验"
+source_ids: ["source_e6608d8f849ad472bbd95143"]
+relations: [{"type": "derived_from", "target_id": "source_e6608d8f849ad472bbd95143", "reason": "具身纪元 Marilyn Liu 解读 Galaxea G0.5 技术报告 vs PI flow matching；非官方 primary source"}]
+---
+
+# 报告数字
+
+LIBERO 98.9% 等仿真数文内亦有；本文仅引 DROID 与 BEHAVIOR 作代表。
```
