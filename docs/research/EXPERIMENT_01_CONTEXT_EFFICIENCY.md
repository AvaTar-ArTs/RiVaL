# Min Maxer's Agent Theory Craft
## Experiment 01 of 05: Context Efficiency

**Project:** RiVaL | **Status:** source-grounded experiment specification, not a completed benchmark
**Baseline date:** 2026-10-29 | **Target:** macOS, Pi, Cindy Pi harness, comparable Claude Code / Codex sessions
**Sequence:** Experiment 1 → acceptance review → 2 Reciprocal Swarms → 3 Permission Reliability → 4 Skill Portability → 5 Model Economics.

### Naming and philosophical boundary

**Min Maxer's Agent Theory Craft** is the working title for the optimization methodology. **RiVaL** means reciprocal intelligence among equal deliberative partners, including allies, apparent opposites, and identical opposites. Neither finding nor objection receives immunity from challenge. This is not adversarial disagreement for its own sake.

### Starting source evidence (not measured outcomes)

Source repository: https://github.com/AvaTar-ArTs/cindy-og

1. `docs/dev-rules/pi-harness.md`: Cindy starts Pi through `pi --mode rpc` (JSONL/stdio); it uses `--append-system-prompt` and retains Pi's default prompt. Large host/companion prompts are supplied via a file.
2. `packages/maker-core/src/agents/pi/index.ts`: Pi provider/model configuration, session lifecycle, tool-policy and prompt assembly.
3. `packages/maker-core/src/agents/pi/cindy-bridge-source.ts`: Cindy's Pi MCP bridge exposes two stable model-side gateway tools (`cindy_mcp_list_tools`, `cindy_mcp_call_tool`) rather than every remote MCP schema at once. Complete schemas remain behind discovery gates.
4. `docs/dev-rules/pi-harness.md` explicitly says `SendOptions.toolsDisabled` suppresses execution but **does not remove tool schemas from the model request**; it cannot be sold as a token-overhead optimization without changing the actual request assembly.
5. `docs/dev-rules/maker-core-and-agent-behavior.md`: Pi native compaction thresholds and native overflow behavior; Cindy imposes per-task context budgets and host rollover on documented deterministic failures. Do not equate compression with preserving all evidence.
6. `docs/dev-rules/pi-harness.md` notes version-matched Pi behavior and a healthcheck script. First pin the actual installed Pi binary/version and reference commit. Do not conflate Pi's various upstream repository lineages.

### Rival investigation swarm

Independent lanes, each with its own written hypothesis and falsification criteria:

- **MINIMALIST**: Lower tool schema + prompt overhead in bare Pi should produce superior efficiency for bounded coding tasks; may fail on complicated workflows.
- **POWER USER**: Existing skills, MCP and orchestration may justify more context because they improve reliability and reduce human effort.
- **PROVENANCE AUDITOR**: Aggressive compression may remove evidence, decisions, or unresolved discrepancies, worsening reproducibility.
- **SECURITY SKEPTIC**: Dynamic tool discovery saves tokens but adds state, permission, schema-gate, and failure complexity.
- **ECONOMIST**: Cheapest tokens aren't cheapest successful workflows; quantify retries, latency, overhead, and paid API calls.
- **INDEPENDENT REVIEWER**: Challenge all lanes, including agreeing conclusions, and demand reproducible evidence.

Real subagents must be launched using Cindy/Orca/Pi host tools and identified by session ID. Parallel source fetching or simulated perspectives alone is NOT a completed swarm.

### Representative workloads: begin with work the creator already performs

1. Python CSV/metadata pipeline: process a sanitized fixture; validate exact output and no accidental source changes.
2. File inventory/deduplication: 1K synthetic paths with deliberately duplicated names and hashes; dry-run only.
3. Audio transcript-to-analysis: supplied transcript fixture with timestamps; produce structured segments, interpretation and prompts without claiming to listen to unavailable audio.
4. GitHub source audit: small synthetic repo or approved public repo; produce source-cited summary and executable test suggestions.

