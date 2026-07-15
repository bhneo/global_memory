---
id: "claim_play2perfect_finetuning_necessary_20260715"
type: "claim"
status: "proposal"
title: "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-15T12:20:00+08:00"
aliases: []
tags: ["finetuning", "contact-rich", "assembly"]
domains: ["robotics"]
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Tight-Insertion", "Play-only vs Play2Perfect", "5–0.5 mm 微调 clearance 范围"]
uncertainty: "Play-only 在宽松间隙仍可能成功；claim 针对 tight/contact-rich regime。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7-8 页 Section 4.3", "excerpt": "RL finetuning is still needed to turn this prior into a precise, contact-rich assembly policy.", "stance": "supports", "reason": "作者结论。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.3", "excerpt": "At 0.5 mm clearance, Play2Perfect still succeeds 60% of the time, whereas Play-only fails completely.", "stance": "supports", "reason": "真实 tight clearance 对比。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.3", "excerpt": "Play-only solves only the loosest insertion settings", "stance": "context", "reason": "play 先验在粗精度仍有用。"}]
---

# 微调必要性

Section 4.3 Play-only vs Play2Perfect。
