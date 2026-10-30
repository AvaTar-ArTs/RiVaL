# RiVaL architecture: working draft

> Status: proposed architecture, not implemented functionality.

## Goal

Create an agentic system where independent partners can propose, challenge, test, revise, and validate work across software development, research, and creative automation.

## Conceptual layers

1. **Identity** — persistent agent identity and provenance.
2. **Role** — changeable task-specific responsibilities and tool scopes.
3. **Context** — session, project, available evidence, and environment.
4. **Capability** — tools, skills, models, and adapters.
5. **Relationship** — collaboration and review links between participants and artifacts.
6. **Orchestration** — task coordination, handoffs, deadlines, and review gates.
7. **Evidence and memory** — append-only or auditable records with revisions and attribution.
8. **Authorization** — explicit limits on execution, data access, and publication.

The layers should be modeled separately, not flattened into a single prompt or folder.

## Minimum viable reciprocal-review loop

1. A user states an objective and acceptance criteria.
2. A builder proposes a plan or artifact.
3. An independent partner examines assumptions, tests, and alternatives.
4. Either partner may revise its position with evidence.
5. Verification uses tests, source references, or observable results.
6. An outcome record preserves agreements, dissent, trade-offs, and decisions.
7. The user controls consequential execution and publication.

For a valid first experiment, agents can run in one process and exchange structured messages. Multiple models and remote execution are later extensions, not prerequisites.

## First milestone

Build a small, testable prototype with:

- Two interchangeable agent roles.
- A structured task and evidence schema.
- Explicit challenge and response turns.
- A deterministic acceptance-criteria evaluator where possible.
- Durable, human-readable review records.
- Tests showing that neither agent is automatically privileged as correct.

## Integration boundaries

Potential adapters: Claude Code, Codex, Pi, MCP-compatible tools, Python automation, and Cindy-related workflows. Evaluate provider terms, licensing, authentication, and safety separately before integration.

Do not treat Cindy's live `CindyGlobal` state as portable source code. No database imports, cloud endpoint replication, or credentials belong in this repository.

## Non-goals for the first milestone

- Reproducing Cindy's entire client.
- Implementing an unreviewed autonomous learning loop.
- Migrating personal memory or private transcripts to a public repo.
- Claiming trademark or official affiliation with referenced projects.
