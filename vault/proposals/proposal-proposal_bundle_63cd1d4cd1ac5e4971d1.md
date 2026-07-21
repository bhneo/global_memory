---
id: "proposal_bundle_63cd1d4cd1ac5e4971d1"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T11:56:00+08:00"
updated_at: "2026-07-20T11:56:01+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_c79f943c818d06054ca5cf92"]
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
extraction_id: "extraction_e62bd6b73d0d7d66a185bfc3"
input_sha256: "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "target_path": "vault/knowledge/concepts/concept_d01c4f0b61292d29f0a7ffe2-动作块级策略优化与动态执行时域.md", "base_sha256": null, "candidate_sha256": "0abbeece325a6ec42b27fbeac3a8881574c4e7069a16d72fd7dbb027a8eae290", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_63cd1d4cd1ac5e4971d1-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_d01c4f0b61292d29f0a7ffe2.md", "working_at": "2026-07-20T11:56:01+08:00"}]
existing_context: [{"id": "reflection_c0693ad0e6abf8397dbdfd87", "type": "reflection", "title": "PAC-ACT：动作块既是生成单位，也应成为信用分配与约束单位", "path": "vault/reflections/reflection-reflection_c0693ad0e6abf8397dbdfd87.md", "status": "active", "source_ids": ["source_c79f943c818d06054ca5cf92"], "snippet": "…与 RL Token 都在保留预训练行为先验的前提下用 [actor-critic] 做后训练。\n  Boundary: PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。\n  Difference: PAC-ACT 改造的是优化和信用分配的时间单位…", "match_reason": "full-text:body"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…并训练低维中间控制接口。\",\n    \"boundary\": \"只有基础策略已覆盖目标行为附近时，低维接口才可能兼顾样本效率和先验保持。\",\n    \"difference\": \"RL Token 使用奖励和 [actor-critic]；FlowDAgger 使用人类纠正、动作反演和监督学习。\"\n  },\n  {\n    \"shared_mechanism\": \"PAC-ACT 与…", "match_reason": "full-text:body"}, {"id": "reflection_5b4f45d757e5b256cdddfcfa", "type": "reflection", "title": "RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口", "path": "vault/reflections/reflection-reflection_5b4f45d757e5b256cdddfcfa.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# RL Token：把 VLA 内部知识暴露成可在线优化的紧凑接口\n\n## Why important\n\n它给出一种清晰的分工：冻结或稳定保留大型 VLA 的感知与动作先验，只让小型 [actor-critic] 通过紧凑 RL token 在少量真机交互中适应精密阶段…", "match_reason": "full-text:body"}, {"id": "concept_f9a9f1d1818632c0380b7942", "type": "concept", "title": "VLA 的强化学习读出接口", "path": "vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md", "status": "working", "source_ids": ["source_40700e61702f4b5a5765e11d"], "snippet": "# VLA 的强化学习读出接口\n\nVLA 的强化学习读出接口，是从预训练模型内部特征中学习紧凑、任务相关的 RL token，供小型 [actor-critic] 在动作锚定约束下在线优化，使基础 VLA 保留通用先验而把适应集中到精密阶段。", "match_reason": "full-text:body"}, {"id": "reflection_cd269bee56819aafec2fd5a3", "type": "reflection", "title": "FlowDAgger：适配接口的位置决定能否保留生成策略先验", "path": "vault/reflections/reflection-reflection_cd269bee56819aafec2fd5a3.md", "status": "active", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "…FlowDAgger 通过监督的人类干预学习潜变量；RL Token 通过环境奖励学习 [actor-critic]；两者的信息来源和安全成本不同。\n\n## Conflicts\n\n- 限制在基础策略的生成支持集有助于保留技能，但若目标行为不在该支持集中，潜空间转向本身可能不足。\n\n## Open questions\n\n- 动作反演误差能否作为是否接受干预、请求更多示范或切换到权重微调的判据？\n\n## Possible mechanisms…", "match_reason": "full-text:body"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_c79f943c818d06054ca5cf92"}
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
- Extraction：`extraction_e62bd6b73d0d7d66a185bfc3`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_d01c4f0b61292d29f0a7ffe2-动作块级策略优化与动态执行时域.md
@@ -0,0 +1,20 @@
+---
+id: "concept_d01c4f0b61292d29f0a7ffe2"
+type: "concept"
+status: "proposal"
+title: "动作块级策略优化与动态执行时域"
+created_at: "2026-07-20T11:56:00+08:00"
+updated_at: "2026-07-20T11:56:00+08:00"
+aliases: ["PAC-ACT", "chunk-level PPO", "action-chunk policy optimization"]
+tags: []
+domains: ["embodied-ai", "robot-rl", "action-chunking", "contact-manipulation"]
+confidence: "high"
+source_ids: ["source_c79f943c818d06054ca5cf92"]
+relations: [{"type": "derived_from", "target_id": "source_c79f943c818d06054ca5cf92", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_c79f943c818d06054ca5cf92"
+reflection_context: {"reflection_ids": ["reflection_c0693ad0e6abf8397dbdfd87"], "importance": "weekly", "changed_belief": "动作块不只是推理加速技巧；若策略一次生成一段动作，价值估计、优势计算、执行时域和 KL 约束也需要与该时间粒度对齐。", "surprising": "在精密接触任务中，目标不仅是成功率，还包括接触稳定和力安全；Contour 任务中超过 60N 的力读数比例据报降低 46 倍。", "connections": [{"shared_mechanism": "与 RL Token 都在保留预训练行为先验的前提下用 actor-critic 做后训练。", "boundary": "PAC-ACT 面向轻量视觉动作块策略和工业精密接触基准，不等同于大型 VLA 的通用在线后训练。", "difference": "PAC-ACT 改造的是优化和信用分配的时间单位；RL Token 改造的是大模型向轻量 RL 暴露的表示接口。"}], "open_questions": ["块长度能否依据接触风险、价值不确定性或阶段边界动态变化，而非全程固定？"]}
+---
+
+# 动作块级策略优化与动态执行时域
+
+动作块级策略优化要求强化学习的决策、价值、优势和行为先验约束与动作块生成单位对齐；块长同时决定吞吐、时间连续性、信用分配跨度和异常后的纠正延迟，因此应被视为可按风险与阶段调整的控制时域。
```
