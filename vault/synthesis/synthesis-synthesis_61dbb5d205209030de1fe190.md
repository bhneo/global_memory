---
id: "synthesis_61dbb5d205209030de1fe190"
type: "synthesis"
status: "active"
title: "Agent runtimes need separate retention, dispatch, and recovery authority"
created_at: "2026-08-02T19:53:28+08:00"
updated_at: "2026-08-02T19:53:28+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["agent-autonomous-systems", "embodied-agents", "runtime-governance"]
confidence: "medium"
source_ids: ["source_8c84c595f1a48ba498b2074e", "source_ddd2f65020c2e556f2b93330"]
relations: []
input_reflections: ["reflection_094021136751760eac7be536", "reflection_0c154d1167b819af9040f0f9"]
input_concepts: ["concept_2db7edf95d63ca80702f042e", "concept_3b83de1641240159d66c23d4", "concept_asymmetric_frozen_vla_harness", "concept_ca2e18a64c50dab0d08b3f1a", "concept_dual_protocol_hri_agent_execution_boundary", "concept_typed_verified_robot_skill_graph"]
emerging_patterns: ["A reliable physical-agent runtime needs validity at three distinct boundaries: retain dependency-closed components, authorize an exact effect at a final gate, and escalate skill recovery from fresh observed state.", "Recovery records and proposed plans are not authority: new candidates or observations must re-enter the appropriate gate, and neither protocol can manufacture motor capability absent from the underlying policy and controllers."]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Both runtimes preserve unaffected work and localize recovery instead of resetting an entire response or task plan after one failure.", "boundary": "HALO formalizes component validity and dispatch authorization at an adapter boundary; ROBOBRIDGE governs physical skill execution and inherits errors from perception, manually tuned thresholds, the frozen VLA, and low-level controllers.", "difference": "HALO computes greatest fixed-point dependency closure and issues a one-dispatch token, whereas ROBOBRIDGE uses a fast success check, slower failure diagnosis, and hierarchical retry, regenerate, replan, or re-perceive actions."}]
unresolved_tensions: ["A combined architecture still needs an explicit mapping from logical component dependencies to physical action phases and their revocation conditions.", "Asynchronous latest-value perception and manually selected monitor thresholds can make recovery decisions stale or miscalibrated even when the orchestration protocol is structurally correct."]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "codex-gpt-5.6-sol-direction-v2-2026-08-02-batch-2"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["agent-autonomous-systems"]
candidate_window: {"from_date": "2026-08-02", "to_date": "2026-08-02"}
delta_kind: "extend"
direction_assignments: [{"reflection_id": "reflection_0c154d1167b819af9040f0f9", "primary_direction": "agent-autonomous-systems", "secondary_directions": [], "subdirections": ["tool-use-and-environment-interaction", "evaluation-and-safety", "reflection-and-recovery"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "The central contribution is a runtime authority protocol that retains a greatest dependency-closed component set, binds an exact executable effect, and requires fresh final-gate authorization before one dispatch.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.27636"}, {"reflection_id": "reflection_094021136751760eac7be536", "primary_direction": "agent-autonomous-systems", "secondary_directions": ["vision-language-action-models", "motion-control-trajectory-generation"], "subdirections": ["planning-and-task-decomposition", "tool-use-and-environment-interaction", "reflection-and-recovery"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "The paper changes the embodied-agent runtime question through a two-phase monitor and hierarchical retry, regenerate, replan, and re-perceive loop around a frozen VLA policy.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.27881"}]
input_syntheses: ["synthesis_4cda1c2094e661cde05160ef"]
---

# Agent runtimes need separate retention, dispatch, and recovery authority

## Emerging patterns

- A reliable physical-agent runtime needs validity at three distinct boundaries: retain dependency-closed components, authorize an exact effect at a final gate, and escalate skill recovery from fresh observed state.
- Recovery records and proposed plans are not authority: new candidates or observations must re-enter the appropriate gate, and neither protocol can manufacture motor capability absent from the underlying policy and controllers.

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Both runtimes preserve unaffected work and localize recovery instead of resetting an entire response or task plan after one failure.",
    "boundary": "HALO formalizes component validity and dispatch authorization at an adapter boundary; ROBOBRIDGE governs physical skill execution and inherits errors from perception, manually tuned thresholds, the frozen VLA, and low-level controllers.",
    "difference": "HALO computes greatest fixed-point dependency closure and issues a one-dispatch token, whereas ROBOBRIDGE uses a fast success check, slower failure diagnosis, and hierarchical retry, regenerate, replan, or re-perceive actions."
  }
]

## Unresolved tensions

- A combined architecture still needs an explicit mapping from logical component dependencies to physical action phases and their revocation conditions.
- Asynchronous latest-value perception and manually selected monitor thresholds can make recovery decisions stale or miscalibrated even when the orchestration protocol is structurally correct.

## Candidate hypotheses

[]

## Possible experiments

None.
