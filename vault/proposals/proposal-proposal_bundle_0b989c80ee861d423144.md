---
id: "proposal_bundle_0b989c80ee861d423144"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-18T16:30:51+08:00"
updated_at: "2026-07-18T16:30:51+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e753604a46350e066a104918"]
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
extraction_id: "extraction_5bda5867d1e50385d394c51e"
input_sha256: "4147506b3162fe998a62486da5efde941bb58e754eff8317ab7d394eb7eb1718"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_a25076aa1f135c515237fa48", "target_path": "vault/knowledge/concepts/concept_a25076aa1f135c515237fa48-the-expansion-function𝑓𝐺-𝑠-this-generalizes-a-notion-from-additi.md", "base_sha256": null, "candidate_sha256": "64f43658450a4c2c74ea2b5697bdf4504ac51f584435e5d4b003b8e44dc4dcc6", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0b989c80ee861d423144-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_a25076aa1f135c515237fa48.md", "working_at": "2026-07-18T16:30:51+08:00"}]
existing_context: [{"id": "question_1e0121d4bdc2f58cea1ca426", "type": "question", "title": "“How would j’s action change if I had acted", "path": "vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md", "status": "working", "source_ids": ["source_c019c0a492cc659d7858134d"], "snippet": "…protocols when this is otherwise not possible.\n6. [Modeling] Other Agents\nComputing the causal inﬂuence reward as introduced…", "match_reason": "full-text:body"}, {"id": "claim_wechat_particle_poincare_irrep_20260716", "type": "claim", "title": "该文介绍维格纳观点：粒子可由庞加莱群的不可约表示定义", "path": "vault/memory/claim/claim_wechat_particle_poincare_irrep_20260716.md", "status": "working", "source_ids": ["source_9bcee8e0abc8386cbba43b87"], "snippet": "该文介绍维格纳观点：粒子可由庞加莱群的不可约表示定义。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_lie_group_continuous_symmetry_20260715", "type": "claim", "title": "该文称李群用于描述可连续变化的对称性，并可定量处理洛伦兹变换与自旋概念", "path": "vault/memory/claim/claim_wechat_lie_group_continuous_symmetry_20260715.md", "status": "working", "source_ids": ["source_941321d95232028c233c9433"], "snippet": "# 李群与连续对称\n\n描述连续对称；洛伦兹变换与自旋。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_lie_group_definition_20260715", "type": "claim", "title": "该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合", "path": "vault/memory/claim/claim_wechat_lie_group_definition_20260715.md", "status": "working", "source_ids": ["source_941321d95232028c233c9433"], "snippet": "# 李群定义\n\n群 + 微分流形 + 相容运算。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_godel_first_incompleteness_20260716", "type": "claim", "title": "该文称哥德尔第一不完全性定理表明：在《数学原理》体系中存在既不可证也不可否的佩亚诺算术命题", "path": "vault/memory/claim/claim_wechat_godel_first_incompleteness_20260716.md", "status": "working", "source_ids": ["source_aff280ea206f7233b98afc6a"], "snippet": "# 第一不完全性定理\n\n存在不可判定命题；非「所有问题都可证伪」。", "match_reason": "metadata:domains"}, {"id": "claim_wechat_standard_model_symmetry_group_20260716", "type": "claim", "title": "该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示", "path": "vault/memory/claim/claim_wechat_standard_model_symmetry_group_20260716.md", "status": "working", "source_ids": ["source_9bcee8e0abc8386cbba43b87"], "snippet": "该文称标准模型通常以对称群 SU(3)×SU(2)×U(1) 表示。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e753604a46350e066a104918"}
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
- Extraction：`extraction_5bda5867d1e50385d394c51e`
- 编译前召回已有对象：6
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_a25076aa1f135c515237fa48-the-expansion-function𝑓𝐺-𝑠-this-generalizes-a-notion-from-additi.md
@@ -0,0 +1,247 @@
+---
+id: "concept_a25076aa1f135c515237fa48"
+type: "concept"
+status: "proposal"
+title: "the expansion function𝑓𝐺′(𝑠). This generalizes a notion from additive number theory."
+created_at: "2026-07-18T16:30:51+08:00"
+updated_at: "2026-07-18T16:30:51+08:00"
+aliases: []
+tags: []
+domains: []
+confidence: "unknown"
+source_ids: ["source_e753604a46350e066a104918"]
+relations: [{"type": "derived_from", "target_id": "source_e753604a46350e066a104918", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "deterministic-bounded-bundle-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_e753604a46350e066a104918"
+---
+
+# the expansion function𝑓𝐺′(𝑠). This generalizes a notion from additive number theory.
+
+the expansion function𝑓𝐺′(𝑠). This generalizes a notion from additive number theory.
+
+Theadditiverankofasubset𝑆⊆Nisthefewestcopiesof𝑆whosesumsetequalsN;theasymptotic
+rankis the fewest copies whose sumset is cofinal inN. When𝑆is too sparse for any finite number
+of copies to coverN, these notions break down. Our expansion function measures instead how
+large a ball can be covered by sums of at most𝑠elements from𝐺′—a natural generalization when
+infinite coverage is impossible.
+That we were led to introduce a definition while studying the role of definitions in mathematics
+is perhaps fitting. Definition formation is so natural to mathematical practice that even analyzing
+math requires new definitions.
+5.Application and Outlook
+Can we give AI agents a sense of direction—an automated criterion for which mathematical
+statements merit attention? Surely historical and cultural factors influence human judgments of
+mathematical interest, but here we attempt to identify observables intrinsic to the mathematical
+representations themselves (see also [BDF]).
+Thecentralthesisofthispapersuggestscompressibilityasanaturalcandidate. Hereweconsider
+two types. For any element𝑢in a mathematical corpus, whether a definition, lemma, or theorem,
+define thereductive compression:
+𝑇0(𝑢)= |𝑆|𝐺+|𝐵| 𝐺
+|𝑆|𝐺′\{𝑢}+|𝐵| 𝐺′\{𝑢}
+,
+
+<!-- page: 24 -->
+
+24 VITALY AKSENOV, EVE BODNIA, MICHAEL H. FREEDMAN, AND MICHAEL MULLIGAN
+𝐺 𝐺 ′\{𝑢}
+𝑆|𝑆| 𝐺 |𝑆|𝐺′\{𝑢}
+𝐵|𝐵| 𝐺 |𝐵|𝐺′\{𝑢}
+Table 3.Four measures of an element with signature𝑆(statement) and body𝐵
+(proof). The ratio across rows measures reductive compression; the ratio down the
+𝐺′\{𝑢}column measures deductive compression.
+the ratio of unwrapped to wrapped length for the full element (signature plus body). Here, we are
+using the monoid notation defined in Section 3.7, where|·|𝐺 corresponds to unwrapped length
+and|·| 𝐺′\{𝑢} to wrapped length. Table 3 summarizes the four resulting measures of an element.
+Elements with large𝑇0 (“taste”) live in regions where definitions provide substantial leverage—
+preciselytheregionswehaveidentifiedwithhumanmathematics. Anagentexploringmathematics
+can track the average value of𝑇0 as it explores from region to region. This might assist it in
+staying close to HM. Although this risks biasing the agent toward abstraction—which should not
+be pursued for its own sake—𝑇0 can contribute to an agent’s sense of direction.
+The ratio of wrapped body length to wrapped signature length measures another type of com-
+pressibility,deductive compression7:
+𝐼0(𝑢)= |𝐵|𝐺′\{𝑢}
+|𝑆|𝐺′\{𝑢}
+.
+Elementswithoutbodies(primitives,structuredeclarations,inductivetypes)have𝐼 0=0;theymay
+still achieve high𝑇0 using definitions. Elements with large𝐼0 (“interest”) have short statements
+but long proofs, even after compression. In MathLib, elements with high𝐼0 include the deep
+theoremsofalgebraicgeometryandcategorytheory,wherelayersofabstractioncompressenormous
+unwrapped expressions into manageable statements. One imagines that formalized versions of
+landmark results—Fermat’s Last Theorem, the Poincaré conjecture, resolution of singularities—
+wouldachieveexceptionalcompressionratios, theirtersestatementsbelyingvastproofmachinery.
+Whenstatementsbecomelongenoughtoencodelogicalconundra,𝐼 0 canbegamed: metamath-
+ematical constructions produce arbitrarily large values for elements of questionable interest. For
+example(andwiththankstoSamBuss),thetheoremasserting𝑘-consistency: thataformalsystem
+has no proof of0=1in fewer than𝑘symbols, can have tiny compressed length, since recursive
+function theory allows the rapid description of certain enormously large integers k. However
+Pudlák[Pud86,Pud87]showedthatanyproofofk-consistencyinasufficientlyrich(andconsistent)
+system must have lengthΩ(𝑘1/2)—no system of definitions can shortcut it. By taking𝑘=BB(𝑛),
+BB denoting the Busy Beaver function, one obtains a family of theorems with phenomenally large
+𝐼0≈BB 1/2(𝑘)/log𝑘that few would considerthatinteresting, at least on an individual basis, since
+7Analternativeis|𝐵| 𝐺/|𝑆|𝐺,i.e.,measuredin𝐺ratherthan𝐺 ′\{𝑢},whichmeasurestheprimitiveproof-to-statement
+ratio before compression. This would strongly reward theorems with naive statements (like Fermat’s Last Theorem)
+that require elaborate additional developments (the theory of elliptic curves) for their proof.
+
+<!-- page: 25 -->
+
+COMPRESSION IS ALL YOU NEED: MODELING MATHEMATICS 25
+this is merely one of a huge family, parameterized by𝑘, of similar theorems; individually, they are
+logical curiosities rather than core mathematics.
+5.1.A PageRank-style refinement.The issue is that𝐼 0 treats all high-compression elements
+equally, regardless of their role in the broader mathematical structure. A refinement should
+incorporate not just the compression achieved by an element, but also itsusefulnessin building
+other high-value elements.
+Google’sPageRankalgorithm[BP98]offersanaturalframework. Considerthefulldependency
+graph, with edges pointing from each element to its dependencies. A random walk on this graph
+would accumulate at primitives—the sinks of the DAG—which achieve low compression and are
+notmathematically interestinginthe sensewe seek. The standardfixis teleportation: at eachstep,
+with probability𝛼the walker follows an edge, and with probability1−𝛼it jumps to a random
+node. Even with uniform teleportation, this may produce nontrivial rankings by identifying useful
+elements from graph structure alone. We suggest biasing teleportation toward high-compression
+elements. We parametrically combine our two compression measures into𝐽0 =𝛽𝑇 0+(1−𝛽)𝐼 0
+(after normalizing each to comparable scales) for some0< 𝛽<1, and let an element𝑢be chosen
+as the teleportation destination with probability𝐽0(𝑢)/Í
+𝑣𝐽0(𝑣). The resulting transition matrix is
+𝑃(𝑣,𝑢)=𝛼· 𝑤(𝑢,𝑣)
+𝑊(𝑢) +(1−𝛼)· 𝐽0(𝑣)
+𝑍 ,
+where𝑤(𝑢,𝑣)isthenumberoftimes𝑢references𝑣,𝑊(𝑢)= Í
+𝑥𝑤(𝑢,𝑥)isthetotalreferencecount
+of𝑢, and𝑍= Í
+𝑥𝐽0(𝑥).
+A stationary distribution𝜋satisfies Í
+𝑢𝑃(𝑣,𝑢)𝜋(𝑢)=𝜋(𝑣); standard PageRank theory (i.e.,
+the Perron–Frobenius theorem) guarantees existence and uniqueness since every node has positive
+teleportation probability. Define
+𝐼1(𝑢)=𝜋(𝑢).
+Elements score highly if they are either high-compression themselves (frequent teleportation des-
+tinations) or depended upon by elements that are visited often. This captures “load-bearing”
+elements: those that support the compressible regions of mathematics. We expect that𝛼will need
+to be properly tuned to avoid trivial𝜋, such as when all mass is concentrated at either the axioms
+or the largest𝐽0 elements in the DAG.
+5.2.SomeOpenQuestions.First,thecomputationalchallenge: determiningoptimalcompression
+requires searching over possible definitions, which is computationally expensive. Our interest
+measures assume a fixed set of definitions, but an agent exploring FM would need to propose new
+definitions on the fly. Can this be done efficiently enough to guide exploration?
+Second, definitional compression occupies one extreme of a spectrum. At the other extreme
+is Kolmogorov complexity, which allows arbitrary algorithmic compression but is uncomputable.
+
+<!-- page: 26 -->
+
+26 VITALY AKSENOV, EVE BODNIA, MICHAEL H. FREEDMAN, AND MICHAEL MULLIGAN
+Definitionalcompressionislocalandefficientlyverifiable: applyingadefinitionrequiresonlycheck-
+ing that certain properties have been derived, and the process runs in at most linear time (in Ben-
+nett’s[Ben88]terminology,ithaslow“logicaldepth”). Isthereusefulmiddleground—compression
+methods more powerful than local substitution but still computationally tractable?
+Finally, we note an empirical question for MathLib and similar repositories: Do the proofs of
+“interesting” statements stay close to the ground (using only shallow intermediate lemmas), or
+do they take flight through highly compressed intermediate statements? In physical terms, what
+potential barriers must be overcome to reach deep theorems? The depth and mass distributions
+in Section 3 offer preliminary data, but a systematic study correlating these metrics with human
+judgments of interest remains to be done.
+References
+[BDF] MaissamBarkeshli,MichaelR.Douglas,andMichaelH.Freedman,Artificialintelligenceandthestructure
+of mathematics. To appear.
+[Ben73] Charles H. Bennett,Logical reversibility of computation, IBM Journal of Research and Development17
+(1973), no. 6, 525–532.
+[Ben88] ,Logical depth and physical complexity, The Universal Turing Machine: A Half-Century Survey
+(1988), 227–257.
+[Boo59] William W. Boone,The word problem, Annals of Mathematics70(1959), no. 2, 207–265.
+[BP98] Sergey Brin and Lawrence Page,The anatomy of a large-scale hypertextual web search engine, Computer
+networks and ISDN systems30(1998), no. 1-7, 107–117.
+[CT06] Thomas M. Cover and Joy A. Thomas,Elements of information theory, 2nd ed., Wiley-Interscience, 2006.
+See Chapter 3 for the Asymptotic Equipartition Property and the size of the Typical Set.
+[dMU21] Leonardo de Moura and Sebastian Ullrich,The Lean 4 theorem prover and programming language, Auto-
+mated deduction – cade 28, 2021, pp. 625–635.
+[Gro81] Mikhael Gromov,Groups of polynomial growth and expanding maps, Publications Mathématiques de
+l’IHÉS53(1981), 53–78.
+[Log25] Logical Intelligence,Aleph, 2025.
+[Mat20] Mathlib Community,The Lean mathematical library, Proceedings of the 9th acm sigplan international
+conference on certified programs and proofs (cpp 2020), 2020, pp. 367–381.
+[Mil68] JohnMilnor,Anoteoncurvatureandfundamentalgroup,JournalofDifferentialGeometry2(1968),no.1,
+1–7.
+[Nov55] PyotrS.Novikov,Onthealgorithmicunsolvabilityofthewordproblemingrouptheory,TrudyMatematich-
+eskogo Instituta imeni V.A. Steklova44(1955), 1–143.
+[Pos47] EmilL.Post,RecursiveunsolvabilityofaproblemofThue,TheJournalofSymbolicLogic12(1947),no.1,
+1–11.
+[Pud86] Pavel Pudlák,On the length of proofs of finitistic consistency statements in first order theories, Logic
+colloquium ’84, 1986, pp. 165–196.
+[Pud87] ,Improvedboundstothelengthofproofsoffinitisticconsistencystatements,Logicandcombinatorics,
+1987, pp. 309–331.
+[Sha48] Claude E. Shannon,A mathematical theory of communication, Bell System Technical Journal27(1948),
+no. 3, 379–423. The foundational text for the definition of entropy rate and redundancy in discrete sources.
+
+<!-- page: 27 -->
+
+COMPRESSION IS ALL YOU NEED: MODELING MATHEMATICS 27
+AppendixA.Additional Expansion Theorems
+The following results complete the picture for𝐴1=Nsummarized in Table 1.
+Theorem 6(Double-logarithmic density gives polynomial expansion
+V E R I F I E D
+Lean ).For𝐴 1 =Nand
+any integer𝑏≥2, the macro set𝑀={𝑏 𝑏𝑗
+:𝑗≥0}has double-logarithmic density and satisfies
+𝑐1𝑠𝑏/(𝑏−1)≤𝑓 𝐺′(𝑠)≤𝑐 2𝑠(2𝑏−1)/(𝑏−1)
+for all𝑠≥1, where𝑐 1,𝑐 2>0depend only on𝑏.
+Proof.Let𝑚 𝑗 =𝑏 𝑏𝑗
+for𝑗≥0. The number of macros with𝐺-length at most𝑟is the number of𝑗
+with𝑏 𝑏𝑗
+≤𝑟, i.e.,𝑗≤log 𝑏 log𝑏𝑟. Thus𝑀has double-logarithmic density.
+Greedyrepresentationof𝑚 𝑘−1.Thelargestmacronotexceeding𝑚 𝑘−1is𝑚 𝑘−1. Thenumber
+of copies used is 𝑚𝑘−1
+𝑚𝑘−1
+
+=
+j
+𝑏𝑏𝑘−1(𝑏−1)−𝑏−𝑏𝑘−1k
+=𝑏 𝑏𝑘−1(𝑏−1)−1,
+with remainder𝑚𝑘−1−1. Letting𝑇 𝑘 =|𝑚 𝑘−1| 𝐺′, we obtain
+𝑇𝑘 =(𝑏 𝑏𝑘−1(𝑏−1)−1)+𝑇 𝑘−1, 𝑇 0=𝑏−1.
+The first term dominates:𝑇𝑘∼𝑏 𝑏𝑘−1(𝑏−1).
+The elements𝑚 𝑘−1are hardest to compress.Let𝑆 𝑗 =max{|𝑥| 𝐺′ :𝑥 < 𝑚𝑗}. We claim
+𝑆𝑗 =𝑇 𝑗 for all𝑗≥0. The base case𝑆 0 =𝑇 0 =𝑏−1is clear. For the inductive step, suppose
+𝑆𝑗 =𝑇 𝑗 andconsiderany𝑥with𝑚 𝑗≤𝑥 <𝑚 𝑗+1. Writing𝑥=𝑐 𝑗·𝑚 𝑗+𝑟with0≤𝑟 <𝑚 𝑗,wehave
+|𝑥|𝐺′≤𝑐 𝑗+𝑇𝑗. Since𝑐 𝑗≤𝑏 𝑏𝑗(𝑏−1)−1, we obtain𝑆𝑗+1≤𝑇 𝑗+1. Equality holds at𝑥=𝑚 𝑗+1−1.
+Upperbound.Fix𝑠≥𝑏−1andlet𝑘satisfy𝑇 𝑘≤𝑠<𝑇 𝑘+1. Theelement(𝑠−𝑇 𝑘+1)𝑚𝑘+(𝑚𝑘−1)
+has𝐺′-lengthequalto(𝑠−𝑇 𝑘+1)+𝑇𝑘 =𝑠+1,soitisnotin𝐵 𝐺′(𝑠). Thus𝑓 𝐺′(𝑠)<(𝑠+2)𝑚 𝑘. From
+therecurrence,𝑇 𝑘≥𝑏 𝑏𝑘−1(𝑏−1)−1,so𝑇 𝑘≤𝑠implies𝑏 𝑏𝑘−1(𝑏−1)≤𝑠+1≤2𝑠. Thus,𝑏 𝑘−1≤ log𝑏(2𝑠)
+𝑏−1
+and we have𝑚𝑘 =𝑏 𝑏·𝑏𝑘−1
+≤(2𝑠) 𝑏/(𝑏−1). Therefore𝑓 𝐺′(𝑠)≤𝑐 2𝑠(2𝑏−1)/(𝑏−1) . For𝑠 < 𝑏−1, we
+simply choose𝑐2 sufficiently large.
+Lower bound.With𝑘as above, any𝑥=𝑐·𝑚 𝑘+𝑦with0≤𝑦 <𝑚 𝑘 satisfies|𝑥| 𝐺′≤𝑐+𝑇 𝑘. If
+𝑐≤𝑠−𝑇 𝑘 then𝑥∈𝐵 𝐺′(𝑠), so𝑓 𝐺′(𝑠)≥(𝑠−𝑇 𝑘+1)𝑚 𝑘−1.
+Case𝑠≤2𝑇 𝑘.Then𝑇 𝑘≥𝑠/2, so𝑚 𝑘 =𝑏 𝑏𝑘
+≥𝑐𝑇 𝑏/(𝑏−1)
+𝑘 ≥𝑐(𝑠/2) 𝑏/(𝑏−1) ≥𝑐 1𝑠𝑏/(𝑏−1). Since
+𝑠−𝑇 𝑘+1≥1, we obtain𝑓 𝐺′(𝑠)≥𝑐𝑠 𝑏/(𝑏−1).
+Case𝑠>2𝑇 𝑘.Then𝑠−𝑇 𝑘+1≥𝑠/2. From𝑠<𝑇 𝑘+1≤𝐶𝑏 𝑏𝑘(𝑏−1) we obtain𝑏𝑘≥ log𝑏(𝑠/𝐶)
+𝑏−1 and
+thus𝑚 𝑘 =𝑏 𝑏𝑘
+≥(𝑠/𝐶) 1/(𝑏−1). Therefore𝑓 𝐺′(𝑠)≥(𝑠/2)(𝑠/𝐶) 1/(𝑏−1)≥𝑐 1𝑠𝑏/(𝑏−1).□
+Theorem 7(Finite macro gives linear expansion
+V E R I F I E D
+Lean ).For𝐴 1 =N, let𝑀be a finite macro
+set. Then𝑓 𝐺′(𝑠)=Θ(𝑠).
+Proof.Let𝐿=max{|𝑚| 𝐺 :𝑚∈𝑀}be the largest𝐺-length among all macros.
+
+<!-- page: 28 -->
+
+28 VITALY AKSENOV, EVE BODNIA, MICHAEL H. FREEDMAN, AND MICHAEL MULLIGAN
+Upperbound.Anyelement𝑥with|𝑥| 𝐺′≤𝑠isasumofatmost𝑠generatorsfrom𝐺 ′=𝐺∪𝑀.
+Each generator has𝐺-length at most𝐿, so|𝑥| 𝐺 ≤𝑠𝐿. Thus𝐵 𝐺′(𝑠) ⊆𝐵𝐺(𝑠𝐿), which gives
+𝑓𝐺′(𝑠)≤𝑠𝐿.
+Lower bound.Since𝐺⊆𝐺 ′, we have|𝑥|𝐺′≤|𝑥| 𝐺 for all𝑥. Thus𝐵 𝐺(𝑠)⊆𝐵 𝐺′(𝑠), which
+gives𝑓 𝐺′(𝑠)≥𝑠.
+Combining the bounds gives𝑓𝐺′(𝑠)=Θ(𝑠).□
+Remark6.Theorems 6 and 7 extend to𝐴𝑛 with the macro sets{𝑏𝑏𝑗
+𝑎𝑖 :𝑖=1,...,𝑛,𝑗≥0}and
+any finite𝑀⊆𝐴 𝑛 respectively, yielding the same asymptotic expansion rates.
+Vitaly Aksenov , Logical Intelligence
+Email address:aksenov@logicalintelligence.com
+Eve Bodnia, Logical Intelligence
+Email address:evebodnia@logicalintelligence.com
+Michael H. Freedman, Logical Intelligence; Center of Mathematical Sciences and Applications, Harvard
+University , Cambridge, MA 02138, USA
+Email address:michael.freedman@logicalintelligence.com, mfreedman@cmsa.fas.harvard.edu
+Michael Mulligan, Logical Intelligence; Department of Physics and Astronomy , University of California,
+Riverside, CA 92521, USA
+Email address:michael.mulligan@logicalintelligence.com, michael.mulligan@ucr.edu
```
