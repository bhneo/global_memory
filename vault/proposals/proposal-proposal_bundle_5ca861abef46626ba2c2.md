---
id: "proposal_bundle_5ca861abef46626ba2c2"
type: "proposal"
status: "migrated"
title: "Compile bundle：2607.22535v1.pdf"
created_at: "2026-07-28T18:36:05+08:00"
updated_at: "2026-07-28T18:36:09+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e81925f355a0e0d30a13439a"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "2607.22535v1.pdf"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_c9041c97275871b77824303a"
input_sha256: "559ba2ac4c9fddaa59f49ba864a071f33354f56217589e5ce76357fc28cc5c33"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_474b5f9742996e9fc68609b6", "target_path": "vault/knowledge/concepts/concept_474b5f9742996e9fc68609b6-部署可用的机器人分解式视觉动作接口-deployment-available-robot-factored-visual-act.md", "base_sha256": null, "candidate_sha256": "61b2bbb0dbe595e5464df76ad837ee2efcf06b44c7f25480b40118e197c11382", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_5ca861abef46626ba2c2-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_474b5f9742996e9fc68609b6.md", "working_at": "2026-07-28T18:36:09+08:00"}]
existing_context: [{"id": "input_2df64789bf5a3babc166441f", "type": "input", "title": "2607.22535v1.pdf", "path": "vault/inputs/input-input_2df64789bf5a3babc166441f.md", "status": "active", "source_ids": ["source_e81925f355a0e0d30a13439a"], "snippet": "…The immutable Source remains authoritative.\n\n# [2607.22535v1.pdf]\n\n> 原始内容：[vault/raw/objects/sha256/55/9b/559ba2ac4c9fddaa59f49ba864a071f33354f56217589e5ce76357fc28cc5c33](../objects/sha256…", "match_reason": "metadata:title"}, {"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_82dbe72420b6c09b6365d051", "type": "input", "title": "[2607.22535] Robot-Factored World Models via Robot Rendering", "path": "vault/inputs/input-input_82dbe72420b6c09b6365d051.md", "status": "active", "source_ids": ["source_3b0dd57a10c8bd53518fdadc"], "snippet": "# [2607.22535] [Robot]-Factored World Models via [Robot] Rendering\n\nInput Episode for `source_3b0dd57a10c8bd53518fdadc`. The immutable Source remains…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-[Robot] separates navigation, manipulation, and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "concept_09dc6e910b167ba474c89c38", "type": "concept", "title": "世界动作模型的激活空间鲁棒性 steering", "path": "vault/memory/concept/concept_09dc6e910b167ba474c89c38.md", "status": "working", "source_ids": ["source_38cba686373b003398483ab2"], "snippet": "# 世界动作模型的激活空间鲁棒性 steering\n\n对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。", "match_reason": "metadata:aliases"}, {"id": "input_76b68fdb85fc376d2226e524", "type": "input", "title": "[2607.19190] Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents", "path": "vault/inputs/input-input_76b68fdb85fc376d2226e524.md", "status": "active", "source_ids": ["source_4ceaa5243dd0d99116547dda"], "snippet": "…Physics-based [World] Modeling with Vision-Language Agents\n\nInput Episode for `source_4ceaa5243dd0d99116547dda`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "input_e69b286ace68f56c81ab185b", "type": "input", "title": "[2607.12894] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents", "path": "vault/inputs/input-input_e69b286ace68f56c81ab185b.md", "status": "active", "source_ids": ["source_bd08e368730960f4f6ce19ca"], "snippet": "…Efficient Physical-[World] Agents\n\nInput Episode for `source_bd08e368730960f4f6ce19ca`. The immutable Source remains authoritative.\n\n# [2607.12894] Hy-Embodied…", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-Action [Models] with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "input_bf6f63ea23391740118ba725", "type": "input", "title": "Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema", "path": "vault/inputs/input-input_bf6f63ea23391740118ba725.md", "status": "active", "source_ids": ["source_d90b4e9bf278dfc5e68d1bb5"], "snippet": "# Frontier [Models] with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema\n\nInput Episode for `source_d90b4e9bf278dfc5e68d1bb5…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied Foundation [Models] for Real-World Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "concept_21a37fbe65868f6e97a68a20", "type": "concept", "title": "机器人坐标系稠密 Pointmap 观察接口", "path": "vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md", "status": "working", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# 机器人坐标系稠密 Pointmap 观察接口\n\n把 RGB-D 像素对应的三维点预先转换到机器人动作所用坐标系，并保留图像 H×W 网格供预训练 VLA 视觉通路编码。该接口减少相机视角到动作坐标的学习负担，但依赖深度和相机标定质量。", "match_reason": "metadata:aliases"}, {"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "reflection_7b23a8a7adc7b353d26fbc30", "type": "reflection", "title": "Robot-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制", "path": "vault/reflections/reflection-reflection_7b23a8a7adc7b353d26fbc30.md", "status": "active", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# [Robot]-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制\n\n## Why important\n\n[Robot]-centric pointmap 把每个 RGB-D 像素转换为机器人基座或末端中心坐标，同时保留 H…", "match_reason": "metadata:title"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e81925f355a0e0d30a13439a"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "66f55092b97414b2e15bf5d56fb96e87e88a847e4db2a4b5ed6ee6d8cf9ec73c"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：2607.22535v1.pdf

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_c9041c97275871b77824303a`
- 编译前召回已有对象：17
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_474b5f9742996e9fc68609b6-部署可用的机器人分解式视觉动作接口-deployment-available-robot-factored-visual-act.md
@@ -0,0 +1,20 @@
+---
+id: "concept_474b5f9742996e9fc68609b6"
+type: "concept"
+status: "proposal"
+title: "部署可用的机器人分解式视觉动作接口 / Deployment-available robot-factored visual action interface"
+created_at: "2026-07-28T18:36:05+08:00"
+updated_at: "2026-07-28T18:36:05+08:00"
+aliases: ["Robot-Factored World Models", "robot-factored visual world-model interface", "nominal trajectory rendering", "机器人分解式世界模型接口"]
+tags: []
+domains: ["robotics", "world-models", "action-representation", "embodied-ai"]
+confidence: "high"
+source_ids: ["source_e81925f355a0e0d30a13439a"]
+relations: [{"type": "derived_from", "target_id": "source_e81925f355a0e0d30a13439a", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_world_model_evaluation", "reason": "视觉动作接口隔离了动作实现与场景响应，但其真实价值仍需通过动作选择、规划和失败恢复等闭环指标验证，而不能只依赖像素相似度。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_e81925f355a0e0d30a13439a"
+reflection_context: {"reflection_ids": ["reflection_52b043d688d780a74db9a1c7"], "importance": "high", "changed_belief": "此前容易把动作条件世界模型的改进归因于更强的视频骨干；本文的同骨干比较表明，动作表示本身可以决定模型是否必须同时学习本体特定的动作实现和场景动力学。", "surprising": "名义轨迹并不需要预知真实接触结果；即便存在抓取失败、滑移等偏差，部署时可计算的机器人侧渲染仍优于向量或位姿注入。", "connections": [{"shared_mechanism": "都把世界模型用于动作条件的未来预测。", "boundary": "现有 action-centered joint world-action model 强调联合预测，而本文贡献是把机器人侧动作实现显式外置为可渲染接口。", "difference": "前者是预测架构概念，后者是部署可用的条件接口，不应合并。"}], "open_questions": ["当真实系统只有部分相机标定、柔性机构或接触丰富的工具时，名义渲染接口的收益会在何处失效？"]}
+---
+
+# 部署可用的机器人分解式视觉动作接口 / Deployment-available robot-factored visual action interface
+
+先把控制命令经机器人控制器或运动学展开为部署时可计算的名义轨迹，再用已知 URDF 与相机标定渲染机器人网格 RGB，并以末端执行器深度补充空间消歧；视频世界模型据此预测场景响应，而无需同时重新学习本体特定的动作实现。论文在 DROID 与 RoboCasa 的同骨干比较中报告该接口优于向量或位姿条件，并显示名义渲染加深度的增益；适用边界包括需要可靠的机器人模型和标定、动态相机场景信息可能不完整，以及成功轨迹不足以覆盖滑移、接触误差和失败。
```
