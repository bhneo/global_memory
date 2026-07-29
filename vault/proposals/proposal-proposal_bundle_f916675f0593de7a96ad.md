---
id: "proposal_bundle_f916675f0593de7a96ad"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T16:32:01+08:00"
updated_at: "2026-07-28T16:32:20+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_c79f943c818d06054ca5cf92"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-strong-model-m91-weekly-v3"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e62bd6b73d0d7d66a185bfc3"
input_sha256: "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_multitimescale_tactile_world_model", "target_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "base_sha256": "da9df931b9a21e7ea31565c8f9edb0d683c2101f32d13fa0215b1ab9c6f6f3fd", "candidate_sha256": "d808f8a927c3195c92830b7d74fd18bdea5e7418dd33f0454af32abeef097a37", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_f916675f0593de7a96ad-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_f916675f0593de7a96ad-concept-1.md", "working_path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-28T16:32:20+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_c0693ad0e6abf8397dbdfd87", "type": "reflection", "title": "PAC-ACT：动作块既是生成单位，也应成为信用分配与约束单位", "path": "vault/reflections/reflection-reflection_c0693ad0e6abf8397dbdfd87.md", "status": "active", "source_ids": ["source_c79f943c818d06054ca5cf92"], "snippet": "…与 RL Token 都在保留预训练行为先验的前提下用 [actor-critic] 做后训练。\n  Boundary: PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。\n  Difference: PAC-ACT 改造的是优化和信用分配的时间单位…", "match_reason": "full-text:body"}, {"id": "synthesis_1fdb28cc5ac38aa6f424e5e1", "type": "synthesis", "title": "精细与接触丰富操作中的 VLA 后训练：反馈接口、时间尺度与物理闭环", "path": "vault/synthesis/synthesis-synthesis_1fdb28cc5ac38aa6f424e5e1.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb", "source_37fe3c1f9d9fb7daa262fa91", "source_40700e61702f4b5a5765e11d", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_b7444ef42015f4f3b6f51032", "source_c79f943c818d06054ca5cf92", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…mechanism\": \"RL Token 与 PAC-ACT 都保留预训练行为先验，并用 [actor-critic] 针对精密阶段进行局部后训练。\",\n    \"boundary\": \"RL Token 的证据限于四项精密真机任务，PAC-ACT 的证据面向轻量视觉动作块策略和工业精密接触基准…", "match_reason": "full-text:body"}, {"id": "concept_d01c4f0b61292d29f0a7ffe2", "type": "concept", "title": "动作块级策略优化与动态执行时域", "path": "vault/memory/concept/concept_d01c4f0b61292d29f0a7ffe2.md", "status": "working", "source_ids": ["source_c79f943c818d06054ca5cf92"], "snippet": "# 动作块级策略优化与动态执行时域\n\n动作块级策略优化要求强化学习的决策、价值、优势和行为先验约束与动作块生成单位对齐；块长同时决定吞吐、时间连续性、信用分配跨度和异常后的纠正延迟，因此应被视为可按风险与阶段调整的控制时域。", "match_reason": "metadata:aliases"}, {"id": "synthesis_a4a2bd5ddcee562f2574676f", "type": "synthesis", "title": "适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界", "path": "vault/synthesis/synthesis-synthesis_a4a2bd5ddcee562f2574676f.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_40700e61702f4b5a5765e11d", "source_6b52a51e2b4a3be43c97c386", "source_7b278ba348f2a8bb94cce1fc", "source_91072aa553af99e6ab97c6cd", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "# 适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界\n\n## Emerging patterns\n\n- VLA 适配不必等同于全模型更新。RPent 把改变放在模型外的规划、记忆与恢复外壳，RL Token 把改变放在面向 [actor-critic] 的紧凑内部读出，FlowDAgger…", "match_reason": "full-text:body"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…并训练低维中间控制接口。\",\n    \"boundary\": \"只有基础策略已覆盖目标行为附近时，低维接口才可能兼顾样本效率和先验保持。\",\n    \"difference\": \"RL Token 使用奖励和 [actor-critic]；FlowDAgger 使用人类纠正、动作反演和监督学习。\"\n  },\n  {\n    \"shared_mechanism\": \"PAC-ACT 与…", "match_reason": "full-text:body"}, {"id": "synthesis_60071a24c6e3071f6731c4e2", "type": "synthesis", "title": "VLA 后训练、动作观察接口与世界模型：分布、表示、反馈和可执行性", "path": "vault/synthesis/synthesis-synthesis_60071a24c6e3071f6731c4e2.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220", "source_4b25f596c34869693b9b8151", "source_4df1017326dd7cc4786f4218", "source_5b8c57a9bef3348109f3b7bb", "source_8b41a014bee47c4239a2fa81", "source_b64b4a539b8c17d0cfe662ba", "source_e6608d8f849ad472bbd95143", "source_ef80ef223077ef0855660839", "source_f4bd7390e1b485ab773f1446", "source_f9128ff3463cfaa7fa41ee7e", "source_fe986df678d73ef2b6234f0c"], "snippet": "…proposed\": \"连续曲线重定时与 [PAC-ACT] 的动作块信用分配位于同一时间接口的不同侧：前者定义执行轨迹，后者定义优化决策单位；两者都必须受接触风险和纠正延迟约束。\",\n    \"reason\": \"B-spline Policy 的表示重定时为既有 [PAC-ACT]/动态执行时域补充了连续轨迹侧的边界。\",\n    \"change_type…", "match_reason": "full-text:body"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…offline iteration and online off-policy VLA [post-training] are distinct paths\n\n## Why important\n\nThe notes separate an…", "match_reason": "metadata:title"}, {"id": "concept_bcf39e7d937cfdf22e3c49e2", "type": "concept", "title": "面向真实零售人形机器人的数据高效 VLA 后训练闭环", "path": "vault/memory/concept/concept_bcf39e7d937cfdf22e3c49e2.md", "status": "working", "source_ids": ["source_3846f8c1451f8a12e0f87b33"], "snippet": "# 面向真实零售人形机器人的数据高效 VLA 后训练闭环\n\n在超市场景中部署预训练 VLA 时，可把控制频率对齐、数据筛选、任务相关视觉突出和降低对 VLA 主动作流依赖的后训练配方，与从当前策略失败状态收集的经验驱动细化结合；其目标是缩小实验室到门店的系统失配，而非证明这些组件可独立保证所有人形机器人任务的可靠性。", "match_reason": "metadata:aliases"}, {"id": "reflection_3b2e99de9c8c6dfc2ba8cd5a", "type": "reflection", "title": "DEED：零售人形 VLA 的可靠性首先是部署系统问题", "path": "vault/reflections/reflection-reflection_3b2e99de9c8c6dfc2ba8cd5a.md", "status": "active", "source_ids": ["source_3846f8c1451f8a12e0f87b33"], "snippet": "# DEED：零售人形 VLA 的可靠性首先是部署系统问题\n\n## Why important\n\nDEED 把零售人形机器人的失效面放在控制频率、数据筛选、视觉重点和部署后经验回收的组合接口上；这为区分基础模型能力不足与系统集成失配提供了更可操作的诊断单位。\n\n## What changed\n\n先前容易把真实部署失败主要归因于 VLA 架构或数据量；该工作提示，在固定基础模型上…", "match_reason": "metadata:domains"}, {"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for Force Accelerating VLA [Post-Training] with Reactive Force Injection Yi Wang 12* , Wendi Chen…", "match_reason": "full-text:body"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口\n\n## Why important\n\n它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 [actor-critic] 通过紧凑 RL token 在少量真机交互中适应精密阶段…", "match_reason": "full-text:body"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 [actor-critic] 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "full-text:body"}, {"id": "concept_34269bf138ea36a302aaa11f", "type": "concept", "title": "接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies", "path": "vault/memory/concept/concept_34269bf138ea36a302aaa11f.md", "status": "working", "source_ids": ["source_bee998153a82cd2a92db045b"], "snippet": "…for flow policies\n\n对生成多个动作候选的 flow policy，可用接触阶段门控在接触前按 TCP 接近物体、接触后按物体向任务目标的一阶距离下降评分，并在候选集合内标准化后形成软动作；这在论文中保持 [actor/critic] 训练目标不变。方法依赖可靠接触、对象和任务几何及所用候选数量，不能替代任意任务的长期价值估计。", "match_reason": "full-text:body"}, {"id": "reflection_cd269bee56819aafec2fd5a3", "type": "reflection", "title": "FlowDAgger：适配接口的位置决定能否保留生成策略先验", "path": "vault/reflections/reflection-reflection_cd269bee56819aafec2fd5a3.md", "status": "active", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "…FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 [actor-critic]；两者的信息来源和安全成本不同。\n\n## Conflicts\n\n- 限制在基础策略的生成支持集有助于保留技能，但若目标行为不在该支持集中，潜空间转向本身可能不足。\n\n## Open questions\n\n- 动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？\n\n## Possible mechanisms…", "match_reason": "full-text:body"}, {"id": "reflection_305130038ee9fd3cb9e18ec4", "type": "reflection", "title": "ExToken：探索预算的关键变量可能是行为模式覆盖而非 rollout 数量", "path": "vault/reflections/reflection-reflection_305130038ee9fd3cb9e18ec4.md", "status": "active", "source_ids": ["source_5b8c57a9bef3348109f3b7bb"], "snippet": "…RL 读出接口从 VLA 内部特征学习供 [actor-critic] 使用的任务表示；ExToken 用离线示范的行为模式 token 主动改变 rollout 分布，并另学状态条件选择器。\n\n## Conflicts\n\n- 示范先验使探索更可行，却也会把探索范围限制在示范表征可聚类出的行为模式附近。\n\n## Open…", "match_reason": "full-text:body"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World [Action] Model\n\n默认由 World [Action] Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 latent [action]\n\n## Why important\n\nWALA 不从原始像素重建 latent [action]，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_c79f943c818d06054ca5cf92"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "2be8f6b637647bb53d07bf3052361aa8c21535a0d138a25ac1c27b5c015c2055"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-strong-model-m91-weekly-v3`
- Extraction：`extraction_e62bd6b73d0d7d66a185bfc3`
- 编译前召回已有对象：21
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_multitimescale_tactile_world_model.md
+++ candidate:vault/memory/concept/concept_multitimescale_tactile_world_model.md
@@ -1,43 +1,26 @@
 ---
 id: "concept_multitimescale_tactile_world_model"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "多时间尺度触觉世界模型控制"
 created_at: "2026-07-19T03:02:53+08:00"
