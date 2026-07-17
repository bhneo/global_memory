---
id: "question_1e0121d4bdc2f58cea1ca426"
type: "question"
status: "working"
title: "“How would j’s action change if I had acted"
created_at: "2026-07-17T12:11:41+08:00"
updated_at: "2026-07-17T18:36:07+08:00"
aliases: []
tags: []
domains: []
confidence: "unknown"
source_ids: ["source_c019c0a492cc659d7858134d"]
relations: [{"type": "derived_from", "target_id": "source_c019c0a492cc659d7858134d", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "working"}]
change_reason: "compile bundle from source_c019c0a492cc659d7858134d"
memory_tier: "working"
created_by: "deterministic-bounded-bundle-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "deterministic-bounded-bundle-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-17T18:36:07+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_70b27fd90bc932fc9712"
origin_item_id: "question-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_70b27fd90bc932fc9712-question-1.md"
origin_candidate_sha256: "2bd756052a8b0afb880b933673e37dc1bf9f606315d2b708ee0e986dc0cffaaa"
memory_schema_version: 2
legacy_status: "working"
epistemic_status: "open_question"
last_consolidation_id: "consolidation_58eedcd85602f4b90b73f635"
---

# “How would j’s action change if I had acted

“How would j’s action change if I had acted

differently in this situation?”.
By sampling several counterfactual actions, and av-
eraging the resulting policy distribution of j in
each case, we obtain the marginal policy of j,
p(aj
t|sj
t ) = ∑
˜ak
t
p(aj
t|˜ak
t,sj
t )p(˜ak
t|sj
t ) —in other words,
j’s policy if it did not consider agentk. The discrepancy
between the marginal policy ofj and the conditional policy
ofj givenk’s action is a measure of the causal inﬂuence
ofk onj; it gives the degree to whichj changes its planned
action distribution because ofk’s action. Thus, the causal
inﬂuence reward for agentk is:
ck
t =
N∑
j=0,j̸=k
[
DKL [p(aj
t|ak
t,sj
t )

∑
˜ak
t
p(aj
t| ˜ak
t,sj
t )p(˜ak
t|sj
t )]
]
=
N∑
j=0,j̸=k
[
DKL [p(aj
t|ak
t,sj
t )
p(aj
t|sj
t )]
]
. (1)
Note that it is possible to use a divergence metric other than
KL; we have found empirically that the inﬂuence reward is
robust to the choice of metric.
The reward in Eq. 4 is related to the mutual information (MI)
between the actions of agentsk andj,I(ak;aj|s). As the
reward is computed over many trajectories sampled inde-
pendently from the environment, we obtain a Monte-Carlo
estimate ofI(ak;aj|s). In expectation, the inﬂuence reward
incentivizes agents to maximize the mutual information
between their actions. The proof is given in Section 10.1
of the Supplementary Material. Intuitively, training agents
to maximize the MI between their actions results in more
coordinated behavior.
Moreover, the variance of policy gradient updates increases
as the number of agents in the environment grows (Lowe et al.,
2017). This issue can hinder convergence to equilibrium for
large-scale MARL tasks. Social inﬂuence can reduce the
variance of policy gradients by introducing explicit depen-
dencies across the actions of each agent. This is because the
conditional variance of the gradients an agent is receiving
will be less than or equal to the marginalized variance.
Note that for the basic inﬂuence model we make two assump-
tions: 1) we use centralized training to computeck
t directly
from the policy of agentj, and 2) we assume that inﬂuence is
unidirectional: agents trained with the inﬂuence reward can
only inﬂuence agents that are not trained with the inﬂuence
reward (the sets of inﬂuencers and inﬂuencees are disjoint,
and the number of inﬂuencers is in[1,N−1]). Both of these
assumptions are relaxed in later sections. Further details, as
well as further explanation of the causal inference procedure
(including causal diagrams) are available in Section 8.
4.1. Experiment I: Basic Inﬂuence
Figure 1 shows the results of testing agents trained with the
basic inﬂuence reward against standard A3C agents, and an
ablated version of the model in which agents do not receive
the inﬂuence reward, but are able to condition their policy
on the actions of other agents (even when the other agents
are not within the agent’s partially observed view of the
environment). We term this ablated model thevisible actions
baseline. In this and all other results ﬁgures, we measure
the total collective reward obtained using the best hyper-
parameter setting tested with 5 random seeds each. Error
bars show a 99.5% conﬁdence interval (CI) over the random
seeds, computed within a sliding window of 200 agent steps.
We use a curriculum learning approach which gradually
increases the weight of the social inﬂuence reward overC
steps (C∈ [0.2−3.5]×108); this sometimes leads to a slight
delay before the inﬂuence models’ performance improves.
As is evident in Figures 1a and 1b, introducing an awareness
of other agents’ actions helps, but having the social inﬂuence
reward eventually leads to signiﬁcantly higher collective
reward in both games. Due to the structure of the SSD games,
we can infer that agents that obtain higher collective reward
learned to cooperate more effectively. In theHarvest MARL

<!-- page: 4 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
setting, it is clear that the inﬂuence reward is essential to
achieve any reasonable learning.
(a) Cleanup
 (b) Harvest
Figure 1: Total collective reward obtained in Experiment 1.
Agents trained with inﬂuence (red) signiﬁcantly outperform
the baseline and ablated agents. In Harvest, the inﬂuence
reward is essential to achieve any meaningful learning.
To understand how social inﬂuence helps agents achieve
cooperative behavior, we investigated the trajectories
produced by high scoring models in both Cleanup and
Harvest; the analysis revealed interesting behavior.
As an example, in the Cleanup video available here:
https://youtu.be/iH_V5WKQxmo a single agent
(shown in purple) was trained with the social inﬂuence
reward. Unlike the other agents, which continue to move
and explore randomly while waiting for apples to spawn,
the inﬂuencer only traverses the map when it is pursuing an
apple, then stops. The rest of the time it stays still.
Figure 2: A moment
of high inﬂuence when
the purple inﬂuencer sig-
nals the presence of
an apple (green tiles)
outside the yellow in-
ﬂuencee’s ﬁeld-of-view
(yellow outlined box).
Figure 2 shows a moment of
high inﬂuence between the in-
ﬂuencer and the yellow inﬂu-
encee. The inﬂuencer has cho-
sen to move towards an ap-
ple that is outside of the ego-
centric ﬁeld-of-view of the yel-
low agent. Because the inﬂu-
encer only moves when apples
are available, this signals to the
yellow agent that an apple must
be present above it which it
cannot see. This changes the
yellow agent’s distribution over
its planned action,p(aj
t|ak
t,sj
t ),
and allows the purple agent to
gain inﬂuence. A similar mo-
ment occurs when the inﬂu-
encer signals to an agent that has
been cleaning the river that no
apples have appeared by staying
still (see Figure 14 in the Sup-
plementary Material).
In this case study, the inﬂuencer agent learned to use its own
actions as a binary code which signals the presence or absence
of apples in the environment. We observe a similar effect in
Harvest. This type of action-based communication could be
likened to the bee waggle dance discovered by von Frisch
(1969). Evidently, the inﬂuence reward gave rise not only to
cooperative behavior, but to emergent communication.
It is important to consider the limitations of the inﬂuence
reward. Whether it will always give rise to cooperative be-
havior may depend on the speciﬁcs of the environment and
task, and tuning the trade-off between environmental and
inﬂuence reward. Although inﬂuence is arguably necessary
for coordination (e.g. two agents coordinating to manipulate
an object must have a high degree of inﬂuence between their
actions), it may be possible to inﬂuence another agent in a
non-cooperative way. The results provided here show that the
inﬂuence reward did lead to increased cooperation, in spite of
cooperation being difﬁcult to achieve in these environments.
5. Inﬂuential Communication
Given the above results, we next experiment with using the
inﬂuence reward to train agents to use an explicit commu-
nication channel. We take some inspiration from research
drawing a connection between inﬂuence and communication
in human learning. According to Melis & Semmann (2010),
human children rapidly learn to use communication to inﬂu-
ence the behavior of others when engaging in cooperative
activities. They explain that “this ability to inﬂuence the
partner via communication has been interpreted as evidence
for a capacity to form shared goals with others”, and that this
capacity may be “what allows humans to engage in a wide
range of cooperative activities”.
Thus, we equip agents with an explicit communication chan-
nel, similar to the approach used by Foerster et al. (2016).
At each timestep, each agentk chooses a discrete commu-
nication symbolmk
t ; these symbols are concatenated into
a combined message vector mt = [m0
t,m1
t...mN
t ], for N
agents. This message vector mt is then given as input to
every other agent in the next timestep. Note that previous
work has shown that self-interested agents do not learn to use
this type of ungrounded, cheap talk communication chan-
nel effectively (Crawford & Sobel, 1982; Cao et al., 2018;
Foerster et al., 2016; Lazaridou et al., 2018).
To train the agents to communicate, we augment our initial
network with an additional A3C output head, that learns a
communication policyπm and value functionVm to deter-
mine which symbol to emit (see Figure 3). The normal policy
and value function used for acting in the environment,πe and
Ve, are trained only with environmental rewarde. We use
the inﬂuence reward as an additional incentive for training
the communication policy,πm, such thatr =αe+βc. Coun-
terfactuals are employed to assess how much inﬂuence an
agent’s communication message from the previous timestep,

