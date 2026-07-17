---
id: "proposal_1e4548999e2e2dbf0a44fc97"
type: "proposal"
status: "migrated"
title: "修订：模型提议：Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动"
created_at: "2026-07-15T14:28:00+08:00"
updated_at: "2026-07-17T11:58:33+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "supersedes", "target_id": "proposal_d844a95491ff017088f292cc", "reason": "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"}]
proposal_kind: "knowledge_revision"
processor: "human-candidate-revision-v1"
action: "create"
target_id: "claim_play2perfect_inhand_pretraining_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_inhand_pretraining_20260715-play2perfect-表明-play-预训练向装配迁移的关键是迫使手指-in-hand-操控而非固定抓握下的手臂运动.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1e4548999e2e2dbf0a44fc97.md"
candidate_sha256: "8d7e38b40e6c1a2b8c505674501d2a1059faf00bcb027743a097b5e09302dd0b"
change_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
revision_of: "proposal_d844a95491ff017088f292cc"
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# 修订：模型提议：Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动

## 修订说明

- 被替代 proposal：`proposal_d844a95491ff017088f292cc`
- 修订理由：人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份
- 建议操作：`create` `vault/knowledge/claims/claim_play2perfect_inhand_pretraining_20260715-play2perfect-表明-play-预训练向装配迁移的关键是迫使手指-in-hand-操控而非固定抓握下的手臂运动.md`
- 原 candidate 保持不可变；本 proposal 使用新的 candidate。

## Base → Revised Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_inhand_pretraining_20260715-play2perfect-表明-play-预训练向装配迁移的关键是迫使手指-in-hand-操控而非固定抓握下的手臂运动.md
@@ -0,0 +1,26 @@
+---
+id: "claim_play2perfect_inhand_pretraining_20260715"
+type: "claim"
+status: "proposal"
+title: "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["pretraining", "in-hand-manipulation", "ablation"]
+domains: ["robotics"]
+confidence: "medium"
+source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Play2Perfect 默认 play 配方", "四装配任务下游微调（3 seeds 均值）", "消融：object diversity、objective、trajectory、goal precision"]
+uncertainty: "作者对 ablation 的综合解读；Translation-only 无法提供 reorientation 先验。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 2 页 Introduction", "excerpt": "play pretraining transfers best when it forces the robot to learn in-hand manipulation using its fingers rather than movement with a fixed grasp.", "stance": "supports", "reason": "引言总结。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "Translation-only pretraining learns grasping and lifting, but does not learn object orientation control", "stance": "supports", "reason": "Objective 消融。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "A loose 10cm threshold fails to transfer because coarse goal reaching does not require accurate object-pose control.", "stance": "supports", "reason": "Goal precision 消融。"}]
+---
+
+# Play 预训练中影响装配迁移的因素
+
+论文对 object diversity、training objective、trajectory diversity 和 goal precision 进行消融，并在四项装配任务、三个种子上比较下游 RL 微调。结果显示，更多物体、随机目标轨迹、完整 6D pose objective 和更精确的目标容差通常带来更快或更稳定的迁移。
+
+其中 orientation control 是关键条件：Translation-only 能学到抓取和抬升，但没有提供装配所需的 in-hand reorientation 先验；10 cm 的宽松目标容差也无法形成精确物体姿态控制。作者据此总结，play 最好迫使机器人用手指进行 in-hand manipulation，而不是依赖固定抓握下的手臂运动。
```
