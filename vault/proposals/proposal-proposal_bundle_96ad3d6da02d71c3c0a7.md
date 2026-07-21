---
id: "proposal_bundle_96ad3d6da02d71c3c0a7"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T11:56:21+08:00"
updated_at: "2026-07-20T11:56:21+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_6506a11d8f50ef2494f8b80e"
input_sha256: "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_abb38fe58cbeee09ce87a01d", "target_path": "vault/knowledge/concepts/concept_abb38fe58cbeee09ce87a01d-跨轨迹任务进度代理校正.md", "base_sha256": null, "candidate_sha256": "4f4115e29baa8e8ece55d4d0f31ea51d688c4395bfbbd29f5b736d63216ca0ac", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_96ad3d6da02d71c3c0a7-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "working_at": "2026-07-20T11:56:21+08:00"}]
existing_context: [{"id": "reflection_052db872e2258b0e016c5ebf", "type": "reflection", "title": "UR-VC：先纠正进度代理，再训练价值或优势条件策略", "path": "vault/reflections/reflection-reflection_052db872e2258b0e016c5ebf.md", "status": "active", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# [UR-VC]：先纠正进度代理，再训练价值或优势条件策略\n\n## Why important\n\n它指出成功示范中的归一化时间并不等于物理进度，尤其接触和可变形物体任务会倒退、停滞或速度不均；错误代理会污染后续价值与优势监督。\n\n## What changed\n\n价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n\n## Surprising\n\n[UR]…", "match_reason": "metadata:title"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…mechanism\": \"Robo-ValueRL 与 [UR-VC] 都先提高进度或价值信号的可靠性，再让该信号参与策略改进。\",\n    \"boundary\": \"该连接只说明信号治理的共同位置，不表示训练式价值估计和无训练标签校正在方法或证据上等价。\",\n    \"difference\": \"[UR-VC] 校正离线时间代理；Robo-ValueRL 学习历史条件价值并延伸到在线数据筛选…", "match_reason": "full-text:body"}, {"id": "concept_d7111f304971448401a57f3b", "type": "concept", "title": "冻结技能库与轻量路由适应", "path": "vault/memory/concept/concept_d7111f304971448401a57f3b.md", "status": "working", "source_ids": ["source_d83bb2c45bcaf70906e9ac96"], "snippet": "# 冻结技能库与轻量路由适应\n\n从多任务示范中学习紧凑、可复用且尽量非冗余的技能库，在迁移时冻结技能表示，只更新轻量路由器和动作头，以减少新任务少样本适应所需的参数与数据。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e326446389e083c6ba9c94c2"}
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

- Provider：`codex-gpt56-m91-vla-posttraining-weekly-20260720`
- Extraction：`extraction_6506a11d8f50ef2494f8b80e`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_abb38fe58cbeee09ce87a01d-跨轨迹任务进度代理校正.md
@@ -0,0 +1,20 @@
+---
+id: "concept_abb38fe58cbeee09ce87a01d"
+type: "concept"
+status: "proposal"
+title: "跨轨迹任务进度代理校正"
+created_at: "2026-07-20T11:56:21+08:00"
+updated_at: "2026-07-20T11:56:21+08:00"
+aliases: ["UR-VC", "Unsupervised Robotic Value Correction", "time-derived progress correction"]
+tags: []
+domains: ["embodied-ai", "vla", "value-learning", "progress-estimation"]
+confidence: "high"
+source_ids: ["source_e326446389e083c6ba9c94c2"]
+relations: [{"type": "derived_from", "target_id": "source_e326446389e083c6ba9c94c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_e326446389e083c6ba9c94c2"
+reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？"]}
+---
+
+# 跨轨迹任务进度代理校正
+
+跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。
```
