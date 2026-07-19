---
id: "proposal_bundle_05825e7660f5c3cb11c6"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:17:50+08:00"
updated_at: "2026-07-19T12:17:50+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_c46b1e0305ec5c9adba634f1"]
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
extraction_id: "extraction_57d107ab4768f3b55bfc9b78"
input_sha256: "9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_portable_embodied_inference_runtime", "target_path": "vault/knowledge/concepts/concept_portable_embodied_inference_runtime-可移植具身推理运行时.md", "base_sha256": null, "candidate_sha256": "490f798522d7604442ff846066c16198c3068d1c6eb980268ca009360e423e2a", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_05825e7660f5c3cb11c6-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_portable_embodied_inference_runtime.md", "working_at": "2026-07-19T12:17:50+08:00"}]
existing_context: [{"id": "concept_end_to_end_embodied_reproducibility", "type": "concept", "title": "端到端具身系统可复现性", "path": "vault/memory/concept/concept_end_to_end_embodied_reproducibility.md", "status": "working", "source_ids": ["source_650f616f1e641912e73115b1"], "snippet": "# 端到端具身系统可复现性\n\n把机械设计与物料清单、低层控制、数据转换、训练配方和推理部署视为同一可复现边界；只开放模型权重或微调代码不足以复现实机具身系统。", "match_reason": "metadata:aliases"}, {"id": "claim_6ed5013981fdc75c87eb19c9", "type": "claim", "title": "real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×", "path": "vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving [inference]…", "match_reason": "metadata:title"}, {"id": "claim_3e9ebe96416b051f59f5eb91", "type": "claim", "title": "Experimental results in simulation", "path": "vault/memory/claim/claim_3e9ebe96416b051f59f5eb91.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Experimental results in simulation\n\nExperimental results in simulation", "match_reason": "metadata:domains"}, {"id": "claim_4a4e2ea931565f8ab567e75e", "type": "claim", "title": "GR00T-N1.6, respectively.", "path": "vault/memory/claim/claim_4a4e2ea931565f8ab567e75e.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# GR00T-N1.6, respectively.\n\nGR00T-N1.6, respectively.", "match_reason": "metadata:domains"}, {"id": "concept_vla_action_cache_refinement", "type": "concept", "title": "VLA 动作缓存与上下文复用", "path": "vault/memory/concept/concept_vla_action_cache_refinement.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "match_reason": "metadata:domains"}, {"id": "claim_0534c95e4004502bb928fc9e", "type": "claim", "title": "34.43× for representative flow-based VLA models, π0.5", "path": "vault/memory/claim/claim_0534c95e4004502bb928fc9e.md", "status": "working", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# 34.43× for representative flow-based VLA models, π0.5\n\n34.43× for representative flow-based VLA models…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_c46b1e0305ec5c9adba634f1"}
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
- Extraction：`extraction_57d107ab4768f3b55bfc9b78`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_portable_embodied_inference_runtime-可移植具身推理运行时.md
@@ -0,0 +1,20 @@
+---
+id: "concept_portable_embodied_inference_runtime"
+type: "concept"
+status: "proposal"
+title: "可移植具身推理运行时"
+created_at: "2026-07-19T12:17:50+08:00"
+updated_at: "2026-07-19T12:17:50+08:00"
+aliases: ["portable embodied inference runtime", "embodied AI inference runtime", "multi-rate embodied runtime"]
+tags: []
+domains: ["embodied-ai", "robotics", "inference-runtime", "edge-deployment"]
+confidence: "medium"
+source_ids: ["source_c46b1e0305ec5c9adba634f1"]
+relations: [{"type": "derived_from", "target_id": "source_c46b1e0305ec5c9adba634f1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "part_of", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "可复现具身全栈必须包含从检查点到异构边缘设备闭环执行的明确运行时边界。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "Embodied.cpp 将 VLA 与 WAM 的共享执行路径放入稳定核心、把动作头和预测模块插件化，为双系统模型的多速率部署提供运行时结构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_c46b1e0305ec5c9adba634f1"
+uncertainty: "论文给出两种 VLA 的闭环结果；WAM 证据仅是单个 Transformer block 的量化微基准，尚不是完整 WAM 闭环验证。"
+---
+
+# 可移植具身推理运行时
+
+面向闭环机器人控制的统一运行时契约：以多速率组件调度、低时延低抖动的 batch-1 执行、可插拔模型头与具身 I/O，把稳定推理核心和模型/机器人专属适配分离。
```
