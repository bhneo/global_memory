---
id: "proposal_bundle_f71684f9590125e4bea4"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-23T18:06:56+08:00"
updated_at: "2026-07-23T18:06:57+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_1f84f8abfca8810ebd19d85b"]
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
extraction_id: "extraction_142885df49e2cd036e79b9cf"
input_sha256: "44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_9d0aea7bfb560c703b51d683", "target_path": "vault/knowledge/concepts/concept_9d0aea7bfb560c703b51d683-从第一视角采集到跨本体训练的具身数据工具链.md", "base_sha256": null, "candidate_sha256": "1c5d9724cab903b3743bd113bf9799fb89ea6cefbe861b093b18374b8f9bbeb9", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_f71684f9590125e4bea4-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_9d0aea7bfb560c703b51d683.md", "working_at": "2026-07-23T18:06:57+08:00"}]
existing_context: [{"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "…Vision-Driven Embodied Agents for Open-World Mobile [Manipulation] · GitHub\n\nInput Episode for `source_a5f8ae205338d5f97eea87c7`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_16a7c84a59e39784c801e4ff", "type": "concept", "title": "非特权开放世界移动操作评测边界", "path": "vault/memory/concept/concept_16a7c84a59e39784c801e4ff.md", "status": "working", "source_ids": ["source_92fed4343c703da77f798f08"], "snippet": "# 非特权开放世界移动操作评测边界\n\n面向开放世界移动操作的评测应限制策略使用 RGB 等物理可获得输入，并把主动探索、视觉消歧和人机意图澄清纳入闭环任务；模拟与实机成绩必须连同具体工具、资产、episode 和本体条件解释。", "match_reason": "metadata:aliases"}, {"id": "concept_186fc27b4c190ed39889bb9e", "type": "concept", "title": "非特权开放世界移动操作的工具化评测契约", "path": "vault/memory/concept/concept_186fc27b4c190ed39889bb9e.md", "status": "working", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "# 非特权开放世界移动操作的工具化评测契约\n\n面向开放世界移动操作的评测框架：Agent从原始RGB进行探索，通过导航、感知和操作工具执行动作，并在指令含糊时与模拟用户澄清意图；可复现评测还需绑定任务配置、episode生命周期、兼容场景和物体资产，仓库声明的仿真或真机成功率不应脱离这些前提解释。", "match_reason": "metadata:aliases"}, {"id": "input_4bec3f6febe9fd2b5e3f75e5", "type": "input", "title": "[2607.15982] Data and Learning Where it Matters for Contact-Rich Manipulation", "path": "vault/inputs/input-input_4bec3f6febe9fd2b5e3f75e5.md", "status": "active", "source_ids": ["source_42e52a18cc082f3af087d574"], "snippet": "# [2607.15982] Data and Learning Where it Matters for Contact-Rich [Manipulation]\n\nInput Episode for `source_42e52a18cc082f3af087d574`. The…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-Robot separates navigation, [manipulation], and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation Model for Dexterous [Manipulation]\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_1f84f8abfca8810ebd19d85b"}
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
- Extraction：`extraction_142885df49e2cd036e79b9cf`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_9d0aea7bfb560c703b51d683-从第一视角采集到跨本体训练的具身数据工具链.md
@@ -0,0 +1,20 @@
+---
+id: "concept_9d0aea7bfb560c703b51d683"
+type: "concept"
+status: "proposal"
+title: "从第一视角采集到跨本体训练的具身数据工具链"
+created_at: "2026-07-23T18:06:56+08:00"
+updated_at: "2026-07-23T18:06:56+08:00"
+aliases: ["Egocentric Data-to-Embodiment Toolchain", "Open-AoE", "第一视角具身数据工具链"]
+tags: []
+domains: ["embodied-data", "egocentric-learning"]
+confidence: "medium"
+source_ids: ["source_1f84f8abfca8810ebd19d85b"]
+relations: [{"type": "derived_from", "target_id": "source_1f84f8abfca8810ebd19d85b", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_embodied_data_loop", "reason": "两者都将数据价值定义为采集、处理和下游复用的闭环；本概念具体限定第一视角和跨本体转换接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_1f84f8abfca8810ebd19d85b"
+reflection_context: {"reflection_ids": ["reflection_92e2e830397ee035b1ab0a8d"], "importance": "high", "changed_belief": "不能把开放视频库直接等同于机器人训练数据；可复用性需要明确的重建、标注、质量检查和跨本体转换接口。", "surprising": "", "connections": [], "open_questions": ["手机采集的手部、相机和动作标注在跨场景与跨本体重定向时，哪些误差会主导下游策略退化？"]}
+---
+
+# 从第一视角采集到跨本体训练的具身数据工具链
+
+具身数据基础设施将连续第一视角采集转为可训练样本：除视频外，还通过动作时间分段、语义标注、手部重建和相机轨迹重建产生结构化信号，并提供可视化、跨本体重定向、模型格式转换和训练配方。其下游价值依赖于采集质量、标注准确性和目标本体的适配方式。
```
