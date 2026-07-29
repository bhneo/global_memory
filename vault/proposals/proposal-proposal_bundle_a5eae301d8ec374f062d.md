---
id: "proposal_bundle_a5eae301d8ec374f062d"
type: "proposal"
status: "migrated"
title: "Compile bundle：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
created_at: "2026-07-28T16:28:10+08:00"
updated_at: "2026-07-28T16:28:11+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_283911da72edc403d1b823fb"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-strong-model-m91-weekly-v3"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_866e814ee1010452743e8b60"
input_sha256: "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_multitimescale_tactile_world_model", "target_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "base_sha256": "da9df931b9a21e7ea31565c8f9edb0d683c2101f32d13fa0215b1ab9c6f6f3fd", "candidate_sha256": "1854d9316b7a65f351aa2be100416318bd37affb629f82e18c0cf27c84f46fe0", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_a5eae301d8ec374f062d-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_a5eae301d8ec374f062d-concept-1.md", "ingestion_action": "duplicate_noop"}]
existing_context: [{"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile [Foundation] Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "reflection_c5765c32f1c3dd7302da4906", "type": "reflection", "title": "TouchWorld：预测与反应必须处在不同控制时间尺度", "path": "vault/reflections/reflection-reflection_c5765c32f1c3dd7302da4906.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# [TouchWorld]：预测与反应必须处在不同控制时间尺度\n\n## Why important\n\n[TouchWorld] 把慢速语义规划、中频动作块、触觉子目标预测和高频残差纠错拆开，说明世界模型的价值不只是预测准确，而是为正确时间尺度的控制回路提供目标。\n\n## What changed\n\n此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。\n\n## Surprising…", "match_reason": "metadata:title"}, {"id": "synthesis_fe1750531bf1b2a79846b657", "type": "synthesis", "title": "具身策略部署中的监督通道、动作接口与反馈时标", "path": "vault/synthesis/synthesis-synthesis_fe1750531bf1b2a79846b657.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_91072aa553af99e6ab97c6cd"], "snippet": "…真正可比较的是每层保留的信息、更新频率、失效信号和对下游动作的责任边界。\n\n## Knowledge updates\n\n[\n  {\n    \"target_id\": \"concept_[predictive]_vla_deployment\",\n    \"previous\": \"预测式 VLA 主要指在视觉—语言—动作映射中加入未来状态或动作后果预测。\",\n    \"proposed…", "match_reason": "full-text:body"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:aliases"}, {"id": "synthesis_a4a2bd5ddcee562f2574676f", "type": "synthesis", "title": "适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界", "path": "vault/synthesis/synthesis-synthesis_a4a2bd5ddcee562f2574676f.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_40700e61702f4b5a5765e11d", "source_6b52a51e2b4a3be43c97c386", "source_7b278ba348f2a8bb94cce1fc", "source_91072aa553af99e6ab97c6cd", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…ACT、[TouchWorld] 与 ActionCache 都把连续控制拆成有边界的时间单元，并在单元之间安排重新估计或纠正。\",\n    \"boundary\": \"该结构适用于动作块、触觉反馈或生成中间状态可被稳定记录的系统；在突发接触、传感延迟或缓存键失配下，较长单元会扩大纠正延迟。\",\n    \"difference\": \"PAC-ACT 对齐学习与执行的动作块，[TouchWorld] 分离预测与高频反应…", "match_reason": "full-text:body"}, {"id": "synthesis_1fdb28cc5ac38aa6f424e5e1", "type": "synthesis", "title": "精细与接触丰富操作中的 VLA 后训练：反馈接口、时间尺度与物理闭环", "path": "vault/synthesis/synthesis-synthesis_1fdb28cc5ac38aa6f424e5e1.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb", "source_37fe3c1f9d9fb7daa262fa91", "source_40700e61702f4b5a5765e11d", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_b7444ef42015f4f3b6f51032", "source_c79f943c818d06054ca5cf92", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…FlowDAgger 提供可迁移的部署纠正机制；Robo-ValueRL 提供价值可靠性机制，但当前材料不足以把它限定为精细操作专用方法。\n- VLA 后训练主要改变跨回合或中低频策略适配，[TouchWorld]、TACTIC 与 TactiDex 则暴露接触预测、力对齐和高频残差；前者不能替代物理闭环，后者也不能替代任务级价值与探索。\n- 示范迁移只有保留手—物关系并通过接触或仿真可行性筛选时…", "match_reason": "full-text:body"}, {"id": "concept_2d8e08b8d8ace05431e064a0", "type": "concept", "title": "接触中心的混合预测控制", "path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "status": "working", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 接触中心的混合预测控制\n\n把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics…", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…closed-loop control, action alignment, or [predictive] fidelity.\n\n## Surprising\n\nThe reported manipulation scaling claim is conditional: more data…", "match_reason": "full-text:body"}, {"id": "reflection_4b63a8834e11b28db3cf2fdc", "type": "reflection", "title": "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心", "path": "vault/reflections/reflection-reflection_4b63a8834e11b28db3cf2fdc.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心\n\n## Why important\n\nTACTIC 不只把触觉追加到 observation，而是让 distributed [tactile]、proximity map、contact Jacobian sampling 和 hybrid…", "match_reason": "metadata:domains"}, {"id": "concept_2ce226e08d585158c1dfbb18", "type": "concept", "title": "接触反馈应区分短时反应、事件记忆与概率后验", "path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "status": "working", "source_ids": ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"], "snippet": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM…", "match_reason": "metadata:aliases"}, {"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for Force Accelerating VLA Post-Training with [Reactive] Force Injection Yi Wang 12* , Wendi Chen…", "match_reason": "full-text:body"}, {"id": "concept_bb69fa188e0417143c3277cf", "type": "concept", "title": "视觉—触觉 simulation-based 位姿后验用于插入 / visuo-tactile simulation-based pose posterior for insertion", "path": "vault/memory/concept/concept_bb69fa188e0417143c3277cf.md", "status": "working", "source_ids": ["source_4757ec1a2e8a0b678a350ee1"], "snippet": "# 视觉—触觉 simulation-based 位姿后验用于插入 / visuo-[tactile] simulation-based pose posterior for insertion\n\n在 peg-in-hole 插入中…", "match_reason": "metadata:title"}, {"id": "concept_1920583cd9c7063491d45a40", "type": "concept", "title": "表示对齐的未来触觉 grounding", "path": "vault/memory/concept/concept_1920583cd9c7063491d45a40.md", "status": "working", "source_ids": ["source_38651a884fe5c5c73a6e190d"], "snippet": "# 表示对齐的未来触觉 grounding\n\n在触觉增强 VLA 中，先以冻结 probe 比较各内部表示对未来触觉状态的可预测性，再将紧凑未来触觉 latent 的预测损失施加到最能表达动作条件接触动力学的中间 action-expert 接口；该训练期约束不同于直接预测噪声较大的原始触觉，也不同于在多个接口无差别叠加损失。", "match_reason": "metadata:aliases"}, {"id": "concept_5b49f7afd60ba18d35ca58e8", "type": "concept", "title": "触觉对齐的人到机器人接触迁移", "path": "vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md", "status": "working", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "# 触觉对齐的人到机器人接触迁移\n\n在人类示范中同步手部运动学、物体状态和全手压力，把接触形成、接触区域时序、力幅值与安全约束作为独立监督和评测维度。该范式纠正纯运动学模仿的接触缺口，但跨本体时不应假设人类接触分布可无条件照搬。", "match_reason": "metadata:aliases"}, {"id": "reflection_243a1a3f0cdc9450748cd215", "type": "reflection", "title": "表示对齐的未来触觉 grounding：监督位置比增加触觉损失更关键", "path": "vault/reflections/reflection-reflection_243a1a3f0cdc9450748cd215.md", "status": "active", "source_ids": ["source_38651a884fe5c5c73a6e190d"], "snippet": "# 表示对齐的未来触觉 grounding：监督位置比增加触觉损失更关键\n\n## Why important\n\n该研究用冻结线性 probe 选择最能预测未来触觉的中间 action-expert 表示，再用紧凑 latent [tactile] target 监督它，说明接触学习的关键是让监督作用于仍含动作条件接触动力学、但尚未压缩为即时电机输出的接口…", "match_reason": "metadata:domains"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "…否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。\n\n## Surprising\n\n纯运动学 baseline 的 kinematic success 明显高于 [tactile]-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。\n\n## Connections\n\n- Shared mechanism: 与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态…", "match_reason": "metadata:domains"}, {"id": "synthesis_be18972801786224075196eb", "type": "synthesis", "title": "灵巧操作、触觉与示范迁移：交互结构、冗余先验和物理可行性", "path": "vault/synthesis/synthesis-synthesis_be18972801786224075196eb.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_951559714c0383331b1b30ac", "source_b7444ef42015f4f3b6f51032", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…物交互拓扑；先验覆盖与分布外检测是共同边界。\n- TactiDex 与 TACTIC 把接触从附加模态提升为监督或规划坐标：一个定义人到机器人的接触保真目标，一个把 [tactile]、proximity 与 contact Jacobian 放入 MPC。\n- TELEDEXTER 与 DemoBridge…", "match_reason": "metadata:domains"}, {"id": "concept_8f8ae7b5cac6690d2e341d40", "type": "concept", "title": "人形行为基础模型的数量—多样性协同扩展", "path": "vault/memory/concept/concept_8f8ae7b5cac6690d2e341d40.md", "status": "working", "source_ids": ["source_46f82af34b1ace2c5c0483af"], "snippet": "# 人形行为基础模型的数量—多样性协同扩展\n\n在人形运动跟踪的强化学习预训练中，在线并行环境与rollout时域主要决定有效交互数据数量，经过筛选的参考动作库主要决定行为分布多样性；两者需与全局全身轨迹接口和可扩展模型架构协同评估，而不能以参考动作数量单独替代训练规模。", "match_reason": "metadata:aliases"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied [Foundation] Models for Real-World Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "…NVIDIA Isaac GR00T N1.7 - A [Foundation] Model for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The…", "match_reason": "metadata:title"}, {"id": "concept_27970fb0de0d8995774e31f6", "type": "concept", "title": "多视角具身合成世界模型数据引擎", "path": "vault/memory/concept/concept_27970fb0de0d8995774e31f6.md", "status": "working", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "# 多视角具身合成世界模型数据引擎\n\n在保留通用图像与视频生成能力的同时，联合学习多视角具身场景、跨本体结构化编辑和具身视频，使世界基础模型既能预测交互也能生成受机器人与相机约束的策略训练数据。合成数据仍需通过几何、接触和闭环收益验证。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_283911da72edc403d1b823fb"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "9560d442d9287bd05f0f3be2b37fb85d2c91f26928051b806b8682e5f1a1ebc6"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation

## 编译边界

- Provider：`codex-strong-model-m91-weekly-v3`
- Extraction：`extraction_866e814ee1010452743e8b60`
- 编译前召回已有对象：21
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_multitimescale_tactile_world_model.md
+++ candidate:vault/memory/concept/concept_multitimescale_tactile_world_model.md
@@ -1,41 +1,20 @@
 ---
 id: "concept_multitimescale_tactile_world_model"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "多时间尺度触觉世界模型控制"
 created_at: "2026-07-19T03:02:53+08:00"
-updated_at: "2026-07-26T12:33:55+08:00"
+updated_at: "2026-07-28T16:28:10+08:00"
 aliases: ["multi-timescale tactile world model", "TouchWorld"]
 tags: []
 domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
 confidence: "medium"
 source_ids: ["source_283911da72edc403d1b823fb"]
-relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
+relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "reason": "TouchWorld 的中频动作生成需要与 PAC-ACT 所描述的块级价值、优势和纠正时域对齐。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_cache_refinement", "reason": "预测子目标与缓存暖启动都减少重复计算，但前者描述未来接触参考，后者复用生成路径；两者需要不同拒绝门禁。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
 change_reason: "compile bundle from source_283911da72edc403d1b823fb"
-uncertainty: "架构和结果局限于论文中的六项长时程接触任务，触觉硬件与标注成本可能影响迁移。"
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "agent-semantic-weekly-gpt56sol-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "agent-semantic-weekly-gpt56sol-v1"
-consolidation_count: 8
-last_consolidated_at: "2026-07-26T12:33:55+08:00"
-last_verified_at: "2026-07-19T03:29:27+08:00"
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_2a787ee43ca54bc95b00"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_2a787ee43ca54bc95b00-concept-1.md"
-origin_candidate_sha256: "e6161d8a748e1a5dd54a5ac7254ede7a78d21d97fc25b7593f1b022e298b82fc"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_e8a84716973852d9bfe19b11"
-evidence: []
-change_history: [{"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": ["aliases"], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "new_statement": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "changed_fields": [], "reason": "compile bundle from source_283911da72edc403d1b823fb", "trigger_source": "source_283911da72edc403d1b823fb", "evidence_added": []}]
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_62e14da60b1cc35f28689c29", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_c5765c32f1c3dd7302da4906"], "importance": "weekly", "changed_belief": "此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。\n动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。\n此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。", "surprising": "缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。\n在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。\n触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。", "connections": [{"shared_mechanism": "都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬", "boundary": "连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解", "difference": "ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合"}, {"shared_mechanism": "与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。", "boundary": "PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。", "difference": "PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。"}, {"shared_mechanism": "都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分", "boundary": "连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务", "difference": "TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示"}], "open_questions": ["缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？", "块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？", "预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？"]}
+proposed_status: "working"
 ---
 
 # 多时间尺度触觉世界模型控制
```
