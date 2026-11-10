# Design and roadmap

## Scope today

The portable `sherlock` skill instructs an agent to choose available skills first and search for missing skills using a sanitized generalized query. The optional Python helper offers bounded filesystem discovery, explainable lexical ranking and a read-only skills.sh query. The agent—not the Python script—understands the prompt and decides whether a skill is relevant. It is possible for a model to ignore or misapply the skill; local metadata and external listings are untrusted data.

When an initial candidate only covers a task's broad label, the skill now calls for a bounded second pass: name the specific gap, search specialist terms across relevant dimensions, inspect source instructions and examples, and compare what each candidate would actually change. A task-specific mini-trial is appropriate when procedural claims remain uncertain. This is intended to reduce shallow matches such as selecting a generic UI skill when the missing capability is distinctive art direction. The helper itself is unchanged and does not implement semantic or multi-source search.

Available skill information differs across harnesses. Filesystem probing is a fallback and cannot enumerate plugins, connectors, disabled or overridden skills with full fidelity, or every custom configuration. Prefer the host's catalog and actual skill invocation API. The helper attempts to skip common implicit-invocation opt-outs; that is not a complete permission or policy check. A skill explicitly requested by the user may need a different treatment from an automatic match.

## Before-every-prompt integration (not implemented)

A genuine hook belongs in the harness rather than in a self-triggering skill. A future adapter should:

1. Run after user and system instructions are available and before the main response, with an opt-out, a time budget and a clean fallback when the router fails.
2. Retrieve the current authorized catalog using the harness's provider APIs, including precedence, namespace and invocation policy. Respect named/required skills and session context, without recursing into Sherlock.
3. Ask the agent or an optional local classifier to produce a minimal task description and select zero or more skills. Restrict output to catalog IDs; validate the decision, do not interpret a score as certainty, and invoke through the host's normal skill mechanism.
4. If nothing fits and the user's network/privacy policy permits it, derive a generic search query that excludes project names, secrets, user data and the full prompt. Do not assume automated redaction is perfect. Search failures must not stop unrelated work.
5. Keep external candidates in a separate untrusted-results view with provenance and review. No external instructions are injected, installed or executed just because they ranked highly.
6. Avoid repeating work across turns with bounded, opt-in caching; never cache private prompt text by default. Make routing decisions inspectable without logging sensitive input.

No DSH code, hooks, system prompts, service settings or running sessions are modified by this project. Host integration must be designed and tested against that host's actual lifecycle and APIs before claiming automatic coverage.

## Evaluation targets

Build a labeled test set covering explicit skill requests, paraphrased tasks, multiple skills, no-skill tasks, plugin skills, disabled skills, ambiguous cases, and requests with private data. Include shallow-match cases where the task label differs from the actual gap (for example, functional UI layout versus distinctive visual direction). Measure precision/recall and especially harmful false-positive activation; test abstention and zero-match behavior. For discovery quality, compare candidate relevance and outcome on bounded matched tasks, counting search and instruction overhead. Measure latency and compare against the host's native selector. Exercise local, no-network, remote-search failure, prompt-injection and source-impersonation cases. Check that only generic queries leave the machine. Use a separate holdout set and do not claim universal routing based on the helper's unit tests.

Potential enhancements: an adapter for DSH's runtime skill catalog; optional local embeddings or LLM classification with benchmarking; GitHub provenance and license verification; explicit user-approved installation; and a versioned registry of review decisions. None is implemented.
