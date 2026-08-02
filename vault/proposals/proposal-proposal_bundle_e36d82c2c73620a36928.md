---
id: "proposal_bundle_e36d82c2c73620a36928"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T18:22:41+08:00"
updated_at: "2026-08-02T18:22:43+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_7fa8acc5e021363b55491e3e"]
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
extraction_id: "extraction_5fe7d54a6c0e30ca35803d7e"
input_sha256: "9a24a80ad02fc6a61b87cf42513004adf02c379fd576c7ef81d33ced1640e492"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_c5189a551eabdd0550bacd70", "target_path": "vault/knowledge/concepts/concept_c5189a551eabdd0550bacd70-未来触觉监督的部署一致信息隔离-deployment-consistent-isolation-of-future-tactil.md", "base_sha256": null, "candidate_sha256": "30a9d73be210489612bc2ab02a98701cc8052b6b91655f0fd3afc46d7db937e9", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_e36d82c2c73620a36928-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_c5189a551eabdd0550bacd70.md", "working_at": "2026-08-02T18:22:43+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_cde49d7c9071270dc3fb8348", "type": "input", "title": "World Action Planner: Generalizable Decision-Making with Action-Conditioned World Models", "path": "vault/inputs/input-input_cde49d7c9071270dc3fb8348.md", "status": "active", "source_ids": ["source_a54ea0123fbadf6d7012c9fb"], "snippet": "# World [Action] Planner: Generalizable Decision-Making with [Action]-Conditioned World Models\n\nInput Episode for `source_a54ea0123fbadf6d7012c9fb`. The immutable…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The [world] component and dual-system [world]-action models both use predictive representations to connect perception with possible…", "match_reason": "metadata:title"}, {"id": "input_82dbe72420b6c09b6365d051", "type": "input", "title": "[2607.22535] Robot-Factored World Models via Robot Rendering", "path": "vault/inputs/input-input_82dbe72420b6c09b6365d051.md", "status": "active", "source_ids": ["source_3b0dd57a10c8bd53518fdadc"], "snippet": "# [2607.22535] Robot-Factored [World] Models via Robot Rendering\n\nInput Episode for `source_3b0dd57a10c8bd53518fdadc`. The immutable Source remains…", "match_reason": "metadata:title"}, {"id": "concept_fdb5ce439cbb603e19af8653", "type": "concept", "title": "前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens", "path": "vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md", "status": "working", "source_ids": ["source_ba71396b5fc37637b125a89f"], "snippet": "# 前缀可解码的有序动作令牌 / Prefix-decodable ordered [action] tokens\n\n动作 tokenizer 同时满足高压缩、任意前缀都可解码为完整可执行动作块，以及由粗到细的有序精化。实现上以 transformer registers 和有限标量量化形成令牌，并用 nested dropout…", "match_reason": "metadata:title"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "synthesis_9ae225f58ef80075a6a8fdcf", "type": "synthesis", "title": "VLA execution interfaces: adaptive action precision without an LLM inner loop", "path": "vault/synthesis/synthesis-synthesis_9ae225f58ef80075a6a8fdcf.md", "status": "active", "source_ids": ["source_ba71396b5fc37637b125a89f", "source_feaf5bf5a081e27b445c569c"], "snippet": "…adaptive [action] precision without an LLM inner loop\n\n## Emerging patterns\n\n- The VLA execution contract now exposes two independent…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_7fa8acc5e021363b55491e3e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "b03e5f1947ccaed1e1b3adc09c3ecb192fee63304f21a4aad4f0b8380edd730f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_5fe7d54a6c0e30ca35803d7e`
- 编译前召回已有对象：11
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_c5189a551eabdd0550bacd70-未来触觉监督的部署一致信息隔离-deployment-consistent-isolation-of-future-tactil.md
@@ -0,0 +1,20 @@
+---
+id: "concept_c5189a551eabdd0550bacd70"
+type: "concept"
+status: "proposal"
+title: "未来触觉监督的部署一致信息隔离 / Deployment-consistent isolation of future-tactile supervision"
+created_at: "2026-08-02T18:22:41+08:00"
+updated_at: "2026-08-02T18:22:41+08:00"
+aliases: ["TacWAM", "AGT attention", "Anchor-Guided Tri-Modal Attention", "SAF tactile encoder"]
+tags: []
+domains: ["robotics", "tactile-manipulation", "world-action-model", "information-isolation"]
+confidence: "high"
+source_ids: ["source_7fa8acc5e021363b55491e3e"]
+relations: [{"type": "derived_from", "target_id": "source_7fa8acc5e021363b55491e3e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_1920583cd9c7063491d45a40", "reason": "两者都以未来触觉预测增强动作学习；TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉潜变量注入 action expert。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_c37ccf2640da63192432d5d5", "reason": "两者都用接触历史缓解部分可观测性；TacWAM 的触觉 latent 历史调制联合预测，既有概念的力历史压缩直接条件化动作。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "tension_bae77e2f84604668cacedd6c", "reason": "TacWAM 的掩码消融给出预测-动作对齐张力的结构性实例：未来目标泄漏可降低训练难度，却破坏部署一致性。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_7fa8acc5e021363b55491e3e"
+reflection_context: {"reflection_ids": ["reflection_7c31cec2267b21f33baf67f2"], "importance": "high", "changed_belief": "我原先倾向认为更充分的跨模态注意力有利于联合世界-动作建模；该消融显示，对未来目标的访问必须按部署可得性严格隔离，信息更多并不等于监督更有效。", "surprising": "仅放松 action-to-future-tactile 的掩码就使两任务平均成功率从完整模型的 82.5% 降到 37.5%，完全双向未来信息则降到 7.5%。", "connections": [{"shared_mechanism": "TacWAM 与 concept_1920583cd9c7063491d45a40 都用未来触觉预测迫使动作模型学习接触相关的中间表征。", "boundary": "该连接只覆盖预测触觉作为训练信号；两者当前证据都不能自动推出在线力安全或开放世界接触泛化。", "difference": "TacWAM 把未来触觉作为与动作隔离的并行监督，既有概念把预测的紧凑触觉 latent token 注入 action expert。"}, {"shared_mechanism": "TacWAM 与 concept_c37ccf2640da63192432d5d5 都利用接触历史缓解单帧观测下的部分可观测性。", "boundary": "历史只在传感器时序与任务接触模式覆盖范围内有效，不能替代异常力监控或形式安全门。", "difference": "TacWAM 用触觉 latent 历史调制视觉、触觉与动作联合预测，既有概念压缩近期力历史并直接条件化动作。"}, {"shared_mechanism": "TacWAM 与 tension_bae77e2f84604668cacedd6c 都要求把预测质量和部署可用的动作对齐分开审计。", "boundary": "TacWAM 的掩码消融只证明其四项任务中的信息泄漏危害，不能独立验证所有 world-action 架构的安全性。", "difference": "既有 Tension 给出一般评估边界，TacWAM 通过 action-to-future-token 的注意力可达性给出具体结构实例。"}], "open_questions": ["能否在不暴露未来真值 token 的前提下，让动作分支读取由自身候选动作因果生成的未来触觉预测，并保持训练与部署一致？"]}
+---
+
+# 未来触觉监督的部署一致信息隔离 / Deployment-consistent isolation of future-tactile supervision
+
+在视觉-触觉世界-动作联合训练中，未来目标应按部署可得性隔离：未来视觉、未来触觉和动作分支可以共享当前视觉与触觉锚点，但动作 token 不得读取由未来真值派生的目标 token，否则训练会利用部署时不存在的信息捷径。TacWAM 以 SAF 编码触觉外观、稠密力与形变流，并用触觉历史表征接触状态；AGT 掩码让未来视觉和未来触觉成为与动作并行的辅助目标。该未来触觉不是 action-conditioned 后果模型，解码预测也不用于在线闭环；证据目前限于一台机器人、四个任务和有限试验。
```
