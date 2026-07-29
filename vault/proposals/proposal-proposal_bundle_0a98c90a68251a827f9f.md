---
id: "proposal_bundle_0a98c90a68251a827f9f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T16:31:27+08:00"
updated_at: "2026-07-28T16:31:44+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-strong-model-m91-weekly-v3"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_6506a11d8f50ef2494f8b80e"
input_sha256: "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_4739daf4ef7eacc9153c535f", "target_path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "base_sha256": "1426d12910a7c17df821bee46f27059c5c1a1ee45a62de5ef6c1a5b0111df9ad", "candidate_sha256": "5f4ad6aaf9b5dba2ad04763e9fab603bb0b43e43c3d36f4f2c3e19040eadcc64", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0a98c90a68251a827f9f-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_0a98c90a68251a827f9f-concept-1.md", "working_path": "vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-28T16:31:44+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_052db872e2258b0e016c5ebf", "type": "reflection", "title": "UR-VC：先纠正进度代理，再训练价值或优势条件策略", "path": "vault/reflections/reflection-reflection_052db872e2258b0e016c5ebf.md", "status": "active", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# [UR-VC]：先纠正进度代理，再训练价值或优势条件策略\n\n## Why important\n\n它指出成功示范中的归一化时间并不等于物理进度，尤其接触和可变形物体任务会倒退、停滞或速度不均；错误代理会污染后续价值与优势监督。\n\n## What changed\n\n价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n\n## Surprising\n\n[UR]…", "match_reason": "metadata:title"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:aliases"}, {"id": "synthesis_a4a2bd5ddcee562f2574676f", "type": "synthesis", "title": "适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界", "path": "vault/synthesis/synthesis-synthesis_a4a2bd5ddcee562f2574676f.md", "status": "active", "source_ids": ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_40700e61702f4b5a5765e11d", "source_6b52a51e2b4a3be43c97c386", "source_7b278ba348f2a8bb94cce1fc", "source_91072aa553af99e6ab97c6cd", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…[UR-VC]、Robo-ValueRL 与 ActionCache 都在允许后续优化或复用前，用一个中介分数判断状态进展、行为质量或上下文相似性。\",\n    \"boundary\": \"时间位置、历史价值与多模态相似度都只是代理；遮挡、接触状态、多解任务和动力学差异会让高分代理对应错误物理状态。\",\n    \"difference\": \"[UR-VC]…", "match_reason": "full-text:body"}, {"id": "synthesis_1e641e385fe894f21693e284", "type": "synthesis", "title": "VLA 后训练的反馈接口：价值、Token、动作块与潜空间干预", "path": "vault/synthesis/synthesis-synthesis_1e641e385fe894f21693e284.md", "status": "active", "source_ids": ["source_40700e61702f4b5a5765e11d", "source_7b278ba348f2a8bb94cce1fc", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"], "snippet": "…mechanism\": \"Robo-ValueRL 与 [UR-VC] 都先提高进度或价值信号的可靠性，再让该信号参与策略改进。\",\n    \"boundary\": \"该连接只说明信号治理的共同位置，不表示训练式价值估计和无训练标签校正在方法或证据上等价。\",\n    \"difference\": \"[UR-VC] 校正离线时间代理；Robo-ValueRL 学习历史条件价值并延伸到在线数据筛选…", "match_reason": "full-text:body"}, {"id": "synthesis_60071a24c6e3071f6731c4e2", "type": "synthesis", "title": "VLA 后训练、动作观察接口与世界模型：分布、表示、反馈和可执行性", "path": "vault/synthesis/synthesis-synthesis_60071a24c6e3071f6731c4e2.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220", "source_4b25f596c34869693b9b8151", "source_4df1017326dd7cc4786f4218", "source_5b8c57a9bef3348109f3b7bb", "source_8b41a014bee47c4239a2fa81", "source_b64b4a539b8c17d0cfe662ba", "source_e6608d8f849ad472bbd95143", "source_ef80ef223077ef0855660839", "source_f4bd7390e1b485ab773f1446", "source_f9128ff3463cfaa7fa41ee7e", "source_fe986df678d73ef2b6234f0c"], "snippet": "…RL Token、PAC-ACT、FlowDAgger、Robo-ValueRL 与 [UR-VC] 都把适配压力放到较小接口，但位置不同：行为条件、内部读出、动作块、生成潜变量、历史价值或进度标签。\n- Pointmap…", "match_reason": "full-text:body"}, {"id": "concept_d7111f304971448401a57f3b", "type": "concept", "title": "冻结技能库与轻量路由适应", "path": "vault/memory/concept/concept_d7111f304971448401a57f3b.md", "status": "working", "source_ids": ["source_d83bb2c45bcaf70906e9ac96"], "snippet": "# 冻结技能库与轻量路由适应\n\n从多任务示范中学习紧凑、可复用且尽量非冗余的技能库，在迁移时冻结技能表示，只更新轻量路由器和动作头，以减少新任务少样本适应所需的参数与数据。", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e326446389e083c6ba9c94c2"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "2be8f6b637647bb53d07bf3052361aa8c21535a0d138a25ac1c27b5c015c2055"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-strong-model-m91-weekly-v3`
- Extraction：`extraction_6506a11d8f50ef2494f8b80e`
- 编译前召回已有对象：8
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md
+++ candidate:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_4739daf4ef7eacc9153c535f"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "可靠价值驱动的离线到在线策略改进"
 created_at: "2026-07-20T11:55:37+08:00"
