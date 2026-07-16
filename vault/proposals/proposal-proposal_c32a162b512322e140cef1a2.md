---
id: "proposal_c32a162b512322e140cef1a2"
type: "proposal"
status: "pending"
title: "模型提议：该文称 Qwen-RobotNav 在宇树 Go2 上单相机零样本部署（Jetson Thor 推理 196ms），训练含 1560 万条样本；NAVSIM 闭环 PDMS 91.4"
created_at: "2026-07-16T11:19:48+08:00"
updated_at: "2026-07-16T11:19:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_11bc6c51fa038191e33bc9a7"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_qwen_robotnav_go2_deployment_20260716"
target_path: "vault/knowledge/claims/claim_wechat_qwen_robotnav_go2_deployment_20260716-该文称-qwen-robotnav-在宇树-go2-上单相机零样本部署-jetson-thor-推理-196ms-训练含-156.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_c32a162b512322e140cef1a2.md"
candidate_sha256: "fe5ca2b3d163530bd69e360f50ece079091197c667358266d8a73885472bb072"
change_reason: "导入 claim_wechat_qwen_robotnav_go2_deployment_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_11bc6c51fa038191e33bc9a7", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "uncertainty": "机器人前瞻 vendor 通稿；SOTA/benchmark 数字 confidence 低，需回阿里官方材料核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 Qwen-RobotNav 在宇树 Go2 上单相机零样本部署（Jetson Thor 推理 196ms），训练含 1560 万条样本；NAVSIM 闭环 PDMS 91.4

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_11bc6c51fa038191e33bc9a7`
- Input SHA-256：`ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6`
- 不确定性：机器人前瞻 vendor 通稿；SOTA/benchmark 数字 confidence 低，需回阿里官方材料核验。
- 提议理由：导入 claim_wechat_qwen_robotnav_go2_deployment_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_qwen_robotnav_go2_deployment_20260716-该文称-qwen-robotnav-在宇树-go2-上单相机零样本部署-jetson-thor-推理-196ms-训练含-156.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_qwen_robotnav_go2_deployment_20260716"
+title: "该文称 Qwen-RobotNav 在宇树 Go2 上单相机零样本部署（Jetson Thor 推理 196ms），训练含 1560 万条样本；NAVSIM 闭环 PDMS 91.4"
+tags: ["VLN", "Unitree-Go2", "zero-shot"]
+domains: ["robotics", "navigation"]
+confidence: "low"
+applicability: ["参数化视觉分配策略", "EXPRESS-Bench +15.4% 叙述"]
+uncertainty: "SOTA/PDMS 数字为媒体转述；未见独立第三方复现。"
+evidence: [{"evidence_id": "ev_468", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 468, "span_end": 492, "original_text": "196ms）上零样本部署，仅使用单个低分辨率相机", "section": "Go2 部署", "stance": "supports", "verification_status": "verified", "reason": "文内对 Go2 零样本部署硬件与传感器配置。"}, {"evidence_id": "ev_1115", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 1115, "span_end": 1339, "original_text": "1560万条数据训练未见过展馆也能精准导航\n\n智能体要操作物体需要先到达目标位置，但不同导航任务对历史信息的需求差异大，指令跟随需要保留长程上下文，目标追踪则几乎只关注最近几帧，任何固定的视觉分配策略都无法同时满足这两类需求。\n\n基于此，Qwen-RobotNav将视觉分配策略本身参数化，根据任务模式选择导航行为、通过可调节参数决定视觉历史的编码方式。该模型的训练样本包含1560万条，同时联合视觉语言数据以保留感知能力，一套权重统一五类导航任务", "section": "训练规模", "stance": "supports", "verification_status": "verified", "reason": "文内对 RobotNav 训练样本量与统一任务说明。"}]
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
+# RobotNav
+
+可控观测协议四控制轴；腿式导航与自动驾驶共享权重叙述。
```
