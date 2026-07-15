---
id: "proposal_2bda12923e2b1eb92619a249"
type: "proposal"
status: "approved"
title: "更新 VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人"
created_at: "2026-07-15T11:46:12+08:00"
updated_at: "2026-07-15T11:48:55+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_86bad679192d3c34f728058b"]
relations: []
proposal_kind: "knowledge_update"
processor: "explicit-candidate-v1"
action: "update"
target_id: "claim_via_interface_first_robot_control_20260715"
target_path: "vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md"
base_path: "vault/proposals/base-proposal_2bda12923e2b1eb92619a249.md"
base_sha256: "68293f443040863e62c6890f58ad0fa752c8cd333b9d267eef8f94c9b09ac7d5"
candidate_path: "vault/proposals/candidate-proposal_2bda12923e2b1eb92619a249.md"
candidate_sha256: "91da9afb63f1033b4f846f3fe3aa20fe2f37adbada50c34653c79fd577fda2bb"
change_reason: "真实材料导入的目标是忠实保存论文知识并验证系统，不要求材料服务于 Global Memory 自身设计；删除越界的架构类比"
reviewed_at: "2026-07-15T11:48:55+08:00"
review_reason: "人工通过 CLI 明确批准"
---

# 更新 VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人

## 更新说明

- Target：`claim_via_interface_first_robot_control_20260715`
- Base SHA-256：`68293f443040863e62c6890f58ad0fa752c8cd333b9d267eef8f94c9b09ac7d5`
- Candidate SHA-256：`91da9afb63f1033b4f846f3fe3aa20fe2f37adbada50c34653c79fd577fda2bb`
- 变更理由：真实材料导入的目标是忠实保存论文知识并验证系统，不要求材料服务于 Global Memory 自身设计；删除越界的架构类比
- 并发策略：审批时 target 必须仍等于 base；不自动合并。

## Base → Candidate Diff

