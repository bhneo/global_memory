---
id: "proposal_9e9df6eef50964f9a0e92a78"
type: "proposal"
status: "superseded"
title: "模型提议：该文报告 EmbodiSkill 在 ALFWorld 上达 93.28% 成功率（冻结 Qwen3.5-27B executor + GPT-5.2 演化 skill），消融显示 skill-aware 归因由 78.36% 提至 93.28%"
created_at: "2026-07-16T11:16:48+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_d01f40e4896de2e186cbbe8a"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_embodiskill_alfworld_results_20260716"
target_path: "vault/knowledge/claims/claim_wechat_embodiskill_alfworld_results_20260716-该文报告-embodiskill-在-alfworld-上达-93-28-成功率-冻结-qwen3-5-27b-executor.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_9e9df6eef50964f9a0e92a78.md"
candidate_sha256: "57b2e788c131a0b90122f99031c93dcba367c4d5fa2070976773a8e3d2b1e288"
change_reason: "导入 claim_wechat_embodiskill_alfworld_results_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_d01f40e4896de2e186cbbe8a", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "uncertainty": "博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文报告 EmbodiSkill 在 ALFWorld 上达 93.28% 成功率（冻结 Qwen3.5-27B executor + GPT-5.2 演化 skill），消融显示 skill-aware 归因由 78.36% 提至 93.28%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_d01f40e4896de2e186cbbe8a`
- Input SHA-256：`f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0`
- 不确定性：博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。
- 提议理由：导入 claim_wechat_embodiskill_alfworld_results_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodiskill_alfworld_results_20260716-该文报告-embodiskill-在-alfworld-上达-93-28-成功率-冻结-qwen3-5-27b-executor.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodiskill_alfworld_results_20260716"
+title: "该文报告 EmbodiSkill 在 ALFWorld 上达 93.28% 成功率（冻结 Qwen3.5-27B executor + GPT-5.2 演化 skill），消融显示 skill-aware 归因由 78.36% 提至 93.28%"
+tags: ["ALFWorld", "benchmark", "ablation"]
+domains: ["agent-systems", "evaluation"]
+confidence: "medium"
+applicability: ["vs G-Memory 74.62%", "Puttwo 100% 叙述"]
+uncertainty: "数字来自博客转述 Ju et al. 2026；GPT-5.2 等命名需回原文核验。"
+evidence: [{"evidence_id": "ev_4125", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 4125, "span_end": 4182, "original_text": "93.28% success rate。这个数字超过直接用 GPT-5.2 当无技能 Agent 的 70.89%", "section": "ALFWorld 主结果", "stance": "supports", "verification_status": "verified", "reason": "文内对 EmbodiSkill 与 direct agent 成功率对比。"}, {"evidence_id": "ev_4845", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 4845, "span_end": 4908, "original_text": "Skill-unaware evolution: 78.36% EmbodiSkill:             93.28%", "section": "消融对比", "stance": "supports", "verification_status": "verified", "reason": "文内同 executor 消融：skill-unaware 78.36% vs EmbodiSkill 93.28%。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:16:00+08:00"
+updated_at: "2026-07-16T11:16:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 EmbodiSkill/SkillEvolver 综述；等待人工核验"
+source_ids: ["source_d01f40e4896de2e186cbbe8a"]
+relations: [{"type": "derived_from", "target_id": "source_d01f40e4896de2e186cbbe8a", "reason": "Gavin AI 记事本解读 EmbodiSkill (2605.10332) 与 SkillEvolver (2605.10500)；原论文未 capture"}]
+---
+
+# EmbodiSkill 实验
+
+EB-Habitat/Navigation 亦报告超 memory baseline 双位数百分点。
```
