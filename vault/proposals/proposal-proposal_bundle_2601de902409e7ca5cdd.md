---
id: "proposal_bundle_2601de902409e7ca5cdd"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-17T12:11:45+08:00"
updated_at: "2026-07-17T12:11:45+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_dbfef5ee180346812d6d9a99"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_32744b02cae33e8a519747c3"
input_sha256: "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_0c81697b0e302dcee8d96199", "target_path": "vault/knowledge/claims/claim_0c81697b0e302dcee8d96199-来源原文-published-in-transactions-on-machine-learning-research-12-2.md", "base_sha256": null, "candidate_sha256": "3da6ca6c6b679535092b53fbfedd6bc1d23f1e709ab853226bd5d1abb481ab09", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_2601de902409e7ca5cdd-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_0c81697b0e302dcee8d96199.md", "working_at": "2026-07-17T12:11:45+08:00"}]
existing_context: [{"id": "claim_physo_units_constraints_reduce_search_20260716", "type": "claim", "title": "Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间", "path": "vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 在生成过程中施加物理单位约束，以排除单位不一致表达式并缩小搜索空间。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_cross_modal_representation_alignment_20260716", "type": "claim", "title": "该文称文本模型与视觉模型随能力增强也呈现更强表征一致性，并以颜色表征与人类感知一致为例", "path": "vault/memory/claim/claim_wechat_cross_modal_representation_alignment_20260716.md", "status": "working", "source_ids": ["source_f35b44d4bd383fb26ca49165"], "snippet": "# 跨模态对齐\n\n文本与视觉表征趋同；颜色例为二手引述。", "match_reason": "metadata:domains"}, {"id": "claim_physo_rnn_reinforcement_learning_method_20260716", "type": "claim", "title": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式", "path": "vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md", "status": "trusted", "source_ids": ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"], "snippet": "Φ-SO 使用深度强化学习训练 RNN 生成符号表达式。", "match_reason": "metadata:tags"}, {"id": "claim_wechat_embodied_data_structure_not_volume_20260716", "type": "claim", "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe", "path": "vault/memory/claim/claim_wechat_embodied_data_structure_not_volume_20260716.md", "status": "working", "source_ids": ["source_0a113baae7ce4d1ab78da1a3"], "snippet": "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_wangjun_global_workspace_integration_20260716", "type": "claim", "title": "该文称 Global neuronal workspace 通过全局工作空间整合各模块信息，是有意识决策的建模方向之一", "path": "vault/memory/claim/claim_wechat_wangjun_global_workspace_integration_20260716.md", "status": "working", "source_ids": ["source_68161c78067d7b4add05ba1a"], "snippet": "# Global workspace\n\n全局整合各模块信息；意识建模候选框架。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_epiplexity_definition_20260715", "type": "claim", "title": "Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable", "path": "vault/memory/claim/claim_wechat_epiplexity_definition_20260715.md", "status": "trusted", "source_ids": ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "For the time-bounded minimum-description-length program P*, the paper defines T-bounded epiplexity S_T(X…", "match_reason": "metadata:domains"}, {"id": "work_arxiv_2605_10500", "type": "work", "title": "[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill", "path": "vault/memory/work/work_arxiv_2605_10500.md", "status": "working", "source_ids": ["source_0214d3d2f8cddf30a1140f8a", "source_ca1f80f2bf2e7d410ab2459e"], "snippet": "…Skill [Learning] as a Meta-Skill\n\n## Logical work identity\n\n- arXiv：`2605.10500`\n- Version：`unknown`\n- Captures：`source_0214d3d2f8cddf30a1140f8a`, `source…", "match_reason": "metadata:title"}, {"id": "work_arxiv_1810_08647", "type": "work", "title": "[1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning", "path": "vault/memory/work/work_arxiv_1810_08647.md", "status": "working", "source_ids": ["source_e9ed0a3745aea832b64d7fa7", "source_c019c0a492cc659d7858134d"], "snippet": "# [1810.08647] Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement [Learning]\n\n## Logical work identity\n\n- arXiv：`1810…", "match_reason": "metadata:title"}, {"id": "claim_wechat_im_rl_framework_internal_rewards_20260716", "type": "claim", "title": "该文称经典 RL 虽常被视为仅处理外在奖励，但 Barto 等框架可将奖励生成机制置于「内部环境」，内在与外在奖励可统一建模", "path": "vault/memory/claim/claim_wechat_im_rl_framework_internal_rewards_20260716.md", "status": "working", "source_ids": ["source_91199da18f239c48bbcdd49f"], "snippet": "# RL 统一奖励\n\n内在奖励可在体内生成；RL 框架不必限定外部通道。", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_dbfef5ee180346812d6d9a99"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_32744b02cae33e8a519747c3`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_0c81697b0e302dcee8d96199-来源原文-published-in-transactions-on-machine-learning-research-12-2.md
@@ -0,0 +1,44 @@
+---
+id: "claim_0c81697b0e302dcee8d96199"
+type: "claim"
+status: "proposal"
+title: "来源原文：Published in Transactions on Machine Learning Research (12/2025)\nSymmetry in Neu"
+created_at: "2026-07-17T12:11:45+08:00"
+updated_at: "2026-07-17T12:11:45+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_dbfef5ee180346812d6d9a99"]
+relations: [{"type": "derived_from", "target_id": "source_dbfef5ee180346812d6d9a99", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_dbfef5ee180346812d6d9a99"
+evidence: [{"evidence_id": "evidence_128adf0ba37d2cf68f22", "evidence_kind": "quote", "source_id": "source_dbfef5ee180346812d6d9a99", "content_id": "content_8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681", "extraction_id": "extraction_32744b02cae33e8a519747c3", "span_start": 18, "span_end": 518, "original_text": "Published in Transactions on Machine Learning Research (12/2025)\nSymmetry in Neural Network Parameter Spaces\nBo Zhao bozhao@ucsd.edu\nUniversity of California, San Diego\nRobin Waltersr.walters@northeastern.edu\nNortheastern University\nRose Yu roseyu@ucsd.edu\nUniversity of California, San Diego\nReviewed on OpenReview:https: // openreview. net/ forum? id= jLpWq5QY6I\nAbstract\nModern deep learning models are highly overparameterized, resulting in large sets of param-\neter configurations that yield the", "page": 1, "stance": "context", "verification_status": "verified", "input_sha256": "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: null
+split_reason: null
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 来源原文：Published in Transactions on Machine Learning Research (12/2025)
+Symmetry in Neu
+
+Published in Transactions on Machine Learning Research (12/2025)
+Symmetry in Neural Network Parameter Spaces
+Bo Zhao bozhao@ucsd.edu
+University of California, San Diego
+Robin Waltersr.walters@northeastern.edu
+Northeastern University
+Rose Yu roseyu@ucsd.edu
+University of California, San Diego
+Reviewed on OpenReview:https: // openreview. net/ forum? id= jLpWq5QY6I
+Abstract
+Modern deep learning models are highly overparameterized, resulting in large sets of param-
+eter configurations that yield the
```
