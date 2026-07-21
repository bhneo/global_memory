---
id: "proposal_bundle_1d0cc88791324b19f67b"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T13:35:32+08:00"
updated_at: "2026-07-20T13:35:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_2d5d59db178b1a20c9213220"]
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
extraction_id: "extraction_6b5fae7658d8ade6ae955eb4"
input_sha256: "941b8c4848f0d4fb79298c035ba8301ae8ce5d436de6906c1da625f2986b45a9"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_ac0f0527a9c7bdba44eb37b8", "target_path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "base_sha256": "9e3e0577b28f9c75a250b4b0af4fa0bc2df4e5299f5b4a47e5de6ca49880165b", "candidate_sha256": "f82c7219c3579ef673b174a498399193d4a35e5678ad1caa520b7b611ada440b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_1d0cc88791324b19f67b-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_1d0cc88791324b19f67b-concept-1.md", "working_path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-20T13:35:51+08:00"}]
existing_context: [{"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 [Latent] Action\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 [latent] action target，再用机器人动作预测与 [latent] world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 [latent] action\n\n## Why important\n\nWALA 不从原始像素重建 [latent] action，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# [Latent] Memory Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "reflection_c3b3e3b0cbbc4d820aa25ce5", "type": "reflection", "title": "CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化", "path": "vault/reflections/reflection-reflection_c3b3e3b0cbbc4d820aa25ce5.md", "status": "active", "source_ids": ["source_f4bd7390e1b485ab773f1446"], "snippet": "# CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化\n\n## Why important\n\nCLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 [latent] action 被背景变化和外观噪声主导。\n\n## What changed\n\n人类视频规模本身不足以保证机器人迁移；若…", "match_reason": "metadata:domains"}, {"id": "concept_fc70bfc09ac7d9473592f09c", "type": "concept", "title": "全身冗余的部分运动学嵌入", "path": "vault/memory/concept/concept_fc70bfc09ac7d9473592f09c.md", "status": "working", "source_ids": ["source_951559714c0383331b1b30ac"], "snippet": "# 全身冗余的部分运动学嵌入\n\n学习给定末端目标下的可行 partial reference 分布，把全身运动学冗余压缩为高层可导航 [latent]，再由低层 imitation controller 保证动力学可行执行。它利用浮动基座和躯干自由度扩大工作空间，但支持集受运动学数据覆盖约束。", "match_reason": "metadata:aliases"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:aliases"}, {"id": "reflection_070e73598e48429fb5eafe01", "type": "reflection", "title": "PAKE：先学习运动学冗余分布，再让 RL 选择部分参考", "path": "vault/reflections/reflection-reflection_070e73598e48429fb5eafe01.md", "status": "active", "source_ids": ["source_951559714c0383331b1b30ac"], "snippet": "…PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。\n\n## Conflicts\n\n- 运动学 [latent] 缩小搜索空间，却可能排除依赖动力学、接触或动量的可行解。\n\n## Open questions\n\n- 怎样检测目标任务所需解落在 KNF…", "match_reason": "full-text:body"}, {"id": "reflection_cd269bee56819aafec2fd5a3", "type": "reflection", "title": "FlowDAgger：适配接口的位置决定能否保留生成策略先验", "path": "vault/reflections/reflection-reflection_cd269bee56819aafec2fd5a3.md", "status": "active", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# FlowDAgger：适配接口的位置决定能否保留生成策略先验\n\n## Why important\n\n它把人类纠正动作反演为冻结生成策略的噪声向量，再训练小型潜空间策略，避免全模型微调破坏已有技能，也避免无约束动作残差离开基础策略支持集。\n\n## What changed\n\n人类在环适配的关键不只是收集多少纠正，而是把纠正写入权重空间、动作空间还是生成潜空间；三者有不同的先验保持和可达行为边界。\n\n## Surprising\n\n人类给出的动作可以通过逆时间积分和局部优化被转译为生成噪声监督，使 DAgger…", "match_reason": "metadata:domains"}]
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

- Provider：`agent-semantic-weekly-gpt56sol-v1`
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
+updated_at: "2026-07-20T13:35:32+08:00"
 aliases: ["Semantic-geometric executable latent action", "WALA", "未来动力学 Latent Action"]
 tags: []
 domains: ["embodied-ai", "vla", "latent-action", "human-video", "future-dynamics"]
 confidence: "high"
 source_ids: ["source_2d5d59db178b1a20c9213220"]
-relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_2d5d59db178b1a20c9213220", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "未来变化提供跨视频来源的共享动作语义，机器人 action loss 则补足跨本体统一接口的执行锚点。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_59f92bcb786f695ddcd47f7f", "reason": "WALA 用语义与深度未来 delta 学 latent action 并以机器人动作约束，FlowWAM 用光流统一视频先验与可解码动作；二者共享视频动力学中介但表征和执行锚点不同。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
 change_reason: "compile bundle from source_2d5d59db178b1a20c9213220"
-reflection_context: {"reflection_ids": ["reflection_3eda5d913d6a736393b8cd9c"], "importance": "high", "changed_belief": "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。", "surprising": "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}], "open_questions": ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？"]}
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
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_3eda5d913d6a736393b8cd9c", "reflection_a74b334857543499d8111c64", "reflection_c3b3e3b0cbbc4d820aa25ce5"], "importance": "weekly", "changed_belief": "此前把人类视频迁移看成给动作模型增加视觉语义；WALA 表明更关键的中介可能是动作造成的未来场景变化，机器人动作与无动作视频可以通过这个共同动力学目标协同训练。\n此前容易把 World Action Model 的动作接口理解为数值动作或抽象 latent；该工作提示，视频原生且可执行的中间表示可以同时承担 policy output、world-model condition 和无动作视频预训练载体。\n人类视频规模本身不足以保证机器人迁移；若 latent space 没有机器人动作锚点，更多视频可能只增强视觉纠缠。对齐目标应明确表达物理可执行性。", "surprising": "论文报告每任务 50 条机器人示范加 400 条无动作人类视频，真机平均表现接近每任务 200 条机器人示范；但零样本验证只有一个 OOD 任务。\n跨 50 个 RoboTwin 任务，预测光流误差与策略成功率呈较强负相关（论文报告 Pearson r=-0.81），说明收益至少部分跟随运动表示质量，而不只是下游解码器捷径。\n论文把 object generalization 与 fine-tuning 后的知识保持分开处理：CLAP-RF 负责连续低时延动作，Knowledge Matching 约束域适配时不要遗忘预训练语义。", "connections": [{"shared_mechanism": "与跨本体通用 VLA 都希望把不同数据来源压缩到统一、可执行的动作表征。", "boundary": "WALA 的人类视频与机器人任务仍需语义相关，真实零样本证据仅覆盖一个任务，不能推出任意互联网视频都能转成机器人技能。", "difference": "跨本体通用 VLA 强调统一动作接口；WALA 用未来语义—几何 delta 作为训练期 latent target，并以机器人动作监督保证执行落地。"}, {"shared_mechanism": "与双系统 World Action Model 都让视频动力学模型同时支持动作生成和未来状态建模。", "boundary": "光流主要描述可见像素运动，遮挡、接触力、不可见关节和跨长时程意图并不天然可观测；论文结果也不能证明跨本体动作解码无需额外适配。", "difference": "双系统 WAM 强调快慢推理分工；FlowWAM 的核心贡献是用光流统一动作与视频模态，并由专门解码器恢复数值控制。"}, {"shared_mechanism": "与 WALA 都把无动作人类视频映射到由机器人数据约束的 latent action 空间。", "boundary": "CLAP 对新物体的已知任务泛化强于仅靠人类视频学习全新任务；人手到平行夹爪的形态差异仍造成不可消除歧义，且当前 extraction 含少量乱码。", "difference": "CLAP 用机器人 VQ 动作词表与对比对齐；WALA 用未来语义和深度变化目标及 world-model 解码监督。"}], "open_questions": ["未来 delta 的时间跨度、深度质量与任务相关性如何共同决定 latent action 是否真正可执行？", "在遮挡、移动相机和接触丰富任务中，光流误差是否仍能稳定预测动作可执行性？", "何时应强制对齐到现有机器人动作词表，何时应保留尚不可执行但可用于未来本体的独立 latent？"]}
+proposed_status: "working"
 ---
 
 # 未来语义—几何变化监督的可执行 Latent Action
```
