---
id: "concept_f5d1ef9eaed1cd6bec4d4c52"
type: "concept"
status: "working"
title: "图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory"
created_at: "2026-07-28T13:11:47+08:00"
updated_at: "2026-07-28T16:34:07+08:00"
aliases: ["graph-based agent memory lifecycle", "agent memory extraction storage retrieval evolution", "图记忆演化闭环", "图式记忆评测"]
tags: []
domains: ["agent-memory", "knowledge-graph", "memory-evolution", "evaluation"]
confidence: "medium"
source_ids: ["source_01ed2f19e91bb0eb1ec3ee92"]
relations: [{"type": "derived_from", "target_id": "source_01ed2f19e91bb0eb1ec3ee92", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-legacy-readmission", "status": "working"}]
change_reason: "compile bundle from source_01ed2f19e91bb0eb1ec3ee92"
reflection_context: {"reflection_ids": ["reflection_7952be977c24d5dfe1da2072"], "importance": "high", "changed_belief": "此前容易把图式记忆的价值概括为多跳检索；综述更重要的启发是，关系结构只有与选择性写入、冲突演化、环境反馈和可隔离的记忆评测结合，才构成长期认知系统。", "surprising": "综述明确指出，许多基准擅长测回忆，却缺少对冲突事实更新、选择性写入、遗忘和隐私保留的系统监督；这意味着检索成绩不能替代记忆演化质量。", "connections": [{"shared_mechanism": "综述的 extraction-storage-retrieval-evolution 生命周期与 Global Memory 的 Raw/Input-Working-Context-governed evolution 都把记忆视为持续更新的结构系统。", "boundary": "综述是广域二手分类材料，不能证明 Global Memory 的具体门禁、数据模型或效果优于其他系统。", "difference": "综述主要按图结构与算法类别组织领域；Global Memory 用 Markdown 真相层和 typed relations 表达图，并把证据、Receipt 与 Canonical 审批作为独立治理边界。"}], "open_questions": ["怎样设计能独立测量冲突更新、选择性写入和长期复用收益，而不把规划器或基础模型能力混入结果的基准？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "gpt-5.6-sol-high-daily-v2-legacy-readmission"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "gpt-5.6-sol-high-daily-v2-legacy-readmission"
consolidation_count: 1
last_consolidated_at: "2026-07-28T16:34:07+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_94d8f36451c94dcdf8dd"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_94d8f36451c94dcdf8dd-concept-1.md"
origin_candidate_sha256: "ae450c5d0a7fe10cb2e9fb93eb60a5a20d0e0f61f92be5868740bfb85dd177c1"
origin_cognitive_artifact_sha256: "c2b05d2462ceda90d223e257abd0b18283744ad3aabe8b3ca42099eb1533c6c2"
memory_schema_version: 2
last_consolidation_id: "consolidation_a7a92cacd4212966412b800e"
---

# 图式 Agent Memory 的生命周期与评测闭环 / lifecycle and evaluation closure for graph-based agent memory

图式 Agent Memory 可被组织为持续循环：从交互或外部材料中选择性抽取记忆单元，将实体、事件、概念或文本块及其语义、时间、因果关系写入图结构；在任务中通过语义相似、图遍历或二者组合检索相关子图；再依据新观察、动作和环境反馈增量增加、修改、失效或冲突化节点与关系。关系图能够支持多跳和层级推理，但结构存在本身不等于长期记忆质量。评测至少要分开测量检索相关性、图的一致性与完整性、冗余和时间一致性、下游任务效用，以及冲突事实更新、选择性写入、遗忘、外部真实性校验、隐私泄漏与来源可追溯性。综述指出现有基准常偏重回忆，难以隔离记忆模块、规划器和基础模型的贡献；因此，高召回或高连接度不能替代记忆演化与证据闭环的验证。该来源是领域综述，提供分类框架而非证明某一实现优于其他系统。
