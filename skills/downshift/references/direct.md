# Direct handoff in one harness

Use when the host actually exposes authorized model routing or delegation. One
UI does not establish that its agents share files, tools, model identities or
permissions. Discover the real capabilities before choosing the mechanism.

## Confirm the route

Record planner, worker and reviewer provider/model IDs and effort, tool and image
support needed for the task, workspace isolation/shared-writer behavior, input
sharing limits, and available budget enforcement. Preserve the user's chosen
roles. If an identity or feature cannot be selected, report it; do not role-play
a cheaper model or independent reviewer on the current model and call it routed.

A skill cannot upgrade permissions or grant provider access. Model switching and
agent creation must use host-supported operations already authorized for this
run. Respect single-resident-model machines, serialized GPU work and services
that host the active conversation. Do not launch a second backend or restart the
current agent merely to hand off work. If routing would terminate the active
session or is unavailable, save the packet using the file mode and let the
supported host/user mechanism resume it.

## Direct assignment

Build the same contract/card as file mode. Supply only this compact assignment:

> Role and exact selected model/effort; original goal and relevant acceptance;
> artifact/base identity; active card ID and dependencies; allowed workspace and
> write scope; relevant paths/evidence; useful verified commands; one finite
> execution limit and stalled-work rule; output/return location; review gate and
> continuation authority. Verify locally, report pass/fail/unknown, and distinguish
> actual checks from suggestions. Do not broaden your assignment.

Use typed task arguments or the host's persistent handoff facility when present;
keep at least a small durable queue and checkpoint for crash recovery and later
review. Do not resend full planner research with every call. If the worker
cannot see an attachment or file, make the missing artifact available through an
authorized channel or block that condition; naming a path is not sharing it.

Default to sequential ownership. Independent tasks can run in parallel only
when that is separately authorized, with compatible budgets and isolated writes.
Do not spawn workers merely to make the workflow look more sophisticated. A
single routed worker per wave is a valid direct implementation.

## Review and next wave

After the wave, gather artifacts and actual usage. The worker may perform a
same-model self-review first. For an authorized stronger review, pin the produced
version and original acceptance, then let the reviewer inspect the source/check
results before relying on the worker's interpretation. Distinguish a different
role from a genuinely separate model call; neither guarantees independent errors.

Return an exception packet only for plan-invalidating findings, two materially
different stalled attempts, consequential regressions or an agreed review gate.
Routine implementation choices stay with the worker. The planner makes a bounded
revision and routes only a wave covered by the user's existing scope and budget.
Record requested versus actual roles, accepted outcomes and costs, including the
review calls. Do not recursively spawn planners or generate unlimited new waves.

A direct-mode packet can be initialized with `--mode direct`; its queue and task
format are deliberately the same as file mode. Switching modes should preserve
IDs and evidence rather than restarting the plan. No router/API client is bundled
with this skill, so direct routing remains unexecuted until the host performs it.
