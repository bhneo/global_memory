---
id: "proposal_bundle_915ac66f5af193cc3ec2"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:19:04+08:00"
updated_at: "2026-07-19T12:19:04+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-weekly-gpt56sol-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_dfb859e53fae61aa66a0c3f5"
input_sha256: "0f7fc3c1792ef4645ef866526736a83a5e2cf4f55be513158bb2e165c62df1dd"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_latent_space_intervention_adaptation", "target_path": "vault/knowledge/concepts/concept_latent_space_intervention_adaptation-生成策略的潜空间干预适应.md", "base_sha256": null, "candidate_sha256": "a1570eba4b9e88ec518093ddc5530da1f62b312f5dd1181cb52fd2a940f7096d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_915ac66f5af193cc3ec2-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "working_at": "2026-07-19T12:19:04+08:00"}]
existing_context: [{"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:tags"}, {"id": "claim_215a419e0f318ce8fbad6627", "type": "claim", "title": "We instantiate this formulation with a generative behavior model", "path": "vault/memory/claim/claim_215a419e0f318ce8fbad6627.md", "status": "working", "source_ids": ["source_8aa5e06bac422cb3319b94e6"], "snippet": "# We instantiate this formulation with a [generative] behavior model\n\nWe instantiate this formulation with a [generative] behavior model", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9a6e63428ed93e1a99ea4c4d"}
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
- Extraction：`extraction_dfb859e53fae61aa66a0c3f5`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_latent_space_intervention_adaptation-生成策略的潜空间干预适应.md
@@ -0,0 +1,20 @@
+---
+id: "concept_latent_space_intervention_adaptation"
+type: "concept"
+status: "proposal"
+title: "生成策略的潜空间干预适应"
+created_at: "2026-07-19T12:19:04+08:00"
+updated_at: "2026-07-19T12:19:04+08:00"
+aliases: ["latent-space intervention adaptation", "noise-space policy adaptation", "FlowDAgger"]
+tags: []
+domains: ["embodied-ai", "robot-learning", "human-in-the-loop", "generative-policy"]
+confidence: "medium"
+source_ids: ["source_9a6e63428ed93e1a99ea4c4d"]
+relations: [{"type": "derived_from", "target_id": "source_9a6e63428ed93e1a99ea4c4d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都冻结生成主干并增加轻量部署模块；动作评估蒸馏负责候选排序，潜空间干预适应则从人类纠正学习如何改变生成噪声。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都保留冻结 VLA 的已有能力；Harness VLA 在外部原语/规划层重组行为，FlowDAgger 在生成潜变量层内转向行为。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "depends_on", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "该方法需要部署时捕获状态、人的纠正动作和对应策略执行，以形成可训练的干预对；可记录的真机迭代闭环是其数据入口。", "confidence": "medium", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_9a6e63428ed93e1a99ea4c4d"
+uncertainty: "适应能力受基础策略动作流形支持范围约束，并依赖人类干预的覆盖与一致性；高度多模态或病态生成动力学会降低反演保真度。"
+---
+
+# 生成策略的潜空间干预适应
+
+把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。
```
