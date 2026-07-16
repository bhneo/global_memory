---
id: "proposal_1d44e0e2946b9ac0720b2746"
type: "proposal"
status: "superseded"
title: "模型提议：该文介绍 G0.5 用 RVQ ActionCodec 与 27 维虚拟骨架（左/右臂、夹爪、底盘）统一跨本体动作 token，并按需只为激活部件生成 token"
created_at: "2026-07-16T11:07:21+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_e6608d8f849ad472bbd95143"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_g05_actioncodec_rvq_skeleton_20260716"
target_path: "vault/knowledge/claims/claim_wechat_g05_actioncodec_rvq_skeleton_20260716-该文介绍-g0-5-用-rvq-actioncodec-与-27-维虚拟骨架-左-右臂-夹爪-底盘-统一跨本体动作-token-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1d44e0e2946b9ac0720b2746.md"
candidate_sha256: "895b484b5265007dfd79767f7d1ae4f9d78c38a682690df66cb5fde18fa198ae"
change_reason: "导入 claim_wechat_g05_actioncodec_rvq_skeleton_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_e6608d8f849ad472bbd95143", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "uncertainty": "自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文介绍 G0.5 用 RVQ ActionCodec 与 27 维虚拟骨架（左/右臂、夹爪、底盘）统一跨本体动作 token，并按需只为激活部件生成 token

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_e6608d8f849ad472bbd95143`
- Input SHA-256：`4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228`
- 不确定性：自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。
- 提议理由：导入 claim_wechat_g05_actioncodec_rvq_skeleton_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_g05_actioncodec_rvq_skeleton_20260716-该文介绍-g0-5-用-rvq-actioncodec-与-27-维虚拟骨架-左-右臂-夹爪-底盘-统一跨本体动作-token-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_g05_actioncodec_rvq_skeleton_20260716"
+title: "该文介绍 G0.5 用 RVQ ActionCodec 与 27 维虚拟骨架（左/右臂、夹爪、底盘）统一跨本体动作 token，并按需只为激活部件生成 token"
+tags: ["ActionCodec", "RVQ", "cross-embodiment"]
+domains: ["robotics", "machine-learning"]
+confidence: "medium"
+applicability: ["三代动作分词器对比", "TCL 时域对比学习"]
+uncertainty: "技术细节来自 G0.5 报告二手转述；benchmark 需回 Galaxea 原文。"
+evidence: [{"evidence_id": "ev_2346", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 2346, "span_end": 2380, "original_text": "残差向量量化（RVQ）的交叉本体动作编解码器（ActionCodec", "section": "RVQ 编解码", "stance": "supports", "verification_status": "verified", "reason": "文内对 G0.5 分词器核心设计。"}, {"evidence_id": "ev_2634", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 2634, "span_end": 2986, "original_text": "27 维。它把所有动作强制解耦为 5 个标准的“乐高模块”：\n\n左臂控制（9维）+ 左夹爪（1维）\n\n右臂控制（9维）+ 右夹爪（1维）\n\n下半身/移动底盘（7维）\n\n一个冻结的单一编解码器消费这套布局，这意味着机器人的对称等物理结构在构造上就被保留了下来。例如，<left_control> 这个 Token 在任何机器人上都只代表左臂，未来哪怕新增一台完全不同形态的本体，也无需在分词器或动作头里增加任何新参数。\n\n在这种结构化的词表之上，G0.5 进一步实现了极致的序列压缩与算力拯救。每个部件会按残差轮次展开成动作码（总长度 = R 个残差轮次 × 当下激活的部件组 × 每组 8 个量化码）。\n\n如果当前任务只需要动左臂，模型就绝不会为闲置的右臂和底盘生成任何无用的 Token。这种“按需生成", "section": "虚拟骨架", "stance": "supports", "verification_status": "verified", "reason": "文内对跨本体布局与按需 token 的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:08:00+08:00"
+updated_at: "2026-07-16T11:08:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 G0.5 vs PI flow matching 解读；等待人工核验"
+source_ids: ["source_e6608d8f849ad472bbd95143"]
+relations: [{"type": "derived_from", "target_id": "source_e6608d8f849ad472bbd95143", "reason": "具身纪元 Marilyn Liu 解读 Galaxea G0.5 技术报告 vs PI flow matching；非官方 primary source"}]
+---
+
+# ActionCodec
+
+5 个乐高模块；冻结单一编解码器消费统一布局。
```
