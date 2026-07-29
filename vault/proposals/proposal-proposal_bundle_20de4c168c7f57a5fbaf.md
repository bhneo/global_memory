---
id: "proposal_bundle_20de4c168c7f57a5fbaf"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-22T18:11:31+08:00"
updated_at: "2026-07-22T18:11:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5260f9244a5030c2143c36e4"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_a41f26eac8c9bbade595bb1b"
input_sha256: "f90c30536dedbf80760901df70be61560dc15f8086309eb64048382111ad7d05"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_3b83de1641240159d66c23d4", "target_path": "vault/knowledge/concepts/concept_3b83de1641240159d66c23d4-显式时钟的异步机器人闭环程序.md", "base_sha256": null, "candidate_sha256": "b92fddc065bddc2d5bca04267f46e757a5bac201787e9c4676434fa103e5a231", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_20de4c168c7f57a5fbaf-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_3b83de1641240159d66c23d4.md", "working_at": "2026-07-22T18:11:32+08:00"}]
existing_context: [{"id": "claim_via_interface_first_robot_control_20260715", "type": "claim", "title": "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人", "path": "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md", "status": "canonical", "source_ids": ["source_86bad679192d3c34f728058b"], "snippet": "# VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人\n\n## 论文主张\n\nVIA 把机器人控制转换为视觉 Agent 的工具使用任务：未经机器人专项微调的前沿通用 Agent 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划…", "match_reason": "metadata:tags"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Generated future video is not itself evidence of contact-accurate dynamics, safe planning, or [closed-loop] execution. Separate…", "match_reason": "full-text:body"}, {"id": "experiment_7101e03fb065226e65f388a5", "type": "experiment", "title": "Cursor M7 真实读取与 receipt 回写验收", "path": "vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md", "status": "working", "source_ids": ["source_113d589e6dadf14b5fa8edea"], "snippet": "…仿真任务中通过 browser visual/tool interface 实现 zero-shot [closed-loop] manipulation；最小提示总体成功率 60%–88%；CC-Fable 在三项 LIBERO…", "match_reason": "full-text:body"}, {"id": "reflection_2183dcf7c9014c62c99ce9d6", "type": "reflection", "title": "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths", "path": "vault/reflections/reflection-reflection_2183dcf7c9014c62c99ce9d6.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "…foregrounds engineering details such as reset burden and [asynchronous] data collection, suggesting that throughput and recovery can dominate…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5260f9244a5030c2143c36e4"}
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

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_a41f26eac8c9bbade595bb1b`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_3b83de1641240159d66c23d4-显式时钟的异步机器人闭环程序.md
@@ -0,0 +1,20 @@
+---
+id: "concept_3b83de1641240159d66c23d4"
+type: "concept"
+status: "proposal"
+title: "显式时钟的异步机器人闭环程序"
+created_at: "2026-07-22T18:11:31+08:00"
+updated_at: "2026-07-22T18:11:31+08:00"
+aliases: ["Explicit-Clock Asynchronous Robot Programs", "Retriever", "异步机器人闭环程序"]
+tags: []
+domains: ["robot-systems", "embodied-ai"]
+confidence: "medium"
+source_ids: ["source_5260f9244a5030c2143c36e4"]
+relations: [{"type": "derived_from", "target_id": "source_5260f9244a5030c2143c36e4", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "二者都要求把组合边界显式化；前者规定时间与数据消费，后者规定任务验证与恢复。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_5260f9244a5030c2143c36e4"
+reflection_context: {"reflection_ids": ["reflection_11d7846e1ebfa021b7ef74ac"], "importance": "high", "changed_belief": "此前容易把异步执行当作部署细节；该工作表明输入消费语义和运行时钟会改变闭环行为，因而必须成为程序接口的一部分。", "surprising": "", "connections": [{"shared_mechanism": "两者都把机器人任务拆成带明确接口与验证点的可组合节点。", "boundary": "该连接只涉及运行时调度与输入同步，不证明任意技能节点的物理正确性。", "difference": "Retriever 定义多速率流和同步策略；技能图关注任务前置条件、验证与恢复语义。"}], "open_questions": ["对感知延迟或时钟漂移的最小可复现测试集应如何定义？"]}
+---
+
+# 显式时钟的异步机器人闭环程序
+
+将感知、状态更新、规划和控制表示为有状态因果流图；每个节点声明运行时钟，每条边声明同步或缓冲策略，使多速率闭环在固定时钟、同步策略和输入轨迹下可重放与调试。该抽象不能替代对单个模块感知精度、控制稳定性或实机安全的验证。
```
