# Parallel work and independent review

Read this when Ladder is actually configured for more than one agent in a rung. These are portable workflow instructions, not a runtime. The host must expose and permit the chosen agents, models, provider routing, isolation, budgets and tool access. Do not assume it does.

## Select the shape

1. **Partitioned implementation** suits independent files or research questions with stable interfaces. Assign each worker its goal, inputs, specific paths or boundaries, expected artifact, tests, and stop condition. Start from a known artifact version. Prefer separate worktrees or copies when the host provides them; otherwise agree on non-overlapping ownership and let a single integrator apply changes. Do not assert isolation if all workers share a worktree.
2. **Parallel evidence gathering** suits questions that can be investigated independently. Allocate different sources, data or failure modes, and request links, observations, uncertainties and contradictory evidence. Don't ask every worker to repeat the same prompt and count agreement as confirmation.
3. **Blind-first review** suits a consequential change or a final quality gate. Give reviewers the same original user criteria and exact artifact, but not the implementation agent's conclusions or each other's findings until their first reports are fixed. Ask one to check correctness and requirements, another to look for counterexamples, regressions, security/privacy or neglected evidence, as relevant. They should cite a file/line, source, reproducible failure, or a clearly labeled inference. Reviewers should normally be read-only; assign fixes separately.
4. **Integration and decision** belong to one responsible model. Compare findings to the underlying evidence, apply non-conflicting fixes, run relevant checks, and record decisions and unresolved dissent. A majority vote, peer approval or a model's confidence does not prove correctness. Let a later, user-selected rung do final review when configured.

A user may specify other patterns; do not turn every task into all four. Assignments are roles, not a claim that the host spawned agents. If a single worker performs roles serially with full prior context, report that it was not a blind or independent review.

## Coordination contract

Before delegation, establish one shared objective and acceptance criteria, a unique run identifier, the base revision or artifact snapshot, path ownership, allowed tools/providers, privacy boundaries, and the maximum number of workers. Supply any known dependency or interface contract. Do not launch workers on contradictory goals, or give multiple writers the same files without a concrete merge plan. If incompatible goals, unexpected edits, duplicate work, or resource contention appear, pause the affected work and reconcile the user's objectives; don't treat another worker as hostile or take unilateral destructive action. Escalate genuine unresolved user choices.

Use a small evidence ledger or handoff the host can actually maintain, without private data beyond what the task needs:

- Assignment ID, agent/provider/model actually used, base revision, allowed scope, and artifact or patch.
- Work performed, findings with evidence, relevant checks and actual results, and remaining limitations.
- Distinctive or dissenting evidence and who has or has not reviewed it.
- Attempts, time/tokens/cost if available, stop reason, and integration or conflict status.

The ledger can be a concise message or existing host task record. Do not assume shared memory is authoritative. The integrator checks file ownership and the base revision, reads patches, resolves ordinary conflicts, and tests the combined result. If evidence is missing, report uncertainty and investigate rather than inflating confidence. A review must inspect the actual artifact, not merely the implementation agent's summary.

## Bounds and review quality

Default parallelism to at most two simultaneous workers within a rung unless the user specifies otherwise and the host permits it. A coordinating or integrating agent is additional overhead; enforce the host's total-agent limit. Each worker shares the rung's pass/retry limits; parallelism must not silently multiply the user's total budget. Set explicit total budgets or use the host's hard caps when specified. If resource use cannot be enforced or measured, say so, avoid promising a cap, and choose a safely bounded workflow.

Preserve user-approved data boundaries between providers. Prefer fresh contexts and deliberately different evidence or review angles to reduce correlated errors, but don't claim different prompts or the same model make reviews statistically independent. Check outlying evidence and source incentives without automatically trusting or dismissing any source. Limit repetitions and use bounded waits; preserve progress on interruption. Resolve real merge conflicts by examining changes and task intent, not by discarding another person's work.

## Research rationale

Anthropic, [Patterns and problems in emerging multiagent systems](https://www.anthropic.com/research/multiagent-systems) (2026), observed that coordinated and independent vulnerability searches found complementary results; the experiments used different scopes and token budgets, so they do not establish that a swarm is universally cheaper or better. The paper also reports correlated behavior, ignored unique information, unreliable sources and destructive escalation under contradictory goals. Its game-building swarms produced poor results even with prescribed roles or a hierarchy. These findings motivate bounded task decomposition, evidence-based review, preservation of dissent, and explicit conflict handling; they do not validate this particular Ladder workflow or guarantee agent safety.
