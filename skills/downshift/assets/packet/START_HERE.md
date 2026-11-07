# Downshift handoff

Mode: {{MODE}}
Packet format: 1
Project root and model roles: CONTRACT.md
Authoritative backlog: QUEUE.md, or its declared existing-project link.

## Before execution

The planner must complete CONTRACT.md and make at least one concrete card Ready.
T001 begins Draft. This scaffold has not inspected the project or run any model.
Read applicable project instructions before changing source. A missing fact is
unknown, not permission to guess or execute an incomplete card.

## Worker prompt

Read CONTRACT.md, STATUS.md and QUEUE.md, then only the first Ready task and its
relevant source/evidence. Confirm the baseline and dependencies. Execute the
finite authorized wave, verify against original acceptance and save actual
results. Update the queue/checkpoint and self-review with REVIEW.md. After two
materially different failed attempts on one blocker (unless the contract sets a
different limit), checkpoint it and continue independent Ready work within scope.
Return at the review gate; do not automatically execute your proposed next wave.

## Reviewer / next-planning prompt

Read the original contract, produced source/artifact identity, changed files and
check outputs. Inspect before relying on the worker's verdict. Assess each
criterion as pass/fail/unknown and record review independence. Keep unmet parent
conditions open. Repair only plan-invalidating assumptions, propose one bounded
next wave, and preserve the prior decision log. Route or return it only through
the contract's authorized mechanism and input-sharing boundaries.

## Where work returns

Save card results and artifacts at the location specified in CONTRACT.md.
Use a distinct review file per completed batch; REVIEW.md is the reusable form.
STATUS.md must name the produced artifact, blockers and next Ready task so a
fresh chat can resume. No runner or model router is installed by this packet.
