---
id: "proposal_bundle_7b7646dd209401064c94"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:44:43+08:00"
updated_at: "2026-07-21T17:44:44+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-readmission-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_4dd99b2ac6f08ddbdd26b117"
input_sha256: "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_dual_protocol_hri_agent_execution_boundary", "target_path": "vault/knowledge/concepts/concept_dual_protocol_hri_agent_execution_boundary-人机客户端与-agent-执行的双协议边界.md", "base_sha256": null, "candidate_sha256": "1790ead5028a0cd26f7f8451eb32a7238d16ee11b34244083bf822bd9619428e", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_7b7646dd209401064c94-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_dual_protocol_hri_agent_execution_boundary.md", "working_at": "2026-07-21T17:44:44+08:00"}]
existing_context: [{"id": "reflection_bfb923cbbf75ed8a49f9df44", "type": "reflection", "title": "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎", "path": "vault/reflections/reflection-reflection_bfb923cbbf75ed8a49f9df44.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "# Xiaomi-[Robotics]-U0：世界基础模型可同时承担具身生成器与数据引擎\n\n## Why important\n\nU0 不把世界基础模型窄化为单一机器人视频预测器，而是联合保持通用图像生成、编辑、多视角具身场景、跨本体 transfer 和具身视频生成，使生成能力能直接扩充策略训练分布。\n\n## What changed\n\n此前常把具身…", "match_reason": "metadata:title"}, {"id": "claim_wechat_kairos_sim2real_training_20260716", "type": "claim", "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期", "path": "vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md", "status": "working", "source_ids": ["source_a20c5fb22d91216503d413e1"], "snippet": "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。", "match_reason": "metadata:tags"}, {"id": "concept_27970fb0de0d8995774e31f6", "type": "concept", "title": "多视角具身合成世界模型数据引擎", "path": "vault/memory/concept/concept_27970fb0de0d8995774e31f6.md", "status": "working", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "# 多视角具身合成世界模型数据引擎\n\n在保留通用图像与视频生成能力的同时，联合学习多视角具身场景、跨本体结构化编辑和具身视频，使世界基础模型既能预测交互也能生成受机器人与相机约束的策略训练数据。合成数据仍需通过几何、接触和闭环收益验证。", "match_reason": "metadata:aliases"}, {"id": "claim_wechat_embodied_eval_bottleneck_20260715", "type": "claim", "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住", "path": "vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md", "status": "working", "source_ids": ["source_2d4f3a7d3525782c8ff503ee"], "snippet": "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_structure_not_volume_20260716", "type": "claim", "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe", "path": "vault/memory/claim/claim_wechat_embodied_data_structure_not_volume_20260716.md", "status": "working", "source_ids": ["source_0a113baae7ce4d1ab78da1a3"], "snippet": "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_a0c7811ba12c9cf80bfd26c9"}
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

- Provider：`agent-semantic-daily-gpt56sol-readmission-v1`
- Extraction：`extraction_4dd99b2ac6f08ddbdd26b117`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_dual_protocol_hri_agent_execution_boundary-人机客户端与-agent-执行的双协议边界.md
@@ -0,0 +1,20 @@
+---
+id: "concept_dual_protocol_hri_agent_execution_boundary"
+type: "concept"
+status: "proposal"
+title: "人机客户端与 Agent 执行的双协议边界"
+created_at: "2026-07-21T17:44:43+08:00"
+updated_at: "2026-07-21T17:44:43+08:00"
+aliases: ["Dual-Protocol HRI and Agent Execution Boundary", "ACP-MCP Robot Architecture", "Agent-Client Protocol", "ACP", "人机交互双协议架构"]
+tags: []
+domains: ["agent-infrastructure", "human-robot-interaction", "mcp"]
+confidence: "medium"
+source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
+relations: [{"type": "derived_from", "target_id": "source_a0c7811ba12c9cf80bfd26c9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "双协议架构定义通信与授权边界，类型化技能图定义可验证执行结构；两者覆盖不同层级。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_a0c7811ba12c9cf80bfd26c9"
+reflection_context: {"reflection_ids": ["reflection_797e923d7a0e6ef67bb26728"], "importance": "high", "changed_belief": "可插拔 Agent 接入不仅需要工具协议，还需要独立的人机交互协议；否则 UI、授权和中断语义仍会与具体 Agent 实现耦合。", "surprising": "作者把原为编码 Agent 设计的 ACP 移植到机器人 HRI，并只在其原型架构上验证；这证明可行性而非实时安全、互操作成熟度或工业可靠性。", "connections": [{"shared_mechanism": "都把物理能力暴露为结构化服务，并保留高层可观察控制。", "boundary": "协议解耦不替代机器人侧安全控制、时限保证或动作验证。", "difference": "RPent 聚焦物理 Agent 基础设施和共享工作空间；ACP+MCP 架构明确拆分人机客户端、Agent 编排与执行协议。"}], "open_questions": ["ACP 的取消、授权和流式状态语义如何映射到不可瞬时中断的物理动作？"]}
+---
+
+# 人机客户端与 Agent 执行的双协议边界
+
+在三层机器人 Agent 架构中，以 Agent-Client Protocol（ACP）连接人类界面与推理 Agent，承载流式可观察性、显式授权和任务中断；以 Model Context Protocol（MCP）连接 Agent 与机器人能力服务。该分层降低 UI、推理器和平台的直接耦合，但协议层可行性不构成实时控制、安全停止或工业互操作保证。
```
