---
id: "claim_wechat_diffusion_rl_baseline_limits_20260716"
title: "该文称 PPO/AWR 等原生高斯策略 RL 难以适配扩散/流匹配 VLA，离线长时序场景中弱于 SFT；两套方案（离线优势 BC vs EXPO-FT）不可混用"
tags: ["baseline-comparison", "diffusion-policy", "VLA"]
domains: ["reinforcement-learning", "robotics"]
confidence: "medium"
applicability: ["vs HIL-SERL/DSRL/HG-DAgger/SFT", "离线/在线框架区分"]
uncertainty: "基线弱势归因为主讲观点；跨任务泛化与算力成本限制文内已承认。"
evidence: [{"evidence_id": "ev_3476", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 3476, "span_end": 3561, "original_text": "PPO属于在线策略（on-policy）算法，AWR原生适配高斯策略，二者底层架构均无法适配扩散/流匹配类VLA策略，这也是对比实验中AWR、PPO性能无法超越纯监督微调", "section": "PPO/AWR 局限", "stance": "supports", "verification_status": "verified", "reason": "文内对 PPO/AWR 不适配扩散 VLA 的说明。"}, {"evidence_id": "ev_1322", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 1322, "span_end": 1331, "original_text": "完全区分，不可混用", "section": "两套方案边界", "stance": "supports", "verification_status": "verified", "reason": "文内强调离线框架与 EXPO-FT 相互独立。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:05:00+08:00"
updated_at: "2026-07-16T11:05:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 EXPO-FT / 离线 VLA RL 研讨会；等待人工核验"
source_ids: ["source_8b41a014bee47c4239a2fa81"]
relations: [{"type": "derived_from", "target_id": "source_8b41a014bee47c4239a2fa81", "reason": "human five 转载 Chelsea Finn & Perry Dong 研讨会：离线迭代 RL 与 EXPO-FT 在线 VLA 微调；原论文未 capture"}]
---

# 基线与边界

扩散 RL 三类离线微调均有上限；EXPO-FT 需人工重置环境。
