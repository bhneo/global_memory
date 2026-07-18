---
id: "experiment_b6f1e1956690ac08fd56a5da"
type: "experiment"
status: "working"
title: "Codex M7 真实读取与 receipt 回写验收"
created_at: "2026-07-16T21:57:20+08:00"
updated_at: "2026-07-18T16:03:19+08:00"
aliases: []
tags: ["m7", "agent-acceptance", "codex"]
domains: ["global-memory"]
confidence: "high"
source_ids: ["source_46d0aad5afd18dd21899796f"]
relations: [{"type": "derived_from", "target_id": "source_46d0aad5afd18dd21899796f", "reason": "由 Codex M7 acceptance receipt 提出", "confidence": "high", "created_by": "codex-acceptance-review", "status": "working"}]
change_reason: "补全真实验收步骤、故障、修复和结果，避免只保留 deterministic fallback 的首句"
memory_tier: "working"
created_by: "deterministic-bounded-bundle-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "deterministic-bounded-bundle-v1"
consolidation_count: 4
last_consolidated_at: "2026-07-18T16:03:19+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_d0aa087dcd1d1fd8e996"
origin_item_id: "experiment-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_d0aa087dcd1d1fd8e996-experiment-1-rev-90b64a245da2.md"
origin_candidate_sha256: "90b64a245da2cdb633df33e8597ccddeacccb7d917acca9cf20f11e34f7e8508"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "unknown"
last_consolidation_id: "consolidation_4be69f60a0c3b26de48d7a22"
---

# Codex M7 真实读取与 receipt 回写验收

## 验收路径

Codex 按 `vault/INDEX.md` 的入口执行了真实的 `gm context → task → receipt → proposal` 流程。任务是从限定 Context Pack 回答 VIA 论文的实验结论和适用边界，没有默认扫描整个 vault，也没有直接修改 canonical。

## 发现并修复的问题

- 完整自然语言问题最初因严格 all-term FTS 匹配返回空包；修复后只在主查询空召回时逐项尝试有区分度的空白分词，并在 Context Pack filters 中记录 `query_fallback`。
- Markdown Context Pack 最初从不存在的 `status` 字段渲染状态，显示为 `None`；修复为读取契约字段 `knowledge_status`。

## 修复后结果

原始完整问题成功选择 confirmed VIA claim 和相关 source，并保留 truth layer、状态、路径、evidence、verification、选择理由与截断报告。Codex 从该包得出有边界的回答：结果来自六项 robosuite 仿真任务，最小提示总体成功率 60%–88%；不能外推到真实机器人、动态控制、长期记忆或持续学习。

## 决定

Codex 第一条真实验收在上述两项修复后通过。该结论仍是 pending experiment proposal；是否进入 canonical 由用户审阅决定。Cursor 和 Claude 的真实验收尚未执行。
