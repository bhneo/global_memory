---
id: "concept_b1b62d103e0a768399664d9d"
type: "concept"
status: "proposal"
title: "Simulator-validated single-view demonstration transfer"
created_at: "2026-07-20T12:48:07+08:00"
updated_at: "2026-07-20T12:48:07+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_513a527cb4d410e4f94a9bb5"]
relations: [{"type": "derived_from", "target_id": "source_513a527cb4d410e4f94a9bb5", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-d-20260720", "status": "proposal"}]
change_reason: "compile bundle from source_513a527cb4d410e4f94a9bb5"
reflection_context: {"reflection_ids": ["reflection_65fb6fe12e2291077f28900c"], "importance": "high", "changed_belief": "Single-view video transfer is best treated as a closed inference-and-validation loop. Perception proposes geometry and phase, planning checks embodiment feasibility, and simulation backtracks when the proposed motion fails.", "surprising": "The paper reports transfer from three real demonstrations with repeated trials, yet the most consequential bottleneck is still basic object tracking under occlusion rather than policy scale.", "connections": [{"shared_mechanism": "Like TELEDEXTER, DemoBridge preserves task-level geometric relations rather than directly retargeting every human joint.", "boundary": "Evidence is limited to a single arm, small demonstration counts, and the tested objects and scenes. Occlusion, reconstruction error, and bimanual interaction remain outside the demonstrated boundary.", "difference": "TELEDEXTER is live hand-object teleoperation with an RL contact controller; DemoBridge is offline single-view trajectory reconstruction with collision planning and simulator validation."}], "open_questions": ["Can phase validation remain reliable when objects are deformable, heavily occluded, or jointly manipulated by two arms?"]}
---

# Simulator-validated single-view demonstration transfer

Convert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.
