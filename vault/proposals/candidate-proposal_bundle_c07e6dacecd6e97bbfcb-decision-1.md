---
id: "decision_7c8f2f94e62bbb5e37e7732b"
type: "decision"
status: "proposal"
title: "the prompt asks the model to answerYES or NO first, and the loop treatsYES as a pass andNO as a fail"
created_at: "2026-07-18T16:30:37+08:00"
updated_at: "2026-07-18T16:30:37+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_5e14510061220db7f2344913"]
relations: [{"type": "derived_from", "target_id": "source_5e14510061220db7f2344913", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
change_reason: "compile bundle from source_5e14510061220db7f2344913"
---

# the prompt asks the model to answerYES or NO first, and the loop treatsYES as a pass andNO as a fail

the prompt asks the model to answerYES or NO first, and the loop treatsYES as a pass andNO as a fail

that triggers retry (or anAlertonce retries are exhausted). The prompts below follow the desktop-clearing
plan in which target objects are placed into a basket and later returned to the table; the agent may generate
task-specific variants at plan time, and persistent corrections from Corrective Memory edit the relevant fields.
Collection success criterion.Target objects are inside the basket.
Collection judging prompt.Are the target objects inside the basket? Answer YES or NO first.
Reset success criterion.Target objects are back on the table outside the basket.
Reset judging prompt.Are the target objects back on the table (not in the basket)? Answer
YES or NO first.
B.2. Data Consolidation
A run produces a log in which every trajectory carries the verifier’s verdict and the context under which it was
collected. Consolidation proceeds in three steps.
Filtering.Each trajectory is kept or discarded by the collection success criterion in the state the operator left it
at the end of the run. Trajectories the verifier marked as failures, and trajectories collected before a criterion
was corrected and re-judged as failures under the corrected criterion, are dropped. Concretely, when a prompt
rule is added to Corrective Memory we re-evaluate the affected trajectories against the updated criterion so
that the entire dataset is labeled under one consistent standard rather than the standard that happened to be
in force when each trajectory was recorded.
Figure 7 shows representative success feedback used during collection and reset verification. These examples
illustrate how successful episodes are confirmed and retained before data consolidation.
21

<!-- page: 22 -->

Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment
Collection
 Collection Episode Successfully Completed
Agent confirms that the grape bunch and banana have been successfully collected according to 
the task requirements. The target objects are placed in the valid collection area around the 
white plate, and the result satisfies the predefined collection success criteria.
Object-level Check:
      • Grape bunch: successfully grasped and placed.
      • Banana: successfully handled and included in the collection scene.
      • White plate: used as the target placement area.
Saved Data:
Multi-view images ｜ action trajectory ｜ robot states ｜ execution logs ｜ success label
Next Step:
Save this collection episode and proceed to reset the environment for the next round.
 Reset Episode Successfully Completed
Agent confirms that the grape bunch, banana, and white plate have been restored to a valid 
reset state according to the predefined reset criteria. The objects are separated from the 
collected configuration, allowing the next collection episode to start from a reusable scene.
Object-level Check:
      • Grape bunch: reset to a valid starting position.
      • Banana: reset to a valid starting position.
      • White plate: remains available as the target area.
Saved Data:
Multi-view images ｜ reset trajectory ｜ robot states ｜ execution logs ｜ reset success label
Next Step:
Continue the collection-reset loop or start the next collection episode.
Collection ResetReset
Figure 7: Representative feedback for successful collection-reset episodes. The system checks whether the
grape bunch, banana, and white plate satisfy the predefined collection or reset criteria. Successful episodes
proceed to data saving and the next step.
Quality report.Over the surviving trajectories we compute summary statistics of the recorded actions, the
per-dimension mean and standard deviation of the action vectors and a diversity measure given by the mean
pairwise distance between trajectory action sequences. These are reported as a read-only description of the
dataset. They are not used to accept or reject individual trajectories and they do not trigger any re-collection;
a low diversity reading is reported, not acted on. This is the deliberate choice noted in Section 3.4 to leave
coverage-driven re-collection to future work.
Packaging.The kept trajectories are written in the observation-action format expected by the policy’s fine-
tuning interface, with each record pairing the camera observation at a step with the action taken at that
step.
B.3. Fine-Tuning
We fine-tune𝜋0.5 (22) on each consolidated dataset, following the training setting of Physical Intelligence(22).
To keep comparisons across collection conditions meaningful, this configuration is held fixed across datasets:
the same base checkpoint, optimizer, schedule, and number of update steps.
B.4. Deployment Evaluation
Each fine-tuned policy is tested on the physical platform with no agent orchestrating it and no VLM verifying its
actions: the policy receives a camera observation and outputs actions directly, exactly as it would in deployment.
This isolates the quality of the learned policy from the collection-time machinery, as argued in Section 3.4.
Protocol.We run 20 blind deployment trials on the desktop-clearing task from randomized initial placements.
A trial counts as a success when the policy completes the task within the criterion used during collection. We
report the overall policy success rate across these trials. Initial placements are drawn from the same distribution
across the policies being compared, so that differences in success rate reflect the policies and not the test
conditions.
Use in the experiments.Section 4 compares policies fine-tuned on datasets from different collection conditions
underthissingleprotocol. Becausefiltering, fine-tuning, andthetestprotocolareallheldfixedacrossconditions,
a difference in policy success rate between two policies is attributable to the data each was trained on.
22

<!-- page: 23 -->

Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment
(a) Basket desktop clearing (b) Basket desktop reset(c) Blue box fruit clearing(d) Two basket object sorting
Figure 8: Representative scenes for the four verifier-correction settings evaluated in Table 2: (a) basket desktop
clearing, (b) basket desktop reset, (c) blue-box fruit clearing, and (d) two-basket object sorting.
C. Experiment Details
This appendix collects supplementary material for the experiments in Section 4: representative scenes for the
verifier-correction settings of Table 2 (Appendix C.1), definitions of the data-quality metrics reported in Table 4
(Appendix C.2), and a per-episode distribution comparison of those metrics for the human and agent datasets
(Appendix C.3).
C.1. Verifier-Correction Scenes
Table 2 evaluates the language-corrected judging rules across four settings that differ in container and layout.
Figure 8 shows a representative scene for each. Panels (a) and (b) depict the basket desktop-clearing task on
which the criterion mismatch was identified: the collection stage (a) is judged under the partial-containment
rule, and the reset stage (b) under the relaxed reset criterion. Panels (c) and (d) show the two layouts used to
test whether the corrected rules transfer: blue-box fruit clearing (c), the harder setting in which containment
judgments are frequently ambiguous, and two-basket object sorting (d), in which the judgment additionally
conditions on object category. Each row of Table 2 reports accuracy over ten judgment cases drawn from scenes
of the corresponding setting.
C.2. Data-Quality Metrics
Scope and aggregation.Table 4 summarizes two datasets, each containing𝑁= 50 episodes. For each metric,
the implementation first computes one value𝑥𝑖 per episode and then reports the unweighted episode mean
and sample standard deviation,
¯𝑥= 1
𝑁
𝑁∑︁
𝑖=1
𝑥𝑖, 𝑠=
⎯⎸⎸⎷ 1
𝑁−1
𝑁∑︁
𝑖=1
(𝑥𝑖−¯𝑥)2.(1)
Thus, the± notation denotes sample standard deviation rather than standard error. Image-based episode values
are averaged hierarchically over sampled frames, then cameras, and finally episodes. Below,clip(𝑧, 𝑎, 𝑏) =
min{max{𝑧, 𝑎}, 𝑏}.
Joint-signal metrics.Let 𝑞𝑡,𝑘 denote the position of arm joint𝑘 at frame𝑡. We use the 12 arm joints (six per
arm), exclude both grippers, and sample at 30 Hz, so∆𝑡= 1/30s. The third forward finite-difference jerk is
𝑗𝑡,𝑘 = 𝑞𝑡+3,𝑘−3𝑞 𝑡+2,𝑘 + 3𝑞𝑡+1,𝑘−𝑞 𝑡,𝑘
∆𝑡3 .(2)
For an episode of𝑇frames, the reported RMS jerk is
𝐽RMS =
⎯⎸⎸⎷ 1
12(𝑇−3)
𝑇−4∑︁
𝑡=0
12∑︁
𝑘=1
𝑗2
𝑡,𝑘,(3)
23

<!-- page: 24 -->

Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment
with units ofrad/s3; lower values indicate smoother joint motion. The implementation-specificSmoothness
diagnostic additionally counts thresholded frame-to-frame discontinuities,
𝐷=
𝑇−2∑︁
𝑡=0
1
{︂
max
1≤𝑘≤12
|𝑞𝑡+1,𝑘−𝑞 𝑡,𝑘|>0.10 rad
}︂
,(4)
then computes
𝑆= clip
(︂
100 exp
(︂
− 𝐽RMS
1200
)︂
−5𝐷,0,100
)︂
.(5)
Higher 𝑆 is better. Because each detected discontinuity incurs a five-point penalty, a dataset can have lower
RMS jerk yet lower Smoothness if its episodes contain more thresholded discontinuities.
Image metrics.For a grayscale sampled frame𝑌𝑓∈[0,255] 𝐻×𝑊, brightness is
𝐵𝑓 = 1
𝐻𝑊
𝐻∑︁
𝑢=1
𝑊∑︁
𝑣=1
𝑌𝑓 (𝑢, 𝑣).(6)
Brightnessrangesfrom0to255andhasnooptimizationdirection; itisreportedasanillumination-comparability
check.
The implementation-specificAestheticsdiagnostic is the custom heuristic
𝐴𝑓 = 100 (0.4𝑠𝑓 + 0.3𝑐𝑓 + 0.3𝑒𝑓 ).(7)
Its sharpness component is
𝑠𝑓 = clip
(︂ log10(1 + Var(Laplacian(𝑌𝑓 )))
3 ,0,1
)︂
.(8)
For the Hasler–Suesstrunk-style colorfulness component, let
𝑟𝑔 =𝑅−𝐺, 𝑦 𝑏 = 𝑅+𝐺
2 −𝐵,(9)
where𝜇 𝑟𝑔 , 𝜇𝑦𝑏 and𝜎 𝑟𝑔 , 𝜎𝑦𝑏 are their pixelwise means and standard deviations. Then
𝐶𝑓 =
√︁
𝜎2𝑟𝑔 +𝜎 2𝑦𝑏 + 0.3
√︁
𝜇2𝑟𝑔 +𝜇 2𝑦𝑏 , 𝑐 𝑓 = clip
(︂ 𝐶𝑓
80 ,0,1
)︂
.(10)
Defining the saturated-pixel fractions as
𝑝over =
⃒⃒{(𝑢, 𝑣) :𝑌𝑓 (𝑢, 𝑣)≥250}
⃒⃒
𝐻𝑊 , 𝑝 under =
⃒⃒{(𝑢, 𝑣) :𝑌𝑓 (𝑢, 𝑣)≤5}
⃒⃒
𝐻𝑊 ,(11)
the exposure component is
𝑒𝑓 = exp
[︃
−
(︂ 𝐵𝑓−128
64
)︂2]︃
clip(1−4(𝑝 over +𝑝 under),0,1).(12)
The resulting Aesthetics score ranges from 0 to 100, with higher values preferred.
C.3. Dataset Metrics Comparison
Figure 9 shows the per-episode distributions of the four diagnostics in Table 4 for the two50-episode datasets of
Section 4.4: the human teleoperation set and theZero2Skill(agent) set. Each panel is a violin-and-boxplot
24

<!-- page: 25 -->

Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment
for one metric—Smoothness, Aesthetics, Brightness, and RMS jerk—with the episode mean marked by a
diamond. The spreads match the aggregate trends in Table 4: brightness is comparable; the agent set has
higher Aesthetics and lower mean RMS jerk; and its Smoothness is lower on average with a wider spread,
consistent with more thresholded discontinuities among agent-collected episodes.
0
20
40
60
80
100
Smoothness
52
54
56
58
60
62
64
Aesthetics
126
128
130
132
134
136
138
140
142
Brightness
0
100
200
300
400
500
RMS jerk
Agent dataset Human dataset Mean
Figure 9: Per-episode distributions of Smoothness, Aesthetics, Brightness, and RMS jerk for the agent-collected
dataset and the human teleoperation dataset (𝑁= 50 episodes each). Diamonds mark episode means; boxes
show quartiles and medians.
25
