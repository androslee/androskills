# File handoff between harnesses

Use when a planner and worker do not share reliable conversation state, such as
a cloud planning harness and a local implementation harness. No particular
vendor, model family, OS or shared drive is required.

## Prepare the packet

Prefer the project's existing task/checkpoint documents. If none exist, the
helper creates this small layout under a chosen project directory:

- `START_HERE.md`: roles, mode, entry prompt and where the worker writes back.
- `CONTRACT.md`: fixed objective, acceptance, environment, constraints, model
  choices, finite execution/review limits and authorized continuation.
- `QUEUE.md`: stable task IDs, dependencies, state and evidence links.
- `tasks/T001.md`: one editable task-card example; add concrete cards only as needed.
- `STATUS.md`: active artifact identity, decisions, blockers and next ready work.
- `REVIEW.md`: reusable review/return fields for a batch; preserve completed
  reviews under distinct names instead of overwriting them.
- `COSTS.csv`: optional measurement ledger, with unknown numeric values empty.

Complete and prune templates from actual project evidence. Paths should be
relative to the declared project/packet root where portable. State separate
planner/worker root mappings when hosts differ; avoid hard-coded personal paths
in reusable public skill sources. Keep a single authoritative queue when an
existing backlog is present; these files may be pointers to it rather than copies.

Pin the baseline using a commit plus dirty diff, or source/artifact hashes and a
preserved copy when no VCS exists. A commit alone does not cover dirty edits.
Record dependency/runtime versions and fixture identity needed for the task.
Before work resumes on another host, check that the expected baseline still
matches. Source drift calls for a narrow reconciliation, not a silent overwrite.

If hosts share a working tree, give it one active writer. If they use copies or
branches, specify how patches, assets, logs and captures come back and who
integrates them. Never assume that a Markdown path exists on the other host.
Preserve user edits and write a compact return diff, not a whole unrelated tree.
Public instructions may be shared; project packets stay private unless their
contents and destination are authorized. A local-only result must not be sent to
a cloud reviewer automatically. Use an allowed redacted summary or local/human
review and record any resulting verification limits.

## Worker startup prompt

Use the packet's mode-specific prompt, adapted to the actual project:

> Read START_HERE.md and CONTRACT.md. Inspect QUEUE.md and the first ready task.
> Confirm the baseline and prerequisites, execute only the authorized wave, and
> preserve the original acceptance. Read only relevant code and references. Save
> actual check results and evidence, self-review each criterion, then update
> QUEUE.md and STATUS.md. Follow the stalled-work and review gates. At the gate,
> write a compact return packet and stop unless the contract already authorizes
> another wave. Do not execute incomplete cards or expand the scope yourself.

The worker does not need to load the entire Downshift planning reference or all
future cards at every turn. The completed contract and card contain the needed
execution rules. Add a short project instruction pointing to START_HERE.md only
when appropriate and authorized; do not replace unrelated AGENTS instructions.

## Return and resume

Return the relevant changed files/patch, baseline and resulting source identity,
per-card status, exact commands and exit codes, artifacts actually viewed,
self-review limits, failed approaches and the smallest next question. Keep logs
bounded in the summary but retain full logs by link. Do not paste a long internal
reasoning transcript as evidence or as instructions for the next model.

The planner/reviewer rechecks source and reported outcomes before merging or
closing parent tasks. When a new check reveals a bad assumption, amend only the
affected cards and record why. Reuse the surviving plan. Update START_HERE and
STATUS so a fresh worker chat can continue without importing its prior entire
history. Synchronization and new turns require the actual harness or user; a
file alone does not run a continuation.
