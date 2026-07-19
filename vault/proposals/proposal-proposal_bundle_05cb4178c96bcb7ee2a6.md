---
id: "proposal_bundle_05cb4178c96bcb7ee2a6"
type: "proposal"
status: "migrated"
title: "Compile bundle：GitHub - physical-superintelligence-lab/SIMPLE: Welcome to SIMPLE, a full-stack simulation environment for humanoid loco-manipulation, built on AMO/SONIC, with integrated support for mainstream VLAs s"
created_at: "2026-07-19T02:51:33+08:00"
updated_at: "2026-07-19T02:51:34+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d75524a9040845cdc76db35c"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56terra-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "GitHub - physical-superintelligence-lab/SIMPLE: Welcome to SIMPLE, a full-stack simulation environment for humanoid loco-manipulation, built on AMO/SONIC, with integrated support for mainstream VLAs s"
source_authority: "official"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_c95fb2886876446c4a8f8164"
input_sha256: "1a51243513029397b224711584cd8898e38ffe1ca160cf480d98c05f29d03a56"
bundle_items: [{"item_id": "architecture-1", "object_type": "architecture", "action": "create", "target_id": "architecture_simple_simulation_policy_loop", "target_path": "vault/action/architectures/architecture_simple_simulation_policy_loop-simple-仿真策略学习与评测环境.md", "base_sha256": null, "candidate_sha256": "17b5db0a1140481078beb2ef9698009ffd69263a2dda4417bacf64e5720ad87e", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_05cb4178c96bcb7ee2a6-architecture-1.md", "base_path": null, "working_path": "vault/memory/architecture/architecture_simple_simulation_policy_loop.md", "working_at": "2026-07-19T02:51:34+08:00"}, {"item_id": "question-2", "object_type": "question", "action": "create", "target_id": "question_38e811a8fb9e1894eed44b9d", "target_path": "vault/frontier/questions/question_38e811a8fb9e1894eed44b9d-simple-中的仿真评测在多大程度上预测真实机器人部署表现.md", "base_sha256": null, "candidate_sha256": "3f2fa259fe347827dcfd2527084d7080d3a33875201e7db42ea75cad502c2e9b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_05cb4178c96bcb7ee2a6-question-2.md", "base_path": null, "working_path": "vault/memory/question/question_38e811a8fb9e1894eed44b9d.md", "working_at": "2026-07-19T02:51:34+08:00"}]
existing_context: [{"id": "question_a6b5d595ace88e906de2e2f0", "type": "question", "title": "can the proxy labels themselves be corrected before", "path": "vault/memory/question/question_a6b5d595ace88e906de2e2f0.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "…UR-VC is\nbased on a [simple] data-driven premise: time-derived labels are\nnoisy mainly because each…", "match_reason": "full-text:body"}, {"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…Further, the agents\nare not trained with RL, but rather analytically compute these\nmeasures in [simple] grid-world…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 2, "source_id": "source_d75524a9040845cdc76db35c"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "official", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 2, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 2, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：GitHub - physical-superintelligence-lab/SIMPLE: Welcome to SIMPLE, a full-stack simulation environment for humanoid loco-manipulation, built on AMO/SONIC, with integrated support for mainstream VLAs s

## 编译边界

- Provider：`agent-semantic-daily-gpt56terra-v1`
- Extraction：`extraction_c95fb2886876446c4a8f8164`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### architecture-1 (create architecture)

```diff
--- /dev/null
+++ candidate:vault/action/architectures/architecture_simple_simulation_policy_loop-simple-仿真策略学习与评测环境.md
@@ -0,0 +1,20 @@
+---
+id: "architecture_simple_simulation_policy_loop"
+type: "architecture"
+status: "proposal"
+title: "SIMPLE 仿真策略学习与评测环境"
+created_at: "2026-07-19T02:51:33+08:00"
+updated_at: "2026-07-19T02:51:33+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "simulation", "vla", "humanoid"]
+confidence: "medium"
+source_ids: ["source_d75524a9040845cdc76db35c"]
+relations: [{"type": "derived_from", "target_id": "source_d75524a9040845cdc76db35c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "该环境提供将异构数据训练配方落到仿真数据生成、策略微调和评测的工程载体。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_sim_to_real_scene_infrastructure", "reason": "SIMPLE 使用大规模场景和任务进行策略学习与仿真评测，属于 Sim-to-Real 场景基础设施。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_d75524a9040845cdc76db35c"
+uncertainty: "仓库页面证明其功能范围，但不能单独证明仿真成绩能预测真实机器人表现。"
+---
+
+# SIMPLE 仿真策略学习与评测环境
+
+SIMPLE 是面向具身策略的数据生成、微调和仿真评测环境，覆盖多种机器人、场景资产和人形全身移动操作任务，并集成多类 VLA 与 World Action Model。
```

### question-2 (create question)

```diff
--- /dev/null
+++ candidate:vault/frontier/questions/question_38e811a8fb9e1894eed44b9d-simple-中的仿真评测在多大程度上预测真实机器人部署表现.md
@@ -0,0 +1,19 @@
+---
+id: "question_38e811a8fb9e1894eed44b9d"
+type: "question"
+status: "proposal"
+title: "SIMPLE 中的仿真评测在多大程度上预测真实机器人部署表现？"
+created_at: "2026-07-19T02:51:33+08:00"
+updated_at: "2026-07-19T02:51:33+08:00"
+aliases: []
+tags: []
+domains: ["embodied-ai", "simulation", "sim-to-real"]
+confidence: "unknown"
+source_ids: ["source_d75524a9040845cdc76db35c"]
+relations: [{"type": "derived_from", "target_id": "source_d75524a9040845cdc76db35c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}, {"type": "raises", "target_id": "tension_world_model_eval_action", "reason": "仿真或世界模型评测与真实动作结果之间可能存在系统性偏差。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56terra-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_d75524a9040845cdc76db35c"
+---
+
+# SIMPLE 中的仿真评测在多大程度上预测真实机器人部署表现？
+
+需要比较同一策略在 SIMPLE 与真实机器人上的任务成功率、失败类型和控制稳定性，才能判断仿真评测的外部有效性。
```
