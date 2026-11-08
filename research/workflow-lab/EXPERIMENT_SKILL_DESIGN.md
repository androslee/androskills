# Proposed occasional experiment skill

Date: 2026-11-08. **Inactive design only. No skill has been created, installed, or activated; no experiment has been run.**

## Purpose and distinction

The scientific principles are established in their own fields. Their proposed transfer to this model/harness setup is what needs testing. “Experiment” means comparing a concrete intervention against a suitable baseline to answer an uncertain question. It does not mean rerunning basic science or treating every routine fix as a research project.

A possible name is `assay` or `workflow-experiment`; naming is unresolved. The reusable capability would be designing and interpreting bounded workflow comparisons. The science analogies would supply optional methods and questions, loaded only when relevant.

## Mason's role

The current [Mason skill](../../skills/mason/SKILL.md) already addresses recurring costs, simpler alternatives, expected benefit, and the option to recommend no change. Its [evaluation reference](../../skills/mason/references/evaluation.md) already covers baselines, comparable isolated tasks, held-out cases, costs, model escalation, and retirement.

The proposal therefore overlaps real existing coverage. Immediate implementation is unnecessary. A future standalone skill would make sense if experiment design is reused by Mason, Ladder, Downshift, model/provider comparisons, or the generation arena and needs substantive methods beyond Mason's reference. Otherwise improving that reference would be smaller and easier to maintain. A later extraction should leave one maintained procedure, not conflicting copies.

Proposed responsibilities:

| Role | Question it answers | Output |
| --- | --- | --- |
| Mason | Is there an evidenced, reusable problem worth changing? | A narrow candidate, simpler alternatives, and remaining uncertainty |
| Experiment capability | What comparison could resolve that uncertainty at acceptable cost? | A bounded protocol, collected observations, and a qualified result |
| Ladder / Downshift | Which available models perform the scoped work and review? | Authorized routing or a written handoff |
| Harness / scripts | Can the protocol be executed reproducibly and within limits? | Isolated states, timestamps, usage logs, artifacts, and enforced limits where supported |
| Owner of the skill or code | Should the tested change be adopted for the stated scope? | Keep, narrow, revise, reject, or leave inconclusive |

These are logical responsibilities. They do not require five agents, multiple providers, or a higher model. A skill does not itself schedule background runs, enforce a budget, or switch models.

## When an experiment would be worthwhile

Use would be event-driven and occasional: a recurrent costly problem or consequential reusable decision has at least two plausible explanations or interventions, existing evidence does not resolve them, and a bounded comparison could change what we do.

Useful signals include conflicting independent observations, a proposed combination of individually useful skills, an uncertain routing change, or a claimed efficiency gain that may instead reflect easier tasks. Expected value depends on avoided future mistakes and reuse as well as the experiment's cost; avoid inventing precise probabilities to make that case look quantitative.

Nearby cases where it should abstain:

- A reproducible bug has a clear correction and an appropriate regression check.
- The needed fact can be obtained by inspecting a file, log, or official API documentation.
- Existing evidence already resolves the choice.
- It is a one-off preference decision with little transferable value.
- Acceptance cannot yet be defined or the proposed measurements cannot distinguish the alternatives.
- The comparison would cost more than it could plausibly save, or its useful results would arrive too late.
- The user has requested that the idea remain inactive, as in this research collection.

Abstention does not prevent ordinary task completion or direct debugging.

## Proposed procedure

1. **State the decision and competing explanations.** Example: “Does earlier review reduce rework enough to cover its cost?” Record what finding would change the decision. Avoid starting from “prove this skill helps.”
2. **Choose a mechanism and the smallest relevant comparison.** Interactions suggest a factorial comparison; copied evidence suggests a provenance check; a blind judge suggests calibration; a stall suggests a targeted diagnostic. Avoid loading every method or searching every science.
3. **Define success, quality constraints, and limits before running.** Include full cost, false acceptance, regressions, and task completion. Set a time/cost/trial limit and stopping rule appropriate to the decision. A short pilot may justify a scoped next step without proving broad savings.
4. **Preserve comparable starting states and raw evidence.** Keep task/model/tool versions, context, cached work, and changed variables recorded. Use isolated copies and fresh contexts where needed. A first run must not quietly teach a second run the answer. Randomize or counterbalance order when it can affect the result.
5. **Collect evidence with the least costly adequate method.** Prefer deterministic measurements where they answer the question. A cheaper model can run tests, capture screenshots, and organize artifacts under a clear protocol. Its summary is distinct from the evidence.
6. **Evaluate against the declared decision.** Use held-out tasks for claims of transfer. For consequential or ambiguous claims, a reviewer can first inspect raw outcomes without seeing the preferred interpretation. Correctness of that reviewer also has limits.
7. **Return a bounded disposition.** Keep for a specified scope, narrow, revise once within budget, reject, or leave inconclusive. Report negative results. Do not promote an intervention merely because it was drafted, a small example worked, or a reviewer liked it.

No recursive chain of “experiment on the experiment skill” is proposed. A material protocol defect can invalidate a result and justify a repair; otherwise the experiment ends at its declared limit. Revisit a rejected idea when new evidence or changed conditions matter, not on every Mason review.

## Model cost and handoffs

Start with the current model for triage. A stronger model may be worth its cost when the uncertainty is experimental design, causal interpretation, or conflicting evidence. It need not watch every run. A cheaper model or deterministic runner can perform repeated trials and produce a compact evidence packet; a stronger reviewer can inspect a limited, representative sample and the measurements.

For two harnesses, protocol and result files would carry exact starting state, acceptance criteria, artifact paths, measurements, uncertainty, and remaining decisions. For one harness the same logical contract could be passed directly. This is a proposed reuse of Downshift, not a new runtime or automatic routing mechanism.

## Candidate result record

A compact record could contain: decision; evidence and alternatives; intervention and baseline; changed variables; task/model/tool versions; quality constraints; budget; raw artifact references; observed results and total cost; uncertainties; disposition and scope; condition for revisiting.

Token counts, currency, local runtime, and human review time should remain distinguishable. If usage is unavailable, savings remain unknown. Fewer tokens alone is not success if the result omits required work.

## Examples for a future pilot

| Observation | Proposed question | Appropriate result |
| --- | --- | --- |
| A local worker repeats edits after ambiguous screenshots | Does a targeted geometry trace resolve the ambiguity faster than another visual review? | A scoped evidence-collection decision, not a global model ranking |
| Two useful skills conflict in one task family | Does their combination change outcomes beyond either alone? | A trigger restriction or compatibility finding, including uncertainty |
| All reviewers accept the same wrong result | Are their judgments independent, or derived from one faulty test/report? | Repair the shared evidence source or compare an additional method |
| Work becomes faster after new task cards | Is the improvement due to the cards, task difficulty, cached work, or skipped verification? | A matched comparison or an honest statement that attribution is unresolved |
| A known launch script fails deterministically | No open workflow question remains | Fix the script and verify; abstain from an experiment skill |

## Current disposition

Preserve this design and broaden the research library. Existing Mason evaluation guidance can serve already-authorized reviews. The proposed scientific applications and standalone skill remain parked; planning a test, authorizing its execution, and adopting its result are separate decisions.