<!-- page: 5 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Figure 3: The communication model has two heads, which
learn the environment policy,πe, and a policy for emitting
communication symbols,πm. Other agents’ communication
messages mt−1 are input to the LSTM.
mk
t−1, has on another agent’s action,aj
t, where:
ck
t =
N∑
j=0,j̸=k
[
DKL [p(aj
t|mk
t−1,sj
t )
p(aj
t|sj
t )]
]
(2)
Importantly, rewarding inﬂuence through a communication
channel does not suffer from the limitation mentioned in the
previous section, i.e. that it may be possible to inﬂuence
another agent in a non-cooperative way. We can see this
for two reasons. First, there is nothing that compels agent
j to act based on agentk’s communication message; ifmk
t
does not contain valuable information,j is free to ignore it.
Second, becausej’s action policyπe is trained only with en-
vironmental reward,j will only change its intended action as
a result of observingmk
t (i.e. be inﬂuenced bymk
t ) if it con-
tains information that helpsj to obtain environmental reward.
Therefore, we hypothesize that inﬂuential communication
must provide useful information to the listener.
5.1. Experiment II: Inﬂuential Communication
Figure 4 shows the collective reward obtained when training
the agents to use an explicit communication channel. Here,
the ablated model has the same structure as in Figure 3, but
the communication policyπm is trained only with environ-
mental reward. We observe that the agents incentivized to
communicate via the social inﬂuence reward learn faster, and
achieve signiﬁcantly higher collective reward for the majority
of training in both games. In fact, in the case ofCleanup, we
found thatα = 0in the optimal hyperparameter setting, mean-
ing that it was most effective to train the communication head
with zero extrinsic reward (see Table 2 in the Supplementary
Material). This suggests that inﬂuence alone can be a suf-
ﬁcient mechanism for training an effective communication
policy. In Harvest, once again inﬂuence is critical to allow
agents to learn coordinated policies and attain high reward.
To analyze the communication behaviour learned by the
agents, we introduce three metrics, partially inspired by
(Bogin et al., 2018). Speaker consistency, is a normalized
score∈ [0,1] which assesses the entropy ofp(ak|mk) and
(a) Cleanup
 (b) Harvest
Figure 4: Total collective reward for deep RL agents with
communication channels. Once again, the inﬂuence reward
is essential to improve or achieve any learning.
p(mk|ak) to determine how consistently a speaker agent
emits a particular symbol when it takes a particular action,
and vice versa (the formula is given in the Supplementary
Material Section 10.4.4). We expect this measure to be
high if, for example, the speaker always emits the same
symbol when it is cleaning the river. We also introduce
two measures of instantaneous coordination (IC), which
are both measures of mutual information (MI): (1) sym-
bol/action IC =I(mk
t ;aj
t+1) measures the MI between the in-
ﬂuencer/speaker’s symbol and the inﬂuencee/listener’s next
action, and (2) action/action IC=I(ak
t ;aj
t+1) measures the
MI between the inﬂuencer’s action and the inﬂuencee’s next
action. To compute these measures we ﬁrst average over all
trajectory steps, then take the maximum value between any
two agents, to determine if any pair of agents are coordinat-
ing. Note that these measures are allinstantaneous, as they
consider only short-term dependencies across two consecu-
tive timesteps, and cannot capture if an agent communicates
inﬂuential compositional messages, i.e. information that re-
quires several consecutive symbols to transmit and only then
affects the other agents behavior.
Figure 5: Metrics describing the quality of learned com-
munication protocols. The models trained with inﬂuence
reward exhibit more consistent communication and more
coordination, especially in moments where inﬂuence is high.
Figure 5 presents the results. The speaker consistencies
metric reveals that inﬂuence agents more unambiguously
communicate about their own actions than baseline agents,
indicating that the emergent communication is more mean-
ingful. The IC metrics demonstrate that baseline agents
show almost no signs of co-ordinating behavior with com-
munication, i.e. speakers saying A and listeners doing B
consistently. This result is aligned with both theoretical re-

<!-- page: 6 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
sults in cheap-talk literature (Crawford & Sobel, 1982), and
recent empirical results in MARL (e.g. Foerster et al. (2016);
Lazaridou et al. (2018); Cao et al. (2018)).
In contrast, we do see high IC between inﬂuence agents,
but only when we limit the analysis to timesteps on which
inﬂuence was greater than or equal to the mean inﬂuence
(cf. inﬂuential moments in Figure 5). Inspecting the results
reveals a common pattern: inﬂuence is sparse in time. An
agent’s inﬂuence is only greater than its mean inﬂuence in
less than 10% of timesteps. Because the listener agent is
not compelled to listen to any given speaker, listeners se-
lectively listen to a speaker only when it is beneﬁcial, and
inﬂuence cannot occur all the time. Only when the listener
decides to change its action based on the speaker’s message
does inﬂuence occur, and in these moments we observe high
I(mk
t ;aj
t+1). It appears the inﬂuencers have learned a strat-
egy of communicating meaningful information about their
own actions, and gaining inﬂuence when this becomes rele-
vant enough for the listener to act on it.
Examining the relationship between the degree to which
agents were inﬂuenced by communication and the reward
they obtained gives a compelling result: agents that are the
most inﬂuenced also achieve higher individual environmental
reward. We sampled 100 different experimental conditions
(i.e., hyper-parameters and random seeds) for both games,
and normalized and correlated the inﬂuence and individual
rewards. We found that agents who are more often inﬂuenced
tend to achieve higher task reward in bothCleanup,ρ =.67,
p<0.001, and Harvest, ρ =.34, p<0.001. This supports
the hypothesis that in order to inﬂuence another agent via
communication, the communication message should contain
information that helps the listener maximize its own environ-
mental reward. Since better listeners/inﬂuencees are more
successful in terms of task reward, we have evidence that
useful information was transmitted to them.
This result is promising, but may depend on the speciﬁc ex-
perimental approach taken here, in which agents interact
with each other repeatedly. In this case, there is no advantage
to the speaker for communicating unreliable information
(i.e. lying), because it would lose inﬂuence with the listener
over time. This may not be guaranteed in one-shot interac-
tions. However, given repeated interactions, the above results
provide empirical evidence that social inﬂuence as intrinsic
motivation allows agents to learn meaningful communication
protocols when this is otherwise not possible.
6. Modeling Other Agents
Computing the causal inﬂuence reward as introduced in Sec-
tion 4 requires knowing the probability of another agent’s
action given a counterfactual, which we previously solved
by using a centralized training approach in which agents
could access other agents’ policy networks. While using a
centralized training framework is common in MARL (e.g.
Foerster et al. (2017; 2016)), it is less realistic than a scenario
in which each agent is trained independently. We can relax
this assumption and achieve independent training by equip-
ping each agent with its own internalModel of Other Agents
(MOA). The MOA consists of a second set of fully-connected
and LSTM layers connected to the agent’s convolutional layer
(see Figure 6), and is trained to predict all other agents’ next
actions given their previous actions, and the agent’s egocen-
tric view of the state:p(at+1|at,sk
t ). The MOA is trained
using observed action trajectories and cross-entropy loss.
Figure 6: The Model of Other Agents (MOA) architecture
learns both an RL policy πe, and a supervised model that
predicts the actions of other agents, at+1. The supervised
model is used for internally computing the inﬂuence reward.
A trained MOA can be used to compute the social inﬂuence
reward in the following way. Each agent can “imagine” coun-
terfactual actions that it could have taken at each timestep,
and use its internal MOA to predict the effect on other agents.
It can then give itself reward for taking actions that it esti-
mates were the most inﬂuential. This has an intuitive appeal,
because it resembles how humans reason about their effect
on others (Ferguson et al., 2010). We often ﬁnd ourselves
asking counterfactual questions of the form, “How would she
have acted if I had done something else in that situation?”,
which we answer using our internal model of others.
Learning a model ofp(aj
t+1|ak
t,sk
t ) requires implicitly mod-
eling both other agents’ internal states and behavior, as well
as the environment transition function. If the model is inaccu-
rate, this would lead to noisy estimates of the causal inﬂuence
reward. To compensate for this, We only give the inﬂuence
reward to an agent (k) when the agent it is attempting to inﬂu-
ence (j) is within its ﬁeld-of-view, because the estimates of
p(aj
t+1|ak
t,sk
t ) are more accurate whenj is visible tok.2 This
constraint could have the side-effect of encouraging agents to
stay in closer proximity. However, an intrinsic social reward
encouraging proximity is reasonable given that humans seek
afﬁliation and to spend time near other people (Tomasello,
2This contrasts with our previous models in which the inﬂuence
reward was obtained even from non-visible agents.

<!-- page: 7 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
2009).
6.1. Experiment III: Modeling Other Agents
As before, we allow the policy LSTM of each agent to condi-
tion on the actions of other agents in the last timestep (actions
are visible). We compare against an ablated version of the
architecture shown in Figure 6, which does not use the output
of the MOA to compute a reward; rather, the MOA can be
thought of as an unsupervised auxiliary task that may help the
model to learn a better shared embedding layer, encouraging
it to encode information relevant to predicting other agents’
behavior. Figure 7 shows the collective reward obtained for
agents trained with a MOA module. While we see that the
auxiliary task does help to improve reward over the A3C base-
line, the inﬂuence agent gets consistently higher collective
reward. These results demonstrate that the inﬂuence reward
can be effectively computed using an internal MOA, and thus
agents can learn socially but independently, optimizing for a
social reward without a centralized controller.
(a) Cleanup
 (b) Harvest