Each task gets explicit functional acceptance tests and source/provenance fidelity checks.

### Controlled variants

A. Bare Pi: native default prompt and tools, no optional extensions.
B. Bare Pi + minimal workflow-specific skill.
C. Bare Pi + selected extensions/MCP.
D. Cindy's Pi harness with host prompts and bridge.
E. Codex and Claude Code comparators if configured and authorized.

Keep model, provider, temperature/effort, task content, worktree and test fixtures comparable *where actually possible*. If provider APIs cannot be matched across harnesses, report confounding rather than claiming a valid cross-harness efficiency score.

For each variant use fresh sessions, fixed snapshots, three or more repetitions initially, and randomized trial order where practical. Measure cold vs warm cache separately.

### Metrics

- `input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_write_tokens` when disclosed
- `tool_schema_tokens` and `system_prompt_tokens` **only when directly observable** or with a clearly marked tokenizer estimate
- total wall-clock time; model calls; tool calls; retries; compactions
- dollar cost using observed usage and a date-stamped provider rate, excluding unknown costs rather than treating them as zero
- acceptance-test pass rate and human corrections
- provenance completeness and lost-decision rate after compaction
- token cost per **verified success**, not simply per response

Do not infer unreported token counts from file size alone. Report tool schema exposure based on actual provider request capture, after redaction, when approved.

### Test plan

**Gate 0: baseline** Verify local installed Pi version, Cindy commit, selected model, consent to API usage and budgets; inspect environment without collecting secrets.

**Gate 1: fixtures** Construct identical synthetic test repos/data; snapshot checksums and acceptance tests.

**Gate 2: runs** Run A–E variants sequentially within each trial, using isolated worktrees, per-turn read-only or scoped write permissions, with logs scrubbed before sharing.

**Gate 3: independent critique** A different reviewer evaluates false efficiency wins (failed task, weaker context retention, hidden human repair time, omitted tools).

**Gate 4: decision** Accept a change only if verifiably better on target workflows without violating minimum success/security/provenance thresholds. Retain negative findings.

### Predicted tradeoffs (hypotheses, NOT findings)

- A lean Pi prompt could improve first-call cost, but omitting critical skills may increase retries.
- Selective tool disclosure may reduce model-visible tool schemas, but demand additional discovery operations.
- Compaction may lower context use while degrading exact history fidelity if no evidence ledger exists.
- A reusable workflow-specific capability may outperform repeated improvisation.

### Acceptance checklist

- [x] Source-grounded architecture anchors identified.
- [x] Rival hypotheses and falsification criteria specified.
- [x] User-realistic workloads and test fixtures defined.
- [x] Quantitative metrics and confounders defined.
- [ ] Actual distinct subagents launched and IDs captured.
- [ ] Baseline environment and model pinned.
- [ ] Controlled trials executed.
- [ ] Independent reviewer signs results.
- [ ] Go/no-go decision recorded.

**Gate verdict: DESIGN COMPLETE; BENCHMARK PENDING. Experiment 02 stays queued pending actual experiment 01 validation, unless the owner explicitly reorders priorities.**

### Exact handoff to Cindy

> Run **Min Maxer's Agent Theory Craft, Experiment 01/05: Context Efficiency** against my local working setup. Follow this file precisely. Use bounded independent subagents for Minimalist, Power User, Provenance Auditor, Security Skeptic, Economist, and Independent Reviewer. First confirm native subagent capability, permissions, Pi/Cindy versions, model availability, costs, and fixture scope. Use the actual workflows I perform. Keep sensitive files local and share only sanitized results. Submit a gate report including worker/session IDs, raw measured metrics, reproducibility, objections, and a go/no-go decision. Do not begin Experiments 02–05 until this gate passes or I direct otherwise.
