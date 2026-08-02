---
id: "concept_913857cf6907564640fd669c"
type: "concept"
status: "proposal"
title: "无 LLM 中心的执行级 VLA 直连通路 / LLM-free execution-path VLA"
created_at: "2026-08-02T12:15:16+08:00"
updated_at: "2026-08-02T12:15:16+08:00"
aliases: ["TurboVLA", "direct vision-language-to-action pathway", "V+L to A execution model", "非 LLM 中心 VLA"]
tags: []
domains: ["robotics", "vision-language-action", "efficient-inference", "action-chunking"]
confidence: "high"
source_ids: ["source_feaf5bf5a081e27b445c569c"]
relations: [{"type": "derived_from", "target_id": "source_feaf5bf5a081e27b445c569c", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_portable_embodied_inference_runtime", "reason": "两者都降低闭环部署成本；运行时概念规定多速率调度与 I/O 契约，TurboVLA 改变模型内部从视觉语言到动作的表示路径。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_d01c4f0b61292d29f0a7ffe2", "reason": "两者都使用 action chunks，但 TurboVLA 解决执行表示与并行解码，动作块级策略优化概念解决价值、优势、KL 和执行时域与块单位的对齐。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "直接 V+L→A 提供高效执行骨干，但论文的固定任务和本体设置不能替代跨本体动作语义、数据覆盖和部署边界。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
change_reason: "compile bundle from source_feaf5bf5a081e27b445c569c"
reflection_context: {"reflection_ids": ["reflection_618d75724d0c590adfaab1e6"], "importance": "high", "changed_belief": "此前常把 VLA 的语言能力与 LLM 位于视觉到动作主路径视为同一件事；该论文显示，在具体执行指令下，语言条件可由轻量文本编码与直接视觉交互保留，而开放式规划仍可作为上层可选模块。", "surprising": "去掉语言使 LIBERO-Goal 大幅下降，但把完整 LLM 替换为 BERT/T5-small 配合双向交互仍保持高成功率，说明语义条件化必要，不等于生成式 LLM 必须位于执行内环。", "connections": [{"shared_mechanism": "都把高层语义与低层执行分成不同计算或调度接口，以降低闭环延迟。", "boundary": "可移植推理运行时解决模型与 I/O 的部署调度，TurboVLA 改变模型内部 V→L→A 的表示依赖；动作块时域概念处理执行长度而非移除 LLM。", "difference": "TurboVLA 是训练架构的 V+L→A 重构，不是缓存、量化、运行时封装或高层规划的替代品。"}], "open_questions": ["直接 V+L→A 在未见组合指令、长程任务分解和跨本体动作空间下何时需要重新引入大模型规划，而不会把其延迟带回控制内环？"]}
---

# 无 LLM 中心的执行级 VLA 直连通路 / LLM-free execution-path VLA

针对已给定具体操作指令的执行级控制，分别用轻量文本编码器和视觉编码器保留完整 token 与空间特征，通过多层双向 cross-attention 同时构造 scene-aware instruction features 和 instruction-conditioned visual features，再把 robot state 直接送入 ACT-style decoder，并行预测连续动作块；视觉和语言不再先通过大型生成式语言模型形成动作表示。该 V+L→A 重构不同于剪枝、缓存、量化或只优化 action head，也不否认语言语义本身的必要性。论文的消融显示去语言会显著损害目标条件任务，而轻量语义编码和双向交互足以支撑其所测执行任务。适用边界是具体执行指令、现有视觉语义与动作监督；开放式任务分解、复杂推理和未见组合语言仍可能需要上层 LLM planner，但不必让其驻留在每个控制步的执行内环。
