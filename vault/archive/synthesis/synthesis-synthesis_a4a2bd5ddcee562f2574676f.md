---
id: "synthesis_a4a2bd5ddcee562f2574676f"
type: "synthesis"
status: "archived"
title: "适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界"
created_at: "2026-07-28T16:27:15+08:00"
updated_at: "2026-07-28T23:03:07+08:00"
change_reason: "User-approved retirement of the mixed calendar-week VLA aggregation. Its governed Working updates and provenance remain intact; future Synthesis must be split by registered directions."
aliases: []
tags: ["archived-period-synthesis", "cognitive-synthesis"]
domains: ["embodied-ai", "vla", "robot-rl", "cross-embodiment", "human-in-the-loop", "world-model", "robot-memory", "contact-manipulation"]
confidence: "medium"
source_ids: ["source_233c4bef3a727389ddf81ae2", "source_283911da72edc403d1b823fb", "source_291d6174cf92660287138f47", "source_34d6513b0522739d0b25e303", "source_40700e61702f4b5a5765e11d", "source_6b52a51e2b4a3be43c97c386", "source_7b278ba348f2a8bb94cce1fc", "source_91072aa553af99e6ab97c6cd", "source_9a6e63428ed93e1a99ea4c4d", "source_c79f943c818d06054ca5cf92", "source_e326446389e083c6ba9c94c2"]
relations: []
period: "2026-W31"
input_reflections: ["reflection_052db872e2258b0e016c5ebf", "reflection_0db16c2a58084d442087245e", "reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_617843f93885fb6b0d3c5f52", "reflection_61def8d05e0b6ddfb18b6f75", "reflection_62e14da60b1cc35f28689c29", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_c5765c32f1c3dd7302da4906", "reflection_cd269bee56819aafec2fd5a3", "reflection_e7fd4c90ed4ee681fb6fdb80"]
input_concepts: ["concept_4739daf4ef7eacc9153c535f", "concept_abb38fe58cbeee09ce87a01d", "concept_asymmetric_frozen_vla_harness", "concept_d01c4f0b61292d29f0a7ffe2", "concept_f9a9f1d1818632c0380b7942", "concept_generalist_cross_embodiment_vla", "concept_latent_space_intervention_adaptation", "concept_multitimescale_tactile_world_model", "concept_predictive_vla_deployment", "concept_progressive_vla_demonstration_curriculum", "concept_vla_action_cache_refinement"]
emerging_patterns: ["VLA 适配不必等同于全模型更新。RPent 把改变放在模型外的规划、记忆与恢复外壳，RL Token 把改变放在面向 actor-critic 的紧凑内部读出，FlowDAgger 把改变放在生成策略的输入潜空间；三者共同保留基础策略先验，但可用反馈、可达行为边界与故障面不同。", "复用或优化之前必须先校准中介信号。UR-VC 校正跨轨迹时间代理，Robo-ValueRL 依赖历史条件价值来筛选离线与在线数据，ActionCache 依赖上下文命中和 refinement 不确定性来决定缓存是否可复用；代理、价值或相似度一旦偏置，后续更新会放大而不是修复该偏置。", "控制与学习的时间单位需要显式对齐。PAC-ACT 把生成、优势、价值与 KL 约束对齐到动作块，TouchWorld 把慢速语义、触觉子目标、中频动作块和高频残差拆成分层闭环，ActionCache 则在相似上下文中缩短生成路径；更长块、更高命中率或更快刷新都不能替代异常后的及时纠错。", "跨本体泛化至少同时依赖动作语义、数据课程和部署监督。GR00T N1.7 用相对末端执行器变化建立弱共享动作坐标，结构化示范通过阶段化数据组织塑造学习分布，LingBot-VLA 2.0 用本体覆盖、全身动作空间和未来语义—几何代理共同约束部署；共享骨干或更多数据本身不足以闭合迁移链。"]
knowledge_updates: [{"target_id": "concept_generalist_cross_embodiment_vla", "previous": "以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "proposed": "跨本体通用 VLA 不仅需要统一输入骨干，还需要声明可跨本体共享的动作语义及其失效边界。相对末端执行器变化可为人类手部运动与部分机器人操作提供弱共享坐标，但全身接触、灵巧手内部自由度、动力学与硬件能力仍需本体专属接口；未来语义—几何监督只有与动作覆盖和本体多样性共同设计时，才可能支持真实部署泛化。", "reason": "GR00T N1.7 把相对 EEF 动作表示与人类视频迁移直接连接，LingBot-VLA 2.0 则表明预测代理必须与动作空间和跨本体数据协同；两者共同限制了原概念中过于笼统的统一接口表述。", "change_type": "refine", "supporting_reflections": ["reflection_0db16c2a58084d442087245e", "reflection_e7fd4c90ed4ee681fb6fdb80"], "supporting_sources": ["source_34d6513b0522739d0b25e303", "source_233c4bef3a727389ddf81ae2"]}, {"target_id": "concept_asymmetric_frozen_vla_harness", "previous": "把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。", "proposed": "冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。", "reason": "RPent、RL Token 与 FlowDAgger 都保留基础 VLA 先验，却分别使用系统执行反馈、环境奖励和人类纠正；把它们合并为单一后训练方法会掩盖可达行为、安全成本和归因边界。", "change_type": "refine", "supporting_reflections": ["reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cd269bee56819aafec2fd5a3"], "supporting_sources": ["source_6b52a51e2b4a3be43c97c386", "source_40700e61702f4b5a5765e11d", "source_9a6e63428ed93e1a99ea4c4d"]}, {"target_id": "concept_4739daf4ef7eacc9153c535f", "previous": "可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "proposed": "可靠价值驱动的离线到在线改进需要在价值学习之前增加代理校准门禁。若训练标签来自归一化时间，必须先检验停滞、倒退与非均匀进度，并用跨轨迹状态一致性或其他物理信号校正；历史条件价值随后才能用于质量条件、在线片段筛选和残差门控。跨轨迹视觉相似与价值估计都可能偏置，因此两级置信度必须分别评估，不能由下游策略收益反向证明上游代理正确。", "reason": "UR-VC 暴露了时间进度代理的系统偏差，Robo-ValueRL 展示价值信号在数据选择与在线更新中的放大作用；二者形成先校正标签、再估计价值、最后更新策略的有序链。", "change_type": "refine", "supporting_reflections": ["reflection_052db872e2258b0e016c5ebf", "reflection_617843f93885fb6b0d3c5f52"], "supporting_sources": ["source_e326446389e083c6ba9c94c2", "source_7b278ba348f2a8bb94cce1fc"]}, {"target_id": "concept_multitimescale_tactile_world_model", "previous": "把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。", "proposed": "多时间尺度触觉世界模型需要同时声明各层的决策单位、信息新鲜度和升级条件。慢速语义层提出子任务，预测层形成触觉子目标，中频策略以动作块作为生成与信用分配单位，高频触觉残差处理局部接触偏差；缓存的中间动作只可在任务阶段、机器人状态和 refinement 不确定性共同通过门禁时作为暖启动。块长、缓存命中和残差幅度达到阈值时应触发拒绝复用或高层重规划，而不是继续由快环无限吸收。", "reason": "TouchWorld 提供预测—反应分层，PAC-ACT 明确动作块同时是优化单位，ActionCache 增加可拒绝的生成路径复用；三者共同补全时间尺度接口，但缓存复用不等同于世界预测。", "change_type": "refine", "supporting_reflections": ["reflection_c5765c32f1c3dd7302da4906", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_62e14da60b1cc35f28689c29"], "supporting_sources": ["source_283911da72edc403d1b823fb", "source_c79f943c818d06054ca5cf92", "source_291d6174cf92660287138f47"]}]
new_connections: [{"shared_mechanism": "RPent、RL Token 与 FlowDAgger 都通过限制可更新接口来保留基础 VLA 的既有先验，并把部署反馈转化为局部修正。", "boundary": "该连接只适用于基础策略已覆盖目标行为附近、且外壳状态、奖励或人类纠正至少有一种可用反馈的任务；它不证明冻结策略能覆盖新的本体能力或远离原支持集的行为。", "difference": "RPent 在模型外重编排原语和记忆，RL Token 用环境奖励优化内部紧凑读出，FlowDAgger 用人类干预监督生成噪声策略。"}, {"shared_mechanism": "UR-VC、Robo-ValueRL 与 ActionCache 都在允许后续优化或复用前，用一个中介分数判断状态进展、行为质量或上下文相似性。", "boundary": "时间位置、历史价值与多模态相似度都只是代理；遮挡、接触状态、多解任务和动力学差异会让高分代理对应错误物理状态。", "difference": "UR-VC 校正离线进度标签，Robo-ValueRL 用价值筛选数据和门控残差，ActionCache 用相似度与生成 refinement 决定是否复用计算路径。"}, {"shared_mechanism": "PAC-ACT、TouchWorld 与 ActionCache 都把连续控制拆成有边界的时间单元，并在单元之间安排重新估计或纠正。", "boundary": "该结构适用于动作块、触觉反馈或生成中间状态可被稳定记录的系统；在突发接触、传感延迟或缓存键失配下，较长单元会扩大纠正延迟。", "difference": "PAC-ACT 对齐学习与执行的动作块，TouchWorld 分离预测与高频反应，ActionCache 复用相似上下文中的生成路径以降低推理延迟。"}, {"shared_mechanism": "GR00T N1.7、结构化示范与 LingBot-VLA 2.0 都通过减少异质数据中的监督错位来提高迁移可学性。", "boundary": "相对 EEF 不能覆盖任意动作空间，课程收益可能来自环境标准化而非子技能复用，未来预测代理也不等同于完整动力学或闭环可靠性。", "difference": "GR00T 选择跨本体动作坐标，结构化示范改变训练数据顺序与组合复杂度，LingBot 联合扩展本体/动作覆盖并蒸馏未来语义—几何目标。"}]
unresolved_tensions: ["更小的适配接口降低样本、计算和遗忘风险，却可能丢失修正所需状态或把行为限制在基础策略支持集；何时应升级到更大范围更新仍缺少统一判据。", "代理校准减少错误信用和错误复用，但每增加一层门禁都会引入新的估计器、阈值和拒绝成本；保守拒绝可提高安全性，也可能错过有效适配。", "更长动作块与缓存命中提高吞吐和时间连续性，却延迟接触异常后的纠正；更频繁重规划提高响应性，也会增加时延、噪声敏感性和跨层不一致。", "跨本体共享表示扩大数据复用，形态专属接口又是动力学与安全的必要条件；过度统一会掩盖不可比自由度，过度分离会失去迁移收益。"]
candidate_hypotheses: [{"statement": "在基础 VLA 已覆盖目标行为邻域的任务中，依据反馈类型与支持域距离，在模型外编排、内部 RL 读出和生成潜空间之间路由局部适配，将比单一全模型微调获得更高的单位交互收益，并减少既有技能退化。", "falsifier": "在相同基础模型、训练数据、真机交互和计算预算下，适配路由系统在样本效率、目标任务成功率、原技能保持率、故障恢复和安全干预次数上均不优于单一全模型微调或固定局部接口基线。", "possible_experiment": "在同一组精密操作与长时程组合任务上构造三种反馈：任务级失败、标量奖励和人类动作纠正；比较固定外壳、固定 RL token、固定潜空间、全模型微调和基于支持域/反馈类型的路由器，统一报告新任务收益、旧技能回归、交互量、延迟和失败归因。", "supporting_patterns": ["RPent 把部署改进放在规划、记忆和恢复外壳", "RL Token 用紧凑内部表征承载少量真机强化学习", "FlowDAgger 用人类干预学习生成潜变量而不改基础权重"], "counter_arguments": ["三个来源的任务、反馈预算和基础策略不同，跨论文共同模式可能不能转化为同一可实现路由器。", "当目标行为远离基础策略支持集时，局部接口会同时失败，而更大范围微调或新示范可能是必要条件。", "多接口系统增加状态估计、调度和归因故障，端到端更新在数据充分时可能更简单且性能更高。"], "supporting_reflections": ["reflection_4430cc70fe95425f717c1e71", "reflection_5b4f45d757e5b256cdddfcfa", "reflection_cd269bee56819aafec2fd5a3"], "supporting_sources": ["source_6b52a51e2b4a3be43c97c386", "source_40700e61702f4b5a5765e11d", "source_9a6e63428ed93e1a99ea4c4d"], "epistemic_status": "hypothetical"}, {"statement": "在接触丰富的动作块 VLA 中，先校准进度或价值代理，并用任务阶段、机器人状态与 refinement 不确定性共同控制缓存复用和重规划，将比只增加动作块长度或缓存命中率降低错误信用、陈旧动作复用和峰值接触失败。", "falsifier": "在统一接触任务、策略和延迟预算下，代理校准与联合复用门禁不能降低错误缓存接受率、进度排序误差、峰值接触失败或异常后的纠正延迟，且最终成功率不优于固定块长和单一相似度缓存基线。", "possible_experiment": "在可控停滞、倒退、遮挡和接触扰动的统一基准中，交叉消融原始/校正进度、单帧/历史价值、固定/风险驱动块长、无缓存/相似度缓存/联合不确定性门禁；报告代理校准、缓存 precision-recall、重规划延迟、峰值力和闭环成功。", "supporting_patterns": ["UR-VC 在价值学习前校正非均匀进度标签", "Robo-ValueRL 用历史价值筛选数据和门控在线更新", "ActionCache 把复用变成相似度门与生成 refinement 的联合决策", "PAC-ACT 与 TouchWorld 分别对齐动作块信用和多时间尺度纠错"], "counter_arguments": ["多级校准会增加实时开销，其收益可能只来自更保守的执行而非更准确的中介信号。", "视觉状态相似、价值和 refinement 不确定性可能共享同一表征偏差，组合门禁不保证错误独立。", "不同论文没有在统一硬件、接触任务和控制频率下直接比较，机制组合的稳定性尚无实证。"], "supporting_reflections": ["reflection_052db872e2258b0e016c5ebf", "reflection_617843f93885fb6b0d3c5f52", "reflection_62e14da60b1cc35f28689c29", "reflection_c0693ad0e6abf8397dbdfd87", "reflection_c5765c32f1c3dd7302da4906"], "supporting_sources": ["source_e326446389e083c6ba9c94c2", "source_7b278ba348f2a8bb94cce1fc", "source_291d6174cf92660287138f47", "source_c79f943c818d06054ca5cf92", "source_283911da72edc403d1b823fb"], "epistemic_status": "hypothetical"}]
possible_experiments: ["建立适配接口路由矩阵，在固定反馈与算力预算下比较模型外编排、RL 读出、潜空间干预、全模型微调及其支持域路由组合。", "把进度标签校正、历史价值估计和在线数据筛选拆成三级消融，分别测量校准误差、选择偏差、策略收益与错误自强化。", "在同一触觉任务上联合扫描动作块长度、缓存新鲜度、refinement 不确定性和高层重规划阈值，同时报告吞吐、纠正延迟、峰值力与成功率。", "在相同骨干和数据预算下交叉比较绝对动作、相对 EEF、对象中心动作，以及随机混合/结构化课程与有无未来语义—几何监督，分离跨本体迁移的动作语义、数据组织和预测目标贡献。"]
truth_layer: "cognitive_synthesis"
created_by: "codex-strong-model-m91-weekly-v3"
execution_safe: false
---

# 适配接口、校准门禁与时间尺度：VLA 从预训练先验到可靠部署的分层边界

## Emerging patterns

- VLA 适配不必等同于全模型更新。RPent 把改变放在模型外的规划、记忆与恢复外壳，RL Token 把改变放在面向 actor-critic 的紧凑内部读出，FlowDAgger 把改变放在生成策略的输入潜空间；三者共同保留基础策略先验，但可用反馈、可达行为边界与故障面不同。
- 复用或优化之前必须先校准中介信号。UR-VC 校正跨轨迹时间代理，Robo-ValueRL 依赖历史条件价值来筛选离线与在线数据，ActionCache 依赖上下文命中和 refinement 不确定性来决定缓存是否可复用；代理、价值或相似度一旦偏置，后续更新会放大而不是修复该偏置。
- 控制与学习的时间单位需要显式对齐。PAC-ACT 把生成、优势、价值与 KL 约束对齐到动作块，TouchWorld 把慢速语义、触觉子目标、中频动作块和高频残差拆成分层闭环，ActionCache 则在相似上下文中缩短生成路径；更长块、更高命中率或更快刷新都不能替代异常后的及时纠错。
- 跨本体泛化至少同时依赖动作语义、数据课程和部署监督。GR00T N1.7 用相对末端执行器变化建立弱共享动作坐标，结构化示范通过阶段化数据组织塑造学习分布，LingBot-VLA 2.0 用本体覆盖、全身动作空间和未来语义—几何代理共同约束部署；共享骨干或更多数据本身不足以闭合迁移链。

## Knowledge updates

[
  {
    "target_id": "concept_generalist_cross_embodiment_vla",
    "previous": "以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。",
    "proposed": "跨本体通用 VLA 不仅需要统一输入骨干，还需要声明可跨本体共享的动作语义及其失效边界。相对末端执行器变化可为人类手部运动与部分机器人操作提供弱共享坐标，但全身接触、灵巧手内部自由度、动力学与硬件能力仍需本体专属接口；未来语义—几何监督只有与动作覆盖和本体多样性共同设计时，才可能支持真实部署泛化。",
    "reason": "GR00T N1.7 把相对 EEF 动作表示与人类视频迁移直接连接，LingBot-VLA 2.0 则表明预测代理必须与动作空间和跨本体数据协同；两者共同限制了原概念中过于笼统的统一接口表述。",
    "change_type": "refine",
    "supporting_reflections": [
      "reflection_0db16c2a58084d442087245e",
      "reflection_e7fd4c90ed4ee681fb6fdb80"
    ],
    "supporting_sources": [
      "source_34d6513b0522739d0b25e303",
      "source_233c4bef3a727389ddf81ae2"
    ]
  },
  {
    "target_id": "concept_asymmetric_frozen_vla_harness",
    "previous": "把冻结 VLA 限定为可重试的局部接触操作专家，由高层代理和固定解析原语负责语义重绑定、自由空间运输、姿态调整、失败重置与验证，并用成功轨迹和失败模型学习各原语的适用范围。",
    "proposed": "冻结 VLA 的适配可以分布在三个不能互换的接口：模型外的规划—记忆—恢复外壳、面向奖励学习的紧凑内部读出，以及生成策略输入端的潜变量控制。路由应依据反馈类型与基础策略支持域选择接口：结构化任务失败可由外壳重编排，奖励可识别的精密阶段可由 RL 读出修正，人类可示范且能被生成器反演的偏差可由潜空间干预修正；任何接口都不能创造基础策略支持集之外的能力，也不能自动证明底层 VLA 得到提升。",
    "reason": "RPent、RL Token 与 FlowDAgger 都保留基础 VLA 先验，却分别使用系统执行反馈、环境奖励和人类纠正；把它们合并为单一后训练方法会掩盖可达行为、安全成本和归因边界。",
    "change_type": "refine",
    "supporting_reflections": [
      "reflection_4430cc70fe95425f717c1e71",
      "reflection_5b4f45d757e5b256cdddfcfa",
      "reflection_cd269bee56819aafec2fd5a3"
    ],
    "supporting_sources": [
      "source_6b52a51e2b4a3be43c97c386",
      "source_40700e61702f4b5a5765e11d",
      "source_9a6e63428ed93e1a99ea4c4d"
    ]
  },
  {
    "target_id": "concept_4739daf4ef7eacc9153c535f",
    "previous": "可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。",
    "proposed": "可靠价值驱动的离线到在线改进需要在价值学习之前增加代理校准门禁。若训练标签来自归一化时间，必须先检验停滞、倒退与非均匀进度，并用跨轨迹状态一致性或其他物理信号校正；历史条件价值随后才能用于质量条件、在线片段筛选和残差门控。跨轨迹视觉相似与价值估计都可能偏置，因此两级置信度必须分别评估，不能由下游策略收益反向证明上游代理正确。",
    "reason": "UR-VC 暴露了时间进度代理的系统偏差，Robo-ValueRL 展示价值信号在数据选择与在线更新中的放大作用；二者形成先校正标签、再估计价值、最后更新策略的有序链。",
    "change_type": "refine",
    "supporting_reflections": [
      "reflection_052db872e2258b0e016c5ebf",
      "reflection_617843f93885fb6b0d3c5f52"
    ],
    "supporting_sources": [
      "source_e326446389e083c6ba9c94c2",
      "source_7b278ba348f2a8bb94cce1fc"
    ]
  },
  {
    "target_id": "concept_multitimescale_tactile_world_model",
    "previous": "把慢速语义子任务规划、触觉子目标预测、中频动作块生成和高频触觉残差修正拆成分层闭环，使触觉既表示预期接触目标，也用于快速纠偏。",
    "proposed": "多时间尺度触觉世界模型需要同时声明各层的决策单位、信息新鲜度和升级条件。慢速语义层提出子任务，预测层形成触觉子目标，中频策略以动作块作为生成与信用分配单位，高频触觉残差处理局部接触偏差；缓存的中间动作只可在任务阶段、机器人状态和 refinement 不确定性共同通过门禁时作为暖启动。块长、缓存命中和残差幅度达到阈值时应触发拒绝复用或高层重规划，而不是继续由快环无限吸收。",
    "reason": "TouchWorld 提供预测—反应分层，PAC-ACT 明确动作块同时是优化单位，ActionCache 增加可拒绝的生成路径复用；三者共同补全时间尺度接口，但缓存复用不等同于世界预测。",
    "change_type": "refine",
    "supporting_reflections": [
      "reflection_c5765c32f1c3dd7302da4906",
      "reflection_c0693ad0e6abf8397dbdfd87",
      "reflection_62e14da60b1cc35f28689c29"
    ],
    "supporting_sources": [
      "source_283911da72edc403d1b823fb",
      "source_c79f943c818d06054ca5cf92",
      "source_291d6174cf92660287138f47"
    ]
  }
]

## New connections

[
  {
    "shared_mechanism": "RPent、RL Token 与 FlowDAgger 都通过限制可更新接口来保留基础 VLA 的既有先验，并把部署反馈转化为局部修正。",
    "boundary": "该连接只适用于基础策略已覆盖目标行为附近、且外壳状态、奖励或人类纠正至少有一种可用反馈的任务；它不证明冻结策略能覆盖新的本体能力或远离原支持集的行为。",
    "difference": "RPent 在模型外重编排原语和记忆，RL Token 用环境奖励优化内部紧凑读出，FlowDAgger 用人类干预监督生成噪声策略。"
  },
  {
    "shared_mechanism": "UR-VC、Robo-ValueRL 与 ActionCache 都在允许后续优化或复用前，用一个中介分数判断状态进展、行为质量或上下文相似性。",
    "boundary": "时间位置、历史价值与多模态相似度都只是代理；遮挡、接触状态、多解任务和动力学差异会让高分代理对应错误物理状态。",
    "difference": "UR-VC 校正离线进度标签，Robo-ValueRL 用价值筛选数据和门控残差，ActionCache 用相似度与生成 refinement 决定是否复用计算路径。"
  },
  {
    "shared_mechanism": "PAC-ACT、TouchWorld 与 ActionCache 都把连续控制拆成有边界的时间单元，并在单元之间安排重新估计或纠正。",
    "boundary": "该结构适用于动作块、触觉反馈或生成中间状态可被稳定记录的系统；在突发接触、传感延迟或缓存键失配下，较长单元会扩大纠正延迟。",
    "difference": "PAC-ACT 对齐学习与执行的动作块，TouchWorld 分离预测与高频反应，ActionCache 复用相似上下文中的生成路径以降低推理延迟。"
  },
  {
    "shared_mechanism": "GR00T N1.7、结构化示范与 LingBot-VLA 2.0 都通过减少异质数据中的监督错位来提高迁移可学性。",
    "boundary": "相对 EEF 不能覆盖任意动作空间，课程收益可能来自环境标准化而非子技能复用，未来预测代理也不等同于完整动力学或闭环可靠性。",
    "difference": "GR00T 选择跨本体动作坐标，结构化示范改变训练数据顺序与组合复杂度，LingBot 联合扩展本体/动作覆盖并蒸馏未来语义—几何目标。"
  }
]

## Unresolved tensions

- 更小的适配接口降低样本、计算和遗忘风险，却可能丢失修正所需状态或把行为限制在基础策略支持集；何时应升级到更大范围更新仍缺少统一判据。
- 代理校准减少错误信用和错误复用，但每增加一层门禁都会引入新的估计器、阈值和拒绝成本；保守拒绝可提高安全性，也可能错过有效适配。
- 更长动作块与缓存命中提高吞吐和时间连续性，却延迟接触异常后的纠正；更频繁重规划提高响应性，也会增加时延、噪声敏感性和跨层不一致。
- 跨本体共享表示扩大数据复用，形态专属接口又是动力学与安全的必要条件；过度统一会掩盖不可比自由度，过度分离会失去迁移收益。

## Candidate hypotheses

[
  {
    "statement": "在基础 VLA 已覆盖目标行为邻域的任务中，依据反馈类型与支持域距离，在模型外编排、内部 RL 读出和生成潜空间之间路由局部适配，将比单一全模型微调获得更高的单位交互收益，并减少既有技能退化。",
    "falsifier": "在相同基础模型、训练数据、真机交互和计算预算下，适配路由系统在样本效率、目标任务成功率、原技能保持率、故障恢复和安全干预次数上均不优于单一全模型微调或固定局部接口基线。",
    "possible_experiment": "在同一组精密操作与长时程组合任务上构造三种反馈：任务级失败、标量奖励和人类动作纠正；比较固定外壳、固定 RL token、固定潜空间、全模型微调和基于支持域/反馈类型的路由器，统一报告新任务收益、旧技能回归、交互量、延迟和失败归因。",
    "supporting_patterns": [
      "RPent 把部署改进放在规划、记忆和恢复外壳",
      "RL Token 用紧凑内部表征承载少量真机强化学习",
      "FlowDAgger 用人类干预学习生成潜变量而不改基础权重"
    ],
    "counter_arguments": [
      "三个来源的任务、反馈预算和基础策略不同，跨论文共同模式可能不能转化为同一可实现路由器。",
      "当目标行为远离基础策略支持集时，局部接口会同时失败，而更大范围微调或新示范可能是必要条件。",
      "多接口系统增加状态估计、调度和归因故障，端到端更新在数据充分时可能更简单且性能更高。"
    ],
    "supporting_reflections": [
      "reflection_4430cc70fe95425f717c1e71",
      "reflection_5b4f45d757e5b256cdddfcfa",
      "reflection_cd269bee56819aafec2fd5a3"
    ],
    "supporting_sources": [
      "source_6b52a51e2b4a3be43c97c386",
      "source_40700e61702f4b5a5765e11d",
      "source_9a6e63428ed93e1a99ea4c4d"
    ],
    "epistemic_status": "hypothetical"
  },
  {
    "statement": "在接触丰富的动作块 VLA 中，先校准进度或价值代理，并用任务阶段、机器人状态与 refinement 不确定性共同控制缓存复用和重规划，将比只增加动作块长度或缓存命中率降低错误信用、陈旧动作复用和峰值接触失败。",
    "falsifier": "在统一接触任务、策略和延迟预算下，代理校准与联合复用门禁不能降低错误缓存接受率、进度排序误差、峰值接触失败或异常后的纠正延迟，且最终成功率不优于固定块长和单一相似度缓存基线。",
    "possible_experiment": "在可控停滞、倒退、遮挡和接触扰动的统一基准中，交叉消融原始/校正进度、单帧/历史价值、固定/风险驱动块长、无缓存/相似度缓存/联合不确定性门禁；报告代理校准、缓存 precision-recall、重规划延迟、峰值力和闭环成功。",
    "supporting_patterns": [
      "UR-VC 在价值学习前校正非均匀进度标签",
      "Robo-ValueRL 用历史价值筛选数据和门控在线更新",
      "ActionCache 把复用变成相似度门与生成 refinement 的联合决策",
      "PAC-ACT 与 TouchWorld 分别对齐动作块信用和多时间尺度纠错"
    ],
    "counter_arguments": [
      "多级校准会增加实时开销，其收益可能只来自更保守的执行而非更准确的中介信号。",
      "视觉状态相似、价值和 refinement 不确定性可能共享同一表征偏差，组合门禁不保证错误独立。",
      "不同论文没有在统一硬件、接触任务和控制频率下直接比较，机制组合的稳定性尚无实证。"
    ],
    "supporting_reflections": [
      "reflection_052db872e2258b0e016c5ebf",
      "reflection_617843f93885fb6b0d3c5f52",
      "reflection_62e14da60b1cc35f28689c29",
      "reflection_c0693ad0e6abf8397dbdfd87",
      "reflection_c5765c32f1c3dd7302da4906"
    ],
    "supporting_sources": [
      "source_e326446389e083c6ba9c94c2",
      "source_7b278ba348f2a8bb94cce1fc",
      "source_291d6174cf92660287138f47",
      "source_c79f943c818d06054ca5cf92",
      "source_283911da72edc403d1b823fb"
    ],
    "epistemic_status": "hypothetical"
  }
]

## Possible experiments

- 建立适配接口路由矩阵，在固定反馈与算力预算下比较模型外编排、RL 读出、潜空间干预、全模型微调及其支持域路由组合。
- 把进度标签校正、历史价值估计和在线数据筛选拆成三级消融，分别测量校准误差、选择偏差、策略收益与错误自强化。
- 在同一触觉任务上联合扫描动作块长度、缓存新鲜度、refinement 不确定性和高层重规划阈值，同时报告吞吐、纠正延迟、峰值力与成功率。
- 在相同骨干和数据预算下交叉比较绝对动作、相对 EEF、对象中心动作，以及随机混合/结构化课程与有无未来语义—几何监督，分离跨本体迁移的动作语义、数据组织和预测目标贡献。
