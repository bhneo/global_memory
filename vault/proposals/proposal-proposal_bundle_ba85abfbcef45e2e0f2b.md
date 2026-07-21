---
id: "proposal_bundle_ba85abfbcef45e2e0f2b"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.09218v2.pdf"
created_at: "2026-07-20T12:39:23+08:00"
updated_at: "2026-07-20T12:39:23+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e8cc1290fdb80e80f77ba2c2"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-c-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.09218v2.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_993dd33a71685f6fb1614a34"
input_sha256: "419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_2d8e08b8d8ace05431e064a0", "target_path": "vault/knowledge/concepts/concept_2d8e08b8d8ace05431e064a0-接触中心的混合预测控制.md", "base_sha256": null, "candidate_sha256": "77ee589accea5146168f050f1639cb57eea47e24b56db71be6d56d9a723e10c1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_ba85abfbcef45e2e0f2b-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "working_at": "2026-07-20T12:39:23+08:00"}]
existing_context: [{"id": "input_680e14163f51a60d9a5da0fb", "type": "input", "title": "2607.09218v2.pdf", "path": "vault/inputs/input-input_680e14163f51a60d9a5da0fb.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.09218v2.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/41/9b/419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source remains authoritative.\n\n# TouchWorld: A Predictive and Reactive Tactile F", "match_reason": "full-text:body"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e8cc1290fdb80e80f77ba2c2"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.09218v2.pdf

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-c-20260720`
- Extraction：`extraction_993dd33a71685f6fb1614a34`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_2d8e08b8d8ace05431e064a0-接触中心的混合预测控制.md
@@ -0,0 +1,20 @@
+---
+id: "concept_2d8e08b8d8ace05431e064a0"
+type: "concept"
+status: "proposal"
+title: "接触中心的混合预测控制"
+created_at: "2026-07-20T12:39:23+08:00"
+updated_at: "2026-07-20T12:39:23+08:00"
+aliases: ["Contact-centric hybrid predictive control", "TACTIC", "whole-arm contact MPC"]
+tags: []
+domains: ["embodied-ai", "tactile-control", "whole-arm-manipulation", "mpc"]
+confidence: "high"
+source_ids: ["source_e8cc1290fdb80e80f77ba2c2"]
+relations: [{"type": "derived_from", "target_id": "source_e8cc1290fdb80e80f77ba2c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "二者都分开处理未来接触预测与快速触觉修正；TACTIC 采用混合 MPC，后者采用分层神经控制。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_e8cc1290fdb80e80f77ba2c2"
+reflection_context: {"reflection_ids": ["reflection_4b63a8834e11b28db3cf2fdc"], "importance": "high", "changed_belief": "此前触觉控制容易被描述为学习一个 visuotactile policy；该工作提示，在稀疏多接触数据下，可靠控制还需要把分析运动学用于可行性，把学习模型用于接触形成与断裂，并在采样阶段主动偏向能调节接触力的方向。", "surprising": "接触 Jacobian 不只是 cost 项，而被直接用于塑形每个 MPC step 的动作扰动，使探索及时对当前接触法向敏感。", "connections": [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉既用于预测未来接触，也用于即时动作修正。", "boundary": "TACTIC 不提供形式安全保证，真实实验使用 mannequin 和 custom exoskeleton 数据；面向真人护理仍需舒适性、安全栈与受试者验证。", "difference": "多时间尺度触觉世界模型强调分层神经控制回路；TACTIC 用 sampling-based MPC、contact Jacobian 和 learned latent dynamics 形成显式混合规划器。"}], "open_questions": ["接触形成/断裂不确定性如何传播到 MPC 风险，而不只以平均预测力进入 cost？"]}
+---
+
+# 接触中心的混合预测控制
+
+把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics 预测接触形成与力演化。它降低稀疏多接触数据下的物理不一致，但不构成形式安全保证。
```
