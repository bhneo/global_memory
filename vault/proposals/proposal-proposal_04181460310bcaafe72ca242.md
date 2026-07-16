---
id: "proposal_04181460310bcaafe72ca242"
type: "proposal"
status: "superseded"
title: "模型提议：该文称阿里开放 Chat2Robot 浏览器评测平台（当前仅 RobotManip、RoboTwin-Clean 50 任务训练），并提及 Qwen-RobotClaw 长程任务与开放世界卫生间搜索 demo"
created_at: "2026-07-16T11:19:49+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_11bc6c51fa038191e33bc9a7"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_qwen_chat2robot_platform_20260716"
target_path: "vault/knowledge/claims/claim_wechat_qwen_chat2robot_platform_20260716-该文称阿里开放-chat2robot-浏览器评测平台-当前仅-robotmanip-robotwin-clean-50-任务训练.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_04181460310bcaafe72ca242.md"
candidate_sha256: "a9d41862471538a6803ec82d5b4f5c8a0195164246a4d5bebd009e32c503c50b"
change_reason: "导入 claim_wechat_qwen_chat2robot_platform_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_11bc6c51fa038191e33bc9a7", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "uncertainty": "机器人前瞻 vendor 通稿；SOTA/benchmark 数字 confidence 低，需回阿里官方材料核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称阿里开放 Chat2Robot 浏览器评测平台（当前仅 RobotManip、RoboTwin-Clean 50 任务训练），并提及 Qwen-RobotClaw 长程任务与开放世界卫生间搜索 demo

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_11bc6c51fa038191e33bc9a7`
- Input SHA-256：`ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6`
- 不确定性：机器人前瞻 vendor 通稿；SOTA/benchmark 数字 confidence 低，需回阿里官方材料核验。
- 提议理由：导入 claim_wechat_qwen_chat2robot_platform_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_qwen_chat2robot_platform_20260716-该文称阿里开放-chat2robot-浏览器评测平台-当前仅-robotmanip-robotwin-clean-50-任务训练.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_qwen_chat2robot_platform_20260716"
+title: "该文称阿里开放 Chat2Robot 浏览器评测平台（当前仅 RobotManip、RoboTwin-Clean 50 任务训练），并提及 Qwen-RobotClaw 长程任务与开放世界卫生间搜索 demo"
+tags: ["Chat2Robot", "evaluation-platform", "agent-framework"]
+domains: ["robotics", "systems"]
+confidence: "low"
+applicability: ["qwen-robotmanip.d-robotics.cc 体验地址", "长程重规划 demo"]
+uncertainty: "平台能力范围与 demo 为宣传描述；开放世界能力「后续发布细节」。"
+evidence: [{"evidence_id": "ev_882", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 882, "span_end": 995, "original_text": "Chat2Robot，用户可以在浏览器中与机器人对话，即可观察机器人的实时响应。Chat2Robot目前仅支持Qwen-RobotManip，且部署策略仅使用RoboTwin-Clean数据集进行训练，该数据集仅包含50个任务", "section": "评测平台限制", "stance": "supports", "verification_status": "verified", "reason": "文内对 Chat2Robot 当前支持范围。"}, {"evidence_id": "ev_626", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 626, "span_end": 700, "original_text": "Qwen-RobotClaw，让Qwen VLM智能体将Qwen-Robot Suite模型作为物理世界工具调用，同时管理长程任务所需的上下文与记忆", "section": "Claw 框架", "stance": "supports", "verification_status": "verified", "reason": "文内对 RobotClaw 组合物理工具与长程记忆说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:20:00+08:00"
+updated_at: "2026-07-16T11:20:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 Qwen-Robot 发布稿；等待人工核验"
+source_ids: ["source_11bc6c51fa038191e33bc9a7"]
+relations: [{"type": "derived_from", "target_id": "source_11bc6c51fa038191e33bc9a7", "reason": "机器人前瞻报道阿里 Qwen-Robot 系列发布（2026-06-16）；属 vendor/媒体软文"}]
+---
+
+# 平台与 demo
+
+三模型独立可用；语言接口便于 Qwen 组合调度。
```
