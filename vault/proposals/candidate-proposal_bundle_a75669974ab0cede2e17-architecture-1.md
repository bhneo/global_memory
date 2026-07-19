---
id: "architecture_929a68a1fd830b00f780f138"
type: "architecture"
status: "proposal"
title: "the policy attends to memory through its existing token-processing pipeline."
created_at: "2026-07-19T01:30:41+08:00"
updated_at: "2026-07-19T01:30:41+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_748cef2215ddc958568e6368"]
relations: [{"type": "derived_from", "target_id": "source_748cef2215ddc958568e6368", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
change_reason: "compile bundle from source_748cef2215ddc958568e6368"
---

# the policy attends to memory through its existing token-processing pipeline.

the policy attends to memory through its existing token-processing pipeline.

We learn these native memory tokens in a first-stage alignment procedure. The pretrained VLA is
frozen, and only the memory branch is trainable. Given the augmented token sequencext, the frozen
VLA predicts the target action using its original action head, and the memory branch is optimized
by the native VLA action loss:
min
ϕmem,qmem,Wmem,bmem
E(Ht,ot,st,ℓ,at) [Lact (πθ(· |ot, st, ℓ,Mt),a t)],(9)
whereθis fixed andϕ mem denotes the parameters of the memory encoder. Since gradients can only
update the memory branch, the learned tokens are encouraged to encode information that is both
action-relevant and aligned with the frozen VLA’s pretrained token space.
For training efficiency, we do not load the full visual history. Instead, for each training step,I t
consists of the first frame of the episode and a recent history window. The first frame provides
coarse task initialization context, while the recent window captures state changes and progress. We
also include the current frame inI t, so that the tokenizer learns a unified frame-level summarization
behavior for both current and past observations. Our memory tokenizer is trained on a mixture of
simulation and real-world demonstrations covering both standard manipulation data and memory-
demanding tasks, and could be reused for downstream memory-augmented finetuning.
3.3 Task-Specific Finetuning and Real-Time Memory Inference
Task-specific finetuning.Given a target-task demonstration dataset, we first use the learned mem-
ory tokenizer to preprocess the visual history offline. For each episode, every frame from each
camera view is converted into its corresponding memory summary tokenˆq v
τ . Since each frame-
view pair is represented by only one token, this preprocessing introduces negligible storage and I/O
overhead compared with storing dense visual token sequences.
For each training stept, we retrieve the cached summary tokens from selected frame indicesI t with
τ≤t, and form the memory sequence following Eq. 7. The resulting memory sequence is appended
to the standard VLA input as in Eq. 8.
We initialize the VLA backbone from the pretrained single-frame policy and loadW mem andb mem
from the first-stage memory branch. The memory tokenizer encoder is kept fixed during this stage,
while the VLA backbone, action head, and memory projection are finetuned on limited target-task
demonstrations using the native action prediction loss:
min
θ′,Wmem,bmem
E(ot,st,ℓ,Mt,at) [Lact (πθ′(· |ot, st, ℓ,Mt),a t)].(10)
Here,θ ′ denotes the finetuned VLA parameters. This preserves the standard VLA finetuning work-
flow while extending the policy with compact historical context.
Real-time memory inference.During deployment, the memory tokenizer can operate indepen-
dently from the VLA policy. As new observations arrive, the tokenizer converts them into memory
5

<!-- page: 6 -->

✅
 ✅
✅
 ✅
✅
✅
(a) Click ButtonsPress BluePress Pink Press YellowStop and Don’t Repeat
(b) Put Back BlockPut into Central Area Put Backto Original Pad
(c) Checkout Scanning (unseen)Stop and Don’t Repeat
Stop and Don’t Repeat
Which ones have been scanned?Which ones have been scanned?
Which is the original pad?
Which stage?Which stage?
✅
 ✅
✅
 ✅
✅
✅
Figure 3:Memory-dependent manipulation tasks.InClick Buttons, the robot must follow a
specified button sequence without repeating completed presses. InPut Back Block, it must remember
the block’s original pad after moving it to the center. InGrocery Checkout Scanning, it must track
which items have already been scanned and avoid duplicate or missed scans.
tokens at a specified update frequency and maintains a compact memory queue. Since the tokenizer
is derived from the original visual encoder and produces only one token per frame-view pair, mem-
ory updates can be performed with low overhead and do not require modifying the VLA inference
pipeline. When the VLA is queried for an action, the current observation, proprioceptive state, and
language instruction are processed as usual. The current memory queue is simply concatenated after
the original input tokens, following Eq 8. Thus, memory construction and policy inference are de-
coupled: the tokenizer can update historical memory at a high frequency, while the VLA consumes
the latest compact memory sequence whenever action prediction is required.
4 Experiments
4.1 Experimental Setup
Datasets and Tasks.We evaluate NATIVEMEM on memory-dependent manipulation tasks in both
simulation and the real world. For real-world evaluation, we consider three tasks, as illustrated in
Fig. 3. Notably,Grocery Checkout Scanning (unseen)is not included during first-stage memory-
tokenizer training. This setting evaluates whether the learned native memory representation trans-
fers to new forms of long-horizon task progress tracking. In simulation, we use three RMBench
tasks [21] and two additional button-pressing tasks. The simulatedClick Buttonstask follows the
same memory requirement as its real-world counterpart, whileClick Buttons (Hard)removes color
distinctions between buttons, forcing the policy to rely on spatial memory and interaction history.
Baselines.We compare NATIVEMEM with representative VLA policies that instantiate different
memory-modeling paradigms. ForVLM-driven memory, we include MemER [19] and Mem-0 [21].
Forexternal memory modules, we include HAMLET [26] and MEM-short [20]. For a fair compar-
ison, we implement both HAMLET and MEM-short on the sameπ 0.5 backbone used by NATIVE-
MEM. Since HAMLET and MEM-short are not publicly released, we faithfully reproduce them
following the official papers. MEM-short is originally designed to be retrained on large-scale data.
To ensure a controlled comparison, we train it using the same demonstration trajectories available to
all methods. Therefore mark them as HAMLET∗ and MEM-short∗ in Tab. 1 and 2.
4.2 Main Results
Simulation Experiments.As shown in Tab. 1, NATIVEMEM achieves the best performance across
all tasks, improving the average success rate to84.0%. The evaluated tasks cover two comple-
mentary memory requirements: long-range recall of early observations, as inPut Back Blockand
6

<!-- page: 7 -->

Method Click Buttons Click Buttons (hard) Swap Blocks Put Back Block Observe and Pickup Avg.
Base VLA Policies
π0.5[4] 0 0 24 11 9 8.8
X-VLA [55] 7 12 16 18 9 12.4
VLM-Driven Memory
MemER [19] 12 8 18 12 2 10.4
Mem-0 [21] 0 1 67 90 4 32.4
Externel Memory Modules
HAMLET∗ [26] 4 17 11 3 10 9.0
MEM-short∗ [20] 0 39 4 15 6 12.8
Ours 94 88 94 100 44 84.0
Table 1: Task success rates (%) in simulation evaluation. The benchmark includes three RMBench
tasks and two additional simulated button-pressing tasks. NATIVEMEM achieves the best perfor-
mance across all tasks. The best result for each task is marked inbold. ∗ indicates reproduced
baselines implemented on the sameπ 0.5 backbone.
Method Click Buttons Put Back Block Grocery Checkout Scanning (unseen)Avg.S1 S2 S3 S1 S2 S1 S2 S3
π0.5[4] 16 8 2 72 14 90 58 28 14.7
π0.5+ RTC [56] 26 18 16 56 24 74 66 64 34.7
Mem-0 [21] 36 4 0 0 0 6 0 0 0.0
MEM-short∗[20] 72 52 40 6 0 72 56 52 30.7
Ours 100 98 96 100 100 100 100 100 98.7
Table 2: Real-world cumulative task success rates (%). S1-S3 denote cumulative success after each
task stage; the last stage corresponds to the overall task success rate.Grocery Checkout Scanning
is unseen during first-stage memory-tokenizer training. The mean overall success rate is reported.
The best results are marked inbold. ∗ denotes reproduced baselines trained with the same number
of task-specific demonstrations as NATIVEMEM.
Observe and Pickup, and continuous progress tracking, as inClick Buttons,Click Buttons (Hard),
andSwap Blocks. Existing VLM-driven or short-horizon memory methods struggle with one or both
settings, while NATIVEMEM remains consistently effective, suggesting its native memory compres-
sion provides a unified representation for both recalling visual evidence and tracking task states.
Real-World Experiments.Tab. 2 shows that NATIVEMEM also transfers effectively to real-robot
manipulation, achieving the highest overall success rate across all tasks. While RTC improves
over theπ 0.5 policy by exploiting temporal action continuity, rather than explicitly remembering
past observations. Its performance still drops in later stages that require explicit historical recall.
MEM-short∗ becomes less stable under limited real-world data, occasionally degrading the pre-
trained VLA’s manipulation capability. In contrast, NATIVEMEM preserves the pretrained policy
prior while adding compact history, achieving the strongest performance across all three tasks.
(b) Data Efficiency(a) Inference Efficiency
607179
1731
54
020406080100
102550Number of Demonstrations
Avg. Success Rate (%)
Mem-0Ours
Figure 4: (a) Inference latency and memory consumption.
(b) Average data efficiency on three RMBench tasks.
Inference Efficiency.Fig. 4(a) com-
pares inference latency and peak
GPU memory under increasing his-
tory length. Our NATIVEMEM sup-
ports up to 5,000 historical frames
within a 32 GB memory budget, and
still attends to about 200 frames un-
der a 100 ms real-time latency con-
straint, enabling substantially longer
histories while preserving the real-
time reactiveness.
Data-Efficiency.Fig. 4(b) shows
that NATIVEMEM adapts effectively
with limited demonstrations. With only 10 demonstrations, it reaches60%average success,3.5×
higher than Mem-0, and consistently outperforms Mem-0 with 25 and 50 demonstrations, reflecting
the benefit of reusing pretrained VLA manipulation priors.
7

<!-- page: 8 -->

(a) Click Buttons (b) Put Back Block
Stage1: Click BlueStage2: Click PinkStage3: Click YellowStage1: PickupInfer and Determine Target Pad
Figure 6: Visualization of attention from action tokens to historical memory snapshots. The x-
axis denotes the timestamp of each memory snapshot, and the y-axis denotes the action prediction
timestep. Each row shows which memories are used for a given action prediction time, while each
column indicates how a specific memory is attended by future predictions. The attention inClick
Buttonsfollows the three clicking stages, while inPut Back Blockit concentrates on the pickup
moment needed to infer the target pad.
Method Click Button Click Button (hard) Swap Blocks Put Back Block Observe and Pickup Avg.
Unfrozen VLA 38 24 45 0 9 23.2
w/o Stage1 94 80 92 17 7 58.0
Sparse update (0.5Hz) 83 63 91 24 9 53.8
Short horizon (2s) 26 87 0 18 39 34.0
Short horizon (4s) 69 87 0 18 37 43.0
Short horizon (6s) 80 88 0 18 44 46.0
Ours 94 88 94 100 44 84.0
Table 3:Ablation Study on Native Memory Compression and its Temporal Coverage.The first
two variants evaluate the memory-compression learning, while the remaining variants examine the
importance of long-horizon and fine-grained history. The best results are marked inbold.
4.3 Qualitative Analysis: What Does Native Memory Capture?
Spatial Attention of the Memory Tokenizer.
(a) Put Back Block(b) Grocery Checkout Scanning (unseen)
Figure 5:Visualization of the spatial attention used by
the memory tokenizer when compressing each frame-
view observation into a single memory token. The top
row shows the tokenizer attention maps over input im-
ages, while the bottom row shows the corresponding
raw observations.
To understand what is encoded into each mem-
ory token, we visualize the tokenizer’s spa-
tial attention over historical observations. As
shown in Fig. 5, the tokenizer consistently fo-
cuses on manipulation-relevant regions rather
than background pixels. ForPut Back Blocks,
attention concentrates on the block and its
corresponding pad. Notably, this behavior
also generalizes toGrocery Checkout Scanning,
which is unseen during tokenizer training: the
tokenizer still attends to foreground objects, es-
pecially the item about to be grasped.
Action Attention over the Memory Se-
quence.To examine how NATIVEMEM uses history during action generation, we visualize the
attention from action tokens to memory tokens across inference time. Fig. 6 shows that the policy
attends to task-relevant moments rather than simply the most recent observations. InClick Buttons,
high-attention memories align with the three timesteps when individual buttons were pressed. InPut
Back Block, attention concentrates on the moment when the block was lifted from its original pad,
which is critical for deciding where to return it.
4.4 Ablation Study
Native Memory Compression.As shown in Tab. 3 (lines 1 and 2), when the VLA is unfrozen
during memory-compression learning, performance drops to23.2%. The model reduces the action
8

<!-- page: 9 -->

loss by directly adapting the pretrained VLA itself rather than forcing the memory branch. After
skipping Native Memory Compression, mean-pooled vision-encoder features are used as memory
tokens. The results show that such generic visual features can capture coarse historical context, but
fail to preserve details required by tasks such asPut Back BlockandObserve and Pickup. These
results indicate that Native Memory Compression is essential for distilling task-relevant historical
cues, enabling the policy to recover critical information needed for downstream action prediction.
Temporal Memory Coverage.Sparse update at0.5Hz broadly reduces success rates, showing that
the policy needs fine-grained temporal evidence to track interaction states. Short horizons degrade
tasks whose critical information falls outside the retained window, such asSwap BlocksandPut Back
Block. Results in Tab. 3 (lines 4∼6) show that NATIVEMEM’s performance relies on both dense
temporal coverage and long-horizon retention: it updates memory frequently enough to capture fine-
grained interaction changes, while its compact native tokens make minute-level history retention
scalable.
5 Conclusion
We presented NATIVEMEM, which enables pretrained single-frame VLAs to retain long-horizon,
fine-grained visual histories throughNative Memory Compression. By repurposing the VLA’s own
vision encoder, NATIVEMEM achieves one-token-per-frame compression. We further introduced a
two-stage training pipeline that first learns an action-supervised memory tokenizer aligned with
the pretrained VLA’s visual-action priors, and then performs task-specific finetuning with limited
demonstrations. Across simulation and real-world manipulation tasks, NATIVEMEM substantially
improves average success rates from 32.4% to 84.0% in simulation and from 34.7% to 98.7% on
real robots, while matching leading memory-designed methods with only 20% of the training data.
6 Limitations
While NATIVEMEM enables dense minute-level visual memory for long-horizon manipulation, it
is not designed to maintain persistent memories over hours or days. Supporting such long-term con-
tinuity will likely require additional system-level memory infrastructure. In addition, our memory
tokenizer is learned solely through action supervision. Although we have not observed clear failures
in our preliminary exploration, more complex tasks may expose a semantic gap between low-level
action losses and higher-level, abstract memory requirements. Exploring more direct and scalable
objectives for learning the relationship between memory and action remains an important direction.
9

<!-- page: 10 -->

References
[1] B. Zitkovich, T. Yu, S. Xu, P. Xu, T. Xiao, F. Xia, J. Wu, P. Wohlhart, S. Welker, A. Wahid,
et al. RT-2: Vision-language-action models transfer web knowledge to robotic control. In
Conference on Robot Learning, 2023.
[2] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster,
G. Lam, P. Sanketi, et al. OpenVLA: An open-source vision-language-action model.arXiv
preprint arXiv:2406.09246, 2024.
[3] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman,
B. Ichter, et al.π 0: A vision-language-action flow model for general robot control.arXiv
preprint arXiv:2410.24164, 2024.
[4] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi,
C. Finn, N. Fusai, et al.π 0.5: a vision-language-action model with Open-World generalization.
arXiv preprint arXiv:2504.16054, 2025.
[5] Q. Bu, Y . Yang, J. Cai, S. Gao, G. Ren, M. Yao, P. Luo, and H. Li. UniVLA: Learning to act
anywhere with task-centric latent actions.arXiv preprint arXiv:2505.06111, 2025.
[6] G. Team, A. Ye, B. Wang, C. Ni, G. Huang, G. Zhao, H. Li, J. Li, J. Zhu, L. Feng,
et al. GigaBrain-0: A world model-powered vision-language-action model.arXiv preprint
arXiv:2510.19430, 2025.
[7] C. Ni, C. Chen, X. Wang, Z. Zhu, W. Zheng, B. Wang, T. Chen, G. Zhao, H. Li, Z. Dong,
et al. SwiftVLA: Unlocking spatiotemporal dynamics for lightweight vla models at minimal
overhead.CVPR 2026, 2026.
[8] A. Ye, B. Wang, C. Ni, G. Huang, G. Zhao, H. Li, H. Li, J. Li, J. Lv, J. Liu, et al. GigaWorld-
Policy: An efficient action-centered world–action model.arXiv preprint arXiv:2603.17240,
2026.
[9] H. Jang, S. Yu, H. Kwon, H. Jeon, Y . Seo, and J. Shin. ContextVLA: Vision-Language-Action
model with amortized multi-frame context.arXiv preprint arXiv:2510.04246, 2025.
[10] J. Zhang, Y . Chen, Y . Xu, Z. Huang, Y . Zhou, Y .-J. Yuan, X. Cai, G. Huang, X. Quan, H. Xu,
et al. 4D-VLA: Spatiotemporal vision-language-action pretraining with cross-scene calibra-
tion.arXiv preprint arXiv:2506.22242, 2025.
[11] L. Beyer, A. Steiner, A. S. Pinto, A. Kolesnikov, X. Wang, D. Salz, M. Neumann, I. Alabdul-
mohsin, M. Tschannen, E. Bugliarello, et al. PaliGemma: A versatile 3b VLM for transfer.
arXiv preprint arXiv:2407.07726, 2024.
[12] A. Marafioti, O. Zohar, M. Farr ´e, M. Noyan, E. Bakouch, P. Cuenca, C. Zakka, L. B. Allal,
A. Lozhkov, N. Tazi, et al. SmolVLM: Redefining small and efficient multimodal models.
arXiv preprint arXiv:2504.05299, 2025.
[13] S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, et al.
Qwen2.5-VL technical report.arXiv preprint arXiv:2502.13923, 2025.
[14] S. Zhou, A. Vilesov, X. He, Z. Wan, S. Zhang, A. Nagachandra, D. Chang, D. Chen, X. E.
Wang, and A. Kadambi. VLM4D: Towards spatiotemporal awareness in vision language mod-
els. InProceedings of the IEEE/CVF international conference on computer vision, 2025.
[15] Z. He, Y . Wang, C. Zhi, Y . Hu, T.-P. Chen, L. Yin, Z. Chen, T. A. Wu, S. Ouyang, Z. Wang,
et al. MemoryArena: Benchmarking agent memory in interdependent multi-session agentic
tasks.arXiv preprint arXiv:2602.16313, 2026.
10

<!-- page: 11 -->

[16] M. Lauri, D. Hsu, and J. Pajarinen. Partially observable markov decision processes in robotics:
A survey.IEEE Transactions on Robotics, 2022.
[17] Y . Wu, S. Liang, C. Zhang, Y . Wang, Y . Zhang, H. Guo, R. Tang, and Y . Liu. From human
memory to AI memory: A survey on memory mechanisms in the era of LLMs.arXiv preprint
arXiv:2504.15965, 2025.
[18] M. Zhai, Z. Gao, Y . Wu, and Y . Jia. Memory-Centric embodied question answering.arXiv
preprint arXiv:2505.13948, 2025.
[19] A. Sridhar, J. Pan, S. Sharma, and C. Finn. MemER: Scaling up memory for robot control via
experience retrieval.arXiv preprint arXiv:2510.20328, 2025.
[20] M. Torne, K. Pertsch, H. Walke, K. Vedder, S. Nair, B. Ichter, A. Z. Ren, H. Wang, J. Tang,
K. Stachowicz, et al. MEM: Multi-scale embodied memory for vision language action models.
arXiv preprint arXiv:2603.03596, 2026.
[21] T. Chen, Y . Wang, M. Li, Y . Qin, H. Shi, Z. Li, Y . Hu, Y . Zhang, K. Wang, Y . Chen, et al. RM-
Bench: Memory-Dependent robotic manipulation benchmark with insights into policy design.
arXiv preprint arXiv:2603.01229, 2026.
[22] Y . Wang, Z. Gu, Y . Gao, A. Jiang, Z. Sun, S. Wang, Y . Heng, and H. Sun. HiST-VLA: A
hierarchical spatio-temporal vision-language-action model for end-to-end autonomous driving.
arXiv preprint arXiv:2602.13329, 2026.
[23] H. Wang, Z. Jing, J. Ao, S. Song, X. Li, G. Huang, and C. Bai. Beyond Short-Horizon:
VQ-Memory for robust long-horizon manipulation in non-markovian simulation benchmarks.
arXiv preprint arXiv:2603.09513, 2026.
[24] Z. Zeng, F. Ding, H. Yang, and X. Li. HELM: Harness-Enhanced long-horizon memory for
vision-language-action manipulation.arXiv preprint arXiv:2604.18791, 2026.
[25] H. Li, F. Shen, D. Chen, L. Yang, X. Wang, J. Shi, Z. Bing, Z. Liu, and A. Knoll. ReMem-VLA:
Empowering vision-language-action model with memory via dual-level recurrent queries.
arXiv preprint arXiv:2603.12942, 2026.
[26] M. Koo, D. Choi, T. Kim, K. Lee, C. Kim, Y . Seo, and J. Shin. HAMLET: Switch your
vision-language-action model into a history-aware policy.arXiv preprint arXiv:2510.00695,
2025.
[27] M. Lin, P. Ding, S. Wang, Z. Zhuang, Y . Liu, X. Tong, W. Song, S. Lyu, S. Huang, and
D. Wang. HiF-VLA: Hindsight, Insight and Foresight through motion representation for
Vision-Language-Action models.arXiv preprint arXiv:2512.09928, 2025.
[28] J. Liu, Y . Qi, J. Zhang, M. Li, S. Wang, K. Wu, H. Ye, H. Zhang, Z. Chen, F. Zhong, et al.
TrackVLA++: Unleashing reasoning and memory capabilities in VLA models for embodied
visual tracking.arXiv preprint arXiv:2510.07134, 2025.
[29] G. Nangue Tasse, M. Riemer, B. Rosman, and T. Klinger. Beyond sliding windows: Learning
to manage memory in non-markovian environments.arXiv e-prints, 2025.
[30] H. Fang, M. Grotz, W. Pumacay, Y . R. Wang, D. Fox, R. Krishna, and J. Duan. SAM2Act: In-
tegrating visual foundation model with a memory architecture for robotic manipulation.arXiv
preprint arXiv:2501.18564, 2025.
[31] Y . Yang, H. Yang, J. Zhou, P. Chen, H. Zhang, Y . Du, and C. Gan. 3D-mem: 3D scene memory
for embodied exploration and reasoning. InProceedings of the Computer Vision and Pattern
Recognition Conference, 2025.
11

<!-- page: 12 -->

[32] Y . Gao, J. Liu, S. Li, and S. Song. Gated memory policy.arXiv preprint arXiv:2604.18933,
2026.
[33] Z. Chen, Y . Hu, Z. Fu, Z. Li, J. Huang, Q. Huang, and Y . Wei. INTENT: Invariance and
discrimination-aware noise mitigation for robust composed image retrieval. InProceedings of
the AAAI Conference on Artificial Intelligence, 2026.
[34] Z. Li, Y . Hu, Z. Chen, S. Zhang, Q. Huang, Z. Fu, and Y . Wei. HABIT: Chrono-synergia
robust progressive learning framework for composed image retrieval. InProceedings of the
AAAI Conference on Artificial Intelligence, 2026.
[35] Z. Li, Y . Hu, Z. Chen, Q. Huang, G. Qiu, Z. Fu, and M. Liu. ReTrack: Evidence-driven dual-
stream directional anchor calibration network for composed video retrieval. InProceedings of
the AAAI Conference on Artificial Intelligence, 2026.
[36] A. Zhai, B. Liu, B. Fang, C. Cai, E. Ma, E. Yin, H. Wang, H. Zhou, J. Wang, L. Shi, et al.
Igniting VLMs toward the embodied space.arXiv preprint arXiv:2509.11766, 2025.
[37] J. Yang, K. Lin, J. Li, W. Zhang, T. Lin, L. Wu, Z. Su, H. Zhao, Y .-Q. Zhang, L. Chen,
et al. RISE: Self-improving robot policy with compositional world model.arXiv preprint
arXiv:2602.11075, 2026.
[38] G. Team, A. Ye, B. Wang, C. Ni, G. Huang, G. Zhao, H. Li, J. Zhu, K. Li, M. Xu,
et al. GigaWorld-0: World models as data engine to empower embodied ai.arXiv preprint
arXiv:2511.19861, 2025.
[39] G. Team, B. Wang, B. Li, C. Ni, G. Huang, G. Zhao, H. Li, J. Li, J. Lv, J. Liu, et al. GigaBrain-
0.5M∗: a vla that learns from world model-based reinforcement learning.arXiv preprint
arXiv:2602.12099, 2026.
[40] A. Ye, Z. Zhang, B. Wang, X. Wang, D. Zhang, and Z. Zhu. VLA-R1: Enhancing reasoning in
vision-language-action models.arXiv preprint arXiv:2510.01623, 2025.
[41] H. Li, I. Zhang, R. Ouyang, X. Wang, Z. Zhu, Z. Yang, Z. Zhang, B. Wang, C. Ni, W. Qin,
et al. MimicDreamer: Aligning human and robot demonstrations for scalable VLA training.
arXiv preprint arXiv:2509.22199, 2025.
[42] Y . Li, L. Zhou, S. Yan, B. Liao, T. Yan, K. Xiong, L. Chen, H. Xie, B. Wang, G. Chen,
et al. UniDriveVLA: Unifying understanding, perception, and action planning for autonomous
driving.arXiv preprint arXiv:2604.02190, 2026.
[43] J. Wen, Y . Zhu, J. Li, M. Zhu, Z. Tang, K. Wu, Z. Xu, N. Liu, R. Cheng, C. Shen, et al.
TinyVLA: Towards fast, data-efficient vision-language-action models for robotic manipula-
tion.IEEE Robotics and Automation Letters, 2025.
[44] W. Zhang, H. Liu, Z. Qi, Y . Wang, X. Yu, J. Zhang, R. Dong, J. He, H. Wang, Z. Zhang, et al.
DreamVLA: a vision-language-action model dreamed with comprehensive world knowledge.
arXiv preprint arXiv:2507.04447, 2025.
[45] B. Chen, Z. Xu, S. Kirmani, B. Ichter, D. Sadigh, L. Guibas, and F. Xia. SpatialVLM: En-
dowing vision-language models with spatial reasoning capabilities. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024.
[46] A. Brohan, N. Brown, J. Carbajal, Y . Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Haus-
man, A. Herzog, J. Hsu, et al. RT-1: Robotics transformer for real-world control at scale.arXiv
preprint arXiv:2212.06817, 2022.
[47] M. J. Kim, C. Finn, and P. Liang. Fine-tuning vision-language-action models: Optimizing
speed and success.arXiv preprint arXiv:2502.19645, 2025.
12

<!-- page: 13 -->

[48] J. Cen, C. Yu, H. Yuan, Y . Jiang, S. Huang, J. Guo, X. Li, Y . Song, H. Luo, F. Wang, et al.
WorldVLA: Towards autoregressive action world model.arXiv preprint arXiv:2506.21539,
2025.
[49] Y . Hu, J.-N. Zaech, N. Nikolov, Y . Yao, S. Dey, G. Albanese, R. Detry, L. Van Gool, and
D. Paudel. AR-VLA: True autoregressive action expert for Vision-Language-Action models.
arXiv preprint arXiv:2603.10126, 2026.
[50] F. Peller-Konrad, R. Kartmann, C. R. Dreher, A. Meixner, F. Reister, M. Grotz, and T. As-
four. A memory system of a robot cognitive architecture and its implementation in ArmarX.
Robotics and Autonomous Systems, 2023.
[51] H. Shi, B. Xie, Y . Liu, L. Sun, F. Liu, T. Wang, E. Zhou, H. Fan, X. Zhang, and G. Huang.
MemoryVLA: Perceptual-cognitive memory in vision-language-action models for robotic ma-
nipulation.arXiv preprint arXiv:2508.19236, 2025.
[52] R. Li, W. Guo, Z. Wu, C. Wang, H. Deng, Z. Weng, Y .-P. Tan, and Z. Wang. MAP-VLA:
Memory-augmented prompting for vision-language-action model in robotic manipulation.
arXiv preprint arXiv:2511.09516, 2025.
[53] M. Neau, Z. Falomir, P. E. Santos, A.-G. Bosser, and C. Buche. GraSP-VLA: Graph-based
symbolic action representation for long-horizon planning with VLA policies.arXiv preprint
arXiv:2511.04357, 2025.
[54] X. Guo, C. Jiang, H. B. Kim, Y . Sun, Y . Xiao, Y . Han, and J. Yang. Chameleon: Episodic
memory for long-horizon robotic manipulation.arXiv preprint arXiv:2603.24576, 2026.
[55] J. Zheng, J. Li, Z. Wang, D. Liu, X. Kang, Y . Feng, Y . Zheng, J. Zou, Y . Chen, J. Zeng, et al. X-
VLA: Soft-prompted transformer as scalable cross-embodiment vision-language-action model.
arXiv preprint arXiv:2510.10274, 2025.
[56] K. Black, A. Z. Ren, M. Equi, and S. Levine. Training-time action conditioning for efficient
real-time chunking.arXiv preprint arXiv:2512.05964, 2025.
13
