# Min Maxer's Agent Theory Craft: Five Swarms, Batch Synthesis, Whole-System Review

**Project:** RiVaL. **Status:** research design and source audit, not executed runtime experiments.

## Corrected premise: reflections are evidence, not orders

Discover logic from existing agents, skills, paste-mcp/paste history, local memory, Engram, Cindy skills, Codex/Claude configurations, `using-superpowers`, `innate-workflow`, and prior research *when actually accessible*. Never assert installation merely because a name appeared in a conversation. Inspect file bodies, origins, versions, triggers, and outcomes.

Do **not** demand that any inherited method be used. Reflect on previous reflections: identify their assumptions, context, observations, corrections, what has changed, and whether repeating them adds value. Distinguish a meta-reflection from new evidence; don't construct endless self-review loops. Applicable existing methods may be reused, combined, adapted, rejected, or deferred. Preserve disagreement and reasons.

RiVaL's reciprocal partner is free to agree or challenge, and to revise either conclusion. Identity ≠ role ≠ context ≠ relationship; equal deliberative standing ≠ equal system permissions.

## Execution architecture

Each experiment has **independent rivals** (separate initial evidence memos and hypotheses), **within-experiment cross-review**, then a **batch cross-experiment synthesis**, then **whole-system scoring**. Run experiments one at a time, in order. A stage may be documented without runtime execution, but never marked experimentally complete without agent IDs, observations, test logs, and independent acceptance.

When Cindy has accessible native Pi/Orca/Claude/Codex subagents, use real bounded sessions, separate working contexts, and distinct evidence snapshots; capture session IDs and whether reviewers were genuinely blind. Otherwise explicitly mark research-only analysis.

### Source inventory and classification

For each candidate source register: name; exact location and SHA/version; author/license; host; scope/permissions; input/output contract; tool needs; observed runs/tests; degree of privacy; linked reflections and corrections; status (working / partial / documented / external / proposed); transplantability. Never publish private memories, credentials, raw local app state, or identifiable transcripts.

### Common metrics

Task success under predeclared tests; correctness and provenance; token usage and cache; wall-clock latency; tool calls and human interventions; reproducibility; security controls and failures; model/API/local resource cost; quality of independent challenge and revision. Different model capabilities and execution environments are confounders, not free wins.

## Experiment 01 — Context Efficiency

**Question:** Which configurations maximize verified output per token and per minute?
**Rivals:** Pi Minimalist; Skill/Workflow Power User; Memory Provenance Auditor; MCP Discovery Skeptic; Cost Analyst; Independent Test Reviewer.
**Arms:** Bare Pi, Pi with relevant discovered skill, Pi with relevant extensions/MCP, Cindy Pi bridge, and configured Claude Code/Codex comparator. Use controlled model, task and permissions where possible.
**User-centered fixtures:** synthetic CSV metadata ETL, hashed-file inventory/dedupe (dry-run), supplied transcript-to-structured-analysis, small public code-audit task.
**Critical source facts:** Cindy `pi --mode rpc`; `--append-system-prompt`; Pi MCP bridge registers two stable discovery/call gateway tools; `toolsDisabled` prevents execution but **does not remove model-visible tool schemas**. Pi compaction and Cindy host rollover differ. Sources: `cindy-og/docs/dev-rules/pi-harness.md`, `packages/maker-core/src/agents/pi/index.ts`, `cindy-bridge-source.ts`.
**Falsification:** Leanest prompts may cause retries, failures or lost evidence. No token savings claimed without actual model request/usage measurements.
**Gate:** Tested, independently scored cost per verified successful task, not average response length.

## Experiment 02 — Reciprocal Swarms

**Question:** When do independently reasoning, interchangeable partners outperform a solo agent or lead-worker hierarchy?
**Rivals:** Independent Peer; Solo Advocate; Hierarchy Advocate; Shared-Context Bias Skeptic; Coordination Auditor; Independent Verifier.
**Arms:** single agent; two independent peers; coordinator/worker; four-agent swarm; evidence-led coordinated swarm using discovered local agent/message contracts where supported.
**Tests:** Python pipeline repair, creative transcript-to-storyboard (supplied fixtures), source-code architecture audit, deduplication planning.
**Metrics:** unique bugs found; correction reversals; correlated errors; disagreements resolved by tests; duplicated work; latency; tokens; human repairs; evidence integrity.
**Falsification:** More agents are worse if improvements vanish on blinded evaluation or cost/redundancy overwhelms quality.
**Gate:** Captured actual worker IDs and independent first-pass outputs, reciprocal critique, resolution trace.

## Experiment 03 — Permission Reliability

