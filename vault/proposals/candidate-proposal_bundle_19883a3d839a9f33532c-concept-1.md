---
id: "concept_64c23c660c9017a5bf73d012"
type: "concept"
status: "proposal"
title: "Consecutive hand-object subgoal teleoperation"
created_at: "2026-07-20T12:47:59+08:00"
updated_at: "2026-07-20T13:07:25+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_570c26541066c02080dd8de5"]
relations: [{"type": "derived_from", "target_id": "source_570c26541066c02080dd8de5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-d-20260720", "status": "working"}]
change_reason: "compile bundle from source_570c26541066c02080dd8de5"
change_type: "needs_review"
reflection_context: {"reflection_ids": ["reflection_631ecd2479bd127e62730569"], "importance": "high", "changed_belief": "A teleoperation interface need not copy every human joint. Sparse joint hand-object targets can preserve task intent while leaving the robot freedom to reorganize contacts, perform finger gaiting, and satisfy embodiment constraints.", "surprising": "One co-tracking controller supports real-time teleoperation across two dexterous hands and seven tasks, and the collected demonstrations train autonomous policies; however, autonomous evaluation uses simplified task subsets.", "connections": [{"shared_mechanism": "Like progressive VLA demonstration curricula, it decomposes complex skills into intermediate targets that are easier to learn than a complete end-to-end trajectory.", "boundary": "The system depends on reliable MoCap estimates of hand and object pose, and simulation does not cover all tool-environment interactions. Contact jams, stalls, and out-of-distribution disturbances remain failure modes.", "difference": "A curriculum organizes data and task difficulty, whereas TELEDEXTER's consecutive subgoals are a live control interface executed by a low-level reinforcement-learning policy."}], "open_questions": ["How should subgoal tolerance encode completion, operator intent, and contact safety simultaneously?"]}
proposed_status: "working"
---

# Consecutive hand-object subgoal teleoperation

Translate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.
