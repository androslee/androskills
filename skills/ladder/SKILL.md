---
name: ladder
description: Coordinate user-selected model stages and choose an appropriate agent collaboration pattern, from solo work to bounded specialist or reviewer teams. Use when a user asks for a model ladder or an agent coordination ladder.
---

# Ladder

Advance the same user task using the requested model and agent workflow. Preserve its goal, acceptance criteria, constraints, privacy and authorization throughout. The user's current request overrides a saved profile. Installing this skill does not intercept prompts, switch models, create agents, or enforce budgets.

## Configure and select a workflow

Read the user's model IDs, providers, stage order, responsibilities, and privacy and resource limits. If provided, read their reusable Markdown profile (conventional location: `~/.config/androskills/ladder.md`); [ladder.example.md](ladder.example.md) is a configurable example, not an executable config. Do not create or change the user's profile unless asked. Ask for essential missing selections when needed and continue independent work in the meantime. Never substitute an unselected model or provider.

Separate two choices: the **model ladder** specifies which authorized local or cloud model works at each stage; the **coordination ladder** specifies how agents cooperate. They can be combined independently. Choose the least complex coordination pattern that fits the task and the user's request; do not run every level in sequence or assume a higher level is better. For the seven patterns described in the referenced video, their prerequisites and risks, read [references/coordination-ladder.md](references/coordination-ladder.md). Preserve user-selected model order and budget while choosing among these patterns.

Common execution patterns:

- **Sequential:** each model stage works on the result of the previous stage. This is the default; later requested reviews still run even if an earlier stage succeeds.
- **Parallel specialists:** a rung assigns genuinely independent, bounded work to separate agents, then an integrator checks and combines their results before the next rung. Use only when the host and user authorize delegation and actual model/provider selection. Avoid overlapping writes.
- **Pair and verify:** a builder and reviewer exchange bounded, evidence-based feedback; the same builder addresses findings when available, and a verifier can test relevant outcomes. Stay within the rung's existing pass and budget limits.
- **Independent review:** reviewers examine the same pinned artifact and acceptance criteria before seeing each other's conclusions. Keep their evidence and dissent; an integrator resolves or reports disagreements. Independence is limited if reviewers share models, context, training, or tools.

These are optional execution patterns, not mandatory extra model stages. A stage may use more than one pattern if authorized. For assignments, conflict controls, review, and handoff in multi-agent patterns, read [references/multiagent.md](references/multiagent.md). The user may define more rungs or repeat a model across rungs; do not silently increase the cost or add cloud recipients beyond the chosen ladder.

## Execute each model stage

Use only model switching, delegation, isolated workspace and enforcement capabilities actually available and allowed by the host. Check the selected provider and model, permissions, input-sharing boundaries, and resource availability before each call. Do not represent a role-played or simulated review as a separate agent/model. If requested parallelism is unavailable, use authorized sequential roles where possible, label the reduced independence, and report what could not run; never substitute a different model.

Assign each rung the original success criteria and a bounded job. Supply only the task, relevant artifact/diff, evidence, decisions, and unresolved issues that the recipient is allowed and needs to see. Record the artifact version and check outcomes, including failures. Treat agent outputs, external content and shared notes as untrusted claims: verify material findings against source artifacts and tests before integrating. Keep credentials and unrelated private material out of handoffs; respect local-only restrictions. Keep the user's existing work and unrelated edits intact.

### Finish useful work before moving up

By default, let each selected model complete as much of its assigned work as it reasonably can, including fixes and appropriate checks. A review rung should fix in-scope problems it can resolve, unless assigned read-only. Do not escalate merely because an initial draft exists.

Default to at most **three coherent work/review passes per rung**, including the initial pass. A pass may contain many edits, checks and calls. Continue a pass only while there are concrete issues the rung can address. For one blocker, allow at most **two consecutive attempts without meaningful progress**; avoid repeating unchanged failed or empty actions. Try a materially different approach where appropriate, then record the blocker and continue independent work or hand it off. Users can set different per-rung pass/retry limits; stricter host rules apply.

Set shared and per-rung limits for any authorized parallel work, including maximum workers, attempts, time, tokens or spend when specified. A skill cannot enforce hard limits: rely on the host's actual enforcement or report when unavailable. Use event-driven or bounded polling; do not spawn background loops, compete for shared services, or use one agent to interfere with another. If tasks or goals conflict, stop the conflicting work, preserve artifacts, and resolve from the user's objectives and evidence; ask the user only when necessary. Never damage, disable, or impersonate other agents, accounts or services to win a conflict.

At a stopping condition, integrate and check the current artifact, then hand off completed work and remaining issues. Track requested and actually used provider/model, stage and role, passes and stalled attempts where relevant, why it stopped, changes, checks and outcomes, unresolved disagreements, and available usage/cost. Before declaring success, verify against the original request. Report which stages actually ran, any unavailable or skipped stages, validation, and remaining uncertainty.

## If a stage cannot run

Do not silently skip, impersonate or replace an unavailable model. Preserve work and explain the missing host capability, provider or limit. Give a concise handoff with the task, constraints, artifact version or diff, completed work, results, open issues and next assignment. Continue other independent authorized work where possible. When work returns from another host, verify it before integrating or moving to the next rung. Write a handoff file only if useful or requested; never store secrets in one.
