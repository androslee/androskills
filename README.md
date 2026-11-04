# Sherlock

Sherlock helps an AI agent understand a request, find relevant skills already available to its harness, and look for external skills when an installed one does not fit. It is a small standalone skill project, inspired by [tstack](https://github.com/t3dotgg/tstack)'s `skills/<name>/SKILL.md` layout.

**Status:** first prototype. Sherlock can be invoked as `$sherlock` in compatible harnesses. An installed skill does not, by itself, force an agent to route every prompt through it; true before-every-prompt behavior needs an explicit integration in the host harness. No such hook is included here. See [design](docs/DESIGN.md).

## How it works

1. The agent generalizes the task without losing user constraints and consults the **harness's skill catalog**. Explicitly requested and mandatory skills take precedence.
2. It reads and applies the useful skills using the harness's own loading mechanism. It can choose multiple skills or decide none is useful.
3. If no installed skill fits and online search is permitted, it searches using short, generic capability terms, not the full prompt or private details.
4. It treats search results as untrusted leads and checks their origin, actual instructions, dependencies, permissions, license and fit. It never silently installs or executes a third-party skill.
5. If nothing fits, it continues the user's task using normal tools.

Sherlock uses the agent's reasoning to generalize and select skills. The included helper can inventory common filesystem roots and rank their names/descriptions by **keyword overlap**; it is not a semantic classifier and its score is not a confidence probability. It may miss relevant skills, find irrelevant ones, or miss plugin, bundled and remote skills. The harness's catalog is authoritative when available.

## Install

Copy the `sherlock` folder into a skill directory supported by your harness:

```bash
# DSH, for your user account
mkdir -p ~/.dsh/skills
cp -R skills/sherlock ~/.dsh/skills/

# Codex, for your user account
mkdir -p ~/.codex/skills
cp -R skills/sherlock ~/.codex/skills/
```

Run these commands from this project's root. Do not overwrite an existing skill without reviewing it. Harnesses may need a fresh session to discover changes. DSH's catalog can also include project-specific, bundled and custom providers; filesystem scanning cannot represent all of those sources. Sherlock does not alter harness configuration or restart DSH.

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