```diff
--- base:vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md
+++ candidate:vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md
@@ -1,39 +1,43 @@
 ---
 id: "claim_via_interface_first_robot_control_20260715"
 type: "claim"
-status: "confirmed"
-title: "VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人"
+status: "proposal"
+proposed_status: "confirmed"
+title: "VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人"
 created_at: "2026-07-15T11:32:00+08:00"
 updated_at: "2026-07-15T11:41:30+08:00"
 aliases: ["VIA Visual Interface Agent"]
 tags: ["agent-interface", "robot-control", "closed-loop", "tool-use", "simulation"]
-domains: ["agent-systems", "robotics", "global-memory-design"]
+domains: ["agent-systems", "robotics"]
 confidence: "medium"
 source_ids: ["source_86bad679192d3c34f728058b"]
 relations: [{"type": "derived_from", "target_id": "source_86bad679192d3c34f728058b", "reason": "由 arXiv 官方 URL 捕获的 VIA 原始论文方法、实验结果与局限直接归纳"}]
 superseded_by: null
 valid_during: null
-change_reason: "URL capture 已完成，改用官方 arXiv web source 作为主证据链；保留旧 proposal 与本地重复来源审计历史"
+change_reason: "纠正首次导入时把机器人接口论文强行映射到 Global Memory 的范围偏差；只保留论文知识与证据边界"
 applicability: ["VIA 论文报告的 robosuite 仿真环境", "六项准静态桌面操作任务", "使用论文定义的浏览器三维界面、MCP 工具和前沿视觉 Agent", "每个 agent-model-prompt-task 配置 10 个随机种子"]
 uncertainty: "论文尚未在真实机器人或动态任务上验证；主实验关闭跨 episode 记忆读写；Rainbow 由人工视觉判定；不同模型对文本示范的收益不一致，因此不能外推为长期记忆、持续学习或通用真实机器人可靠性的证据。"
 evidence: [{"source_id": "source_86bad679192d3c34f728058b", "location": "第 1-5 页，Figure 1-2、Section 3.1-3.3", "excerpt": "Agent 通过截图和人类可理解的工具调整虚拟目标夹爪，显式 execute_waypoint 后机器人执行，并在新观察上继续规划。", "stance": "supports", "reason": "直接描述无机器人微调、无特权状态的观察—操作—执行—再观察闭环及显式执行边界。"}, {"source_id": "source_86bad679192d3c34f728058b", "location": "第 6-8 页，Table 2、Section 4.1-4.2", "excerpt": "最小提示下各配置总体成功率为 60% 至 88%；CC-Fable 在三个 LIBERO-Goal 任务通过 29/30，并在 Rainbow 达到 100%。", "stance": "supports", "reason": "给出论文所研究接口在限定仿真任务中的零样本实验证据。"}, {"source_id": "source_86bad679192d3c34f728058b", "location": "第 6-8 页，实验协议、结果分析与 Limitations", "excerpt": "全部任务运行于模拟器；每配置每任务 10 个种子；主实验关闭 memory read/write；真实机器人属于下一步；慢推理限制系统用于准静态任务。", "stance": "context", "reason": "限定结果适用范围，防止把仿真闭环控制外推为长期记忆、持续学习或真实机器人通用能力。"}]
-approved_via: "proposal_4c04c8ec3528956d9864772b"
 ---
 
-# VIA 表明稳定的视觉工具界面可让通用 Agent 在限定仿真任务中零样本闭环控制机器人
+# VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人
 
-## 候选主张
+## 论文主张
 
-VIA 的实验表明：在论文定义的仿真桌面任务、浏览器三维界面和 MCP 工具条件下，未经机器人专项微调的前沿通用视觉 Agent，可以仅依靠界面观察、低层目标夹爪操作、显式 waypoint 执行和结果复查完成零样本闭环机器人控制。该证据支持“稳定、可观察、显式提交的 Agent 接口能够释放通用模型已有能力”，但不证明长期记忆、跨任务持续学习、动态控制或真实机器人可靠性。
+VIA 把机器人控制转换为视觉 Agent 的工具使用任务：未经机器人专项微调的前沿通用 Agent 观察浏览器中的三维点云和相机画面，通过 MCP 工具设置虚拟目标夹爪，显式执行 waypoint，再根据新观察纠错和继续规划。
 
-## 对 Global Memory 的设计启发（解释层，非论文直接实验结论）
+## 实验结果
 
-- 把可反复调整的候选状态与不可轻易撤销的真实执行分开，对应 proposal → inspect/diff → approve → canonical。
-- 每次工具操作后返回可观察状态、结构化结果和来源，使 Agent 能闭环验证而非开环连续修改。
-- 保留人类可检查的事实界面；索引、分数和模型内部状态不应成为隐藏的唯一真相源。
-- 工具保持最小、确定和符合 Agent 感知限制，同时避免一个会静默完成全部工作的高抽象接口。
-- 稳定、模型无关的工具协议可以继承未来模型能力提升；经审核的文本示范更适合作为 workflow/skill，而不是事实知识。
+- 六项任务全部在 robosuite 模拟器中运行，每个 agent-model-prompt-task 配置评估 10 个随机种子。
+- 最小提示下，四种 agent-model 配置的总体成功率为 60% 至 88%。
+- CC-Fable 在三个 LIBERO-Goal 任务通过 29/30，并在七块积木 Rainbow 任务达到 100%。
+- T-block 对约 8 mm 的放置精度要求较高，各配置成功率仅为 10% 至 40%。
+- 为较弱的 CC-Opus 提供文本 waypoint 示例后，其三个 LIBERO-Goal 任务平均成功率从 77% 提高到 100%；Codex-5.5 没有从同类详细提示中获益。
 
-## 审阅边界
+## 适用边界
 
-上述 Global Memory 映射是我们的架构类比，不是论文直接验证的记忆系统结论。批准本 proposal 只表示接受这一有范围限定的材料归纳，不表示接受“通用 Agent 已可取代机器人策略”或“自动记忆会自然带来持续学习”。
+- 论文没有报告真实机器人实验，真实机器人部署被列为未来工作。
+- 推理速度限制 VIA 处理准静态任务，不适用于接球等动态任务。
+- 主实验关闭跨 episode memory read/write，因此论文不构成长期记忆或持续学习的验证。
+- Rainbow 的成功由人工视觉判断，其余任务使用二元成功检测器。
+- 这些结果不能外推为通用 Agent 已经可以取代真实机器人控制策略。
```
