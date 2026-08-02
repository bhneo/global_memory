---
id: "synthesis_93372d68a4a8d430df544876"
type: "synthesis"
status: "active"
title: "World-model control needs explicit prediction-access topology"
created_at: "2026-08-02T19:52:49+08:00"
updated_at: "2026-08-02T19:52:49+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["world-models-predictive-representations", "robot-planning", "contact-rich-manipulation"]
confidence: "medium"
source_ids: ["source_7fa8acc5e021363b55491e3e", "source_a54ea0123fbadf6d7012c9fb"]
relations: []
input_reflections: ["reflection_7c31cec2267b21f33baf67f2", "reflection_d4da03127a4726ff3f567d63"]
input_concepts: ["concept_1920583cd9c7063491d45a40", "concept_1bc84fc99981d367b712d161", "concept_2db7edf95d63ca80702f042e", "concept_8f574f03117d21adf127d23f", "concept_c5189a551eabdd0550bacd70"]
emerging_patterns: ["Predictive states affect action through at least two non-interchangeable paths: isolated training-time supervision and inference-time imagined-rollout search.", "Control value depends not only on what a world model predicts, but on exactly when and which branch can read the prediction, and whether generated futures are checked against real outcomes."]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Both systems let predictions reshape behavior without declaring a predicted future to be a current fact: TacWAM shapes the representation while action reads current anchors, and World Action Planner evaluates candidate plans through model imagination.", "boundary": "TacWAM's evidence is limited to a small set of real contact tasks and its futures are neither action-conditioned nor an online correction loop; the World Action Planner source is an official project page without a captured numeric result table, and iterative search can exploit world-model error.", "difference": "TacWAM deliberately blocks future-target access at deployment to prevent leakage, whereas World Action Planner deliberately consumes generated futures at inference to revise the plan."}]
unresolved_tensions: ["Excess prediction access can leak privileged targets, while insufficient access prevents causal plan comparison; the useful boundary is architecture- and deployment-dependent.", "Inference-time search can amplify systematic world-model bias unless imagined outcomes are calibrated against fresh observations and real execution traces."]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "codex-gpt-5.6-sol-direction-v2-2026-08-02-batch-2"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["world-models-predictive-representations"]
candidate_window: {"from_date": "2026-08-02", "to_date": "2026-08-02"}
delta_kind: "extend"
direction_assignments: [{"reflection_id": "reflection_7c31cec2267b21f33baf67f2", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["dexterous-manipulation-contact-rich-control", "motion-control-trajectory-generation"], "subdirections": ["multimodal-and-tactile-prediction", "predictive-evaluation-and-failure-detection"], "crosscut_dimensions": ["data-and-demonstrations", "system-and-deployment"], "routing_confidence": "high", "reason": "The main research change is an information-topology constraint: future tactile prediction supervises representation learning in parallel, while the deployed action branch remains restricted to current observation anchors.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.28391"}, {"reflection_id": "reflection_d4da03127a4726ff3f567d63", "primary_direction": "world-models-predictive-representations", "secondary_directions": ["agent-and-autonomous-systems"], "subdirections": ["rollout-and-planning-interfaces", "action-conditioned-prediction", "predictive-evaluation-and-failure-detection"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "medium", "reason": "The project changes the planning question by using action-conditioned imagined rollouts as an inference-time search signal that revises a VLM plan rather than treating the first plan as final.", "source_role": "official-project-page", "logical_work_id": "project:world-action-planner"}]
input_syntheses: ["synthesis_6afd38e074bc25801dc1558b"]
---

# World-model control needs explicit prediction-access topology

## Emerging patterns

- Predictive states affect action through at least two non-interchangeable paths: isolated training-time supervision and inference-time imagined-rollout search.
- Control value depends not only on what a world model predicts, but on exactly when and which branch can read the prediction, and whether generated futures are checked against real outcomes.

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Both systems let predictions reshape behavior without declaring a predicted future to be a current fact: TacWAM shapes the representation while action reads current anchors, and World Action Planner evaluates candidate plans through model imagination.",
    "boundary": "TacWAM's evidence is limited to a small set of real contact tasks and its futures are neither action-conditioned nor an online correction loop; the World Action Planner source is an official project page without a captured numeric result table, and iterative search can exploit world-model error.",
    "difference": "TacWAM deliberately blocks future-target access at deployment to prevent leakage, whereas World Action Planner deliberately consumes generated futures at inference to revise the plan."
  }
]

## Unresolved tensions

- Excess prediction access can leak privileged targets, while insufficient access prevents causal plan comparison; the useful boundary is architecture- and deployment-dependent.
- Inference-time search can amplify systematic world-model bias unless imagined outcomes are calibrated against fresh observations and real execution traces.

## Candidate hypotheses

[]

## Possible experiments

None.
