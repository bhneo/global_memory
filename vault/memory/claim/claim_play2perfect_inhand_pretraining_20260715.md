---
id: "claim_play2perfect_inhand_pretraining_20260715"
type: "claim"
status: "working"
title: "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: []
tags: ["pretraining", "in-hand-manipulation", "ablation"]
domains: ["robotics"]
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Play2Perfect 默认 play 配方", "四装配任务下游微调（3 seeds 均值）", "消融：object diversity、objective、trajectory、goal precision"]
uncertainty: "作者对 ablation 的综合解读；Translation-only 无法提供 reorientation 先验。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 2 页 Introduction", "excerpt": "play pretraining transfers best when it forces the robot to learn in-hand manipulation using its fingers rather than movement with a fixed grasp.", "stance": "supports", "reason": "引言总结。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "Translation-only pretraining learns grasping and lifting, but does not learn object orientation control", "stance": "supports", "reason": "Objective 消融。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.2", "excerpt": "A loose 10cm threshold fails to transfer because coarse goal reaching does not require accurate object-pose control.", "stance": "supports", "reason": "Goal precision 消融。"}]
memory_tier: "working"
created_by: "human-candidate-revision-v1"
updated_by: "weekly-consolidation-v1"
model_provider: null
model_version: null
compiler_version: "human-candidate-revision-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-17T12:01:10+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_1e4548999e2e2dbf0a44fc97"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_1e4548999e2e2dbf0a44fc97.md"
origin_candidate_sha256: "8d7e38b40e6c1a2b8c505674501d2a1059faf00bcb027743a097b5e09302dd0b"
memory_schema_version: 1
---

# Play 预训练中影响装配迁移的因素

论文对 object diversity、training objective、trajectory diversity 和 goal precision 进行消融，并在四项装配任务、三个种子上比较下游 RL 微调。结果显示，更多物体、随机目标轨迹、完整 6D pose objective 和更精确的目标容差通常带来更快或更稳定的迁移。

其中 orientation control 是关键条件：Translation-only 能学到抓取和抬升，但没有提供装配所需的 in-hand reorientation 先验；10 cm 的宽松目标容差也无法形成精确物体姿态控制。作者据此总结，play 最好迫使机器人用手指进行 in-hand manipulation，而不是依赖固定抓握下的手臂运动。
