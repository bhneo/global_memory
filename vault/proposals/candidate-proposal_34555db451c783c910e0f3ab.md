---
id: "claim_wechat_embodied_data_four_layers_20260716"
title: "该文将具身数据基础设施分为可视化、目录检索、标注供给与评测训练闭环四层，称最内层闭环最难外包"
tags: ["data-platform", "evaluation", "foxglove"]
domains: ["robotics", "data-engineering"]
confidence: "low"
applicability: ["Foxglove/Rerun/Scale 产品层定位讨论", "头部公司自建系统原因分析"]
uncertainty: "四层框架为作者构造；与 Joe Harris 观点的延伸，非行业标准 taxonomy。"
evidence: [{"evidence_id": "ev_261", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 261, "span_end": 2545, "original_text": "Foxglove 拿了 4000 万美元 B 轮，Rerun 拿了 1700 万美元 seed，Scale AI 也专门开了 embodied AI 产品线。钱砸下去了，人也不算少，行业却还是在喊缺数据。一个看上去这么显而易见的工程问题，在资本和人才都不缺的前提下做了几年还是没解，比较合理的怀疑只能是：问题本身就搞错了。\n\n今天我们聊聊数据问题，大家都在说缺数据，但是真的只是缺数据吗？能不能再精准一点呢？\n\n这有点像你拍了几万小时的飞行录像，然后困惑为什么看了这么多录像还是造不出飞机。也许问题从一开始就不在录像不够多。\n\n二、第一层：「我们缺数据」\n\n行业最表层的叙事一直都很稳定。每次 robotics 的进展不及预期，第一反应几乎都是数据不够。基础模型团队花大钱搞仿真和遥操作采集，部署中的机器人每天产生 IMU、相机、激光雷达、关节状态日志，全躺在存储桶里发霉。表面上看，这当然像是一个典型的供需错配。\n\n先说在前面：熟悉我的朋友都知道，我不是 scaling law 的信徒。我不认为它能在任何场景下都无条件生效。但我也承认，数据量和模型规模的增长确实在很多领域兑现了真实效果，这一点没什么好否认的。所以更值得追问的是：robotics 里的 scaling，到底在沿着哪个变量扩展，又在哪里开始失灵。这才是我们需要关心的问题。\n\n如果带着这个问题去看那些真正推着机器人基础模型往前的结果，答案其实已经开始浮现：驱动进步的，并不像「只是缺数据」那么简单。\n\nRT-2 是一个很好的例子。它的动作数据只来自 13 台机器人、17 个月、一间 office kitchen，听起来并不算多。真正让它上了一个台阶的，恰恰是接入了互联网规模的视觉语言预训练，跟机器人动作数据的增量关系不大。\n\nDeepMind 官方博客写得很清楚：RT-2 用的是 web 预训练的视觉语言模型，再结合 RT-1 的机器人示范数据。换句话说，RT-2 的成功更像是「互联网语义先验加有限机器人动作数据」的联合产物，很难被简单归结为「只要继续多收机器人数据，能力就会持续上升」的案例。\n\nOpen X-Embodiment 把这件事又往前推了一步。22 种机器人、500 多种技能、超过 100 万个 episode 被汇到一起训练，结果当然是好的：RT-1-X 比各家原始模型平均高了 50%，RT-2-X 在全新技能上的成功率是 RT-2 的三倍。\n\n但你仔细看它给出的证据，依然会发现关键不在于「总量继续变大」本身，而在于跨 embodiment、跨任务、跨环境的数据多样性终于开始产生迁移效应。这里出现的不是 LLM 那种 token 翻倍、loss 平滑下降的 scaling，更像是训练分布跨过某个门槛之后，模型突然拿到了一种以前没有的泛化能力。\n\nRe-Mix 则进一步印证了这个直觉。斯坦福的 Dorsa Sadigh 团队在 2024 年的 Re-Mix 论文里用 Open X-Embodiment 检验数据混合策略，最后发现学出来的 domain weight 比均匀混合高 38%，比人工挑的权重还高 32%。\n\n如果问题真的只是「数据还不够多」，这种差异不应该这么大。它之所以这么大，正好印证了一件事：决定结果的，更多是这些数据以什么比例进入模型、落在什么训练结构里、最终让模型学到了什么。\n\n如果借用我之前写 Epiplexity 时用过的视角，这里的关键其实在于「数据里到底有多少结构，能被当前这个学习系统提取、重用、迁移」。同样是一堆日志，随机噪声再多，也未必比一个组织良好的失败案例更有价值；\n\n同样是一段轨迹，能不能被模型吸收，不只取决于它是不是真实世界采来的，还取决于它有没有把任务结构、环境差异和动作约束以一种可学习的方式呈现出来。这样回头看，所谓数据的语义结构，说到底就是数据里那些对当前学习者来说真正可学的部分。\n\n仿真更像一个反向证据。因为不少人每次听到「缺数据」，第一个条件反射几乎都是：那就用 Isaac Sim 无限生成。Figure 确实在用仿真训人形步态，NVIDIA 也在用 Isaac Sim 和 Cosmos 做稀有场景和数据增强，但所有顶级团队最后回到的表述都是 real-to-real workflow：先有真实数据，再由世界模型去扩展。如果堆量这件事本身就够，无限仿真早该把通用机器人往前推一大截了。但很显然，它没有。\n\n所以回头看，迄今为止最成功的几个机器人基础模型，关键变量都落在**「这些数据到底是什么结构」上，远比「有多少数据」重要得多**。\n\n「缺数据」这三个字，把一个结构性问题简化成了一个数量问题。\n\n三、第二层：「数据够了，只是不可用」\n\nJoe Harris 给出的修正比第一层聪明。格式不统一、没标注、不可检索、schema 不兼容，所以没人能用。这听起来像个 data engineering 问题，理论上应该能解。\n\n也确实有人在解。但只要把这个领域稍微拆开看一下，你就会发现 Joe Harris 其实也只看到了最外面的几层。\n\n最外层是观测和调试。Foxglove、Rerun 做的事，就是让工程师能看见机器人到底在干嘛。Foxglove 给 Slip Robotics 做的案例很典型：过去工程师要从 AWS 下载 ROS bag、写脚本抽数据、手动拼日志，拿到正确数据十分钟起步，跨工具 debug 动辄几小时。\n\n接了 Foxglove 之后，原来几小时的事情，几分钟就能做完", "section": "可视化层", "stance": "supports", "verification_status": "verified", "reason": "文内对最外层观测/调试层的说明。"}, {"evidence_id": "ev_3093", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 3093, "span_end": 3234, "original_text": "评测与训练闭环。定义什么算失败，怎么把长尾 case 筛出来重放，怎么拿历史 intervention 做 counterfactual evaluation，怎么根据评测结果调整下一轮训练配方。这一层一旦缺了，前面三层做得再漂亮，也只是把数据从「看不见」变成了「看得见但改不动模型", "section": "最内层瓶颈", "stance": "supports", "verification_status": "verified", "reason": "文内对第四层为核心卡点的判断。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T01:19:00+08:00"
updated_at: "2026-07-16T01:19:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入具身数据问题分析文；等待人工核验"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析"}]
---

# 四层基础设施

可见→可找→可标注→评测闭环；内层最难外包。
