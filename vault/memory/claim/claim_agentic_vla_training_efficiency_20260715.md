---
id: "claim_agentic_vla_training_efficiency_20260715"
type: "claim"
status: "working"
title: "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×"
created_at: "2026-07-15T12:20:00+08:00"
updated_at: "2026-07-17T12:01:10+08:00"
aliases: []
tags: ["vla", "training-efficiency"]
domains: ["robot-learning"]
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
superseded_by: null
valid_during: null
change_reason: "批量导入原始论文知识；等待人工核验"
applicability: ["LIBERO-Long", "90% SR 收敛阈值", "Table 4 对比 SimpleVLA-RL / EVOLVE-VLA"]
uncertainty: "90% 为论文自定义阈值；wall-clock 未量化。"
evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "2.4× faster convergence compared to existing online adaptation methods", "stance": "supports", "reason": "摘要加速比。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8-9 页 Table 4", "excerpt": "EVOLVE-VLA 1,680 ... Agentic-VLA 700 ... 2.4×", "stance": "supports", "reason": "Table 4 迭代与 speedup。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 9 页 Section 4.5", "excerpt": "only 22.4k rollouts to achieve target performance, compared to 53.8k for EVOLVE-VLA", "stance": "supports", "reason": "rollout 规模。"}]
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
origin_proposal_id: "proposal_0e1b5b493ea68c0127447da6"
origin_item_id: "candidate"
origin_candidate_path: "vault/proposals/candidate-proposal_0e1b5b493ea68c0127447da6.md"
origin_candidate_sha256: "c3986800beab34361e10863afba2f285e201ea342cdbfb9646dbdfd1f59bd355"
memory_schema_version: 1
---

# Agentic-VLA 的训练效率

在 LIBERO-Long 达到论文定义的 90% 成功率阈值时，Agentic-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE-VLA 使用 1,680 次迭代和 53.8k rollouts。论文据此报告相对 EVOLVE-VLA 的 2.4× 收敛加速。

这里的“效率”指达到指定成功率阈值所需的 iteration 和 rollout 数量。论文没有给出对应 wall-clock 时间，因此不能把 2.4× 写成实际训练时长或计算成本加速。
