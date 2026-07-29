---
id: "proposal_bundle_644b8a6703a70f13ad7e"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T18:15:24+08:00"
updated_at: "2026-07-27T18:15:26+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_bee998153a82cd2a92db045b"]
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
extraction_id: "extraction_b87311a0e6c08cf8b5dd97cc"
input_sha256: "6d964feafefc4d95c69d8b834c53175821928c65beb28beb377dfe15a4035902"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_34269bf138ea36a302aaa11f", "target_path": "vault/knowledge/concepts/concept_34269bf138ea36a302aaa11f-接触分阶段的-flow-policy-候选选择-contact-phase-candidate-selection-for-fl.md", "base_sha256": null, "candidate_sha256": "ff76af3f8d7470df2a84b8703741abecab174f1c14f4fbd5b936b5629db30ef5", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_644b8a6703a70f13ad7e-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_34269bf138ea36a302aaa11f.md", "working_at": "2026-07-27T18:15:26+08:00"}]
existing_context: [{"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_hierarchical_mathematical_compression", "type": "concept", "title": "数学兴趣的层级压缩模型", "path": "vault/memory/concept/concept_hierarchical_mathematical_compression.md", "status": "working", "source_ids": ["source_e753604a46350e066a104918"], "snippet": "# 数学兴趣的层级压缩模型\n\n把形式数学对象表示为依赖图中的层级宏：wrapped length 记录使用已有定义后的局部表达长度，unwrapped length 记录递归展开到原语后的长度，depth 记录定义嵌套层数。Aksenov 等人在 arXiv:2603.20396 中以 Mathlib 为…", "match_reason": "metadata:aliases"}, {"id": "reflection_070e73598e48429fb5eafe01", "type": "reflection", "title": "PAKE：先学习运动学冗余分布，再让 RL 选择部分参考", "path": "vault/reflections/reflection-reflection_070e73598e48429fb5eafe01.md", "status": "active", "source_ids": ["source_951559714c0383331b1b30ac"], "snippet": "# PAKE：先学习运动学冗余分布，再让 RL 选择部分参考\n\n## Why important\n\nPAKE 把高维全身 loco-manipulation 拆成 Kinematic Normalizing Flow 生成多样可行的 partial reference…", "match_reason": "metadata:domains"}, {"id": "reflection_e8e62c04da8ad9f420c37be4", "type": "reflection", "title": "TactiDex：人形动作相似不等于接触层面的人类式操作", "path": "vault/reflections/reflection-reflection_e8e62c04da8ad9f420c37be4.md", "status": "active", "source_ids": ["source_37fe3c1f9d9fb7daa262fa91"], "snippet": "…Open questions\n\n- 哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？\n\n## Possible mechanisms\n\n- contact [guidance] 防止悬空模仿，alignment 对齐接触时空结构，force constraint 抑制通过过大压力投机完成任务。\n\n## Future directions\n\n- 引入真机触觉闭环与…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_bee998153a82cd2a92db045b"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "854c6e1ba595ee3115a57ecd4b72f9ebb5c24242e8ab24d406895e0c1d5883f4"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_b87311a0e6c08cf8b5dd97cc`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_34269bf138ea36a302aaa11f-接触分阶段的-flow-policy-候选选择-contact-phase-candidate-selection-for-fl.md
@@ -0,0 +1,20 @@
+---
+id: "concept_34269bf138ea36a302aaa11f"
+type: "concept"
+status: "proposal"
+title: "接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies"
+created_at: "2026-07-27T18:15:24+08:00"
+updated_at: "2026-07-27T18:15:24+08:00"
+aliases: ["HCPG-Flow", "hierarchical contact-progress guidance", "接触进度候选选择"]
+tags: []
+domains: ["robotics", "reinforcement-learning", "flow-policies"]
+confidence: "medium"
+source_ids: ["source_bee998153a82cd2a92db045b"]
+relations: [{"type": "derived_from", "target_id": "source_bee998153a82cd2a92db045b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_bee998153a82cd2a92db045b"
+reflection_context: {"reflection_ids": ["reflection_93c4dfb77bd88bfdd67b84c8"], "importance": "high", "changed_belief": "我会把其收益归于显式对象几何、可用接触信号和任务距离，而不把解析 selector 当成对未知任务或缺少接触感知的普适替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都在执行时利用非参数化的局部物理/几何结构改善生成式策略选择。", "boundary": "本文限于其 contact gate、对象中心距离、K=4 候选和 SAC-Flow 评测设置。", "difference": "critic ranking 依赖学习到的长程价值；HCPG 在接触前后使用分阶段的一阶局部进度。"}], "open_questions": ["接触判定噪声和任务进度不可由单一距离表示时，selector 如何退化或校准？"]}
+---
+
+# 接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies
+
+对生成多个动作候选的 flow policy，可用接触阶段门控在接触前按 TCP 接近物体、接触后按物体向任务目标的一阶距离下降评分，并在候选集合内标准化后形成软动作；这在论文中保持 actor/critic 训练目标不变。方法依赖可靠接触、对象和任务几何及所用候选数量，不能替代任意任务的长期价值估计。
```
