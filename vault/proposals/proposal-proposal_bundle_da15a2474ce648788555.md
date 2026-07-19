---
id: "proposal_bundle_da15a2474ce648788555"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T12:19:14+08:00"
updated_at: "2026-07-19T12:19:15+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b1f4ea371eb10f3bc7a0f532"]
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
extraction_id: "extraction_c4d48d9b61e5984deceecfde"
input_sha256: "69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_geometry_grounded_proprioception", "target_path": "vault/knowledge/concepts/concept_geometry_grounded_proprioception-几何落地的本体感觉视觉融合.md", "base_sha256": null, "candidate_sha256": "6b8590ab7025b8368790e060d598fa55e81761a6a63c0c217b35c081c863e94d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_da15a2474ce648788555-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_geometry_grounded_proprioception.md", "working_at": "2026-07-19T12:19:15+08:00"}]
existing_context: [{"id": "claim_375ec2bd655859372380b6b0", "type": "claim", "title": "then, we post-train a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.", "path": "vault/memory/claim/claim_375ec2bd655859372380b6b0.md", "status": "working", "source_ids": ["source_691f3acc1fe3382639690f59"], "snippet": "# then, we post-train a flow-based action expert on high-quality humanoid [robot] data to learn precise…", "match_reason": "metadata:title"}, {"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first [Robot] Control\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b1f4ea371eb10f3bc7a0f532"}
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
- Extraction：`extraction_c4d48d9b61e5984deceecfde`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_geometry_grounded_proprioception-几何落地的本体感觉视觉融合.md
@@ -0,0 +1,20 @@
+---
+id: "concept_geometry_grounded_proprioception"
+type: "concept"
+status: "proposal"
+title: "几何落地的本体感觉视觉融合"
+created_at: "2026-07-19T12:19:14+08:00"
+updated_at: "2026-07-19T12:19:14+08:00"
+aliases: ["geometry-grounded proprioception", "proprioception-vision geometric grounding", "GeoProp"]
+tags: []
+domains: ["embodied-ai", "robot-perception", "proprioception", "visual-grounding"]
+confidence: "medium"
+source_ids: ["source_b1f4ea371eb10f3bc7a0f532"]
+relations: [{"type": "derived_from", "target_id": "source_b1f4ea371eb10f3bc7a0f532", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "refines", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "GeoProp 为通用 VLA 中常被当作独立向量的本体状态提供显式 3D 到 2D 对齐机制，并在 Diffusion Policy 与 π0 两类架构上测试。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "limits", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "该对齐依赖已知相机内外参且只投影末端位置；跨相机、灵巧手和全身本体的直接可移植性因此受约束。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "GeoProp 的 predictive kinematic sampling 使用局部运动前视补充当前状态，但它预测的是短时投影位置，不等同于完整未来状态或世界动力学预测。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b1f4ea371eb10f3bc7a0f532"
+uncertainty: "方法在相机标定漂移、投影点被遮挡、急剧转向和接触切换时可能退化；单固定主相机实验不足以证明多视角与移动相机泛化。"
+---
+
+# 几何落地的本体感觉视觉融合
+
+把末端位姿投影到图像特征平面，在共定位视觉 token 上采样并注入本体状态，同时用近期运动预测短时前视坐标，使机器人运动学与场景语义形成显式对应。
```
