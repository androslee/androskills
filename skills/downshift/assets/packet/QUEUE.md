# Task queue

This is an execution view of the original backlog, not changed acceptance.
Replace a duplicate queue with a pointer to the existing authoritative one.

| ID | Parent | Concrete outcome | Dependencies | State | Card | Result/evidence |
| --- | --- | --- | --- | --- | --- | --- |
| T001 | Unspecified | Planner must fill the task | Unspecified | Draft | tasks/T001.md | None |

Suggested states: Draft, Ready, In progress, Implemented pending verification,
Self-reviewed pass, Partial, Blocked, Independently reviewed, Accepted.
Keep self-review, independent review and user acceptance distinct. Use only the
review authority the contract actually establishes. Do not close an unmet parent
because a child passes. Re-check formerly blocked dependencies after progress.