-updated_at: "2026-07-20T11:56:59+08:00"
+updated_at: "2026-07-28T16:31:27+08:00"
 aliases: ["Robo-ValueRL", "value-guided offline-to-online adaptation"]
 tags: []
 domains: ["embodied-ai", "robot-rl", "vla", "value-learning"]
 confidence: "medium"
-source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
-relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}]
-change_reason: "compile bundle from source_7b278ba348f2a8bb94cce1fc"
-reflection_context: {"reflection_ids": ["reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-vla-posttraining-weekly-20260720"
-consolidation_count: 1
-last_consolidated_at: "2026-07-20T11:56:59+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_4b54c5c2979985532fa7"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_4b54c5c2979985532fa7-concept-1.md"
-origin_candidate_sha256: "95db7958cead1edd694b45998b7c0f21f1921311c766c8fc3f0203026af8b8ff"
-memory_schema_version: 2
-last_consolidation_id: "consolidation_bc26ef979b149316e780adba"
+source_ids: ["source_7b278ba348f2a8bb94cce1fc", "source_e326446389e083c6ba9c94c2"]
+relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-vla-posttraining-weekly-20260720", "status": "working"}, {"type": "depends_on", "target_id": "concept_abb38fe58cbeee09ce87a01d", "reason": "当价值监督来自时间进度时，先校正跨轨迹进度代理是避免下游选择偏差自强化的上游条件。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
+change_reason: "compile bundle from source_e326446389e083c6ba9c94c2"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_052db872e2258b0e016c5ebf", "reflection_617843f93885fb6b0d3c5f52"], "importance": "weekly", "changed_belief": "价值学习的上游问题不只是估计器容量，而是监督目标是否系统性偏置；在学习更强价值模型前，可以先利用跨轨迹相似状态校正时间标签。\n此前容易把离线到在线 RL 的关键归结为更多 rollout 或更强优化器；该材料提示，价值估计能否保持全局进度、局部流畅性并识别执行错误，可能先于在线更新规模决定改进是否稳定。", "surprising": "UR-VC 不训练额外模型，也不需要人工进度或奖励标签，而是聚合其他轨迹中相似状态的时间位置，恢复局部倒退和非均匀进度。\n同一价值信号既被用来构造离线动作质量条件，也被用来过滤在线片段和门控轻量残差适配，形成了一条统一的数据利用链。", "connections": [{"shared_mechanism": "与 Robo-ValueRL 都把任务进度或价值作为策略改进的中介信号，并强调该信号的可靠性。", "boundary": "UR-VC 校正的是示范内时间代理，依赖跨轨迹可检索的相似状态；它不是在线价值学习器，也没有直接证明能稳定提升所有 VLA。", "difference": "UR-VC 在训练前修正监督标签且不训练价值模型；Robo-ValueRL 学习历史条件价值并把它用于离线质量条件和在线残差适应。"}, {"shared_mechanism": "与 RL Token 都用轻量适配器保留预训练策略先验，并把在线学习集中到高价值的局部修正。", "boundary": "Robo-ValueRL 当前证据来自官方项目页，尚不能按论文正文验证训练细节、基线和统计显著性。", "difference": "Robo-ValueRL 的核心接口是历史条件价值及其质量标签；RL Token 的核心接口是从 VLA 内部特征读出的紧凑表征。"}], "open_questions": ["如何在遮挡、形变和多解任务中验证检索到的相似状态具有相同物理进度？", "价值可靠性指标在不同任务阶段与不同视觉历史长度下，能否稳定预测实际策略收益？"]}
+proposed_status: "working"
 ---
 
 # 可靠价值驱动的离线到在线策略改进
 
 可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。
+
+## 新增来源材料
+
+- `source_e326446389e083c6ba9c94c2`：可靠价值驱动的离线到在线改进需要在价值学习之前增加代理校准门禁。若训练标签来自归一化时间，必须先检验停滞、倒退与非均匀进度，并用跨轨迹状态一致性或其他物理信号校正；历史条件价值随后才能用于质量条件、在线片段筛选和残差门控。跨轨迹视觉相似与价值估计都可能偏置，因此两级置信度必须分别评估，不能由下游策略收益反向证明上游代理正确。
```
