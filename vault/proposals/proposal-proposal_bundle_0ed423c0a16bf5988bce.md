---
id: "proposal_bundle_0ed423c0a16bf5988bce"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:22:32+08:00"
updated_at: "2026-07-21T17:22:33+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e753604a46350e066a104918"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_5bda5867d1e50385d394c51e"
input_sha256: "4147506b3162fe998a62486da5efde941bb58e754eff8317ab7d394eb7eb1718"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_hierarchical_mathematical_compression", "target_path": "vault/knowledge/concepts/concept_hierarchical_mathematical_compression-数学兴趣的层级压缩模型.md", "base_sha256": null, "candidate_sha256": "7d853e0612c104bbd75937988e3603eab5aed35f71a5ea040b60f51cd361f128", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0ed423c0a16bf5988bce-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_hierarchical_mathematical_compression.md", "working_at": "2026-07-21T17:22:33+08:00"}, {"item_id": "question-2", "object_type": "question", "action": "create", "target_id": "question_compression_biased_mathematical_search", "target_path": "vault/frontier/questions/question_compression_biased_mathematical_search-压缩偏置会把自动数学探索引向真正有价值的结果吗.md", "base_sha256": null, "candidate_sha256": "04b936af473e178c3536acdd05061cd9ebefc5989a239c071acbe54d2cabe43d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0ed423c0a16bf5988bce-question-2.md", "base_path": null, "working_path": "vault/memory/question/question_compression_biased_mathematical_search.md", "working_at": "2026-07-21T17:22:33+08:00"}]
existing_context: [{"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…loop action generation.\n\n## What changed\n\nA teleoperation interface [need] not copy every human joint. Sparse joint hand-object…", "match_reason": "full-text:body"}, {"id": "concept_f67f822ee20789d74d7b75e3", "type": "concept", "title": "物理失败合成驱动的稠密机器人奖励建模", "path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "status": "working", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# 物理失败合成驱动的稠密机器人奖励建模\n\n通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。", "match_reason": "metadata:aliases"}, {"id": "reflection_cb246940931502d077f687f5", "type": "reflection", "title": "DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配", "path": "vault/reflections/reflection-reflection_cb246940931502d077f687f5.md", "status": "active", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配\n\n## Why important\n\nDenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。\n\n## What changed\n\n此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。\n\n## Surprising\n\n两帧历史优于一帧…", "match_reason": "metadata:domains"}, {"id": "reflection_4b63a8834e11b28db3cf2fdc", "type": "reflection", "title": "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心", "path": "vault/reflections/reflection-reflection_4b63a8834e11b28db3cf2fdc.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心\n\n## Why important\n\nTACTIC 不只把触觉追加到 observation，而是让 distributed tactile、proximity map、contact Jacobian sampling 和 hybrid…", "match_reason": "metadata:domains"}, {"id": "claim_wechat_particle_poincare_irrep_20260716", "type": "claim", "title": "该文介绍维格纳观点：粒子可由庞加莱群的不可约表示定义", "path": "vault/memory/claim/claim_wechat_particle_poincare_irrep_20260716.md", "status": "working", "source_ids": ["source_9bcee8e0abc8386cbba43b87"], "snippet": "该文介绍维格纳观点：粒子可由庞加莱群的不可约表示定义。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_lie_group_continuous_symmetry_20260715", "type": "claim", "title": "该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念", "path": "vault/memory/claim/claim_wechat_lie_group_continuous_symmetry_20260715.md", "status": "working", "source_ids": ["source_941321d95232028c233c9433"], "snippet": "# 李群与连续对称\n\n描述连续对称；洛伦兹变换与自旋。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_lie_group_definition_20260715", "type": "claim", "title": "该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合", "path": "vault/memory/claim/claim_wechat_lie_group_definition_20260715.md", "status": "working", "source_ids": ["source_941321d95232028c233c9433"], "snippet": "# 李群定义\n\n群 + 微分流形 + 相容运算。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_godel_first_incompleteness_20260716", "type": "claim", "title": "该文称哥德尔第一不完全性定理表明：在《数学原理》体系中存在既不可证也不可否的佩亚诺算术命题", "path": "vault/memory/claim/claim_wechat_godel_first_incompleteness_20260716.md", "status": "working", "source_ids": ["source_aff280ea206f7233b98afc6a"], "snippet": "# 第一不完全性定理\n\n存在不可判定命题；非「所有问题都可证伪」。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_standard_model_symmetry_group_20260716", "type": "claim", "title": "该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示", "path": "vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md", "status": "working", "source_ids": ["source_9bcee8e0abc8386cbba43b87"], "snippet": "该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_e753604a46350e066a104918"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 2, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 2, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-daily-gpt56sol-v1`
- Extraction：`extraction_5bda5867d1e50385d394c51e`
- 编译前召回已有对象：9
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_hierarchical_mathematical_compression-数学兴趣的层级压缩模型.md
@@ -0,0 +1,21 @@
+---
+id: "concept_hierarchical_mathematical_compression"
+type: "concept"
+status: "proposal"
+title: "数学兴趣的层级压缩模型"
+created_at: "2026-07-21T17:22:32+08:00"
+updated_at: "2026-07-21T17:22:32+08:00"
+aliases: ["Hierarchical Compression Model of Mathematical Interest", "Hierarchical Mathematical Compression", "Mathematical Interest via Compression", "数学层级压缩", "数学兴趣压缩模型", "HM/FM compression model", "HM/FM 压缩模型"]
+tags: []
+domains: ["automated-reasoning", "formal-mathematics", "knowledge-graphs", "mathematical-discovery"]
+confidence: "medium"
+source_ids: ["source_e753604a46350e066a104918"]
+relations: [{"type": "derived_from", "target_id": "source_e753604a46350e066a104918", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "proposal"}, {"type": "raises", "target_id": "question_compression_biased_mathematical_search", "reason": "把压缩从描述性特征转为探索目标，会直接引出其外部效度、可操纵性与抽象偏置问题。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e753604a46350e066a104918"
+uncertainty: "经验部分只覆盖作者选定版本和处理方式下的 Mathlib；与慢增长 monoid 模型相容不等于排除了所有其他解释，且兴趣度量尚未与人类判断或搜索收益系统校准。"
+reflection_context: {"reflection_ids": ["reflection_81c9fd8c2a3fe78fb40e0e68"], "importance": "high", "changed_belief": "此前库中没有关于数学兴趣度量的活跃语义对象；旧 deterministic 编译只截取了第 24 页片段并产生错误标题。重新阅读全文后，核心应是层级定义带来的 reductive/deductive compression、Mathlib 经验观测，以及这些量作为探索启发式而非真值或审美判据的边界。", "surprising": "作者在约 46.4 万个 Mathlib 声明构成的依赖 DAG 上报告：中位 log2(unwrapped length) 随 depth 近线性增长、wrapped length 跨深度大致保持在 50–120 tokens、log2(unwrapped length) 对 wrapped length 的斜率约为 0.4 bits/token；这些观测与其自由阿贝尔/慢增长 monoid 模型相容，但不能唯一确认该模型。", "connections": [{"shared_mechanism": "层级命名和可复用依赖都把长推导折叠为较短的可组合对象，并可在图结构上度量其下游复用。", "boundary": "压缩和 PageRank 只能作为固定形式库中的研究启发式；它们不证明定理为真，也不等价于人类数学价值，更不能取代证明检查。", "difference": "reductive compression 衡量定义对表达长度的缩减，deductive compression 衡量短陈述背后的证明负担；PageRank-style refinement 再加入对象对其他高压缩对象的承重作用。"}], "open_questions": ["在不同形式库、不同定义粒度和多证明超图表示下，压缩—深度关系是否保持？", "将人类专家兴趣判断作为外部标签时，压缩与图中心性组合能否优于引用、复用次数或证明长度等简单基线？"]}
+---
+
+# 数学兴趣的层级压缩模型
+
+把形式数学对象表示为依赖图中的层级宏：wrapped length 记录使用已有定义后的局部表达长度，unwrapped length 记录递归展开到原语后的长度，depth 记录定义嵌套层数。Aksenov 等人在 arXiv:2603.20396 中以 Mathlib 为 human mathematics 的代理，观察到展开长度随深度和包装长度近似指数增长，而包装长度跨深度大致稳定；据此提出 reductive compression、deductive compression 与 compression-biased PageRank 可作为自动数学探索的方向信号。该模型是预印本提出并在单一形式库上检验的启发式，不是数学兴趣的既定定义，也不提供正确性证据。
```

### question-2 (create question)

```diff
--- /dev/null
+++ candidate:vault/frontier/questions/question_compression_biased_mathematical_search-压缩偏置会把自动数学探索引向真正有价值的结果吗.md
@@ -0,0 +1,20 @@
+---
+id: "question_compression_biased_mathematical_search"
+type: "question"
+status: "proposal"
+title: "压缩偏置会把自动数学探索引向真正有价值的结果吗？"
+created_at: "2026-07-21T17:22:32+08:00"
+updated_at: "2026-07-21T17:22:32+08:00"
+aliases: ["Does Compression Bias Guide Valuable Mathematical Discovery?", "Compression-Biased Mathematical Search", "压缩偏置数学搜索"]
+tags: []
+domains: ["automated-reasoning", "formal-mathematics", "mathematical-discovery"]
+confidence: "medium"
+source_ids: ["source_e753604a46350e066a104918"]
+relations: [{"type": "derived_from", "target_id": "source_e753604a46350e066a104918", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_hierarchical_mathematical_compression", "reason": "该问题直接检验层级压缩模型从描述性观测迁移为自动探索目标时的效度和偏差。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e753604a46350e066a104918"
+reflection_context: {"reflection_ids": ["reflection_81c9fd8c2a3fe78fb40e0e68"], "importance": "high", "changed_belief": "此前库中没有关于数学兴趣度量的活跃语义对象；旧 deterministic 编译只截取了第 24 页片段并产生错误标题。重新阅读全文后，核心应是层级定义带来的 reductive/deductive compression、Mathlib 经验观测，以及这些量作为探索启发式而非真值或审美判据的边界。", "surprising": "作者在约 46.4 万个 Mathlib 声明构成的依赖 DAG 上报告：中位 log2(unwrapped length) 随 depth 近线性增长、wrapped length 跨深度大致保持在 50–120 tokens、log2(unwrapped length) 对 wrapped length 的斜率约为 0.4 bits/token；这些观测与其自由阿贝尔/慢增长 monoid 模型相容，但不能唯一确认该模型。", "connections": [{"shared_mechanism": "层级命名和可复用依赖都把长推导折叠为较短的可组合对象，并可在图结构上度量其下游复用。", "boundary": "压缩和 PageRank 只能作为固定形式库中的研究启发式；它们不证明定理为真，也不等价于人类数学价值，更不能取代证明检查。", "difference": "reductive compression 衡量定义对表达长度的缩减，deductive compression 衡量短陈述背后的证明负担；PageRank-style refinement 再加入对象对其他高压缩对象的承重作用。"}], "open_questions": ["在不同形式库、不同定义粒度和多证明超图表示下，压缩—深度关系是否保持？", "将人类专家兴趣判断作为外部标签时，压缩与图中心性组合能否优于引用、复用次数或证明长度等简单基线？"]}
+---
+
+# 压缩偏置会把自动数学探索引向真正有价值的结果吗？
+
+若以 reductive/deductive compression 和依赖图 PageRank 为自动推理的探索奖励，需要验证它是否能预测专家兴趣与搜索收益，同时避免偏爱抽象、库工程热点或可人为构造的高压缩对象。关键检验应跨形式库、定义粒度与历史时间切片，并与简单图统计和证明长度基线比较。
```
