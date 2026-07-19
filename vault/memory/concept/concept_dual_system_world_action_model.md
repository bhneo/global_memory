---
id: "concept_dual_system_world_action_model"
type: "concept"
status: "working"
title: "双系统 World Action Model"
created_at: "2026-07-19T03:03:07+08:00"
updated_at: "2026-07-19T03:39:20+08:00"
aliases: ["dual-system world-action model", "DSWAM"]
tags: []
domains: ["embodied-ai", "world-action-model", "vla", "planning"]
confidence: "medium"
source_ids: ["source_ba057c2c11df2a5eba107870"]
relations: [{"type": "derived_from", "target_id": "source_ba057c2c11df2a5eba107870", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "两者都将预测性世界表征接入动作系统，但 DSWAM 以 WAM 执行为默认路径。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两种架构都用双速或多速层级分离语义规划与动作执行。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "raises", "target_id": "tension_world_model_eval_action", "reason": "DSWAM 直接比较 WAM 与 VLA 执行路径，触及世界模型应作为评估器还是动作生成器的边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_ba057c2c11df2a5eba107870"
uncertainty: "是否优于单体 VLA 取决于公平数据、机器人本体、任务协议和实时系统实现。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 4
last_consolidated_at: "2026-07-19T03:39:20+08:00"
last_verified_at: "2026-07-19T03:30:06+08:00"
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_6eccb3b8a64c69fe1836"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_6eccb3b8a64c69fe1836-concept-1.md"
origin_candidate_sha256: "5ced4e982782653e5e4f9f97f7086ab5478c17d667f40eb20011da720d7de8b4"
memory_schema_version: 2
last_consolidation_id: "consolidation_7d1695288f24b7980f03e684"
evidence: []
change_history: [{"change_type": "metadata_only", "previous_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "new_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ba057c2c11df2a5eba107870", "trigger_source": "source_ba057c2c11df2a5eba107870", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "new_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_ba057c2c11df2a5eba107870", "trigger_source": "source_ba057c2c11df2a5eba107870", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "new_statement": "# 双系统 World Action Model\n\n默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "changed_fields": ["aliases"], "reason": "compile bundle from source_ba057c2c11df2a5eba107870", "trigger_source": "source_ba057c2c11df2a5eba107870", "evidence_added": []}]
---

# 双系统 World Action Model

默认由 World Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。
