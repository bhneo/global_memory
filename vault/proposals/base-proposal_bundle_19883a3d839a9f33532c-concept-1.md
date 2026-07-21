---
id: "concept_64c23c660c9017a5bf73d012"
type: "concept"
status: "working"
title: "Consecutive hand-object subgoal teleoperation"
created_at: "2026-07-20T12:47:59+08:00"
updated_at: "2026-07-20T12:47:59+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_570c26541066c02080dd8de5"]
relations: [{"type": "derived_from", "target_id": "source_570c26541066c02080dd8de5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-d-20260720", "status": "working"}]
change_reason: "compile bundle from source_570c26541066c02080dd8de5"
reflection_context: {"reflection_ids": ["reflection_631ecd2479bd127e62730569"], "importance": "high", "changed_belief": "A teleoperation interface need not copy every human joint. Sparse joint hand-object targets can preserve task intent while leaving the robot freedom to reorganize contacts, perform finger gaiting, and satisfy embodiment constraints.", "surprising": "One co-tracking controller supports real-time teleoperation across two dexterous hands and seven tasks, and the collected demonstrations train autonomous policies; however, autonomous evaluation uses simplified task subsets.", "connections": [{"shared_mechanism": "Like progressive VLA demonstration curricula, it decomposes complex skills into intermediate targets that are easier to learn than a complete end-to-end trajectory.", "boundary": "The system depends on reliable MoCap estimates of hand and object pose, and simulation does not cover all tool-environment interactions. Contact jams, stalls, and out-of-distribution disturbances remain failure modes.", "difference": "A curriculum organizes data and task difficulty, whereas TELEDEXTER's consecutive subgoals are a live control interface executed by a low-level reinforcement-learning policy."}], "open_questions": ["How should subgoal tolerance encode completion, operator intent, and contact safety simultaneously?"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-daily-batch-d-20260720"
updated_by: "working-ingestion-v1"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-daily-batch-d-20260720"
consolidation_count: 0
last_consolidated_at: null
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_0e0c7318a4fb8fb5bf1f"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_0e0c7318a4fb8fb5bf1f-concept-1.md"
origin_candidate_sha256: "9a04f819b32b8f63d6e093cd780ec6d5e0c94ba5566a08e37f51a01b43b5da62"
memory_schema_version: 2
---

# Consecutive hand-object subgoal teleoperation

Translate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.
