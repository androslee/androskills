# Archived optics brainstorm

Recorded: 2026-11-08. **Inactive; preserved for discussion, not execution.**

## Starting idea

The motivating analogy: a model is a fire or light source; tokens are fuel; a skill is a lens that focuses the output so solving a problem consumes less fuel. The discussion broadened to multiple models, Ladder, skills, and harness changes.

The metaphor helps describe attention and resource allocation. It does not establish a physical relationship between tokens, optical energy, or correctness. Language-model answers have no optical phase that would make incorrect answers cancel through destructive interference.

## Ideas to retain

| Optical idea | Proposed workflow interpretation | Possible future mechanism | Limitation |
| --- | --- | --- | --- |
| Lens | Focus effort on relevant constraints and techniques | Smaller task packets, relevant skill selection | Narrowing too much can remove necessary context |
| Interferometer/reference arm | Compare a completion claim against an independent observation | Record criterion, source version, artifact, measurement, and disagreement | The comparison is explicit verification, not wave interference |
| Detector calibration | Check whether a judge notices known successes and failures | Known-good and deliberately broken fixtures; criterion-specific judge scores | Calibration must transfer to the actual task distribution |
| Adaptive optics | Adjust workflow for recurring model/tool weaknesses | Capability/failure profiles; narrowly targeted escalation or tool repair | A profile can become stale or overfit a few examples |
| Beam splitter | Explore independent approaches to a difficult blocker | Isolated candidate solutions or reviews, followed by evidence-based comparison | Two models may share the same blind spot; additional branches cost time |
| Aperture/polarizer | Select relevant context and control what can bias evaluation | Separate worker and reviewer packets; reviewer first sees raw evidence | Withholding essential context can make review worse |
| Feedback cavity | Repeated passes can improve a result or sustain an unproductive loop | Record new evidence per retry; bounded retries and checkpoints | Changed wording is not evidence of progress |
| Double-slit-inspired experiment | Compare individual interventions and their combination | A baseline/cards/review/cards-plus-review factorial experiment | This tests interaction effects; it is not quantum interference |

## Concrete examples from the discussion

- A character's root or foot-pivot position does not prove that the visible boot geometry avoids the floor. A useful reference measurement would examine the rendered geometry or its world-space bounds.
- An image judge might reliably detect two people yet fail at whether someone is eating. Calibration should distinguish these criteria.
- A model encountering a broken capture script needs a tool fix, not necessarily more reasoning tokens.
- Separate model branches can run sequentially on a host that supports only one loaded large model. Independence of evidence matters more than simultaneous execution.
- A reviewer given the worker's persuasive explanation before inspecting the evidence may inherit its interpretation.
- A retry that introduces no new measurement, artifact, or supported diagnosis may merely consume tokens.

## Proposed measurement, not yet performed

Compare four conditions: existing workflow; more exact task cards; separate evidence review; both interventions. Use matched tasks, repeated trials, fixed model settings, and held-out acceptance criteria. Count planning, worker, retries, tool runs, review, and repair costs.

Primary outcome: total cost and elapsed time per independently accepted result. Also count false completion claims, regressions, and unresolved tasks. Faster completion of recent task cards does not establish that any one workflow change caused the improvement: task difficulty and no-change findings differ.

## Disposition

The preceding discussion suggested evidence gates, judge calibration, and more selective Ladder routing. The current research disposition is to **save these proposals and broaden the scientific investigation before adopting anything**.
