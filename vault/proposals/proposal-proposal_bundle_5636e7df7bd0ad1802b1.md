---
id: "proposal_bundle_5636e7df7bd0ad1802b1"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T11:55:51+08:00"
updated_at: "2026-07-20T11:55:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_40700e61702f4b5a5765e11d"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_4fd58691d04124ef005981f1"
input_sha256: "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_f9a9f1d1818632c0380b7942", "target_path": "vault/knowledge/concepts/concept_f9a9f1d1818632c0380b7942-vla-的强化学习读出接口.md", "base_sha256": null, "candidate_sha256": "ae071f337fbafeeced37bcd21a8a60c7e3aee808b4dc78f3d2c61b2f25f8a8fa", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_5636e7df7bd0ad1802b1-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "working_at": "2026-07-20T11:55:51+08:00"}]
existing_context: [{"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "# VLA 后训练的反馈接口：价值、[Token]、动作块与潜空间干预\n\n## Emerging patterns\n\n- VLA 后训练的瓶颈不只是优化算法，而是基础策略向纠正过程暴露什么反馈接口：进度标签、价值、内部 [token]、动作块或生成潜变量。\n- 五条路径都试图保留预训练行为先验，只把学习压力放到较小的标签、读出…", "match_reason": "metadata:title"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口\n\n## Why important\n\n它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 actor-critic 通过紧凑 RL token 在少量真机交互中适应精密阶段…", "match_reason": "metadata:domains"}, {"id": "concept_4739daf4ef7eacc9153c535f", "type": "concept", "title": "可靠价值驱动的离线到在线策略改进", "path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "status": "working", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "match_reason": "metadata:aliases"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、Long 成功率分别为 `97.2…", "match_reason": "metadata:tags"}, {"id": "reflection_617843f93885fb6b0d3c5f52", "type": "reflection", "title": "Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口", "path": "vault/reflections/reflection-reflection_617843f93885fb6b0d3c5f52.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "# Robo-ValueRL：价值可靠性是离线经验进入在线改进的接口\n\n## Why important\n\n它把价值函数从训练配件提升为贯穿数据筛选、质量条件策略学习和在线残差适应的接口，并强调历史条件价值对遮挡、重复动作和相似阶段歧义的处理。\n\n## What changed\n\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度…", "match_reason": "metadata:domains"}, {"id": "input_bb9068321957f044c9f1310a", "type": "input", "title": "Robo-ValueRL", "path": "vault/inputs/input-input_bb9068321957f044c9f1310a.md", "status": "active", "source_ids": ["source_7b278ba348f2a8bb94cce1fc"], "snippet": "…Reliable Value Estimation for Offline-to-[Online] Reinforcement Learning Wenke Xia 1,* , Pei Ren 2,* , Wenbo Yu 3…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_40700e61702f4b5a5765e11d"}
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

- Provider：`codex-gpt56-m91-vla-posttraining-weekly-20260720`
- Extraction：`extraction_4fd58691d04124ef005981f1`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_f9a9f1d1818632c0380b7942-vla-的强化学习读出接口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_f9a9f1d1818632c0380b7942"
+type: "concept"
+status: "proposal"
+title: "VLA 的强化学习读出接口"
+created_at: "2026-07-20T11:55:51+08:00"
+updated_at: "2026-07-20T11:55:51+08:00"
+aliases: ["RL Token", "RLT", "reinforcement-learning readout interface"]
+tags: []
+domains: ["embodied-ai", "robot-rl", "vla", "representation-learning"]
+confidence: "high"
+source_ids: ["source_40700e61702f4b5a5765e11d"]
+relations: [{"type": "derived_from", "target_id": "source_40700e61702f4b5a5765e11d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_40700e61702f4b5a5765e11d"
+reflection_context: {"reflection_ids": ["reflection_5b4f45d757e5b256cdddfcfa"], "importance": "weekly", "changed_belief": "VLA 的在线 RL 不必在全模型微调与从零训练小策略之间二选一；关键可以是训练一个足以支持价值判断和动作修正、但远小于主干的读出接口。", "surprising": "收益集中在任务最难的精密阶段：论文报告关键阶段最高约 3 倍提速，螺钉插入成功率由 20% 提升到 65%，训练量为数分钟到数小时的真机经验。", "connections": [{"shared_mechanism": "与 FlowDAgger 都冻结或保护生成式基础策略，并在低维中间空间训练轻量控制模块。", "boundary": "RL Token 需要奖励和自主在线交互，论文只覆盖四项精密真机任务，不能推出广泛长时程或跨任务持续学习能力。", "difference": "RL Token 学习面向 actor-critic 的内部特征读出并用 RL 优化；FlowDAgger 反演人类纠正动作对应的生成噪声并用监督学习优化。"}], "open_questions": ["RL token 的收益来自预训练语义、动作阶段信息还是任务进度表征，各自占比多少？"]}
+---
+
+# VLA 的强化学习读出接口
+
+VLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 actor-critic 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。
```
