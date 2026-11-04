# Example ladder profile

Copy this file to `~/.config/androskills/ladder.md` and replace the placeholders with model IDs and provider names available in your harness. This is a profile for the agent to read; it does not install models, configure accounts, enforce a budget, or cause the harness to switch models. Do not put API keys or passwords here.

## Stage 1 — implementation

- Provider / endpoint: local model server
- Model: <your local model ID>
- Assignment: implement the main task and run appropriate checks.

## Stage 2 — review and fixes

- Provider / endpoint: <your lower-cost cloud provider>
- Model: <your lower-cost model ID>
- Assignment: review the implementation for bugs and missing requirements, fix what is within scope, and report checks and remaining issues.

## Stage 3 — final review

- Provider / endpoint: <your higher-quality cloud provider>
- Model: <your final-review model ID>
- Assignment: independently check the result against the original request, correct material problems, and polish it.

## Limits

- Work/review passes per rung: 3 total, including the initial pass (change per rung if useful).
- Consecutive attempts without progress on the same blocker: 2; then record the blocker and continue independent work or hand off.
- Cloud sharing: <what task context and files may be sent to each provider>
- Maximum spend or tokens: <optional limit, and what to do when reached>
- Other constraints: <optional>
