---
name: mason
description: Review completed or substantially repeated work for evidence-backed opportunities to create, improve, or reuse a skill. Use for a requested workflow retrospective or recurring corrections and rediscovery; recommend no change when the evidence or expected benefit is weak. Does not replace task execution or ordinary skill routing.
---

# Mason

Find a reusable intervention that would improve the next comparable task. A skill
is one possible intervention; no change is a valid and often preferable outcome.
Optimize verified outcomes and total cost, not the number of skills produced.

## When and how much

Work at a natural checkpoint, after useful task progress, or when explicitly
asked. Do one short review; do not interrupt every tool call or keep revisiting
the same declined idea. Continue the actual task unless the user paused it.

Use the current model first. Do not change models, effort, or providers merely
because this is a meta-task. A stronger review may be worthwhile when evidence
supports reuse but generalization is uncertain, a proposed instruction could
cause consequential actions, or independent evaluations disagree. State the
specific uncertainty and provide a small evidence packet if the host cannot
perform an authorized escalation. Weak evidence is a reason to defer a proposal,
not a reason to spend more proving it desirable. Never promise savings from a
model's name, price, effort label, or agreement alone.

A skill is not a background observer or scheduler. Automatic end-of-task review
requires the host to invoke it or a relevant agent decision to load it. Do not
claim continuous monitoring, hard budget enforcement, or automatic model switching.

## Review

1. **Find the recurring cost.** Use only authorized conversation, artifacts and
   task records. Identify the correction, failed approach, repeated discovery or
   non-obvious decision, with concrete evidence. Repeated retries on one incident
   are not independent examples of future reuse. Normally seek evidence from at
   least two distinct tasks or sessions. A single costly incident can justify a
   bounded pilot only when a specific upcoming reuse and a transferable lesson
   are already supported; label the uncertainty. Do not manufacture recurrence.
2. **Choose the right intervention.** A stable command or transformation usually
   belongs in a script; project facts in project documentation; a persistent
   preference in supported memory; enforceable invariants in configuration or
   tooling; a defect in the owning code. A skill fits reusable judgment, workflow,
   or reference selection that changes how an agent approaches a class of tasks.
   Do not preserve a workaround after fixing its root cause.
3. **Check existing coverage cheaply.** Start with the host skill catalog and
   any authorized collection index, including selected-but-inactive packages.
   Read only plausible matches. If available, Sherlock can help discovery and
   skill-creator can help authoring; neither is a required dependency. Distinguish
   absent capability from a skill that was not invoked, poor routing, and bad
   instructions. Prefer reuse, routing repair, or a small existing-skill update
   over a duplicate. Discovery does not authorize installation or activation.
4. **Check transfer and cost.** Is the lesson specific, non-obvious, and useful
   beyond this incident? Can its trigger exclude nearby unsuitable tasks? What
   would it let the agent omit or decide better? Compare expected avoided work
   with drafting, review, future instruction-loading and maintenance costs. Use
   measurements when available; label estimates and unknowns. Concise tasks can
   become more expensive when a large skill is loaded.
5. **Choose a disposition.** Recommend **none**, **reuse/route**, **script/docs/code**,
   **update existing skill**, or **pilot a new skill**. A new-skill proposal needs
   supported reuse, an uncovered procedural gap, a clear trigger/boundary, a
   plausible net benefit and a way to test it. If a necessary condition is weak,
   preserve the observation only if a useful existing ledger warrants it; do not
   recommend a skill just to fill an output template.

## A worthwhile proposal

Return at most one strong proposal in a routine review. A requested portfolio
review can cover more. Keep it short:

- **Decision and evidence:** what changes, the concrete examples, and uncertainty.
- **Existing coverage / alternative:** why reuse or a simpler intervention is
  insufficient; an inactive matching skill may already solve the problem.
- **Trigger and boundary:** when to load it and when to stay out.
- **Reusable change:** the decisions or procedure it adds; not a transcript dump.
- **Pilot:** a comparable task, a nearby task where it should abstain, success
  checks, costs to record and a condition for rejecting or retiring it.

When explicitly asked to review and nothing qualifies, explain briefly why.
During optional internal triage with no useful finding, add no user-facing
suggestion. Do not create files or ask approval solely to record “none.”

Recommend a candidate before creating it unless the user already authorized
skill authoring or improvement. Authorization to suggest skills does not by
itself authorize changing active instructions, broad searches, uploading task
records, or connecting providers. Keep private examples out of public skill
sources; use generic examples only where they clarify the reusable decision.

## Pilot and learning

For cost/quality claims or disputed candidates, read
[the evaluation protocol](references/evaluation.md). It covers baselines,
abstention, model escalation, evidence and retirement. A well-written draft or
passing file validation is not evidence of token savings or behavioral quality.

Keep candidate creation, collection, activation, and proven usefulness distinct.
Do not automatically promote a pilot, rewrite Mason after every use, create
recursive skill generators, or expand a skill to encode every exception.
