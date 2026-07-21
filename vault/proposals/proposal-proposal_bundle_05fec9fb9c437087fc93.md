---
id: "proposal_bundle_05fec9fb9c437087fc93"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:34:28+08:00"
updated_at: "2026-07-20T12:34:28+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_2d5d59db178b1a20c9213220"]
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
extraction_id: "extraction_6b5fae7658d8ade6ae955eb4"
input_sha256: "941b8c4848f0d4fb79298c035ba8301ae8ce5d436de6906c1da625f2986b45a9"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_ac0f0527a9c7bdba44eb37b8", "target_path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "base_sha256": "9e3e0577b28f9c75a250b4b0af4fa0bc2df4e5299f5b4a47e5de6ca49880165b", "candidate_sha256": "1c01bf0e9e5c1985294680c35b552a58f26dd3f55ed2f77e60121ab4b9d88af3", "decision": "exception", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_05fec9fb9c437087fc93-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_05fec9fb9c437087fc93-concept-1.md", "exception_reasons": ["unclassified incremental change"]}]
existing_context: [{"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 [Latent] Action\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 [latent] action target，再用机器人动作预测与 [latent] world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 [latent] action\n\n## Why important\n\nWALA 不从原始像素重建 [latent] action，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# [Latent] Memory Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "reflection_c3b3e3b0cbbc4d820aa25ce5", "type": "reflection", "title": "CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化", "path": "vault/reflections/reflection-reflection_c3b3e3b0cbbc4d820aa25ce5.md", "status": "active", "source_ids": ["source_f4bd7390e1b485ab773f1446"], "snippet": "# CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化\n\n## Why important\n\nCLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 [latent] action 被背景变化和外观噪声主导。\n\n## What changed\n\n人类视频规模本身不足以保证机器人迁移；若…", "match_reason": "metadata:domains"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:aliases"}, {"id": "reflection_cd269bee56819aafec2fd5a3", "type": "reflection", "title": "FlowDAgger：适配接口的位置决定能否保留生成策略先验", "path": "vault/reflections/reflection-reflection_cd269bee56819aafec2fd5a3.md", "status": "active", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# FlowDAgger：适配接口的位置决定能否保留生成策略先验\n\n## Why important\n\n它把人类纠正动作反演为冻结生成策略的噪声向量，再训练小型潜空间策略，避免全模型微调破坏已有技能，也避免无约束动作残差离开基础策略支持集。\n\n## What changed\n\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。\n\n## Surprising\n\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger…", "match_reason": "metadata:domains"}, {"id": "reflection_a74b334857543499d8111c64", "type": "reflection", "title": "FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口", "path": "vault/reflections/reflection-reflection_a74b334857543499d8111c64.md", "status": "active", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "…并可解码回机器人动作。\n\n## What changed\n\n此前容易把 World Action Model 的动作接口理解为数值动作或抽象 [latent]；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。\n\n## Surprising…", "match_reason": "full-text:body"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…人类纠正和离线跨轨迹一致性是互补监督源，分别交换自主性、安全成本与标签偏差。\n\n## Knowledge updates\n\n[\n  {\n    \"target_id\": \"concept_[latent]_space_intervention_adaptation\",\n    \"previous\": \"通过人类干预的动作反演，在冻结生成策略的潜空间中学习轻量适配。\",\n    \"proposed\": \"潜空间干预适配属于 VLA…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_2d5d59db178b1a20c9213220"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-b-20260720`
- Extraction：`extraction_6b5fae7658d8ade6ae955eb4`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md
+++ candidate:vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md
@@ -1,38 +1,20 @@
 ---
 id: "concept_ac0f0527a9c7bdba44eb37b8"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "未来语义—几何变化监督的可执行 Latent Action"
 created_at: "2026-07-20T12:33:32+08:00"
-updated_at: "2026-07-20T12:33:32+08:00"
+updated_at: "2026-07-20T12:34:28+08:00"
 aliases: ["Semantic-geometric executable latent action", "WALA", "未来动力学 Latent Action"]
 tags: []
 domains: ["embodied-ai", "vla", "latent-action", "human-video", "future-dynamics"]
 confidence: "high"
 source_ids: ["source_2d5d59db178b1a20c9213220"]
-relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
 change_reason: "compile bundle from source_2d5d59db178b1a20c9213220"
+change_type: "needs_review"
 reflection_context: {"reflection_ids": ["reflection_3eda5d913d6a736393b8cd9c"], "importance": "high", "changed_belief": "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。", "surprising": "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}], "open_questions": ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-daily-batch-b-20260720"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-daily-batch-b-20260720"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_8f490857ade5069cef6e"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_8f490857ade5069cef6e-concept-1.md"
-origin_candidate_sha256: "da55b7c05d3f4a7ddcfe7dde8ea7f7c4bbe7ced9c8440b293c7fb98ea6105ac6"
-memory_schema_version: 2
+proposed_status: "working"
 ---
 
 # 未来语义—几何变化监督的可执行 Latent Action
```
