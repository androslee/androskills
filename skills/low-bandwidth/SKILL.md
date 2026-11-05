---
name: low-bandwidth
description: Keep responses concise for low-bandwidth connections or fit a small display when the user requests low-bandwidth, pager, or 140-character mode.
---

# Low-bandwidth response modifier

Apply this alongside the user's task and other selected skills. Reduce user-facing response size while preserving the actual work, correctness, essential context, constraints, and required citations or disclosures. Do not shorten code, data, commands, quoted material, or requested deliverables in ways that make them incomplete or unusable. Follow higher-priority instructions and any explicit user-specified format or length.

## Modes

- **Low bandwidth (default):** Answer directly in brief plain text, prioritizing the result and necessary next action. Omit repetition and optional background. Use compact formatting and avoid unnecessary markup or large tables. This mode has no invented fixed limit; honor an explicit byte, character or message limit when provided.
- **Pager or tweet (when requested):** Fit the complete user-facing response within 140 Unicode code points, including spaces, punctuation and line breaks, unless the user specifies another limit or its counting rule. Prefer one plain-text message. Count the final message with an available reliable tool when practical; otherwise state that the limit is best-effort rather than claiming an exact count. The 140-code-point convention is not a guarantee of fitting a transport's byte limit, screen width, encoding, or a platform's weighted character count; use the user's specified constraints when known.

If the answer, essential qualification, required citation or disclosure cannot fit safely or accurately, do not conceal the limitation or imply completeness. Give the most important accurate information and a brief indication that more is needed, or explain that the limit cannot be met, depending on the user's priorities and applicable requirements. If the user permits multiple messages, use numbered parts only when necessary; do not silently exceed a one-message constraint. For byte-limited links or payloads, Unicode, encoding and protocol overhead matter; a character limit alone does not enforce a byte budget.

The modifier guides wording; it does not compress the network stream, suppress host-generated messages, count automatically, or enforce limits. Follow host rules for progress and tools; keep any permitted status messages brief. Do not claim that hidden reasoning or tool traffic has been reduced or that content was transmitted successfully merely because the visible answer is short.
