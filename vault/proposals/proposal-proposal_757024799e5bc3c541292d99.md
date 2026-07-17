---
id: "proposal_757024799e5bc3c541292d99"
type: "proposal"
status: "migrated"
title: "修订：模型提议：Play2Perfect 的 dexterous play 预训练使装配 RL 微调比从零训练（含稠密奖励）样本效率高约 33 倍"
created_at: "2026-07-15T14:28:08+08:00"
updated_at: "2026-07-17T11:58:54+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "supersedes", "target_id": "proposal_5096cc0d13f8c4171cb4ed51", "reason": "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"}]
proposal_kind: "knowledge_revision"
processor: "human-candidate-revision-v1"
action: "create"
target_id: "claim_play2perfect_sample_efficiency_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_sample_efficiency_20260715-play2perfect-的-dexterous-play-预训练使装配-rl-微调比从零训练-含稠密奖励-样本效率高约-33-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_757024799e5bc3c541292d99.md"
candidate_sha256: "d0e5fb70314443e119dd38ed6c3f9cd05006574f4f5d6b99fbef5d3f9047d764"
change_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
revision_of: "proposal_5096cc0d13f8c4171cb4ed51"
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# 修订：模型提议：Play2Perfect 的 dexterous play 预训练使装配 RL 微调比从零训练（含稠密奖励）样本效率高约 33 倍

## 修订说明

- 被替代 proposal：`proposal_5096cc0d13f8c4171cb4ed51`
- 修订理由：人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份
- 建议操作：`create` `vault/knowledge/claims/claim_play2perfect_sample_efficiency_20260715-play2perfect-的-dexterous-play-预训练使装配-rl-微调比从零训练-含稠密奖励-样本效率高约-33-.md`
- 原 candidate 保持不可变；本 proposal 使用新的 candidate。

## Base → Revised Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_sample_efficiency_20260715-play2perfect-的-dexterous-play-预训练使装配-rl-微调比从零训练-含稠密奖励-样本效率高约-33-.md
@@ -0,0 +1,26 @@
+---
+id: "claim_play2perfect_sample_efficiency_20260715"
+type: "claim"
+status: "proposal"
+title: "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: ["Play2Perfect 33x"]
+tags: ["dexterous-manipulation", "reinforcement-learning", "pretraining", "assembly"]
+domains: ["robotics", "robot-learning"]
+confidence: "medium"
+source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Play2Perfect：仿真 play 预训练 + 稀疏奖励装配微调", "Tight-Insertion (Fixtured) wall-clock 对比", "Scratch (dense reward) 含 10 waypoint shaping", "22-DoF Sharpa 手 + 7-DoF KUKA iiwa 14"]
+uncertainty: "33× 量化来自 Fixtured 任务 dense-scratch 对比；主任务 scratch 24h 无成功 rollout。不能外推为通用加速比。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "We show that our prior is 33x more sample-efficient than RL training from scratch, even when provided with dense, multi-stage rewards.", "stance": "supports", "reason": "摘要直接陈述样本效率倍数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "Scratch (dense reward) requires over 100 hours to reach near-perfect success, while Play2Perfect reaches the same success rate in only 4 hours, yielding a 33× speed-up.", "stance": "supports", "reason": "Fixtured 任务 wall-clock 对比。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 6 页 Section 4.1", "excerpt": "both scratch baselines produce no successful rollouts even after 24 hours", "stance": "context", "reason": "主任务 scratch 失败，限定对比范围。"}]
+---
+
+# Play2Perfect 在简化插入任务中的训练效率
+
+在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward scratch 需要超过 100 小时达到接近满成功率，而 Play2Perfect 使用 play 先验和 sparse assembly reward 约 4 小时达到相同水平；论文将其概括为 33× speed-up/sample-efficiency improvement。
+
+这个 33× 数字只对应上述简化任务的 wall-clock 对比。四项主要装配任务中，两种 scratch baseline 在 24 小时后都没有成功 rollout，因而没有形成可直接计算的通用倍数；不应把 33× 外推为所有装配任务或所有硬件的加速比。
```
