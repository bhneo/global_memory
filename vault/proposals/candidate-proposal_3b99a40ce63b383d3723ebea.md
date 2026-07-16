---
id: "claim_wechat_qwen_robotmanip_unified_80d_20260716"
title: "该文称 Qwen-RobotManip 以 Qwen3.5-4B VL + 流匹配 DiT 动作头，用 80 维统一状态-动作与相机系 EEF 增量位姿，在 >38100 小时开源数据上跨本体训练"
tags: ["Qwen-RobotManip", "cross-embodiment", "flow-matching"]
domains: ["robotics", "VLA"]
confidence: "low"
applicability: ["人类视频→机器人数据合成 24808h", "RoboChallenge Table30 45% SR 叙述"]
uncertainty: "benchmark 对比 π0.5 等为厂商通稿；需回官方技术报告。"
evidence: [{"evidence_id": "ev_2089", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 2089, "span_end": 2137, "original_text": "80维状态-动作表示在单臂、双臂、灵巧手和移动平台等本体间共享，相机坐标系下的末端执行器增量位姿", "section": "统一表示", "stance": "supports", "verification_status": "verified", "reason": "文内对跨本体 80 维状态-动作与 EEF 增量的说明。"}, {"evidence_id": "ev_299", "evidence_kind": "quote", "source_id": "source_11bc6c51fa038191e33bc9a7", "content_id": "content_ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "extraction_id": "extraction_abc5ebaba4c64d5f80e1daa8", "input_sha256": "ee8016cabd1c0eaccb570735f1d909141dfcab8a05da10364adb722f13aa88b6", "span_start": 299, "span_end": 319, "original_text": "38100小时操作数据实现了大规模多机型", "section": "训练数据量", "stance": "supports", "verification_status": "verified", "reason": "文内对 RobotManip 总训练时长叙述。"}]
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

# RobotManip

对齐是规模化前提：UnifiedSpace+UnifiedEEF 才现对数线性 scaling 叙述。
