---
id: "claim_play2perfect_inhand_pretraining_20260715"
type: "claim"
status: "proposal"
title: "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-15T12:20:00+08:00"
aliases: []
tags: ["pretraining", "in-hand-manipulation", "ablation"]
domains: ["robotics"]
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Play2Perfect 默认 play 配方", "四装配任务下游微调（3 seeds 均值）", "消融：object diversity、objective、trajectory、goal precision"]
uncertainty: "作者对 ablation 的综合解读；Translation-only 无法提供 reorientation 先验。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 2 页 Introduction", "excerpt": "play pretraining transfers best when it forces the robot to learn in-hand manipulation using its fingers rather than movement with a fixed grasp.", "stance": "supports", "reason": "引言总结。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "Translation-only pretraining learns grasping and lifting, but does not learn object orientation control", "stance": "supports", "reason": "Objective 消融。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "A loose 10cm threshold fails to transfer because coarse goal reaching does not require accurate object-pose control.", "stance": "supports", "reason": "Goal precision 消融。"}]
---

# in-hand 预训练设计

见 Section 4.2 ablations。
