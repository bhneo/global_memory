---
id: "proposal_bundle_b6df8ef41f739a435b18"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-22T18:12:38+08:00"
updated_at: "2026-07-22T18:12:39+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d33321374508784864c44d65"]
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
extraction_id: "extraction_9e63ab50b34ee793a68c2cb3"
input_sha256: "a872430d3ff153516d3e9e31ff5a301d0e9f97701e097ec1d5dafb71cc65394b"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_769f84122571858ee48f9c48", "target_path": "vault/knowledge/concepts/concept_769f84122571858ee48f9c48-共享持久对象状态的可验证人形-vla-闭环.md", "base_sha256": null, "candidate_sha256": "6dc0395fc48a10d5068efb490605bfc3529348f6b412afb48d01f4149514fda5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b6df8ef41f739a435b18-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_769f84122571858ee48f9c48.md", "working_at": "2026-07-22T18:12:39+08:00"}]
existing_context: [{"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "input_ab5a33edd49eec243cb3862f", "type": "input", "title": "DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting", "path": "vault/inputs/input-input_ab5a33edd49eec243cb3862f.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…A Simulation-in-the-[Loop] Toolkit for Single-View Human Demonstration Retargeting\n\nInput Episode for `source_513a527cb4d410e4f94a9bb5`. The…", "match_reason": "metadata:title"}, {"id": "reflection_65fb6fe12e2291077f28900c", "type": "reflection", "title": "DemoBridge: single-view demonstration transfer needs simulator-in-the-loop feasibility", "path": "vault/reflections/reflection-reflection_65fb6fe12e2291077f28900c.md", "status": "active", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "…single-view demonstration transfer needs simulator-in-the-[loop] feasibility\n\n## Why important\n\nDemoBridge couples RGB observation, stereo reconstruction…", "match_reason": "metadata:title"}, {"id": "concept_b1b62d103e0a768399664d9d", "type": "concept", "title": "Simulator-validated single-view demonstration transfer", "path": "vault/memory/concept/concept_b1b62d103e0a768399664d9d.md", "status": "working", "source_ids": ["source_513a527cb4d410e4f94a9bb5"], "snippet": "# Simulator-validated single-view demonstration transfer\n\nConvert a single-view human demonstration into a robot plan through stereo…", "match_reason": "metadata:aliases"}, {"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "canonical", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "# VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人\n\n## 论文主张\n\nVIA 把机器人控制转换为视觉 Agent 的工具使用任务：未经机器人专项微调的前沿通用 Agent 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划…", "match_reason": "metadata:tags"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:domains"}, {"id": "reflection_6628e0dee92b8a90b106317d", "type": "reflection", "title": "Zero2Skill：语言纠错记忆把自主采集失败转为下一轮约束", "path": "vault/reflections/reflection-reflection_6628e0dee92b8a90b106317d.md", "status": "active", "source_ids": ["source_5e14510061220db7f2344913"], "snippet": "# Zero2Skill：语言纠错记忆把自主采集失败转为下一轮约束\n\n## Why important\n\n它将自主采集、少量人类语言干预、持久纠错记忆、轨迹认证与下游策略训练闭合为数据飞轮，明确区分采集成功率和最终策略质量。\n\n## What changed\n\n人类在环的主要价值不一定是持续遥操作，而可以是把重复失败压缩为可复用语言约束；但验证器误判会直接污染数据集。\n\n## Surprising\n\n作者在所测桌面任务中报告无需遥操作即可达到 100% episode…", "match_reason": "metadata:domains"}, {"id": "concept_8f8ae7b5cac6690d2e341d40", "type": "concept", "title": "人形行为基础模型的数量—多样性协同扩展", "path": "vault/memory/concept/concept_8f8ae7b5cac6690d2e341d40.md", "status": "working", "source_ids": ["source_46f82af34b1ace2c5c0483af"], "snippet": "# 人形行为基础模型的数量—多样性协同扩展\n\n在人形运动跟踪的强化学习预训练中，在线并行环境与rollout时域主要决定有效交互数据数量，经过筛选的参考动作库主要决定行为分布多样性；两者需与全局全身轨迹接口和可扩展模型架构协同评估，而不能以参考动作数量单独替代训练规模。", "match_reason": "metadata:aliases"}, {"id": "concept_staged_cross_embodiment_alignment", "type": "concept", "title": "异构具身数据的分阶段对齐", "path": "vault/memory/concept/concept_staged_cross_embodiment_alignment.md", "status": "working", "source_ids": ["source_691f3acc1fe3382639690f59"], "snippet": "# 异构具身数据的分阶段对齐\n\n把人类视频中的通用视觉—动作表征学习，与机器人本体专属的连续控制学习拆成不同阶段，以减少人类运动学和机器人运动学差异造成的负迁移。", "match_reason": "metadata:domains"}, {"id": "architecture_simple_simulation_policy_loop", "type": "architecture", "title": "SIMPLE 仿真策略学习与评测环境", "path": "vault/memory/architecture/architecture_simple_simulation_policy_loop.md", "status": "working", "source_ids": ["source_d75524a9040845cdc76db35c"], "snippet": "# SIMPLE 仿真策略学习与评测环境\n\nSIMPLE 是面向具身策略的数据生成、微调和仿真评测环境，覆盖多种机器人、场景资产和人形全身移动操作任务，并集成多类 VLA 与 World Action Model。", "match_reason": "metadata:domains"}, {"id": "concept_generalist_cross_embodiment_vla", "type": "concept", "title": "跨本体通用 VLA 策略", "path": "vault/memory/concept/concept_generalist_cross_embodiment_vla.md", "status": "working", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "match_reason": "metadata:domains"}, {"id": "concept_705dff5d5d3ebdcb87f1564f", "type": "concept", "title": "形态可重构机器人的跨本体控制边界", "path": "vault/memory/concept/concept_705dff5d5d3ebdcb87f1564f.md", "status": "working", "source_ids": ["source_adcddc61e96d32f765d29c90"], "snippet": "# 形态可重构机器人的跨本体控制边界\n\n将同一组可重用机电关节模块配置为灵巧手或人形身体，并在各形态下采用相应遥操作、抓取、在手操作、步态或全身控制接口的实验平台；共享硬件不消除由接触几何、任务角色和稳定性约束导致的控制差异。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_d33321374508784864c44d65"}
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
- Extraction：`extraction_9e63ab50b34ee793a68c2cb3`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_769f84122571858ee48f9c48-共享持久对象状态的可验证人形-vla-闭环.md
@@ -0,0 +1,20 @@
+---
+id: "concept_769f84122571858ee48f9c48"
+type: "concept"
+status: "proposal"
+title: "共享持久对象状态的可验证人形 VLA 闭环"
+created_at: "2026-07-22T18:12:38+08:00"
+updated_at: "2026-07-22T18:12:38+08:00"
+aliases: ["Persistent Object Tokenization", "POT-VLA", "Persistent 3D Object Tokens", "持久三维对象 token"]
+tags: []
+domains: ["humanoid-robotics", "vla", "execution-verification"]
+confidence: "medium"
+source_ids: ["source_d33321374508784864c44d65"]
+relations: [{"type": "derived_from", "target_id": "source_d33321374508784864c44d65", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_relation_triggered_process_safety", "reason": "两者都通过明确条件阻止流程在未验证状态下推进；POT-VLA 将条件绑定到共享对象记忆。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_d33321374508784864c44d65"
+reflection_context: {"reflection_ids": ["reflection_5dc40c1f6baef6a5579f8b47"], "importance": "high", "changed_belief": "闭环验证的关键不只是额外加一个监视器，而是让动作与验证共享并在每个动作块后刷新同一可定位对象状态。", "surprising": "", "connections": [{"shared_mechanism": "两者都依赖动作后观测、条件检查和失败恢复来约束流程推进。", "boundary": "对象 token 的共享状态不等于已验证的接触力、动力学可行性或跨环境鲁棒性。", "difference": "POT-VLA 使用角色索引三维对象记录；现有过程安全概念定义更一般的关系触发检查。"}], "open_questions": ["遮挡或低置信度对象在何时应触发重观测而非继续执行恢复动作？"]}
+---
+
+# 共享持久对象状态的可验证人形 VLA 闭环
+
+对每个活跃子任务维护角色索引的 RGB-D 三维对象记录，将其序列化为动作专家的对象 token，并在执行动作块后刷新同一记录以检查几何成功谓词和触发恢复。该方法依赖对象角色绑定、深度观测与谓词定义，不能把报告的特定 Unitree G1 结果当作一般保证。
```
