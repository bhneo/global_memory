---
id: "proposal_bundle_b994da5a62be9588eb42"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T10:03:00+08:00"
updated_at: "2026-07-28T10:03:58+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_f54583cf90b22697a9e728e9"]
relations: []
proposal_kind: "compile_bundle"
processor: "gpt-5.6-sol-high-daily-v2-readmission"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_8666065e768f390f8e11aefb"
input_sha256: "f6c59ebe5d12cd0253019510883d00f218c1d6d631fdad7b7b3004299e267efe"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_d28c0e5c8a5f864e616e2f7a", "target_path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "base_sha256": "278f6d6f2adc5eecc5b48e9a0c3d3425234ee434f6fbe54f27ed57ec9fbec1d8", "candidate_sha256": "6be982320a740dae3feaaa3f68565cad5d5ad9cd0fafb1de2d42b986c7c48889", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_b994da5a62be9588eb42-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_b994da5a62be9588eb42-concept-1.md", "working_path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "evolution_action": "limit", "exception_id": null, "working_at": "2026-07-28T10:03:58+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_d93bec5ed6088b94ef286b28", "type": "input", "title": "[hep-th/0603001] Holographic Derivation of Entanglement Entropy from AdS/CFT", "path": "vault/inputs/input-input_d93bec5ed6088b94ef286b28.md", "status": "active", "source_ids": ["source_6c0e05be9fc0c544826d7f9b"], "snippet": "# [hep-th/0603001] Holographic [Derivation] of Entanglement Entropy from AdS/CFT\n\nInput Episode for `source_6c0e05be9fc0c544826d7f9b`. The immutable…", "match_reason": "metadata:title"}, {"id": "input_b6e3f29e044d376ac9465e43", "type": "input", "title": "[2504.06297] Comment on \"Hilbert's Sixth Problem: Derivation of Fluid Equations via Boltzmann's Kinetic Theory\" by Deng, Hani, and Ma", "path": "vault/inputs/input-input_b6e3f29e044d376ac9465e43.md", "status": "active", "source_ids": ["source_969253c160fba88bdba75603"], "snippet": "…Derivation of Fluid Equations via Boltzmann's [Kinetic] Theory\" by Deng, Hani, and Ma\n\nInput Episode for `source…", "match_reason": "metadata:title"}, {"id": "reflection_0ce867c38dc7603e19a61160", "type": "reflection", "title": "波动动理学综述重复：标度律与图相消不重复计数 / review duplicate does not add a second derivation", "path": "vault/reflections/reflection-reflection_0ce867c38dc7603e19a61160.md", "status": "active", "source_ids": ["source_542db9d12c226d58c56b30fd"], "snippet": "# 波动动理学综述重复：标度律与图相消不重复计数 / review duplicate does not add a second derivation\n\n## Why important\n\n该摘要重述自然动理学时间上严格 WKE 导出依赖联合标度与任意阶图展开相消，已有反思已保存这些条件和有限有效窗口。\n\n## What changed…", "match_reason": "metadata:domains"}, {"id": "reflection_5950c81347199b019d31ef79", "type": "reflection", "title": "Verlinde 熵引力原始主张：导出形式不等于机制确证 / Verlinde entropic gravity: derivation is not mechanism validation", "path": "vault/reflections/reflection-reflection_5950c81347199b019d31ef79.md", "status": "active", "source_ids": ["source_35c0773ed4e8dcc92518936e"], "snippet": "# Verlinde 熵引力原始主张：导出形式不等于机制确证 / Verlinde entropic gravity: [derivation] is not mechanism validation\n\n## Why important\n\n原论文摘要将 Newton 力律的导出置于全息涌现空间假设下；形式推导不能单独确证温度、熵和信息屏的微观机制…", "match_reason": "metadata:title"}, {"id": "reflection_2e36e252e77618ec2e7ba6b5", "type": "reflection", "title": "硬球到 Boltzmann 的长时导出综述：光滑解寿命是边界 / long-time derivation is bounded by smooth-solution lifespan", "path": "vault/reflections/reflection-reflection_2e36e252e77618ec2e7ba6b5.md", "status": "active", "source_ids": ["source_5455a1b96c9684e7ce041786"], "snippet": "# 硬球到 Boltzmann 的长时导出综述：光滑解寿命是边界 / long-time [derivation] is bounded by smooth-solution lifespan\n\n## Why important\n\n综述说明硬球动力学的收敛可延长到 Boltzmann 方程光滑解存在的时间…", "match_reason": "metadata:title"}, {"id": "reflection_88da128593d6adeb3fda7549", "type": "reflection", "title": "Jacobson 局部视界热力学：状态方程推导与本体结论须分开 / local-horizon derivation is not ontology", "path": "vault/reflections/reflection-reflection_88da128593d6adeb3fda7549.md", "status": "active", "source_ids": ["source_4be2cb176dad6fdd8673bd31"], "snippet": "# Jacobson 局部视界热力学：状态方程推导与本体结论须分开 / local-horizon [derivation] is not ontology\n\n## Why important\n\n该文区分了在明确 Clausius、面积熵和局部 Rindler 假设下导出 Einstein 方程…", "match_reason": "metadata:title"}, {"id": "reflection_b5eedb8a6746a43f5a974635", "type": "reflection", "title": "视界热力学综述：观察者可及性不是引力微观推导 / horizon thermodynamics: observer accessibility is not a microscopic derivation", "path": "vault/reflections/reflection-reflection_b5eedb8a6746a43f5a974635.md", "status": "active", "source_ids": ["source_b732cdebf93f01a26b8adaff"], "snippet": "…observer accessibility is not a microscopic [derivation]\n\n## Why important\n\n该综述将热力学引力论证拆为观察者可及变量、量子场论的视界热性和对 Einstein--Hilbert 作用量的约束三层，避免把视界热行为直接当作已完成的引力微观推导。\n\n## What changed\n\n我会区分局部视界的可及性原则…", "match_reason": "metadata:title"}, {"id": "reflection_fec86130b52bb4cf70d5e7b8", "type": "reflection", "title": "Hilbert VI 评论：稀薄极限的形式推导不能单独确证连续流体完成度 / dilute-limit derivation does not by itself establish continuum-fluid completion", "path": "vault/reflections/reflection-reflection_fec86130b52bb4cf70d5e7b8.md", "status": "active", "source_ids": ["source_969253c160fba88bdba75603"], "snippet": "# Hilbert VI 评论：稀薄极限的形式推导不能单独确证连续流体完成度 / dilute-limit [derivation] does not by itself establish continuum-fluid completion\n\n## Why important\n\n该评论把数学严格的两步极限与其是否代表连续…", "match_reason": "metadata:title"}, {"id": "concept_d28c0e5c8a5f864e616e2f7a", "type": "concept", "title": "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS", "path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "status": "working", "source_ids": ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e", "source_3c493939fefd8cf6ca2e4ba2"], "snippet": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-[kinetic] limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L…", "match_reason": "metadata:title"}, {"id": "input_dc842109f2de463e2185e842", "type": "input", "title": "[2207.08358] Rigorous justification of the wave kinetic theory", "path": "vault/inputs/input-input_dc842109f2de463e2185e842.md", "status": "active", "source_ids": ["source_542db9d12c226d58c56b30fd"], "snippet": "# [2207.08358] Rigorous justification of the wave [kinetic] theory\n\nInput Episode for `source_542db9d12c226d58c56b30fd`. The immutable Source remains…", "match_reason": "metadata:title"}, {"id": "reflection_46d4dcf890fae70ce354f2d4", "type": "reflection", "title": "长时波湍流严格导出：有效窗口由 WKE 寿命而非小动理学时间决定 / long-time wave-turbulence justification is bounded by WKE lifespan", "path": "vault/reflections/reflection-reflection_46d4dcf890fae70ce354f2d4.md", "status": "active", "source_ids": ["source_ebf287b4d71ccdc41101466e"], "snippet": "# 长时波湍流严格导出：有效窗口由 WKE 寿命而非小动理学时间决定 / long-time [wave]-turbulence justification is bounded by WKE lifespan\n\n## Why important\n\nDeng 与…", "match_reason": "metadata:title"}, {"id": "synthesis_3a3249675668a93b9087ee43", "type": "synthesis", "title": "边界先于统一：视界热力学、Kakeya、动力学极限与流式接触控制的四条机制链", "path": "vault/synthesis/synthesis-synthesis_3a3249675668a93b9087ee43.md", "status": "active", "source_ids": ["source_086150581c4c39aee0813d57", "source_1ee2c3fae53a9d05689cd143", "source_299adfe6dd42f97b6f75b777", "source_323f116c3573f26f4af7785d", "source_32ee0cb3589fdf1de3cb8542", "source_3851b9ffbfbae3ca166308fd", "source_396cec9f720ec3afa4a7e9ad", "source_3c493939fefd8cf6ca2e4ba2", "source_408691502cdb43e7e2ea5c3b", "source_443db75c1157e4ee28fb3ea0", "source_4757ec1a2e8a0b678a350ee1", "source_4be2cb176dad6fdd8673bd31", "source_60c6677de9abc0b4e62a7dbe", "source_63ea95cc7031bab39a9b7461", "source_6b6bf6a9d857d2e74c2037ba", "source_6c565d5532cc4f2d0020ba4f", "source_7ab41149787a9cd99bd2fe58", "source_84c8c0edd41364ae0542b7ca", "source_9ec7a0dfcdc6c43339383f13", "source_a44d98212ed6d44a4998646e", "source_a9cfdeabfce614c49a3a92a1", "source_ad785f5be8067788394ec708", "source_b6d55666cda69c2a1c407986", "source_bd59f7e9cadcd7af4910d1e9", "source_bee998153a82cd2a92db045b", "source_cf15e6b90aaf4c6584d5efe2", "source_d211d7e773bf278ce50a7ac8", "source_ddde97eaf66d06d61a930ffa", "source_e67cd99ac31c7017d6f7f7c7", "source_e8651a193623cbe2b86becb0", "source_ebf287b4d71ccdc41101466e"], "snippet": "…与耦合强度的联合缩放，后者依赖稀薄硬球、平衡或近平特征以及碰撞树控制；证明工具不能直接迁移。\",\n    \"difference\": \"NLS 结果主要控制波作用谱向 wave [kinetic] equation 的收敛及其时间窗，硬球结果主要控制经验密度涨落的协方差或高斯场，并不等于非线性密度演化的同一极限。\"\n  },\n  {\n    \"shared_mechanism\": \"phi-divergence moment…", "match_reason": "metadata:domains"}, {"id": "reflection_6389c8b8e4c5e0fab459021a", "type": "reflection", "title": "波动动理学早期导出：标度改变会暴露共振与树展开失效", "path": "vault/reflections/reflection-reflection_6389c8b8e4c5e0fab459021a.md", "status": "active", "source_ids": ["source_f54583cf90b22697a9e728e9"], "snippet": "# 波动动理学早期导出：标度改变会暴露共振与树展开失效\n\n## Why important\n\n该文不仅给出正向的动理学极限窗口，还指出不同的弱非线性--大盒联合标度会让精确共振或树展开发散主导，从而阻碍用同一图展开方法延伸到 Tkin。\n\n## What changed\n\n即使弱非线性提示 Tkin∼alpha⁻²，我也不会假定同一论证能抵达该时间；可达窗口还取决于尺度关系和环面算术。\n\n## Surprising…", "match_reason": "metadata:domains"}, {"id": "reflection_5070fd4218e0e79c54eafa09", "type": "reflection", "title": "波动动理学严格化综述：标度律与混沌传播共同限定近似 / scaling laws and chaos constrain WKE", "path": "vault/reflections/reflection-reflection_5070fd4218e0e79c54eafa09.md", "status": "active", "source_ids": ["source_20fd6152d1c920afb55fa977"], "snippet": "# 波动动理学严格化综述：标度律与混沌传播共同限定近似 / scaling laws and chaos constrain WKE\n\n## Why important\n\n该说明将大盒和弱非线性的标度律、随机相位初值与图展开中的高阶相消共同视为严格 WKE 近似的条件，防止将动理学方程当成任意确定性波场的自动长时描述。\n\n## What changed\n\n我会把标度选择与混沌传播视为同等重要的有效方程前提…", "match_reason": "metadata:domains"}, {"id": "reflection_039e793833ff803621c37f30", "type": "reflection", "title": "波动动理学：NLS 的弱非线性极限需要匹配尺度与动理学时间", "path": "vault/reflections/reflection-reflection_039e793833ff803621c37f30.md", "status": "active", "source_ids": ["source_9ec7a0dfcdc6c43339383f13"], "snippet": "# 波动动理学：NLS 的弱非线性极限需要匹配尺度与动理学时间\n\n## Why important\n\nDeng 与 Hani 在 d≥3、L→∞ 与弱非线性 α→0 且 α∼L…", "match_reason": "metadata:domains"}, {"id": "reflection_2aa4c5bf8a7b1c9211cfb86e", "type": "reflection", "title": "波动动理学全标度：图展开的相消机制仍只保证有限窗口 / full scaling range retains a finite WKE window", "path": "vault/reflections/reflection-reflection_2aa4c5bf8a7b1c9211cfb86e.md", "status": "active", "source_ids": ["source_3c493939fefd8cf6ca2e4ba2"], "snippet": "# 波动动理学全标度：图展开的相消机制仍只保证有限窗口 / full scaling range retains a finite WKE window\n\n## Why important\n\n该文将 NLS 到 WKE 的严格性扩至 gamma…", "match_reason": "metadata:domains"}, {"id": "concept_972e54ed590f8b093808209f", "type": "concept", "title": "Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit", "path": "vault/memory/concept/concept_972e54ed590f8b093808209f.md", "status": "working", "source_ids": ["source_408691502cdb43e7e2ea5c3b", "source_aa1393c9b110562ca3f37509"], "snippet": "# Boltzmann--Grad 涨落层级 / fluctuation hierarchy in the Boltzmann--Grad limit\n\n在满足 Boltzmann--Grad 标度的稀薄硬球系统中，经验密度可在短时收敛到 Boltzmann 方程解；围绕平均的适当缩放涨落可收敛到由线性化…", "match_reason": "metadata:aliases"}, {"id": "concept_fb8af053ac360e94db141e7f", "type": "concept", "title": "Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure", "path": "vault/memory/concept/concept_fb8af053ac360e94db141e7f.md", "status": "working", "source_ids": ["source_6c565d5532cc4f2d0020ba4f"], "snippet": "# Phi-divergence 结构保持矩闭合 / phi-divergence structure-preserving moment closure\n\n对 Boltzmann 方程的 phi-divergence 矩闭合以受约束的 phi-divergence 最小化构造近似分布…", "match_reason": "metadata:domains"}, {"id": "reflection_bd92c5839c8839407acedd26", "type": "reflection", "title": "Hilbert 第六问题综述：不变流形方法把近似层级显式化", "path": "vault/reflections/reflection-reflection_bd92c5839c8839407acedd26.md", "status": "active", "source_ids": ["source_ca2fe79655cb6179fd2f7e6d"], "snippet": "# Hilbert 第六问题综述：不变流形方法把近似层级显式化\n\n## Why important\n\n该综述把从 Boltzmann 型动力学到流体方程的问题表述为分布空间中的慢不变流形，并比较 Chapman-Enskog 展开、直接不变性方程与 Newton 迭代；它提示推导是否可用取决于近似层级和短波边界，而不是只看形式展开是否存在。\n\n## What…", "match_reason": "metadata:domains"}, {"id": "reflection_de983eca7caffe455793c909", "type": "reflection", "title": "硬球统计动力学：同一涨落层级的修订来源覆盖", "path": "vault/reflections/reflection-reflection_de983eca7caffe455793c909.md", "status": "active", "source_ids": ["source_a92a32cadbf446fe33e3c588"], "snippet": "# 硬球统计动力学：同一涨落层级的修订来源覆盖\n\n## Why important\n\n论文使 Boltzmann 大数律、Gaussian 涨落过程和大偏差泛函成为三个显式分开的统计描述，各自具有不同标度和时间假设；当前版本为已存在的硬球涨落概念提供了来源级覆盖而非新机制。\n\n## What changed\n\n我会把成功的 Boltzmann--Grad 导出视为一组分层结论，而不是一条有效方程同时捕获典型与罕见行为的证据…", "match_reason": "metadata:domains"}, {"id": "input_57adc74f55821ba73e81d43f", "type": "input", "title": "[gr-qc/9504004] Thermodynamics of Spacetime: The Einstein Equation of State", "path": "vault/inputs/input-input_57adc74f55821ba73e81d43f.md", "status": "active", "source_ids": ["source_4be2cb176dad6fdd8673bd31"], "snippet": "…The Einstein [Equation] of State\n\nInput Episode for `source_4be2cb176dad6fdd8673bd31`. The immutable Source remains authoritative.\n\n# [gr-qc/9504004…", "match_reason": "metadata:title"}, {"id": "reflection_ae7589ae5a41e7354d0782e1", "type": "reflection", "title": "Jacobson 状态方程：局部平衡前提不能替代微观解释 / Jacobson equation of state needs local equilibrium", "path": "vault/reflections/reflection-reflection_ae7589ae5a41e7354d0782e1.md", "status": "active", "source_ids": ["source_057e50214c8825e0185c4a81"], "snippet": "# Jacobson 状态方程：局部平衡前提不能替代微观解释 / Jacobson [equation] of state needs local equilibrium\n\n## Why important\n\n可复用的认知价值是明确 Einstein 方程的局部热力学推导依赖面积熵、Unruh 温度、所有局部…", "match_reason": "metadata:title"}, {"id": "concept_e41100353a87ecb775dd5c71", "type": "concept", "title": "局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein equation of state", "path": "vault/memory/concept/concept_e41100353a87ecb775dd5c71.md", "status": "working", "source_ids": ["source_4be2cb176dad6fdd8673bd31", "source_bd59f7e9cadcd7af4910d1e9", "source_086150581c4c39aee0813d57"], "snippet": "# 局部 Rindler Clausius 关系与 Einstein 方程状态方程 / local-Rindler Clausius relation and Einstein [equation] of state\n\n在假定视界熵与面积成正比、并要求每个时空点的所有局部 Rindler…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_f54583cf90b22697a9e728e9"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "282e3a3fa513c853ee2951555889f101d9c1b8517a4b65c9e87831e97ed507a9"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`gpt-5.6-sol-high-daily-v2-readmission`
- Extraction：`extraction_8666065e768f390f8e11aefb`
- 编译前召回已有对象：25
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md
+++ candidate:vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md
@@ -1,43 +1,20 @@
 ---
 id: "concept_d28c0e5c8a5f864e616e2f7a"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
 created_at: "2026-07-27T10:47:14+08:00"
