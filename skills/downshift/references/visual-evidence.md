# Visual evidence handoff

Use this reference when a task's acceptance depends on screenshots, rendered
images, animation or video. Keep the original task criteria; this workflow
reduces expensive visual review without treating the worker's self-review as
independent proof.

## Before implementation

- Planner defines the visual claims, required views or time ranges, controlled
  comparison conditions, and what a reviewer must be able to decide.
- Capture only what those checks need. For comparisons, record source revision
  or hashes, scene/stage, seed, camera, viewport, renderer, settings and input
  or staging. Preserve valid before captures before scripts can overwrite them.
- Keep every required raw capture locally. Do not upload or forward a complete
  gallery to another provider unless that sharing is authorized and needed.

## Worker capture and local triage

The cheaper worker runs the checks and inspects the full relevant capture set
with its available local vision tools. It creates a compact evidence index that
maps each original criterion to:

- pass / fail / unknown;
- exact image, crop, clip and timestamp paths;
- a short observation of what is visible and what is not;
- fixture/source identity and any limitation that affects comparison.

Metrics, image hashes, generated captions and automated scores can help find
evidence, but they do not replace inspecting the relevant output. If the worker
cannot view an artifact, it must say so and leave that criterion unknown.
Stills cannot establish motion; use a short clip or consecutive timestamped
frames for animation claims.

## Bounded expensive review

The reviewer first receives the acceptance criteria, source/test summary and
evidence index, not a dump of every image or the full execution transcript. It
then inspects a deliberately small raw subset tied to the most important or
uncertain claims. A useful default is one matched before/after pair or two to
three representative images/frames; motion claims need a short clip or a small
consecutive frame sequence. This is a starting point, not a hard cap: request
more only when distinct criteria cannot be judged or a safety/regression concern
requires it. Record why each selected artifact was chosen.

When independence matters, give the reviewer the criteria and raw selected
artifacts before revealing the worker's favorable verdict. After its first
assessment, provide the local observations and ask it to resolve disagreements.
The reviewer may request a specific additional crop, image or time range rather
than receiving the whole gallery. Keep all unreviewed claims marked as such.

For separate harnesses, keep the evidence index and raw files at durable paths;
transfer only the selected artifacts through the user's authorized route. A
path in Markdown does not imply the other harness can read that file. Respect
provider input limits and privacy constraints; if selected images cannot be
shared, keep the evaluation local or report the cloud review as unavailable.

## Record the cost and limit

Record total captures, locally inspected captures, artifacts sent to the
expensive reviewer, reviewer requests for more evidence, and available image
input/token or provider charges. Include local inference time separately. Do
not claim savings from a smaller image batch alone; compare total review cost
and accepted quality with the previous process when data is available.
