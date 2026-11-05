# Example ladder profile

Copy this file to `~/.config/androskills/ladder.md` and replace placeholders with models, providers and permissions actually available in your harness. Delete stages you do not want, or change their order or roles. A profile is read as instructions; it does not install models, launch agents, enforce limits, or configure API credentials. Do not store secrets here. A current request can override it.

This example is a sequence of model stages. The separate coordination ladder in [references/coordination-ladder.md](references/coordination-ladder.md) describes ways agents may cooperate within those stages. This longer example spends the early stages locally, uses a lower-cost cloud model for review, then reserves a stronger model for integration and final judgment. It is an example, not a requirement to run six stages on every task. If a stage cannot run with the selected model, report it and preserve a handoff instead of substituting another provider.

## Stage 1 — local scope and plan

- Provider / model: <local provider> / <local model ID>
- Assignment: inspect the task and relevant artifacts, identify acceptance criteria and risks, and outline bounded implementation work.
- Pattern: sequential. Do not send private inputs to a cloud provider at this stage.

## Stage 2 — local implementation

- Provider / model: <local provider> / <local model ID>
- Assignment: implement the task, run appropriate checks, and fix in-scope failures while useful progress is possible.
- Pattern: sequential by default. If explicitly authorized and supported, independent components may be handled by bounded parallel specialists with non-overlapping workspaces.

## Stage 3 — local verification

- Provider / model: <local provider> / <local model ID>
- Assignment: check the actual artifact against the original requirements, exercise likely failure cases, fix in-scope problems, and record test results and remaining risks.
- Pattern: sequential. Reusing the same model and context is a verification pass, not an independent review.

## Stage 4 — lower-cost cloud review and fixes

- Provider / model: <approved lower-cost cloud provider> / <lower-cost model ID>
- Assignment: inspect the local result for missing requirements and bugs; make authorized in-scope fixes and run available checks.
- Pattern: sequential. Send only material explicitly allowed for this provider.

## Stage 5 — independent reviews, when supported

- Provider / model: <approved lower-cost cloud provider> / <selected reviewer model ID>
- Assignment: two read-only reviews of the same pinned artifact and original criteria; one looks for correctness and regressions, the other for overlooked requirements, counterexamples and appropriate privacy/security concerns. Each reports evidence and limitations before seeing the other's findings.
- Pattern: at most two parallel workers if the host and user allow it. Otherwise run the authorized reviews sequentially where possible, disclose shared context and reduced independence, or provide a handoff. The reviews share this stage's total budget.

## Stage 6 — final integration and polish

- Provider / model: <approved higher-quality cloud provider> / <final model ID>
- Assignment: verify the artifact and reviews against the original request, investigate important disagreements, integrate needed fixes, run appropriate checks, and report what did and did not run.
- Pattern: sequential integrator. Preserve legitimate dissent and disclose unresolved issues.

## Limits and sharing

- Work/review passes per stage: 3 total by default, including the initial pass; override per stage when needed.
- Consecutive attempts without progress on one blocker: 2 by default, then record it and continue independent work or hand off.
- Coordination pattern: <solo, fan-out, effort scaling, pair, or manager; long-lived leads and swarms require explicit authorization and compatible host support>.
- Maximum simultaneous parallel workers: 2 by default, subject to the host's total-agent limit; a coordinator may consume an additional slot.
- Maximum total spend, tokens or elapsed time: <set an actual limit or say none specified; host enforcement is required for a hard cap>.
- Per-stage limits and behavior when a limit is reached: <optional>.
- Allowed cloud sharing by provider: <list approved files or categories; exclude secrets and unrelated private data>.
- Shared-workspace and merge rules: <choose isolated worktrees if supported, or non-overlapping ownership and one integrator>.
- Other task-specific constraints: <optional>.
