---
name: downshift
description: Prepare and run cost-aware handoffs from a stronger planner to a cheaper implementation model, with bounded tasks, evidence-based review and replanning. Use for requested expensive-planner/cheap-worker workflows within one harness or across harnesses through Markdown files; not for ordinary task planning without a model handoff.
---

# Downshift

Spend planning effort where it lets a cheaper worker finish more verified work.
A detailed plan is a reusable asset, not evidence of savings or successful work.
Keep the original goal and acceptance criteria throughout execution and review.

## Roles and fit

When resuming an existing packet, honor its assigned role and active card. A
worker reads the execution contract; it does not repeat the full planning phase
or turn itself into a stronger planner. Apply the preparation steps below only
to a new handoff or an authorized plan revision.

Use the current capable model as planner unless another role is selected. Record
exact planner, worker and reviewer identities/effort when known; leave unknowns
explicit. Respect the user's selected models and providers. Do not infer that a
larger parameter count or a higher price guarantees suitability. If choosing
models requires current capability or pricing evidence, consult an available
catalog or model-selection skill; do not invent access, costs or benchmarks.

Check whether the work has separable, verifiable units and enough repeated
execution to plausibly repay planning, context loading and review. For a short
one-off fix, unstable goal or inseparable research problem, recommend direct work
or a small pilot rather than generating an elaborate queue. If the user still
wants the workflow, provide a bounded pilot and label savings unproven.

Distinguish implementation readiness from uncertainty. Investigate the few facts
needed to make the first tasks actionable; put genuine unknowns into bounded
research cards with a deliverable and decision gate. Do not encode guessed API
names, invented commands or unsupported diagnoses as exact worker instructions.

## Choose the handoff mode

Inspect the actual workspace, harness facilities, allowed providers and context
boundaries. Load only the relevant mode reference:

- **Separate harnesses / files:** [references/files.md](references/files.md).
  Persist a self-contained handoff and return path; no shared chat is assumed.
- **One harness / direct:** [references/direct.md](references/direct.md).
  Use available, authorized routing; preserve a small durable checkpoint anyway.
  If routing is unavailable, fall back to the file mode and report that fact.

A skill supplies a procedure. It cannot switch models, enforce hard limits,
continue a stopped harness, create an independent reviewer or reduce bills by
itself. Do not install hidden runners, alter service/model settings, or send
artifacts to an additional provider merely because this skill was loaded.

## Prepare once, refine when evidence changes

1. **Pin the contract.** Reuse the existing backlog and project instructions.
   Record the objective, unchanged acceptance, relevant source version or hashes,
   known behavior/evidence, scope exclusions, actual tool/launch/check commands,
   provider/input-sharing limits, and shared-service/resource constraints. Keep
   parent IDs: child-card completion does not silently close a larger goal.
2. **Make a small ready wave.** Give each task a stable ID, dependency, observed
   defect, narrow owner/files, one coherent outcome, suggested implementation,
   acceptance check, evidence location, allowed changes and stopping condition.
   Add exact commands only after discovering them. Detail should remove
   ambiguity at fragile steps while letting the worker adapt to verified facts.
   Keep future tasks as an outline until dependencies support precise steps.
3. **Separate plan from proof.** Give the worker only the contract summary,
   active card, needed code/evidence and last unresolved issue. Keep background
   research, full transcripts and unrelated skills outside its working packet.
   Include prompts for execution, self-review and return-to-planner review.
4. **Set a finite run.** Reuse user limits; otherwise suggest one wave of up to
   three coherent cards and two materially different attempts per blocker before
   checkpointing. Record what these limits count. A time-consuming check is not
   automatically stalled; a new command string is not automatically progress.
   Specify the review gate and who may authorize another wave. Never create an
   unbounded self-generated queue or infer new budget from elapsed time.

Use existing project documents whenever they already meet this contract. For a
new file handoff, the optional helper creates editable templates without
replacing files:

```bash
python3 scripts/init_handoff.py /path/to/project/.downshift --mode files
```

Run the helper relative to this skill's folder or use its absolute path. It does
not inspect the project, choose models, complete task cards or execute a model.
Do not hand unfinished templates to a worker as ready instructions.

## Execute, review, return

The worker performs one card, checks relevant behavior, records failures and
actual inspected artifacts, then self-reviews against the original criteria.
Use per-criterion **pass / fail / unknown**; missing checks remain unknown.
Stills do not establish motion, a build does not establish behavior, and a model's
caption does not establish a matched before/after comparison. Capture source and
fixture identity where attribution matters. Preserve earlier evidence.

Self-review can catch mistakes and propose the next wave. Label it **same-model**
even in a fresh chat; agreement between repeated calls is not independent proof.
Keep self-reviewed results distinct from independent review and user acceptance.
Do not automatically regenerate requirements from the worker's own judgments.

A reviewer receives the contract, relevant diff/artifact, observed check outputs,
remaining failures and cost summary. For a separate review, ask for an initial
inspection before revealing the worker's favorable assessment where useful.
Verify material claims and look for a counterexample. If source drift, a wrong
assumption, repeated failure or a cross-system regression invalidates the plan,
return a compact exception packet to the planner. Continue independent ready
work within the existing budget; avoid repeatedly calling the expensive planner
for small choices the worker can resolve from local evidence.

The planner repairs affected cards and dependencies rather than rewriting the
whole plan. Keep retired/failed assumptions in a short decision log, preserve
original acceptance, and propose at most the next bounded wave. Execute that
wave only within explicit existing continuation authorization or after a new
instruction. At completion audit the original contract, not the number of cards.

## Check the economics

For a pilot, doubtful savings or model comparison, read
[references/evaluation.md](references/evaluation.md). Count planner creation and
revisions, worker retries/context, reviews, tools and integration. Compare total
cost and elapsed time per accepted outcome at comparable quality. Unknown prices
stay unknown; local inference has time/resource costs. Report "workflow prepared"
or "pilot completed" until a fair comparison supports savings.

Ladder may supply an already-authorized ordered model sequence; Downshift adds
the reusable planner-to-worker contract. Neither skill is a required dependency
of the other, and loading one does not start the other automatically.
