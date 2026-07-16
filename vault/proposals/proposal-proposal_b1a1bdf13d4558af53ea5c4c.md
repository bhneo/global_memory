---
id: "proposal_b1a1bdf13d4558af53ea5c4c"
type: "proposal"
status: "superseded"
title: "模型提议：该文列举 Ego 第一人称视频采集优势为低成本可扩展，但缺乏力触觉/精确关节轨迹且需对齐与清洗"
created_at: "2026-07-16T01:11:55+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_ego_collection_limitations_20260716"
target_path: "vault/knowledge/claims/claim_wechat_ego_collection_limitations_20260716-该文列举-ego-第一人称视频采集优势为低成本可扩展-但缺乏力触觉-精确关节轨迹且需对齐与清洗.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b1a1bdf13d4558af53ea5c4c.md"
candidate_sha256: "ea9a253d867b5980c33dd60993708d1eb584eb090d2f16223c6a2a397525bf90"
change_reason: "导入 claim_wechat_ego_collection_limitations_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_cda5a1b9e036598aff53e5be", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "uncertainty": "行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文列举 Ego 第一人称视频采集优势为低成本可扩展，但缺乏力触觉/精确关节轨迹且需对齐与清洗

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_cda5a1b9e036598aff53e5be`
- Input SHA-256：`4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5`
- 不确定性：行业软文/厂商宣传；特斯拉/OpenAI/数据堂数据需回原始来源核验。
- 提议理由：导入 claim_wechat_ego_collection_limitations_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_ego_collection_limitations_20260716-该文列举-ego-第一人称视频采集优势为低成本可扩展-但缺乏力触觉-精确关节轨迹且需对齐与清洗.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_ego_collection_limitations_20260716"
+title: "该文列举 Ego 第一人称视频采集优势为低成本可扩展，但缺乏力触觉/精确关节轨迹且需对齐与清洗"
+tags: ["ego-centric", "data-quality", "limitations"]
+domains: ["robotics", "computer-vision"]
+confidence: "medium"
+applicability: ["Ego 采集方案利弊分析", "EgoScale/DreamDojo 引用语境"]
+uncertainty: "优劣势为科普归纳；英伟达项目能力数字为二手引述。"
+evidence: [{"evidence_id": "ev_1831", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 1831, "span_end": 1845, "original_text": "采集成本极低、规模可无限放大", "section": "Ego 优势", "stance": "supports", "verification_status": "verified", "reason": "文内对 Ego 成本与规模优势的说明。"}, {"evidence_id": "ev_950", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 950, "span_end": 2058, "original_text": "力触觉信息，训练出来的模型可以直接运用到同型号机器人上，无需额外适配。可以直接使用π0算法来训练，不用迁移。\n\n但缺陷同样严重，数据与机器人强绑定，几乎无法跨机型迁移；真机采集场景受限，多样性差；遥操作会限制操作员动作，采集的数据不自然；真机成本高，采集效率低，通常需要两人配合，有效数据时长短。\n\n因此，这种真机遥操的方式很难低成本积累大量的预训练数据。\n\n2. UMI通用夹爪：从通用性、真实性出发，降低采集成本\n\nUMI通用夹爪是斯坦福大学2024年提出的折中方案：人手持标准化的通用夹爪（3D打印+GoPro等运动相机），在真实野外场景中操作，同步记录末端视角、夹爪状态、相对轨迹与运动信息。\n\n这种方式兼顾了成本与复用性，设备成本低、高便携、数据可跨机器人复用，贴近主流夹爪执行逻辑。\n\n但是仍旧存在缺陷，夹爪仍然是一个不自然，对操作员有较多限制的末端执行器，难以完成拧螺丝、分拣细物等精细操作。数据缺少环境、行走决策等信息，难以用在人形机器人训练，多用于机械臂。\n\n3. 动作捕捉：直接无侵入捕获真实人类的动作\n\n动作捕捉则跳出了对机器人本体和UMI夹爪的依赖，通过穿戴式设备捕捉人体和手部关键点轨迹，再映射到机器人系统中。\n\n优势在于采集成本低、可批量开展，无需部署真实机器人，人类的动作更自然。\n\n动捕的方案和设备在虚拟数字人方面已经非常成熟，但具身智能数据采集上，依然会遇到一个问题——设备部署需要单独的环境和空间，无法便携的带到千家万户的真实场景中去，并且对遮挡等敏感。\n\n4. Ego 第一人称视频：可穿戴式的无侵入数据采集方案\n\nEgo（Ego Centric）数据是2025年底从硅谷火到国内的具身智能采集方式，Ego采集是从第一视角采集而不是爬取第三方视角数据来获取更高质量的数据，而且采集成本比从互联网爬取、清洗更低！\n\n记录的数据包括了第一人称视角中双手的操作，环境数据，身体关键点数据。\n\n采集员只需佩戴头环、头戴式相机，使用双手操作即可。由于是可穿戴设备，很容易进入家庭、商业等场景中进行数据采集。\n\n这种方式的优势极为突出：采集成本极低、规模可无限放大。\n\n英伟达的EgoScale和DreamDojo已展示数万小时级的采集能力。\n\n同时，第一视角蕴含了环境信息、人类的决策逻辑、视觉注意力切换，也包括了丰富的手-物交互细节。\n\n当然，它也有自己的劣势：多设备需要时间对齐、空间标定，设备需要长时间稳定运行；原始视频中包含大量无效片段，需清洗才能提取有效数据；不包含任何力触觉信息或精确的关节轨迹；其人体关节仅捕获手和脚，其他关键点需要预测，手部关键点和位置需要使用双目相机预测", "section": "Ego 局限", "stance": "supports", "verification_status": "verified", "reason": "文内对 Ego 缺失力触觉与关键点预测的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:11:00+08:00"
+updated_at: "2026-07-16T01:11:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入具身数据采集软文；等待人工核验"
+source_ids: ["source_cda5a1b9e036598aff53e5be"]
+relations: [{"type": "derived_from", "target_id": "source_cda5a1b9e036598aff53e5be", "reason": "由新智元对数据堂具身数据采集框架的软文归纳；特斯拉/OpenAI 路线为二手引述"}]
+---
+
+# Ego 采集利弊
+
+低成本大规模 vs 无力触觉/需清洗对齐。
```
