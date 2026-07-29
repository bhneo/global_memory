---
id: "proposal_bundle_6069de7ae897e0394597"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T01:47:28+08:00"
updated_at: "2026-07-28T01:47:29+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_86550a0f567215a8394cf9e5"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_fc0cd9718c4bc1611a484994"
input_sha256: "932f850ee892b2d3a11dbcf4030402be6b95fbfc93927e066a3b21207967fc60"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_3c58f95c4a4b1d14f5e755dc", "target_path": "vault/knowledge/concepts/concept_3c58f95c4a4b1d14f5e755dc-boltzmann-方程到不可压-navier--stokes-的受限水动力极限-bounded-hydrodynamic-li.md", "base_sha256": null, "candidate_sha256": "4250231220ea8b2d3125489eac622fece84c4ea6ab56fffbbc1744a03dff164e", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_6069de7ae897e0394597-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_3c58f95c4a4b1d14f5e755dc.md", "working_at": "2026-07-28T01:47:29+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_3919401ac5ba9591d0682172", "type": "reflection", "title": "Boltzmann 到不可压 NS：Leray 极限受缩放与核条件限定 / incompressible NS limit is bounded by scaling and hard-cutoff assumptions", "path": "vault/reflections/reflection-reflection_3919401ac5ba9591d0682172.md", "status": "active", "source_ids": ["source_86550a0f567215a8394cf9e5"], "snippet": "# Boltzmann 到不可压 NS：Leray 极限受缩放与核条件限定 / [incompressible] NS limit is bounded by scaling and hard-cutoff assumptions\n\n## Why important…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_86550a0f567215a8394cf9e5"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_fc0cd9718c4bc1611a484994`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_3c58f95c4a4b1d14f5e755dc-boltzmann-方程到不可压-navier--stokes-的受限水动力极限-bounded-hydrodynamic-li.md
@@ -0,0 +1,20 @@
+---
+id: "concept_3c58f95c4a4b1d14f5e755dc"
+type: "concept"
+status: "proposal"
+title: "Boltzmann 方程到不可压 Navier--Stokes 的受限水动力极限 / bounded hydrodynamic limit from Boltzmann to incompressible Navier--Stokes"
+created_at: "2026-07-28T01:47:28+08:00"
+updated_at: "2026-07-28T01:47:28+08:00"
+aliases: ["Boltzmann to incompressible Navier--Stokes limit", "incompressible hydrodynamic limit", "Boltzmann 不可压水动力极限", "Leray 极限"]
+tags: []
+domains: ["kinetic-theory", "fluid-dynamics", "boltzmann-equation"]
+confidence: "high"
+source_ids: ["source_86550a0f567215a8394cf9e5"]
+relations: [{"type": "derived_from", "target_id": "source_86550a0f567215a8394cf9e5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}, {"type": "related_to", "target_id": "concept_972e54ed590f8b093808209f", "reason": "两者都研究动理学极限，但既有节点从稀薄硬球粒子得到 Boltzmann 层级，本项从 Boltzmann 方程经水动力标度得到不可压流体弱解。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "proposal"}]
+change_reason: "compile bundle from source_86550a0f567215a8394cf9e5"
+reflection_context: {"reflection_ids": ["reflection_3919401ac5ba9591d0682172"], "importance": "high", "changed_belief": "我会区分 Boltzmann--Grad 粒子极限与此处 Boltzmann 方程到流体方程的水动力缩放，且不把弱收敛外推为唯一性或强收敛。", "surprising": "", "connections": [{"shared_mechanism": "两者都以明确标度和弱解紧性把微观描述连接到有效动力学。", "boundary": "本文限于硬截断势、小 Mach/Knudsen 同阶极限与重整化 Boltzmann 解。", "difference": "Boltzmann--Grad 处理粒子到动理学；本文从既有 Boltzmann 方程导出不可压 Leray 流体解。"}], "open_questions": ["何种额外正则性或稳定性条件能提高收敛方式或处理更广碰撞核？"]}
+---
+
+# Boltzmann 方程到不可压 Navier--Stokes 的受限水动力极限 / bounded hydrodynamic limit from Boltzmann to incompressible Navier--Stokes
+
+对围绕 Maxwellian 的小涨落，在 Mach 数与 Knudsen 数渐近同阶、碰撞核满足论文的硬截断条件且采用全局重整化 Boltzmann 解时，任意极限点具有无穷小 Maxwellian 形式，其宏观场满足不可压 Navier--Stokes--Fourier 弱方程；在更强的初始相对熵条件下，速度场是 Leray 解并满足能量不等式。该结论是弱的子序列极限，不提供 Leray 解唯一性、全序列强收敛，也不是从硬球粒子系统直接到流体方程的 Boltzmann--Grad 极限。
```
