# RiVaL design session — findings and reasoning (2026-10-29)

Status: in progress. Three rival reviewers are still running; their reports will land in
`rival-source-review/swarm/` (local, untracked) and feed design v3. This document records what was
found and decided **before** those reports. Each claim is tagged: **SOURCE** (directly in a file),
**VERIFIED** (checked by command this session), **INTERPRETATION**, or **OPEN**.

## 1. Request and approach

- `/design` was invoked with a Python extractor as the brief. That pointed to a design drawn from the
  making-of-RiVaL conversation. INTERPRETATION
- The owner then asked for:
  - the output to go in `rival-design/`
  - a deep-dive approached "as a subagent swarm with rivals"
  - versions kept side by side ("don't remake or remove v1, do v2 v3")
  - a changelog commit
  - this findings document
  SOURCE (session messages)
- Design target: a landing page for RiVaL. HTML item 75 names `RiVaL.avatararts.org` as a destination. Deployment was **not**
  requested and nothing was deployed. SOURCE / VERIFIED

## 2. Sources and their identity

| Source | Facts | Tag |
|---|---|---|
| `~/Downloads/making-of-RiVaL (1).html` | 246,527 bytes · SHA-256 `21ccdcfabed340887b900f5598c956b855703e16e125a14cd6dbfb82fa66053f` | VERIFIED |
| Copy in `source-backing-html-continuation/` | Same SHA-256 as the Downloads original | VERIFIED |
| Extraction (`extract-html-visible.py`) | 77 items: 42 user, 35 assistant; no unclosed item | VERIFIED |
| Earlier backing JSON | 27 user nodes. The HTML adds 15 user entries; the first 27 line up in order (24 identical, 3 with attachment labels appended) | SOURCE (other agent's alignment file); counts VERIFIED (42 − 27 = 15) |
| GitHub `AvaTar-ArTs/RiVaL` | Public. 9 commits, 2026-10-30 02:01–02:29 UTC. 10 files: README, `docs/` and `docs/research/` | VERIFIED (`gh api`) |

The extraction is static. No HTML scripts, remote libraries or assets were run. Images and
attachments are not part of the extracted text. VERIFIED

## 3. Authorship: who sent it vs who wrote it

- A "user" role in the HTML proves who **submitted** a message, not who wrote it. SOURCE (other agent's review), checked
  here against the text: INTERPRETATION confirmed for these items:
  - **Item 23** mixes the owner's own stream of thought with pasted material:
    - an assistant-style money-making list (owner-sent)
    - a quoted "lab coat… 91 rooms" passage, which is pasted assistant text
  - **Item 59** pastes assistant commentary on the working name.
  - **Item 67** pastes Cindy's earlier answer ("The philosophy determines what counts as useful…").
- The owner's **own** words on the metaphor (item 23):
  > "if roomc and room6 are just as opposite as alike and the hallways is long and not a room and then
  > the stairs are there ---- but the one in the coat is the reason why the coat is the thing it is --
  > the before the coat and after doesnt on and off -- its the spacde that is certain and constant …
  > the only constant is that of change -- which itself will never change"
  SOURCE
- Other direct owner statements used in the design:
  - item 3: "if you dream it, we can achieve it"
  - item 5: translate, then personalize
  - item 13: "call it RiVaL"
  - item 19: "rival == meaning equal partners in all things, even the exact identical opposites"
  - item 21: "like a spring [sparring] partner"
  - item 54: "Min Maxer's Agent Theory craft"
  - item 56: "center the features and functions on what i already do -- just this is the built in"
  - items 58/61: five experiments, one at a time, "swarm rivals each independently --- then in a batch kind -- then in total"
  SOURCE

## 4. GitHub repo findings

- Commit **`b0b0a73`** exists (2026-10-30T02:08:53Z) and adds
  `docs/research/SWARM_REVERSE_ENGINEERING.md`. The earlier handoff called this SHA "asserted at 301
  but not independently confirmed". That claim is now **confirmed**. VERIFIED. The handoff itself was not
  edited. OPEN: add a note beside it if wanted.
- The repo text was drafted by an assistant and pushed by Cindy under the owner's authorization (item 42).
  INTERPRETATION (based on commit timing and the conversation)
- `docs/PHILOSOPHY.md` assigns fixed meanings: wearer = identity, coat = role, room = context,
  hallway = relationship, stairs = transformation. It calls these "working metaphors", but Cindy's later review
  (around item 74) flags that this still freezes each image's function. SOURCE
- README tagline: "If you **can** dream it, we can achieve it." The owner's item 3 has no "can". The design
  uses the owner's wording. VERIFIED
- The repo states no runtime exists and that the five-swarms program is "research design … not executed
  runtime experiments". This matches the design's "Not started" statuses. SOURCE

## 5. Checking the other agent's report

- An agent's report was pasted, claiming:
  - the HTML was preserved
  - there are 15 more user entries
  - the handoff was updated
  - earlier versions were kept
- All four claims checked out. VERIFIED
- One gap: `RiVaL-export-guide.md` was also rewritten at 22:48 with no `before` copy. That goes against the
  no-overwrite rule. VERIFIED (timestamps; no earlier copy found)
- That report's main point was to center RiVaL on existing workflows and run the experiments in order, then compare.
  It was adopted into v2. SOURCE

## 6. Design decisions

**Look** (shared by v1 and v2):
- dark ground `#0E0F12`
- two accents of equal strength, blue `#5B9CFF` and orange `#FF8A3D`
- Space Grotesk with JetBrains Mono

Neither partner's colour dominates, and the "V" in the wordmark is the neutral seam: equal standing
is expressed in the design itself. The accents can be changed under Tweaks. Blue and orange were chosen over
red and green for colour-blind safety. INTERPRETATION (design rationale)

**v1** (`Main.dc.html`) sections: hero, the meaning timeline, five coat/room cards, reciprocal-review rules
with the withdrawn-objection case, the five experiments, footer.
Problems found after publishing:
- The coat cards and the line "The philosophy is not decoration…" come from item 67, Cindy's pasted text,
  but the page presents them as RiVaL's own position.
- It shows experiments 02–05 as "Pending" without saying they run in order.
- It frames RiVaL mainly as an agent-review method.
v1 is kept unchanged as the record.

**v2** (`Main-v2.dc.html`, beside v1):
- New "The work comes first" section built on item 56. One card holds the candidate workflow (Paste
  conversation intelligence, marked "candidate · not yet run"); two `[YOUR WORKFLOW]` placeholders take the place
  of invented examples.
- The coat section quotes the owner's item 23, with spelling tidied and labelled "a metaphor still being
  worked out". The fixed mapping and item 67 text are removed.
- New rule: "Who sent it is not who wrote it".
- Experiments: in order, run as rivals independently → batch → total. Statuses: 01 "Design ready · tests pending"
  (item 61), 02–05 "Not started". The section also states that no experiment has run.

Not put on the page: local paths, account or owner IDs, raw transcripts. VERIFIED (by authoring)

## 7. Rival swarm (running)

Three independent reviewers, each with a separate task and one output file:
- **rival_meaning**: the owner's goals in order, core concepts, what items 60–77 add, faithfulness of v1/v2.
- **rival_counter**: competing readings, flattening, pasted-vs-owned text, privacy/trademark risk,
  whether the public repo freezes the meaning, and a counter-proposal. It must list objections it withdrew.
- **rival_evidence**: extractor correctness, mapping between the HTML and the JSON, a line-by-line fact-check of the design's
  quotes, and a re-check of `b0b0a73`.

The repo and v2 were added to all three while they were running. Limit: they share one model family.
Separate tasks reduce shared framing but do not make them statistically independent. OPEN: their
findings, cross-challenges and v3.

## 8. Open items

1. Cross-challenge the three rival reports; keep what survives a source check; build **v3** beside v1/v2.
2. The owner fills in the `[YOUR WORKFLOW]` cards, or names the workflows to center on.
3. Decide whether the design follows the owner's words or the public repo's wording, and whether the
   repo's PHILOSOPHY.md should be revised (no push without explicit approval).
4. Optionally add a dated note beside the handoff recording that `b0b0a73` is confirmed.
5. The canvas is private; it must be shared from its Share menu before anyone else can open it.
6. This local git repo has no remote and its history is separate from GitHub `AvaTar-ArTs/RiVaL`.
   Pushing here would need a decision about how the two histories relate.

## 9. What was not done or checked

- Nothing was deployed, pushed, or written to GitHub, Notion or the server.
- The design was not rendered or screenshotted. Phone-width layout was built in but not visually confirmed.
- Not all 5,272 extracted lines were read in this session; the swarm is doing the full read.
  Coordinator reading here: all user items (shortened), items 23, 53–77 headers, 56, and the coat passages.
- The JSON transcript and the HTML were not compared independently; that relied on the other agent's alignment
  file plus the count check.