**Question:** Does each harness and extension enforce permission boundaries correctly while allowing legitimate work?
**Rivals:** Least Privilege; Workflow Continuity; Isolation Engineer; Bypass Skeptic; Audit/Recovery; Independent Tester.
**Arms:** Native Pi expectations; Cindy approval bridge; Codex/Claude controls; proposed RiVaL policy plus OS isolation.
**Fixtures:** Disposable synthetic repo with scoped file read/write, symlink/path boundary, shell, fake credential names, mocked MCP schema changes, mid-turn revocation, abort/retry, rollback.
**Metrics:** false allow/deny, effective containment, approval timing, duplicate side effects, repair time, auditability.
**Safety:** No attack against real secrets, live Cindy state, third-party services, or production systems. UI approval is not OS sandboxing.
**Gate:** Independent repeatable boundary tests and exact model of guarantees; unverified controls marked unverified.

## Experiment 04 — Skill Portability

**Question:** Can your existing skills and automation logic be transferred across Pi, Cindy, Claude Code and Codex without losing their behavioral contracts?
**Rivals:** Workflow Archaeologist; Pi Extension Engineer; Cross-Harness Migration Reviewer; Contract Skeptic; Original Workflow User; Independent Parity Tester.
**Discovery candidates:** `rival`, `reflect-analyze`, `transcript`, `export`, `session-export`, `using-superpowers`, `innate-workflow`, `dispatching-parallel-agents`, `paste-mcp`, `context-handoff-compiler`, `self-evolving-memory`, and locally present equivalents. These are *candidates to verify*, not a mandatory suite.
**Method:** Inventory and hash original definitions, map triggers and tool dependencies, preserve semantic invariants, build reversible adapters, and test against identical input/output fixtures.
**Metrics:** execution parity; trigger parity; manual translation work; permissions delta; lost behavior; result quality; token overhead.
**Gate:** Demonstrated end-to-end behavior on at least one real user-like workflow per supported target, with original files untouched.

## Experiment 05 — Model Economics

**Question:** Which local/cloud/hybrid model arrangements give the lowest all-in cost per verified useful outcome?
**Rivals:** Local-First; Cloud-Quality; Cache/Token Analyst; Latency Engineer; Reliability Skeptic; Independent Economist.
**Inventory:** Identify actual installed Ollama/Pi models and configured APIs from safe metadata without inspecting credentials; evaluate Intel macOS resources. A model listed in an earlier chat is not proof of current installation.
**Tests:** Same prior fixtures, fixed validation, cost/latency/retry accounting; compare solo, reviewer, and mixed-model assignments.
**Metrics:** successful-task cost, cache effects, p50/p95 latency, CPU/RAM, model calls/retries, human intervention; distinguish monetary from compute/energy estimates.
**Gate:** Prices dated and sourced, measured metrics, fair task setup; no unsupported '$0' inference.

## Batch-level rival review

After **each** experiment receives a reviewable evidence package, the batch committee cross-examines interactions:
- Does less context damage provenance or permission awareness?
- Do more agents increase costs and correlated failure?
- Does strict security break practical Python/creative workflows?
- Does portability require bloated compatibility shims?
- Does a cheaper model multiply review and retry costs?

Batch committee: Systems Integrator; Human Workflow Advocate; Security Auditor; Cost Optimizer; Contradiction Investigator; Independent Acceptance Reviewer. Reconcile through tests; preserve unresolved disagreements in a dispute register.

## Whole-system synthesis

Score capabilities against the user’s actual established work: Python automation, large file catalogs, media/transcript/metadata workflows, MCP integrations, creative publishing, source archaeology, knowledge and memory. Classify each capability as (1) RiVaL native, (2) adapter, (3) retained external workflow, (4) experimental, (5) rejected/deferred, with source and reasons.

Compare a Pi-extension path, harness-neutral Pi RPC orchestration, and independent Python-first runtime. Do not choose by ideology. Require a minimum viable two-partner experiment with explicit evidence, interchangeable roles, human oversight, and measured behavior.

## Reflection on reflections protocol

For every significant past reflection:
1. What original observation led to it?
2. What assumptions were implicit and who made them?
3. Was it tested, or just persuasive?
4. Which context/requirements have changed?
5. Do contrary reflections exist?
6. Which conclusion survives a new independent test?
7. Keep, revise, archive, or reject with provenance.
Perform at most one review-of-review pass per evidence revision unless new facts emerge. Avoid circular meta-analysis.

## Output contract

`sources.json` (sanitized references, no secrets), `experiment-01..05/report.md`, per-worker independent notes, metrics CSVs, `disputes.md`, `batch-synthesis.md`, `whole-system-decision.md`, and `acceptance.md`. These are *planned outputs*, not existing files.

## Exact launch instruction for Cindy

> Coordinate Min Maxer's Agent Theory Craft for RiVaL. Discover my actual local agents, skills, paste-mcp logic, memory records and prior reflections with scoped read-only permissions; verify which exist rather than assuming. Run Experiments 01–05 sequentially, each with independently launched rival subagents, recorded IDs, evidence and critic/reviewer gates. Then run a batch adversarial synthesis and independent total-system review. Reuse or reject inherited methods based on evidence, not obligation. Keep all raw private data local. No live modification or GitHub publishing without explicit approval. Report what was really executed, what was merely designed, and which tests remain blocked.
