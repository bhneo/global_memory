---
id: "concept_3d739e54fe54c8a5205d2301"
type: "concept"
status: "proposal"
title: "多坐标系同步动作去噪"
created_at: "2026-07-20T12:33:09+08:00"
updated_at: "2026-07-20T13:35:03+08:00"
aliases: ["Synchronized multi-frame action denoising", "Mixture of Frames Policy", "MoF", "多 Frame 扩散策略"]
tags: []
domains: ["embodied-ai", "diffusion-policy", "coordinate-frames", "bimanual-manipulation"]
confidence: "high"
source_ids: ["source_4df1017326dd7cc4786f4218"]
relations: [{"type": "derived_from", "target_id": "source_4df1017326dd7cc4786f4218", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "二者都处理动作参考系差异；前者在单一本体内融合多 frame，后者在多本体间寻求统一动作接口。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-b-20260720", "status": "working"}, {"type": "related_to", "target_id": "concept_21a37fbe65868f6e97a68a20", "reason": "Pointmap 在观察侧统一 robot-frame 几何，MoF 在动作侧同步多个 frame 专家；共同机制是显式坐标变换，差异是输入归一化与输出分布建模。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "proposal"}]
change_reason: "compile bundle from source_4df1017326dd7cc4786f4218"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_7b23a8a7adc7b353d26fbc30", "reflection_a4abd223b36c137fb9bd6ae4"], "importance": "weekly", "changed_belief": "此前倾向把多视角泛化问题交给更大视觉模型；该材料提示，显式消除 observation-action frame mismatch 可以减少不必要的函数复杂度，并保留既有视觉 token 接口。\n此前把坐标系视为预处理约定；该工作把它提升为可学习的 mixture axis，表明动作模型难度有一部分是参数化造成的，而非任务本身不可约复杂度。", "surprising": "在相同 depth、intrinsics 和 extrinsics 信息下，预计算 robot-frame pointmap 仍优于把这些信息直接交给策略学习转换，隔离出显式几何变换本身的收益。\nMoF 在部分任务上超过按整项任务选择最佳单 frame 的 oracle；路由权重随阶段变化较大的任务收益更高，论文报告两者具有正相关。", "connections": [{"shared_mechanism": "与 VLA 注意力泛化—动作泛化缺口都区分看见操作区域与把它稳定映射为机器人动作。", "boundary": "pointmap 需要训练和测试时的相机内外参及深度；当前相机变化主要覆盖 placement/extrinsics，未覆盖摄像头数量与视场变化。", "difference": "注意力—动作缺口描述表征与执行之间的一般问题；pointmap 通过把视觉几何预先表达在动作坐标系中解决其中的 frame mismatch。"}, {"shared_mechanism": "与跨本体通用 VLA 都需要把不同运动学参考系映射到统一的可执行动作接口。", "boundary": "MoF 依赖预先给定的候选 frame 和准确的 proprioceptive frame transform，当前证据集中于双臂移动操作，不能直接推出未知本体上的 frame 自动发现。", "difference": "跨本体通用 VLA 追求不同机器人共享输入输出协议；MoF 在单个机器人内部同时维护多个坐标系专家，并在同一扩散轨迹上融合噪声预测。"}], "open_questions": ["当标定随时间漂移时，pointmap 应作为确定输入还是带不确定性的几何分布进入策略？", "能否从数据中发现任务相关 frame，并把 frame transform 不确定性传播进扩散去噪与执行风险？"]}
proposed_status: "working"
---

# 多坐标系同步动作去噪

在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。
