---
id: "claim_agentic_vla_libero_main_20260715"
type: "claim"
status: "working"
title: "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: ["Agentic-VLA LIBERO"]
tags: ["vla", "libero", "online-adaptation"]
domains: ["robot-learning"]
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["LIBERO 四套件", "OpenVLA-OFT 基线", "5 seeds mean±std"]
uncertainty: "LIBERO 仿真 benchmark；+12.3% 相对 SFT baseline（Table 1 Δ 列）。"
evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "+12.3% on long-horizon tasks", "stance": "supports", "reason": "摘要 Long 提升。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7 页 Table 1", "excerpt": "Agentic-VLA† 97.8±0.4 ... Δ vs. SFT baseline +12.3", "stance": "supports", "reason": "Table 1 平均与 Long 差值。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7 页 Section 4.2", "excerpt": "Reporting mean ± std over 5 independent seeds", "stance": "context", "reason": "统计协议。"}]
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
origin_proposal_id: "proposal_a99124724d635b4102390d75"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_a99124724d635b4102390d75.md"
origin_candidate_sha256: "9b3e8467bac10234561572ef50cc3d68fa4c9714c794930760c38293eabc2deb"
memory_schema_version: 1
---

# Agentic-VLA 的 LIBERO 主结果

在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2±0.6%`、`98.6±0.5%`、`97.4±0.6%` 和 `98.1±0.8%`，平均为 `97.8±0.4%`。相对复现的 OpenVLA-OFT SFT baseline，Long 套件提高 12.3 个百分点；相对 EVOLVE-VLA，平均提高 2.0 个百分点。

这些结果来自 LIBERO 仿真 benchmark，论文对自行运行的方法报告 5 个独立种子的 mean±std；它们不能直接外推为真实机器人成功率。
