# Beyond optics: scientific comparisons for fallible model workflows

Recorded and sources checked: 2026-11-08.

**Status: inactive research. All workflow mechanisms and experiments below are proposals, not active instructions or demonstrated improvements.**

## 1. First separate the mechanisms

The phrase “good output + bad output = bad output” describes a possible failure, not a universal rule. The combining operation matters:

- **Serial dependency:** an uncorrected false premise can invalidate later work that depends on it.
- **Revision after discussion:** a model may abandon a correct answer after seeing persuasive incorrect reasoning.
- **Voting:** a wrong answer may be rejected, accepted, or tied depending on the voters and their error dependence.
- **Verification and selection:** a test may reject a faulty candidate and preserve a correct one, within the test's coverage.
- **Synthesis:** merging individually plausible suggestions can introduce a contradiction or incompatible assumptions.

Correctness can also be local: an answer may contain a correct diagnosis and a bad proposed fix. Tracking individual claims and their dependencies may be more informative than labeling an entire response good or bad.

Direct evidence exists for harmful revision: Wynn, Satija, and Hadfield report multi-agent debates in which models moved from correct answers to incorrect ones after exposure to peer reasoning, including conditions where stronger models were the majority. This establishes a failure mode in their experiments, not a law that incorrect answers always dominate. [Primary research, 2025](https://arxiv.org/abs/2509.05396).

## 2. Genetics: dominance is a limited analogy; epistasis is more useful

**Established concept.** Dominance concerns how alleles relate to an observed trait; it is not a ranking of truth, usefulness, frequency, or moral quality. Epistasis concerns one gene modifying or masking another gene's effect. [NHGRI: dominance](https://www.genome.gov/genetics-glossary/Dominant); [NHGRI: epistasis](https://www.genome.gov/genetics-glossary/Epistasis).

**Possible mapping.** A planning rule, context-selection rule, and verification rule can interact. For example, an otherwise useful “keep trying” instruction could become counterproductive when a broken test reports failure indefinitely. A change may help one model/harness combination but hinder another. This is a proposal about component interactions, not evidence that prompts behave biologically.

**Question it suggests.** Does A help by itself, but become harmful when B is present? Test baseline, A, B, and A+B. On a chosen additive outcome scale, an interaction estimate is `score(A+B) - score(A) - score(B) + score(baseline)`. Results depend on the metric, task mix, and measurement uncertainty.

**Boundary.** Outputs are not paired alleles and a conversation is not inheritance. Calling correctness “recessive” would give a descriptive metaphor more explanatory power than it has. “Which interaction suppresses reliable evidence?” is a better research question.

## 3. DNA sequencing: preserve provenance and distinguish independent evidence

**Established method.** Duplex Sequencing tracks the two complementary strands of a DNA molecule and compares their independently derived sequence evidence. This helps distinguish genuine variants from many amplification or sequencing artifacts. Its physical complementarity provides a constraint that model answers do not possess. [Schmitt et al., PNAS 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3437896/).

**Possible mapping.** Repeated claims derived from one unsupported assertion are copies of one evidence lineage. They are not several independent confirmations. Record where a claim originated and which observations support it before treating repetition as confidence.

Example: a worker says “the feet no longer clip,” a summary repeats that statement, and a reviewer repeats the summary. This is one unverified assertion repeated three times. A raw gameplay capture plus an appropriate geometry measurement would supply different checks, although both could still miss the same issue.

**Possible mechanism.** Preserve raw artifacts and associate each claim with its source, code version, and measurement method. A reviewer could inspect independently collected evidence before reading the worker's interpretation.

**Boundary.** Two LLMs do not provide complementary DNA strands or guaranteed independence. Agreement is supporting evidence only to the extent that their failure modes and underlying observations differ. Correlated model errors are documented even across providers and architectures. [Kim et al., ICML 2025](https://arxiv.org/abs/2506.07962).

## 4. Directed evolution: optimize by variation and selection

**Established method.** Chen and Arnold used repeated mutation and screening to obtain enzyme variants with improved activity in a specified solvent environment. [Original experiment, PNAS 1993](https://pubmed.ncbi.nlm.nih.gov/8516309/).

**Possible mapping.** Candidate skills, task-card formats, routing policies, or prompts are variants. The model, harness, and task distribution form their operating environment. External acceptance criteria provide a selection procedure.

Possible future cycle: retain a baseline, propose a few bounded variants, evaluate them on comparable tasks, and retain improvements that survive held-out checks. Preserve variants that work in different task families rather than force a single global winner.

**Boundary.** Improving a prompt or harness does not train the model's weights. Optimizing for a judge's score can select ways to satisfy that judge without improving the user's actual outcome. A misleading selection test would reward the wrong variants. No unbounded self-improvement loop is proposed here.

## 5. Chemistry: inhibition and reaction conditions

**Established concept.** Chemical systems include substances that accelerate reactions and substances that inhibit reactions or deactivate catalysts. Their effects depend on the particular reaction and conditions. IUPAC distinguishes inhibition and poisoning from the misleading phrase “negative catalysis.” [IUPAC terminology recommendations, 1976](https://publications.iupac.org/pac/1976/pdf/4601x0071.pdf).

**Possible mapping.** A well-placed procedure might shorten a search. An incorrect constraint, stale API assumption, or contradictory instruction might obstruct useful work disproportionately to its token count. This suggests studying the effect and placement of particular context elements instead of assuming that adding more good instructions will dilute a bad one.

**Possible mechanism.** Keep unverified hypotheses distinguishable from verified facts; invalidate an assumption when its supporting evidence fails; compare fresh-context recovery with repeatedly appending corrections to the same conversation.

**Boundary.** There is no demonstrated chemical concentration law for prompt influence. More tokens are not necessarily a higher “dose,” and a helpful instruction can be harmful on a different task. This analogy is useful for formulating experiments, not predicting numerical performance.

Source access note: the IUPAC definition was available in the search index; direct retrieval of the PDF and Gold Book pages returned access errors during this review. The chemistry claim here is limited to that indexed definition.

## 6. Social influence: agreement can replace independent judgment

**Established finding.** In Lorenz and colleagues' estimation experiments, seeing other people's estimates reduced the diversity of answers without a corresponding improvement in collective error. This is a result for the studied setting, not a claim that collaboration always harms accuracy. [Lorenz et al., PNAS 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299/).

**Possible mapping.** Shared conclusions may reduce disagreement because reviewers conform, rather than because new evidence resolves the question. This is closer to the observed harmful-revision mechanism than genetic dominance is.

**Possible mechanism.** Record initial independent judgments, reveal peer reasoning afterward, and require an evidence-linked reason for changing a judgment. Track correct-to-incorrect and incorrect-to-correct revisions separately. Distinguish a justified correction from agreement for its own sake.

**Boundary.** Human social psychology does not by itself establish model behavior. The direct model-debate paper in section 1 provides the relevant model-specific evidence. Independence must be balanced against the benefit of sharing real discoveries.

## 7. Reliability engineering: prevent one mistake from spreading

Reframed after user feedback: the previous explanation focused too much on combining models. The useful question is: **What would have to go wrong for us to accept an incorrect result, and where could we interrupt that chain?**

Consider two backup devices that share one failed power supply. Counting the devices overstates their protection. In a model workflow, three reviewers relying on the same faulty test can have the same problem: the shared input defeats all three checks.

A proposed game-workflow analysis would start with “an unfinished feature is accepted as complete,” then trace possible causes: the wrong build was tested; the test misses the defect; a reviewer trusts an unsupported summary; or acceptance proceeds despite missing evidence. Different causes call for different repairs. Replacing a model will not repair a shared broken test. A small defect confined to one task should not automatically contaminate the whole queue.

Fault-tree analysis works backward from an undesired result through combinations of causes, including failures that have a shared cause. [NASA Fault Tree Handbook](https://s3vi.ndc.nasa.gov/ssri-kb/static/resources/Fault%20Tree%20Handbook_NASA.pdf). The example above is our proposed application, not a NASA finding about LLMs.

**Established framework.** Software fault tolerance includes error detection, recovery, and multiple implementations whose differing failure modes may provide redundancy. These approaches depend on their assumptions about failures and acceptance checks. [Torres-Pomales, NASA, 2000](https://ntrs.nasa.gov/citations/20000120144).

**Possible mapping.** Treat a generated answer as a fallible component, and its reviewer, test runner, merger, and acceptance rule as additional fallible components. Identify where an error can propagate and where it can be detected or contained.

An illustrative calculation, not a model benchmark:

- Three independent binary voters, each wrong with probability 0.1, have majority error `3 * 0.1^2 * 0.9 + 0.1^3 = 0.028`.
- If all three always share the same errors, their majority error stays 0.1.
- A serial process that succeeds only if all three independent stages succeed has success `0.9^3 = 0.729`.

These are different architectures, so the same component accuracies imply different system outcomes. Real model tasks violate many of these assumptions: errors correlate, tasks differ, stages can repair errors, and some outputs cannot be reduced to binary votes.

**Possible mechanism.** Narrow acceptance gates and recoverable checkpoints could prevent one uncertain claim from becoming a global premise. A different model is useful only when it supplies a capability or failure pattern that adds value; counting models alone is insufficient.

**Boundary.** A faulty test or shared specification can fool every implementation. No voting rule guarantees truth without additional assumptions and evidence.

## 8. Fit to the user's questions

| Question | Most useful lens to investigate | Why |
| --- | --- | --- |
| Why can a wrong suggestion override a correct one? | Social influence and harmful revision | Studies the actual direction of answer changes |
| Why do useful skills sometimes conflict? | Epistasis and factorial experiments | Makes interaction effects explicit |
| Does repeated agreement provide new evidence? | Sequencing provenance and correlated errors | Separates independent observations from copied claims |
| How might skills or routing improve over time? | Directed evolution with held-out selection | Separates proposing variants from judging them |
| Why can one bad assumption waste so much work? | Inhibition and dependency propagation | Focuses on obstructing assumptions and their downstream effects |
| How should Ladder combine models? | Reliability engineering | Examines routing, verification, recovery, and shared failures |

No single field supplies a complete model. Optics remains useful for attention and measurement; the alternatives explain other mechanisms more precisely.

## 9. Parked experiment ideas — not a queue

All experiments require a later decision to proceed. No models are being launched or settings changed for them.

| ID | Question | Comparison | Essential measurement |
| --- | --- | --- | --- |
| R01 | When does bad advice displace a correct answer? | Isolated judgment versus exposure to correct/incorrect peer advice, with order randomized | Correct-to-incorrect and incorrect-to-correct rates, plus final accuracy |
| R02 | Does independent evidence outperform repeated agreement? | Copies of one report versus separately collected observations on the same cases | False acceptance, missed defects, evidence dependence, and collection cost |
| R03 | Do precise cards and separate review interact? | Baseline, cards, review, cards+review | Accepted outcomes and total cost/time; interaction with uncertainty |
| R04 | Can a false assumption be contained? | Same controlled task with/without one plausible false premise; compare recovery strategies | Error propagation, recovery success, and wasted work |
| R05 | Can skill variants improve without overfitting? | Baseline and bounded variants on development tasks, then held-out tasks | Accepted outcomes, regressions, and full end-to-end cost |

If revisited, use isolated test copies or fixtures rather than introduce deliberate faults into a running production task. Keep model versions, effort, tools, and task difficulty recorded; repeat trials; choose acceptance criteria before seeing results. Ambiguous visual judgments require separate treatment from executable correctness checks.

Cost accounting would include planner/reviewer tokens, worker retries, evidence generation, repair time, and local compute time. An analogy becomes worth adopting only if its proposed mechanism improves measured outcomes enough to justify that overhead.

## 10. Further fields — hypotheses and design ideas, still inactive

### Control theory: observations and corrective actions

Control theory studies how measurements and feedback relate to a system's behavior. Observability concerns what internal state can be recovered from available measurements; feedback delay can affect stability. [Caltech: output feedback](https://murray.cds.caltech.edu/CDS_101/110_-_Output_Feedback); [Caltech: loop analysis](https://murray.cds.caltech.edu/CDS_101/110_-_Loop_Analysis).

**Proposed transfer:** if screenshots cannot distinguish two suspected causes, adding another reviewer may not help; obtain a better observation first. Repeatedly changing several game settings in response to stale captures could produce alternating corrections. A future pilot could compare broad repeated edits with bounded edits followed by fresh, version-matched observations. Measure whether the target improves and how often previously corrected defects return.

**Limit:** an agent workflow is not automatically a linear control system. A formal stability guarantee would require an actual model and validated assumptions. Review on every tool call is not implied.

### Metrology: inspect the measuring instrument

Measurement science separates uncertainty contributions and documents how a measurement was obtained. NIST explicitly distinguishes the method used to evaluate uncertainty from whether its source is random or systematic. [NIST uncertainty components](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-d2-identification-uncertainty-components).

**Proposed transfer:** a judge may be consistent but miss a category of defect. Before interpreting a score improvement, examine whether camera angle, lighting, test fixtures, runtime differences, or judge errors could explain it. Reference cases with known defects could reveal a check that never detects the relevant failure. Repeatability, correctness, and coverage are separate questions.

**Limit:** subjective visual preferences have no universal reference value. Known mechanical defects and user preferences need different evaluation methods; an LLM's self-reported confidence is not a calibrated uncertainty interval.

### Active learning and decision theory: choose the next useful observation

Research on active learning with real annotation costs studies both the information obtained and the varying expense of obtaining labels. [Settles, Craven, and Friedland, 2008; authors' publication record](https://burrsettles.com/publications), [paper](https://burrsettles.com/pub/settles.nips08ws.pdf).

**Proposed transfer:** select a capture, test, or human question that could distinguish competing explanations and change the next action. If the alternatives are “collision defect” and “visual pose defect,” one synchronized movement/geometry trace may be more informative than ten similar screenshots. In an image tournament, a small informative set might reduce repetitive voting.

**Limit:** uncertainty alone can select distracting outliers. Selection should account for task relevance and cost, and retain representative checks to expose shared blind spots. This proposed use selects diagnostic evidence; it does not necessarily train model weights. No numerical information gain or savings has been measured here.

### Statistical physics: annealing and escaping a local optimum

Simulated annealing adapts an idea from statistical mechanics into optimization: controlled acceptance of worse intermediate candidates can help a search move beyond local optima, with acceptance changing over the search schedule. [Kirkpatrick, Gelatt, and Vecchi, Science 1983](https://www.ida.liu.se/~zebpe83/heuristic/papers/sa_science.pdf).

**Proposed transfer:** when small rendering tweaks stop producing a meaningful improvement, compare a few substantially different approaches in isolated branches or fixtures, then concentrate work on a promising approach. Preserve the best verified version while exploring. An example would be comparing a new plant representation against further tweaks to the existing primitive mesh.

**Limit:** a casual exploration schedule is not a full simulated-annealing implementation. Algorithmic temperature is not automatically equivalent to an LLM's sampling temperature. This does not justify accepting regressions into the main game or promise finding the global best design.

### Operations research: completed outcomes and bottlenecks

Little's law relates average work in a queue, throughput, and time spent in the system under its assumptions. It does not say that starting more work increases completion capacity. [Little, Operations Research 1961](https://pubsonline.informs.org/doi/epdf/10.1287/opre.9.3.383).

**Proposed transfer:** measure tasks waiting for implementation, evidence, and review separately. If review is the limiting stage, adding more implementation workers could build a review backlog instead of increasing verified completions. On a host with one loaded large model, model switches and shared browser/GPU use also belong in scheduling measurements. A future pilot could compare review batch sizes or work-in-progress limits.

**Limit:** the finite game queue is not necessarily stationary, and task sizes differ. Use measured stage times and dependencies; do not apply a steady-state formula as an exact project-duration prediction.

## 11. Which idea belongs where?

These are potential methods to select for a concrete question, not a requirement to run every scientific analogy on every task. A stable command belongs in tooling, a known defect in its owning code, and an uncertain reusable workflow change may justify an experiment. See the [inactive experiment skill design](EXPERIMENT_SKILL_DESIGN.md) for the proposed division of responsibilities with Mason.
