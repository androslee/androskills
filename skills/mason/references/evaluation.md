# Evaluating a Mason proposal

Use this when judging a pilot, making efficiency claims, choosing a stronger
reviewer, or deciding whether to keep a proposed intervention. Ordinary quick
triage does not need this file or a new tracking system.

## Small evidence packet

Include the user's outcome and constraints, a few permitted artifact references,
the costly decisions/corrections, what existing coverage was checked, and the
specific remaining uncertainty. Keep observed facts separate from interpretations.
Exclude secrets and unrelated transcripts. A remote review is subject to the
same privacy and spending authorization as any other remote model call.

Use the project's existing decision/proposal ledger when one exists. A useful
entry has: problem, evidence, disposition, proposed change, activation status,
pilot result, and next review trigger. Do not create an elaborate database or
persist a whole chat for a small proposal. Revisit a declined candidate only
when materially new evidence or a changed user preference warrants it.

## Baseline and counterfactual

Ask: what would the agent have done differently if the proposed skill existed
and was actually selected? Rewording the final answer or restating “be careful”
is not a mechanism. Identify a decision, source-selection step or verification
boundary that changes, and how that change prevents the observed cost.

Compare against the best simpler alternative, not only an intentionally weak
baseline. Existing project docs, a short script, better routing, or a bug fix
may provide the same gain with less ongoing context.

## A bounded pilot

1. Choose a few comparable tasks not used to write the proposal, plus nearby
   negative cases. Include at least one case already covered by another skill
   and one where more instructions would be needless overhead.
2. Run a baseline without the candidate and a candidate condition on equivalent
   isolated starting states. Preserve the same outcome, model/effort, tools,
   constraints and acceptance checks. Use fresh contexts where practical; do not
   teach the second run the answer from the first. Vary order or repeat if the
   decision is sensitive to model randomness or caching.
3. Evaluate actual artifacts and task results. A shorter response that omits
   required work is a regression. Check unnecessary tool calls, clarification
   burden and whether the candidate is selected only when useful.
4. Record input/output/cached-token counts separately when supplied by the host,
   relevant tool/provider charges, elapsed time, retries, and quality. Cost can
   differ despite equal token counts. If usage is unavailable, record observed
   steps and label token/currency savings unknown; do not invent counts.
5. Keep, revise or reject against the predeclared acceptance checks. Small pilots
   support a limited conclusion; retain failures and avoid selecting only wins.

A possible qualitative break-even test is:

    expected future uses × avoided per-use cost
      > drafting + review + future instruction-loading + maintenance costs

This is a planning estimate, not a measured result. Count one-time authoring
separately from per-use work. Do not claim net savings until costs and quality
have been observed across enough representative uses for the stated claim.

## Model and effort escalation

- Start ordinary triage with the current model. Better evidence and a smaller
  question may help more than a larger reviewer.
- Escalate for a named ambiguity: distinguishing a general lesson from a
  misleading example, competing interventions, conflicting pilot outcomes, or
  consequential instructions that deserve a second review.
- Let an independent reviewer assess raw evidence and alternatives before seeing
  the preferred proposal when feasible. Agreement is not a correctness test.
- Keep any higher-model review bounded. Authoring and implementation can use a
  cheaper model once the acceptance criteria are concrete, then verify results.
- Use only host-supported, authorized switching/delegation. Otherwise provide a
  handoff. Do not install a runtime or launch a model server to conduct a review.

## Calibration scenarios

These are authored walkthrough cases, not a passed behavioral benchmark. Use
held-out, realistic tasks to measure actual model behavior.

| Situation | Appropriate disposition |
| --- | --- |
| One ordinary typo correction, no expected recurrence | None; fix the typo. |
| Repeated port error caused by a broken launch script | Fix the script; consider a regression check, not a new skill. |
| A needed skill exists but was never selected | Reuse or repair routing; no duplicate package. |
| A suitable package is collected but inactive | Suggest selective activation/review, not creation. |
| A project repeatedly forgets its deployment address | Project documentation/configuration, not a global skill. |
| Several tasks repeatedly choose the wrong source of visual evidence, beyond existing guidance | A narrow existing-skill update or new pilot, depending on overlap. |
| Two failed attempts on the same novel rendering bug | Diagnose the bug; insufficient independent recurrence for a general skill. |
| A user declines an interview-heavy process | Respect the preference; do not repeatedly propose another interview skill. |
| A proposal matches its authoring examples but fails new tasks | Reject or narrow it; no proven transfer. |
| The shorter run omits required browser verification | Quality failure; not an efficiency win. |

## Retire or simplify

Retire a candidate when it duplicates another skill, repeatedly misroutes,
costs more than it avoids, becomes stale, or fits no remaining tasks. Prefer
removing unnecessary instructions over adding more exception branches. Preserve
only a concise decision record where useful; do not delete user data or active
packages without the authorization appropriate to that action.
