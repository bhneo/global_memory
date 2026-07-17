---
id: "claim_play2perfect_realworld_tight_insertion_20260715"
type: "claim"
status: "working"
title: "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: []
tags: ["sim-to-real", "dexterous-manipulation", "assembly"]
domains: ["robotics"]
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["Tight-Insertion 真实部署", "FoundationPose 跟踪、无 real-world finetuning", "10 rollouts/条件", "Sharpa + KUKA iiwa 14"]
uncertainty: "仅 10 次 rollout/条件；依赖 FoundationPose；摘要 60% 与 Table 1 的 6/10 一致。"
evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "achieving 60% success on tight insertions with only 0.5 mm contact clearance", "stance": "supports", "reason": "摘要给出 0.5 mm 成功率。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Table 1", "excerpt": "Success Rate 10/10 9/10 6/10", "stance": "supports", "reason": "Table 1 各 clearance 成功次数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.4", "excerpt": "using FoundationPose for object pose tracking and no real-world finetuning", "stance": "context", "reason": "限定 sim-to-real 设定。"}]
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
origin_proposal_id: "proposal_e4c5d7883d8cafc851d3a466"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_e4c5d7883d8cafc851d3a466.md"
origin_candidate_sha256: "4496101420695eb52879175a9be69b74c16c7cf7ebc149a42b0fe544eb4aeb2d"
memory_schema_version: 1
---

# Play2Perfect 的真实世界紧配合插入结果

论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 real-world finetuning。在 Tight-Insertion 的 10 次 rollout/条件中，10 mm、2 mm 和 0.5 mm clearance 分别取得 `10/10`、`9/10` 和 `6/10`。

该结果证明的是论文特定硬件、视觉跟踪和插入任务上的零样本 sim-to-real 表现。每个条件只有 10 次 rollout，失败仍集中在最终接触阶段，因此不能外推为一般真实装配可靠性。
