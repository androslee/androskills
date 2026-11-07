# Does downshifting save money?

A successful scaffold or plausible plan is not a measurement. Compare accepted
outcomes against an appropriate direct-work baseline, keeping quality criteria,
starting artifacts, task difficulty and allowable tools comparable.

## Minimal pilot

1. Choose a representative task plus a nearby case where planning overhead may
   not be worthwhile. Preserve separate starting copies for direct execution and
   downshift execution. Reuse existing evaluation tasks when available.
2. Pin the contract, baseline, exact models/quantization/backend/effort and allowed
   tools. Separate the cost of authoring this reusable skill from the cost of
   creating each project's plan; both matter, but have different reuse counts.
3. Run each approach within its authorized budget. On repeated comparisons,
   vary order and use equivalent tasks or isolated starting state so one arm
   does not inherit the other's solution. Include failures and abandoned work.
4. Review against original criteria; use objective checks where possible and
   label same-model judgment. For subjective artifacts, use matched comparisons
   and record human/independent review when performed. Do not promote confidence,
   verbosity, token speed or a completed checklist into an outcome metric.
5. Compare total cost, elapsed time, accepted tasks, regressions and review effort.
   A single tiny task can establish feasibility, not broad savings or reliability.

## Accounting

Use `COSTS.csv` if tooling does not already capture this. Record planner creation
and revisions, worker input/output/reasoning, retries, cached input, reviews,
provider/tool charges, image count/vision input where available, elapsed time and
local resource time when measurable. For visual tasks, separately record how
many artifacts the worker captured and inspected locally versus how many
the expensive reviewer received, and vision input tokens if the provider
exposes them; see [visual evidence](visual-evidence.md). The optional
`COSTS.csv` template has columns for these counts and leaves unknown values
empty.
Record unmeasured values as empty/unknown, not zero. Include model/backend/effort
and a pointer to the raw usage or invoice facts; do not store credentials.

Pricing and token accounting vary by provider. Cached input may be a subset of
reported input, and reasoning may already be counted in billed output: do not
add overlapping buckets. Use actual billed cost where available, or clearly
label an estimate with its dated rates and units. Local inference need not have
a per-token charge, but elapsed time, energy/hardware and opportunity cost are
separate quantities. Do not invent a cash equivalent for them.

A useful conceptual comparison is:

`downshift total = project planning + worker execution/retries + review + integration`

Compare that with direct execution **at equivalent acceptance**, including the
cost of direct retries/review. For repeated comparable work, report how project
planning and reusable skill authoring are amortized, using measured reuse rather
than an assumed infinite queue. If prices are unknown, compare token/time and
quality components separately; leave dollar savings unknown. If no task passed,
cost per accepted task is undefined rather than a fabricated low number.

## Adapt or retire

Downshift is failing its purpose if the planner keeps repairing individual edits,
the worker repeatedly needs the entire transcript, acceptance is being weakened,
or combined retries/review cost exceeds direct work at comparable quality.
Narrow cards, repair missing tooling or select a better-suited authorized worker
before adding more planning text. Escalate a difficult task within the agreed
route, or return to direct execution. Keep a small useful lesson; do not defend
the workflow by excluding failed attempts from the totals.
