---
id: "proposal_bundle_2497f86721e472e3b8a5"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.11643v1.pdf"
created_at: "2026-07-20T12:39:13+08:00"
updated_at: "2026-07-20T12:39:14+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_fe986df678d73ef2b6234f0c"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-c-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.11643v1.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a0841e0d27a34cdc2d648e31"
input_sha256: "01b968b3080e6992746fbf1ae073bdb99e560d6fabab66c4fe31e06ee7212f20"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_27970fb0de0d8995774e31f6", "target_path": "vault/knowledge/concepts/concept_27970fb0de0d8995774e31f6-多视角具身合成世界模型数据引擎.md", "base_sha256": null, "candidate_sha256": "cd2dfa2768e307abacf9d53dbaa146f3f006b9eb39678e636bd6c27a9f5398a8", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_2497f86721e472e3b8a5-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_27970fb0de0d8995774e31f6.md", "working_at": "2026-07-20T12:39:14+08:00"}]
existing_context: [{"id": "input_0c37ad2ab47dfef7536c9850", "type": "input", "title": "2607.11643v1.pdf", "path": "vault/inputs/input-input_0c37ad2ab47dfef7536c9850.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.11643v1.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/01/b9/01b968b3080e6992746fbf1ae073bdb99e560d6fabab66c4fe31e06ee7212f20](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "concept_end_to_end_embodied_reproducibility", "type": "concept", "title": "端到端具身系统可复现性", "path": "vault/memory/concept/concept_end_to_end_embodied_reproducibility.md", "status": "working", "source_ids": ["source_650f616f1e641912e73115b1"], "snippet": "# 端到端具身系统可复现性\n\n把机械设计与物料清单、低层控制、数据转换、训练配方和推理部署视为同一可复现边界；只开放模型权重或微调代码不足以复现实机具身系统。", "match_reason": "metadata:aliases"}, {"id": "concept_portable_embodied_inference_runtime", "type": "concept", "title": "可移植具身推理运行时", "path": "vault/memory/concept/concept_portable_embodied_inference_runtime.md", "status": "working", "source_ids": ["source_c46b1e0305ec5c9adba634f1"], "snippet": "# 可移植具身推理运行时\n\n面向闭环机器人控制的统一运行时契约：以多速率组件调度、低时延低抖动的 batch-1 执行、可插拔模型头与具身 I/O，把稳定推理核心和模型/机器人专属适配分离。", "match_reason": "metadata:aliases"}, {"id": "concept_f67f822ee20789d74d7b75e3", "type": "concept", "title": "物理失败合成驱动的稠密机器人奖励建模", "path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "status": "working", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# 物理失败合成驱动的稠密机器人奖励建模\n\n通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。", "match_reason": "metadata:aliases"}, {"id": "synthesis_77d12a9c578c8e5a6223bff4", "type": "synthesis", "title": "具身泛化中的中间表示、接口解耦与动作落差", "path": "vault/synthesis/synthesis-synthesis_77d12a9c578c8e5a6223bff4.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277", "source_61f3045b170e78e4adb2422c", "source_886372de22c708b28cd11e4b", "source_be9781ec8ca637c5dfd8fabb", "source_d83bb2c45bcaf70906e9ac96"], "snippet": "# 具身泛化中的中间表示、接口解耦与动作落差\n\n## Emerging patterns\n\n- 多种具身系统都在端到端感知—动作映射中插入有结构的中间层：可变长度潜推理、可复用技能库、世界预测通道、视觉瓶颈或指向式动作接口；这些中间层的共同作用不是增加抽象数量，而是隔离任务相关内容与本体、相机、行为风格或计算预算等干扰因素。\n- 表征泛化与动作泛化应被拆开：模型可以共享世界变化、聚焦正确对象或学习通用技能先验，却仍需要本体相关动作解码…", "match_reason": "metadata:tags"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "# VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预\n\n## Emerging patterns\n\n- VLA 后训练的瓶颈不只是优化算法，而是基础策略向纠正过程暴露什么反馈接口：进度标签、价值、内部 token、动作块或生成潜变量。\n- 五条路径都试图保留预训练行为先验，只把学习压力放到较小的标签、读出…", "match_reason": "metadata:tags"}, {"id": "synthesis_fe1750531bf1b2a79846b657", "type": "synthesis", "title": "具身策略部署中的监督通道、动作接口与反馈时标", "path": "vault/synthesis/synthesis-synthesis_fe1750531bf1b2a79846b657.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_91072aa553af99e6ab97c6cd"], "snippet": "# 具身策略部署中的监督通道、动作接口与反馈时标\n\n## Emerging patterns\n\n- 真实部署泛化不是单一共享表示问题，而是至少包含三层契约：训练时选择跨本体较稳定的监督变量，策略输出时选择可比较的动作坐标，执行时按环境变化速度配置反馈与纠错回路。\n- 计算效率和控制鲁棒性共同依赖失效边界。ActionCache 需要判断何时拒绝陈旧动作，TouchWorld 需要判断何时由高频残差吸收误差、何时上升到高层重规划；二者都不是无条件复用。\n- 数据组织、动作表示和未来预测分别作用于学习分布…", "match_reason": "metadata:tags"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_fe986df678d73ef2b6234f0c"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.11643v1.pdf

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-c-20260720`
- Extraction：`extraction_a0841e0d27a34cdc2d648e31`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_27970fb0de0d8995774e31f6-多视角具身合成世界模型数据引擎.md
@@ -0,0 +1,20 @@
+---
+id: "concept_27970fb0de0d8995774e31f6"
+type: "concept"
+status: "proposal"
+title: "多视角具身合成世界模型数据引擎"
+created_at: "2026-07-20T12:39:13+08:00"
+updated_at: "2026-07-20T12:39:13+08:00"
+aliases: ["Embodied world-foundation data engine", "Xiaomi-Robotics-U0", "统一具身合成"]
+tags: []
+domains: ["embodied-ai", "world-model", "data-engine", "multiview-generation"]
+confidence: "medium"
+source_ids: ["source_fe986df678d73ef2b6234f0c"]
+relations: [{"type": "derived_from", "target_id": "source_fe986df678d73ef2b6234f0c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dual_system_world_action_model", "reason": "二者都复用视频生成先验服务机器人动作；数据引擎扩展训练分布，双系统 WAM 组织运行时推理。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_fe986df678d73ef2b6234f0c"
+reflection_context: {"reflection_ids": ["reflection_bfb923cbbf75ed8a49f9df44"], "importance": "high", "changed_belief": "此前常把具身 world model 视为预测下一帧或规划 rollout；该工作把 structured multi-view editing 也纳入世界模型接口，强调数据生成与动力学建模可以共享基础模型但需要不同一致性约束。", "surprising": "论文报告用零样本生成的多视角关键帧扩增数据后，π0.5 在所选真机 OOD 条件下成功率从 36.9% 提升到 63.2%，但这证明的是特定增广管线收益，不是生成视频已具备完整物理真实性。", "connections": [{"shared_mechanism": "与双系统 World Action Model 都复用视频生成先验来表示未来交互，并服务下游动作策略。", "boundary": "U0 的场景生成与视频生成仍分离，长 rollout 会累积误差；深度中间表示会引入细节伪影，32K context 也限制长时程。", "difference": "双系统 WAM 关注运行时快慢动作推理；U0 更像多任务具身合成基础模型和可控数据增广引擎。"}], "open_questions": ["怎样用几何、接触和策略闭环指标筛掉视觉上合理但控制上有害的合成轨迹？"]}
+---
+
+# 多视角具身合成世界模型数据引擎
+
+在保留通用图像与视频生成能力的同时，联合学习多视角具身场景、跨本体结构化编辑和具身视频，使世界基础模型既能预测交互也能生成受机器人与相机约束的策略训练数据。合成数据仍需通过几何、接触和闭环收益验证。
```