Figure 7: Total collective reward for MOA models. Again,
intrinsic inﬂuence consistently improves learning, with the
powerful A3C agent baselines not being able to learn.
Agents with inﬂuence achieve higher collective reward than
the previous state-of-the-art for these environments (275 for
Cleanup and 750 for Harvest) (Hughes et al., 2018). This is
compelling, given that previous work relied on the assump-
tion that agents could view one another’s rewards; we make
no such assumption, instead relying only on agents viewing
each other’s actions. Table 4 of the Supplementary Material
gives the ﬁnal collective reward obtained in previous work,
and by each inﬂuence model for all three experiments.
7. Related work
Several attempts have been made to develop intrinsic social
rewards.3 Sequeira et al. (2011) developed hand-crafted re-
wards for a foraging environment, in which agents were pun-
ished for eating more than their fair share of food. Another
approach gave agents an emotional intrinsic reward based
on their perception of their neighbours’ cooperativeness in
a networked version of the iterated prisoner’s dilemma, but
is limited to scenarios in which it is possible to directly clas-
3Note that intrinsic is not a synonym ofinternal; other people
can be intrinsically motivating (Stavropoulos & Carver, 2013).
sify each action as cooperative or non-cooperative (Yu et al.,
2013). This is untenable in complex settings with long-term
strategies, such as the SSDs under investigation here.
Some approaches allow agents to view each others’ rewards
in order to optimize for collective reward. Peysakhovich &
Lerer (2018) show that if even a single agent is trained to op-
timize for others’ rewards, it can signiﬁcantly help the group.
Hughes et al. (2018) introduced an inequity aversion moti-
vation, which penalized agents if their rewards differed too
much from those of the group. Liu et al. (2014) train agents
to learn their own optimal reward function in a cooperative,
multi-agent setting with known group reward. However, the
assumption that agents can view and optimize for each oth-
ers’ rewards may be unrealistic. Thus, recent work explores
training agents that learn when to cooperate based solely on
their own past rewards (Peysakhovich & Lerer, 2017).
Training agents to learn emergent communication protocols
has been explored (Foerster et al., 2016; Cao et al., 2018; Choi
et al., 2018; Lazaridou et al., 2018; Bogin et al., 2018), with
many authors ﬁnding that selﬁsh agents do not learn to use an
ungrounded, cheap talk communication channel effectively.
Crawford & Sobel (1982) ﬁnd that in theory, the information
communicated is proportional to the amount of common
interest; thus, as agents’ interests diverge, no communication
is to be expected. And while communication can emerge
when agents are prosocial (Foerster et al., 2016; Lazaridou
et al., 2018), curious (Oudeyer & Kaplan, 2006; Oudeyer &
Smith, 2016; Forestier & Oudeyer, 2017), or hand-crafted
(Crandall et al., 2017), self-interested agents do not to learn
to communicate (Cao et al., 2018). We have shown that
the social inﬂuence reward can encourage agents to learn to
communicate more effectively in complex environments.
Our MOA is related to work on machine theory of mind
(Rabinowitz et al., 2018), which demonstrated that a model
trained to predict agents’ actions can model false beliefs.
LOLA agents model the impact of their policy on the param-
eter updates of other agents, and directly incorporate this into
the agent’s own learning rule (Foerster et al., 2018).
Barton et al. (2018) propose causal inﬂuence as a way to mea-
sure coordination between agents, speciﬁcally using Con-
vergence Cross Mapping (CCM) to analyze the degree of
dependence between two agents’ policies. The limitation
if CCM is that estimates of causality are known to degrade
in the presence of stochastic effects (Tajima et al., 2015).
Counterfactual reasoning has also been used in a multi-agent
setting, to marginalize out the effect of one agent on a pre-
dicted global value function estimating collective reward, and
thus obtain an improved baseline for computing each agent’s
advantage function (Foerster et al., 2017). A similar paper
shows that counterfactuals can be used with potential-based
reward shaping to improve credit assignment for training a
joint policy in multi-agent RL (Devlin et al., 2014). However,

<!-- page: 8 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
once again these approaches rely on a centralized controller.
Mutual information (MI) has been explored as a tool for de-
signing social rewards. Strouse et al. (2018) train agents to
optimize the MI between their actions and a categorical goal,
as a way to signal or hide the agent’s intentions. However, this
approach depends on agents pursuing a known, categorical
goal. Guckelsberger et al. (2018), in pursuit of the ultimate
video game adversary, develop an agent that maximizes its
empowerment, minimizes the player’s empowerment, and
maximizes its empowerment over the player’s next state.
This third goal, termedtransfer empowerment, is obtained
by maximizing the MI between the agent’s actions and the
player’s future state. While a social form of empowerment,
the authors ﬁnd that agents trained with transfer empower-
ment simply tend to stay near the player. Further, the agents
are not trained with RL, but rather analytically compute these
measures in simple grid-world environments. As such, the
agent cannot learn to model other agents or the environment.
Given the social inﬂuence reward incentivizes maximizing
the mutual information between agents’ actions, our work
also has ties to the literature on empowerment, in which
agents maximize the mutual information between their ac-
tions and their future state (Klyubin et al., 2005; Mohamed &
Rezende, 2015). Thus, our proposed reward can be seen as a
novel social form of empowerment.
8. Details on Causal Inference
The causal inﬂuence reward presented in Eq. 4 is assessed
using counterfactual reasoning. Unlike ado-calculus inter-
vention (which estimates the general expected causal effect
of one variable on another), a counterfactual involves condi-
tioning on a set of variables observed in a given situation and
asking how would the outcome have changed if some vari-
able were different, and all other variables remained the same
(Pearl et al., 2016). This type of inquiry allows us to measure
the precise causal effect of agentk’s action at timestept,ak
t ,
on agentj’s action,aj
t, in the speciﬁc environment statest,
providing a richer and less sparse reward for agentk. Com-
puting counterfactuals requires conditioning on the correct
set of observed variables to ensure there are no confounds.
In our case, the conditioning set must include not only an
agent’s partially observed view of the environment state,sj
t,
but also the agent’s internal LSTM stateuj
t, to remove any
dependency on previous timesteps in the trajectory. Thus, the
basic causal inﬂuence reward can be more accurately written:
ck
t =
N∑
j=0,j̸=k
[
DKL [p(aj
t|ak
t,sj
t,uj
t )||p(aj
t|sj
t,uj
t )]
]
. (3)
Figure 8 shows the causal diagrams for computing the inﬂu-
ence reward in both the basic case (8a) and the MOA case (8b).
Because basic inﬂuence looks at inﬂuence between agents’
actions in the same timestep, the diagram is much simpler.
However, to avoid circular dependencies in the graph, it re-
quires that agentk choose its action beforej, and therefore
k can inﬂuencej butj cannot inﬂuencek. If there are more
than two agents, we assume a disjoint set of inﬂuencer and
inﬂuencee agents, and all inﬂuencers must act ﬁrst.
(a) Basic
 (b) MOA
Figure 8: Causal diagrams of agentk’s effect onj’s action.
Shaded nodes are conditioned on, and we intervene onak
t
(blue node) by replacing it with counterfactuals. Nodes with
a green background must be modeled using the MOA module.
Note that there is no backdoor path betweenak
t andst in the
MOA case, since it would require traversing a collider that is
not in the conditioning set.
Computing inﬂuence across timesteps, as in the communica-
tion and MOA experiments, complicates the causal diagram,
but ensures that each agent can inﬂuence every other agent.
Figure 8b shows the diagram in the MOA case, in which we
can isolate the causal effect ofak
t onaj
t+1 because the back-
door path throughst is blocked by the collider nodes atst+1
anduj
t+1 (Pearl et al., 2016). Note that it would be sufﬁcient
to condition only onsk
t in order to block all back-door paths
in this case, but we show⟨uk
t,sk
t,aj
t⟩ as shaded because all of
these are given as inputs to the MOA to help it predictaj
t+1.
For the MOA to accurately estimatep(aj
t+1|ak
t,sk
t ), it must
model both the environment transition functionT , as well as
aspects of the internal LSTM state of the other agent,uj
t+1,
as shown by the shaded green variables in Figure 8b.
This is a simple case of counterfactual reasoning, that does
not require using abduction to update the probability of any
unobserved variables (Pearl, 2013). This is because we have
built all relevant models, know all of their inputs, and can
easily store the values for those variables at every step of the
trajectory in order to condition on them so that there are no
unobserved variables that could act as a confounder.
9. Conclusions and Future Work
All three experiments have shown that the proposed intrinsic
social inﬂuence reward consistently leads to higher collec-
tive return. Despite variation in the tasks, hyper-parameters,
neural network architectures and experimental setups, the
learning curves for agents trained with the inﬂuence reward