-updated_at: "2026-07-26T12:33:55+08:00"
+updated_at: "2026-07-28T16:32:01+08:00"
 aliases: ["multi-timescale tactile world model", "TouchWorld"]
 tags: []
 domains: ["embodied-ai", "vla", "world-model", "tactile", "dexterous-manipulation"]
 confidence: "medium"
-source_ids: ["source_283911da72edc403d1b823fb"]
-relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}]
-change_reason: "compile bundle from source_283911da72edc403d1b823fb"
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
+source_ids: ["source_283911da72edc403d1b823fb", "source_c79f943c818d06054ca5cf92"]
+relations: [{"type": "derived_from", "target_id": "source_283911da72edc403d1b823fb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "refines", "target_id": "concept_predictive_vla_deployment", "reason": "它把预测式 VLA 进一步扩展为触觉子目标预测与高频接触反馈的多时间尺度架构。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "触觉世界模型预测未来接触子目标，但在这里直接服务动作生成而不只是离线评价。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "reason": "TouchWorld 的中频动作生成需要与 PAC-ACT 所描述的块级价值、优势和纠正时域对齐。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_cache_refinement", "reason": "预测子目标与缓存暖启动都减少重复计算，但前者描述未来接触参考，后者复用生成路径；两者需要不同拒绝门禁。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
+change_reason: "compile bundle from source_c79f943c818d06054ca5cf92"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_62e14da60b1cc35f28689c29", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_c5765c32f1c3dd7302da4906"], "importance": "weekly", "changed_belief": "此前动作缓存更像单纯的系统加速技巧；该材料说明它实际上是带相似度门和生成式校正的短期经验复用机制。\n动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。\n此前世界模型与 VLA 的结合容易被描述为在主干中加入未来预测；该材料强调预测路径和反应路径必须解耦，否则慢速语义推理会限制接触纠错。", "surprising": "缓存可以跨 episode 甚至跨任务复用，说明可复用单元并非上一时刻动作本身，而是条件生成路径附近的中间状态。\n在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。\n触觉在同一架构中同时承担未来接触参考和即时误差反馈，两种角色共享模态但具有不同时间语义。", "connections": [{"shared_mechanism": "都把已有中间结果作为下一次决策的候选起点，并通过后续过程校正而不是直接照搬", "boundary": "连接限于在线计算复用，不表示 ActionCache 形成长期技能、事实记忆或任务理解", "difference": "ActionCache 复用连续动作生成状态并由 denoising 修正；技能库复用较稳定的行为先验并由路由器组合"}, {"shared_mechanism": "与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。", "boundary": "PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。", "difference": "PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。"}, {"shared_mechanism": "都将预测结果作为动作生成或校正的中间目标，而不是只用于离线评分", "boundary": "连接限于预测辅助控制；触觉接触闭环不能直接推广到无接触导航或只有视觉输入的任务", "difference": "TouchWorld 用高频触觉残差处理局部接触偏差，LingBot 用语义与深度未来查询改善较慢的动作表示"}], "open_questions": ["缓存命中应如何联合视觉相似度、任务阶段、机器人状态和 refinement 不确定性进行校准？", "块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？", "预测子目标的误差何时应触发高层重规划，而不是继续由高频残差策略吸收？"]}
+proposed_status: "working"
 ---
 
 # 多时间尺度触觉世界模型控制
 
 把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。
+
+## 新增来源材料
+
+- `source_c79f943c818d06054ca5cf92`：多时间尺度触觉世界模型需要同时声明各层的决策单位、信息新鲜度和升级条件。慢速语义层提出子任务，预测层形成触觉子目标，中频策略以动作块作为生成与信用分配单位，高频触觉残差处理局部接触偏差；缓存的中间动作只可在任务阶段、机器人状态和 refinement 不确定性共同通过门禁时作为暖启动。块长、缓存命中和残差幅度达到阈值时应触发拒绝复用或高层重规划，而不是继续由快环无限吸收。
```
