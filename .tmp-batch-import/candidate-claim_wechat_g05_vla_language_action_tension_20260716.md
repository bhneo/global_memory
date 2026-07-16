---
id: "claim_wechat_g05_vla_language_action_tension_20260716"
title: "该文称 VLA 需同时处理离散语言 token 与连续实时控制；PI π0 以 VLM 理解 + 独立流匹配动作专家为行业主流之一"
tags: ["VLA", "flow-matching", "architecture"]
domains: ["robotics", "machine-learning"]
confidence: "medium"
applicability: ["自回归 vs 流匹配路线之争", "RT-2/OpenVLA/π0-FAST 离散化动作"]
uncertainty: "为自媒体架构综述；「定调」等表述含作者判断。"
evidence: [{"evidence_id": "ev_28", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 28, "span_end": 57, "original_text": "语言是离散的下一个 token 预测，动作是连续的实时控制", "section": "语言-动作矛盾", "stance": "supports", "verification_status": "verified", "reason": "文内对 VLA 双信号冲突的定义。"}, {"evidence_id": "ev_151", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 151, "span_end": 160, "original_text": "流匹配专家管出动作", "section": "PI 双模块", "stance": "supports", "verification_status": "verified", "reason": "文内对 π0 架构分工的叙述。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:08:00+08:00"
updated_at: "2026-07-16T11:08:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 G0.5 vs PI flow matching 解读；等待人工核验"
source_ids: ["source_e6608d8f849ad472bbd95143"]
relations: [{"type": "derived_from", "target_id": "source_e6608d8f849ad472bbd95143", "reason": "具身纪元 Marilyn Liu 解读 Galaxea G0.5 技术报告 vs PI flow matching；非官方 primary source"}]
---

# 架构分歧

G0.5 主张统一权重自回归；质疑 flow matching 为唯一解。
