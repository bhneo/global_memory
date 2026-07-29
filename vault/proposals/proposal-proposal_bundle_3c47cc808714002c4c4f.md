---
id: "proposal_bundle_3c47cc808714002c4c4f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T17:24:09+08:00"
updated_at: "2026-07-27T17:24:10+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_4757ec1a2e8a0b678a350ee1"]
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
extraction_id: "extraction_cf9725f5aaa2bf9805fb6565"
input_sha256: "94a2187dbaf622d4d8e94bd48895c629ca9017090632d130674a619f86b8c43b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_bb69fa188e0417143c3277cf", "target_path": "vault/knowledge/concepts/concept_bb69fa188e0417143c3277cf-视觉-触觉-simulation-based-位姿后验用于插入-visuo-tactile-simulation-based-p.md", "base_sha256": null, "candidate_sha256": "6f74ea0b125b150fb35852fb10b5ee6f0df88497734ead2ea39890f266a98035", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3c47cc808714002c4c4f-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_bb69fa188e0417143c3277cf.md", "working_at": "2026-07-27T17:24:10+08:00"}]
existing_context: [{"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "# Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a three-part physical-agent stack: configurable visual history for navig", "match_reason": "full-text:body"}, {"id": "synthesis_be18972801786224075196eb", "type": "synthesis", "title": "灵巧操作、触觉与示范迁移：交互结构、冗余先验和物理可行性", "path": "vault/synthesis/synthesis-synthesis_be18972801786224075196eb.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91", "source_513a527cb4d410e4f94a9bb5", "source_570c26541066c02080dd8de5", "source_951559714c0383331b1b30ac", "source_b7444ef42015f4f3b6f51032", "source_e8cc1290fdb80e80f77ba2c2"], "snippet": "…完全复现人类压力分布未必最优。\n- 运动学可行性和碰撞检查能筛掉明显错误，却无法覆盖接触力、柔顺性、动量和未建模动力学。\n- 更依赖 MoCap、object [pose]、深度与系统辨识的方案可能获得更强控制，但会降低在野数据采集和开放部署能力。\n\n## Candidate hypotheses\n\n[\n  {\n    \"statement\": \"在人到机器人灵巧示范迁移中，先保留手—物交互结构，再通过本体特定的运动学…", "match_reason": "full-text:body"}, {"id": "claim_play2perfect_inhand_pretraining_20260715", "type": "claim", "title": "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动", "path": "vault/memory/claim/claim_play2perfect_inhand_pretraining_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "…三个种子上比较下游 RL 微调。结果显示，更多物体、随机目标轨迹、完整 6D [pose] objective 和更精确的目标容差通常带来更快或更稳定的迁移。\n\n其中 orientation control 是关键条件：Translation-only 能学到抓取和抬升…", "match_reason": "full-text:body"}, {"id": "concept_64c23c660c9017a5bf73d012", "type": "concept", "title": "Consecutive hand-object subgoal teleoperation", "path": "vault/memory/concept/concept_64c23c660c9017a5bf73d012.md", "status": "working", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object [pose]…", "match_reason": "full-text:body"}, {"id": "reflection_70226423f917bfceeef74a93", "type": "reflection", "title": "REGRIND：单示范有效的前提是保留手—物交互结构而非只复制姿态", "path": "vault/reflections/reflection-reflection_70226423f917bfceeef74a93.md", "status": "active", "source_ids": ["source_b7444ef42015f4f3b6f51032"], "snippet": "…REGRIND 仅覆盖四个 task-hand setting，并依赖动作捕捉、object [pose] 与细致系统辨识；在野视觉和未知物体状态仍未解决。\n  Difference: REGRIND 用 hand-object keypoint mesh 和…", "match_reason": "full-text:body"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…The system depends on reliable MoCap estimates of hand and object [pose], and simulation does not cover all…", "match_reason": "full-text:body"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:domains"}, {"id": "reflection_052db872e2258b0e016c5ebf", "type": "reflection", "title": "UR-VC：先纠正进度代理，再训练价值或优势条件策略", "path": "vault/reflections/reflection-reflection_052db872e2258b0e016c5ebf.md", "status": "active", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# UR-VC：先纠正进度代理，再训练价值或优势条件策略\n\n## Why important\n\n它指出成功示范中的归一化时间并不等于物理进度，尤其接触和可变形物体任务会倒退、停滞或速度不均；错误代理会污染后续价值与优势监督。\n\n## What changed\n\n价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n\n## Surprising\n\nUR…", "match_reason": "metadata:domains"}, {"id": "input_bb9068321957f044c9f1310a", "type": "input", "title": "Robo-ValueRL", "path": "vault/inputs/input-input_bb9068321957f044c9f1310a.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "…Reliable Value [Estimation] for Offline-to-Online Reinforcement Learning Wenke Xia 1,* , Pei Ren 2,* , Wenbo Yu 3…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_4757ec1a2e8a0b678a350ee1"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "15dc1eb71b077f8a63965a18bcfd38cbc1d4b7dc994789fdfcd47519b3ea5859"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_cf9725f5aaa2bf9805fb6565`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_bb69fa188e0417143c3277cf-视觉-触觉-simulation-based-位姿后验用于插入-visuo-tactile-simulation-based-p.md
@@ -0,0 +1,20 @@
+---
+id: "concept_bb69fa188e0417143c3277cf"
+type: "concept"
+status: "proposal"
+title: "视觉—触觉 simulation-based 位姿后验用于插入 / visuo-tactile simulation-based pose posterior for insertion"
+created_at: "2026-07-27T17:24:09+08:00"
+updated_at: "2026-07-27T17:24:09+08:00"
+aliases: ["BayesContact", "视觉触觉位姿后验", "visuo-tactile pose posterior"]
+tags: []
+domains: ["robotics", "tactile-sensing", "bayesian-inference"]
+confidence: "medium"
+source_ids: ["source_4757ec1a2e8a0b678a350ee1"]
+relations: [{"type": "derived_from", "target_id": "source_4757ec1a2e8a0b678a350ee1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_4757ec1a2e8a0b678a350ee1"
+reflection_context: {"reflection_ids": ["reflection_438aaa4e8fa10fc299c05d87"], "importance": "high", "changed_belief": "我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。", "surprising": "", "connections": [{"shared_mechanism": "两者都用视觉和接触信息缩小接触操作中的状态不确定性。", "boundary": "本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。", "difference": "深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。"}], "open_questions": ["接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？"]}
+---
+
+# 视觉—触觉 simulation-based 位姿后验用于插入 / visuo-tactile simulation-based pose posterior for insertion
+
+在 peg-in-hole 插入中，可用粒子表示物体位姿 belief，并以深度观测和由力/力矩导出的接触证据通过仿真前向模型进行 simulation-based 更新；该方法输出可随接触更新的后验而非单点位姿。其有效性依赖接触与传感仿真的模型保真度及论文的任务设置，未保证对任意几何、摩擦或环境零样本泛化。
```
