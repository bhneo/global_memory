---
id: "concept_real_robot_deployment_iteration_loop"
type: "concept"
status: "working"
title: "真机部署评估迭代闭环"
created_at: "2026-07-19T12:18:02+08:00"
updated_at: "2026-07-19T12:20:21+08:00"
aliases: ["real-robot deployment-evaluation loop", "physical robot iteration loop", "deployment, evaluation and data-collection loop"]
tags: []
domains: ["embodied-ai", "robotics", "real-robot-evaluation", "data-collection"]
confidence: "medium"
source_ids: ["source_3e845794fed758f1dda5248e"]
relations: [{"type": "derived_from", "target_id": "source_3e845794fed758f1dda5248e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "part_of", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "端到端复现不仅要复现模型，还要固定观测、预测、平滑和实际执行命令之间的真机协议与日志。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_portable_embodied_inference_runtime", "reason": "可移植推理运行时解决模型侧异构执行，EVA-Client 解决机器人侧调度、逆解、采集和评估；两者是互补而非重复的部署层。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "claim_wechat_embodied_eval_bottleneck_20260715", "reason": "EVA-Client 把笼统的真机评估瓶颈具体化为场景协议、里程碑评分以及原始预测、平滑动作、实际命令三路可归因日志。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_3e845794fed758f1dda5248e"
uncertainty: "EVA-Client 是基础设施而非策略或 benchmark；文中任务结果是说明性部署观察，不能当作受控方法优越性实验。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-19T12:20:21+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_e231d1eaf0d303698229"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_e231d1eaf0d303698229-concept-1.md"
origin_candidate_sha256: "578066e560ea1336ef9aa4f91f6254668a5aa0dcec63fce8a4d81ff6e8a5f14f"
memory_schema_version: 2
last_consolidation_id: "consolidation_c24563aa0144d6d9d728eddd"
---

# 真机部署评估迭代闭环

用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。
