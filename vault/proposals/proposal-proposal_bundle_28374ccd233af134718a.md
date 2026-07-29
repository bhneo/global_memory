---
id: "proposal_bundle_28374ccd233af134718a"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-25T18:08:43+08:00"
updated_at: "2026-07-25T18:08:44+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_0c017bf657a648ca70e9ae25"]
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
extraction_id: "extraction_221feb881b79fce85df44633"
input_sha256: "fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_88f87ddc5dcf77113c5154c4", "target_path": "vault/knowledge/concepts/concept_88f87ddc5dcf77113c5154c4-面向组合式-ood-操作的子任务监督与状态条件视觉遮蔽.md", "base_sha256": null, "candidate_sha256": "765f4a17651a52733816a6681f7953a601846221e1b20b5571d7d565b26a5d55", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_28374ccd233af134718a-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_88f87ddc5dcf77113c5154c4.md", "working_at": "2026-07-25T18:08:44+08:00"}]
existing_context: [{"id": "concept_3363773a8f142fcedd29ce9d", "type": "concept", "title": "训练—模型—部署三分布的操作鲁棒性诊断", "path": "vault/memory/concept/concept_3363773a8f142fcedd29ce9d.md", "status": "working", "source_ids": ["source_cdce2dfd2021019fc46a9ea7"], "snippet": "# 训练—模型—部署三分布的操作鲁棒性诊断\n\n在长时程机器人操作中，分别检查专家演示训练分布、策略学习到的归纳偏置和实机执行轨迹分布之间的失配；对齐措施应标明其针对数据覆盖、动作采样还是推理—执行时延。该诊断框架不意味着三个分布可被完全观测或由单一指标消除。", "match_reason": "metadata:domains"}, {"id": "reflection_1f4ab26f44d5ff91048664cc", "type": "reflection", "title": "χ0：长时程鲁棒性需要区分训练、模型与部署分布", "path": "vault/reflections/reflection-reflection_1f4ab26f44d5ff91048664cc.md", "status": "active", "source_ids": ["source_cdce2dfd2021019fc46a9ea7"], "snippet": "# χ0：长时程鲁棒性需要区分训练、模型与部署分布\n\n## Why important\n\n该论文把长时程操作的失稳归为演示训练分布、策略归纳偏置和实际执行轨迹之间的不同失配，并分别提出权重合并、阶段优势和训练—部署对齐；它为诊断失败提供了比单一成功率更具体的分层位置。\n\n## What changed\n\n资源规模不是部署鲁棒性的唯一解释变量；同一策略可能在训练数据覆盖、动作采样和执行时延三个边界上分别失配。\n\n## Surprising\n\nNot…", "match_reason": "metadata:domains"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…Contact jams, stalls, and [out-of-distribution] disturbances remain failure modes.\n  Difference: A curriculum organizes data and task…", "match_reason": "full-text:body"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World [Action] Model\n\n默认由 World [Action] Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 latent [action]\n\n## Why important\n\nWALA 不从原始像素重建 latent [action]，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_0c017bf657a648ca70e9ae25"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "d5db9ed65bb828213bb502386e14f4d8b86022e452da0964f4f87844c36a8354"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_221feb881b79fce85df44633`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_88f87ddc5dcf77113c5154c4-面向组合式-ood-操作的子任务监督与状态条件视觉遮蔽.md
@@ -0,0 +1,20 @@
+---
+id: "concept_88f87ddc5dcf77113c5154c4"
+type: "concept"
+status: "proposal"
+title: "面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽"
+created_at: "2026-07-25T18:08:43+08:00"
+updated_at: "2026-07-25T18:08:43+08:00"
+aliases: ["Compositional Supervision and State-Conditioned Asymmetric Masking", "AC-VLA", "组合式动作学习"]
+tags: []
+domains: ["vla", "compositional-generalization", "robot-learning"]
+confidence: "medium"
+source_ids: ["source_0c017bf657a648ca70e9ae25"]
+relations: [{"type": "derived_from", "target_id": "source_0c017bf657a648ca70e9ae25", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_90d52ab5e62d9847f9529875", "reason": "两者都关注视觉表征不能自动保证动作泛化；AC-VLA 提出训练期的子任务监督与状态遮蔽干预，该既有概念要求将注意力迁移和动作级成功分开评估。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_0c017bf657a648ca70e9ae25"
+reflection_context: {"reflection_ids": ["reflection_4b0d86fae587571975ca7c09"], "importance": "high", "changed_belief": "此前容易将组合 OOD 失败归为缺少更多演示；本文提示，即使熟悉子技能都出现过，训练目标若保留完整轨迹关联和局部纹理捷径，模型仍可能无法按新对象—目标组合执行。", "surprising": "", "connections": [{"shared_mechanism": "两者都区分模型注意到任务相关区域与模型能否将该信息稳定转化为正确动作。", "boundary": "该连接适用于研究视觉语言动作模型在组合式操作任务中的表征与执行误差，不足以替代对真实机器人接触、控制频率或安全约束的评估。", "difference": "AC-VLA 通过分解监督和抓取阶段遮蔽改变训练信号；既有概念概括的是注意力迁移与动作成功之间的评测缺口。"}], "open_questions": []}
+---
+
+# 面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽
+
+AC-VLA 针对视觉语言动作模型在未见子任务组合中的轨迹过拟合和腕部视角感知捷径，将复杂指令和对应本体感觉轨迹对齐为稠密子任务监督，并与完整演示混合训练；同时在闭爪阶段按状态抑制腕部视角，以迫使模型更多利用全局空间语义。该方法在论文所述 π0.5 与 LIBERO 设置中报告组合 OOD 改善，但其可迁移性仍需在不同骨干、传感器和真实任务中独立验证。
```
