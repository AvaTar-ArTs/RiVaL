# RiVaL Swarm Reverse-Engineering Protocol

**Status:** operational handoff; source-grounded design, not a claim that autonomous subagents have run.
**Target:** local Cindy checkout plus read-only reference `AvaTar-ArTs/cindy-og`.
**Output:** sanitized research suitable for RiVaL; do not push live state or credentials.

## Mission

Deconstruct Cindy as a reference implementation through parallel, bounded subagent investigations. Reconcile independent observations into an evidence-backed architecture for RiVaL, whose reciprocal partners have equal deliberative standing, without identical permissions or reflexive disagreement.

## Launch gate

Before spawning workers, the coordinating host must verify that actual subagent execution is available, identify the current harness (Pi, Codex, Claude Code, or Orca), determine allowed concurrency and budgets, and verify read-only access to the checkout. If subagent execution is unavailable, report that fact instead of simulating agent outputs.

## Wave 1: independent fact-finding

Assign a distinct worktree or read-only scope to each worker. Each reports exact file paths, symbols, current commit, citations, and uncertainties.

1. **PI-RUNTIME**: `docs/dev-rules/pi-harness.md`; `packages/maker-core/src/agents/pi/`; `apps/desktop/src/main/maker-host/pi-host.ts`. Trace one local Pi session from bootstrap through RPC, tools, events, compaction, and teardown.
2. **ORCA-ORCHESTRATION**: `docs/dev-rules/orca-team-architecture.md`; `packages/orca-workflow/`; corresponding IPC and MCP implementations. Identify worker roles, handoffs, control plane, and review semantics. Separate Part 1 current architecture from Part 2 proposals.
3. **IDENTITY-MEMORY**: `packages/maker-core/src/memory/`, companion runtime and managed-skills code. Trace SOUL, skills, memory, learning state, and session boundaries. Do not read live user memories by default.
4. **SECURITY-BOUNDARIES**: `docs/dev-rules/electron-security-and-process-boundaries.md`; Pi permission bridge, credential boundaries, and remote execution. Document what is actually enforced versus advisory.
5. **EXTENSIBILITY**: `cindy-skill-creator`, `cindy-plugin-creator`, MCP environment, SkillHub integration. Identify lifecycle, activation, isolation, publication boundaries.
6. **PRODUCT-AND-EVAL**: `docs/product-rules/core-product-principles.md`, `docs/README.md`, cindy.app experience claims, `makecindy/eval-bank`. Map claim -> implementation -> test -> unresolved limitations.
7. **LOCALIZATION-AND-PROVENANCE**: glossary, i18n layouts, Chinese-only docs, notices, trademark rules, dependency versions and origin. Distinguish translation, adaptation, original work, and third-party components.

## Evidence contract for every worker

Use this structure:

- Claim and classification: observed source / tested runtime / documented intent / inference / proposal.
- Commit SHA and relevant path plus symbol or line range.
- Mechanism: initiating input, ownership, transitions, outputs and failure modes.
- Existing test names, and whether actually executed.
- Security/privacy and license implications.
- Counter-hypothesis and falsification test.
- Confidence and unresolved unknowns.
- RiVaL relevance, without copying code unnecessarily.

## Wave 2: reciprocal review

Pair different lanes for critique:
- PI-RUNTIME <-> SECURITY-BOUNDARIES
- ORCA-ORCHESTRATION <-> IDENTITY-MEMORY
- EXTENSIBILITY <-> LOCALIZATION-AND-PROVENANCE
- PRODUCT-AND-EVAL independently verifies claims across all lanes

Reviewers must initially see source evidence and claims, not the author's interpretation if feasible. Challenge substantive assumptions, not personalities. Agreement must also be tested against shared-source bias.

## Wave 3: synthesis

Coordinator builds:
- end-to-end Pi execution trace;
- source-grounded Orca multi-agent lifecycle;
- normalized concept map: identity / role / context / relationship / capability / session / authorization;
- trust-boundary graph;
- feature provenance and dependency ledger;
- English translation backlog;
- candidate RiVaL architecture options (Pi extension, Pi RPC adapter, Python-first runtime);
- one minimal two-partner reciprocal-review prototype specification.

Record contradictions in a dispute register; do not resolve without discriminating evidence.

## Wave 4: independent acceptance

A separate verification worker checks each report:
1. Traceable source and correct source version.
2. Current implementation separated from roadmap.
3. Test evidence distinguished from test presence.
4. Credential and user-state exclusion.
5. License and third-party attribution.
6. No unsupported product claims.
7. RiVaL's equal deliberative standing, without removing human control.

## Safety and governance

- No writes to live Cindy/CindyGlobal.
- Do not expose account tokens, cookies, SQLite rows, device IDs, private memory, or transcripts.
- Never push raw application support directories.
- No destructive commands, deployment, installation, or publishing without separate approval.
- Workers have bounded scope, time and token budgets; coordinator owns merges and decisions.
- Report partial findings and blockers rather than inventing a completed swarm.

## First executable slice

Run PI-RUNTIME and SECURITY-BOUNDARIES concurrently; add ORCA-ORCHESTRATION and PRODUCT-AND-EVAL after the first source map. Have the independent verification worker review the Pi lifecycle before any RiVaL prototype code is written.

## Handoff prompt for Cindy

> Act as swarm coordinator for the RiVaL investigation. Read this protocol, inspect the active harness and actual available subagent tools, then launch bounded independent workers against the local Cindy source checkout. Use the evidence contract and reciprocal reviews. Begin with the Pi runtime and permissions lanes. Remain read-only. Return a verified first-wave source map, disagreement register, and next review gate. Do not describe parallel reasoning as spawned subagents unless processes/sessions truly exist.
