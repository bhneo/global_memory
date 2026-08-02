---
id: "proposal_bundle_b25307b92f3b4330d800"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T12:15:16+08:00"
updated_at: "2026-08-02T12:15:17+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_feaf5bf5a081e27b445c569c"]
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
extraction_id: "extraction_fd156a37b55e3809b3d15235"
input_sha256: "7221e0da1d8b4c120545f621b65ae2d97b3209f51ad3d3a53636d47e466f24df"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_913857cf6907564640fd669c", "target_path": "vault/knowledge/concepts/concept_913857cf6907564640fd669c-无-llm-中心的执行级-vla-直连通路-llm-free-execution-path-vla.md", "base_sha256": null, "candidate_sha256": "5389109e62a7d6087eb42ada60b11faea4e24faaefea435ab883bc9828a13063", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b25307b92f3b4330d800-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_913857cf6907564640fd669c.md", "working_at": "2026-08-02T12:15:17+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World Action [Model]\n\n默认由 World Action [Model] 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation [Model] for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "…NVIDIA Isaac GR00T N1.7 - A Foundation [Model] for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_feaf5bf5a081e27b445c569c"}
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
- Extraction：`extraction_fd156a37b55e3809b3d15235`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_913857cf6907564640fd669c-无-llm-中心的执行级-vla-直连通路-llm-free-execution-path-vla.md
@@ -0,0 +1,20 @@
+---
+id: "concept_913857cf6907564640fd669c"
+type: "concept"
+status: "proposal"
+title: "无 LLM 中心的执行级 VLA 直连通路 / LLM-free execution-path VLA"
+created_at: "2026-08-02T12:15:16+08:00"
+updated_at: "2026-08-02T12:15:16+08:00"
+aliases: ["TurboVLA", "direct vision-language-to-action pathway", "V+L to A execution model", "非 LLM 中心 VLA"]
+tags: []
+domains: ["robotics", "vision-language-action", "efficient-inference", "action-chunking"]
+confidence: "high"
+source_ids: ["source_feaf5bf5a081e27b445c569c"]
+relations: [{"type": "derived_from", "target_id": "source_feaf5bf5a081e27b445c569c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_portable_embodied_inference_runtime", "reason": "两者都降低闭环部署成本；运行时概念规定多速率调度与 I/O 契约，TurboVLA 改变模型内部从视觉语言到动作的表示路径。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "reason": "两者都使用 action chunks，但 TurboVLA 解决执行表示与并行解码，动作块级策略优化概念解决价值、优势、KL 和执行时域与块单位的对齐。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "直接 V+L→A 提供高效执行骨干，但论文的固定任务和本体设置不能替代跨本体动作语义、数据覆盖和部署边界。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_feaf5bf5a081e27b445c569c"
+reflection_context: {"reflection_ids": ["reflection_618d75724d0c590adfaab1e6"], "importance": "high", "changed_belief": "此前常把 VLA 的语言能力与 LLM 位于视觉到动作主路径视为同一件事；该论文显示，在具体执行指令下，语言条件可由轻量文本编码与直接视觉交互保留，而开放式规划仍可作为上层可选模块。", "surprising": "去掉语言使 LIBERO-Goal 大幅下降，但把完整 LLM 替换为 BERT/T5-small 配合双向交互仍保持高成功率，说明语义条件化必要，不等于生成式 LLM 必须位于执行内环。", "connections": [{"shared_mechanism": "都把高层语义与低层执行分成不同计算或调度接口，以降低闭环延迟。", "boundary": "可移植推理运行时解决模型与 I/O 的部署调度，TurboVLA 改变模型内部 V→L→A 的表示依赖；动作块时域概念处理执行长度而非移除 LLM。", "difference": "TurboVLA 是训练架构的 V+L→A 重构，不是缓存、量化、运行时封装或高层规划的替代品。"}], "open_questions": ["直接 V+L→A 在未见组合指令、长程任务分解和跨本体动作空间下何时需要重新引入大模型规划，而不会把其延迟带回控制内环？"]}
+---
+
+# 无 LLM 中心的执行级 VLA 直连通路 / LLM-free execution-path VLA
+
+针对已给定具体操作指令的执行级控制，分别用轻量文本编码器和视觉编码器保留完整 token 与空间特征，通过多层双向 cross-attention 同时构造 scene-aware instruction features 和 instruction-conditioned visual features，再把 robot state 直接送入 ACT-style decoder，并行预测连续动作块；视觉和语言不再先通过大型生成式语言模型形成动作表示。该 V+L→A 重构不同于剪枝、缓存、量化或只优化 action head，也不否认语言语义本身的必要性。论文的消融显示去语言会显著损害目标条件任务，而轻量语义编码和双向交互足以支撑其所测执行任务。适用边界是具体执行指令、现有视觉语义与动作监督；开放式任务分解、复杂推理和未见组合语言仍可能需要上层 LLM planner，但不必让其驻留在每个控制步的执行内环。
```
