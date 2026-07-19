---
id: "proposal_bundle_73e6e7e0950651801331"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T22:43:05+08:00"
updated_at: "2026-07-19T22:43:05+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_be9781ec8ca637c5dfd8fabb"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_28adad28f4cf31860cfdac98"
input_sha256: "0e618ede28c928da76ff6a782d3c9bdb0c739977526ad749c8284a2be7ec895d"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_0c7884679bf6d4e1287ce225", "target_path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "base_sha256": "54ee0a364009174df6afa014f5f30c89df69e35cf7524406cebe1a8d9d8a0172", "candidate_sha256": "72a6b7382f6c60cdfc059fbc56642d39fe7aee6978a11a559ed9fb1eeef96b05", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_73e6e7e0950651801331-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_73e6e7e0950651801331-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# Latent Memory Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:domains"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:aliases"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:aliases"}, {"id": "experiment_7101e03fb065226e65f388a5", "type": "experiment", "title": "Cursor M7 真实读取与 receipt 回写验收", "path": "vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md", "status": "working", "source_ids": ["source_113d589e6dadf14b5fa8edea"], "snippet": "# Cursor M7 真实读取与 receipt 回写验收\n\n## 验收路径\n\nCursor 按协议读取了 `AGENTS.md`、`.cursor/rules/global-[memory].mdc` 和 `vault/INDEX…", "match_reason": "metadata:domains"}, {"id": "experiment_b6f1e1956690ac08fd56a5da", "type": "experiment", "title": "Codex M7 真实读取与 receipt 回写验收", "path": "vault/memory/experiment/experiment_b6f1e1956690ac08fd56a5da.md", "status": "working", "source_ids": ["source_46d0aad5afd18dd21899796f"], "snippet": "# Codex M7 真实读取与 receipt 回写验收\n\n## 验收路径\n\nCodex 按 `vault/INDEX.md` 的入口执行了真实的 `gm context → task → receipt → proposal` 流程…", "match_reason": "metadata:domains"}, {"id": "concept_adaptive_interleaved_multimodal_planning", "type": "concept", "title": "自适应交错多模态规划", "path": "vault/memory/concept/concept_adaptive_interleaved_multimodal_planning.md", "status": "working", "source_ids": ["source_4ac7cf9f4fce43551683a04b"], "snippet": "# 自适应交错多模态规划\n\n长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_be9781ec8ca637c5dfd8fabb"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_28adad28f4cf31860cfdac98`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md
+++ candidate:vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_0c7884679bf6d4e1287ce225"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "控制策略的自适应潜空间推理"
 created_at: "2026-07-19T17:16:26+08:00"
-updated_at: "2026-07-19T17:16:26+08:00"
+updated_at: "2026-07-19T22:43:05+08:00"
 aliases: ["Adaptive Latent Reasoning for Control", "自适应潜推理控制", "Latent Memory Palace", "LMP"]
 tags: []
 domains: ["embodied-ai", "robot-control", "latent-reasoning"]
 confidence: "medium"
 source_ids: ["source_be9781ec8ca637c5dfd8fabb"]
-relations: [{"type": "derived_from", "target_id": "source_be9781ec8ca637c5dfd8fabb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者分别在动作前内部推理和动作后执行阶段自适应分配预算，构成不同控制层的可变计算时域。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_be9781ec8ca637c5dfd8fabb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者分别在动作前内部推理和动作后执行阶段自适应分配预算，构成不同控制层的可变计算时域。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者分别在动作前内部推理和动作后执行阶段自适应分配预算，构成不同控制层的可变计算时域。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_be9781ec8ca637c5dfd8fabb"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_12ec24dd673a937d90f5bc21"], "importance": "high", "changed_belief": "此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数。", "surprising": "同一套自回归潜变量框架还可产生可变长度动作 tokenizer，暗示推理长度与动作分段可能由共同的表示机制控制。", "connections": [{"shared_mechanism": "都根据当前状态与任务难度动态分配有限的计算或执行预算", "boundary": "连接只适用于自适应预算分配，不表示内部推理步数与外部动作执行时域等价", "difference": "LMP 调整动作生成前的潜变量推断长度，动态执行时域调整动作生成后的开环执行长度"}], "open_questions": ["潜推理长度能否被校准为任务难度或失败风险的可靠信号？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_87d81cda9f050aeb5052"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_87d81cda9f050aeb5052-concept-1.md"
-origin_candidate_sha256: "a9bae0a81cbb64aeb9c26f0e3f63cf26700aafce0e02c9009cda603184b2c6e7"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 控制策略的自适应潜空间推理
```
