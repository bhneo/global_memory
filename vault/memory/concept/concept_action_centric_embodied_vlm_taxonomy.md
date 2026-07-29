---
id: "concept_action_centric_embodied_vlm_taxonomy"
type: "concept"
status: "working"
title: "动作中心的具身 VLM 能力分类"
created_at: "2026-07-21T17:45:09+08:00"
updated_at: "2026-07-26T12:33:43+08:00"
aliases: ["Action-Centric Embodied VLM Capability Taxonomy", "Hy-Embodied-VLM-1.0", "Action-Relevant State Understanding", "动作中心具身视觉语言模型"]
tags: []
domains: ["embodied-ai", "vision-language-model", "action-reasoning"]
confidence: "medium"
source_ids: ["source_bd08e368730960f4f6ce19ca"]
relations: [{"type": "derived_from", "target_id": "source_bd08e368730960f4f6ce19ca", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "动作中心 VLM 提供状态和转移推理表征，预测式 VLA 则把类似信息直接用于动作策略训练与部署。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "working"}]
change_reason: "compile bundle from source_bd08e368730960f4f6ce19ca"
reflection_context: {"reflection_ids": ["reflection_d622c6d4e908ef7dae5470b8"], "importance": "medium", "changed_belief": "具身 VLM 的价值可体现在动作前的状态与转移推理，但 benchmark 排名不能证明机器人闭环执行能力。", "surprising": "论文摘要和项目页报告约 30B 总参数、每 token 激活约 3B，并在 38 个具身相关 benchmark 中 19 项第一；当前抓取的论文来源只有 arXiv 摘要页，细节主要由配套仓库补充。", "connections": [{"shared_mechanism": "都以动作相关信息组织视觉语言表示。", "boundary": "具身 VLM benchmark 不等于连续动作生成、低层控制或真实安全验证。", "difference": "Hy-Embodied-VLM 输出状态与动作推理表征；VLA 概念进一步要求将观察和语言映射为可执行动作。"}], "open_questions": ["动作中心 taxonomy 的每一维对下游真实机器人成功率分别贡献多少？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56sol-readmission-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56sol-readmission-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:43+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_54e90a60992f6351761d"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_54e90a60992f6351761d-concept-1.md"
origin_candidate_sha256: "b4b890c04e14ce20c3734c7e2f8264b074a465e6ff32be4f60d29ddf764747a0"
memory_schema_version: 2
last_consolidation_id: "consolidation_7d5354796e9237ff761cc948"
---

# 动作中心的具身 VLM 能力分类

Hy-Embodied-VLM-1.0 将具身视觉语言能力划分为动作相关状态理解、动作转移推理、序列与自适应推理，并据此组织预训练和后训练数据；其稀疏 MoE 架构面向延迟敏感部署。该分类描述的是动作前置的视觉语言推理能力，不应与连续动作生成、闭环 VLA 控制或真实机器人安全混同。
