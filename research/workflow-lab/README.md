# Workflow Lab: parked research proposals

Recorded: 2026-11-08. **Status: inactive research; no pilots have run and no new skills are installed or activated by this collection.**

This is an optional research catalog for Mason and other workflow reviews. It preserves ideas about improving verified outcomes and total cost, together with their scientific origins, limits, and questions worth testing. Scientific foundations do not establish that the proposed applications improve an agent workflow.

These documents are deliberately outside `skills/` and have no `SKILL.md` entrypoints. The existing skill inventory does not install or route to them. Reading a proposal is distinct from authorizing a test or adopting a change.

## Find the relevant material

- [Scientific comparisons](SCIENCE_COMPARISONS.md): mechanisms, proposed applications, limitations, primary sources, and five parked experiment ideas.
- [Experiment capability design](EXPERIMENT_SKILL_DESIGN.md): a possible occasional skill, its relationship to Mason, its abstention conditions, and existing coverage that may make a separate skill unnecessary.
- [Optics archive](OPTICS_IDEAS.md): the original lens, measurement, calibration, context-selection, and feedback proposals, with the limits of the analogy.
- Existing [Mason](../../skills/mason/SKILL.md) and [evaluation procedure](../../skills/mason/references/evaluation.md): the current reusable review process. This catalog does not replace or modify them.

## Candidate catalog

Each `WL-*` ID identifies a hypothesis family, not a task assignment. All entries are **parked**: applications untested, total savings unknown, activation inactive. Preserve IDs when titles change. The R01–R05 labels in the scientific notes identify suggested comparisons, not additional active work.

| ID | Candidate | Reconsider when | Possible intervention and first question |
| --- | --- | --- | --- |
| WL-01 | Epistasis / instruction interactions | Individually useful skills or rules appear to conflict | Test a narrow compatibility rule: how do baseline, A, B, and A+B differ on comparable tasks? |
| WL-02 | Sequencing / evidence provenance | Several approvals may descend from one unsupported assertion | Add claim-to-artifact links or collect a different observation: is there any independent evidence? |
| WL-03 | Directed evolution / variation and selection | Repeated tasks offer a bounded opportunity to improve a procedure | Compare a few variants against a baseline and held-out tasks: does improvement transfer? |
| WL-04 | Chemistry / inhibiting assumptions | Work repeatedly follows a plausible but unsupported premise | Remove or isolate the suspect assumption: does that resolve the blockage more effectively than appending instructions? |
| WL-05 | Reliability / fault containment | One mistaken observation or test could fool every check | Trace an incorrect acceptance back to its causes: which shared failure needs repair or a different check? |
| WL-06 | Social influence / harmful revision | Reviewers converge after sharing conclusions without new evidence | Compare initial judgments with evidence-linked revisions: are correct answers being displaced? |
| WL-07 | Control theory / observation and feedback | Repeated corrections alternate or rely on stale/ambiguous measurements | Compare bounded edits with fresh observations: does the loop converge without recurring regressions? |
| WL-08 | Metrology / measurement uncertainty | A stable score conflicts with known defects or user observations | Calibrate with relevant reference cases: is the measurement capable of detecting the target defect? |
| WL-09 | Active learning / informative evidence | Many similar tests, captures, or human votes add little information | Select a discriminating observation: which affordable result would change the next decision? |
| WL-10 | Statistical physics / escaping local optima | Small refinements stop producing meaningful improvements | Compare different approaches in isolated versions: does exploration outperform further polishing within budget? |
| WL-11 | Operations research / bottlenecks | More work is started but verified completions do not increase | Measure waiting, implementation, evidence, and review times: which stage limits completion? |
| WL-12 | Optics / focus and calibration | Context selection, reference comparison, or judge calibration seems to be the recurring cost | Select only the relevant archived mechanism; compare its value with a smaller docs or tooling change. |
| WL-13 | Occasional experiment capability | Several workflows need experimental decisions beyond Mason's existing evaluation reference | First check overlap: would extracting a shared experiment procedure avoid repeated work? |

## How Mason could use this later

When Mason is invoked for a relevant review, this catalog can be supplied as an authorized collection index. Read its small table first and open only the matching source section. Most reviews need no entry. A theme match alone is not evidence that an intervention is needed.

Use this decision path:

1. Identify an actual recurring cost or a supported upcoming reuse; distinguish observations from interpretations.
2. Check existing skills, owning code, project documentation, and tools. A known defect with a clear fix usually needs ordinary verification.
3. If a catalog entry helps explain an unresolved decision, cite its ID and propose the smallest useful comparison, including a baseline, quality checks, full cost, and stopping condition.
4. Respect the candidate's parked status and the current run's authorization. Collection or inspection does not start a pilot. No scheduling, model switching, provider calls, or background monitoring is supplied here.
5. If a pilot later runs, preserve its actual evidence, negative results, and uncertainty. Reuse, a script/code fix, or an existing-skill update may remain the best disposition even after a successful result.

Example review request from the repository root:

> Use Mason to review the completed work. Consult research/workflow-lab/README.md only for hypotheses relevant to observed recurring costs. Recommend no change when evidence is weak. Propose a bounded comparison if it would resolve an important uncertainty; leave parked experiments unexecuted.

This example requests review and planning. A later run can explicitly authorize a chosen pilot and its resource limits. A copied installation of Mason does not automatically include this repository catalog; supply the checkout path or an approved copy when using it in another harness.

## Evidence and adoption are separate

| Stage | Meaning |
| --- | --- |
| Parked | Mechanism and question recorded; no workflow-benefit evidence yet |
| Pilot planned | Comparison and acceptance defined; execution may still be inactive |
| Pilot observed | A bounded run produced artifacts and measurements, including failures |
| Supported for a scope | Evidence justifies a limited conclusion for named tasks and conditions |
| Adopted | A separately authorized skill, code, documentation, or routing change implements the result |
| Rejected / inconclusive / retired | Preserve why it failed, remained uncertain, or ceased to be useful |

A promising analogy is not a validated skill, and a successful small pilot does not establish universal savings. Adoption does not require a new skill. Keep evidence status and activation status explicit.

## Record future results here

Use the table below for short decisions; link a longer record under `pilots/<ID>-<short-name>.md` only when an actual proposal needs it. There are currently **no pilot results**. Avoid empty result files or an elaborate tracking system.

| Date | Candidate ID | Evidence / decision | Activation | Result artifact | Revisit condition |
| --- | --- | --- | --- | --- | --- |

A substantive pilot record should identify the question, baseline, changed variables, versions and comparable starting states, acceptance checks, limits, actual observations, complete cost when available, uncertainty, disposition, and scope. Keep private project paths, transcripts, credentials, proprietary artifacts, and identifying task details in private project records; public results can link to a sanitized summary when publication is authorized.

## Contribution boundary

Add ideas only when they identify a mechanism and a question that could change a decision. Cite the scientific source and distinguish its findings from the proposed transfer. Preserve useful rejected results. Prefer the smallest maintained procedure and avoid turning every scientific metaphor into a separate skill.
