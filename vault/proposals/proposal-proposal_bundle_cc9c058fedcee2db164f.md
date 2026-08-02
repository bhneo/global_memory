---
id: "proposal_bundle_cc9c058fedcee2db164f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T12:14:58+08:00"
updated_at: "2026-08-02T12:14:59+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d0908c8e9c58809dd2665c1e"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_dcf3d40d403c32ab30ddb29d"
input_sha256: "d912a103f952878d6f6fe1f05e38c766d9f56353a499c71eb501119e7fdad4fc"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_5495a66616b2989c1ce38a5f", "target_path": "vault/knowledge/concepts/concept_5495a66616b2989c1ce38a5f-经验成熟度驱动的机器人能力编译与回退-experience-maturity-driven-robotic-capability.md", "base_sha256": null, "candidate_sha256": "9d9fafe2732437db67403e914c6312c01b8d50f0ecb293e1edd4359476f6da22", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_cc9c058fedcee2db164f-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_5495a66616b2989c1ce38a5f.md", "working_at": "2026-08-02T12:14:59+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_34269bf138ea36a302aaa11f", "type": "concept", "title": "接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies", "path": "vault/memory/concept/concept_34269bf138ea36a302aaa11f.md", "status": "working", "source_ids": ["source_bee998153a82cd2a92db045b"], "snippet": "# 接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow [policies]\n\n对生成多个动作候选的 flow policy，可用接触阶段门控在接触前按 TCP 接近物体、接触后按物体向任务目标的一阶距离下降评分…", "match_reason": "metadata:title"}, {"id": "concept_d5965e0770273320ea6b28f2", "type": "concept", "title": "主动真机因子评测", "path": "vault/memory/concept/concept_d5965e0770273320ea6b28f2.md", "status": "working", "source_ids": ["source_61152ca8210ad3913764a291"], "snippet": "# 主动真机因子评测\n\n把机器人策略在对象位姿、相机视角和初始状态等结构化任务因子组合上的性能视为未知函数，用带不确定性估计的概率代理模型和信息增益准则依次选择真机试验，以在有限预算下估计性能分布并定位易失败区域。", "match_reason": "metadata:aliases"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_d0908c8e9c58809dd2665c1e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "07cd53fc7af1bf3f109a79f88f031e0076fefcf0f787b35d3378ba788670e82f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_dcf3d40d403c32ab30ddb29d`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_5495a66616b2989c1ce38a5f-经验成熟度驱动的机器人能力编译与回退-experience-maturity-driven-robotic-capability.md
@@ -0,0 +1,20 @@
+---
+id: "concept_5495a66616b2989c1ce38a5f"
+type: "concept"
+status: "proposal"
+title: "经验成熟度驱动的机器人能力编译与回退 / Experience-maturity-driven robotic capability compilation"
+created_at: "2026-08-02T12:14:58+08:00"
+updated_at: "2026-08-02T12:14:58+08:00"
+aliases: ["HERO capability evolution", "heuristic-exemplar-reflexive hierarchy", "H2E2R capability compilation", "机器人经验到肌肉记忆编译"]
+tags: []
+domains: ["robotics", "embodied-agents", "capability-learning", "policy-orchestration"]
+confidence: "high"
+source_ids: ["source_d0908c8e9c58809dd2665c1e"]
+relations: [{"type": "derived_from", "target_id": "source_d0908c8e9c58809dd2665c1e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_f35cd7f55e4108ce45ec35d7", "reason": "两者都由 orchestrator 路由异构能力并处理失败；RoboHarness 关注静态策略的能力边界与状态分布交接，HERO 关注经验成熟度驱动的能力创建、编译和反向回退。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "能力编译需要把真实执行、成功判定、经验筛选和重新训练闭合为可回放迭代；部署迭代闭环提供数据入口，但不自动保证验证或能力演化正确。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_d0908c8e9c58809dd2665c1e"
+reflection_context: {"reflection_ids": ["reflection_0927933ce742db3006087d15"], "importance": "high", "changed_belief": "此前能力编排容易被看作对一组静态策略做任务路由；该论文进一步表明，编排器可以把成功经验从昂贵推理逐步转化为可复用轨迹，再编译为低延迟闭环策略，并在部署时反向按成熟度回退。", "surprising": "HERO 的数据演化采用 H→E→R，而部署采用 R→E→H；训练与执行沿同一能力谱反向流动，使快速已学能力优先，同时保留经验迁移和从头推理作为恢复路径。", "connections": [{"shared_mechanism": "都通过高层 orchestrator 在异构机器人能力之间路由，并显式处理失败与交接。", "boundary": "RoboHarness 主要估计静态策略的能力边界与状态分布交接；HERO 还让成功经验随重复使用从启发式执行演化为 exemplar，再训练为 reflexive policy。", "difference": "前者强调未经联合训练策略之间的输入状态可达性，后者强调经验成熟度驱动的能力创建、编译和反向回退。"}], "open_questions": ["如何在不依赖人工定义 primitive skill space 的前提下发现新能力层，并防止错误的成功判定被编译进 reflexive policy？"]}
+---
+
+# 经验成熟度驱动的机器人能力编译与回退 / Experience-maturity-driven robotic capability compilation
+
+把机器人能力按经验成熟度组织为三个可演化执行层：启发式 bootstrapper 用 VLM 和几何原语处理无经验任务，exemplar accelerator 对成功轨迹做对象点云配准与几何迁移，reflexive policy 则把重复且通过筛选的经验训练为闭环 visuomotor 控制。数据演化沿 H→E→R 把昂贵推理逐步编译为快速策略，部署沿 R→E→H 优先使用已内化能力，并在 policy 不可用或失败时退回轨迹复用和从头推理。该机制不同于只路由静态策略的能力编排：orchestrator 同时改变能力库存的生命周期。它仍依赖成功验证器、深度/点云质量、人工定义 primitive skill space、每任务训练和可恢复场景；错误成功判定可能污染 exemplar 与下游 policy，不能把少量真实任务结果外推为开放世界自主学习保证。
```
