---
id: "proposal_bundle_05dba53c3c9f85990185"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-23T18:07:07+08:00"
updated_at: "2026-07-23T18:07:07+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_c2d7b53bd1c40ed0af8ea5cb"]
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
extraction_id: "extraction_753d2dd08ee34e71cdb2fa02"
input_sha256: "23d7d8083a28139b6e95055de37e54f3ffe53ec02b4e2631e799ec9b8c9b56cc"
bundle_items: [{"item_id": "tension-1", "object_type": "tension", "action": "create", "target_id": "tension_bae77e2f84604668cacedd6c", "target_path": "vault/frontier/tensions/tension_bae77e2f84604668cacedd6c-世界预测可解释性与动作对齐安全之间的张力.md", "base_sha256": null, "candidate_sha256": "506193d5a44e7f2d2113fdac56bd0761d24afa094befe32152f230ce9ded790b", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_05dba53c3c9f85990185-tension-1.md", "base_path": null, "working_path": "vault/memory/tension/tension_bae77e2f84604668cacedd6c.md", "working_at": "2026-07-23T18:07:07+08:00"}]
existing_context: [{"id": "reflection_65fb6fe12e2291077f28900c", "type": "reflection", "title": "DemoBridge: single-view demonstration transfer needs simulator-in-the-loop feasibility", "path": "vault/reflections/reflection-reflection_65fb6fe12e2291077f28900c.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…Perception proposes geometry and phase, planning checks embodiment feasibility, and simulation backtracks [when] the proposed motion fails.\n\n## Surprising…", "match_reason": "full-text:body"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World Action] Model\n\n默认由 [World Action] Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:aliases"}, {"id": "concept_09dc6e910b167ba474c89c38", "type": "concept", "title": "世界动作模型的激活空间鲁棒性 steering", "path": "vault/memory/concept/concept_09dc6e910b167ba474c89c38.md", "status": "working", "source_ids": ["source_38cba686373b003398483ab2"], "snippet": "# 世界动作模型的激活空间鲁棒性 steering\n\n对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。", "match_reason": "metadata:aliases"}, {"id": "concept_action_centered_joint_world_action_model", "type": "concept", "title": "动作中心的联合世界—动作模型", "path": "vault/memory/concept/concept_action_centered_joint_world_action_model.md", "status": "working", "source_ids": ["source_e2614742b0c3ee7cf985d616"], "snippet": "# 动作中心的联合世界—动作模型\n\nGigaWorld-Policy-0.5 以视觉专家和动作专家构成 Mixture-of-Transformers，在因果注意力约束下从当前多视角观察、机器人状态和语言同时预测动作块与未来视觉 token，并配合 KV cache 等推理加速。它提供的是特定系统中联合世界…", "match_reason": "metadata:aliases"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "full-text:body"}, {"id": "reflection_a74b334857543499d8111c64", "type": "reflection", "title": "FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口", "path": "vault/reflections/reflection-reflection_a74b334857543499d8111c64.md", "status": "active", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# FlowWAM：光流把视频先验、动作预测和世界建模放进同一运动接口\n\n## Why important\n\nFlowWAM 把 optical flow 从辅助视觉信号提升为主要动作表示：它既与预训练视频生成器的输入格式兼容，又保留逐像素跨帧运动，并可解码回机器人动作。\n\n## What changed\n\n此前容易把 [World Action]…", "match_reason": "metadata:domains"}, {"id": "concept_59f92bcb786f695ddcd47f7f", "type": "concept", "title": "视频原生的光流动作接口", "path": "vault/memory/concept/concept_59f92bcb786f695ddcd47f7f.md", "status": "working", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# 视频原生的光流动作接口\n\n用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。", "match_reason": "metadata:domains"}, {"id": "reflection_aeafd32447e03d5456e70a02", "type": "reflection", "title": "GigaWorld-Policy-0.5：动作与未来视觉联合建模需要独立验证闭环收益", "path": "vault/reflections/reflection-reflection_aeafd32447e03d5456e70a02.md", "status": "active", "source_ids": ["source_e2614742b0c3ee7cf985d616"], "snippet": "# GigaWorld-Policy-0.5：动作与未来视觉联合建模需要独立验证闭环收益\n\n## Why important\n\n该工作把 WAM 的动作生成、未来视觉预测和推理加速放在同一系统中，并用自动研究流程搜索训练配方，适合检验世界预测是否真正改善闭环控制。\n\n## What changed\n\n联合未来视觉损失不能直接视为世界模型能力；必须分别检查动作成功率、预测质量…", "match_reason": "metadata:domains"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The world component and dual-system [world-action] models both use predictive representations to connect perception with possible…", "match_reason": "full-text:body"}, {"id": "architecture_simple_simulation_policy_loop", "type": "architecture", "title": "SIMPLE 仿真策略学习与评测环境", "path": "vault/memory/architecture/architecture_simple_simulation_policy_loop.md", "status": "working", "source_ids": ["source_d75524a9040845cdc76db35c"], "snippet": "# SIMPLE 仿真策略学习与评测环境\n\nSIMPLE 是面向具身策略的数据生成、微调和仿真评测环境，覆盖多种机器人、场景资产和人形全身移动操作任务，并集成多类 VLA 与 [World Action] Model。", "match_reason": "full-text:body"}, {"id": "reflection_bfb923cbbf75ed8a49f9df44", "type": "reflection", "title": "Xiaomi-Robotics-U0：世界基础模型可同时承担具身生成器与数据引擎", "path": "vault/reflections/reflection-reflection_bfb923cbbf75ed8a49f9df44.md", "status": "active", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "…与双系统 [World Action] Model 都复用视频生成先验来表示未来交互，并服务下游动作策略。\n  Boundary: U0 的场景生成与视频生成仍分离，长 rollout 会累积误差；深度中间表示会引入细节伪影，32K context 也限制长时程。\n  Difference: 双系统…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-Action [Models] with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "input_bf6f63ea23391740118ba725", "type": "input", "title": "Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema", "path": "vault/inputs/input-input_bf6f63ea23391740118ba725.md", "status": "active", "source_ids": ["source_d90b4e9bf278dfc5e68d1bb5"], "snippet": "# Frontier [Models] with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema\n\nInput Episode for `source_d90b4e9bf278dfc5e68d1bb5…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied Foundation [Models] for Real-World Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_c2d7b53bd1c40ed0af8ea5cb"}
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
- Extraction：`extraction_753d2dd08ee34e71cdb2fa02`
- 编译前召回已有对象：14
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### tension-1 (create tension)

```diff
--- /dev/null
+++ candidate:vault/frontier/tensions/tension_bae77e2f84604668cacedd6c-世界预测可解释性与动作对齐安全之间的张力.md
@@ -0,0 +1,20 @@
+---
+id: "tension_bae77e2f84604668cacedd6c"
+type: "tension"
+status: "proposal"
+title: "世界预测可解释性与动作对齐安全之间的张力"
+created_at: "2026-07-23T18:07:07+08:00"
+updated_at: "2026-07-23T18:07:07+08:00"
+aliases: ["World-Action Alignment Tension", "BadWAM", "世界动作对齐张力"]
+tags: []
+domains: ["world-action-model", "robot-safety"]
+confidence: "medium"
+source_ids: ["source_c2d7b53bd1c40ed0af8ea5cb"]
+relations: [{"type": "derived_from", "target_id": "source_c2d7b53bd1c40ed0af8ea5cb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_action_centered_joint_world_action_model", "reason": "两者均涉及动作与未来表征的联合输出；该张力指出联合输出仍需针对二者对齐进行独立验收。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_c2d7b53bd1c40ed0af8ea5cb"
+reflection_context: {"reflection_ids": ["reflection_dc9e5944bbe8d789e0935906"], "importance": "high", "changed_belief": "世界动作模型的预测质量与闭环动作正确性必须分别验证；未来画面未明显漂移并不蕴含动作仍与该未来一致。", "surprising": "", "connections": [{"shared_mechanism": "两者都依赖未来表征与动作输出的联合建模。", "boundary": "该连接仅说明联合建模存在需要验证的接口，不说明所有世界动作模型或所有扰动都会发生同类攻击。", "difference": "既有动作中心联合世界—动作模型描述生成架构；BadWAM 聚焦该架构中想象与执行可被脱钩的安全失败模式。"}], "open_questions": []}
+---
+
+# 世界预测可解释性与动作对齐安全之间的张力
+
+世界动作模型可用预测未来作为动作后果的可解释表示，但视觉扰动可能使预测未来保持表面合理而动作输出偏离该未来并导致任务失败。因此，未来预测质量不能单独充当动作安全或闭环正确性的充分验收条件。
```
