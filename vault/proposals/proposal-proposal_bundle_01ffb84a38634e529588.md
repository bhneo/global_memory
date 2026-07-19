---
id: "proposal_bundle_01ffb84a38634e529588"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-19T01:40:12+08:00"
updated_at: "2026-07-19T01:40:12+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_c79f943c818d06054ca5cf92"]
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
extraction_id: "extraction_e62bd6b73d0d7d66a185bfc3"
input_sha256: "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
bundle_items: [{"item_id": "experiment-1", "object_type": "experiment", "action": "create", "target_id": "experiment_305648b9377f92e9f4ef9a5f", "target_path": "vault/action/experiments/experiment_305648b9377f92e9f4ef9a5f-the-policy-is-initialized-from-the-same-act-model.md", "base_sha256": null, "candidate_sha256": "ae762ac2eddaafbde21e38d7da883ed626f0f78c4981b75d37cef9124e0fca05", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_01ffb84a38634e529588-experiment-1.md", "base_path": null, "working_path": "vault/memory/experiment/experiment_305648b9377f92e9f4ef9a5f.md", "working_at": "2026-07-19T01:40:12+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "# “How would j’s [action] change if I had acted\n\n“How would j’s [action] change if I…", "match_reason": "metadata:title"}, {"id": "architecture_929a68a1fd830b00f780f138", "type": "architecture", "title": "the policy attends to memory through its existing token-processing pipeline.", "path": "vault/memory/architecture/architecture_929a68a1fd830b00f780f138.md", "status": "working", "source_ids": ["source_748cef2215ddc958568e6368"], "snippet": "…Given the augmented token sequencext, the frozen\nVLA predicts the target [action] using its original [action] head, and…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_c79f943c818d06054ca5cf92"}
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
- Extraction：`extraction_e62bd6b73d0d7d66a185bfc3`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### experiment-1 (create experiment)

```diff
--- /dev/null
+++ candidate:vault/action/experiments/experiment_305648b9377f92e9f4ef9a5f-the-policy-is-initialized-from-the-same-act-model.md
@@ -0,0 +1,257 @@
+---
+id: "experiment_305648b9377f92e9f4ef9a5f"
+type: "experiment"
+status: "proposal"
+title: "the policy is initialized from the same ACT model"
+created_at: "2026-07-19T01:40:12+08:00"
+updated_at: "2026-07-19T01:40:12+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_c79f943c818d06054ca5cf92"]
+relations: [{"type": "derived_from", "target_id": "source_c79f943c818d06054ca5cf92", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_c79f943c818d06054ca5cf92"
+---
+
+# the policy is initialized from the same ACT model
+
+the policy is initialized from the same ACT model
+
+pretrained on 800 episodes, the initial pose is randomized
+within±2cm, the training limit is set to 10000 episodes,
+and the hybrid KL behavior-prior constraint is retained. No
+additional demonstration trajectory replay or demonstration-
+action supervision is used during training.
+As shown in Fig. 7, under this setting PAC-ACT with
+β1 = 3.0still converges to a 100% rollout success rate and
+maintains a structured trajectory close to the contour action
+sequence, indicating that the pretrained action chunking policy
+provides a strong behavior prior for chunk-level PPO. As a
+comparison, we set the KL coefficient to zero (β 1 = 0) under
+the same sparse-reward setting. Qualitative video playback
+and end-effector trajectory sampling show that this policy
+deviates from the pretrained ACT contour temporal action
+sequence early in training and instead forms shortcut behavior
+
+<!-- page: 11 -->
+
+Fig. 7. Training success rate and end-effector trajectory structure diagnosis
+in the sparse-reward ablation. Left: rollout success-rate curves under different
+reward and regularization configurations on the Contour task; shaded regions
+indicate local fluctuations, and the dashed line marks the 95% success-
+rate threshold. Right: top-view trajectory from one validation rollout for the
+corresponding policy, where blue points visualize the end-effector trajectory
+sampled uniformly by arc length. When only the success reward is retained
+but the KL constraint is kept, the policy maintains structured motion close to
+the contour action sequence. When the KL constraint is removed under the
+same sparse-reward condition, later rollout success can partially recover, but
+the sampled end-effector points show a clearly dispersed boundary-touching
+exploration pattern, indicating that success-rate metrics may mask degradation
+of temporal structure.
+that directly touches multiple target boundaries to obtain
+the success reward. Because this behavior can still trigger
+the sparse success condition, the later local rollout window
+reaches a maximum success rate of 88.5%; however, under
+the same training limit, the cumulative total success rate
+is only 22.0%, and the final rollout window also drops to
+72.7%. Therefore, the success-rate rebound without KL does
+not indicate recovery of structured contact skills, but instead
+shows that relying only on sparse success metrics can obscure
+degradation of temporal structure. This comparison indicates
+that KL regularization is a key mechanism for maintaining
+the pretrained behavior manifold and preventing structured
+behavior collapse under sparse rewards.
+V. DISCUSSION
+The experiments reveal a paradigm in which imitation learn-
+ing provides a behavior prior and reinforcement learning per-
+forms behavior customization, consistent with the basic idea of
+recent RL fine-tuning studies on pretrained policies [19]–[21],
+[24]. The behavior cloning stage learns basic contact skills
+and temporal action structure, while the RL stage selectively
+refines these skills through environmental reward feedback,
+improving task success, force safety, and time efficiency
+while preserving the basic behavior structure. The ablations
+in Sec. IV-I further validate the design at the architectural
+level: the encoder-value Critic outperforms the flat-decoder
+critic in final-window mean success rate (96.4% vs. 88.0%)
+and stability (±3.0% vs.±7.4%) with lower computational
+overhead; removing the CV AE avoids conflict between an
+additional stochasticity source and the KL constraint, while
+the CV AE-retained actor achieves only an 83.1% final-window
+mean, further supporting the design choice.
+Pretrained action chunking policies can reduce sensitivity
+to reward engineering during RL, but this does not mean
+that the main method does not require dense rewards. The
+main experiments use dense rewards to obtain the best task
+completion efficiency and force safety, while the sparse-reward
+experiment is only an additional ablation. The results show
+that, when the KL constraint and frozen baseline policy
+constraint are retained, keeping only the success bonus still
+allows convergence under randomized initial poses; when KL
+is removed, local success may partially recover, but the end-
+effector trajectory structure clearly degrades. This indicates
+that the pretrained action chunking policy provides a strong
+low-level behavior prior, and that the behavior-prior constraint
+is critical for preventing collapse of structured contact skills
+under sparse rewards.
+The force-safety results deserve particular attention. The
+substantial reduction in extreme force events, with the peak
+force decreasing from 8452.5N to 120.9N, shows that a
+pretrained ACT policy can produce unsafe forces in a non-
+negligible fraction of episodes even when it achieves a rea-
+sonable task success rate. Such events may be missed in pure
+BC evaluation because (a) they occur in out-of-distribution
+states that BC evaluation may not systematically probe, and (b)
+they do not necessarily cause immediate task failure: a policy
+may generate unsafe force while still completing part or all
+of the task. RL fine-tuning with an appropriate safety reward
+provides a principled mechanism for detecting and mitigating
+such hidden failures, which is relevant to industrial scenarios
+with strict contact-safety requirements.
+This study has several limitations. The experiments are
+mainly conducted in simulation, and sim-to-real transfer of
+the learned policy remains to be validated. The current exper-
+iments primarily examine object initial-position perturbations
+and multi-trajectory generalization, but do not cover visual
+or physical perturbations such as viewpoint changes, lighting
+variation, or dynamics-parameter changes. A more systematic
+robustness evaluation is left for future work. Although re-
+moving the CV AE module simplifies RL optimization, it may
+limit the ability of the policy to represent highly multi-modal
+action distributions. Future work can explore regularized
+CV AE integration that preserves multimodality while main-
+taining optimization stability. Finally, the current framework
+still requires task-specific reward design; developing more
+automated reward specification methods would further reduce
+the engineering burden of RL-based policy customization.
+VI. CONCLUSION
+This paper presents PAC-ACT, a chunk-level PPO post-
+training framework for pretrained ACT policies. Through
+MDP reformulation, ACT-transferred Actor-Critic design, and
+hybrid KL constraints, PAC-ACT structurally aligns action
+chunking policies with RL optimization. On Metal Touch
+and Square Assembly, the method improves task success
+(Contour 60%→100%, Square 51.2%→98.2%) and execution
+efficiency, reducing completion steps by 2.8 times. Dedicated
+force-safety analysis shows that hazardous force events are
+
+<!-- page: 12 -->
+
+reduced by 46 times and peak contact force by 70 times.
+All improvements are achieved while maintaining low latency
+and low GPU memory usage (88.1±23.4ms inference, 2.30GB
+GPU memory), indicating the potential of the method for fur-
+ther adaptation and deployment in industrial precision contact
+scenarios.
+Future work will extend the evaluation to real robot plat-
+forms to validate sim-to-real transfer, explore more complex
+multi-stage manipulation tasks, and investigate more general
+reward design mechanisms that can further reduce the engi-
+neering cost of RL-based policy customization.
+REFERENCES
+[1] F. Chaumette and S. Hutchinson, “Visual servo control. I. Basic ap-
+proaches,”IEEE Robotics & Automation Magazine, vol. 13, no. 4, pp.
+82–90, 2006, doi: 10.1109/MRA.2006.250573.
+[2] V . Kyrki, D. Kragic, and H. I. Christensen, “Measurement errors in
+visual servoing,”Robotics and Autonomous Systems, vol. 54, no. 10,
+pp. 815–827, 2006, doi: 10.1016/j.robot.2006.05.002.
+[3] T. Z. Zhao, V . Kumar, S. Levine, and C. Finn, “Learning fine-grained
+bimanual manipulation with low-cost hardware,” inProc. Robotics:
+Science and Systems (RSS), 2023.
+[4] S. Ross, G. Gordon, and D. Bagnell, “A reduction of imitation learning
+and structured prediction to no-regret online learning,” inProc. Inter-
+national Conference on Artificial Intelligence and Statistics (AISTATS),
+PMLR, vol. 15, pp. 627–635, 2011.
+[5] A. Mandlekar, D. Xu, J. Wong, S. Nasiriany, C. Wang, R. Kulkarni,
+L. Fei-Fei, et al., “What matters in learning from offline human
+demonstrations for robot manipulation,” inProc. Conference on Robot
+Learning (CoRL), PMLR, vol. 164, pp. 1678–1690, 2022.
+[6] M. Suomalainen, Y . Karayiannidis, and V . Kyrki, “A survey of robot
+manipulation in contact,”Robotics and Autonomous Systems, vol. 156,
+Art. no. 104224, 2022, doi: 10.1016/j.robot.2022.104224.
+[7] N. Hogan, “Impedance control: An approach to manipulation: Part I—
+Theory,”Journal of Dynamic Systems, Measurement, and Control, vol.
+107, no. 1, pp. 1–7, 1985, doi: 10.1115/1.3140702.
+[8] D. Tian, O. Celik, and G. Neumann, “Chunking the critic: A
+transformer-based soft actor-critic with n-step returns,” arXiv preprint
+arXiv:2503.03660, 2025.
+[9] Q. Li, Z. Zhou, and S. Levine, “Reinforcement learning with action
+chunking,” inProc. Advances in Neural Information Processing Systems
+(NeurIPS), 2025.
+[10] R. Cadene, S. Alibert, F. Capuano, M. Aractingi, A. Zouitine, P.
+Kooijmans, et al., “LeRobot: An open-source library for end-to-end
+robot learning,” inProc. International Conference on Learning Rep-
+resentations (ICLR), 2026.
+[11] K. Sohn, H. Lee, and X. Yan, “Learning structured output representation
+using deep conditional generative models,” inProc. Advances in Neural
+Information Processing Systems (NeurIPS), 2015.
+[12] C. Chi, S. Feng, Y . Du, Z. Xu, E. Cousineau, B. Burchfiel, and S. Song,
+“Diffusion policy: Visuomotor policy learning via action diffusion,” in
+Proc. Robotics: Science and Systems (RSS), 2023.
+[13] N. M. Shafiullah, Z. Cui, A. Altanzaya, and L. Pinto, “Behavior
+transformers: Cloningkmodes with one stone,” inProc. Advances in
+Neural Information Processing Systems (NeurIPS), 2022.
+[14] B. Zitkovich et al., “RT-2: Vision-language-action models transfer web
+knowledge to robotic control,” inProc. Conference on Robot Learning
+(CoRL), PMLR, vol. 229, pp. 2165–2183, 2023.
+[15] Physical Intelligence, K. Black, N. Brown, J. Darpinian, et al., “π0.5:
+a vision-language-action model with open-world generalization,” arXiv
+preprint arXiv:2504.16054, 2025.
+[16] P. Florence, C. Lynch, A. Zeng, et al., “Implicit behavioral cloning,” in
+Proc. Conference on Robot Learning (CoRL), 2021.
+[17] Y . Seo and P. Abbeel, “Coarse-to-fine Q-network with action se-
+quence for data-efficient reinforcement learning,” arXiv preprint
+arXiv:2411.12155, 2024.
+[18] T. Haarnoja et al., “Soft actor-critic: Off-policy maximum entropy deep
+reinforcement learning with a stochastic actor,” inProc. International
+Conference on Machine Learning (ICML), 2018.
+[19] J. Yang, B. Zhu, J. Chen, and Y .-G. Jiang, “Actor-critic for continuous
+action chunks: A reinforcement learning framework for long-horizon
+robotic manipulation with sparse reward,” inProc. AAAI Conference on
+Artificial Intelligence (AAAI), vol. 40, no. 22, pp. 18692–18700, 2026,
+doi: 10.1609/aaai.v40i22.38937.
+[20] A. Kumar, A. Zhou, G. Tucker, and S. Levine, “Conservative Q-
+learning for offline reinforcement learning,” inProc. Advances in Neural
+Information Processing Systems (NeurIPS), 2020.
+[21] I. Kostrikov, A. Nair, and S. Levine, “Offline reinforcement learning
+with implicit Q-learning,” inProc. International Conference on Learning
+Representations (ICLR), 2022.
+[22] L. Brunke, M. Greeff, A. W. Hall, Z. Yuan, S. Zhou, J. Panerati, and A.
+P. Schoellig, “Safe learning in robotics: From learning-based control to
+safe reinforcement learning,”Annual Review of Control, Robotics, and
+Autonomous Systems, vol. 5, pp. 411–444, 2022, doi: 10.1146/annurev-
+control-042920-020211.
+[23] Open X-Embodiment Collaboration, A. O’Neill, A. Rehman,
+et al., “Open X-Embodiment: Robotic learning datasets and
+RT-X models,” inProc. IEEE International Conference on
+Robotics and Automation (ICRA), pp. 6892–6903, 2024, doi:
+10.1109/ICRA57147.2024.10611477.
+[24] A. Z. Ren, J. Lidard, L. L. Ankile, A. Simeonov, P. Agrawal, A.
+Majumdar, et al., “Diffusion policy policy optimization,” arXiv preprint
+arXiv:2409.00588, 2024.
+[25] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
+recognition,” inProc. IEEE/CVF Conference on Computer Vision and
+Pattern Recognition (CVPR), 2016.
+[26] A. Vaswani et al., “Attention is all you need,” inProc. Advances in
+Neural Information Processing Systems (NeurIPS), 2017.
+[27] S. Nair, A. Rajeswaran, V . Kumar, C. Finn, and A. Gupta, “R3M:
+A universal visual representation for robot manipulation,” inProc.
+Conference on Robot Learning (CoRL), PMLR, vol. 205, pp. 892–909,
+2023.
+[28] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Prox-
+imal policy optimization algorithms,” arXiv preprint arXiv:1707.06347,
+2017.
+[29] J. Schulman, S. Levine, P. Abbeel, M. Jordan, and P. Moritz, “Trust re-
+gion policy optimization,” inProc. International Conference on Machine
+Learning (ICML), 2015.
+[30] E. Todorov, T. Erez, and Y . Tassa, “MuJoCo: A physics engine for
+model-based control,” inProc. IEEE/RSJ International Conference on
+Intelligent Robots and Systems (IROS), 2012.
+[31] Y . Zhu, J. Wong, A. Mandlekar, R. Martin-Martin, A. Joshi, K. Lin,
+et al., “robosuite: A modular simulation framework and benchmark for
+robot learning,” arXiv preprint arXiv:2009.12293, 2020.
+[32] Y . Yue, Y . Wang, B. Kang, Y . Han, S. Wang, S. Song, J. Feng, and G.
+Huang, “DeeR-VLA: Dynamic inference of multimodal large language
+models for efficient robot execution,” inProc. Advances in Neural
+Information Processing Systems (NeurIPS), 2024.
```
