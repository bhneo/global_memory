---
id: "claim_wechat_jiuwen_edge_cloud_ascend_20260716"
title: "该文称 Symbiosis 采用端云协同：云侧 LLM/VLM 负责复杂规划，端侧实时感知执行；并宣称与昇腾 NPU、鲲鹏 CPU 异构分工以降功耗"
tags: ["edge-cloud", "Ascend", "open-source"]
domains: ["robotics", "systems"]
confidence: "low"
applicability: ["gitcode.com/openJiuwen/jiuwensymbiosis 开源", "华为云 AgentArts 商业化"]
uncertainty: "典型 vendor 生态宣传；TOPS/功耗/吞吐提升缺乏第三方验证。"
evidence: [{"evidence_id": "ev_4052", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 4052, "span_end": 4084, "original_text": "端云协同架构：其中，大规模推理和复杂规划运行在云侧LLM/VLM", "section": "端云架构", "stance": "supports", "verification_status": "verified", "reason": "文内对端云分工的描述。"}, {"evidence_id": "ev_3884", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 3884, "span_end": 4177, "original_text": "昇腾版及其他生态兼容模型，完成下游任务联动。\n\nJiuwen Symbiosis与昇腾、鲲鹏\n\n很多physical AI系统仍然沿用“大模型+GPU”的思路。\n\n但在真实机器人场景中，问题往往不是单纯的模型推理，而是如何让感知、认知、规划和执行在有限功耗和有限带宽下形成稳定闭环。\n\nJiuwen Symbiosis从设计之初就采用了端云协同架构：其中，大规模推理和复杂规划运行在云侧LLM/VLM，端侧则专注于实时感知与执行。\n\n这种架构与昇腾、鲲鹏的异构计算能力形成了天然匹配：\n\n昇腾提供较高TOPS的AI推理能力，可承担目标检测、视觉理解、多模态感知等高频任务；\n\n鲲鹏CPU", "section": "异构分工", "stance": "supports", "verification_status": "verified", "reason": "文内对昇腾/鲲鹏资源分工的说明。"}]
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

# 端云 + 昇腾

2026-06 开源 Symbiosis；教 How 非 What 的共生叙事。
