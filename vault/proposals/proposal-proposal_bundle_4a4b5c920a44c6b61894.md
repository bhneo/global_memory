---
id: "proposal_bundle_4a4b5c920a44c6b61894"
type: "proposal"
status: "migrated"
title: "Compile bundle：Robostral Navigate: single-camera AI navigation | Mistral AI"
created_at: "2026-07-19T22:43:39+08:00"
updated_at: "2026-07-19T22:43:40+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_886372de22c708b28cd11e4b"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "Robostral Navigate: single-camera AI navigation | Mistral AI"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_7d905139e0a50f16e1e11ac6"
input_sha256: "8b9a83153e214570a7db447dd3bd88f7d76d8cd0383448bf21d37baa09c30939"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_34abf7a170a7e0fc0492fc16", "target_path": "vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md", "base_sha256": "fb84ae26a30e2bb2ba49918be337d0c62b69ca0cd45cbd930b4fd48242ef6b9f", "candidate_sha256": "78ad7d03680591b9a6178e09e2ede1860b539e5283a9eec2c4cebeee085f0cc8", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_4a4b5c920a44c6b61894-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_4a4b5c920a44c6b61894-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "input_a318de5517033fc7e9a86795", "type": "input", "title": "Robostral Navigate: single-camera AI navigation | Mistral AI", "path": "vault/inputs/input-input_a318de5517033fc7e9a86795.md", "status": "active", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "…single-camera AI navigation | [Mistral] AI\n\nInput Episode for `source_886372de22c708b28cd11e4b`. The immutable Source remains authoritative.\n\n# Robostral Navigate…", "match_reason": "metadata:title"}, {"id": "reflection_6a9092352b95c1ab440d2274", "type": "reflection", "title": "Robostral Navigate：动作接口选择可以降低传感与本体耦合", "path": "vault/reflections/reflection-reflection_6a9092352b95c1ab440d2274.md", "status": "active", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "# Robostral Navigate：动作接口选择可以降低传感与本体耦合\n\n## Why important\n\n它把单目导航的泛化部分归因于动作表达：优先预测当前图像中的目标点与到达朝向，在目标不在视野时才回退到局部坐标位移，从而减少对相机内参、世界尺度和特定底盘的耦合。\n\n## What changed\n\n此前容易把导航鲁棒性主要归因于更多传感器或更大模型；该材料提示视觉坐标系中的指向接口本身就是一种跨相机与跨本体归纳偏置。\n\n## Surprising\n\n官方页面报告单 RGB、仿真训练的…", "match_reason": "metadata:domains"}, {"id": "concept_34abf7a170a7e0fc0492fc16", "type": "concept", "title": "指向式视觉导航接口", "path": "vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md", "status": "working", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "# 指向式视觉导航接口\n\n导航策略优先在当前 RGB 图像中预测目标位置与到达朝向，用视觉坐标减少对相机内参和世界尺度的依赖；当目标不可见时，再回退到机器人局部坐标位移。", "match_reason": "metadata:aliases"}, {"id": "synthesis_77d12a9c578c8e5a6223bff4", "type": "synthesis", "title": "具身泛化中的中间表示、接口解耦与动作落差", "path": "vault/synthesis/synthesis-synthesis_77d12a9c578c8e5a6223bff4.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277", "source_61f3045b170e78e4adb2422c", "source_886372de22c708b28cd11e4b", "source_be9781ec8ca637c5dfd8fabb", "source_d83bb2c45bcaf70906e9ac96"], "snippet": "…却可能把执行差异推迟到动作头，使最终控制仍受少量机器人数据限制。\n- 自适应计算、技能路由和接口回退都需要可靠停止或失效信号；如果信号未校准，系统可能在困难状态过早压缩或继续复用错误结构。\n- 本周材料的证据成熟度不一致：四篇为论文或预印本，[Robostral] 的主要结果来自厂商页面，跨来源综合不能消除这一来源差异。\n\n## Candidate hypotheses\n\n[\n  {\n    \"statement\": \"在跨本体机器人学习中，将任务相关世界/视觉表示与本体特定动作解码显式分离，比仅扩大共享端到端动作解码器更能提高未见本体迁移…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_886372de22c708b28cd11e4b"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Robostral Navigate: single-camera AI navigation | Mistral AI

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_7d905139e0a50f16e1e11ac6`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md
+++ candidate:vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_34abf7a170a7e0fc0492fc16"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "指向式视觉导航接口"
 created_at: "2026-07-19T17:17:03+08:00"
-updated_at: "2026-07-19T17:17:04+08:00"
+updated_at: "2026-07-19T22:43:39+08:00"
 aliases: ["Pointing-Based Visual Navigation Interface", "Visual Pointing Navigation", "单目指向导航", "Robostral Navigate"]
 tags: []
 domains: ["embodied-ai", "visual-navigation", "robot-interface"]
 confidence: "low"
 source_ids: ["source_886372de22c708b28cd11e4b"]
-relations: [{"type": "derived_from", "target_id": "source_886372de22c708b28cd11e4b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "claim_via_interface_first_robot_control_20260715", "reason": "二者都使用可观察视觉目标接口形成闭环，但一个是专用导航动作表示，另一个是通用 Agent 的仿真工具控制。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_886372de22c708b28cd11e4b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "claim_via_interface_first_robot_control_20260715", "reason": "二者都使用可观察视觉目标接口形成闭环，但一个是专用导航动作表示，另一个是通用 Agent 的仿真工具控制。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "claim_via_interface_first_robot_control_20260715", "reason": "二者都使用可观察视觉目标接口形成闭环，但一个是专用导航动作表示，另一个是通用 Agent 的仿真工具控制。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_886372de22c708b28cd11e4b"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_6a9092352b95c1ab440d2274"], "importance": "medium", "changed_belief": "此前容易把导航鲁棒性主要归因于更多传感器或更大模型；该材料提示视觉坐标系中的指向接口本身就是一种跨相机与跨本体归纳偏置。", "surprising": "官方页面报告单 RGB、仿真训练的 8B 模型在 R2R-CE validation unseen 达到 76.6%，但真实环境泛化叙述来自厂商页面，尚需独立论文与评测核验。", "connections": [{"shared_mechanism": "都把机器人控制转换为模型可观察、可反复修正的视觉目标接口", "boundary": "连接只覆盖视觉接口与闭环更新，不把专用导航策略等同于通用视觉 Agent 工具控制", "difference": "Robostral 直接预测图像目标点和局部位移，VIA 由通用 Agent 通过显式工具设置并执行虚拟夹爪 waypoint"}], "open_questions": ["指向与局部位移的切换条件能否用不确定性或可见性显式校准？"]}
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
-origin_proposal_id: "proposal_bundle_e1795614dab57cbde78b"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_e1795614dab57cbde78b-concept-1.md"
-origin_candidate_sha256: "9f3cf1f163198a887dc141f9e56cea83e61cf63a0a954be1d5df43530f62d959"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 指向式视觉导航接口
```
