---
id: "proposal_bundle_21a3d976042f2d38be49"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-26T12:18:41+08:00"
updated_at: "2026-07-26T12:18:42+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_d4762e0cf2330ab6ea00a521"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-m91-weekly-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_0489c6674420e5533e1c12d6"
input_sha256: "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_a858f8d191d3afdd69418471", "target_path": "vault/knowledge/concepts/concept_a858f8d191d3afdd69418471-陈旧性对齐的异步慢上下文-快控制接口.md", "base_sha256": null, "candidate_sha256": "0cddb098247b5d0be61626e25961b5a980817764ff04dee957399b7b9eee4c34", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_21a3d976042f2d38be49-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "working_at": "2026-07-26T12:18:42+08:00"}]
existing_context: [{"id": "work_arxiv_2601_03220", "type": "work", "title": "From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence", "path": "vault/memory/work/work_arxiv_2601_03220.md", "status": "working", "source_ids": ["source_deb313c98b03fc4d0b33794a", "source_1c0f944bf6b14cf9d1fff939"], "snippet": "# From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence\n\n## Logical work identity\n\n- arXiv：`2601.03220`\n- Version：`unknown`\n- Captures：`source_deb313c98b03fc4d0b33794a`, `source_1c0f944bf6b14cf9d1fff939", "match_reason": "metadata:title"}, {"id": "concept_3b83de1641240159d66c23d4", "type": "concept", "title": "显式时钟的异步机器人闭环程序", "path": "vault/memory/concept/concept_3b83de1641240159d66c23d4.md", "status": "working", "source_ids": ["source_5260f9244a5030c2143c36e4"], "snippet": "# 显式时钟的异步机器人闭环程序\n\n将感知、状态更新、规划和控制表示为有状态因果流图；每个节点声明运行时钟，每条边声明同步或缓冲策略，使多速率闭环在固定时钟、同步策略和输入轨迹下可重放与调试。该抽象不能替代对单个模块感知精度、控制稳定性或实机安全的验证。", "match_reason": "metadata:aliases"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…foregrounds engineering details such as reset burden and [asynchronous] data collection, suggesting that throughput and recovery can dominate…", "match_reason": "full-text:body"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language-Action] Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for [Vision-Language-Action] Models with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_d4762e0cf2330ab6ea00a521"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "7496b4e69979dfc80abc6121b1c8f5e68cd245d00d654caada8eb5124e6839a5"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-m91-weekly-daily-v1`
- Extraction：`extraction_0489c6674420e5533e1c12d6`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_a858f8d191d3afdd69418471-陈旧性对齐的异步慢上下文-快控制接口.md
@@ -0,0 +1,20 @@
+---
+id: "concept_a858f8d191d3afdd69418471"
+type: "concept"
+status: "proposal"
+title: "陈旧性对齐的异步慢上下文—快控制接口"
+created_at: "2026-07-26T12:18:41+08:00"
+updated_at: "2026-07-26T12:18:41+08:00"
+aliases: ["Staleness-Aligned Asynchronous Slow-Context Fast-Control Interface", "FastSlow-LMDrive", "异步快慢 VLA 接口"]
+tags: []
+domains: ["vla", "real-time-control", "autonomous-driving"]
+confidence: "medium"
+source_ids: ["source_d4762e0cf2330ab6ea00a521"]
+relations: [{"type": "derived_from", "target_id": "source_d4762e0cf2330ab6ea00a521", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2ce226e08d585158c1dfbb18", "reason": "两者都在保留慢速预训练表示的同时增加读取新鲜局部传感的快分支；前者面向视觉驾驶缓存，后者面向动作块内力反馈。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "两者都依赖非对称接口使冻结主干可被复用；FastSlow 在单策略内部复用缓存，既有概念在多原语编排中复用冻结局部专家。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-m91-weekly-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_d4762e0cf2330ab6ea00a521"
+reflection_context: {"reflection_ids": ["reflection_743b2d2d30d2f822bf2bfb9f"], "importance": "high", "changed_belief": "此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支 token、缓存可增量等价更新且快分支在训练中见过滞后上下文时，异步复用才是可验证的系统契约。", "surprising": "同一 action expert 从 10 Hz 提升到 20 Hz 主要提高路线完成率与减少偏航/超时，而综合 driving score 未同步提高并伴随更多车辆碰撞暴露；控制新鲜度和安全驾驶质量不是同一指标。", "connections": [{"shared_mechanism": "FastSlow-LMDrive 与块内反应式力注入都保留慢速预训练先验，同时用更快、更新鲜的局部观测驱动轻量动作分支。", "boundary": "连接适用于慢上下文在多个控制 tick 内仍有用、快路径可独立读取当前传感且延迟分布可在训练中覆盖的任务。", "difference": "FastSlow-LMDrive 通过逐层视觉语言 KV cache 服务驾驶 waypoint expert；力注入概念通过近期六维力记忆修正接触动作块，安全变量与传感动力学不同。"}], "open_questions": ["能否用快慢分支分歧和缓存年龄共同触发安全降级，并在长路线密集交通中减少完成率上升带来的碰撞暴露？"]}
+---
+
+# 陈旧性对齐的异步慢上下文—快控制接口
+
+在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。
```
