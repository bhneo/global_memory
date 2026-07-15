---
id: "proposal_ab07afad179e245bd689b95d"
type: "proposal"
status: "superseded"
title: "模型提议：VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人"
created_at: "2026-07-15T11:31:57+08:00"
updated_at: "2026-07-15T11:34:09+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_5899fd47fd1a85ea3afcae99"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_via_interface_first_robot_control_20260715"
target_path: "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_ab07afad179e245bd689b95d.md"
candidate_sha256: "cfe08a304bbfde5016f68e3a2e3b90b614431c440b1641132137390f45667686"
change_reason: "从 VIA 原始论文导入有证据位置和适用边界的接口设计主张"
model_run: {"provider": "openai-codex", "model": "gpt-5", "prompt_version": "material-review-v1", "prompt_sha256": null, "input_source_id": "source_5899fd47fd1a85ea3afcae99", "input_sha256": "2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3", "uncertainty": "真实机器人、动态任务、跨 episode 记忆和跨模型文本示范收益尚未验证"}
reviewed_at: "2026-07-15T11:34:09+08:00"
review_reason: "URL capture 已完成，改用官方 arXiv web source 作为主证据链；保留旧 proposal 与本地重复来源审计历史"
superseded_by: "proposal_4c04c8ec3528956d9864772b"
---

# 模型提议：VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人

## 模型运行记录

- Provider：`openai-codex`
- Model：`gpt-5`
- Prompt version：`material-review-v1`
- Prompt SHA-256：`not-recorded`
- Input source：`source_5899fd47fd1a85ea3afcae99`
- Input SHA-256：`2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3`
- 不确定性：真实机器人、动态任务、跨 episode 记忆和跨模型文本示范收益尚未验证
- 提议理由：从 VIA 原始论文导入有证据位置和适用边界的接口设计主张
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md
@@ -0,0 +1,38 @@
+---
+id: "claim_via_interface_first_robot_control_20260715"
+type: "claim"
+status: "proposal"
+title: "VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人"
+created_at: "2026-07-15T11:32:00+08:00"
+updated_at: "2026-07-15T11:32:00+08:00"
+aliases: ["VIA Visual Interface Agent"]
+tags: ["agent-interface", "robot-control", "closed-loop", "tool-use", "simulation"]
+domains: ["agent-systems", "robotics", "global-memory-design"]
+confidence: "medium"
+source_ids: ["source_5899fd47fd1a85ea3afcae99"]
+relations: [{"type": "derived_from", "target_id": "source_5899fd47fd1a85ea3afcae99", "reason": "由 VIA 原始论文的方法、实验结果与局限直接归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "导入真实论文材料并保留实验与适用边界，等待人工审阅"
+applicability: ["VIA 论文报告的 robosuite 仿真环境", "六项准静态桌面操作任务", "使用论文定义的浏览器三维界面、MCP 工具和前沿视觉 Agent", "每个 agent-model-prompt-task 配置 10 个随机种子"]
+uncertainty: "论文尚未在真实机器人或动态任务上验证；主实验关闭跨 episode 记忆读写；Rainbow 由人工视觉判定；不同模型对文本示范的收益不一致，因此不能外推为长期记忆、持续学习或通用真实机器人可靠性的证据。"
+evidence: [{"source_id": "source_5899fd47fd1a85ea3afcae99", "location": "第 1-5 页，Figure 1-2、Section 3.1-3.3", "excerpt": "Agent 通过截图和人类可理解的工具调整虚拟目标夹爪，显式 execute_waypoint 后机器人执行，并在新观察上继续规划。", "stance": "supports", "reason": "直接描述无机器人微调、无特权状态的观察—操作—执行—再观察闭环及显式执行边界。"}, {"source_id": "source_5899fd47fd1a85ea3afcae99", "location": "第 6-8 页，Table 2、Section 4.1-4.2", "excerpt": "最小提示下各配置总体成功率为 60% 至 88%；CC-Fable 在三个 LIBERO-Goal 任务通过 29/30，并在 Rainbow 达到 100%。", "stance": "supports", "reason": "给出论文所研究接口在限定仿真任务中的零样本实验证据。"}, {"source_id": "source_5899fd47fd1a85ea3afcae99", "location": "第 6-8 页，实验协议、结果分析与 Limitations", "excerpt": "全部任务运行于模拟器；每配置每任务 10 个种子；主实验关闭 memory read/write；真实机器人属于下一步；慢推理限制系统用于准静态任务。", "stance": "context", "reason": "限定结果适用范围，防止把仿真闭环控制外推为长期记忆、持续学习或真实机器人通用能力。"}]
+---
+
+# VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人
+
+## 候选主张
+
+VIA 的实验表明：在论文定义的仿真桌面任务、浏览器三维界面和 MCP 工具条件下，未经机器人专项微调的前沿通用视觉 Agent，可以仅依靠界面观察、低层目标夹爪操作、显式 waypoint 执行和结果复查完成零样本闭环机器人控制。该证据支持“稳定、可观察、显式提交的 Agent 接口能够释放通用模型已有能力”，但不证明长期记忆、跨任务持续学习、动态控制或真实机器人可靠性。
+
+## 对 Global Memory 的设计启发（解释层，非论文直接实验结论）
+
+- 把可反复调整的候选状态与不可轻易撤销的真实执行分开，对应 proposal → inspect/diff → approve → canonical。
+- 每次工具操作后返回可观察状态、结构化结果和来源，使 Agent 能闭环验证而非开环连续修改。
+- 保留人类可检查的事实界面；索引、分数和模型内部状态不应成为隐藏的唯一真相源。
+- 工具保持最小、确定和符合 Agent 感知限制，同时避免一个会静默完成全部工作的高抽象接口。
+- 稳定、模型无关的工具协议可以继承未来模型能力提升；经审核的文本示范更适合作为 workflow/skill，而不是事实知识。
+
+## 审阅边界
+
+上述 Global Memory 映射是我们的架构类比，不是论文直接验证的记忆系统结论。批准本 proposal 只表示接受这一有范围限定的材料归纳，不表示接受“通用 Agent 已可取代机器人策略”或“自动记忆会自然带来持续学习”。
```
