# Engineering decisions and evidence

Androskills explores how an agent workflow can preserve intent, limit wasted
work, and make results reviewable across different models and harnesses. This
guide connects the design to inspectable artifacts. It is not a production-scale
validation report or a benchmark of model effectiveness.

## What is implemented

- Portable instructions under `skills/`, with references and packet templates.
- A [Sherlock Python helper](../skills/sherlock/scripts/sherlock.py) for local
  inventory, lexical ranking, and a bounded directory search.
- A [Downshift packet initializer](../skills/downshift/scripts/init_handoff.py)
  that writes a new draft handoff without invoking a model or replacing a packet.
- [Helper tests](../tests/) for concrete filesystem and command behavior.

The repository does not implement a scheduler, automatic model router, durable
agent runner, or service that enforces the instructions' budgets.

## Decisions worth inspecting

### Put enforceable authority in the host

Skills describe a procedure; the harness controls tools, providers, permissions,
and execution limits. Keeping that boundary explicit avoids presenting a written
budget as an enforced cap. It also makes skills portable, at the cost of relying
on host support and agent adherence.

Read [Ladder](../skills/ladder/SKILL.md),
[Downshift](../skills/downshift/SKILL.md), and the
[host integration design](DESIGN.md). Automatic invocation and enforcement remain
integration work rather than capabilities established by installing these files.

### Use a small, inspectable routing helper

Sherlock's helper ranks metadata by keyword overlap. This is easy to run locally
and inspect without a model dependency, but it can miss paraphrases and cannot
represent every harness catalog. The agent uses the actual host catalog when
available and decides relevance.

[test_sherlock.py](../tests/test_sherlock.py) checks ranking and abstention,
malformed/disabled entries, root overrides, and bounded external results. Those
tests establish helper behavior; they do not establish semantic routing accuracy.
[DESIGN.md](DESIGN.md#evaluation-targets) describes the broader evaluation needed.

### Preserve work across handoffs without overwriting it

Downshift's initializer reads templates before creating the destination, rejects
an existing destination, and creates files exclusively. A resumed packet is edited
as existing work rather than initialized again. Interrupted creation can leave a
partial new directory, which the command reports for inspection.

[test_downshift.py](../tests/test_downshift.py) checks both modes, paths with
spaces, existing content, symlinks, invalid modes, and nonzero CLI failure status.
These are preservation checks, not evidence that the resulting agent plan is good.

### Keep acceptance separate from a worker's confidence

Downshift records pass/fail/unknown against the original acceptance criteria.
Same-model self-review stays labeled, missing motion evidence stays unknown, and
completed child tasks do not automatically close a larger objective. This makes
uncertainty visible, while adding capture, reporting, and review overhead.

Inspect the [visual evidence procedure](../skills/downshift/references/visual-evidence.md)
and [packet templates](../skills/downshift/assets/packet/). Whether this overhead
pays for itself needs comparable accepted outcomes and complete cost accounting.

### Treat workflow changes as hypotheses

Mason can recommend a script, documentation, code repair, skill reuse, or no change.
Workflow Lab keeps scientific analogies as candidate questions with boundaries.
This preserves ideas without quietly adopting an untested procedure.

Read [Mason's evaluation protocol](../skills/mason/references/evaluation.md) and
the [Workflow Lab catalog](../research/workflow-lab/README.md). No pilot results
or demonstrated savings are recorded in that catalog.

## Reproduce the helper checks

From the repository root with Python 3.10+:

```sh
python3 -m unittest discover -s tests -v
```

Inspect the test cases and actual exit status. Passing helper tests does not
validate model behavior, host integration, or the research proposals.

## Evidence that would strengthen this project

The next useful public case study would follow one bounded task from initial
problem through a design decision, implementation, failure, correction, and
external acceptance. It should include:

- A reproducible starting version, task, model/harness settings, and limits.
- The exact intervention and an unchanged baseline or comparable control.
- Artifacts supporting acceptance, including negative results and remaining gaps.
- Planning, execution, retries, tool time, review, and available token/cost totals.
- A description of the human decisions and AI assistance, with links to relevant
  commits or reviews. Repository ownership alone does not establish authorship of
  each implementation decision.

A short recorded walkthrough can complement the case study: explain why an
alternative was rejected, reproduce a failure, and show how the fix is verified.
Only publish material authorized for public release. Personal experience and
employer-scale results require their own evidence; they are not demonstrated by
this repository's helper tests.