-updated_at: "2026-07-27T15:06:40+08:00"
-aliases: ["全标度三次 NLS 波动动理学导出", "full-range scaling wave kinetic derivation"]
+updated_at: "2026-07-28T10:03:00+08:00"
+aliases: ["wave kinetic scaling obstruction", "WKE tree divergence", "波动动理学标度障碍", "精确共振与树展开失效"]
 tags: []
-domains: ["wave-turbulence", "kinetic-theory"]
+domains: ["wave-turbulence", "kinetic-theory", "nonlinear-schrodinger-equation"]
 confidence: "high"
-source_ids: ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e", "source_3c493939fefd8cf6ca2e4ba2"]
+source_ids: ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e", "source_3c493939fefd8cf6ca2e4ba2", "source_f54583cf90b22697a9e728e9"]
 relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_3c493939fefd8cf6ca2e4ba2"
-reflection_context: {"reflection_ids": ["reflection_2aa4c5bf8a7b1c9211cfb86e"], "importance": "high", "changed_belief": "我会把标度覆盖与时间覆盖视为两条独立的定理维度。", "surprising": "", "connections": [{"shared_mechanism": "大盒--弱非线性协同极限将随机 NLS 二点统计连接到 WKE。", "boundary": "结论限于 d≥3、随机 Schwartz 初值、gamma∈(0,1)及小固定 Tkin 倍数。", "difference": "既有长时结果可至 tau*<taumax；本文主要解决完整标度与图展开收敛。"}], "open_questions": ["覆盖全标度的图相消方法能否与长时迭代结合，而不越过 WKE 的存在边界？"]}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "trustworthy-consolidation-v2"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 2
-last_consolidated_at: "2026-07-27T15:06:40+08:00"
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_b43108e78a2a6116b029"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b43108e78a2a6116b029-concept-1.md"
-origin_candidate_sha256: "5187efb5f75f79ce8d7758660bf81ea980a482d5f945fe2f2ad3830bb94bd9ac"
-origin_cognitive_artifact_sha256: "4451ba8095f3fddeba82a9383e77828628ba8be1be6dd8738784909274a4c30c"
-memory_schema_version: 2
-change_type: "refine"
+change_reason: "compile bundle from source_f54583cf90b22697a9e728e9"
+change_type: "limit"
+reflection_context: {"reflection_ids": ["reflection_6389c8b8e4c5e0fab459021a"], "importance": "high", "changed_belief": "即使弱非线性提示 Tkin∼alpha⁻²，我也不会假定同一论证能抵达该时间；可达窗口还取决于尺度关系和环面算术。", "surprising": "", "connections": [{"shared_mechanism": "它与现有三次 NLS 波动动理学概念都通过大盒与弱非线性的协同极限得到有效方程。", "boundary": "该来源假定良好准备的随机数据及其具体的标度和时间区间，不验证任意 NLS 的长时行为。", "difference": "既有概念浓缩正向严格极限；本文突出标度依赖的障碍、绝对收敛与可能条件抵消之间的差别。"}], "open_questions": []}
 proposed_status: "working"
