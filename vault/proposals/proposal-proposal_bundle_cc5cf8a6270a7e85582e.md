---
id: "proposal_bundle_cc5cf8a6270a7e85582e"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T18:08:44+08:00"
updated_at: "2026-07-21T18:08:44+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_adcddc61e96d32f765d29c90"]
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
extraction_id: "extraction_95e7396c8933352c28515ee3"
input_sha256: "6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_705dff5d5d3ebdcb87f1564f", "target_path": "vault/knowledge/concepts/concept_705dff5d5d3ebdcb87f1564f-形态可重构机器人的跨本体控制边界.md", "base_sha256": null, "candidate_sha256": "7c6e5e7ad1ac3e83f88a8f04f243231d0d3e7fbea21d942593fd536335b13539", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_cc5cf8a6270a7e85582e-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_705dff5d5d3ebdcb87f1564f.md", "working_at": "2026-07-21T18:08:44+08:00"}]
existing_context: [{"id": "work_arxiv_2606_26428", "type": "work", "title": "Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?", "path": "vault/memory/work/work_arxiv_2606_26428.md", "status": "working", "source_ids": ["source_05d8a9da9e0b53b94872f2a7", "source_ea5eb55121fccd1ed14a40b0"], "snippet": "…What Matters in [Dexterous] Play Pretraining for Precise Assembly?\n\n## Logical work identity\n\n- arXiv：`2606.26428`\n- Version：`unknown`\n- Captures…", "match_reason": "metadata:title"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…dexterous teleoperation through consecutive [hand]-object subgoals\n\n## Why important\n\nTELEDEXTER represents operator intent as consecutive [hand]-object co…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation Model for [Dexterous] Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "claim_play2perfect_realworld_tight_insertion_20260715", "type": "claim", "title": "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10", "path": "vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 的真实世界紧配合插入结果\n\n论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 real-world finetuning…", "match_reason": "metadata:tags"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:tags"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "…alignment 与安全约束纳入迁移目标和评测，直接暴露纯运动学 imitation 的物理缺口。\n\n## What changed\n\n此前人到机器人 [dexterous] transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。\n\n## Surprising\n\n纯运动学 baseline 的…", "match_reason": "metadata:domains"}, {"id": "concept_64c23c660c9017a5bf73d012", "type": "concept", "title": "Consecutive hand-object subgoal teleoperation", "path": "vault/memory/concept/concept_64c23c660c9017a5bf73d012.md", "status": "working", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "# Consecutive [hand]-object subgoal teleoperation\n\nTranslate live human intent into consecutive [hand]-object co-tracking subgoals, then let…", "match_reason": "metadata:title"}, {"id": "claim_play2perfect_inhand_pretraining_20260715", "type": "claim", "title": "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动", "path": "vault/memory/claim/claim_play2perfect_inhand_pretraining_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "…Translation-only 能学到抓取和抬升，但没有提供装配所需的 in-[hand] reorientation 先验；10 cm 的宽松目标容差也无法形成精确物体姿态控制。作者据此总结，play 最好迫使机器人用手指进行 in-[hand] manipulation，而不是依赖固定抓握下的手臂运动。", "match_reason": "metadata:title"}, {"id": "concept_interaction_structure_preserving_demonstration_prior", "type": "concept", "title": "手—物交互结构保真的示范先验", "path": "vault/memory/concept/concept_interaction_structure_preserving_demonstration_prior.md", "status": "working", "source_ids": ["source_b7444ef42015f4f3b6f51032"], "snippet": "# 手—物交互结构保真的示范先验\n\n从人类示范中保留手指、物体与任务关键点之间的空间—接触关系，把该关系作为机器人 reference 与探索邻域，再由本体特定的运动学、残差控制或仿真门禁求解可执行动作。该先验比逐关节姿态更接近任务结构，但受物体状态可观测性、示范接触拓扑和系统辨识范围限制。", "match_reason": "metadata:aliases"}, {"id": "reflection_70226423f917bfceeef74a93", "type": "reflection", "title": "REGRIND：单示范有效的前提是保留手—物交互结构而非只复制姿态", "path": "vault/reflections/reflection-reflection_70226423f917bfceeef74a93.md", "status": "active", "source_ids": ["source_b7444ef42015f4f3b6f51032"], "snippet": "# REGRIND：单示范有效的前提是保留手—物交互结构而非只复制姿态\n\n## Why important\n\nREGRIND 从单个人类示范构造 [hand]-object interaction mesh 与 object-centric keypoint reference，把 reference…", "match_reason": "full-text:body"}, {"id": "synthesis_be18972801786224075196eb", "type": "synthesis", "title": "灵巧操作、触觉与示范迁移：交互结构、冗余先验和物理可行性", "path": "vault/synthesis/synthesis-synthesis_be18972801786224075196eb.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_951559714c0383331b1b30ac", "source_b7444ef42015f4f3b6f51032", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…mesh 与 residual RL，TactiDex 显式监督触觉时空和力，TELEDEXTER 在线执行连续 [hand]-object subgoals。\"\n  },\n  {\n    \"shared_mechanism\": \"PAKE 与 REGRIND 都把结构化 reference…", "match_reason": "full-text:body"}, {"id": "input_ab5a33edd49eec243cb3862f", "type": "input", "title": "DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting", "path": "vault/inputs/input-input_ab5a33edd49eec243cb3862f.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…I Introduction II Related Work Collecting manipulation demonstrations [Hand]-to-robot retargeting III System Overview IV Design Choices…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_adcddc61e96d32f765d29c90"}
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
- Extraction：`extraction_95e7396c8933352c28515ee3`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_705dff5d5d3ebdcb87f1564f-形态可重构机器人的跨本体控制边界.md
@@ -0,0 +1,20 @@
+---
+id: "concept_705dff5d5d3ebdcb87f1564f"
+type: "concept"
+status: "proposal"
+title: "形态可重构机器人的跨本体控制边界"
+created_at: "2026-07-21T18:08:44+08:00"
+updated_at: "2026-07-21T18:08:44+08:00"
+aliases: ["Morphology-Reconfigurable Robot Cross-Embodiment Control Boundary", "Handroid", "形态可重构跨本体控制"]
+tags: []
+domains: ["embodied-ai", "dexterous-manipulation", "humanoid-robotics"]
+confidence: "medium"
+source_ids: ["source_adcddc61e96d32f765d29c90"]
+relations: [{"type": "derived_from", "target_id": "source_adcddc61e96d32f765d29c90", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_end_to_end_embodied_reproducibility", "reason": "二者均把硬件、控制和部署视为能力声明的一部分；前者聚焦形态切换带来的接口变化，后者强调完整可复现边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_adcddc61e96d32f765d29c90"
+reflection_context: {"reflection_ids": ["reflection_b36ae3f4f0dfb6a2942e94ab"], "importance": "high", "changed_belief": "此前把手部灵巧性和人形移动操作当作独立平台问题；该平台表明可复用关节模块可以形成共同实验边界，但重构后仍会改变自由度的功能分配和控制目标。", "surprising": "", "connections": [{"shared_mechanism": "两者都要求在明确本体和控制接口的条件下验证端到端具身能力。", "boundary": "连接不表示一个可重构硬件平台已经证明通用跨形态策略迁移。", "difference": "Handroid在物理模块层重构手与人形；端到端具身系统可复现性覆盖从机械设计到训练和部署的完整工程发布边界。"}], "open_questions": ["哪些表示或控制模块能够在形态切换时复用，哪些必须因接触几何、可达性和稳定性约束而重新训练？"]}
+---
+
+# 形态可重构机器人的跨本体控制边界
+
+将同一组可重用机电关节模块配置为灵巧手或人形身体，并在各形态下采用相应遥操作、抓取、在手操作、步态或全身控制接口的实验平台；共享硬件不消除由接触几何、任务角色和稳定性约束导致的控制差异。
```
