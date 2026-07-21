---
id: "reflection_2183dcf7c9014c62c99ce9d6"
type: "reflection"
status: "active"
title: "Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths"
created_at: "2026-07-20T12:48:14+08:00"
updated_at: "2026-07-20T12:48:14+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["vla", "reinforcement-learning", "post-training", "secondary-source"]
confidence: "low"
source_ids: ["source_8b41a014bee47c4239a2fa81"]
relations: []
target_ids: ["input_30f3dd905ee97551e16138bd", "source_8b41a014bee47c4239a2fa81"]
input_id: "input_30f3dd905ee97551e16138bd"
created_by: "agent"
reflection_kind: "article"
importance: "medium"
why_important: "The notes separate an iterative offline path based on advantage-conditioned behavior cloning and human corrections from an online off-policy path using residual actions and a learned value function. That distinction helps organize post-training questions without treating reinforcement learning as one method."
what_changed: "Reliability gains may come from different data loops, credit signals, and deployment risks. Offline relabeling and correction recycling should not be evaluated with the same evidence expectations as live off-policy interaction."
surprising: "The secondary account foregrounds engineering details such as reset burden and asynchronous data collection, suggesting that throughput and recovery can dominate algorithm labels."
connections: [{"shared_mechanism": "Both paths concentrate new supervision around policy failures instead of uniformly expanding demonstrations.", "boundary": "This is a WeChat seminar summary, not the cited primary papers or experiment logs. Named algorithms, reported hours, success rates, and timing figures are research pointers and cannot support first-hand factual claims.", "difference": "The offline path reuses collected corrections through relabeling and cloning, while the online path updates value and residual policies from continuing environment interaction."}]
conflicts: ["A shared label of VLA post-training can hide materially different assumptions about exploration safety, reset access, and data stationarity."]
open_questions: ["Which primary papers and recorded talks substantiate each algorithm and reported metric?"]
possible_mechanisms: ["Failure-focused data and advantage estimates may increase useful gradient density relative to undifferentiated behavior cloning."]
future_directions: ["Retrieve the primary papers, video, and experiment appendices before using any quantitative result or implementation claim."]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# Secondary seminar notes: offline iteration and online off-policy VLA post-training are distinct paths

## Why important

The notes separate an iterative offline path based on advantage-conditioned behavior cloning and human corrections from an online off-policy path using residual actions and a learned value function. That distinction helps organize post-training questions without treating reinforcement learning as one method.

## What changed

Reliability gains may come from different data loops, credit signals, and deployment risks. Offline relabeling and correction recycling should not be evaluated with the same evidence expectations as live off-policy interaction.

## Surprising

The secondary account foregrounds engineering details such as reset burden and asynchronous data collection, suggesting that throughput and recovery can dominate algorithm labels.

## Connections

- Shared mechanism: Both paths concentrate new supervision around policy failures instead of uniformly expanding demonstrations.
  Boundary: This is a WeChat seminar summary, not the cited primary papers or experiment logs. Named algorithms, reported hours, success rates, and timing figures are research pointers and cannot support first-hand factual claims.
  Difference: The offline path reuses collected corrections through relabeling and cloning, while the online path updates value and residual policies from continuing environment interaction.

## Conflicts

- A shared label of VLA post-training can hide materially different assumptions about exploration safety, reset access, and data stationarity.

## Open questions

- Which primary papers and recorded talks substantiate each algorithm and reported metric?

## Possible mechanisms

- Failure-focused data and advantage estimates may increase useful gradient density relative to undifferentiated behavior cloning.

## Future directions

- Retrieve the primary papers, video, and experiment appendices before using any quantitative result or implementation claim.