-change_history: [{"change_type": "refine", "previous_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。", "new_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。", "changed_fields": [], "reason": "compile bundle from source_ebf287b4d71ccdc41101466e", "trigger_source": "source_ebf287b4d71ccdc41101466e", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。", "new_statement": "# 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS\n\n对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。\n\n## 新增来源材料\n\n- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。\n\n## 新增来源材料\n\n- `source_3c493939fefd8cf6ca2e4ba2`：在 d≥3 的任意周期矩形盒上，若三次 NLS 取随机 Schwartz 初值并满足 alpha=L^-gamma（gamma∈(0,1)），Deng 与 Hani 在 L→∞ 时将二点统计与 WKE 的近似严格覆盖到动理学时间 Tkin 的固定小倍数；该结果依赖随机初值、标度和有限窗口，不能替代至 WKE 最大寿命的长时结论。", "changed_fields": [], "reason": "compile bundle from source_3c493939fefd8cf6ca2e4ba2", "trigger_source": "source_3c493939fefd8cf6ca2e4ba2", "evidence_added": []}]
-last_consolidation_id: "consolidation_a011c23624aee356ecab9dc4"
 ---
 
 # 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS
@@ -51,3 +28,7 @@
 ## 新增来源材料
 
 - `source_3c493939fefd8cf6ca2e4ba2`：在 d≥3 的任意周期矩形盒上，若三次 NLS 取随机 Schwartz 初值并满足 alpha=L^-gamma（gamma∈(0,1)），Deng 与 Hani 在 L→∞ 时将二点统计与 WKE 的近似严格覆盖到动理学时间 Tkin 的固定小倍数；该结果依赖随机初值、标度和有限窗口，不能替代至 WKE 最大寿命的长时结论。
+
+## 新增来源材料
+
+- `source_f54583cf90b22697a9e728e9`：对良好准备的随机数据，三次 NLS 到波动动理学方程的严格逼近不仅受维度、初值和有限时间窗口约束，还依赖弱非线性强度 alpha 与大盒尺度 L 的联合标度。在论文区分的两类有利标度中，配对树展开绝对收敛并可到达 O(Tkin L^-epsilon)；在其他标度中，精确共振或树展开的绝对发散会在更早时间 T* 主导。因而形式上的 Tkin∼alpha^-2 不保证同一证明可抵达 Tkin，进一步延伸需要证明不同树或配对项之间的条件相消，或采用新的控制机制。
```
