# Pi coding agent: RiVaL foundation research

> Research note, 2026-10-29. Architecture reference, not an embedded dependency. No Pi runtime has been installed or tested as part of this commit.

## What Pi is

Pi is an open-source, TypeScript/Node.js coding-agent framework and CLI created by Mario Zechner. It provides a relatively small agent runtime with model/tool interaction, session support, and extension mechanisms.

Primary source: https://github.com/badlogic/pi-mono
Coding agent docs: https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent

## Conceptual layers

- `@mariozechner/pi-ai`: interfaces to multiple model providers.
- `@mariozechner/pi-agent-core`: agent loop and tool calling.
- `@mariozechner/pi-coding-agent`: interactive CLI, sessions, and coding tools.
- Extensions: TypeScript hooks for events, tools, commands, and safeguards.
- Skills: reusable instructions and procedural knowledge.
- SDK and RPC: embedding or controlling Pi from other processes.

Verify exact packages and APIs against the version selected for implementation.

## How Cindy relates

Cindy lists Pi alongside Claude Code and Codex as a harness. Cindy adds its own client, companion, orchestration, memory, UI, tool, device, and provider infrastructure. Cindy documentation describes additional Pi integration for subagents, model routing, compaction digests, and session branching.

Sources:
- https://github.com/makecindy/cindy
- https://github.com/makecindy/cindy/blob/main/docs/dev-rules/pi-harness.md

## RiVaL implementation choices

1. **Pi extension:** fastest experimental path for reciprocal review. Add custom tools/hooks while relying on Pi runtime.
2. **Pi SDK/RPC adapter:** control Pi from a RiVaL orchestrator with independent state, permissions, and records.
3. **Independent Python runtime:** implement RiVaL's own orchestration while using Pi as a reference or optional compatible worker.

Recommended research sequence: explore Pi CLI -> understand agent loop -> test a two-role exchange -> record evidence and provenance -> evaluate SDK/RPC adapter. No local installation or cloud authorization should be assumed.

## Key distinction

A *model* generates responses; a *harness* coordinates model interactions with tools and sessions; an *orchestrator* coordinates one or more harnesses/agents; an *application* provides UI and product infrastructure.

RiVaL's equality is equality in deliberative standing, not unrestricted system permissions. A sparring partner must be able to support a conclusion as freely as it challenges one.

## Licensing and security

Review Pi's current license, all dependencies, provider terms, and extension permissions before redistribution. Third-party brand identities remain their owners' property. Do not import CindyGlobal credentials, local memories, runtime databases, or complete agent homes into this public repository.
