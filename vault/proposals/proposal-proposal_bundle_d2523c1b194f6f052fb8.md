---
id: "proposal_bundle_d2523c1b194f6f052fb8"
type: "proposal"
status: "migrated"
title: "Compile bundle：全身智能：迈向人形基础模型 | Archon Robotics | Archon Robotics"
created_at: "2026-08-03T18:19:21+08:00"
updated_at: "2026-08-03T18:19:22+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b6445078b10e858d8d6d3f94"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "全身智能：迈向人形基础模型 | Archon Robotics | Archon Robotics"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_8c85ae8ecdde564e6b13f24a"
input_sha256: "745d5ec0097d2d8a392a54f96a4c0551b8d73274106460128250cece4c17b884"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_9337306ba824767665ce40c4", "target_path": "vault/knowledge/concepts/concept_9337306ba824767665ce40c4-人形基础模型的分层预训练-执行栈-layered-pretraining-to-execution-stack-for-huma.md", "base_sha256": null, "candidate_sha256": "6ac974aa6ee4d0afc78dd268c9a244ced58cf3afacb788457d460247c30a8ea5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_d2523c1b194f6f052fb8-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_9337306ba824767665ce40c4.md", "working_at": "2026-08-03T18:19:22+08:00"}]
existing_context: [{"id": "input_821cff7088c50d54f4596592", "type": "input", "title": "全身智能：迈向人形基础模型 | Archon Robotics | Archon Robotics", "path": "vault/inputs/input-input_821cff7088c50d54f4596592.md", "status": "active", "source_ids": ["source_b6445078b10e858d8d6d3f94"], "snippet": "# 全身智能：迈向人形基础模型 | [Archon] Robotics | [Archon] Robotics\n\nInput Episode for `source_b6445078b10e858d8d6d3f94`. The immutable Source remains authoritative.\n\n# 全身智能：迈向人形基础模型…", "match_reason": "metadata:title"}, {"id": "input_ced7182acd54cc772f9868c7", "type": "input", "title": "Gemini Robotics ER 2", "path": "vault/inputs/input-input_ced7182acd54cc772f9868c7.md", "status": "active", "source_ids": ["source_4ef330780a196b3bf1fdfc2c"], "snippet": "# Gemini [Robotics] ER 2\n\nInput Episode for `source_4ef330780a196b3bf1fdfc2c`. The immutable Source remains authoritative.\n\n# Gemini [Robotics] ER 2…", "match_reason": "metadata:title"}, {"id": "reflection_3ea617cf483f3d85a6aa4d31", "type": "reflection", "title": "Xiaomi-Robotics-1：状态转换语言把可扩展轨迹预训练接到机器人指令", "path": "vault/reflections/reflection-reflection_3ea617cf483f3d85a6aa4d31.md", "status": "active", "source_ids": ["source_5df8ebbcd9bd1afec33d46cc"], "snippet": "# Xiaomi-[Robotics]-1：状态转换语言把可扩展轨迹预训练接到机器人指令\n\n## Why important\n\n该工作把大规模 UMI 轨迹的自动状态转换标注与跨本体后训练明确分成两个接口：先学习从观察和目标状态描述生成动作，再对齐真实机器人及人类常用的祈使指令。它为“扩大数据量”提供了可检查的语义桥接，而不是把非机器人轨迹直接等同于可部署机器人示范。\n\n## What changed\n\n此前容易把…", "match_reason": "metadata:title"}, {"id": "reflection_bfb923cbbf75ed8a49f9df44", "type": "reflection", "title": "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎", "path": "vault/reflections/reflection-reflection_bfb923cbbf75ed8a49f9df44.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "# Xiaomi-[Robotics]-U0：世界基础模型可同时承担具身生成器与数据引擎\n\n## Why important\n\nU0 不把世界基础模型窄化为单一机器人视频预测器，而是联合保持通用图像生成、编辑、多视角具身场景、跨本体 transfer 和具身视频生成，使生成能力能直接扩充策略训练分布。\n\n## What changed\n\n此前常把具身…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b6445078b10e858d8d6d3f94"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "fc3307487966e5e12f0718c2cb377a330c6780b6edf75e7edbc59420c45893c5"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：全身智能：迈向人形基础模型 | Archon Robotics | Archon Robotics

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_8c85ae8ecdde564e6b13f24a`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_9337306ba824767665ce40c4-人形基础模型的分层预训练-执行栈-layered-pretraining-to-execution-stack-for-huma.md
@@ -0,0 +1,20 @@
+---
+id: "concept_9337306ba824767665ce40c4"
+type: "concept"
+status: "proposal"
+title: "人形基础模型的分层预训练—执行栈 / Layered pretraining-to-execution stack for humanoid foundation models"
+created_at: "2026-08-03T18:19:21+08:00"
+updated_at: "2026-08-03T18:19:21+08:00"
+aliases: ["Whole-Body Intelligence", "WBI", "Large Humanoid Model", "LHM", "全身智能", "人形基础模型"]
+tags: []
+domains: ["humanoid-robotics", "foundation-models", "whole-body-control", "pretraining", "embodied-ai"]
+confidence: "medium"
+source_ids: ["source_b6445078b10e858d8d6d3f94"]
+relations: [{"type": "derived_from", "target_id": "source_b6445078b10e858d8d6d3f94", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "depends_on", "target_id": "concept_8f8ae7b5cac6690d2e341d40", "reason": "S0.5/S0 的可复用身体先验依赖规模化全身运动跟踪及参考动作数量—多样性的协同扩展，但该先验本身不提供 S1/S2 语义能力。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都利用跨本体视觉语言状态与动作数据；WBI 分层进一步把共享的 S1 表示和本体专属的 S0.5/S0 执行边界显式分开。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_fc70bfc09ac7d9473592f09c", "reason": "部分运动学嵌入是 S0.5 类型接口的一种具体候选：它把全身冗余压缩为可导航 latent，再由低层执行器保证动力学可行。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_b6445078b10e858d8d6d3f94"
+reflection_context: {"reflection_ids": ["reflection_3c1d1a7a941f516e8b0aca44"], "importance": "high", "changed_belief": "我原先更容易把人形 foundation model 视为扩大动作空间的 VLA；该文章提示，foundation 属性还取决于身体先验、意图到参考运动的中间接口、硬件约束和失败回流能否被共同预训练与持续改进。", "surprising": "文章明确把 S0.5 单列为 motion generation + BFM 的转换层：它既不是高层语义模型的缩小版，也不是低层控制器，而是把动作意图变成具身可执行参考运动的接口。", "connections": [{"shared_mechanism": "该分层栈与 concept_8f8ae7b5cac6690d2e341d40 都把大规模 motion tracking/BFM 视为可复用身体先验。", "boundary": "BFM 的扩展证据只支持运动跟踪预训练，不自动提供任务语义、感知 grounding 或长程规划。", "difference": "既有节点解释 BFM 数量与多样性的协同扩展；这里把 BFM 放在 S0.5/S0 接口，并要求它接受 S1 意图、输出可安全跟踪参考。"}, {"shared_mechanism": "该分层栈与 concept_generalist_cross_embodiment_vla 都需要从异构人类与机器人数据学习可迁移表示，同时保留本体专属执行边界。", "boundary": "跨本体共享不能消除接触、动力学、传感器和硬件安全差异。", "difference": "跨本体 VLA 节点聚焦统一视觉语言状态到动作接口；全身智能栈进一步显式分离任务语义、原生人形策略、运动生成和高频控制。"}], "open_questions": ["S1 输出到 S0.5 的 action chunk、motion token 或约束接口，应如何同时保留任务可组合性、接触可执行性和不同人形硬件的迁移边界？"]}
+---
+
+# 人形基础模型的分层预训练—执行栈 / Layered pretraining-to-execution stack for humanoid foundation models
+
+把人形 foundation model 定义为跨层预训练与执行体系：S2 将开放任务转成语义阶段目标与安全约束；S1 以视觉、语言、本体、触觉和历史状态生成原生全身动作意图；S0.5 用 motion generation 与行为基础模型把意图变成结合当前物理状态的参考运动；S0 在平衡、接触、力、关节和低延迟约束下高频跟踪。人类数据提供行为规模，机器人与硬件数据限定可执行边界，仿真、失败和部署日志支撑覆盖、恢复和持续后训练。该分层是 Archon 提出的研究路线而非已验证行业标准；跨层接口、统一训练目标、硬件迁移和整栈泛化仍需受控实验。
```
