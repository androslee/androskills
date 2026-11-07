# Sherlock

Androskills is a collection of portable agent skills, inspired by [tstack](https://github.com/t3dotgg/tstack)'s `skills/<name>/SKILL.md` layout. **Sherlock** finds suitable skills for a request. **Ladder** guides an ordered sequence of user-chosen models to work on and review a task, with optional bounded multi-agent patterns when the host supports them.

**Status:** first prototype. Sherlock can be invoked as `$sherlock` in compatible harnesses. An installed skill does not, by itself, force an agent to route every prompt through it; true before-every-prompt behavior needs an explicit integration in the host harness. No such hook is included here. See [design](docs/DESIGN.md).

## How it works

1. The agent generalizes the task without losing user constraints and consults the **harness's skill catalog**. Explicitly requested and mandatory skills take precedence.
2. It reads and applies the useful skills using the harness's own loading mechanism. It can choose multiple skills or decide none is useful.
3. If no installed skill fits and online search is permitted, it searches using short, generic capability terms, not the full prompt or private details.
4. It treats search results as untrusted leads and checks their origin, actual instructions, dependencies, permissions, license and fit. It never silently installs or executes a third-party skill.
5. If nothing fits, it continues the user's task using normal tools.

Sherlock uses the agent's reasoning to generalize and select skills. The included helper can inventory common filesystem roots and rank their names/descriptions by **keyword overlap**; it is not a semantic classifier and its score is not a confidence probability. It may miss relevant skills, find irrelevant ones, or miss plugin, bundled and remote skills. The harness's catalog is authoritative when available.

## Install

Copy the skills you want into a skill directory supported by your harness:

```bash
# DSH, for your user account
mkdir -p ~/.dsh/skills
cp -R skills/sherlock skills/ladder skills/remote-verify skills/mason ~/.dsh/skills/

# Codex, for your user account
mkdir -p ~/.codex/skills
cp -R skills/sherlock skills/ladder skills/remote-verify skills/mason ~/.codex/skills/
```

Run these commands from this project's root. Do not overwrite an existing skill without reviewing it. Harnesses may need a fresh session to discover changes. DSH's catalog can also include project-specific, bundled and custom providers; filesystem scanning cannot represent all of those sources. Sherlock does not alter harness configuration or restart DSH.

## Ladder: work across models

Invoke `$ladder` and give it an ordered list of available provider/model IDs and a job for each stage. For example, a local model can implement a change, a lower-cost cloud model can review and fix it, and a stronger cloud model can perform the final review. Include any spending limits and what information each provider may receive. You can use a different order or number of stages.

By default each rung works through its assigned task and fixes what it can before handing off. It gets up to three complete work/review passes, including its initial pass, and stops retrying an individual blocker after two consecutive attempts without progress. A pass can contain many edits and tool calls. The next rung receives the remaining issues; later review stages still run when earlier ones succeed. You can set different limits for each rung. These are skill instructions, so a host must enforce any hard spending or execution limits.

Alongside the ordered model stages, Ladder can select a separate coordination pattern: one agent, fan-out, effort scaling, pairs, a manager thread, long-lived leads, or a swarm. These patterns are described in the [coordination ladder](skills/ladder/references/coordination-ladder.md); they are options, not a required seven-stage pipeline. Long-lived leads and swarms are experimental and need host support and explicit authorization. Ladder can also use bounded parallel specialists for independent tasks, or blind-first reviewers followed by a single integrator. It preserves dissent and evidence instead of treating agreement as proof. These patterns are optional: sequential work remains the default, and host permissions, model routing, privacy and resource limits still apply. The [multi-agent reference](skills/ladder/references/multiagent.md) explains assignments, isolation, coordination and the evidence behind these choices.

To reuse a list, copy [the six-stage example profile](skills/ladder/ladder.example.md) to `~/.config/androskills/ladder.md` and fill it in. The profile is read as instructions; it is not a program or a model configuration. Keep credentials out of it. A current request can override it.

**Host support matters:** The skill does not install models, switch the active model, create agents, enforce budgets, or send calls by itself. The harness must expose and permit the selected models and switching or delegation. If it cannot run a stage, Ladder preserves the work and provides a handoff for the user to run with the selected model. It reports which stages actually ran. Installing or invoking Sherlock does not automatically run Ladder on every prompt.

## Remote verification modifier

Invoke `$remote-verify` alongside `$ladder` or another workflow when a task needs verification on authorized external machines. Specify which stage or stages require it, the approved targets or inventory group, and the expected behavior. If physical hardware is required, say so. The modifier keeps verification within the current stage and carries results forward; it does not alter Ladder or automatically grant remote access. The harness must provide and enforce the necessary tools, permissions and limits. If required verification cannot run, the stage must report it as blocked rather than passed. See [the skill instructions](skills/remote-verify/SKILL.md).

Example: `$ladder $remote-verify Implement the change and verify each implementation stage on the authorized test hosts in inventory group staging-lab; use the existing deployment workflow and report the candidate version, hosts and observed results.`

## Mason: learn where a skill would help

Use `$mason` at a task checkpoint to review repeated corrections, rediscovery
or failed approaches for a worthwhile reusable intervention. It can recommend
no change, reuse/routing, a script/docs/code fix, an existing-skill update, or a
bounded new-skill pilot. It does not create a skill merely because a task was
long or difficult.

Mason checks existing coverage, including authorized inactive collections, and
asks what would actually change the next task. It starts with the current model;
a stronger review is an option for a named ambiguity, not a mandatory fee.
Any efficiency claim needs an outcome-preserving comparison that counts
instruction loading, authoring, review and maintenance as well as avoided work.
The included scenarios are calibration examples, not measured proof of savings.

Sherlock finds useful skills; Mason identifies a missing or improvable reusable
workflow; skill-creator can turn an authorized proposal into a package. Mason
does not install or activate its recommendations automatically. Regular
end-of-task invocation needs host integration; installing the skill alone does
not create a background monitor or schedule.

Source: [Mason](skills/mason/SKILL.md). For a pilot or model/cost comparison, see
[the evaluation protocol](skills/mason/references/evaluation.md). To install it
from this repository, copy `skills/mason` into your harness's skill directory
alongside the other authored skills.

Example: `$mason Review the completed work for a reusable lesson. Check existing
skills first and recommend none unless a concrete, testable benefit is likely.`

## Try the helper

Python 3.10+ is enough; no extra packages, local model or API keys are required.

```bash
# Inventory common local skill directories. This does not make network requests.
python3 skills/sherlock/scripts/sherlock.py inventory

# Suggest local skills for a generalized task. Review the matches.
python3 skills/sherlock/scripts/sherlock.py rank 'edit PDF documents'

# Search one skill directory over the internet; the query is sent to skills.sh.
python3 skills/sherlock/scripts/sherlock.py search 'PDF editing'
```

`rank` and `inventory` accept `--workspace /path/to/project`; `--root /path/to/skills` can be repeated and replaces the default roots. Only skill frontmatter and optional local invocation-policy metadata are read. Metadata parsing covers a small YAML subset; unusual skill formats, project root resolution, custom roots and non-filesystem providers may be missed. Output is JSON; it includes file paths locally. No logging or persistence is added by the helper, but the surrounding terminal/harness may record commands and output.

`search` makes a read-only HTTPS request to the public `skills.sh` API and returns names, sources, install counts and directory links. Its query is visible to that service and may appear in network/terminal logs. Use generic words only. A length check is **not** a privacy filter; the caller is responsible for excluding private information. This prototype uses one directory, does not prove a returned repository actually contains a safe or working skill, and does not automatically search GitHub independently or install anything. Install counts are provided by the directory, can change, and are not quality or security ratings.

## Existing projects

- [Vercel `find-skills`](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) is an existing skill-finder and uses the [skills CLI](https://github.com/vercel-labs/skills). Sherlock combines local-first routing with a finder and remains usable without Node.
- [Agent Skill Router](https://github.com/paulpas/agent-skill-router) also provides semantic task routing and integration. Evaluate its provider and deployment requirements before adopting it.
- [tstack](https://github.com/t3dotgg/tstack) is a collection of reusable skills and is the layout inspiration, not a dependency.

## Development

```bash
python3 -m unittest discover -s tests -v
```

See [docs/DESIGN.md](docs/DESIGN.md) for host integration, privacy and evaluation work. The project uses the MIT license.
