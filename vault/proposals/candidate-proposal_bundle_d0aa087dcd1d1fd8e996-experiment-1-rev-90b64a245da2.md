---
id: "experiment_b6f1e1956690ac08fd56a5da"
type: "experiment"
status: "proposal"
title: "Codex M7 真实读取与 receipt 回写验收"
created_at: "2026-07-16T21:57:20+08:00"
updated_at: "2026-07-16T21:57:20+08:00"
aliases: []
tags: ["m7", "agent-acceptance", "codex"]
domains: ["global-memory"]
confidence: "high"
source_ids: ["source_46d0aad5afd18dd21899796f"]
relations: [{"type": "derived_from", "target_id": "source_46d0aad5afd18dd21899796f", "reason": "由 Codex M7 acceptance receipt 提出", "confidence": "high", "created_by": "codex-acceptance-review", "status": "proposal"}]
change_reason: "补全真实验收步骤、故障、修复和结果，避免只保留 deterministic fallback 的首句"
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
