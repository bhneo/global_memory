---
id: "proposal_264478dfd12ed55986311e6d"
type: "proposal"
status: "pending"
title: "模型提议：该文称 EmbodiSkill 与 SkillEvolver 代表技能自进化两条分叉：前者区分技能缺陷 vs 执行偏差归因，后者把技能写作变成可审计的 meta-skill 在线学习"
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
target_id: "claim_wechat_embodiskill_skillevolver_fork_20260716"
target_path: "vault/knowledge/claims/claim_wechat_embodiskill_skillevolver_fork_20260716-该文称-embodiskill-与-skillevolver-代表技能自进化两条分叉-前者区分技能缺陷-vs-执行偏差归因-后者.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_264478dfd12ed55986311e6d.md"
candidate_sha256: "cae1fdcaa28aeac4cf2bb721b66ad9f27b36c6c85de4956e4cc219b0a96bc477"
change_reason: "导入 claim_wechat_embodiskill_skillevolver_fork_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_d01f40e4896de2e186cbbe8a", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "uncertainty": "博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 EmbodiSkill 与 SkillEvolver 代表技能自进化两条分叉：前者区分技能缺陷 vs 执行偏差归因，后者把技能写作变成可审计的 meta-skill 在线学习

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_d01f40e4896de2e186cbbe8a`
- Input SHA-256：`f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0`
- 不确定性：博客转述 2605.10332/2605.10500；benchmark 数字需回 arXiv 原文核验。
- 提议理由：导入 claim_wechat_embodiskill_skillevolver_fork_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_embodiskill_skillevolver_fork_20260716-该文称-embodiskill-与-skillevolver-代表技能自进化两条分叉-前者区分技能缺陷-vs-执行偏差归因-后者.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_embodiskill_skillevolver_fork_20260716"
+title: "该文称 EmbodiSkill 与 SkillEvolver 代表技能自进化两条分叉：前者区分技能缺陷 vs 执行偏差归因，后者把技能写作变成可审计的 meta-skill 在线学习"
+tags: ["skill-evolution", "EmbodiSkill", "SkillEvolver"]
+domains: ["agent-systems", "robotics"]
+confidence: "medium"
+applicability: ["2026-05-11 同期 arXiv 论文对比", "外部 skill 资产 vs 权重更新"]
+uncertainty: "为博客综述；系统边界对比为作者归纳。"
+evidence: [{"evidence_id": "ev_58", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 58, "span_end": 2217, "original_text": "EmbodiSkill 解决“失败到底是技能错了，还是执行时没照做”；SkillEvolver 解决“一个技能能不能在真实部署后，靠另一个元技能从失败里继续学”。前者把具身轨迹变成有归因的技能修订，后者把技能写作本身变成可审计、可迭代的在线学习流程。\n\nAgent 技能这件事，过去很容易被写成一个轻飘飘的词：skill。\n\n但如果认真拆开，它其实不是一个东西，而是一组不同层级的外部能力资产。可以是一段系统提示词，可以是一份 SKILL.md 操作手册，可以是一组 helper scripts，也可以是一套具身任务里的 procedural rules。模型权重不变，但 Agent 读到这些技能之后，行为会变。\n\n所以最近“Agent 自进化”里最值得看的问题，不是模型会不会自己变聪明，而是：\n\nAgent 能不能把一次次真实执行里的失败，变成下一次可复用、可部署、可审计的技能资产？\n\n这两篇新论文刚好从两个方向回答了这个问题。\n\nEmbodiSkill 面向 embodied agents。它关心的是厨房、房间、导航、抓取、找物体这类环境里，Agent 执行失败到底该怎么归因。失败可能是技能规则真的错了，也可能是规则本来对，但执行器没有遵守。如果不分清这两类原因，系统就会把本来有效的规则改坏。\n\nSkillEvolver 面向 CLI-agent 和通用任务技能。它关心的是技能生成能不能从 one-shot 写作，升级为在线学习。一个 meta-skill 先写出领域技能，再把这个技能交给新的下游 Agent 去用；如果下游 Agent 用失败了，meta-skill 再从这些失败里修技能。\n\n一句话概括：\n\nEmbodiSkill 解决的是“技能更新时的归因问题”；SkillEvolver 解决的是“技能写作本身如何变成一个可迭代学习过程”。\n\n先把“技能自进化”说清楚\n\n在这类论文里，skill 不是模型权重里的隐性能力，而是模型外部的一份可读、可改、可部署的程序性知识。它通常会告诉 Agent：遇到某类任务时先观察什么，怎么分解目标，什么时候调用工具，如何处理边界条件，哪些失败模式要避免。\n\n这和普通 prompt engineering 的差别在于，skill 不应该是人一次性写完的静态说明书。真正有价值的 skill 应该能从运行轨迹里更新。\n\n可以把一般形式写成：\n\nskill_{t+1} = Update(skill_t, trajectory_t, feedback_t, verifier_t)\n\n问题在于，这个 Update 很难。\n\n如果更新太粗，系统会把一条失败轨迹总结成“以后要更小心”这种废话；如果更新太猛，它会把整份 skill 重写一遍，导致有效规则被覆盖；如果更新太具体，它会把训练样本里的文件名、字段名、阈值、答案写进技能，到了验证集就泄漏或过拟合。\n\nEmbodiSkill 和 SkillEvolver 的共同点，是都不再满足于“从轨迹生成一段反思”。它们都把技能更新做成了一个结构化过程：哪些证据能改正文，哪些证据只能提醒执行，哪些补丁要被独立审计，哪些失败说明技能根本没被调用。\n\n这也是这两篇论文值得放在一起看的原因。\n\nEmbodiSkill：具身任务里，失败不一定说明技能错了\n\nEmbodiSkill 的出发点很具体：在 embodied environment 里，失败原因比数字环境复杂得多。\n\n一个 Agent 被要求“把桌上的杯子放进抽屉”。它可能失败，是因为 skill 没写清楚要先打开抽屉；也可能是 skill 已经写了，但 Agent 在执行时没遵守；还可能是视觉观察里没看到杯子、路径规划绕错、动作前置条件没满足，或者容器状态没有正确跟踪。\n\n如果系统只看到最终 reward = 0，然后直接让 LLM 总结“技能哪里要改”，就会出现一个危险情况：\n\n本来正确的技能，被一次执行 lapse 当成技能缺陷改掉。\n\nEmbodiSkill 的 Figure 1 就是这个动机。静态 skill 可能不完整；普通 skill evolution 会从失败轨迹粗暴改整份技能；而 EmbodiSkill 要做的是 skill-aware reflection：先判断轨迹证据到底指向哪类更新，再决定是改技能正文，还是只更新 appendix 来提醒执行器遵守已有规则。\n\n论文把一个 skill 表示成两部分：\n\nS(n) = (S_body(n), S_app(n))\n\nS_body 是技能正文，包含真正的任务执行规则；S_app 是技能附录，只负责强调正文里已经存在、但执行器容易漏掉的有效规则。这个拆分很关键，因为 EmbodiSkill 不允许 execution lapse 直接改正文。\n\n执行器本身是冻结的：\n\na_t ~ pi_theta(. | I, S(n), h_t)\n\n其中 I 是任务指令，h_t 是当前轨迹历史，theta 不更新。性能提升只能来自外部 skill 的演化。\n\n四类反思：Discovery、Optimization、SkillDefect、ExecutionLapse", "section": "EmbodiSkill 定位", "stance": "supports", "verification_status": "verified", "reason": "文内摘要中对 EmbodiSkill 问题定义。"}, {"evidence_id": "ev_93", "evidence_kind": "quote", "source_id": "source_d01f40e4896de2e186cbbe8a", "content_id": "content_f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "extraction_id": "extraction_86edc5111c5d99c3f9f2bf7c", "input_sha256": "f12b772ae8623dddca24343cc8b500e4ab99ff37a61e232605764cf6d0dbf3b0", "span_start": 93, "span_end": 696, "original_text": "SkillEvolver 解决“一个技能能不能在真实部署后，靠另一个元技能从失败里继续学”。前者把具身轨迹变成有归因的技能修订，后者把技能写作本身变成可审计、可迭代的在线学习流程。\n\nAgent 技能这件事，过去很容易被写成一个轻飘飘的词：skill。\n\n但如果认真拆开，它其实不是一个东西，而是一组不同层级的外部能力资产。可以是一段系统提示词，可以是一份 SKILL.md 操作手册，可以是一组 helper scripts，也可以是一套具身任务里的 procedural rules。模型权重不变，但 Agent 读到这些技能之后，行为会变。\n\n所以最近“Agent 自进化”里最值得看的问题，不是模型会不会自己变聪明，而是：\n\nAgent 能不能把一次次真实执行里的失败，变成下一次可复用、可部署、可审计的技能资产？\n\n这两篇新论文刚好从两个方向回答了这个问题。\n\nEmbodiSkill 面向 embodied agents。它关心的是厨房、房间、导航、抓取、找物体这类环境里，Agent 执行失败到底该怎么归因。失败可能是技能规则真的错了，也可能是规则本来对，但执行器没有遵守。如果不分清这两类原因，系统就会把本来有效的规则改坏。\n\nSkillEvolver 面向 CLI-agent 和通用任务技能。它关心的是技能生成能不能从 one-shot 写作，升级为在线学习。一个 meta-skill", "section": "SkillEvolver 定位", "stance": "supports", "verification_status": "verified", "reason": "文内摘要中对 SkillEvolver 问题定义。"}]
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
+# 两条分叉
+
+skill 是外部可读可改程序性知识；Update 需结构化非自由反思。
```
