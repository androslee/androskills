---
name: remote-verify
description: Add verification on authorized external physical or remote hosts to a task or any stage of a model ladder; use when the user requests testing changes on remote machines.
---

# Remote verification modifier

Apply this alongside the user's main workflow, including any requested Ladder rung or coordination pattern. It adds remote verification to the selected stage's completion criteria; it does not change model order, escalate to another rung, grant access, or create a remote execution service. Carry the requirement and evidence through handoffs. Later changes invalidate affected verification until retested. If host selection, access or capabilities are missing, continue independent work and report remote verification as blocked, not passed.

## Establish the verification contract

Identify the behavior and observable acceptance criteria, which stage(s) require remote checks, the existing system's normal build, deployment, host-selection and verification paths, and permitted actions. Prefer the user's explicitly identified hosts or a trusted inventory/test group; do not infer permission from connectivity. Resolve selectors to exact host identities and environment, enforce the approved scope and host count, and fail closed if ambiguous, stale, unexpected, or outside authorization. Ask for the missing target or access only when necessary. Never silently substitute production or an unrelated machine.

Identify whether the specified test requires physical hardware; verify the host's identity and relevant hardware characteristics using trustworthy evidence, rather than assuming a VM, container, or hostname proves it. If physical hardware is not required, other authorized remote hosts may suffice. Record the candidate revision, artifact digest or build identifier, configuration and target identity so verification can be tied to the actual candidate and host.

## Execute and iterate

Use the existing system's supported workflow where possible. Check prerequisites and baseline state, deploy or select the exact candidate when authorized, and confirm that the remote execution actually uses it. Run tests that observe remote behavior and state independently of an operation's reported success; where relevant, include expected failures and ensure unintended targets remain unchanged. Record commands or test identifiers, timestamps, targets, candidate identity, outcomes and concise evidence, excluding credentials and sensitive data. Preview or dry-run where useful, but do not count a preview, mock, local test, or agent review as remote verification.

Keep state-changing operations within explicit user and host permissions, existing change controls and the approved environment; use scoped credentials, bounded targets, concurrency, retries and timeouts. Plan cleanup and recovery before mutations. Production changes require the applicable authorization and controls; do not promote or expand scope merely because tests pass. Treat unexpected targets, uncertain identity, failed safety checks, or unavailable recovery as blockers for affected actions.

Feed evidence and failures to the current stage's builder so it can fix and retest within the task's existing budget and retry limits. Do not mark the stage complete if required remote verification is missing or failing. Continue unrelated authorized work; if blocked, preserve work and hand off the concrete blocker, attempted checks and remaining verification. Report cleanup failures and distinguish actual remote passes, failures, skips, and unverified claims. Follow the user's requested later stages without implying that a previous pass validates subsequent changes.

This skill supplies instructions only. The host's tools and permissions must actually perform and enforce remote execution, isolation and resource limits.
