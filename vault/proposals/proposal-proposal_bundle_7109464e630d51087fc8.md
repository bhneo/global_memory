---
id: "proposal_bundle_7109464e630d51087fc8"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-18T16:30:40+08:00"
updated_at: "2026-07-18T16:30:40+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_79475aef7849b08664b51a4e"]
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
extraction_id: "extraction_0910d8df1547c174208b8eba"
input_sha256: "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_9e31e4b4eddc1ce8ee21db0f", "target_path": "vault/knowledge/claims/claim_9e31e4b4eddc1ce8ee21db0f-来源原文-2026-7-17-robottt-context-scaling-for-robot-policies-yunfan.md", "base_sha256": null, "candidate_sha256": "a5dc21022d9c72d63c3f487427ed5f50bae2e30d7c62035018f15ad8aee3c2b1", "decision": "working", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_7109464e630d51087fc8-claim-1.md", "base_path": null, "working_path": "vault/memory/claim/claim_9e31e4b4eddc1ce8ee21db0f.md", "working_at": "2026-07-18T16:30:40+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…In theHarvest MARL\n\n<!-- [page]: 4 -->\n\nSocial Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL\nsetting, it is…", "match_reason": "full-text:body"}, {"id": "work_arxiv_2607_11119", "type": "work", "title": "VIA: Interface-first Robot Control", "path": "vault/memory/work/work_arxiv_2607_11119.md", "status": "working", "source_ids": ["source_5899fd47fd1a85ea3afcae99", "source_86bad679192d3c34f728058b"], "snippet": "…Interface-first [Robot] Control\n\n## Logical work identity\n\n- arXiv：`2607.11119`\n- Version：`v1`\n- Captures：`source_5899fd47fd1a85ea3afcae99`, `source_86bad679192d3c34f728058b`\n\n此对象聚合现实世界作品身份…", "match_reason": "metadata:title"}, {"id": "claim_wechat_embodied_eval_bottleneck_20260715", "type": "claim", "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住", "path": "vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md", "status": "working", "source_ids": ["source_2d4f3a7d3525782c8ff503ee"], "snippet": "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。", "match_reason": "metadata:tags"}, {"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "canonical", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "# VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人\n\n## 论文主张\n\nVIA 把机器人控制转换为视觉 Agent 的工具使用任务：未经机器人专项微调的前沿通用 Agent 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划…", "match_reason": "metadata:tags"}, {"id": "claim_agentic_vla_training_efficiency_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×", "path": "vault/memory/claim/claim_agentic_vla_training_efficiency_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的训练效率\n\n在 LIBERO-Long 达到论文定义的 90% 成功率阈值时，Agentic-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE…", "match_reason": "metadata:domains"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-Long 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "metadata:domains"}, {"id": "claim_agentic_vla_one_shot_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点", "path": "vault/memory/claim/claim_agentic_vla_one_shot_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 one-shot 结果\n\n在每个任务仅使用一条 demonstration 做 SFT pre-training 的设定下，Agentic-VLA 在 LIBERO 四套件上的平均成功率为…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_79475aef7849b08664b51a4e"}
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

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_0910d8df1547c174208b8eba`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_9e31e4b4eddc1ce8ee21db0f-来源原文-2026-7-17-robottt-context-scaling-for-robot-policies-yunfan.md
@@ -0,0 +1,43 @@
+---
+id: "claim_9e31e4b4eddc1ce8ee21db0f"
+type: "claim"
+status: "proposal"
+title: "来源原文：2026-7-17\nRoboTTT: Context Scaling for Robot Policies\nYunfan Jiang1,2, Yevgen Ch"
+created_at: "2026-07-18T16:30:40+08:00"
+updated_at: "2026-07-18T16:30:40+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_79475aef7849b08664b51a4e"]
+relations: [{"type": "derived_from", "target_id": "source_79475aef7849b08664b51a4e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_79475aef7849b08664b51a4e"
+evidence: [{"evidence_id": "evidence_51f6f595cb7d49b1a296", "evidence_kind": "quote", "source_id": "source_79475aef7849b08664b51a4e", "content_id": "content_6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0", "extraction_id": "extraction_0910d8df1547c174208b8eba", "span_start": 18, "span_end": 518, "original_text": "2026-7-17\nRoboTTT: Context Scaling for Robot Policies\nYunfan Jiang1,2, Yevgen Chebotar1, Ruijie Zheng1, Fengyuan Hu1, Yunhao Ge1\nJimmy Wu1, Tianyuan Dai1,3, Scott Reed1, Li Fei-Fei2,†, Yuke Zhu1,3,†, Linxi “Jim” Fan1,†\n1NVIDIA 2Stanford University 3The University of Texas at Austin †Equal advising\nresearch.nvidia.com/labs/gear/robottt\nBetter Long-Horizon Task Performance (Duration = 5 Minutes)\nOne-Shot Imitation from In-Context Human Demonstration\nIn-Context Human Demonstration Top View\nBottom V", "interpretation": null, "section": null, "page": 1, "stance": "context", "verification_status": "verified", "input_sha256": "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0", "extractor": "pypdf", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: null
+split_reason: null
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "primary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 来源原文：2026-7-17
+RoboTTT: Context Scaling for Robot Policies
+Yunfan Jiang1,2, Yevgen Ch
+
+2026-7-17
+RoboTTT: Context Scaling for Robot Policies
+Yunfan Jiang1,2, Yevgen Chebotar1, Ruijie Zheng1, Fengyuan Hu1, Yunhao Ge1
+Jimmy Wu1, Tianyuan Dai1,3, Scott Reed1, Li Fei-Fei2,†, Yuke Zhu1,3,†, Linxi “Jim” Fan1,†
+1NVIDIA 2Stanford University 3The University of Texas at Austin †Equal advising
+research.nvidia.com/labs/gear/robottt
+Better Long-Horizon Task Performance (Duration = 5 Minutes)
+One-Shot Imitation from In-Context Human Demonstration
+In-Context Human Demonstration Top View
+Bottom V
```
