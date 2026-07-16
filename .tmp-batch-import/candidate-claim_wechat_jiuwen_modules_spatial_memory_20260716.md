---
id: "claim_wechat_jiuwen_modules_spatial_memory_20260716"
title: "该文列举 Symbiosis 模块：多模态感知产出结构化世界状态；安全规划校检物理可行性；空间记忆以 3D Scene Graph 维护物体关系"
tags: ["safe-planning", "spatial-memory", "skill-tool"]
domains: ["robotics", "agent-systems"]
confidence: "low"
applicability: ["Skill/Action Tool 原子能力", "Feedback 闭环修正"]
uncertainty: "模块能力为设计声明；零样本跨本体等效益未附量化证据。"
evidence: [{"evidence_id": "ev_2335", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 2335, "span_end": 2520, "original_text": "安全规划，状态感知，观测反馈，空间记忆等关键技术模块。\n\n多模态感知（Multimodal Perception）\n\n使physical AI Agent主动感知世界，是Agent由数字走向物理的基础。\n\n同时，把理解从决策中分离，在进行Action之前对场景进行充分理解，产出结构化世界状态，例如被检测对象、对象位姿、置信度等。\n\n安全规划（Safe Planning", "section": "安全规划模块", "stance": "supports", "verification_status": "verified", "reason": "文内对 Safe Planning 模块标题。"}, {"evidence_id": "ev_2350", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 2350, "span_end": 2971, "original_text": "空间记忆等关键技术模块。\n\n多模态感知（Multimodal Perception）\n\n使physical AI Agent主动感知世界，是Agent由数字走向物理的基础。\n\n同时，把理解从决策中分离，在进行Action之前对场景进行充分理解，产出结构化世界状态，例如被检测对象、对象位姿、置信度等。\n\n安全规划（Safe Planning）\n\n基于Prompt任务指令与结构化世界状态，进行任务规划，对相关Skill中的参数动态赋值，并进行物理可行性、安全性与约束校检，拒绝不可执行方案。\n\n物理执行（Physical Action）\n\n按照Skill的建议，调用相关Action Tool原子能力，最终完成位移、抓取、放置、交互等一系列连续可控的物理运动。\n\n状态观察（Observation）\n\n负责对物理动作执行后的真实世界状态进行采集与结构化提取。\n\n通过视觉等传感器获取执行结果，识别物体位姿、环境变化、交互效果等关键信息，输出结构化的世界观测状态，为后续Feedback偏差计算提供客观依据。\n\n观测反馈（Feedback）\n\n基于观测结果构建闭环修正机制，将执行偏差、异常状态、成功/失败判据回传至推理与规划模块。\n\n实现动作参数实时调整、规划序列动态优化、异常场景自主恢复，同时沉淀交互数据用于技能迭代，形成“感知-规划-执行-观测-反馈”的完整闭环，持续提升态势感知规划的鲁棒性。\n\n空间记忆（Spatial Memory", "section": "空间记忆模块", "stance": "supports", "verification_status": "verified", "reason": "文内对 Spatial Memory 模块标题。"}, {"evidence_id": "ev_2995", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 2995, "span_end": 3021, "original_text": "3D Scene Graph），构建物体级的空间关系", "section": "场景图", "stance": "supports", "verification_status": "verified", "reason": "文内对 3D Scene Graph 物体级空间关系说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:10:00+08:00"
updated_at: "2026-07-16T11:10:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 Jiuwen Symbiosis 宣传文；等待人工核验"
source_ids: ["source_6ada1b3b0033883b83a3bf40"]
relations: [{"type": "derived_from", "target_id": "source_6ada1b3b0033883b83a3bf40", "reason": "量子位授权转载 openJiuwen Jiuwen Symbiosis 开源宣传；属 vendor/社区软文"}]
---

# 功能模块

Action 前场景理解结构化；观测反馈支撑参数调整与异常恢复。