<!-- page: 9 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
are signiﬁcantly better than the curves of powerful agents
such as A3C and their improved baselines. In some cases,
it is clear that inﬂuence is essential to achieve any form of
learning, attesting to the promise of this idea and highlight-
ing the complexity of learning general deep neural network
multi-agent policies.
Experiment I also showed that the inﬂuence reward can lead
to the emergence of communication protocols. In experiment
II, which included an explicit communication channel, we
saw that inﬂuence improved communication. Experiment
III showed that inﬂuence can be computed by augmenting
agents with an internal model of other agents. The inﬂu-
ence reward can thus be computed without having access to
another agent’s reward function, or requiring a centralized
controller. We were able to surpass state-of-the-art perfor-
mance on the SSDs studied here, despite the fact that previous
work relied on agents’ ability to view other agents’ rewards.
Using counterfactuals to allow agents to understand the ef-
fects of their actions on others is a promising approach with
many extensions. Agents could use counterfactuals to de-
velop a form of ‘empathy’, by simulating how their actions
affect another agent’s value function. Inﬂuence could also
be used to drive coordinated behavior in robots attempting to
do cooperative manipulation and control tasks. Finally, if we
view multi-agent networks as single agents, inﬂuence could
be used as a regularizer to encourage different modules of the
network to integrate information from other networks; for
example, to hopefully prevent collapse in hierarchical RL.
Acknowledgements
We are grateful to Eugene Vinitsky for his help in reproduc-
ing the SSD environments in open source to improve the
replicability of the paper. We also thank Steven Wheelwright,
Neil Rabinowitz, Thore Graepel, Alexander Novikov, Scott
Reed, Pedro Mediano, Jane Wang, Max Kleiman-Weiner, An-
drea Tacchetti, Kevin McKee, Yannick Schroecker, Matthias
Bauer, David Rolnick, Francis Song, David Budden, and
Csaba Szepesvari, as well as everyone on the DeepMind
Machine Learning and Multi-Agent teams for their helpful
discussions and support.
References
Barton, S. L., Waytowich, N. R., Zaroukian, E., and
Asher, D. E. Measuring collaborative emergent behav-
ior in multi-agent reinforcement learning.arXiv preprint
arXiv:1807.08663, 2018.
Bogin, B., Geva, M., and Berant, J. Emergence of commu-
nication in an interactive world with consistent speakers.
arXiv preprint arXiv:1809.00549, 2018.
Cao, K., Lazaridou, A., Lanctot, M., Leibo, J. Z., Tuyls, K.,
and Clark, S. Emergent communication through negotia-
tion. arXiv preprint arXiv:1804.03980, 2018.
Capdepuy, P., Polani, D., and Nehaniv, C. L. Maximization
of potential information ﬂow as a universal utility for col-
lective behaviour. InArtiﬁcial Life, 2007. ALIFE’07. IEEE
Symposium on, pp. 207–213. Ieee, 2007.
Choi, E., Lazaridou, A., and de Freitas, N. Compositional
obverter communication learning from raw visual input.
arXiv preprint arXiv:1804.02341, 2018.
Crandall, J. W., Oudah, M., Chenlinangjia, T., Ishowo-
Oloko, F., Abdallah, S., Bonnefon, J., Cebri´an, M., Shar-
iff, A., Goodrich, M. A., and Rahwan, I. Cooperating
with machines. CoRR, abs/1703.06207, 2017. URL
http://arxiv.org/abs/1703.06207.
Crawford, V . P. and Sobel, J. Strategic information transmis-
sion. Econometrica: Journal of the Econometric Society,
pp. 1431–1451, 1982.
Devlin, S., Yliniemi, L., Kudenko, D., and Tumer, K.
Potential-based difference rewards for multiagent rein-
forcement learning. In Proceedings of the 2014 interna-
tional conference on Autonomous agents and multi-agent
systems, pp. 165–172. International Foundation for Au-
tonomous Agents and Multiagent Systems, 2014.
Ferguson, H. J., Scheepers, C., and Sanford, A. J. Ex-
pectations in counterfactual and theory of mind reason-
ing. Language and Cognitive Processes, 25(3):297–346,
2010. doi: 10.1080/01690960903041174. URL https:
//doi.org/10.1080/01690960903041174.
Foerster, J., Assael, I. A., de Freitas, N., and Whiteson, S.
Learning to communicate with deep multi-agent reinforce-
ment learning. In Advances in Neural Information Pro-
cessing Systems, pp. 2137–2145, 2016.
Foerster, J., Farquhar, G., Afouras, T., Nardelli, N., and
Whiteson, S. Counterfactual multi-agent policy gradients.
arXiv preprint arXiv:1705.08926, 2017.
Foerster, J., Chen, R. Y ., Al-Shedivat, M., Whiteson, S.,
Abbeel, P., and Mordatch, I. Learning with opponent-
learning awareness. In Proceedings of the 17th Interna-
tional Conference on Autonomous Agents and MultiAgent
Systems, pp. 122–130. International Foundation for Au-
tonomous Agents and Multiagent Systems, 2018.
Forestier, S. and Oudeyer, P.-Y . A uniﬁed model of speech
and tool use early development. In 39th Annual Con-
ference of the Cognitive Science Society (CogSci 2017),
2017.
Gers, F. A., Schmidhuber, J., and Cummins, F. Learning to
forget: Continual prediction with lstm. 1999.

