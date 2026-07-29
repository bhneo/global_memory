---
id: "concept_4739daf4ef7eacc9153c535f"
type: "concept"
status: "working"
title: "可靠价值驱动的离线到在线策略改进"
created_at: "2026-07-20T11:55:37+08:00"
updated_at: "2026-07-20T11:56:59+08:00"
aliases: ["Robo-ValueRL", "value-guided offline-to-online adaptation"]
tags: []
domains: ["embodied-ai", "robot-rl", "vla", "value-learning"]
confidence: "medium"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}]
change_reason: "compile bundle from source_7b278ba348f2a8bb94cce1fc"
reflection_context: {"reflection_ids": ["reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
consolidation_count: 1
last_consolidated_at: "2026-07-20T11:56:59+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_4b54c5c2979985532fa7"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_4b54c5c2979985532fa7-concept-1.md"
origin_candidate_sha256: "95db7958cead1edd694b45998b7c0f21f1921311c766c8fc3f0203026af8b8ff"
memory_schema_version: 2
last_consolidation_id: "consolidation_bc26ef979b149316e780adba"
---

# 可靠价值驱动的离线到在线策略改进

可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。
