---
id: "proposal_bundle_b7a90c6a2444df7fea58"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:33:20+08:00"
updated_at: "2026-07-20T12:33:21+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b64b4a539b8c17d0cfe662ba"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-b-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_27ea83c1e055457ea97d95bf"
input_sha256: "c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_21a37fbe65868f6e97a68a20", "target_path": "vault/knowledge/concepts/concept_21a37fbe65868f6e97a68a20-机器人坐标系稠密-pointmap-观察接口.md", "base_sha256": null, "candidate_sha256": "ab5f679713d6b1238e6ea4b1e96e0b826505396cc22c32a8bf5d28fa983d6722", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b7a90c6a2444df7fea58-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md", "working_at": "2026-07-20T12:33:21+08:00"}]
existing_context: [{"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first [Robot] Control\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b64b4a539b8c17d0cfe662ba"}
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

- Provider：`codex-gpt56-m91-daily-batch-b-20260720`
- Extraction：`extraction_27ea83c1e055457ea97d95bf`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_21a37fbe65868f6e97a68a20-机器人坐标系稠密-pointmap-观察接口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_21a37fbe65868f6e97a68a20"
+type: "concept"
+status: "proposal"
+title: "机器人坐标系稠密 Pointmap 观察接口"
+created_at: "2026-07-20T12:33:20+08:00"
+updated_at: "2026-07-20T12:33:20+08:00"
+aliases: ["Robot-centric pointmap observation", "See Like a Robot", "机器人中心点图", "robot-frame pointmap"]
+tags: []
+domains: ["embodied-ai", "vla", "3d-geometry", "viewpoint-generalization"]
+confidence: "high"
+source_ids: ["source_b64b4a539b8c17d0cfe662ba"]
+relations: [{"type": "derived_from", "target_id": "source_b64b4a539b8c17d0cfe662ba", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_90d52ab5e62d9847f9529875", "reason": "pointmap 为注意力已定位的视觉区域补充与机器人动作同 frame 的度量几何，缩小感知泛化到动作泛化的接口缺口。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_b64b4a539b8c17d0cfe662ba"
+reflection_context: {"reflection_ids": ["reflection_7b23a8a7adc7b353d26fbc30"], "importance": "high", "changed_belief": "此前倾向把多视角泛化问题交给更大视觉模型；该材料提示，显式消除 observation-action frame mismatch 可以减少不必要的函数复杂度，并保留既有视觉 token 接口。", "surprising": "在相同 depth、intrinsics 和 extrinsics 信息下，预计算 robot-frame pointmap 仍优于把这些信息直接交给策略学习转换，隔离出显式几何变换本身的收益。", "connections": [{"shared_mechanism": "与 VLA 注意力泛化—动作泛化缺口都区分看见操作区域与把它稳定映射为机器人动作。", "boundary": "pointmap 需要训练和测试时的相机内外参及深度；当前相机变化主要覆盖 placement/extrinsics，未覆盖摄像头数量与视场变化。", "difference": "注意力—动作缺口描述表征与执行之间的一般问题；pointmap 通过把视觉几何预先表达在动作坐标系中解决其中的 frame mismatch。"}], "open_questions": ["当标定随时间漂移时，pointmap 应作为确定输入还是带不确定性的几何分布进入策略？"]}
+---
+
+# 机器人坐标系稠密 Pointmap 观察接口
+
+把 RGB-D 像素对应的三维点预先转换到机器人动作所用坐标系，并保留图像 H×W 网格供预训练 VLA 视觉通路编码。该接口减少相机视角到动作坐标的学习负担，但依赖深度和相机标定质量。
```
