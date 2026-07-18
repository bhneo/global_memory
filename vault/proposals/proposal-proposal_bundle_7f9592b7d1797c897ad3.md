---
id: "proposal_bundle_7f9592b7d1797c897ad3"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-18T16:30:42+08:00"
updated_at: "2026-07-18T16:30:42+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_4dd99b2ac6f08ddbdd26b117"
input_sha256: "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_22f24b48f35fd93994db4200", "target_path": "vault/knowledge/claims/claim_22f24b48f35fd93994db4200-ieee-robotics.md", "base_sha256": null, "candidate_sha256": "f47cccd083906cef2c0ce844a8e082b49c5b3cc9acecd666da4f514734af0f17", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "full", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7f9592b7d1797c897ad3-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_22f24b48f35fd93994db4200.md", "working_at": "2026-07-18T16:30:42+08:00"}, {"item_id": "claim-2", "object_type": "claim", "action": "create", "target_id": "claim_f18f73fad2499635f142ede5", "target_path": "vault/knowledge/claims/claim_f18f73fad2499635f142ede5-automation-letters-preprint-version-submitted-july-2026-1-human-.md", "base_sha256": null, "candidate_sha256": "3f2e6b4f6a1d58a2445e39a41cc3217835c99c7b45621a40c0ce3ec20141aed3", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7f9592b7d1797c897ad3-claim-2.md", "base_path": null, "working_path": "vault/memory/claim/claim_f18f73fad2499635f142ede5.md", "working_at": "2026-07-18T16:30:42+08:00"}, {"item_id": "claim-3", "object_type": "claim", "action": "create", "target_id": "claim_de218ebcf16d288520ce4d0e", "target_path": "vault/knowledge/claims/claim_de218ebcf16d288520ce4d0e-javier-gonzalez-jimenez-1-abstract-recent-advances-in-generative.md", "base_sha256": null, "candidate_sha256": "4491fd09aa53ad2924ad5d35b621b10467022046ef956f03f2f4cb2611d56029", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7f9592b7d1797c897ad3-claim-3.md", "base_path": null, "working_path": "vault/memory/claim/claim_de218ebcf16d288520ce4d0e.md", "working_at": "2026-07-18T16:30:42+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…The 2005 [IEEE] Congress on,\nvolume 1, pp. 128–135. [IEEE], 2005.\nLaland, K. N. Darwin’s unﬁnished…", "match_reason": "full-text:body"}, {"id": "claim_wechat_kairos_sim2real_training_20260716", "type": "claim", "title": "该文称 Kairos-HomeWorld 已用于大晓机器人训练，支持跨房间导航与全屋整理等长程任务并缩短 sim-to-real 迁移周期", "path": "vault/memory/claim/claim_wechat_kairos_sim2real_training_20260716.md", "status": "working", "source_ids": ["source_a20c5fb22d91216503d413e1"], "snippet": "# Sim-to-real\n\n跨房间/全屋整理训练；迁移周期声称待量化。", "match_reason": "metadata:tags"}, {"id": "claim_wechat_embodied_eval_bottleneck_20260715", "type": "claim", "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住", "path": "vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md", "status": "working", "source_ids": ["source_2d4f3a7d3525782c8ff503ee"], "snippet": "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_structure_not_volume_20260716", "type": "claim", "title": "该文主张机器人瓶颈不只是数据量，而是把数据转化为能力的结构与 recipe", "path": "vault/memory/claim/claim_wechat_embodied_data_structure_not_volume_20260716.md", "status": "working", "source_ids": ["source_0a113baae7ce4d1ab78da1a3"], "snippet": "# 结构 vs 数量\n\n缺的是把数据变成能力的结构，非单纯缺 TB 日志。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_embodied_data_quality_cost_tradeoff_20260716", "type": "claim", "title": "该文称具身数据采集存在质量与成本难以兼得的矛盾，并以特斯拉重资产遥操对比 OpenAI 低成本众包路线", "path": "vault/memory/claim/claim_wechat_embodied_data_quality_cost_tradeoff_20260716.md", "status": "working", "source_ids": ["source_cda5a1b9e036598aff53e5be"], "snippet": "# 质量 vs 成本\n\n遥操高精度 vs 众包低成本；难以兼得（文内观点）。", "match_reason": "metadata:domains"}, {"id": "claim_play2perfect_inhand_pretraining_20260715", "type": "claim", "title": "Play2Perfect 表明 play 预训练向装配迁移的关键是迫使手指 in-hand 操控而非固定抓握下的手臂运动", "path": "vault/memory/claim/claim_play2perfect_inhand_pretraining_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play 预训练中影响装配迁移的因素\n\n论文对 object diversity、training objective、trajectory diversity 和 goal precision 进行消融，并在四项装配任务、三个种子上比较下游 RL 微调。结果显示…", "match_reason": "metadata:domains"}, {"id": "claim_play2perfect_realworld_tight_insertion_20260715", "type": "claim", "title": "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10", "path": "vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 的真实世界紧配合插入结果\n\n论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 real-world finetuning…", "match_reason": "metadata:domains"}, {"id": "claim_play2perfect_finetuning_necessary_20260715", "type": "claim", "title": "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要", "path": "vault/memory/claim/claim_play2perfect_finetuning_necessary_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play 预训练与装配微调的职责边界\n\n论文在 Tight-Insertion 上比较冻结的 Play-only policy 和经过装配 RL 微调的 Play2Perfect。Play-only 只在宽松 clearance 下有较高成功率…", "match_reason": "metadata:domains"}, {"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-reward…", "match_reason": "metadata:domains"}, {"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "canonical", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "# VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人\n\n## 论文主张\n\nVIA 把机器人控制转换为视觉 Agent 的工具使用任务：未经机器人专项微调的前沿通用 Agent 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 3, "source_id": "source_a0c7811ba12c9cf80bfd26c9"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 3, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 3, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_4dd99b2ac6f08ddbdd26b117`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_22f24b48f35fd93994db4200-ieee-robotics.md
@@ -0,0 +1,32 @@
+---
+id: "claim_22f24b48f35fd93994db4200"
+type: "claim"
+status: "proposal"
+title: "IEEE ROBOTICS"
+created_at: "2026-07-18T16:30:42+08:00"
+updated_at: "2026-07-18T16:30:42+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
+relations: [{"type": "derived_from", "target_id": "source_a0c7811ba12c9cf80bfd26c9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_a0c7811ba12c9cf80bfd26c9"
+evidence: [{"evidence_id": "evidence_5b2b1a8feadf8f093c4c", "evidence_kind": "quote", "source_id": "source_a0c7811ba12c9cf80bfd26c9", "content_id": "content_dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extraction_id": "extraction_4dd99b2ac6f08ddbdd26b117", "span_start": 18, "span_end": 31, "original_text": "IEEE ROBOTICS", "interpretation": null, "section": null, "page": 1, "stance": "context", "verification_status": "verified", "input_sha256": "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "full"
+split_from: "IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1\nHuman-Robot Interaction in GenAI Architectures\nvia the Agent-Client Protocol\nJesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1, and Javier Gonzalez-Jimenez 1\nAbstract—Recent advances in Generative Artificial Intelligence\n(GenAI), particularly Large Language Models (LLMs), are driv-\ning robotic architectures toward agent-based high-level orches-\ntration, in which natural-language instructions can be translated\ninto "
+split_reason: "multiple independently testable clauses"
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# IEEE ROBOTICS
+
+IEEE ROBOTICS
```

### claim-2 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_f18f73fad2499635f142ede5-automation-letters-preprint-version-submitted-july-2026-1-human-.md
@@ -0,0 +1,32 @@
+---
+id: "claim_f18f73fad2499635f142ede5"
+type: "claim"
+status: "proposal"
+title: "AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1 Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol Jesus Moncada-Ramirez"
+created_at: "2026-07-18T16:30:42+08:00"
+updated_at: "2026-07-18T16:30:42+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
+relations: [{"type": "derived_from", "target_id": "source_a0c7811ba12c9cf80bfd26c9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_a0c7811ba12c9cf80bfd26c9"
+evidence: [{"evidence_id": "evidence_cbd962729a4b3e8a1480", "evidence_kind": "paraphrase", "source_id": "source_a0c7811ba12c9cf80bfd26c9", "content_id": "content_dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extraction_id": "extraction_4dd99b2ac6f08ddbdd26b117", "span_start": -1, "span_end": 190, "original_text": "AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1 Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol Jesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1,", "interpretation": "AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1 Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol Jesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1,", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1\nHuman-Robot Interaction in GenAI Architectures\nvia the Agent-Client Protocol\nJesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1, and Javier Gonzalez-Jimenez 1\nAbstract—Recent advances in Generative Artificial Intelligence\n(GenAI), particularly Large Language Models (LLMs), are driv-\ning robotic architectures toward agent-based high-level orches-\ntration, in which natural-language instructions can be translated\ninto "
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1 Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol Jesus Moncada-Ramirez
+
+AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1 Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol Jesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1,
```

### claim-3 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_de218ebcf16d288520ce4d0e-javier-gonzalez-jimenez-1-abstract-recent-advances-in-generative.md
@@ -0,0 +1,32 @@
+---
+id: "claim_de218ebcf16d288520ce4d0e"
+type: "claim"
+status: "proposal"
+title: "Javier Gonzalez-Jimenez 1 Abstract—Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driv- ing robot"
+created_at: "2026-07-18T16:30:42+08:00"
+updated_at: "2026-07-18T16:30:42+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_a0c7811ba12c9cf80bfd26c9"]
+relations: [{"type": "derived_from", "target_id": "source_a0c7811ba12c9cf80bfd26c9", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_a0c7811ba12c9cf80bfd26c9"
+evidence: [{"evidence_id": "evidence_38cf55d1fb41e6411103", "evidence_kind": "paraphrase", "source_id": "source_a0c7811ba12c9cf80bfd26c9", "content_id": "content_dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extraction_id": "extraction_4dd99b2ac6f08ddbdd26b117", "span_start": -1, "span_end": 284, "original_text": "Javier Gonzalez-Jimenez 1 Abstract—Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driv- ing robotic architectures toward agent-based high-level orches- tration, in which natural-language instructions can be translated into", "interpretation": "Javier Gonzalez-Jimenez 1 Abstract—Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driv- ing robotic architectures toward agent-based high-level orches- tration, in which natural-language instructions can be translated into", "section": "deterministic extracted block", "page": null, "stance": "context", "verification_status": "derived", "input_sha256": "dc3c104a1ecb28d6c1fee814096fdefcc667b9bc01b132204237726e087ee54d", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: "IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. SUBMITTED JULY , 2026 1\nHuman-Robot Interaction in GenAI Architectures\nvia the Agent-Client Protocol\nJesus Moncada-Ramirez 1, Jose-Raul Ruiz-Sarmiento 1, and Javier Gonzalez-Jimenez 1\nAbstract—Recent advances in Generative Artificial Intelligence\n(GenAI), particularly Large Language Models (LLMs), are driv-\ning robotic architectures toward agent-based high-level orches-\ntration, in which natural-language instructions can be translated\ninto "
+split_reason: "multiple independently testable clauses"
+quote_verification: "failed"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# Javier Gonzalez-Jimenez 1 Abstract—Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driv- ing robot
+
+Javier Gonzalez-Jimenez 1 Abstract—Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driv- ing robotic architectures toward agent-based high-level orches- tration, in which natural-language instructions can be translated into
```
