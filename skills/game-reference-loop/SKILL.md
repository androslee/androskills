---
name: game-reference-loop
description: Improve an existing game through sustained reference research, screenshot and gameplay comparison, an evidence-backed TODO, implementation and verification loops. Use for continuing a game-comparison backlog or pursuing a reference game's visual and mechanical quality.
---

# Game reference loop

Carry an authorized game-improvement task through repeated research, implementation
and verification cycles. Preserve the user's project, reference game, chosen scope
and operational constraints. Use original assets and implementations; reference
material is evidence, not an asset pack or permission to extract game files.

## Establish or resume the experiment

Read project instructions, the existing TODO, reference catalog, last review and
resume checkpoint before editing. Reuse these documents instead of creating a
second competing backlog. Discover the actual launch, capture, build and test
commands. Preserve services that host the agent and the user's unrelated work.

Identify the reference title, edition/build/date, platform, relevant settings and
local test hardware. Unknown details remain unknown. Do not assume mechanics from
another installment or treat announced updates as released content. If this is an
established project, refresh evidence relevant to the next task rather than
restarting a comprehensive survey each run.

For a new comparison, first perform a broad evidence pass covering applicable
categories: environment/levels/biomes, lighting/water/materials, characters/enemies
and animations, tools/items/equipment, crafting/building/tech trees, survival and
combat, progression/goals/endings, encounters/rewards and UI/input/playability.
Then investigate the highest-impact gaps deeply enough to write implementable
tasks. Do not spend the whole run searching for an exhaustive catalog.

Read [references/evidence.md](references/evidence.md) when gathering or extending
reference evidence. Inspect real images and moving footage where tools permit;
search snippets, transcripts and memory alone do not establish visual quality or
motion. Record what was actually viewed and which claims remain unverified.

## Turn evidence into a bounded TODO

Write findings before implementing. Prefer the project's current TODO filename;
otherwise use `VISUAL_TODO.md`. Keep a linked reference catalog for substantial
source detail. Each actionable task needs:

- Stable ID, category, dependency/tier and a concrete observed gap.
- Reference evidence ID/source and timestamp or image region, with confidence.
- Desired local behavior or appearance, plus a reproducible acceptance check.
- Current state: open, in progress, implemented pending verification, verified,
  blocked by evidence/tools, or deferred by user. Use unchecked boxes with labels
  if the existing format has only checkboxes.
- Result/capture links and remaining differences after verification.

Track visual fidelity, mechanical behavior, content coverage and evidence
confidence separately. Numerical ratings are optional ordinal judgments, not
probabilities or proof. An implementation checklist closing does not establish
commercial-game parity. Preserve parent IDs and original acceptance criteria; do
not improve counts by inventing tiny completed tasks or narrowing old criteria.
Keep unknown reference claims in a research queue with the evidence needed, not
as fictional recipes, bosses, spaceship endings or random-event rules to build.
A feature is absent only with adequate scoped evidence; not seeing it is unknown.

## Review deliberately; implement economically

Recommend a more capable model or higher reasoning effort for the initial gap
analysis, difficult diagnosis and milestone/final judging. Recommend a cheaper
model at low/moderate effort for well-specified, reversible implementation tasks.
These are routing heuristics, not guarantees about named models or pricing.

Keep a concrete handoff: pinned captures/version, original acceptance condition,
observed defect, relevant files, reproducible commands and constraints. Obtain
current model availability/cost evidence only when making specific recommendations.
Do not switch models, raise spend, upload artifacts to a new provider or spawn
agents just because this skill recommends role separation. Use only routing and
delegation actually authorized and supported by the harness. If unavailable,
continue useful work on the current model and label review as same-model; never
pretend another model independently judged it. No model switch is required to
use the workflow.

Request stronger diagnosis when two materially different controlled fixes miss
the same target, regressions cross rendering/gameplay systems, or evidence does
not support the proposed explanation. Preserve the failing fixture and stop
repeating the same experiment. Continue independent backlog work when possible.

## Work through the queue without repeated prompts

Within the authorized run, repeat the following cycle across multiple tasks;
finishing one item is not a reason to ask whether to continue:

1. Select a small, coherent task with satisfied dependencies. By default rotate
   among applicable categories, taking their lowest incomplete tier first; do
   not polish one category indefinitely while the others stagnate. Respect a
   user-selected task or batching preference. Split large tasks into verifiable
   slices without claiming their parent is complete.
2. Capture the current baseline and compare it to relevant reference evidence.
   State the specific defect and intended result before editing. Reuse an exact
   prior baseline when source/settings/camera still match.
3. Implement the change. Asset, silhouette and composition problems need art or
   geometry work; extra bloom, fog or polygons alone do not demonstrate progress.
   Preserve input, navigation, collision, progression and multiplayer as relevant.
4. Run appropriate build/runtime checks, capture the actual result, inspect it
   and compare against the acceptance condition and reference. Check transitions
   and motion for animated changes; stills cannot verify animation. Use real
   keyboard/controller play for claims about playability, not only staged cameras.
5. Correct regressions or reject the attempt if the evidence does not improve.
   Keep failed attempts labeled. When it passes, update the task, source-linked
   comparison notes and resume checkpoint, then select the next ready task.

Use fixed seed, camera, time, resolution and quality for local before/after work
where possible. Label staged inspection separately from actual gameplay. Do not
edit live-reloaded source during a capture/profile. Serialize tests sharing a GPU
or input focus. Show the user captured screenshots in the conversation using the
available image viewer, and link clips/galleries; do not merely claim they exist.
Summarize each coherent batch with visible gains, unchanged gaps and meaningful
check results. If results plateau, change the hypothesis or asset approach instead
of accumulating near-identical captures and optimistic completion claims.

Measure CPU/GPU/frame timing when changes materially affect rendering or scope.
Identify hardware versus software rendering, warm-up, resolution and sample
window. Keep gameplay and visual checks separate from timing; build success alone
is not evidence of quality. Avoid attributing sequential timing changes to one
feature without a controlled comparison.

## Checkpoint, completion and continuation

Maintain a short project resume file (convention: `ITERATION_STATE.md`) after
coherent batches and before context/budget exhaustion. Store the reference/build,
active task, category rotation cursor, changed files, exact commands/results,
artifact paths, review model/effort if known, remaining defects/blockers and next
ready tasks. Do not store credentials or reset completed work after compaction.

Continue until all agreed acceptance conditions are actually verified, the user
pauses/redirects, a hard host/resource limit is reached, or no meaningful in-scope
work can proceed. An unavailable stronger reviewer is not a reason to stop all
implementation. Mark only the affected items blocked; never mark them complete.
Before claiming completion, audit the original scope against the latest evidence
and report unknowns or residual differences explicitly.

A skill supplies instructions; it cannot create a new turn, replenish tokens or
run after the harness stops. Use an authorized host continuation/goal mechanism
only when requested and available. Otherwise checkpoint cleanly and explain that
resuming loads the same queue. Do not install a hidden background runner, modify
billing, or claim automatic continuation that was not configured.
