---
id: "synthesis_c39036fad2cb3b01ea32745c"
type: "synthesis"
status: "active"
title: "Frozen-policy RL interfaces: staged latent training and failure-gated test-time steering"
created_at: "2026-08-02T12:27:48+08:00"
updated_at: "2026-08-02T12:27:48+08:00"
aliases: []
tags: ["direction-synthesis", "cognitive-synthesis"]
domains: ["reinforcement-learning", "vla-posttraining", "flow-policy"]
confidence: "medium"
source_ids: ["source_98bb68f21232969a79d77918", "source_e504623270d30d733b2cb9e1"]
relations: []
input_reflections: ["reflection_f2923d7702925e8f48787602", "reflection_ff2ab4bfb8e8d08d5e0ab7df"]
input_concepts: ["concept_6a559a41722de87986c350e7", "concept_e69974f653450465afb2aa3e", "concept_latent_space_intervention_adaptation", "concept_vla_action_evaluation_distillation"]
emerging_patterns: ["Post-training around a frozen generative policy now separates two adaptation clocks: training-time latent-distribution improvement and failure-gated test-time candidate diversification.", "Keeping the base decoder fixed is not a sufficient safety boundary; stability also depends on critic warm-up, gradual latent degrees of freedom, detector calibration, verifier quality, and the support of the offline data."]
knowledge_updates: []
new_connections: [{"shared_mechanism": "Both works preserve the pretrained flow/VLA decoder and intervene through a smaller velocity or latent interface rather than rewriting the full policy.", "boundary": "RLMM-Flow learns an initial-noise distribution before deployment, whereas RL2-VLA composes velocity fields and selects candidates during inference; their guarantees and compute costs are not interchangeable.", "difference": "The first stabilizes high-dimensional chunk optimization with critic warm-up and coarse-to-fine latent freedom; the second protects successful modes by activating diversity only under predicted failure."}]
unresolved_tensions: ["A narrow intervention interface can preserve pretrained behavior while still concentrating errors when critics, failure detectors, or verifiers are miscalibrated outside their training support.", "Training-time improvement and test-time scaling may compound rather than cancel distribution shift, so their combination requires matched ablations rather than an additive-performance assumption."]
candidate_hypotheses: []
possible_experiments: []
truth_layer: "cognitive_synthesis"
created_by: "codex-gpt-5.6-sol-direction-v2-2026-08-02"
execution_safe: false
synthesis_protocol_version: 2
scope_kind: "direction"
scope_ids: ["reinforcement-learning-policy-posttraining"]
candidate_window: {"from_date": "2026-07-27", "to_date": "2026-08-02"}
delta_kind: "extend"
direction_assignments: [{"reflection_id": "reflection_ff2ab4bfb8e8d08d5e0ab7df", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": ["motion-control-execution-interfaces"], "subdirections": ["offline-rl", "residual-and-parameter-efficient-updates", "safety-and-support-domain-constraints"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "RLMM-Flow changes the policy-improvement interface by freezing the flow decoder, distilling chunk value into a latent critic, and staging horizon-shared then temporal-residual steering.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.26460"}, {"reflection_id": "reflection_f2923d7702925e8f48787602", "primary_direction": "reinforcement-learning-policy-posttraining", "secondary_directions": ["vla-architecture-pretraining-cross-embodiment", "value-reward-progress-uncertainty"], "subdirections": ["offline-rl", "actor-critic-or-token-level-adaptation", "safety-and-support-domain-constraints"], "crosscut_dimensions": ["system-and-deployment"], "routing_confidence": "high", "reason": "RL2-VLA changes test-time policy adaptation by composing frozen VLA and offline-RL velocity fields only when a failure detector predicts that the base policy needs intervention.", "source_role": "primary-result", "logical_work_id": "arxiv:2607.26991"}]
input_syntheses: ["synthesis_2cb5cbca9beef026f0c2b54e"]
---

# Frozen-policy RL interfaces: staged latent training and failure-gated test-time steering

## Emerging patterns

- Post-training around a frozen generative policy now separates two adaptation clocks: training-time latent-distribution improvement and failure-gated test-time candidate diversification.
- Keeping the base decoder fixed is not a sufficient safety boundary; stability also depends on critic warm-up, gradual latent degrees of freedom, detector calibration, verifier quality, and the support of the offline data.

## Knowledge updates

[]

## New connections

[
  {
    "shared_mechanism": "Both works preserve the pretrained flow/VLA decoder and intervene through a smaller velocity or latent interface rather than rewriting the full policy.",
    "boundary": "RLMM-Flow learns an initial-noise distribution before deployment, whereas RL2-VLA composes velocity fields and selects candidates during inference; their guarantees and compute costs are not interchangeable.",
    "difference": "The first stabilizes high-dimensional chunk optimization with critic warm-up and coarse-to-fine latent freedom; the second protects successful modes by activating diversity only under predicted failure."
  }
]

## Unresolved tensions

- A narrow intervention interface can preserve pretrained behavior while still concentrating errors when critics, failure detectors, or verifiers are miscalibrated outside their training support.
- Training-time improvement and test-time scaling may compound rather than cancel distribution shift, so their combination requires matched ablations rather than an additive-performance assumption.

## Candidate hypotheses

[]

## Possible experiments

None.
