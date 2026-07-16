---
id: "claim_wechat_qwen_robotnav_go2_deployment_20260716"
title: "该文称 Qwen-RobotNav 在宇树 Go2 上单相机零样本部署（Jetson Thor 推理 196ms），训练含 1560 万条样本；NAVSIM 闭环 PDMS 91.4"
tags: ["VLN", "Unitree-Go2", "zero-shot"]
domains: ["robotics", "navigation"]
confidence: "low"
applicability: ["参数化视觉分配策略", "EXPRESS-Bench +15.4% 叙述"]
uncertainty: "SOTA/PDMS 数字为媒体转述；未见独立第三方复现。"
evidence: [{"evidence_id": "ev_468", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 468, "span_end": 492, "original_text": "196ms）上零样本部署，仅使用单个低分辨率相机", "section": "Go2 部署", "stance": "supports", "verification_status": "verified", "reason": "文内对 Go2 零样本部署硬件与传感器配置。"}, {"evidence_id": "ev_1115", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 1115, "span_end": 1339, "original_text": "1560万条数据训练未见过展馆也能精准导航\n\n智能体要操作物体需要先到达目标位置，但不同导航任务对历史信息的需求差异大，指令跟随需要保留长程上下文，目标追踪则几乎只关注最近几帧，任何固定的视觉分配策略都无法同时满足这两类需求。\n\n基于此，Qwen-RobotNav将视觉分配策略本身参数化，根据任务模式选择导航行为、通过可调节参数决定视觉历史的编码方式。该模型的训练样本包含1560万条，同时联合视觉语言数据以保留感知能力，一套权重统一五类导航任务", "section": "训练规模", "stance": "supports", "verification_status": "verified", "reason": "文内对 RobotNav 训练样本量与统一任务说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:20:00+08:00"
updated_at: "2026-07-16T11:20:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 Qwen-Robot 发布稿；等待人工核验"
source_ids: ["source_11bc6c51fa038191e33bc9a7"]
relations: [{"type": "derived_from", "target_id": "source_11bc6c51fa038191e33bc9a7", "reason": "机器人前瞻报道阿里 Qwen-Robot 系列发布（2026-06-16）；属 vendor/媒体软文"}]
---

# RobotNav

可控观测协议四控制轴；腿式导航与自动驾驶共享权重叙述。
