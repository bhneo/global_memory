---
id: "experiment_7101e03fb065226e65f388a5"
type: "experiment"
status: "proposal"
title: "Cursor M7 真实读取与 receipt 回写验收"
created_at: "2026-07-16T22:16:57+08:00"
updated_at: "2026-07-16T22:16:57+08:00"
aliases: []
tags: ["m7", "agent-acceptance", "cursor"]
domains: ["global-memory"]
confidence: "high"
source_ids: ["source_113d589e6dadf14b5fa8edea"]
relations: [{"type": "derived_from", "target_id": "source_113d589e6dadf14b5fa8edea", "reason": "由 Cursor M7 acceptance receipt 提出", "confidence": "high", "created_by": "cursor-acceptance-review", "status": "proposal"}]
change_reason: "补全真实验收步骤、Context Pack 边界、故障和结果，避免只保留 deterministic fallback 的首句"
---

# Cursor M7 真实读取与 receipt 回写验收

## 验收路径

Cursor 按协议读取了 `AGENTS.md`、`.cursor/rules/global-memory.mdc` 和 `vault/INDEX.md`，随后执行 `gm maintain` 与 `gm context`（通过 `python -m global_memory`，因 PowerShell 将 `gm` 别名为 `Get-Member`）。任务是从限定 Context Pack 回答 VIA 实验结论和适用边界，没有扫描整个 vault，也没有直接修改 canonical。

## Context Pack 结果

- 查询成功返回 1 项、0 省略、预算未耗尽。
- 选中的是先前 Codex M7 验收 receipt（`source_46d0aad5afd18dd21899796f`），而非 confirmed VIA claim 或论文 source。
- 证据边界为 second-hand：答案来自 receipt 中对 VIA 的摘要，缺少 claim ID 与论文 source ID 的直接链接。

## 任务回答（受 receipt 内容约束）

- 主要结论：VIA 在六项 robosuite 仿真任务中通过 browser visual/tool interface 实现 zero-shot closed-loop manipulation；最小提示总体成功率 60%–88%；CC-Fable 在三项 LIBERO-Goal 任务 29/30、Rainbow 100%。
- 适用边界：仅限仿真、多为 quasi-static 任务、每配置 ten seeds、主设置 cross-episode memory disabled。
- 不能从论文推出：真实机器人部署、动态控制、长期记忆、持续学习、替代通用 robot-control policy。

## 发现的问题

- PowerShell `gm` 别名冲突，需使用 `.\scripts\gm.ps1` 或 `python -m global_memory`。
- Context Pack 检索可能回归或排序问题：完整 VIA 查询返回 Codex receipt 而非 VIA claim/source（与 Codex 修复后报告不一致）。

## 决定

Cursor read → task → receipt → proposal 路径已执行。未编辑或批准 canonical。该结论仍是 pending experiment proposal；是否进入 canonical 由用户审阅决定。
