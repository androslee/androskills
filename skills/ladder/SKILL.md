---
name: ladder
description: Carry out a user-specified sequence of model stages, such as local drafting followed by cloud review and final polishing. Use when a user asks to split one task across an ordered ladder of models.
---

# Ladder

Use the user's ordered model ladder to advance the same task through distinct stages. Preserve the original goal, acceptance criteria, constraints, and authorization at every stage. The user's current request overrides a saved ladder. Do not imply that installing this skill automatically switches models or intercepts prompts.

## Choose the ladder

Read model names, provider or endpoint, order, stage responsibilities, and any budget or privacy limits from the user's request. If the user has provided a reusable profile, read it; a conventional location is `~/.config/androskills/ladder.md`. The format is ordinary Markdown, not an automatically executed configuration file. An example is in `ladder.example.md` beside this skill. Do not create or modify a profile unless asked.

If essential selections are missing, ask for them when needed while continuing independent work. A common ladder is: a local model implements the first draft; an inexpensive cloud model finds and fixes issues; a stronger cloud model reviews and polishes the result. The user may choose other stages, models or roles. Do not substitute a model, provider, budget, or cloud service without authorization.

## Run each stage

Use only model selection, delegation, and tool capabilities actually provided and permitted by the host. Check that the requested model is available and that the destination is the selected local or cloud provider; follow host rules for delegation. Do not claim that a model ran merely because its role was described in a prompt. Work sequentially: give each stage the current artifact and relevant findings from preceding stages, then inspect its output before handing it onward. Keep the existing worktree and unrelated edits intact.

Give each model an appropriate bounded assignment and the original acceptance criteria. Pass the smallest useful context, changed files or diff, relevant verification results, decisions, and unresolved issues. Do not include credentials or unrelated private material. Respect the user's local-only and other data-sharing restrictions. Use the user's authorized external providers for the task; do not silently send local material elsewhere or fall back to an unselected provider. Avoid repeating the entire task at every stage unless the user wants that.

### Finish useful work on each rung

By default, have each selected model complete as much of its assigned work as it reasonably can, including fixes and appropriate checks, before escalating. Do not stop after an initial draft or a list of findings when that rung can make further progress. A review rung should fix in-scope problems it can resolve. Preserve the user's assigned roles and still run the later rungs for their requested reviews even when an earlier rung reports success.

To bound loops, use at most **three full work/review passes per rung by default**, including the initial pass. A pass is a coherent sweep of that rung's assigned work and may include many edits, tool calls and checks; it is not a limit of three commands or three files. After a pass, continue only if there are concrete unresolved issues the model can address. Stop early if the rung has completed its assignment, cannot make further meaningful progress, or its budget or other user-specified limit is reached. The user may set a different pass limit, including per-rung limits.

For an individual blocker, allow at most **two consecutive attempts without meaningful progress** by default; do not repeat an unchanged failing or empty-result action. Try a materially different approach when appropriate, then record the blocker and continue other independent work on that rung. At a pass or retry limit, preserve the changes, record why the rung stopped and any unresolved items, and hand off to the next configured rung. On the final rung, report unresolved items rather than implying completion. Follow stricter host limits and stop earlier when required.

Track for each stage the requested and actually used provider/model, role, passes and stalled attempts where relevant, reason for handoff, completion or failure, changes, checks performed and their results, and available usage or cost. Distinguish findings from fixes and unverified claims. Respect a stated budget or stage limit. Review the final artifact against the original request and report which stages actually ran, any failed or skipped stages, meaningful validation, and known limitations.

## When a stage cannot run

Do not silently skip, impersonate, or replace an unavailable model. Preserve the completed work, explain the missing capability or provider, and give a concise handoff containing the task, constraints, relevant artifact paths or diff, completed work, check results, unresolved issues, and the next stage's assignment. Continue independent authorized work where possible. If the user runs that stage elsewhere, resume from its returned changes or findings and verify them before the next handoff. Do not write a handoff file unless useful or requested; never store secrets in one.
