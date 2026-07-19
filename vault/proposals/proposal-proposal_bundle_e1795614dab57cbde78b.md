---
id: "proposal_bundle_e1795614dab57cbde78b"
type: "proposal"
status: "migrated"
title: "Compile bundle：Robostral Navigate: single-camera AI navigation | Mistral AI"
created_at: "2026-07-19T17:17:03+08:00"
updated_at: "2026-07-19T17:17:04+08:00"
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
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_34abf7a170a7e0fc0492fc16", "target_path": "vault/knowledge/concepts/concept_34abf7a170a7e0fc0492fc16-指向式视觉导航接口.md", "base_sha256": null, "candidate_sha256": "9f3cf1f163198a887dc141f9e56cea83e61cf63a0a954be1d5df43530f62d959", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_e1795614dab57cbde78b-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md", "working_at": "2026-07-19T17:17:04+08:00"}]
existing_context: [{"id": "input_a318de5517033fc7e9a86795", "type": "input", "title": "Robostral Navigate: single-camera AI navigation | Mistral AI", "path": "vault/inputs/input-input_a318de5517033fc7e9a86795.md", "status": "active", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "…single-camera AI navigation | [Mistral] AI\n\nInput Episode for `source_886372de22c708b28cd11e4b`. The immutable Source remains authoritative.\n\n# Robostral Navigate…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_886372de22c708b28cd11e4b"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：Robostral Navigate: single-camera AI navigation | Mistral AI

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_7d905139e0a50f16e1e11ac6`
- 编译前召回已有对象：1
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_34abf7a170a7e0fc0492fc16-指向式视觉导航接口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_34abf7a170a7e0fc0492fc16"
+type: "concept"
+status: "proposal"
+title: "指向式视觉导航接口"
+created_at: "2026-07-19T17:17:03+08:00"
+updated_at: "2026-07-19T17:17:03+08:00"
+aliases: ["Pointing-Based Visual Navigation Interface", "Visual Pointing Navigation", "单目指向导航", "Robostral Navigate"]
+tags: []
+domains: ["embodied-ai", "visual-navigation", "robot-interface"]
+confidence: "low"
+source_ids: ["source_886372de22c708b28cd11e4b"]
+relations: [{"type": "derived_from", "target_id": "source_886372de22c708b28cd11e4b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "claim_via_interface_first_robot_control_20260715", "reason": "二者都使用可观察视觉目标接口形成闭环，但一个是专用导航动作表示，另一个是通用 Agent 的仿真工具控制。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_886372de22c708b28cd11e4b"
+reflection_context: {"reflection_ids": ["reflection_6a9092352b95c1ab440d2274"], "importance": "medium", "changed_belief": "此前容易把导航鲁棒性主要归因于更多传感器或更大模型；该材料提示视觉坐标系中的指向接口本身就是一种跨相机与跨本体归纳偏置。", "surprising": "官方页面报告单 RGB、仿真训练的 8B 模型在 R2R-CE validation unseen 达到 76.6%，但真实环境泛化叙述来自厂商页面，尚需独立论文与评测核验。", "connections": [{"shared_mechanism": "都把机器人控制转换为模型可观察、可反复修正的视觉目标接口", "boundary": "连接只覆盖视觉接口与闭环更新，不把专用导航策略等同于通用视觉 Agent 工具控制", "difference": "Robostral 直接预测图像目标点和局部位移，VIA 由通用 Agent 通过显式工具设置并执行虚拟夹爪 waypoint"}], "open_questions": ["指向与局部位移的切换条件能否用不确定性或可见性显式校准？"]}
+---
+
+# 指向式视觉导航接口
+
+导航策略优先在当前 RGB 图像中预测目标位置与到达朝向，用视觉坐标减少对相机内参和世界尺度的依赖；当目标不可见时，再回退到机器人局部坐标位移。
```
