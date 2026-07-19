---
id: "proposal_bundle_4b838b6e25783ddf7b9b"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T01:40:20+08:00"
updated_at: "2026-07-19T01:40:20+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e326446389e083c6ba9c94c2"]
relations: []
proposal_kind: "compile_bundle"
processor: "deterministic-bounded-bundle-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_6506a11d8f50ef2494f8b80e"
input_sha256: "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
bundle_items: [{"item_id": "question-1", "object_type": "question", "action": "create", "target_id": "question_a6b5d595ace88e906de2e2f0", "target_path": "vault/frontier/questions/question_a6b5d595ace88e906de2e2f0-can-the-proxy-labels-themselves-be-corrected-before.md", "base_sha256": null, "candidate_sha256": "27f49d8f353e6a4bbe4474ded956777fe0186af11bf524c0f2f1f7d70e97028d", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_4b838b6e25783ddf7b9b-question-1.md", "base_path": null, "working_path": "vault/memory/question/question_a6b5d595ace88e906de2e2f0.md", "working_at": "2026-07-19T01:40:20+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…the MOA can be\nthought of as an [unsupervised] auxiliary task that may help the\nmodel to learn…", "match_reason": "full-text:body"}, {"id": "architecture_929a68a1fd830b00f780f138", "type": "architecture", "title": "the policy attends to memory through its existing token-processing pipeline.", "path": "vault/memory/architecture/architecture_929a68a1fd830b00f780f138.md", "status": "working", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "…Vision-language-action models transfer web knowledge to [robotic] control. In\nConference on Robot Learning, 2023.\n[2] M…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e326446389e083c6ba9c94c2"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`deterministic-bounded-bundle-v1`
- Extraction：`extraction_6506a11d8f50ef2494f8b80e`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### question-1 (create question)

```diff
--- /dev/null
+++ candidate:vault/frontier/questions/question_a6b5d595ace88e906de2e2f0-can-the-proxy-labels-themselves-be-corrected-before.md
@@ -0,0 +1,660 @@
+---
+id: "question_a6b5d595ace88e906de2e2f0"
+type: "question"
+status: "proposal"
+title: "can the proxy labels themselves be corrected before"
+created_at: "2026-07-19T01:40:20+08:00"
+updated_at: "2026-07-19T01:40:20+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_e326446389e083c6ba9c94c2"]
+relations: [{"type": "derived_from", "target_id": "source_e326446389e083c6ba9c94c2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e326446389e083c6ba9c94c2"
+---
+
+# can the proxy labels themselves be corrected before
+
+can the proxy labels themselves be corrected before
+
+they serve as supervision for estimators or policies?
+We introduceUnsupervised Robotic Value Correction
+(UR-VC), an offline, training-free method for correcting time-
+derived progress labels in demonstration datasets. UR-VC is
+based on a simple data-driven premise: time-derived labels are
+noisy mainly because each demonstration has its own temporal
+distortion. Cross-episode state matches provide anchors for
+reducing this distortion: when similar physical states are found
+in independently collected episodes, the state is approximately
+held fixed while the timestamp varies across trajectories.
+Aggregating the time-derived labels of these matched states
+therefore estimates where that state typically lies in the task,
+rather than where it happened to occur in one particular
+episode. UR-VC operationalizes this idea by retrieving se-
+arXiv:2607.12892v1  [cs.RO]  14 Jul 2026
+
+<!-- page: 2 -->
+
+t=0.06
+ t=0.25
+ t=0.28
+ t=0.80
+ t=0.97
+0.0 0.2 0.4 0.6 0.8 1.0
+episode time (normalized)
+0.0
+0.2
+0.4
+0.6
+0.8
+1.0progress
+grasp slips  progress regresses
+(the time label keeps rising)
+time label (proxy)
+UR-VC corrected
+Fig. 1:Time is not progress.In a real cloth flatten-and-fold episode, the garment is first smoothed, but a slipping grasp
+reintroduces wrinkles and causes physical progress to regress. The time-derived label (gray) remains monotone by construction,
+whereas UR-VC estimates corrected progress by retrieving semantically similar frames from other episodes and aggregating their
+time-derived labels, producing a correction (red) that decreases when the visual state worsens. Across the primary evaluation
+set, 13.4% of frames receive a negative horizon advantage under UR-VC, capturing regressions the time proxy misses.
+mantically similar frames from other episodes using SigLIP-
+2 visual embeddings [26] and aggregating their time-derived
+labels into a corrected progress estimate, with at most one
+matched label contributed by each episode to avoid over-
+weighting temporally adjacent frames.
+We study UR-VC on real bimanual cloth flatten-and-fold
+data. Cloth manipulation is a natural testbed for this problem
+because progress is visually meaningful, local regressions
+occur frequently, and similar intermediate states recur across
+garments and episodes [28, 8]. Since true physical progress
+is not directly observed in demonstrations, we first evalu-
+ate the conditions that make correction useful: cross-episode
+coverage, task-state consistency, stability under aggregation,
+and recovery of non-monotone progress. We find that these
+conditions hold in our data: high-quality matches are abundant
+even at moderate dataset sizes (Fig. 2), retrieved frames align
+with folding state across different garments (Fig. 3), the
+corrected estimate becomes smoother as the evaluation set
+grows (Fig. 4), and the labels recover local regressions while
+preserving the overall task trend (Fig. 1). As a downstream use
+case, we convert the corrected signal into advantage labels for
+VLA training, following recent advantage-conditioned policy
+learning [1, 22], and observe a positive trend in real-robot task
+success under matched training settings (Tab. I).
+Our contributions are summarized as follows:
+•Proxy-label perspective.We formulate normalized time
+as a noisy proxy for latent physical task progress, and
+highlight its limitations both within episodes and across
+episodes in non-monotone manipulation.
+•Unsupervised correction.We propose UR-VC, an of-
+fline and training-free method that corrects time-derived
+progress labels by aggregating semantically similar states
+across episodes, requiring no manual progress labels,
+reward annotations, or an additional value model.
+•Real-robot evidence.On real bimanual cloth flatten-and-
+fold data, we validate the conditions needed for correction
+and demonstrate a downstream use case in advantage-
+conditioned VLA training.
+II. RELATEDWORK
+Progress and value supervision in robot learning.Vision-
+language-action models such as RT-2 [5], OpenVLA [15],
+and theπ 0/π0.5 family [4, 3] make large-scale robot pol-
+icy learning practical, and recent systems consume explicit
+progress or value signals:π ∗
+0.6 [1] learns a value function
+for advantage conditioning, and Gemini Robotics 1.5 [25]
+uses stage progress for planning and completion judgment.
+A body of work learns visual progress, reward, or value
+estimators from contrastive video objectives, language-image
+representations, value pretraining, optimal transport, or gener-
+ative modeling [23, 24, 18, 19, 2, 11, 13], or elicits values from
+large pretrained models [20, 7, 17]. UR-VC is complementary
+to both lines: it corrects the proxy scoresbeforeany estimator
+is trained, targeting the supervision itself.
+Cross-episode redundancy and label correction.UR-
+VC is also related to learning with noisy labels [21, 10]
+and graph/nearest-neighbor label propagation [29, 14]. The
+difference is the source of redundancy. Rather than propagating
+sparse human labels over an image graph, UR-VC exploits
+repeated robot states across independently collected episodes,
+where each timestamp is a noisy measurement of the same
+latent physical progress.
+
+<!-- page: 3 -->
+
+Deformable manipulation and semantic encoders.Cloth
+manipulation has been studied in simulation and real-robot
+settings, including SoftGym [16], ALOHA/ACT [28], Mobile
+ALOHA [12], and CLASP [8]. UR-VC studies real bimanual
+cloth flatten-and-fold data since this setting exposes both
+within-episode regressions and across-episode timing variation
+in time-derived progress labels. We use SigLIP-2 [26], an
+image–text pretrained semantic vision encoder, to retrieve
+cross-episode state matches.
+III. METHOD
+We first formalize normalized time as a noisy proxy for
+latent task progress and explain why its fixed-horizon dif-
+ference provides a degenerate advantage signal. We then
+introduce UR-VC, which corrects this proxy by aggregating
+time-derived labels from semantically matched states across
+episodes. Finally, we describe how the corrected progress
+estimate is converted into advantage labels for policy training.
+A. Time-derived progress as a noisy proxy
+Let episodeecontain frameso (e)
+1 , . . . , o(e)
+Te . A common
+time-derived proxy defines
+g(e)
+t =t/T e,(1)
+treating elapsed time as progress supervision. We assume there
+is also an unobserved task progressp(o)∈[0,1], determined
+by the physical state relevant to the task. This progresspis a
+conceptual target, not a quantity available to the algorithm.
+The mismatch betweengandpappears in two ways. First,
+within an episode, physical progress can be non-monotone
+while normalized time is monotone by construction. For
+instance, if a cloth fold slips or a grasp fails,p(o (e)
+t )may
+decrease even thoughg (e)
+t continues to increase. As a result,
+raw time labels cannot distinguish actions that improve the task
+state from actions that stall or locally undo progress. Second,
+across episodes, the same physical state can appear at different
+normalized times. Operators may move at different speeds,
+pause for different durations, or take different recovery paths
+after local failures. Thus,g (e)
+t contains not only information
+about task progress, but also episode-specific timing distortion.
+A frame that is physically close to completion may receive
+a lower time-derived label in a slow episode, while a less
+advanced state may receive a higher label in a fast episode.
+These two issues directly affect downstream learning. For
+advantage conditioning with a fixed action horizonH, the
+finite difference of the raw time proxy is
+gt+H −g t = H
+Te
+,(2)
+constant within episodee. Therefore, within the same episode,
+naively differencing the raw label gives every frame the same
+ranking signal, regardless of whether the action improves or
+worsens the physical state.
+Across episodes the difference varies only through the
+episode lengthT e, which primarily reflects execution speed
+rather than state improvement. More generally, any method
+101
+102
+103
+104
+number of retrieval episodes
+0.0
+0.2
+0.4
+0.6
+0.8
+1.0frames with a cross-episode match
+99.9%
+90.4%
+primary evaluation set
+(150 episodes: 98%)
+similarity  0.90
+similarity  0.955
+Fig. 2:Cross-episode matches are abundant.Fraction of
+task-region frames with at least one semantically similar
+neighbor in adifferentepisode as more retrieval episodes are
+added. On real flatten-fold demonstrations, the 150-episode
+primary evaluation set already covers 98% of frames at simi-
+larity≥0.90, indicating that independently collected episodes
+provide sufficient anchors for correcting time-derived progress
+labels. Coverage further improves at the10 4-episode scale,
+reaching 99.9% at≥0.90and 90.4% at≥0.955.
+that consumes raw time labels as progress or value supervision
+inherits these within-episode monotonicity errors and across-
+episode timing distortions.
+B. UR-VC: Episode-Balanced Cross-Episode Correction
+UR-VC corrects a time-derived proxy by exploiting cross-
+episode recurrence: similar physical states often appear in
+independently collected demonstrations, but at different nor-
+malized times. For an idealized recurring state, episodee’s
+time-derived score can be viewed as
+g(e) =p+ε e,(3)
+wherepis the latent progress andε e is an episode-specific tim-
+ing error. Averaging proxy scores across independent episodes
+can reduce this error; averaging many nearby frames from the
+same episode would not, since their errors are correlated.
+Concretely, letf i be theL 2-normalized SigLIP-2 embed-
+ding of query framei, and letf ⊤
+i fj denote cosine similarity.
+For every other episodee, we form an in-band candidate set
+Ci,e ={j: ep(j) =e,|g j −g i| ≤τ}.(4)
+We then keep only the best representative from that episode,
+j∗
+i,e = arg max
+j∈Ci,e
+f ⊤
+i fj,(5)
+and discard it if its similarity is belowρ. LetM i be the
+remaining episode representatives, optionally capped to the
+topmepisodes by similarity. The corrected estimate is
+ˆgi = 1
+|Mi|
+X
+e∈Mi
+gj∗
+i,e .(6)
+
+<!-- page: 4 -->
+
+query  p=0.09
+ sim=0.961
+highly similar frames in other episodes  (similarity shown)
+sim=0.956
+ sim=0.956
+ sim=0.955
+ sim=0.953
+query  p=0.80
+ sim=0.966
+ sim=0.965
+ sim=0.964
+ sim=0.962
+ sim=0.962
+query  p=0.84
+ sim=0.972
+ sim=0.960
+ sim=0.960
+ sim=0.957
+ sim=0.955
+query  p=0.96
+ sim=0.953
+ sim=0.951
+ sim=0.950
+ sim=0.949
+ sim=0.948
+Fig. 3:Cross-episode retrieval captures folding state across garment appearances.For query frames at successive fold
+stages (left, black borders), nearest neighbors retrieved fromotherepisodes (red borders, similarity shown) exhibit the same
+folding state across different garment colors.
+If no representative survives, we leaveg i unchanged.
+The episode-balanced form matches the statistical assump-
+tion above: each episode contributes at most one proxy score
+to the average, so the estimate aggregates evidence across
+demonstrations rather than across temporally adjacent frames
+from a single trajectory. The similarity thresholdρacts as
+a conservative match filter, preventing episodes without a
+sufficiently similar state from contributing to the estimate.
+The temporal bandτimposes a locality constraint on label
+correction: all averaged labels satisfy|g j −g i| ≤τ, and
+therefore the correction magnitude is bounded as|ˆgi −g i| ≤τ.
+UR-VC is an offline label-correction procedure. After com-
+puting visual embeddings, it only requires similarity search,
+per-episode representative selection, and scalar averaging. In
+implementation, the per-episode argmax is computed with a
+single masked scatter-max over the offline corpus, so the
+correction reduces to a small number of matrix operations.
+UR-VC doesn’t require manual progress labels, reward anno-
+tations, online rollouts, or training an additional value model.
+C. Advantage Labels from Corrected Progress
+After correcting the time-derived proxy, we use the resulting
+estimateˆgto construct advantage labels for policy training
+followingπ ∗
+0.6. This step is only one downstream use of UR-
+VC: the correction is performed at the progress-label level,
+before any policy or value model is trained.
+For an action chunk starting at frameiwith horizonH, we
+define a scalar corrected advantage proxy as
+ri = ˆgi+H −ˆgi.(7)
+Near the end of an episode, we compute the difference to the
+final frame and rescale it to the horizon rate:
+ri = H
+Te −i
+ 
+ˆgTe −ˆgi
+
+.(8)
+Here we follow the indexing conventiono (e)
+1 , . . . , o(e)
+Te . If the
+implementation uses zero-indexed frames, the denominator
+should be adjusted accordingly.
+We rank frames byr i and mark the top20%as positive-
+advantage examples. The corresponding training frames re-
+ceive a plain-text prompt suffix, e.g., “..., advantage:
+positive”. At deployment, the policy is queried with the
+same positive-advantage suffix. The policy architecture, train-
+ing data, and optimization schedule are otherwise unchanged.
+Thus, UR-VC introduces no new policy objective and no
+separate value model. It only replaces the raw time-derived
+supervision with a corrected signal, allowing existing progress-
+or advantage-conditioned pipelines to use cross-episode infor-
+mation without additional annotation or critic training.
+IV. EXPERIMENTS
+We evaluate UR-VC on real bimanual cloth flatten-and-
+fold data. Since true physical progress is not directly ob-
+served in real demonstrations, we do not claim access to
+ground-truth progress labels. Instead, our evaluation follows
+the requirements implied by the method: cross-episode state
+recurrences should be sufficiently dense, retrieved frames
+should correspond to the same semantic task state rather than
+superficial appearance, the corrected labels should express
+non-monotone progress, and the resulting signal should be
+usable in a downstream robot-learning pipeline.
+
+<!-- page: 5 -->
+
+102
+103
+104
+number of retrieval episodes
+0.0350
+0.0375
+0.0400
+0.0425
+0.0450
+0.0475
+0.0500
+0.0525
+0.0550mean | 2g|
+primary evaluation set
+roughness of raw estimate
+episode-balanced coverage
+0.90
+0.92
+0.94
+0.96
+0.98
+1.00
+coverage
+Fig. 4:The correction improves with more retrieval
+episodes.Episode-balanced UR-VC across retrieval-set sizes,
+reported as mean±std over random subsets. The roughness
+of the corrected progress estimate, measured by mean|∆ 2ˆgt|,
+decreases by roughly one third from 50 episodes to the10 4-
+episode scale. Meanwhile, coverage remains high and rises
+from 96% to 99.9%, showing that larger retrieval sets provide
+both denser support and more stable correction. The 150-
+episode primary evaluation set already lies in a usable regime.
+A. Experimental Setup
+Task and data.We study a long-horizon bimanual cloth
+flatten-and-fold task. Each episode starts from a garment
+placed on a table and requires the robot to flatten the cloth and
+then fold it into the target configuration. This task is a natural
+setting for evaluating time-derived progress proxies: progress
+is visually meaningful, intermediate states recur across gar-
+ments and episodes, and local regressions frequently occur
+due to slips, failed grasps, wrinkles, or partial undoing. Unless
+otherwise stated, intrinsic analyses use a primary evaluation
+set of 150 real robot episodes sampled from a flatten-and-fold
+dataset released by [27]. We additionally report scaling trends
+by increasing the retrieval pool up to the10 4-episode scale.
+UR-VC implementation.For each frame, we compute an
+L2-normalized SigLIP-2 visual embedding and retrieve seman-
+tically similar frames from other episodes. Unless otherwise
+stated, we use a temporal bandτ= 0.3and a cosine-similarity
+thresholdρ= 0.90, which provide a conservative locality
+constraint and filter weak cross-episode matches.
+Metrics.We evaluate four aspects of the correction. First,
+coveragemeasures the fraction of query frames that have
+at least one valid match from a different episode. Second,
+semantic consistencychecks whether retrieved frames preserve
+task state across appearance variation. Third,non-monotone
+recoverymeasures whether the corrected estimate produces
+negative horizon advantages in states where progress locally
+regresses, while preserving the overall task trend. Finally, we
+test a downstream use case by using UR-VC-derived advantage
+labels to train an advantage-conditioned VLA and evaluate it
+on a dual 7-DoF AgileX robot with absolute joint control.
+B. Cross-Episode Coverage and Scaling
+UR-VC is useful only if query states have high-quality
+matches in other episodes. This condition already holds at the
+scale of the primary evaluation set. With 150 episodes, 98%
+of frames have a nearest neighbor in a different episode with
+cosine similarity at least 0.90; 69.9% remain covered under
+the stricter threshold 0.955.
+Coverage further improves with retrieval-set size. As the
+retrieval pool increases from the primary set to the10 4-episode
+scale corpus, coverage rises to 99.9% at threshold 0.90 and
+90.4% at threshold 0.955 (Fig. 2). This suggests that cross-
+episode redundancy is not only present in large-scale robot
+datasets but is already available at moderate collection scales,
+and it becomes denser as more demonstrations are added.
+C. Semantic Consistency of Retrieved States
+High coverage alone is insufficient: visually similar frames
+must also correspond to similar task states. Otherwise, aver-
+aging their time-derived labels would blur together unrelated
+configurations rather than correct temporal distortion. We
+therefore inspect nearest-neighbor retrievals across different
+episodes and garments (Fig. 3). The retrieved frames preserve
+the folding state across garment colors and appearances,
+indicating that the embedding primarily captures cloth config-
+uration rather than superficial texture. These results support
+the main assumption behind UR-VC: semantically similar
+task states recur across independently collected episodes, and
+retrieval can identify them despite appearance variation.
+D. Recovering Non-Monotone Progress
+We next examine whether UR-VC expresses progress pat-
+terns that normalized time cannot represent. A normalized-
+time label is monotone by construction, so its fixed-horizon ad-
+vantage is non-negative and nearly constant within an episode.
+It therefore cannot distinguish an action that improves the cloth
+state from one that stalls or temporarily undoes progress.
+UR-VC preserves the global task trend while allowing local
+regressions. In the real episode shown in Fig. 1, the cor-
+rected estimate decreases when a slipping grasp reintroduces
+wrinkles and the cloth state visibly worsens, whereas the raw
+time-derived label continues to increase. Across the primary
+evaluation set, 13.4% of frames receive a negative horizon
+advantage under UR-VC, using (r i <−0.02with a horizon of
+5% of the episode length, approximately≈1.7 s). At the same
+time, the corrected estimate remains highly correlated with
+normalized time overall (0.98), which is expected because the
+temporal band constrains the correction to remain local. Thus,
+UR-VC does not discard the coarse temporal ordering of the
+demonstration; it selectively corrects local regions where the
+visual state suggests that progress has regressed.
+The correction also becomes more stable as the retrieval
+pool grows. From 50 episodes to the10 4-episode scale, the
+roughness of the corrected estimate, measured by mean|∆ 2ˆgt|,
+decreases by roughly one third, while coverage increases from
+96% to 99.9 % (Fig. 4). Larger retrieval sets provide both
+denser support and smoother estimates.
+
+<!-- page: 6 -->
+
+TABLE I:Downstream real-robot evaluation.Conditions
+correspond to different tablecloth backgrounds, with 30 trials
+per condition. UR-VC improves the average success rate from
+72.8% to 78.9% and performs better in 5 of 6 conditions.
+Condition Baseline UR-VC
+Bare table 0.900.97
+Beige cloth 0.700.73
+Blue-gray cloth0.500.43
+Light-yellow cloth 0.630.90
+Light-gray cloth 0.770.80
+Khaki cloth 0.870.90
+Average 0.7280.789
+E. Downstream Real-Robot Evaluation
+UR-VC produces a corrected progress signal independently
+of how that signal is consumed. We evaluate one downstream
+use case: advantage-conditioned VLA training in the style of
+π∗
+0.6, using aπ 0.5 backbone.
+Setup.All methods share the same human-collected training
+set, model architecture, training schedule, and hyperparame-
+ters; one policy is trained per labelling scheme. The training
+mix combines 5700 flatten-and-fold demonstrations with 1795
+dedicatedrecoverydemonstrations that pass through degraded
+cloth states—precisely the regime where time-derived labels
+are least reliable. The no-advantage baseline trains without
+advantage labels. The UR-VC variant computes corrected
+progress with Eq. 6, marks its top-20% advantage frames as
+positive (Sec. III-C), and conditions the policy on the resulting
+positive/negative labels.
+Evaluation protocol.We evaluate on an AgileX bimanual
+robot performing flatten-then-fold on short-sleeve garments.
+The test set contains six table conditions, including a bare-
+table condition and five tablecloth backgrounds. For each
+condition, we evaluate 6 garments with 5 repetitions each,
+yielding 30 trials per condition and 180 trials per method. We
+report per-condition and the average success rates in Tab. I.
+Results.UR-VC advantage conditioning improves average
+success from 0.728 (131/180) to 0.789 (142/180), with higher
+success in 5 of 6 table conditions. These results provide
+application-level evidence that UR-VC-derived advantage la-
+bels can improve policy performance when inserted into a
+standard advantage-conditioned VLA pipeline. Importantly,
+the improvement is obtained without changing the backbone,
+training data, optimization schedule, or policy objective, sug-
+gesting that the gains are attributable to the supervision signal
+rather than additional model capacity or training changes.
+V. LIMITATIONS
+UR-VC assumes that visually similar observations indicate
+similar task progress. This assumption is shared with progress
+estimator and value models: when visually similar states occur
+at different task stages or after different action histories, their
+latent progress can be ambiguous. Episode-balanced averaging
+reduces trajectory-specific timing noise, but it cannot correct
+systematic retrieval errors.
+Our downstream evaluation focuses on one representative
+use case: using UR-VC-derived supervision for advantage-
+conditioned VLA training in real bimanual cloth manipulation.
+Under matched experimental settings, the corrected labels lead
+to higher average success, suggesting their practical utility as
+a drop-in supervision signal. Future work may further examine
+the method across broader task families, training scales, and
+hyperparameter settings.
+VI. CONCLUSION
+UR-VC corrects time-derived progress proxies by averaging
+semantic state recurrences across independent robot episodes.
+It exploits dataset redundancy to better align scalable proxy
+labels with latent physical progress. On real bimanual cloth
+data, cross-episode matches are abundant and semantic, cor-
+rected estimates recover regressions that a monotone time
+proxy cannot express, and the resulting signal can be used
+for advantage-conditioned VLA training. Time provides useful
+and scalable supervision, but it should not be conflated with
+physical progress. As a model-agnostic preprocessing step,
+UR-VC refines timestamp-derived labels before downstream
+model training, without requiring an additional value model
+or any changes to the model architecture or training objective.
+REFERENCES
+[1] Ali Amin, Raichelle Aniceto, Ashwin Balakrishna, Kevin
+Black, Ken Conley, Grace Connors, James Darpinian,
+Karan Dhabalia, Jared DiCarlo, et al.π ∗
+0.6: a vla that
+learns from experience.arXiv.org, 2511.14759.
+[2] Chethan Bhateja, Derek Guo, Dibya Ghosh, Anikait
+Singh, Manan Tomar, Quan Vuong, Yevgen Chebotar,
+Sergey Levine, and Aviral Kumar. Robotic offline rl from
+internet videos via value-function pre-training.arXiv.org,
+2309.13041.
+[3] Kevin Black, Noah Brown, James Darpinian, Karan
+Dhabalia, Danny Driess, Adnan Esmail, Michael Robert
+Equi, Chelsea Finn, Niccolo Fusai, Manuel Y Galliker,
+et al.π 0.5: A vision-language-action model with open-
+world generalization. InCoRL, 2025.
+[4] Kevin Black, Noah Brown, Danny Driess, Adnan Esber,
+Michael Equi, Chelsea Finn, et al.π 0: A vision-language-
+action flow model for general robot control. InRSS,
+2025.
+[5] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen
+Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding,
+Danny Driess, Avinava Dubey, Chelsea Finn, et al. RT-2:
+Vision-language-action models transfer web knowledge
+to robotic control. InCoRL, 2023.
+[6] Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee,
+Aditya Grover, Misha Laskin, Pieter Abbeel, Aravind
+Srinivas, and Igor Mordatch. Decision transformer: Rein-
+forcement learning via sequence modeling. InNeurIPS,
+2021.
+[7] Shirui Chen, Cole Harrison, Ying-Chun Lee, Angela Jin
+Yang, Zhongzheng Ren, Lillian J Ratliff, Jiafei Duan,
+Dieter Fox, and Ranjay Krishna. Topreward: Token
+
+<!-- page: 7 -->
+
+probabilities as hidden zero-shot rewards for robotics.
+arXiv.org, 2602.19313.
+[8] Yuhong Deng, Chao Tang, Cunjun Yu, Linfeng Li, and
+David Hsu. Clasp: General-purpose clothes manipulation
+with semantic keypoints.arXiv.org, 2408.08160.
+[9] Scott Emmons, Benjamin Eysenbach, Ilya Kostrikov, and
+Sergey Levine. Rvs: What is essential for offline rl via
+supervised learning? InICLR, 2022.
+[10] Beno ˆıt Fr ´enay and Michel Verleysen. Classification in
+the presence of label noise: a survey.IEEE Transactions
+on Neural Networks and Learning Systems, 2013.
+[11] Yuwei Fu, Haichao Zhang, Di Wu, Wei Xu, and Benoit
+Boulet. Robot policy learning with temporal optimal
+transport reward. InNeurIPS, 2024.
+[12] Zipeng Fu, Tony Z Zhao, and Chelsea Finn. Mobile
+aloha: Learning bimanual mobile manipulation with low-
+cost whole-body teleoperation. InCoRL, 2024.
+[13] Tao Huang, Guangqi Jiang, Yanjie Ze, and Huazhe Xu.
+Diffusion reward: Learning rewards via conditional video
+diffusion. InECCV, 2024.
+[14] Ahmet Iscen, Giorgos Tolias, Yannis Avrithis, and Ondrej
+Chum. Label propagation for deep semi-supervised
+learning. InCVPR, 2019.
+[15] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted
+Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov,
+Ethan Foster, Grace Lam, Pannag Sanketi, et al. Open-
+VLA: An open-source vision-language-action model. In
+CoRL, 2024.
+[16] Xingyu Lin, Yufei Wang, Jake Olkin, and David Held.
+Softgym: Benchmarking deep reinforcement learning for
+deformable object manipulation. InCoRL, 2021.
+[17] Jindi Lv, Hao Li, Jie Li, Yifei Nie, Fankun Kong, Yang
+Wang, Xiaofeng Wang, Zheng Zhu, Chaojun Ni, Qiuping
+Deng, et al. Viva: A video-generative value model for
+robot reinforcement learning.arXiv.org, 2604.08168.
+[18] Yecheng Jason Ma, Vikash Kumar, Amy Zhang, Osbert
+Bastani, and Dinesh Jayaraman. Liv: Language-image
+representations and rewards for robotic control. InICML,
+2023.
+[19] Yecheng Jason Ma, Shagun Sodhani, Dinesh Jayaraman,
+Osbert Bastani, Vikash Kumar, and Amy Zhang. Vip:
+Towards universal visual reward and representation via
+value-implicit pre-training. InICLR, 2023.
+[20] Yecheng Jason Ma, Joey Hejna, Chuyuan Fu, Dhruv
+Shah, Jacky Liang, Zhuo Xu, Sean Kirmani, Peng Xu,
+Danny Driess, Ted Xiao, et al. Vision language models
+are in-context value learners. InICLR, 2025.
+[21] Nagarajan Natarajan, Inderjit S Dhillon, Pradeep K
+Ravikumar, and Ambuj Tewari. Learning with noisy
+labels. InNeurIPS, 2013.
+[22] Xue Bin Peng, Aviral Kumar, Grace Zhang, and Sergey
+Levine. Advantage-weighted regression: Simple and
+scalable off-policy reinforcement learning.arXiv.org,
+1910.00177.
+[23] Pierre Sermanet, Corey Lynch, Yevgen Chebotar, Jas-
+mine Hsu, Eric Jang, Stefan Schaal, Sergey Levine,
+and Google Brain. Time-contrastive networks: Self-
+supervised learning from video. InICRA, 2018.
+[24] Sumedh Sontakke, Jesse Zhang, S ´eb Arnold, Karl
+Pertsch, Erdem Bıyık, Dorsa Sadigh, Chelsea Finn, and
+Laurent Itti. Roboclip: One demonstration is enough to
+learn robot policies. InNeurIPS, 2023.
+[25] Gemini Robotics Team, Abbas Abdolmaleki, Saminda
+Abeyruwan, Joshua Ainslie, Jean-Baptiste Alayrac,
+Montserrat Gonzalez Arenas, Ashwin Balakrishna,
+Nathan Batchelor, Alex Bewley, Jeff Bingham, et al.
+Gemini robotics 1.5: Pushing the frontier of generalist
+robots with advanced embodied reasoning, thinking, and
+motion transfer.arXiv.org, 2510.03342.
+[26] Michael Tschannen, Alexey Gritsenko, Xiao Wang,
+Muhammad Ferjad Naeem, Ibrahim Alabdulmohsin,
+Nikhil Parthasarathy, Talfan Evans, Lucas Beyer, Ye Xia,
+Basil Mustafa, et al. Siglip 2: Multilingual vision-
+language encoders with improved semantic under-
+standing, localization, and dense features.arXiv.org,
+2502.14786.
+[27] Checheng Yu, Chonghao Sima, Gangcheng Jiang, Hai
+Zhang, Haoguang Mai, Hongyang Li, Huijie Wang, Jin
+Chen, Kaiyang Wu, Li Chen, et al.χ 0: Resource-aware
+robust manipulation via taming distributional inconsis-
+tencies.arXiv.org, 2602.09021.
+[28] Tony Z Zhao, Vikash Kumar, Sergey Levine, and Chelsea
+Finn. Learning fine-grained bimanual manipulation with
+low-cost hardware. InRSS, 2023.
+[29] Xiaojin Zhu, Zoubin Ghahramani, and John Lafferty.
+Semi-supervised learning using gaussian fields and har-
+monic functions. InICML, 2003.
```
