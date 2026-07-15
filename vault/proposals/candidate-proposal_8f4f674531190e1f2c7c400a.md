---
id: "claim_play2perfect_realworld_tight_insertion_20260715"
type: "claim"
status: "proposal"
title: "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-15T12:20:00+08:00"
aliases: []
tags: ["sim-to-real", "dexterous-manipulation", "assembly"]
domains: ["robotics"]
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Tight-Insertion 真实部署", "FoundationPose 跟踪、无 real-world finetuning", "10 rollouts/条件", "Sharpa + KUKA iiwa 14"]
uncertainty: "仅 10 次 rollout/条件；依赖 FoundationPose；摘要 60% 与 Table 1 的 6/10 一致。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "achieving 60% success on tight insertions with only 0.5 mm contact clearance", "stance": "supports", "reason": "摘要给出 0.5 mm 成功率。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Table 1", "excerpt": "Success Rate 10/10 9/10 6/10", "stance": "supports", "reason": "Table 1 各 clearance 成功次数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.4", "excerpt": "using FoundationPose for object pose tracking and no real-world finetuning", "stance": "context", "reason": "限定 sim-to-real 设定。"}]
---

# 真实世界紧插入

10mm:10/10; 2mm:9/10; 0.5mm:6/10。
