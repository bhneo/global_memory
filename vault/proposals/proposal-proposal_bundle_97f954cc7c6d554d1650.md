---
id: "proposal_bundle_97f954cc7c6d554d1650"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T18:05:58+08:00"
updated_at: "2026-07-20T18:05:58+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_38651a884fe5c5c73a6e190d"]
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
extraction_id: "extraction_eba0221e33968b7113f76b01"
input_sha256: "3918d93d2d2bc16be906a82401e7f4aeecf54faca136769af8d4763a2baa040e"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_1920583cd9c7063491d45a40", "target_path": "vault/knowledge/concepts/concept_1920583cd9c7063491d45a40-表示对齐的未来触觉-grounding.md", "base_sha256": null, "candidate_sha256": "37bf5e3397fa64af1f0df977dac350e645d400de82200d21d19b854045ac306e", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_97f954cc7c6d554d1650-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_1920583cd9c7063491d45a40.md", "working_at": "2026-07-20T18:05:58+08:00"}]
existing_context: [{"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive [Tactile] Foundation Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_multitimescale_tactile_world_model", "type": "concept", "title": "多时间尺度触觉世界模型控制", "path": "vault/memory/concept/concept_multitimescale_tactile_world_model.md", "status": "working", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "# 多时间尺度触觉世界模型控制\n\n把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "match_reason": "metadata:aliases"}, {"id": "concept_5b49f7afd60ba18d35ca58e8", "type": "concept", "title": "触觉对齐的人到机器人接触迁移", "path": "vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md", "status": "working", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "# 触觉对齐的人到机器人接触迁移\n\n在人类示范中同步手部运动学、物体状态和全手压力，把接触形成、接触区域时序、力幅值与安全约束作为独立监督和评测维度。该范式纠正纯运动学模仿的接触缺口，但跨本体时不应假设人类接触分布可无条件照搬。", "match_reason": "metadata:aliases"}, {"id": "reflection_4b63a8834e11b28db3cf2fdc", "type": "reflection", "title": "TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心", "path": "vault/reflections/reflection-reflection_4b63a8834e11b28db3cf2fdc.md", "status": "active", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# TACTIC：接触丰富控制需要感知、采样和预测都以接触为中心\n\n## Why important\n\nTACTIC 不只把触觉追加到 observation，而是让 distributed [tactile]、proximity map、contact Jacobian sampling 和 hybrid…", "match_reason": "metadata:domains"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "…否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。\n\n## Surprising\n\n纯运动学 baseline 的 kinematic success 明显高于 [tactile]-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。\n\n## Connections\n\n- Shared mechanism: 与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态…", "match_reason": "metadata:domains"}, {"id": "synthesis_be18972801786224075196eb", "type": "synthesis", "title": "灵巧操作、触觉与示范迁移：交互结构、冗余先验和物理可行性", "path": "vault/synthesis/synthesis-synthesis_be18972801786224075196eb.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_951559714c0383331b1b30ac", "source_b7444ef42015f4f3b6f51032", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…物交互拓扑；先验覆盖与分布外检测是共同边界。\n- TactiDex 与 TACTIC 把接触从附加模态提升为监督或规划坐标：一个定义人到机器人的接触保真目标，一个把 [tactile]、proximity 与 contact Jacobian 放入 MPC。\n- TELEDEXTER 与 DemoBridge…", "match_reason": "metadata:domains"}, {"id": "concept_2d8e08b8d8ace05431e064a0", "type": "concept", "title": "接触中心的混合预测控制", "path": "vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md", "status": "working", "source_ids": ["source_e8cc1290fdb80e80f77ba2c2"], "snippet": "# 接触中心的混合预测控制\n\n把 RGB-D、分布式触觉和 proximity map 融为接触状态，用 contact Jacobian 塑形 MPC 动作采样，并以分析运动学约束可行性、学习 latent dynamics…", "match_reason": "metadata:domains"}, {"id": "concept_geometry_grounded_proprioception", "type": "concept", "title": "几何落地的本体感觉视觉融合", "path": "vault/memory/concept/concept_geometry_grounded_proprioception.md", "status": "working", "source_ids": ["source_b1f4ea371eb10f3bc7a0f532"], "snippet": "# 几何落地的本体感觉视觉融合\n\n把末端位姿投影到图像特征平面，在共定位视觉 token 上采样并注入本体状态，同时用近期运动预测短时前视坐标，使机器人运动学与场景语义形成显式对应。", "match_reason": "metadata:aliases"}, {"id": "reflection_f5a4802aeb05942de18022f0", "type": "reflection", "title": "WAM 鲁棒性干预：可分离激活是可操控性的诊断而非普适保证", "path": "vault/reflections/reflection-reflection_f5a4802aeb05942de18022f0.md", "status": "active", "source_ids": ["source_38cba686373b003398483ab2"], "snippet": "…表示对齐触觉 [grounding] 在训练期把未来接触结果监督到中间层；WAM steering 在不微调模型时，于推理期调节已存在的激活方向。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 在新的相机、夹爪和视觉噪声组合上，线性可分性与闭环 steering 效果的相关性是否仍能校准？\n\n## Possible…", "match_reason": "full-text:body"}, {"id": "reflection_59bfe9d29f3ebbb4c8a6b162", "type": "reflection", "title": "Secondary architecture commentary: autoregression versus flow matching is an interface question", "path": "vault/reflections/reflection-reflection_59bfe9d29f3ebbb4c8a6b162.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…architecture choice affects how language-conditioned correction, visual [grounding], and action tokens share representation. This is a useful…", "match_reason": "full-text:body"}, {"id": "claim_play2perfect_finetuning_necessary_20260715", "type": "claim", "title": "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要", "path": "vault/memory/claim/claim_play2perfect_finetuning_necessary_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "…Play-only 为 0%。\n\n因此论文支持的结论是：play 预训练提供抓取和重定向先验，但在该 tight/[contact-rich] 装配设置中仍需要任务专用 RL 微调。它不意味着 Play-only 对所有装配任务均无效。", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_38651a884fe5c5c73a6e190d"}
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

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_eba0221e33968b7113f76b01`
- 编译前召回已有对象：11
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_1920583cd9c7063491d45a40-表示对齐的未来触觉-grounding.md
@@ -0,0 +1,20 @@
+---
+id: "concept_1920583cd9c7063491d45a40"
+type: "concept"
+status: "proposal"
+title: "表示对齐的未来触觉 grounding"
+created_at: "2026-07-20T18:05:58+08:00"
+updated_at: "2026-07-20T18:05:58+08:00"
+aliases: ["Representation-Aligned Future Tactile Grounding", "Latent Tactile Predictor", "LTP", "未来触觉表征对齐"]
+tags: []
+domains: ["embodied-ai", "tactile-manipulation", "vla"]
+confidence: "medium"
+source_ids: ["source_38651a884fe5c5c73a6e190d"]
+relations: [{"type": "derived_from", "target_id": "source_38651a884fe5c5c73a6e190d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都把未来触觉作为控制相关目标，但前者在 VLA 的训练期选择内部 grounding 接口，后者在分层闭环中用触觉子目标与高频残差。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_38651a884fe5c5c73a6e190d"
+reflection_context: {"reflection_ids": ["reflection_243a1a3f0cdc9450748cd215"], "importance": "high", "changed_belief": "此前触觉增强常被理解为增加输入模态或辅助损失；这里要求先验证内部接口与目标是否对齐，且多层广泛施加同一损失可能反而造成失配。", "surprising": "", "connections": [{"shared_mechanism": "两者都从动作条件的中间表示预测未来接触相关结果。", "boundary": "连接不表示生成触觉图像的跨传感器保真度已足以作为控制监督。", "difference": "VQ-Touch 面向传感器家族间的触觉图像生成；本文的 LTP 以未来紧凑触觉 latent 在策略内部约束接触控制表示。"}], "open_questions": ["在线传感器漂移或更换触觉皮肤后，如何重新验证被选中的 action-expert 接口仍是未来接触的最佳监督位置？"]}
+---
+
+# 表示对齐的未来触觉 grounding
+
+在触觉增强 VLA 中，先以冻结 probe 比较各内部表示对未来触觉状态的可预测性，再将紧凑未来触觉 latent 的预测损失施加到最能表达动作条件接触动力学的中间 action-expert 接口；该训练期约束不同于直接预测噪声较大的原始触觉，也不同于在多个接口无差别叠加损失。
```
