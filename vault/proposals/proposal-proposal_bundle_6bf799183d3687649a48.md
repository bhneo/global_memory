---
id: "proposal_bundle_6bf799183d3687649a48"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-22T18:12:08+08:00"
updated_at: "2026-07-22T18:12:09+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9b0d550203c4d7bd7acf8a36"]
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
extraction_id: "extraction_2008a8fa5ae1732eada45c25"
input_sha256: "29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_149582520594364a508516c6", "target_path": "vault/knowledge/concepts/concept_149582520594364a508516c6-查询介导的-vla-动作表征塑形.md", "base_sha256": null, "candidate_sha256": "18dbf30f24c377f356a3539042c45ab7ea48eac74bfd0be49ebfdf0679a72c13", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_6bf799183d3687649a48-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_149582520594364a508516c6.md", "working_at": "2026-07-22T18:12:09+08:00"}]
existing_context: [{"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World [Action] Model\n\n默认由 World [Action] Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 latent [action]\n\n## Why important\n\nWALA 不从原始像素重建 latent [action]，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex [Structured] Demonstrations for Vision-Language-Action Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_9443d1789c9a179bd1611be3", "type": "concept", "title": "示范先验条件化的 VLA 结构化探索", "path": "vault/memory/concept/concept_9443d1789c9a179bd1611be3.md", "status": "working", "source_ids": ["source_5b8c57a9bef3348109f3b7bb"], "snippet": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。", "match_reason": "metadata:aliases"}, {"id": "reflection_bfb923cbbf75ed8a49f9df44", "type": "reflection", "title": "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎", "path": "vault/reflections/reflection-reflection_bfb923cbbf75ed8a49f9df44.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "…What changed\n\n此前常把具身 world model 视为预测下一帧或规划 rollout；该工作把 [structured] multi-view editing 也纳入世界模型接口，强调数据生成与动力学建模可以共享基础模型但需要不同一致性约束。\n\n## Surprising\n\n论文报告用零样本生成的多视角关键帧扩增数据后，π0.5…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…safety refusal mechanisms work in code?\n\n## Possible mechanisms\n\n- [Structured] world state and post-action observation make deviations measurable…", "match_reason": "full-text:body"}, {"id": "concept_17750931a381f8453b27ccba", "type": "concept", "title": "连续曲线动作接口与执行重定时", "path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "status": "working", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "match_reason": "metadata:aliases"}, {"id": "concept_1920583cd9c7063491d45a40", "type": "concept", "title": "表示对齐的未来触觉 grounding", "path": "vault/memory/concept/concept_1920583cd9c7063491d45a40.md", "status": "working", "source_ids": ["source_38651a884fe5c5c73a6e190d"], "snippet": "# 表示对齐的未来触觉 grounding\n\n在触觉增强 VLA 中，先以冻结 probe 比较各内部表示对未来触觉状态的可预测性，再将紧凑未来触觉 latent 的预测损失施加到最能表达动作条件接触动力学的中间 action-expert 接口；该训练期约束不同于直接预测噪声较大的原始触觉，也不同于在多个接口无差别叠加损失。", "match_reason": "metadata:aliases"}, {"id": "claim_wechat_cross_modal_representation_alignment_20260716", "type": "claim", "title": "该文称文本模型与视觉模型随能力增强也呈现更强表征一致性，并以颜色表征与人类感知一致为例", "path": "vault/memory/claim/claim_wechat_cross_modal_representation_alignment_20260716.md", "status": "working", "source_ids": ["source_f35b44d4bd383fb26ca49165"], "snippet": "# 跨模态对齐\n\n文本与视觉表征趋同；颜色例为二手引述。", "match_reason": "metadata:tags"}, {"id": "concept_59f92bcb786f695ddcd47f7f", "type": "concept", "title": "视频原生的光流动作接口", "path": "vault/memory/concept/concept_59f92bcb786f695ddcd47f7f.md", "status": "working", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# 视频原生的光流动作接口\n\n用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。", "match_reason": "metadata:domains"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "metadata:domains"}, {"id": "reflection_0db16c2a58084d442087245e", "type": "reflection", "title": "GR00T N1.7：跨本体迁移依赖共享动作语义而非仅共享骨干", "path": "vault/reflections/reflection-reflection_0db16c2a58084d442087245e.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "# GR00T N1.7：跨本体迁移依赖共享动作语义而非仅共享骨干\n\n## Why important\n\nGR00T N1.7 把相对末端执行器动作空间与人类视频预训练放在同一迁移链路中：只有当人类与机器人数据能够共享动作变化的参照语义时，人类视觉经验才更可能转化为机器人控制先验。\n\n## What changed\n\n此前跨本体通用 VLA 主要被描述为数据混合和统一接口问题；该材料进一步表明…", "match_reason": "metadata:domains"}, {"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline Policy：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:domains"}, {"id": "reflection_a74b334857543499d8111c64", "type": "reflection", "title": "FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口", "path": "vault/reflections/reflection-reflection_a74b334857543499d8111c64.md", "status": "active", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口\n\n## Why important\n\nFlowWAM 把 optical flow 从辅助视觉信号提升为主要动作表示：它既与预训练视频生成器的输入格式兼容，又保留逐像素跨帧运动，并可解码回机器人动作。\n\n## What changed\n\n此前容易把 World Action…", "match_reason": "metadata:domains"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口\n\n## Why important\n\n它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 actor-critic 通过紧凑 RL token 在少量真机交互中适应精密阶段…", "match_reason": "metadata:domains"}, {"id": "reflection_a4abd223b36c137fb9bd6ae4", "type": "reflection", "title": "Mixture of Frames：动作分布复杂度部分来自坐标系选择", "path": "vault/reflections/reflection-reflection_a4abd223b36c137fb9bd6ae4.md", "status": "active", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "# Mixture of Frames：动作分布复杂度部分来自坐标系选择\n\n## Why important\n\nMoF 说明同一操作动作在夹爪、基座或相对轨迹坐标系中具有不同统计复杂度，且最合适坐标系会随任务阶段变化；策略可以并行去噪多个 frame 专家而非固定一个表示。\n\n## What changed\n\n此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9b0d550203c4d7bd7acf8a36"}
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
- Extraction：`extraction_2008a8fa5ae1732eada45c25`
- 编译前召回已有对象：18
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_149582520594364a508516c6-查询介导的-vla-动作表征塑形.md
@@ -0,0 +1,20 @@
+---
+id: "concept_149582520594364a508516c6"
+type: "concept"
+status: "proposal"
+title: "查询介导的 VLA 动作表征塑形"
+created_at: "2026-07-22T18:12:08+08:00"
+updated_at: "2026-07-22T18:12:08+08:00"
+aliases: ["Query-Mediated VLA Action Representation Shaping", "Action QFormer", "动作 QFormer"]
+tags: []
+domains: ["vla", "representation-learning"]
+confidence: "medium"
+source_ids: ["source_9b0d550203c4d7bd7acf8a36"]
+relations: [{"type": "derived_from", "target_id": "source_9b0d550203c4d7bd7acf8a36", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_action_centric_embodied_vlm_taxonomy", "reason": "两者关注把多模态表征组织成可行动信息；本概念额外限定训练时动作梯度的接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_9b0d550203c4d7bd7acf8a36"
+reflection_context: {"reflection_ids": ["reflection_63063bb66f27ff296bc9d7d2"], "importance": "high", "changed_belief": "动作接口不只是从表征读取控制量的末端模块，它还决定动作损失如何回写视觉语言通路。", "surprising": "", "connections": [{"shared_mechanism": "两者都通过显式中间接口约束高层表示如何影响动作。", "boundary": "该连接不说明接口设计可替代障碍规避、规划或真实接触验证。", "difference": "Action QFormer 是训练时查询接口；现有分类概念描述的是具身 VLM 的功能组织。"}], "open_questions": ["查询接口在接触操作和长时程重规划中是否仍能避免语言侧表征退化？"]}
+---
+
+# 查询介导的 VLA 动作表征塑形
+
+在预训练多模态骨干和动作策略头之间插入由指令条件化查询构成的动作接口，以先重组继承表征再预测动作，并让部分动作损失经该接口传播。该机制在论文的零样本仿真到真实导航设置中改善闭环结果，但不单独解决障碍感知规划。
```
