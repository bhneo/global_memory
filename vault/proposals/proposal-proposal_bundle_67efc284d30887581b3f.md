---
id: "proposal_bundle_67efc284d30887581b3f"
type: "proposal"
status: "migrated"
title: "Compile bundle：google/asimov_agentic · Datasets at Hugging Face"
created_at: "2026-08-03T18:23:22+08:00"
updated_at: "2026-08-03T18:23:22+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a06c4ee2dabe3916d074bc1e"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "google/asimov_agentic · Datasets at Hugging Face"
source_authority: "unknown"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_230dd6adca0c4523f8bf9190"
input_sha256: "6356a13fa5776927f42a8a9332b8fbdd7934b4e5803a25558ff8155a0dc618ca"
bundle_items: [{"item_id": "work-1", "object_type": "work", "action": "create", "target_id": "work_asimov_agentic_safety_evaluation", "target_path": "vault/knowledge/works/work_asimov_agentic_safety_evaluation-asimov-agentic-safety-evaluation-asimov-具身智能体安全评测.md", "base_sha256": null, "candidate_sha256": "3e33657e1969d79d709bdb1d1084aad640d6dfd17e2f75d933b5b8002b4a8da2", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_67efc284d30887581b3f-work-1.md", "base_path": null, "working_path": "vault/memory/work/work_asimov_agentic_safety_evaluation.md", "working_at": "2026-08-03T18:23:22+08:00"}]
existing_context: [{"id": "input_e85b57f50a6ad4e6825ba667", "type": "input", "title": "google/asimov_agentic · Datasets at Hugging Face", "path": "vault/inputs/input-input_e85b57f50a6ad4e6825ba667.md", "status": "active", "source_ids": ["source_a06c4ee2dabe3916d074bc1e"], "snippet": "# google/asimov_agentic · Datasets at Hugging [Face]\n\nInput Episode for `source_a06c4ee2dabe3916d074bc1e`. The immutable Source remains authoritative.\n\n# google…", "match_reason": "metadata:title"}, {"id": "input_3b93bb83f5c7407a5a03dcad", "type": "input", "title": "Building scalable AI agents with modular prompt transpilation - Google Developers Blog", "path": "vault/inputs/input-input_3b93bb83f5c7407a5a03dcad.md", "status": "active", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# Building scalable AI agents with modular prompt transpilation - [Google] Developers Blog\n\nInput Episode for `source_3521fe9ac8d8f054440ec0af`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_ced7182acd54cc772f9868c7", "type": "input", "title": "Gemini Robotics ER 2", "path": "vault/inputs/input-input_ced7182acd54cc772f9868c7.md", "status": "active", "source_ids": ["source_4ef330780a196b3bf1fdfc2c"], "snippet": "…[Google] DeepMind blog [Google] Research blog [Google] Developers blog [Google] Cloud blog Back Products & platforms See all in…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_a06c4ee2dabe3916d074bc1e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "unknown", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "29a81779d6495ca7071a75dec74124bd466d65889d6366406912552d410bf371"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：google/asimov_agentic · Datasets at Hugging Face

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_230dd6adca0c4523f8bf9190`
- 编译前召回已有对象：3
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### work-1 (create work)

```diff
--- /dev/null
+++ candidate:vault/knowledge/works/work_asimov_agentic_safety_evaluation-asimov-agentic-safety-evaluation-asimov-具身智能体安全评测.md
@@ -0,0 +1,25 @@
+---
+id: "work_asimov_agentic_safety_evaluation"
+type: "work"
+status: "proposal"
+title: "Asimov Agentic Safety Evaluation / Asimov 具身智能体安全评测"
+created_at: "2026-08-03T18:23:22+08:00"
+updated_at: "2026-08-03T18:23:22+08:00"
+aliases: ["Asimov Agentic Safety", "google/asimov_agentic", "具身智能体安全评测", "agentic robotics safety evaluation"]
+tags: []
+domains: ["robot-safety", "agent-evaluation", "embodied-ai", "benchmarks", "uncertainty"]
+confidence: "medium"
+source_ids: ["source_a06c4ee2dabe3916d074bc1e"]
+relations: [{"type": "derived_from", "target_id": "source_a06c4ee2dabe3916d074bc1e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_asymmetric_frozen_vla_harness", "reason": "Asimov 的闭环 VLA estimator/emulator 与工具调用任务可评测高层 Agent 编排能力有界 VLA/API 时的可行性、约束与安全决策，但不授予运行时执行权限。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都在执行期把观察转成 stop/continue 或修复信号；Asimov 扩展到物理约束、不确定性、仪表和人类接近，CheckVLA 聚焦动作条件后果一致性。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_648a44e346f991eab5956e55", "reason": "Asimov 的物理约束与安全工具测试可用于检查语义层是否越权；FORGE-plus 则把不可提升力预算和硬权限留在快环，二者分别是评测面和控制契约。", "confidence": "medium", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_a06c4ee2dabe3916d074bc1e"
+work_type: "dataset"
+canonical_title: "Asimov Agentic Safety Evaluation"
+authors: ["Google"]
+language: "en"
+same_work_as: []
+reflection_context: {"reflection_ids": ["reflection_143f067fd8015dea49aaf62a"], "importance": "high", "changed_belief": "我原先会把具身 Agent 安全 benchmark 主要看成危险指令遵循；该 harness 显示，安全还需要同时测试物理能力边界、何时表达不可读/不确定、闭环规划中的成功概率与安全合规，以及时序视觉中的人类接近停机。", "surprising": "官方页面同时提供 tool_use 与 JSON prediction 协议，说明同一安全能力可以分别测最终权限动作和中间感知估计；但数据文件受 gated access 与 Git LFS 约束，当前阅读材料没有任何可核验模型结果。", "connections": [{"shared_mechanism": "Asimov 的 closed-loop estimator/emulator 与 concept_asymmetric_frozen_vla_harness 都把高层 Agent 对低层 VLA/API 的调用视为需要显式成功概率、约束和恢复检查的接口。", "boundary": "评测 harness 只能测预定义任务与阈值，不授予真实机器人执行权限，也不能覆盖未建模物理危险。", "difference": "现有 harness 节点描述运行时编排与恢复；Asimov 是用于比较模型在物理约束、可行性、不确定性和安全监控上的外部评测工具。"}, {"shared_mechanism": "人类接近与安全工具调用测试和 concept_2db7edf95d63ca80702f042e 都把观察转成执行期间的 stop/continue 或修复决策。", "boundary": "Asimov 的阈值与图像数据不能证明真实控制环的制动距离、延迟或伤害上界。", "difference": "CheckVLA 验证已提交动作的后果一致性；Asimov 评测物理约束、读数不确定性、人类接近和安全工具选择等更广的 Agent 决策面。"}], "open_questions": ["如何把这些离散评测协议连接成端到端 harm-oriented 安全曲线，同时保持 autorater、oracle instruction、距离阈值和真实制动动力学之间的边界可审计？"]}
+---
+
+# Asimov Agentic Safety Evaluation / Asimov 具身智能体安全评测
+
+Google 发布的可运行评测 harness 与 gated dataset，把具身 Agent 安全拆成物理约束决策、扩展对话 VLA 可行性、安全监控工具调用、不确定性消解、对抗仪表读取、闭环 VLA estimator/emulator 和时序人类接近检测。协议同时包含 tool_use 与 JSON prediction，并可用 Inspect trace 检查轨迹。当前官方页面只建立仓库结构、命令与接口：数据文件需接受条款并通过 Git LFS 获取，未提供可核验模型结果、样本质量审计、autorater 校准或真实硬件 harm/制动验证；该 Work 因此是评测资源，不是安全保证。
```
