---
id: "synthesis_4cda1c2094e661cde05160ef"
type: "synthesis"
status: "active"
title: "Agent capability lifecycles: verify frozen skills, then compile mature experience"
created_at: "2026-08-02T12:28:13+08:00"
updated_at: "2026-08-02T12:28:13+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["embodied-agents", "capability-learning", "policy-orchestration"]
confidence: "medium"
source_ids: ["source_38375a0f6ddc91f3bfde47d3", "source_d0908c8e9c58809dd2665c1e"]
relations: []
input_reflections: ["reflection_0927933ce742db3006087d15", "reflection_9e08fb71dc807c22fb1b8bf5"]
input_concepts: ["concept_5495a66616b2989c1ce38a5f", "concept_d7111f304971448401a57f3b", "concept_f35cd7f55e4108ce45ec35d7", "concept_typed_verified_robot_skill_graph"]
emerging_patterns: ["A physical agent's capability inventory is not static: verified execution traces can move from expensive open-ended reasoning to reusable exemplars and then to low-latency closed-loop policies.", "Verification has two roles that must remain distinct: it closes an individual skill-execution loop and it filters which experiences are safe enough to compile into future capability."]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Both systems keep heterogeneous motor capabilities behind an orchestrator that observes outcomes, routes the next action, and falls back when the selected capability fails.", "boundary": "Pigey evaluates a fixed skill library and adds no motor training, while HERO changes the library over time by reusing and training on selected experiences; one does not establish the other's continual-learning claims.", "difference": "Pigey's main intervention is a per-episode verify-and-recover loop; HERO's additional intervention is a cross-episode maturity ladder with heuristic-to-exemplar-to-reflexive compilation and reverse deployment fallback."}]
unresolved_tensions: ["The same imperfect success signal that enables recovery can contaminate exemplars and downstream policies when it is reused as a capability-compilation gate.", "More aggressive compilation reduces latency but can hide task novelty until a mature policy fails, making fallback sensitivity and capability-support estimation central governance questions."]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "codex-gpt-5.6-sol-direction-v2-2026-08-02"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["agent-autonomous-systems"]
candidate_window: {"from_date": "2026-07-27", "to_date": "2026-08-02"}
delta_kind: "extend"
direction_assignments: [{"reflection_id": "reflection_9e08fb71dc807c22fb1b8bf5", "primary_direction": "agent-autonomous-systems", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment"], "subdirections": ["planning-and-task-decomposition", "tool-use-and-environment-interaction", "reflection-and-recovery"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "Pigey changes the task-level agent loop by placing decomposition, skill routing, typed failure feedback, verification, and recovery around frozen motor backends.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.21725"}, {"reflection_id": "reflection_0927933ce742db3006087d15", "primary_direction": "agent-autonomous-systems", "secondary_directions": ["motion-control-execution-interfaces"], "subdirections": ["memory-and-continual-learning", "planning-and-task-decomposition", "reflection-and-recovery"], "crosscut_dimensions": ["data-and-demonstrations", "system-and-deployment"], "routing_confidence": "high", "reason": "HERO changes the capability lifecycle by promoting successful experience from heuristic reasoning to exemplar reuse and reflexive policy execution, with reverse fallback at deployment.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.26809"}]
input_syntheses: ["synthesis_ec1aa84e855b7b9c6d3e6fb7"]
---

# Agent capability lifecycles: verify frozen skills, then compile mature experience

## Emerging patterns

- A physical agent's capability inventory is not static: verified execution traces can move from expensive open-ended reasoning to reusable exemplars and then to low-latency closed-loop policies.
- Verification has two roles that must remain distinct: it closes an individual skill-execution loop and it filters which experiences are safe enough to compile into future capability.

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Both systems keep heterogeneous motor capabilities behind an orchestrator that observes outcomes, routes the next action, and falls back when the selected capability fails.",
    "boundary": "Pigey evaluates a fixed skill library and adds no motor training, while HERO changes the library over time by reusing and training on selected experiences; one does not establish the other's continual-learning claims.",
    "difference": "Pigey's main intervention is a per-episode verify-and-recover loop; HERO's additional intervention is a cross-episode maturity ladder with heuristic-to-exemplar-to-reflexive compilation and reverse deployment fallback."
  }
]

## Unresolved tensions

- The same imperfect success signal that enables recovery can contaminate exemplars and downstream policies when it is reused as a capability-compilation gate.
- More aggressive compilation reduces latency but can hide task novelty until a mature policy fails, making fallback sensitivity and capability-support estimation central governance questions.

## Candidate hypotheses

[]

## Possible experiments

None.
