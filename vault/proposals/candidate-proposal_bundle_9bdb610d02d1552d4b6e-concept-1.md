---
id: "concept_21a37fbe65868f6e97a68a20"
type: "concept"
status: "proposal"
title: "机器人坐标系稠密 Pointmap 观察接口"
created_at: "2026-07-20T12:33:20+08:00"
updated_at: "2026-07-20T12:34:17+08:00"
aliases: ["Robot-centric pointmap observation", "See Like a Robot", "机器人中心点图", "robot-frame pointmap"]
tags: []
domains: ["embodied-ai", "vla", "3d-geometry", "viewpoint-generalization"]
confidence: "high"
source_ids: ["source_b64b4a539b8c17d0cfe662ba"]
relations: [{"type": "derived_from", "target_id": "source_b64b4a539b8c17d0cfe662ba", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_90d52ab5e62d9847f9529875", "reason": "pointmap 为注意力已定位的视觉区域补充与机器人动作同 frame 的度量几何，缩小感知泛化到动作泛化的接口缺口。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_90d52ab5e62d9847f9529875", "reason": "pointmap 为注意力已定位的视觉区域补充与机器人动作同 frame 的度量几何，缩小感知泛化到动作泛化的接口缺口。", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_b64b4a539b8c17d0cfe662ba"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_7b23a8a7adc7b353d26fbc30"], "importance": "high", "changed_belief": "此前倾向把多视角泛化问题交给更大视觉模型；该材料提示，显式消除 observation-action frame mismatch 可以减少不必要的函数复杂度，并保留既有视觉 token 接口。", "surprising": "在相同 depth、intrinsics 和 extrinsics 信息下，预计算 robot-frame pointmap 仍优于把这些信息直接交给策略学习转换，隔离出显式几何变换本身的收益。", "connections": [{"shared_mechanism": "与 VLA 注意力泛化—动作泛化缺口都区分看见操作区域与把它稳定映射为机器人动作。", "boundary": "pointmap 需要训练和测试时的相机内外参及深度；当前相机变化主要覆盖 placement/extrinsics，未覆盖摄像头数量与视场变化。", "difference": "注意力—动作缺口描述表征与执行之间的一般问题；pointmap 通过把视觉几何预先表达在动作坐标系中解决其中的 frame mismatch。"}], "open_questions": ["当标定随时间漂移时，pointmap 应作为确定输入还是带不确定性的几何分布进入策略？"]}
proposed_status: "working"
---

# 机器人坐标系稠密 Pointmap 观察接口

把 RGB-D 像素对应的三维点预先转换到机器人动作所用坐标系，并保留图像 H×W 网格供预训练 VLA 视觉通路编码。该接口减少相机视角到动作坐标的学习负担，但依赖深度和相机标定质量。
