---
id: "concept_hierarchical_mathematical_compression"
type: "concept"
status: "working"
title: "数学兴趣的层级压缩模型"
created_at: "2026-07-21T17:22:32+08:00"
updated_at: "2026-07-26T12:33:53+08:00"
aliases: ["Hierarchical Compression Model of Mathematical Interest", "Hierarchical Mathematical Compression", "Mathematical Interest via Compression", "数学层级压缩", "数学兴趣压缩模型", "HM/FM compression model", "HM/FM 压缩模型"]
tags: []
domains: ["automated-reasoning", "formal-mathematics", "knowledge-graphs", "mathematical-discovery"]
confidence: "medium"
source_ids: ["source_e753604a46350e066a104918"]
relations: [{"type": "derived_from", "target_id": "source_e753604a46350e066a104918", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "working"}, {"type": "raises", "target_id": "question_compression_biased_mathematical_search", "reason": "把压缩从描述性特征转为探索目标，会直接引出其外部效度、可操纵性与抽象偏置问题。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "working"}]
change_reason: "compile bundle from source_e753604a46350e066a104918"
uncertainty: "经验部分只覆盖作者选定版本和处理方式下的 Mathlib；与慢增长 monoid 模型相容不等于排除了所有其他解释，且兴趣度量尚未与人类判断或搜索收益系统校准。"
reflection_context: {"reflection_ids": ["reflection_81c9fd8c2a3fe78fb40e0e68"], "importance": "high", "changed_belief": "此前库中没有关于数学兴趣度量的活跃语义对象；旧 deterministic 编译只截取了第 24 页片段并产生错误标题。重新阅读全文后，核心应是层级定义带来的 reductive/deductive compression、Mathlib 经验观测，以及这些量作为探索启发式而非真值或审美判据的边界。", "surprising": "作者在约 46.4 万个 Mathlib 声明构成的依赖 DAG 上报告：中位 log2(unwrapped length) 随 depth 近线性增长、wrapped length 跨深度大致保持在 50–120 tokens、log2(unwrapped length) 对 wrapped length 的斜率约为 0.4 bits/token；这些观测与其自由阿贝尔/慢增长 monoid 模型相容，但不能唯一确认该模型。", "connections": [{"shared_mechanism": "层级命名和可复用依赖都把长推导折叠为较短的可组合对象，并可在图结构上度量其下游复用。", "boundary": "压缩和 PageRank 只能作为固定形式库中的研究启发式；它们不证明定理为真，也不等价于人类数学价值，更不能取代证明检查。", "difference": "reductive compression 衡量定义对表达长度的缩减，deductive compression 衡量短陈述背后的证明负担；PageRank-style refinement 再加入对象对其他高压缩对象的承重作用。"}], "open_questions": ["在不同形式库、不同定义粒度和多证明超图表示下，压缩—深度关系是否保持？", "将人类专家兴趣判断作为外部标签时，压缩与图中心性组合能否优于引用、复用次数或证明长度等简单基线？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-daily-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-daily-gpt56sol-v1"
consolidation_count: 1
last_consolidated_at: "2026-07-26T12:33:53+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0ed423c0a16bf5988bce"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0ed423c0a16bf5988bce-concept-1.md"
origin_candidate_sha256: "7d853e0612c104bbd75937988e3603eab5aed35f71a5ea040b60f51cd361f128"
memory_schema_version: 2
last_consolidation_id: "consolidation_5f004ffd4d12a9539e2c5860"
---

# 数学兴趣的层级压缩模型

把形式数学对象表示为依赖图中的层级宏：wrapped length 记录使用已有定义后的局部表达长度，unwrapped length 记录递归展开到原语后的长度，depth 记录定义嵌套层数。Aksenov 等人在 arXiv:2603.20396 中以 Mathlib 为 human mathematics 的代理，观察到展开长度随深度和包装长度近似指数增长，而包装长度跨深度大致稳定；据此提出 reductive compression、deductive compression 与 compression-biased PageRank 可作为自动数学探索的方向信号。该模型是预印本提出并在单一形式库上检验的启发式，不是数学兴趣的既定定义，也不提供正确性证据。
