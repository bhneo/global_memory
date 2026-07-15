---
id: "proposal_d844a95491ff017088f292cc"
type: "proposal"
status: "superseded"
title: "模型提议：Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动"
created_at: "2026-07-15T12:25:11+08:00"
updated_at: "2026-07-15T14:28:00+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_play2perfect_inhand_pretraining_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_inhand_pretraining_20260715-play2perfect-表明-play-预训练向装配迁移的关键是迫使手指-in-hand-操控而非固定抓握下的手臂运动.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_d844a95491ff017088f292cc.md"
candidate_sha256: "3ca0a880955b4b6ecf09a742c8b5998a6036e5832e457817cba45349700c0062"
change_reason: "Play2Perfect in-hand"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_05d8a9da9e0b53b94872f2a7", "input_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:28:00+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_1e4548999e2e2dbf0a44fc97"
---

# 模型提议：Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_05d8a9da9e0b53b94872f2a7`
- Input SHA-256：`a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Play2Perfect in-hand
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_inhand_pretraining_20260715-play2perfect-表明-play-预训练向装配迁移的关键是迫使手指-in-hand-操控而非固定抓握下的手臂运动.md
@@ -0,0 +1,24 @@
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
+source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Play2Perfect 默认 play 配方", "四装配任务下游微调（3 seeds 均值）", "消融：object diversity、objective、trajectory、goal precision"]
+uncertainty: "作者对 ablation 的综合解读；Translation-only 无法提供 reorientation 先验。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 2 页 Introduction", "excerpt": "play pretraining transfers best when it forces the robot to learn in-hand manipulation using its fingers rather than movement with a fixed grasp.", "stance": "supports", "reason": "引言总结。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "Translation-only pretraining learns grasping and lifting, but does not learn object orientation control", "stance": "supports", "reason": "Objective 消融。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "A loose 10cm threshold fails to transfer because coarse goal reaching does not require accurate object-pose control.", "stance": "supports", "reason": "Goal precision 消融。"}]
+---
+
+# in-hand 预训练设计
+
+见 Section 4.2 ablations。
```
