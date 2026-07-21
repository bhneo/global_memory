---
id: "proposal_bundle_cd720382dd1ddfa13fe5"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:39:31+08:00"
updated_at: "2026-07-20T12:39:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_37fe3c1f9d9fb7daa262fa91"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-c-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "degraded"
extraction_quality: "degraded"
extraction_id: "extraction_0461c1d31ab0d9953067e43a"
input_sha256: "5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_5b49f7afd60ba18d35ca58e8", "target_path": "vault/knowledge/concepts/concept_5b49f7afd60ba18d35ca58e8-触觉对齐的人到机器人接触迁移.md", "base_sha256": null, "candidate_sha256": "aa6ee2f3ecdda77c7f8cf33f3d65a6db3039bd51c43e9a97c694fd6c81c1b006", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_cd720382dd1ddfa13fe5-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md", "working_at": "2026-07-20T12:39:32+08:00"}]
existing_context: [{"id": "claim_play2perfect_realworld_tight_insertion_20260715", "type": "claim", "title": "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10", "path": "vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 的真实世界紧配合插入结果\n\n论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 [real-world] finetuning…", "match_reason": "full-text:body"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "…个百分点；相对 EVOLVE-VLA，平均提高 2.0 个百分点。\n\n这些结果来自 LIBERO 仿真 [benchmark]，论文对自行运行的方法报告 5 个独立种子的 mean±std；它们不能直接外推为真实机器人成功率。", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_37fe3c1f9d9fb7daa262fa91"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "degraded", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-daily-batch-c-20260720`
- Extraction：`extraction_0461c1d31ab0d9953067e43a`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_5b49f7afd60ba18d35ca58e8-触觉对齐的人到机器人接触迁移.md
@@ -0,0 +1,20 @@
+---
+id: "concept_5b49f7afd60ba18d35ca58e8"
+type: "concept"
+status: "proposal"
+title: "触觉对齐的人到机器人接触迁移"
+created_at: "2026-07-20T12:39:31+08:00"
+updated_at: "2026-07-20T12:39:31+08:00"
+aliases: ["Tactile-aligned human-to-robot contact transfer", "TactiDex", "TactiSkill", "接触保真迁移"]
+tags: []
+domains: ["embodied-ai", "dexterous-manipulation", "tactile-transfer", "contact-evaluation"]
+confidence: "high"
+source_ids: ["source_37fe3c1f9d9fb7daa262fa91"]
+relations: [{"type": "derived_from", "target_id": "source_37fe3c1f9d9fb7daa262fa91", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "触觉迁移提供目标接触结构，多时间尺度控制提供运行时预测与快速纠偏，两者覆盖训练 reference 与执行闭环的不同环节。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-c-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_37fe3c1f9d9fb7daa262fa91"
+reflection_context: {"reflection_ids": ["reflection_e8e62c04da8ad9f420c37be4"], "importance": "high", "changed_belief": "此前人到机器人 dexterous transfer 常以轨迹或成功率衡量；该工作提示，接触时空位置和力分布应成为独立指标，否则策略可能完成几何动作却以不稳定或不安全的接触方式完成。", "surprising": "纯运动学 baseline 的 kinematic success 明显高于 tactile-aware success；但当前真机部署虽然硬件有触觉，执行时并未把触觉作为闭环反馈。", "connections": [{"shared_mechanism": "与多时间尺度触觉世界模型控制都把触觉定义为目标接触结构和在线误差信号，而非普通附加模态。", "boundary": "TactiSkill 的真实部署当前主要继承仿真中学习的触觉约束，传感噪声、分辨率与柔顺性差异会削弱 sim-to-real 力对齐；闭环真机触觉适配仍是未来工作。", "difference": "多时间尺度触觉世界模型强调运行时分层预测与残差；TactiDex/TactiSkill 首先提供人类触觉 reference、三分量奖励与接触保真评测。"}], "open_questions": ["哪些人类触觉特征应跨本体保持，哪些应按机器人形态、材料和任务安全约束重新标定？"]}
+---
+
+# 触觉对齐的人到机器人接触迁移
+
+在人类示范中同步手部运动学、物体状态和全手压力，把接触形成、接触区域时序、力幅值与安全约束作为独立监督和评测维度。该范式纠正纯运动学模仿的接触缺口，但跨本体时不应假设人类接触分布可无条件照搬。
```