<!-- page: 10 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Guckelsberger, C., Salge, C., and Togelius, J. New
and surprising ways to be mean. adversarial npcs with
coupled empowerment minimisation. arXiv preprint
arXiv:1806.01387, 2018.
Harari, Y . N.Sapiens: A brief history of humankind. Random
House, 2014.
Henrich, J. The Secret of Our Success: How culture is driving
human evolution, domesticating our species, and making
us smart. Princeton University Press, Princeton, NJ, 2015.
URL http://press.princeton.edu/titles/
10543.html.
Herrmann, E., Call, J., Hern `andez-Lloreda, M. V ., Hare,
B., and Tomasello, M. Humans have evolved spe-
cialized skills of social cognition: The cultural intel-
ligence hypothesis. Science, 317(5843):1360–1366,
2007. ISSN 0036-8075. doi: 10.1126/science.
1146282. URL http://science.sciencemag.
org/content/317/5843/1360.
Hughes, E., Leibo, J. Z., Phillips, M. G., Tuyls, K., Du´e˜nez-
Guzm´an, E. A., Casta ˜neda, A. G., Dunning, I., Zhu, T.,
McKee, K. R., Koster, R., et al. Inequity aversion improves
cooperation in intertemporal social dilemmas. InAdvances
in neural information processing systems (NIPS), Mon-
treal, Canada, 2018.
Klyubin, A. S., Polani, D., and Nehaniv, C. L. Empowerment:
A universal agent-centric measure of control. In Evolu-
tionary Computation, 2005. The 2005 IEEE Congress on,
volume 1, pp. 128–135. IEEE, 2005.
Laland, K. N. Darwin’s unﬁnished symphony : how cul-
ture made the human mind / Kevin N. Laland. Princeton
University Press Princeton, 2017. ISBN 9781400884872
140088487.
Lazaridou, A., Hermann, K. M., Tuyls, K., and Clark, S.
Emergence of linguistic communication from referential
games with symbolic and pixel input. arXiv preprint
arXiv:1804.03984, 2018.
Leibo, J. Z., Zambaldi, V ., Lanctot, M., Marecki, J., and Grae-
pel, T. Multi-agent reinforcement learning in sequential
social dilemmas. In Proceedings of the 16th Conference
on Autonomous Agents and MultiAgent Systems, pp. 464–
473. International Foundation for Autonomous Agents and
Multiagent Systems, 2017.
Liu, B., Singh, S., Lewis, R. L., and Qin, S. Optimal rewards
for cooperative agents.IEEE Transactions on Autonomous
Mental Development, 6(4):286–297, 2014.
Lizier, J. T. and Prokopenko, M. Differentiating information
transfer and causal effect. The European Physical Journal
B, 73(4):605–615, 2010.
Lowe, R., Wu, Y ., Tamar, A., Harb, J., Abbeel, O. P., and Mor-
datch, I. Multi-agent actor-critic for mixed cooperative-
competitive environments. In Advances in Neural Infor-
mation Processing Systems, pp. 6379–6390, 2017.
Melis, A. P. and Semmann, D. How is human cooperation
different? Philosophical Transactions of the Royal Society
of London B: Biological Sciences, 365(1553):2663–2674,
2010.
Mnih, V ., Badia, A. P., Mirza, M., Graves, A., Lillicrap, T.,
Harley, T., Silver, D., and Kavukcuoglu, K. Asynchronous
methods for deep reinforcement learning. InInternational
conference on machine learning, pp. 1928–1937, 2016.
Mohamed, S. and Rezende, D. J. Variational information
maximisation for intrinsically motivated reinforcement
learning. In Advances in neural information processing
systems, pp. 2125–2133, 2015.
Oudeyer, P.-Y . and Kaplan, F. Discovering communication.
Connection Science, 18(2):189–206, 2006.
Oudeyer, P.-Y . and Smith, L. B. How evolution may work
through curiosity-driven developmental process.Topics
in Cognitive Science, 8(2):492–502, 2016.
Pathak, D., Agrawal, P., Efros, A. A., and Darrell, T.
Curiosity-driven exploration by self-supervised predic-
tion. In International Conference on Machine Learning
(ICML), volume 2017, 2017.
Pearl, J. Structural counterfactuals: A brief introduction.
Cognitive science, 37(6):977–985, 2013.
Pearl, J., Glymour, M., and Jewell, N. P.Causal inference in
statistics: a primer. John Wiley & Sons, 2016.
Perolat, J., Leibo, J. Z., Zambaldi, V ., Beattie, C., Tuyls,
K., and Graepel, T. A multi-agent reinforcement learn-
ing model of common-pool resource appropriation. In
Advances in Neural Information Processing Systems, pp.
3643–3652, 2017.
Peysakhovich, A. and Lerer, A. Consequentialist conditional
cooperation in social dilemmas with imperfect informa-
tion. arXiv preprint arXiv:1710.06975, 2017.
Peysakhovich, A. and Lerer, A. Prosocial learning agents
solve generalized stag hunts better than selﬁsh ones. In
Proceedings of the 17th International Conference on Au-
tonomous Agents and MultiAgent Systems, pp. 2043–2044.
International Foundation for Autonomous Agents and
Multiagent Systems, 2018.
Rabinowitz, N. C., Perbet, F., Song, H. F., Zhang, C., Eslami,
S., and Botvinick, M. Machine theory of mind. arXiv
preprint arXiv:1802.07740, 2018.

<!-- page: 11 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Schelling, T. C. Hockey helmets, concealed weapons, and
daylight saving: A study of binary choices with exter-
nalities. Journal of Conﬂict resolution, 17(3):381–428,
1973.
Schmidhuber, J. Formal theory of creativity, fun, and in-
trinsic motivation (1990–2010). IEEE Transactions on
Autonomous Mental Development, 2(3):230–247, 2010.
Sequeira, P., Melo, F. S., Prada, R., and Paiva, A. Emerging
social awareness: Exploring intrinsic motivation in mul-
tiagent learning. In Development and Learning (ICDL),
2011 IEEE International Conference on, volume 2, pp.
1–6. IEEE, 2011.
Singh, S. P., Barto, A. G., and Chentanez, N. Intrinsically
motivated reinforcement learning. InAdvances in Neural
Information Processing Systems 17 [Neural Information
Processing Systems, NIPS 2004, December 13-18, 2004,
Vancouver, British Columbia, Canada], pp. 1281–1288,
2004.
Stavropoulos, K. K. and Carver, L. J. Research review: social
motivation and oxytocin in autism–implications for joint
attention development and intervention.Journal of Child
Psychology and Psychiatry, 54(6):603–618, 2013.
Strouse, D., Kleiman-Weiner, M., Tenenbaum, J., Botvinick,
M., and Schwab, D. Learning to share and hide inten-
tions using information regularization. arXiv preprint
arXiv:1808.02093, 2018.
Tajima, S., Yanagawa, T., Fujii, N., and Toyoizumi, T.
Untangling brain-wide dynamics in consciousness by
cross-embedding. PLoS computational biology, 11(11):
e1004537, 2015.
Tomasello, M. Why we cooperate. MIT press, 2009.
van Schaik, C. P. and Burkart, J. M. Social learning and evo-
lution: the cultural intelligence hypothesis. Philosophical
Transactions of the Royal Society B: Biological Sciences,
366(1567):1008–1016, 2011.
von Frisch, K. The dance language and orientation of bees.
5, 06 1969.
Yu, C., Zhang, M., and Ren, F. Emotional multiagent rein-
forcement learning in social dilemmas. InInternational
Conference on Principles and Practice of Multi-Agent
Systems, pp. 372–387. Springer, 2013.
10. Supplementary Material
10.1. Inﬂuence as Mutual Information
The causal inﬂuence of agentk on agentj is:
DKL
[
p(aj
t|ak
t,zt)
p(aj
t|zt)
]
, (4)
wherezt represents all relevantu ands background variables
at timestept. The inﬂuence reward to the mutual information
(MI) between the actions of agentsk andj, which is given by
I(Aj;Ak|z) =
∑
ak,aj
p(aj,ak|z)log p(aj,ak|z)
p(aj|z)p(ak|z)
=
∑
ak
p(ak|z)DKL
[
p(aj|ak,z)
p(aj|z)
]
, (5)
where we see that the DKL factor in Eq. 5 is the causal
inﬂuence reward given in Eq. 4.
By samplingN independent trajectoriesτn from the environ-
ment, wherek’s actionsak
n are drawn according top(ak|z),
we perform a Monte-Carlo approximation of the MI (see e.g.
Strouse et al. (2018)),
I(Ak;Aj|z) =Eτ
[
DKL
[
p(Aj|Ak,z)
p(Aj|z)
]⏐⏐⏐z
]
≈ 1
N
∑
n
DKL
[
p(Aj|ak
n,z)
p(Aj|z)
]
. (6)
Thus, in expectation, the social inﬂuence reward is the MI
between agents’ actions.
Whether the policy trained with Eq. 4 actually learns to ap-
proximate the MI depends on the learning dynamics. We
calculate the intrinsic social inﬂuence reward using Eq. 4, be-
cause unlike Eq. 5, which gives an estimate of the symmetric
bandwidth betweenk andj, Eq. 4 gives the directed causal
effect of the speciﬁc action taken by agentk,ak
t . We believe
this will result in an easier reward to learn, since it allows for
better credit assignment; agentk can more easily learn which
of its actions lead to high inﬂuence.
The connection to mutual information is interesting, because
a frequently used intrinsic motivation for single agent RL
is empowerment, which rewards the agent for having high
mutual information between its actions and the future state
of the environment (e.g. Klyubin et al. (2005); Capdepuy
et al. (2007)). To the extent that the social inﬂuence reward
approximates the MI,k is rewarded for having empowerment
overj’s actions.
The social inﬂuence reward can also be computed using
other divergence measures besides KL-divergence. Lizier &
Prokopenko (2010) proposelocal information ﬂowas a mea-
sure of direct causal effect; this is equivalent to thepointwise
mutual information (the innermost term of Eq. 6), given by:
pmi(ak;aj|Z =z) = logp(aj|ak,z)
p(aj|z)
= log p(ak,aj|z)
p(ak|z)p(aj|z). (7)
The PMI gives us a measure of inﬂuence of a single action of
k on the single action taken byj. The expectation of the PMI

<!-- page: 12 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
overp(aj,ak|z) is the MI. We experiment with using the PMI
and a number of divergence measures, including the Jensen-
Shannon Divergence (JSD), and ﬁnd that the inﬂuence reward
is robust to the choice of measure.
10.2. Sequential Social Dilemmas
Figure 9 depicts the SSD games under investigation. In each
of the games, an agent is rewarded +1 for every apple it
collects, but the apples are a limited resource. Agents have
the ability to punish each other with a ﬁning beam, which
costs−1 reward to ﬁre, and ﬁnes any agent it hits−50 reward.
In Cleanup (a public goods game) agents must clean a
river before apples can grow, but are not able to harvest
apples while cleaning. InHarvest (a common pool resource
game), apples respawn at a rate proportional to the amount
of nearby apples; if apples are harvested too quickly, they
will not grow back. Both coordination, and cooperation
are required to solve both games. In Cleanup, agents
must efﬁciently time harvesting apples and cleaning
the river, and allow agents cleaning the river a chance
to consume apples. In Harvest, agents must spatially
distribute their harvesting, and abstain from consuming
apples too quickly in order to harvest sustainably. The
code for these games, including hyperparameter settings
and apple and waste respawn probabilities, can be found
at https://github.com/eugenevinitsky/
sequential_social_dilemma_games.
The reward structure of the games is shown in Figure 10,
which gives the Schelling diagram for both SSD tasks under
investigation. A Schelling diagram (Schelling, 1973; Perolat
et al., 2017) depicts the relative payoffs for a single agent’s
strategy given a ﬁxed number of other agents who are coop-
erative. These diagrams show that all agents would beneﬁt
from learning to cooperate, because even the agents that are
being exploited get higher reward than in the regime where
all agents defect. However, traditional RL agents struggle to
learn to cooperate and solve these tasks effectively (Hughes
et al., 2018).
10.3. Additional experiment - Box Trapped
As a proof-of-concept experiment to test whether the inﬂu-
ence reward works as expected, we constructed a special
environment, shown in Figure 11. In this environment, one
agent (teal) is trapped in a box. The other agent (purple) has
a special action it can use to open the box... or it can simply
choose to consume apples, which exist outside the box and
are inexhaustible in this environment.
As expected, a vanilla A3C agent learns to act selﬁshly; the
purple agent will simply consume apples, and chooses the
open box action in 0% of trajectories once the policy has con-
verged. A video of A3C agents trained in this environment
is available at: https://youtu.be/C8SE9_YKzxI,
which shows that the purple agent leaves its compatriot
trapped in the box throughout the trajectory.
In contrast, an agent trained with the social inﬂuence re-
ward chooses the open box action in 88% of trajectories,
releasing its fellow agent so that they are both able to
consume apples. A video of this behavior is shown at:
https://youtu.be/Gfo248-qt3c. Further, as Fig-
ure 12 reveals, the purple inﬂuencer agent usually chooses to
open the box within the ﬁrst few steps of the trajetory, giving
its fellow agent more time to collect reward.
Most importantly though, Figure 13 shows the inﬂuence
reward over the course of a trajectory in the Box trapped
environment. The agent chooses theopen box action in the
second timestep; at this point, we see a corresponding spike
in the inﬂuence reward. This reveals that the inﬂuence reward
works as expected, incentivizing an action which has a strong
— and in this case, prosocial — effect on the other agent’s
behavior.
10.4. Implementation details
All models are trained with a single convolutional layer with
a kernel of size 3, stride of size 1, and 6 output channels.
This is connected to two fully connected layers of size 32
each, and an LSTM with 128 cells. We use a discount factor
γ =.99. The number of agentsN is ﬁxed to 5.
In addition to the comparison function used to compute inﬂu-
ence (e.g. KL-divergence, PMI, JSD), there are many other
hyperparameters that can be tuned for each model. We use a
random search over hyperparameters, ensuring a fair compar-
ison with the search size over the baseline parameters that are
shared with the inﬂuence models. For all models we search
for the optimal entropy reward and learning rate, where we
anneal the learning rate from an initial value lr init to
lr final. The below sections give the parameters found
to be most effective for each of the three experiments.
10.4.1. B ASIC INFLUENCE HYPERPARAMETERS
In this setting we vary the number of inﬂuencers from1−4,
the inﬂuence reward weightβ, and the number of curriculum
steps over which the weight of the inﬂuence reward is lin-
early increasedC. In this setting, since we have a centralised
controller, we also experiment with giving the inﬂuence re-
ward to the agent being inﬂuenced as well, and ﬁnd that this
sometimes helps. This ‘inﬂuencee’ reward is not used in the
other two experiments, since it precludes independent train-
ing. The hyperparameters found to give the best performance
for each model are shown in Table 1.

<!-- page: 13 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Figure 9: The two SSD environments, Cleanup (left) and Harvest (right). Agents can exploit other agents for immediate
payoff, but at the expense of the long-term collective reward of the group. Reproduced with permission from Hughes et al.
(2018).
(a) Cleanup
 (b) Harvest
Figure 10: Schelling diagrams for the two social dilemma tasks show that an individual agent is motivated to defect, though
everyone beneﬁts when more agents cooperate. Reproduced with permission from Hughes et al. (2018).
Cleanup Harvest
Hyperparameter A3C
baseline
Visible actions
baseline Inﬂuence A3C
baseline
Visible actions
baseline Inﬂuence
Entropy reg. .00176 .00176 .000248 .000687 .00184 .00025
lr init .00126 .00126 .00107 .00136 .00215 .00107
lr end .000012 .000012 .000042 .000028 .000013 .000042
Number of inﬂuencers - 3 1 - 3 3
Inﬂuence weightβ - 0 .146 - 0 .224
CurriculumC - - 140 - - 140
Policy comparison - - JSD - - PMI
Inﬂuencee reward - - 1 - - 0
Table 1: Optimal hyperparameter settings for the models in the basic inﬂuence experiment.
Figure 11: The Box trapped environment in which the teal
agent is trapped, and the purple agent can release it with a
special open box action.
10.4.2. C OMMUNICATION HYPERPARAMETERS
Because the communication models have an extra A2C out-
put head for the communication policy, we use an additional
entropy regularization term just for this head, and apply a
weight to the communication loss in the loss function. We
also vary the number of communication symbols that the
agents can emit, and the size of the linear layer that connects
the LSTM to the communication policy layer, which we term
the communication embedding size. Finally, in the commu-
nication regime, we experiment to setting the weight on the
extrinsic reward E,α, to zero. The best hyperparameters for
each of the communication models are shown in Table 2.
10.4.3. M ODEL OF OTHER AGENTS (MOA)
HYPERPARAMETERS
The MOA hyperparameters include whether to only train the
MOA with cross-entropy loss on the actions of agents that
are visible, and how much to weight the supervised loss in
the overall loss of the model. The best hyperparameters are
shown in Table 3.

<!-- page: 14 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Cleanup Harvest
Hyperparameter A3C
baseline
Comm.
baseline
Inﬂuence
comm.
A3C
baseline
Comm.
baseline
Inﬂuence
comm.
Entropy reg. .00176 .000249 .00305 .000687 .000174 .00220
lr init .00126 .00223 .00249 .00136 .00137 .000413
lr end .000012 .000022 .0000127 .000028 .0000127 .000049
Inﬂuence weightβ - 0 2.752 - 0 4.825
Extrinsic reward
weightα - - 0 - - 1.0
CurriculumC - - 1 - - 8
Policy comparison - - KL - - KL
Comm. entropy reg. - - .000789 - - .00208
Comm. loss weight - - .0758 - - .0709
Symbol vocab size - - 9 - - 7
Comm. embedding - - 32 - - 16
Table 2: Optimal hyperparameter settings for the models in the communication experiment.
Cleanup Harvest
Hyperparameter A3C
baseline
MOA
baseline
Inﬂuence
MOA
A3C
baseline
MOA
baseline
Inﬂuence
MOA
Entropy reg. .00176 .00176 .00176 .000687 .00495 .00223
lr init .00126 .00123 .00123 .00136 .00206 .00120
lr end .000012 .000012 .000012 .000028 .000022 .000044
Inﬂuence weightβ - 0 .620 - 0 2.521
MOA loss weight - 1.312 15.007 - 1.711 10.911
CurriculumC - - 40 - - 226
Policy comparison - - KL - - KL
Train MOA only
when visible - False True - False True
Table 3: Optimal hyperparameter settings for the models in the model of other agents (MOA) experiment.
Figure 12: Number of times the open box action occurs at
each trajectory step over 100 trajectories.
Figure 13: Inﬂuence reward over a trajectory inBox trapped.
An agent gets high inﬂuence for letting another agent out of
the box in which it is trapped.
10.4.4. C OMMUNICATION ANALYSIS
The speaker consistency metric is calculated as:
N∑
k=1
0.5[
∑
c
1−H(p(ak|mk =c))
Hmax
+
∑
a
1−H(p(mk|ak =a))
Hmax
], (8)

<!-- page: 15 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
whereH is the entropy function andHmax is the maximum
entropy based on the number of discrete symbols or actions.
The goal of the metric is to measure how much of a 1:1
correspondence exists between a speaker’s action and the
speaker’s communication message.
10.5. Additional results
10.5.1. BASIC INFLUENCE EMERGENT COMMUNICATION
Figure 14 shows an additional moment of high inﬂuence in
the Cleanup game. The purple inﬂuencer agent can see the
area within the white box, and therefore all of the apple patch.
The ﬁeld-of-view of the magenta inﬂuencee is outlined with
the magenta box; it cannot see if apples have appeared, even
though it has been cleaning the river, which is the action re-
quired to cause apples to appear. When the purple inﬂuencer
turns left and does not move towards the apple patch, this
signals to the magenta agent that no apples have appeared,
since otherwise the inﬂuence would move right.
Figure 14: A moment of high inﬂuence between the purple
inﬂuencer and magenta inﬂuencee.
10.5.2. O PTIMIZING FOR COLLECTIVE REWARD
(a) Cleanup
 (b) Tragedy
Figure 15: Total collective reward obtained by agents trained
to optimize for the collective reward, for the 5 best hyperpa-
rameter settings with 5 random seeds each. Error bars show
a 99.5% conﬁdence interval (CI) computed within a sliding
window of 200 agent steps.
In this section we include the results of training explicitly
prosocial agents, which directly optimize for the collective
reward of all agents. Previous work (e.g. Peysakhovich &
Lerer (2018)) has shown that training agents to optimize
for the rewards of other agents can help the group to obtain
better collective outcomes. Following a similar principle, we
implemented agents that optimize for a convex combination
of their own individual rewardek
t and the collective reward
of all other agents,∑N
i=1,i̸=kei
t. Thus, the reward function
for agentk isrk
t =ek
t +η∑N
i=1,i̸=kei
t. We conducted the
same hyperparameter search over the parameters mentioned
in Section 10.4.1 varying the weight placed on the collective
reward,η∈ [0,2].
As expected, we ﬁnd that agents trained to optimize for col-
lective reward attain higher collective reward in bothCleanup
and Harvest, as is shown in Figure 15. In both games, the
optimal value forη = 0.85. Interestingly, however, the equal-
ity in the individual returns for these agents is extremely low.
Across the hyperparameter sweep, no solution to theCleanup
game which scored more than 20 points in terms of collective
return was found in which all agents scored an individual
return above 0. It seems that in Cleanup, when agents are
trained to optimize for collective return, they converge on a
solution in which some agents never receive any reward.
Note that training agents to optimize for collective reward
requires that each agent can view the rewards obtained by
other agents. As discussed previously, the social inﬂuence
reward is a novel way to obtain cooperative behavior, that
does not require making this assumption.
10.5.3. C OLLECTIVE REWARD AND EQUALITY
It is important to note that collective reward is not always the
perfect metric of cooperative behavior, a ﬁnding that was also
discovered by Barton et al. (2018) and emphasized by Leibo
et al. (2017). In the case, we ﬁnd that there is a spurious
solution to the Harvest game, in which one agent fails to
learn and fails to collect any apples. This leads to very high
collective reward, since it means there is one fewer agent
that can exploit the others, and makes sustainable harvesting
easier to achieve. Therefore, for the results shown in the
paper, we eliminate any random seed inHarvest for which
one of the agents has failed to learn to collect apples, as in
previous work (Hughes et al., 2018).
However, here we also present an alternative strategy for
assessing the overall collective outcomes: weighting the total
collective reward by an index of equality of the individual
rewards. Speciﬁcally, we compute the Gini coefﬁcient over
theN agents’ individual environmental rewardsek
t :
G =
∑N
i=1
∑N
j=1|ei
t−ej
t|
2N∑N
i=1ei
t
, (9)

<!-- page: 16 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
which gives us a measure of the inequality of the returns,
whereG∈ [0,1], withG = 0indicating perfect equality. Thus,
1−G is a measure of equality; we use this to weight the
collective reward for each experiment, and plot the results in
Figure 16. Once again, we see that the inﬂuence models give
the highest ﬁnal performance, even with this new metric.
10.5.4. C OLLECTIVE REWARD OVER MULTIPLE
HYPERPARAMETERS
Finally, we would like to show that the inﬂuence reward is
robust to the choice of hyperparameter settings. Therefore,
in Figure 17, we plot the collective reward of the top 5 best
hyperparameter settings for each experiment, over 5 random
seeds each. Once again, the inﬂuence models result in higher
collective reward, which provides evidence that the model is
robust to the choice of hyperparameters.
10.5.5. PERFORMANCE COMPARISON BETWEEN MODELS
AND RELATED WORK
Table 4 presents the ﬁnal collective reward obtained by each
of the models tested in the experiments presented in the
paper. We see that in several cases, the inﬂuence agents are
even able to out-perform the state-of-the-art results on these
tasks reported by (Hughes et al., 2018), despite the fact that
the solution proposed by (Hughes et al., 2018) requires that
agents can view other agents’ rewards, whereas we do not
make this assumption, and instead only require that agents
can view each others’ actions.
Cleanup Harvest
A3C baseline 89 485
Inequity aversion (Hughes et al.) 275 750
Inﬂuence - Basic 190 1073
Inﬂuence - Communication 166 951
Inﬂuence - Model of other agents 392 588
Table 4: Final collective reward over the last 50 agent steps
for each of the models considered. Bolded entries represent
experiments in which the inﬂuence models signiﬁcantly out-
performed the scores reported in previous work oninequity
aversion (Hughes et al., 2018). This is impressive, consid-
ering the inequity averse agents are able to view all other
agents’ rewards. We make no such assumption, and yet are
able to achieve similar or superior performance.

<!-- page: 17 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
(a) Cleanup - Basic inﬂuence
 (b) Harvest - Basic inﬂuence
(c) Cleanup - Communication
 (d) Harvest - Communication
(e) Cleanup - Model of other agents
 (f) Harvest - Model of other agents
Figure 16: Total collective reward times equality,R∗(1−G), obtained in all experiments. Error bars show a 99.5% conﬁdence
interval (CI) over 5 random seeds, computed within a sliding window of 200 agent steps. Once again, the models trained with
inﬂuence reward (red) signiﬁcantly outperform the baseline and ablated models.

<!-- page: 18 -->

Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
(a) Cleanup - Basic inﬂuence
 (b) Harvest - Basic inﬂuence
(c) Cleanup - Communication
 (d) Harvest - Communication
(e) Cleanup - Model of other agents
 (f) Harvest - Model of other agents
Figure 17: Total collective reward over the top 5 hyperparameter settings, with 5 random seeds each, for all experiments. Error
bars show a 99.5% conﬁdence interval (CI) computed within a sliding window of 200 agent steps. The inﬂuence models
still maintain an advantage over the baselines and ablated models, suggesting the technique is robust to the hyperparameter
settings.

<!-- page: 19 -->

000
001
002
003
004
005
006
007
008
009
010
011
012
013
014
015
016
017
018
019
020
021
022
023
024
025
026
027
028
029
030
031
032
033
034
035
036
037
038
039
040
041
042
043
044
045
046
047
048
049
050
051
052
053
054
Supplementary Material for Social Inﬂuence as Intrinsic Motivation
for Multi-Agent Deep Reinforcement Learning
Anonymous Authors1
1. Inﬂuence as Mutual Information
The causal inﬂuence of agentk on agentj is:
DKL
[
p(aj
t|ak
t,zt)
p(aj
t|zt)
]
, (1)
wherezt represents the conditioning variables at timestep
t,zt =⟨uj
t,sj
t⟩. The inﬂuence reward to the mutual infor-
mation (MI) between the actions of agentsk andj, which
is given by
I(Aj;Ak|z) =
∑
ak,aj
p(aj,ak|z) log p(aj,ak|z)
p(aj|z)p(ak|z)
=
∑
ak
p(ak|z)DKL
[
p(aj|ak,z )
p(aj|z)
]
,
(2)
where we see that the DKL factor in Eq. 2 is the causal
inﬂuence reward given in Eq. 1.
By sampling N independent trajectories τn from the en-
vironment, where k’s actionsak
n are drawn according to
p(ak|z), we perform a Monte-Carlo approximation of the
MI (see e.g. ?),
I(Ak;Aj|z) = Eτ
[
DKL
[
p(Aj|Ak,z )
p(Aj|z)
]⏐⏐⏐z
]
≈ 1
N
∑
n
DKL
[
p(Aj|ak
n,z )
p(Aj|z)
]
. (3)
Thus, in expectation, the social inﬂuence reward is the MI
between agents’ actions.
Whether the policy trained with Eq. 1 actually learns to
approximate the MI depends on the learning dynamics. We
calculate the intrinsic social inﬂuence reward using Eq. 1,
because unlike Eq. 2, which gives an estimate of the sym-
metric bandwidth betweenk andj, Eq. 1 gives the directed
causal effect of the speciﬁc action taken by agentk,ak
t . We
1Anonymous Institution, Anonymous City, Anonymous Region,
Anonymous Country. Correspondence to: Anonymous Author
<anon.email@domain.com>.
Preliminary work. Under review by the International Conference
on Machine Learning (ICML). Do not distribute.
believe this will result in an easier reward to learn, since it
allows for better credit assignment; agentk can more easily
learn which of its actions lead to high inﬂuence.
The connection to mutual information is interesting, because
a frequently used intrinsic motivation for single agent RL
is empowerment, which rewards the agent for having high
mutual information between its actions and the future state
of the environment (e.g. ??). To the extent that the social
inﬂuence reward approximates the MI, k is rewarded for
having empowerment overj’s actions.
The social inﬂuence reward can also be computed using
other divergence measures besides KL-divergence. ? pro-
pose local information ﬂow as a measure of direct causal
effect; this is equivalent to thepointwise mutual information
(the innermost term of Eq. 3), given by:
pmi(ak;aj|Z =z) = log p(aj|ak,z )
p(aj|z)
= log p(ak,aj|z)
p(ak|z)p(aj|z). (4)
The PMI gives us a measure of inﬂuence of a single action
ofk on the single action taken byj. The expectation of the
PMI overp(aj,ak|z) is the MI. We experiment with using
the PMI and a number of divergence measures, including
the Jensen-Shannon Divergence (JSD), and ﬁnd that the
inﬂuence reward is robust to the choice of measure.
2. Sequential Social Dilemmas
Figure 1 depicts the SSD games under investigation. In
each of the games, an agent is rewarded +1 for every apple
it collects, but the apples are a limited resource. Agents
have the ability to punish each other with a ﬁning beam,
which costs−1 reward to ﬁre, and ﬁnes any agent it hits
−50 reward.
In Cleanup (a public goods game) agents must clean a
river before apples can grow, but are not able to harvest
apples while cleaning. In Harvest (a common pool resource
game), apples respawn at a rate proportional to the amount
of nearby apples; if apples are harvested too quickly, they
will not grow back. Both coordination, and cooperation
are required to solve both games. In Cleanup, agents
arXiv:1810.08647v4  [cs.LG]  18 Jun 2019

<!-- page: 20 -->

055
056
057
058
059
060
061
062
063
064
065
066
067
068
069
070
071
072
073
074
075
076
077
078
079
080
081
082
083
084
085
086
087
088
089
090
091
092
093
094
095
096
097
098
099
100
101
102
103
104
105
106
107
108
109
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Figure 1: The two SSD environments, Cleanup (left) and Harvest (right). Agents can exploit other agents for immediate
payoff, but at the expense of the long-term collective reward of the group. Reproduced with permission from ?.
(a) Cleanup
 (b) Harvest
Figure 2: Schelling diagrams for the two social dilemma tasks show that an individual agent is motivated to defect, though
everyone beneﬁts when more agents cooperate. Reproduced with permission from ?.
must efﬁciently time harvesting apples and cleaning
the river, and allow agents cleaning the river a chance
to consume apples. In Harvest, agents must spatially
distribute their harvesting, and abstain from consuming
apples too quickly in order to harvest sustainably. The
code for these games, including hyperparameter settings
and apple and waste respawn probabilities, can be found
at https://github.com/eugenevinitsky/
sequential_social_dilemma_games.
The reward structure of the games is shown in Figure 2,
which gives the Schelling diagram for both SSD tasks under
investigation. A Schelling diagram (??) depicts the relative
payoffs for a single agent’s strategy given a ﬁxed number
of other agents who are cooperative. These diagrams show
that all agents would beneﬁt from learning to cooperate,
because even the agents that are being exploited get higher
reward than in the regime where all agents defect. However,
traditional RL agents struggle to learn to cooperate and solve
these tasks effectively (?).
3. Additional experiment - Box Trapped
As a proof-of-concept experiment to test whether the inﬂu-
ence reward works as expected, we constructed a special
environment, shown in Figure 3. In this environment, one
agent (teal) is trapped in a box. The other agent (purple) has
a special action it can use to open the box... or it can simply
choose to consume apples, which exist outside the box and
are inexhaustible in this environment.
As expected, a vanilla A3C agent learns to act selﬁshly; the
Figure 3: The Box trapped environment in which the teal
agent is trapped, and the purple agent can release it with a
special open box action.
purple agent will simply consume apples, and chooses the
open box action in 0% of trajectories once the policy has con-
verged. A video of A3C agents trained in this environment
is available at: https://youtu.be/C8SE9_YKzxI,
which shows that the purple agent leaves its compatriot
trapped in the box throughout the trajectory.
In contrast, an agent trained with the social inﬂuence re-
ward chooses the open box action in 88% of trajectories,
releasing its fellow agent so that they are both able to
consume apples. A video of this behavior is shown at:
https://youtu.be/Gfo248-qt3c. Further, as Fig-
ure 4 reveals, the purple inﬂuencer agent usually chooses
to open the box within the ﬁrst few steps of the trajetory,
giving its fellow agent more time to collect reward.
Most importantly though, Figure 5 shows the inﬂuence re-

<!-- page: 21 -->

110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
ward over the course of a trajectory in the Box trapped
environment. The agent chooses the open box action in
the second timestep; at this point, we see a corresponding
spike in the inﬂuence reward. This reveals that the inﬂuence
reward works as expected, incentivizing an action which
has a strong — and in this case, prosocial — effect on the
other agent’s behavior.
Figure 4: Number of times the open box action occurs at
each trajectory step over 100 trajectories.
Figure 5: Inﬂuence reward over a trajectory in Box trapped.
An agent gets high inﬂuence for letting another agent out of
the box in which it is trapped.
4. Implementation details
All models are trained with a single convolutional layer with
a kernel of size 3, stride of size 1, and 6 output channels.
This is connected to two fully connected layers of size 32
each, and an LSTM with 128 cells. We use a discount factor
γ =.99. The number of agentsN is ﬁxed to 5.
In addition to the comparison function used to compute
inﬂuence (e.g. KL-divergence, PMI, JSD), there are many
other hyperparameters that can be tuned for each model.
We use a random search over hyperparameters, ensuring
a fair comparison with the search size over the baseline
parameters that are shared with the inﬂuence models. For
all models we search for the optimal entropy reward and
learning rate, where we anneal the learning rate from an
initial value lr init to lr final. The below sections
give the parameters found to be most effective for each of
the three experiments.
4.1. Basic inﬂuence hyperparameters
In this setting we vary the number of inﬂuencers from 1− 4,
the inﬂuence reward weightβ, and the number of curricu-
lum steps over which the weight of the inﬂuence reward
is linearly increased C. In this setting, since we have a
centralised controller, we also experiment with giving the
inﬂuence reward to the agent being inﬂuenced as well, and
ﬁnd that this sometimes helps. This ‘inﬂuencee’ reward is
not used in the other two experiments, since it precludes
independent training. The hyperparameters found to give
the best performance for each model are shown in Table 1.
4.2. Communication hyperparameters
Because the communication models have an extra A2C out-
put head for the communication policy, we use an additional
entropy regularization term just for this head, and apply a
weight to the communication loss in the loss function. We
also vary the number of communication symbols that the
agents can emit, and the size of the linear layer that con-
nects the LSTM to the communication policy layer, which
we term the communication embedding size. Finally, in the
communication regime, we experiment to setting the weight
on the extrinsic reward E,α, to zero. The best hyperparam-
eters for each of the communication models are shown in
Table 2.
4.3. Model of other agents (MOA) hyperparameters
The MOA hyperparameters include whether to only train
the MOA with cross-entropy loss on the actions of agents
that are visible, and how much to weight the supervised loss
in the overall loss of the model. The best hyperparameters
are shown in Table 3.
4.4. Communication analysis
The speaker consistency metric is calculated as:
N∑
k=1
0.5[
∑
c
1− H(p(ak|mk =c))
Hmax
+
∑
a
1− H(p(mk|ak =a))
Hmax
], (5)
whereH is the entropy function andHmax is the maximum
entropy based on the number of discrete symbols or actions.

<!-- page: 22 -->

165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Cleanup Harvest
Hyperparameter A3C
baseline
Visible actions
baseline Inﬂuence A3C
baseline
Visible actions
baseline Inﬂuence
Entropy reg. .00176 .00176 .000248 .000687 .00184 .00025
lr init .00126 .00126 .00107 .00136 .00215 .00107
lr end .000012 .000012 .000042 .000028 .000013 .000042
Number of inﬂuencers - 3 1 - 3 3
Inﬂuence weightβ - 0 .146 - 0 .224
CurriculumC - - 140 - - 140
Policy comparison - - JSD - - PMI
Inﬂuencee reward - - 1 - - 0
Table 1: Optimal hyperparameter settings for the models in the basic inﬂuence experiment.
Cleanup Harvest
Hyperparameter A3C
baseline
Comm.
baseline
Inﬂuence
comm.
A3C
baseline
Comm.
baseline
Inﬂuence
comm.
Entropy reg. .00176 .000249 .00305 .000687 .000174 .00220
lr init .00126 .00223 .00249 .00136 .00137 .000413
lr end .000012 .000022 .0000127 .000028 .0000127 .000049
Inﬂuence weightβ - 0 2.752 - 0 4.825
Extrinsic reward
weightα - - 0 - - 1.0
CurriculumC - - 1 - - 8
Policy comparison - - KL - - KL
Comm. entropy reg. - - .000789 - - .00208
Comm. loss weight - - .0758 - - .0709
Symbol vocab size - - 9 - - 7
Comm. embedding - - 32 - - 16
Table 2: Optimal hyperparameter settings for the models in the communication experiment.
The goal of the metric is to measure how much of a 1:1
correspondence exists between a speaker’s action and the
speaker’s communication message.
5. Additional results
5.1. Basic inﬂuence emergent communication
Figure 6 shows an additional moment of high inﬂuence in
the Cleanup game. The purple inﬂuencer agent can see the
area within the white box, and therefore all of the apple
patch. The ﬁeld-of-view of the magenta inﬂuencee is out-
lined with the magenta box; it cannot see if apples have
appeared, even though it has been cleaning the river, which
is the action required to cause apples to appear. When the
purple inﬂuencer turns left and does not move towards the
apple patch, this signals to the magenta agent that no apples
have appeared, since otherwise the inﬂuence would move
right.
5.2. Optimizing for collective reward
In this section we include the results of training explicitly
prosocial agents, which directly optimize for the collective
reward of all agents. Previous work (e.g. ?) has shown that
training agents to optimize for the rewards of other agents
can help the group to obtain better collective outcomes.
Figure 6: A moment of high inﬂuence between the purple
inﬂuencer and magenta inﬂuencee.
Following a similar principle, we implemented agents that
optimize for a convex combination of their own individual
reward ek
t and the collective reward of all other agents,∑N
i=1,i̸=kei
t. Thus, the reward function for agentk isrk
t =
ek
t +η∑N
i=1,i̸=kei
t. We conducted the same hyperparameter
search over the parameters mentioned in Section 4.1 varying
the weight placed on the collective reward,η∈ [0, 2].
As expected, we ﬁnd that agents trained to optimize for
collective reward attain higher collective reward in both

<!-- page: 23 -->

220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Cleanup Harvest
Hyperparameter A3C
baseline
MOA
baseline
Inﬂuence
MOA
A3C
baseline
MOA
baseline
Inﬂuence
MOA
Entropy reg. .00176 .00176 .00176 .000687 .00495 .00223
lr init .00126 .00123 .00123 .00136 .00206 .00120
lr end .000012 .000012 .000012 .000028 .000022 .000044
Inﬂuence weightβ - 0 .620 - 0 2.521
MOA loss weight - 1.312 15.007 - 1.711 10.911
CurriculumC - - 40 - - 226
Policy comparison - - KL - - KL
Train MOA only
when visible - False True - False True
Table 3: Optimal hyperparameter settings for the models in the model of other agents (MOA) experiment.
(a) Cleanup
 (b) Tragedy
Figure 7: Total collective reward obtained by agents trained
to optimize for the collective reward, for the 5 best hyperpa-
rameter settings with 5 random seeds each. Error bars show
a 99.5% conﬁdence interval (CI) computed within a sliding
window of 200 agent steps.
Cleanup and Harvest, as is shown in Figure 7. In both
games, the optimal value forη = 0.85. Interestingly, how-
ever, the equality in the individual returns for these agents
is extremely low. Across the hyperparameter sweep, no
solution to the Cleanup game which scored more than 20
points in terms of collective return was found in which all
agents scored an individual return above 0. It seems that in
Cleanup, when agents are trained to optimize for collective
return, they converge on a solution in which some agents
never receive any reward.
Note that training agents to optimize for collective reward
requires that each agent can view the rewards obtained by
other agents. As discussed previously, the social inﬂuence
reward is a novel way to obtain cooperative behavior, that
does not require making this assumption.
5.3. Performance comparison between models and
related work
Table 4 presents the ﬁnal collective reward obtained by each
of the models tested in the experiments presented in the
paper. We see that in several cases, the inﬂuence agents
are even able to out-perform the state-of-the-art results on
these tasks reported by ( ?), despite the fact that the solu-
tion proposed by ( ?) requires that agents can view other
agents’ rewards, whereas we do not make this assumption,
and instead only require that agents can view each others’
actions.
5.4. Collective reward and equality
It is important to note that collective reward is not always
the perfect metric of cooperative behavior, a ﬁnding that was
also discovered by ? and emphasized by ?. In the case, we
ﬁnd that there is a spurious solution to the Harvest game, in
which one agent fails to learn and fails to collect any apples.
This leads to very high collective reward, since it means
there is one fewer agent that can exploit the others, and
makes sustainable harvesting easier to achieve. Therefore,
for the results shown in the paper, we eliminate any random
seed in Harvest for which one of the agents has failed to
learn to collect apples, as in previous work (?).
However, here we also present an alternative strategy for as-
sessing the overall collective outcomes: weighting the total
collective reward by an index of equality of the individual
rewards. Speciﬁcally, we compute the Gini coefﬁcient over
theN agents’ individual environmental rewardsek
t :
G =
∑N
i=1
∑N
j=1|ei
t−ej
t|
2N∑N
i=1ei
t
, (6)
which gives us a measure of the inequality of the returns,
whereG∈ [0, 1], with G = 0 indicating perfect equality.
Thus, 1−G is a measure of equality; we use this to weight
the collective reward for each experiment, and plot the re-
sults in Figure 8. Once again, we see that the inﬂuence
models give the highest ﬁnal performance, even with this
new metric.
5.5. Collective reward over multiple hyperparameters
Finally, we would like to show that the inﬂuence reward is
robust to the choice of hyperparameter settings. Therefore,
in Figure 9, we plot the collective reward of the top 5 best
hyperparameter settings for each experiment, over 5 random
seeds each. Once again, the inﬂuence models result in higher

<!-- page: 24 -->

275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
Cleanup Harvest
A3C baseline 89 485
Inequity aversion (?) 275 750
Inﬂuence - Basic 190 1073
Inﬂuence - Communication 166 951
Inﬂuence - Model of other agents 392 588
Table 4: Final collective reward over the last 50 agent steps for each of the models considered. Bolded entries represent
experiments in which the inﬂuence models signiﬁcantly outperformed the scores reported in previous work on inequity
aversion(?). This is impressive, considering the inequity averse agents are able to view all other agents’ rewards. We make
no such assumption, and yet are able to achieve similar or superior performance.
collective reward, which provides evidence that the model
is robust to the choice of hyperparameters.

<!-- page: 25 -->

330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
(a) Cleanup - Basic inﬂuence
 (b) Harvest - Basic inﬂuence
(c) Cleanup - Communication
 (d) Harvest - Communication
(e) Cleanup - Model of other agents
 (f) Harvest - Model of other agents
Figure 8: Total collective reward times equality, R∗ (1−G), obtained in all experiments. Error bars show a 99.5%
conﬁdence interval (CI) over 5 random seeds, computed within a sliding window of 200 agent steps. Once again, the models
trained with inﬂuence reward (red) signiﬁcantly outperform the baseline and ablated models.

<!-- page: 26 -->

385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
Supplementary Material for Social Inﬂuence as Intrinsic Motivation for Multi-Agent Deep RL
(a) Cleanup - Basic inﬂuence
 (b) Harvest - Basic inﬂuence
(c) Cleanup - Communication
 (d) Harvest - Communication
(e) Cleanup - Model of other agents
 (f) Harvest - Model of other agents
Figure 9: Total collective reward over the top 5 hyperparameter settings, with 5 random seeds each, for all experiments. Error
bars show a 99.5% conﬁdence interval (CI) computed within a sliding window of 200 agent steps. The inﬂuence models
still maintain an advantage over the baselines and ablated models, suggesting the technique is robust to the hyperparameter
settings.
