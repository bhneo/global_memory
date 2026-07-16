---
id: "proposal_b09f4c1e153af33653a51224"
type: "proposal"
status: "superseded"
title: "模型提议：该文称当前深度学习本质是 X→Y 映射，缺乏 System 2 式思考，在新环境下适应有限"
created_at: "2026-07-16T01:31:07+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_68161c78067d7b4add05ba1a"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_wangjun_dl_x_to_y_limit_20260716"
target_path: "vault/knowledge/claims/claim_wechat_wangjun_dl_x_to_y_limit_20260716-该文称当前深度学习本质是-x-y-映射-缺乏-system-2-式思考-在新环境下适应有限.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_b09f4c1e153af33653a51224.md"
candidate_sha256: "2085390dd2683d4a30e810b842ea76b38007ce4b4ac9e306948d74329e039db0"
change_reason: "导入 claim_wechat_wangjun_dl_x_to_y_limit_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_68161c78067d7b4add05ba1a", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "uncertainty": "2023 演讲整理；IIT/意识主张为理论观点，非共识事实。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称当前深度学习本质是 X→Y 映射，缺乏 System 2 式思考，在新环境下适应有限

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_68161c78067d7b4add05ba1a`
- Input SHA-256：`9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45`
- 不确定性：2023 演讲整理；IIT/意识主张为理论观点，非共识事实。
- 提议理由：导入 claim_wechat_wangjun_dl_x_to_y_limit_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_wangjun_dl_x_to_y_limit_20260716-该文称当前深度学习本质是-x-y-映射-缺乏-system-2-式思考-在新环境下适应有限.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_wangjun_dl_x_to_y_limit_20260716"
+title: "该文称当前深度学习本质是 X→Y 映射，缺乏 System 2 式思考，在新环境下适应有限"
+tags: ["deep-learning", "system1-system2", "generalization"]
+domains: ["machine-learning", "cognitive-science"]
+confidence: "low"
+applicability: ["汪军 2023 演讲对神经网络局限的论述", "自动驾驶复杂决策类比"]
+uncertainty: "为演讲者观点；与当前大模型推理能力争论需区分时代背景（2023）。"
+evidence: [{"evidence_id": "ev_1261", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 1261, "span_end": 2282, "original_text": "X 到 Y 的映射，我们可以处理各种各样的问题，比如监督学习和无监督学习、分类问题、生成式模型和强化学习。既然深度学习或者神经网络能够实现从 X 到 Y 的映射，大家对它展开了一些理论研究，比如它的能力边界在哪？之前有理论分析它是一个通用近似理论（universal approximation theorem），即在一定约束的情况下可以映射从任意的 X 到 Y 的拟合。\n\n机器学习中有个「No free lunch」理论，我们在用神经网络或其他功能进行学习时，它对有些任务拟合得非常好。但是在有先验知识的情况下，如果拟合符合当前的先验知识，你必然能找到一类或一个任务无法学习。也就是说，虽然神经网络具有普适性且逼近如何拟合，但它并不适合所有任务。在有些任务上成功必然会在另一些任务上失败。\n\n既然这样，我们如何让智能体拥有一个很好的学习方法？它能够非常适应周围环境，尤其是不断变化的环境。这点对人和机器学习都非常重要。由于机器学习讲究的是泛化性，如果无法泛化到一个以前没有见过的环境，它的学习能力显然也是有限制的。\n\n回过头看，对于复杂的任务，现在的机器学习方法还未能达到解决的地步。比如自动驾驶，你可以将它归结为当前 AI 系统还不能像人一样观察环境、根据当前情况进行判断、做决策和执行。\n\n如下图所示，英国的 Magic Roundabout，它有好几圈的十字路口。这时候作为人去开车的话，要经过非常深入的观察、判断以及决策。如果从生物或者认知学角度来讲，它是通过所谓的 System 2 的方式来执行。在这种情况下，如果你问人（即驾驶者）当时是如何去执行的？他会非常清楚地告诉你看到了哪些车子以及怎样做出的判断等。\n\n人其实是有意识的，可以主观感受到并报告给你当时发生的情况。当然人在驾驶的时候也有另一种模式，即 System 1。在这种模式下，你可以打电话，将自己的注意力或意识放在别的地方，同时你也可以开车。但是你在开车的情况下，只能适应一些简单的、你熟悉的路况。当你被问到是否碰到红绿灯或者其他情况，你完全不知道，这时你的意识集中在打电话这件事上。\n\n所以从人的角度看，你会发现，当人要适应一个变化多样的环境时，它不是所谓的 System 1，肌肉记忆要从 X 预测到 Y，在当前状态下要干什么。它要经过思考、判断来决策。那么如何让机器思考或者现在的机器甚至最大的大模型有没有思考呢？按照当前的神经网络架构来看，它是没有思考的", "section": "映射局限", "stance": "supports", "verification_status": "verified", "reason": "文内对神经网络缺乏思考的表述。"}, {"evidence_id": "ev_1901", "evidence_kind": "quote", "source_id": "source_68161c78067d7b4add05ba1a", "content_id": "content_9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "extraction_id": "extraction_fe8826e067e84de0741c77af", "input_sha256": "9e993068d54477c4444841a6b3d7b5b93d8671d448d7bbb30da4e3a515e51c45", "span_start": 1901, "span_end": 2336, "original_text": "System 2 的方式来执行。在这种情况下，如果你问人（即驾驶者）当时是如何去执行的？他会非常清楚地告诉你看到了哪些车子以及怎样做出的判断等。\n\n人其实是有意识的，可以主观感受到并报告给你当时发生的情况。当然人在驾驶的时候也有另一种模式，即 System 1。在这种模式下，你可以打电话，将自己的注意力或意识放在别的地方，同时你也可以开车。但是你在开车的情况下，只能适应一些简单的、你熟悉的路况。当你被问到是否碰到红绿灯或者其他情况，你完全不知道，这时你的意识集中在打电话这件事上。\n\n所以从人的角度看，你会发现，当人要适应一个变化多样的环境时，它不是所谓的 System 1，肌肉记忆要从 X 预测到 Y，在当前状态下要干什么。它要经过思考、判断来决策。那么如何让机器思考或者现在的机器甚至最大的大模型有没有思考呢？按照当前的神经网络架构来看，它是没有思考的。它就是 X 到 Y 的映射，在一个状态下应该怎样做出行为。所以在新的环境下，它是没有办法实现非常有效的适应", "section": "System 1/2", "stance": "supports", "verification_status": "verified", "reason": "文内对比 System 2 与当前 NN 在新环境适应。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T01:30:00+08:00"
+updated_at: "2026-07-16T01:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入汪军机器意识演讲；等待人工核验"
+source_ids: ["source_68161c78067d7b4add05ba1a"]
+relations: [{"type": "derived_from", "target_id": "source_68161c78067d7b4add05ba1a", "reason": "由机器之心对 UCL 汪军 2023 AI 科技年会演讲整理归纳；非原始讲稿 capture"}]
+---
+
+# X→Y 映射局限
+
+拟合非思考；复杂环境需 System 2（演讲观点）。
```
