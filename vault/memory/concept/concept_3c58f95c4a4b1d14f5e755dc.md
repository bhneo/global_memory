---
id: "concept_3c58f95c4a4b1d14f5e755dc"
type: "concept"
status: "working"
title: "Boltzmann 方程到不可压 Navier--Stokes 的受限水动力极限 / bounded hydrodynamic limit from Boltzmann to incompressible Navier--Stokes"
created_at: "2026-07-28T01:47:28+08:00"
updated_at: "2026-08-02T12:30:35+08:00"
aliases: ["Boltzmann to incompressible Navier--Stokes limit", "incompressible hydrodynamic limit", "Boltzmann 不可压水动力极限", "Leray 极限"]
tags: []
domains: ["kinetic-theory", "fluid-dynamics", "boltzmann-equation"]
confidence: "high"
source_ids: ["source_86550a0f567215a8394cf9e5"]
relations: [{"type": "derived_from", "target_id": "source_86550a0f567215a8394cf9e5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}, {"type": "related_to", "target_id": "concept_972e54ed590f8b093808209f", "reason": "两者都研究动理学极限，但既有节点从稀薄硬球粒子得到 Boltzmann 层级，本项从 Boltzmann 方程经水动力标度得到不可压流体弱解。", "confidence": "high", "created_by": "gpt-5.6-sol-high-daily-v2-readmission", "status": "working"}]
change_reason: "compile bundle from source_86550a0f567215a8394cf9e5"
reflection_context: {"reflection_ids": ["reflection_3919401ac5ba9591d0682172"], "importance": "high", "changed_belief": "我会区分 Boltzmann--Grad 粒子极限与此处 Boltzmann 方程到流体方程的水动力缩放，且不把弱收敛外推为唯一性或强收敛。", "surprising": "", "connections": [{"shared_mechanism": "两者都以明确标度和弱解紧性把微观描述连接到有效动力学。", "boundary": "本文限于硬截断势、小 Mach/Knudsen 同阶极限与重整化 Boltzmann 解。", "difference": "Boltzmann--Grad 处理粒子到动理学；本文从既有 Boltzmann 方程导出不可压 Leray 流体解。"}], "open_questions": ["何种额外正则性或稳定性条件能提高收敛方式或处理更广碰撞核？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "gpt-5.6-sol-high-daily-v2-readmission"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "gpt-5.6-sol-high-daily-v2-readmission"
consolidation_count: 2
last_consolidated_at: "2026-08-02T12:30:35+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_6069de7ae897e0394597"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_6069de7ae897e0394597-concept-1.md"
origin_candidate_sha256: "4250231220ea8b2d3125489eac622fece84c4ea6ab56fffbbc1744a03dff164e"
origin_cognitive_artifact_sha256: "cfe20fe689003cabeea44a54c2b6c67f1dccb705f5177de4daa557f1ea996a47"
memory_schema_version: 2
last_consolidation_id: "consolidation_e665b15163ca1d5cff10e052"
---

# Boltzmann 方程到不可压 Navier--Stokes 的受限水动力极限 / bounded hydrodynamic limit from Boltzmann to incompressible Navier--Stokes

对围绕 Maxwellian 的小涨落，在 Mach 数与 Knudsen 数渐近同阶、碰撞核满足论文的硬截断条件且采用全局重整化 Boltzmann 解时，任意极限点具有无穷小 Maxwellian 形式，其宏观场满足不可压 Navier--Stokes--Fourier 弱方程；在更强的初始相对熵条件下，速度场是 Leray 解并满足能量不等式。该结论是弱的子序列极限，不提供 Leray 解唯一性、全序列强收敛，也不是从硬球粒子系统直接到流体方程的 Boltzmann--Grad 极限。
