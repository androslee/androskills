---
name: health-baseline
description: Measure and review project performance, resource use and maintenance bloat against a reproducible baseline; use when asked to track regressions or review accumulated changes.
---

# Health baseline

Work with the user's project and its real priorities. Choose a small, relevant set of measurements and assess whether changes in cost buy useful capability, reliability, security or maintainability. Use alongside Ladder when requested, without changing its stages. Never equate smaller code or fewer tests with better software.

## Establish a useful comparison

Identify the affected component, representative scenarios and workload, user-visible requirements, constraints and the decision the measurements should inform. Inspect existing benchmarks, observability, tests and documentation before inventing new instrumentation. Select metrics appropriate to the component, such as latency distribution and throughput, CPU, peak and steady memory, database size/query count/query latency, network I/O, startup time, artifact size, dependency footprint or test runtime and coverage of meaningful behaviors. Avoid collecting data or adding tests merely to increase counts.

Record the artifact revision, environment, hardware, input data shape and scale, commands, configuration and measurement date. Where possible compare a previous baseline and candidate under the same conditions, including warmup, sample count and variability. Note caches, background load, database growth and other confounders. Use isolated or representative synthetic data when feasible; do not copy sensitive production data or impose load on shared systems without authorization. If no comparable historic baseline exists, establish the first baseline and explicitly say historical regression cannot be established. Never manufacture earlier measurements.

## Evaluate and act

Run proportional checks, measure resource use and inspect relevant changes, dependencies, database growth and test suites. Separate measured facts from hypotheses and distinguish intentional growth from avoidable overhead. Investigate large deltas against acceptance criteria and explain tradeoffs; feature changes, data retention and useful reliability checks can justify cost. For tests, assess distinct behaviors, coverage and failure detection before proposing consolidation; don't remove tests simply because they are short, numerous or superficially similar.

Propose prioritized findings with evidence, impact, confidence, likely cause and validation steps. Implement in-scope improvements when authorized, preserve behavior and meaningful tests, then repeat comparable measurements and relevant checks. Avoid destructive cleanup or production migrations without appropriate authorization and recovery. Report failures, missing baselines and limitations rather than promising no future regressions.

If ongoing tracking is requested, reuse existing project mechanisms or propose a small, versioned baseline and reproducible commands with scenario-specific thresholds, reasonable variance and ownership. Do not invent a universal budget or schedule; follow the user's cadence (for example after ten changes) and distinguish an informational threshold from an enforced gate. A skill alone does not collect telemetry, track change counts, schedule reviews or enforce performance limits; the host and project need actual tooling for that.
