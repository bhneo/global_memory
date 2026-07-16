---
id: "proposal_0dcbb63797499d43dbbd9457"
type: "proposal"
status: "pending"
title: "模型提议：该文介绍 EmbodiSkill 将 skill 拆为 S_body 与 S_app：Discovery/Optimization/SkillDefect 可改正文，ExecutionLapse 仅更新附录强调执行遵守"
created_at: "2026-07-16T11:16:48+08:00"
updated_at: "2026-07-16T11:16:48+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_d01f40e4896de2e186cbbe8a"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_embodiskill_body_appendix_attribution_20260716"
target_path: "vault/knowledge/claims/claim_wechat_embodiskill_body_appendix_attribution_20260716-该文介绍-embodiskill-将-skill-拆为-s_body-与-s_app-discovery-optimizatio.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_0dcbb63797499d43dbbd9457.md"
candidate_sha256: "14f6e1dc53017a179d80dd3d5ebc0611266034d1ede8227ad812e8c5fe8dd351"
change_reason: "导入 claim_wechat_embodiskill_body_appendix_attribution_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_d01f40e4896de2e186cbbe8a", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "uncertainty": "博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文介绍 EmbodiSkill 将 skill 拆为 S_body 与 S_app：Discovery/Optimization/SkillDefect 可改正文，ExecutionLapse 仅更新附录强调执行遵守

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_d01f40e4896de2e186cbbe8a`
- Input SHA-256：`f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0`
- 不确定性：博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。
- 提议理由：导入 claim_wechat_embodiskill_body_appendix_attribution_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodiskill_body_appendix_attribution_20260716-该文介绍-embodiskill-将-skill-拆为-s_body-与-s_app-discovery-optimizatio.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodiskill_body_appendix_attribution_20260716"
+title: "该文介绍 EmbodiSkill 将 skill 拆为 S_body 与 S_app：Discovery/Optimization/SkillDefect 可改正文，ExecutionLapse 仅更新附录强调执行遵守"
+tags: ["skill-aware-reflection", "embodied-agents", "attribution"]
+domains: ["agent-systems", "robotics"]
+confidence: "medium"
+applicability: ["冻结 executor 仅演化外部 skill", "revision buffer 分区更新"]
+uncertainty: "算法细节来自论文转述；K=1 等超参需回 arXiv:2605.10332。"
+evidence: [{"evidence_id": "ev_1924", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 1924, "span_end": 1940, "original_text": "S_body(n), S_app", "section": "skill 二分", "stance": "supports", "verification_status": "verified", "reason": "文内对 skill 正文与附录的形式化拆分。"}, {"evidence_id": "ev_2203", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 2203, "span_end": 2728, "original_text": "ExecutionLapse\n\nEmbodiSkill 的核心技术点，是把每条轨迹反思成四类结构化记录。\n\n成功轨迹只能产生两类反思：\n\nc_i in {Discovery, Optimization}, r = 1\n\n失败轨迹只能产生两类反思：\n\nc_i in {SkillDefect, ExecutionLapse}, r = 0\n\n这四类不是命名游戏，而是决定后面能不能改 skill body。\n\nDiscovery 表示成功轨迹发现了当前 skill 没覆盖的新规则。例如某类容器操作里，先检查容器是否打开会显著减少无效动作。它可以往正文里新增内容。\n\nOptimization 表示已有规则是对的，但轨迹暴露出更好的执行方式。它必须指向某段已有 skill content，并给出更优改写。\n\nSkillDefect 表示已有规则错误、不完整或描述太弱。它也必须指向具体 target skill content，并提供轨迹证据和修正方案。\n\nExecutionLapse 最容易被忽视。它表示规则本身是对的，但执行器没有照做。比如 skill 已经写了“拿物体前先定位目标容器”，但 Agent 直接开始拿东西导致失败。这时不能改正文", "section": "执行偏差处理", "stance": "supports", "verification_status": "verified", "reason": "文内对 ExecutionLapse 不可改正文的规则。"}]
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
+# EmbodiSkill 归因
+
+Skill-Aware Evolution Spiral：执行→轨迹→归因→定向修订。
```
