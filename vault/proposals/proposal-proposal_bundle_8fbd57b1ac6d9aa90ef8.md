---
id: "proposal_bundle_8fbd57b1ac6d9aa90ef8"
type: "proposal"
status: "pending"
title: "Compile bundle：对话李弘扬：从端到端 UniAD 之后，重新寻找机器智能的源点｜What's Next"
created_at: "2026-07-16T23:14:16+08:00"
updated_at: "2026-07-16T23:14:16+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_fbe623b6e75223f553071d03"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "对话李弘扬：从端到端 UniAD 之后，重新寻找机器智能的源点｜What's Next"
source_authority: "secondary_analysis"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_49b8ffeac0de053a509f4bd2"
input_sha256: "3b428837a31f2f57d282df6a6421d2b0f3c132b1c1a7590aff9986065c61c247"
bundle_items: [{"item_id": "claim-1", "object_type": "claim", "action": "create", "target_id": "claim_23283adb0c3baf33a884cdac", "target_path": "vault/knowledge/claims/claim_23283adb0c3baf33a884cdac-来源原文-嘉宾-李弘扬-香港大学助理教授-香港大学计算与数据科学学院助理院长-上海创智学院全时导师-opendrivelab创始.md", "base_sha256": null, "candidate_sha256": "4f46751b523278812885c65300e89450f33b9b8b46fa8effc3de3680c34dbcbe", "decision": "pending", "potential_conflicts": [], "atomicity_status": "atomic", "evidence_coverage": "partial", "review_tier": "low", "candidate_path": "vault/proposals/candidate-proposal_bundle_8fbd57b1ac6d9aa90ef8-claim-1.md", "base_path": null}]
existing_context: []
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_fbe623b6e75223f553071d03"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "secondary_analysis", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
---

# Compile bundle：对话李弘扬：从端到端 UniAD 之后，重新寻找机器智能的源点｜What's Next

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_49b8ffeac0de053a509f4bd2`
- 编译前召回已有对象：0
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### claim-1 (create claim)

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_23283adb0c3baf33a884cdac-来源原文-嘉宾-李弘扬-香港大学助理教授-香港大学计算与数据科学学院助理院长-上海创智学院全时导师-opendrivelab创始.md
@@ -0,0 +1,36 @@
+---
+id: "claim_23283adb0c3baf33a884cdac"
+type: "claim"
+status: "proposal"
+title: "来源原文：嘉宾｜李弘扬，香港大学助理教授、香港大学计算与数据科学学院助理院长、上海创智学院全时导师、OpenDriveLab创始人兼负责人、源策智能创始人\n访谈｜东寰、刘"
+created_at: "2026-07-16T23:14:16+08:00"
+updated_at: "2026-07-16T23:14:16+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "low"
+source_ids: ["source_fbe623b6e75223f553071d03"]
+relations: [{"type": "derived_from", "target_id": "source_fbe623b6e75223f553071d03", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_fbe623b6e75223f553071d03"
+evidence: [{"evidence_id": "evidence_ec86732b0efb58249184", "evidence_kind": "quote", "source_id": "source_fbe623b6e75223f553071d03", "content_id": "content_3b428837a31f2f57d282df6a6421d2b0f3c132b1c1a7590aff9986065c61c247", "extraction_id": "extraction_49b8ffeac0de053a509f4bd2", "span_start": 0, "span_end": 478, "original_text": "嘉宾｜李弘扬，香港大学助理教授、香港大学计算与数据科学学院助理院长、上海创智学院全时导师、OpenDriveLab创始人兼负责人、源策智能创始人\n访谈｜东寰、刘洵\n编者导语2023 年，UniAD 斩获 CVPR 最佳论文，特斯拉 FSD V12 同步走向端到端——一个学术判断与产业终局在同一时刻被双向印证。就在那个被外界视为\"乘胜追击\"的时点，李弘扬却选择从自动驾驶的牌桌上抽身，转向更难、更早期、共识更稀薄的具身智能。三年之后的今天，他既是港大的青年学者，也是 OpenDriveLab 的掌舵人，更是刚刚启程的源策智能创始人。当 VLA、世界模型、人形机器人的概念在赛道上彼此挤压、众声喧哗，这位自称到了\"在互联网会失业第一年\"的 36 岁学者，给出了一份冷静到近乎冒犯的判断：具身智能至多处于自动驾驶的 L1.5 时代，VLA 和世界模型都不够本质，真正的胜负手在于\"让机器更像人\"的 Ego-centric 数据范式与原生大模型架构。这是一篇关于范式跃迁、关于第一性原理、也关于一位科学家如何向企业家身份完成自我重构的深度对话。\n本期访谈嘉宾：", "page": null, "stance": "context", "verification_status": "verified", "input_sha256": "3b428837a31f2f57d282df6a6421d2b0f3c132b1c1a7590aff9986065c61c247", "extractor": "wechat-article-v1", "extractor_version": "1.0", "reason": "确定性 fallback 只确认逐字位置，不自动判断支持或反对。"}]
+applicability: []
+uncertainty: "确定性 fallback 能力有限；该原文尚未经过语义事实核验。"
+atomicity_status: "atomic"
+evidence_coverage: "partial"
+split_from: null
+split_reason: null
+quote_verification: "exact"
+extraction_quality: "good"
+epistemic_source_authority: "secondary"
+evidence_entailment: "none"
+claim_confidence: "low"
+publication_gate: "needs_review"
+---
+
+# 来源原文：嘉宾｜李弘扬，香港大学助理教授、香港大学计算与数据科学学院助理院长、上海创智学院全时导师、OpenDriveLab创始人兼负责人、源策智能创始人
+访谈｜东寰、刘
+
+嘉宾｜李弘扬，香港大学助理教授、香港大学计算与数据科学学院助理院长、上海创智学院全时导师、OpenDriveLab创始人兼负责人、源策智能创始人
+访谈｜东寰、刘洵
+编者导语2023 年，UniAD 斩获 CVPR 最佳论文，特斯拉 FSD V12 同步走向端到端——一个学术判断与产业终局在同一时刻被双向印证。就在那个被外界视为"乘胜追击"的时点，李弘扬却选择从自动驾驶的牌桌上抽身，转向更难、更早期、共识更稀薄的具身智能。三年之后的今天，他既是港大的青年学者，也是 OpenDriveLab 的掌舵人，更是刚刚启程的源策智能创始人。当 VLA、世界模型、人形机器人的概念在赛道上彼此挤压、众声喧哗，这位自称到了"在互联网会失业第一年"的 36 岁学者，给出了一份冷静到近乎冒犯的判断：具身智能至多处于自动驾驶的 L1.5 时代，VLA 和世界模型都不够本质，真正的胜负手在于"让机器更像人"的 Ego-centric 数据范式与原生大模型架构。这是一篇关于范式跃迁、关于第一性原理、也关于一位科学家如何向企业家身份完成自我重构的深度对话。
+本期访谈嘉宾：
```
