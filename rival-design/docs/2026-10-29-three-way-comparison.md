# RiVaL: three-way comparison and corrections (2026-10-29, later)

This adds to `2026-10-29-design-session-findings.md`, which is kept unchanged as the record of what
was understood before the rival swarm reported. Tags as before: **SOURCE**, **VERIFIED**,
**INTERPRETATION**, **OPEN**. HTML item numbers refer to `rival-source-review/html-visible-records.json`.

## 1. The three positions

| | What it is | State read |
|---|---|---|
| **A**: first understanding | local commit `2108945`: v1, v2, the findings doc, the changelog | never pushed to GitHub. Published only to the private claude.ai canvas |
| **B**: public repo | `AvaTar-ArTs/RiVaL` @ `f8afb3657f90…` | 9 commits, 9 files, docs only. Unchanged during the session (VERIFIED `gh api`) |
| **C**: current understanding | the three rival reports plus three comparison reports in `rival-source-review/swarm/` | each claim below re-checked against the HTML by the coordinator unless marked |

The swarm consisted of three independent reviewers. **Meaning** read for meaning. **Counter** gave an
adversarial reading and withdrew 9 objections and then 8 more. **Evidence** audited the extractor and
checked quotes line by line. All three are the same model family, so their agreement is strong
evidence but not proof against a shared blind spot. INTERPRETATION

## 2. Corrections to A's findings doc

| A said | Now | Tag |
|---|---|---|
| The repo was "pushed by Cindy" (§4). Item 74 is "Cindy's later review" | The HTML is a **ChatGPT** export (`chatgpt.com/c/6ae3e968…` and the "ChatGPT Exporter" credit). ChatGPT wrote and pushed the repo through the owner's GitHub connector (items 29, 41, 52; 7 create_file calls match the first 7 commits). Only the pasted items 59 and 67 are Cindy-session text | VERIFIED |
| The repo has 10 files | 9 files | VERIFIED |
| The repo "matches Not started" for experiments 02–05 | EXPERIMENT_01 reads "DESIGN COMPLETE; BENCHMARK PENDING", and 02–05 are outlined and queued. "Not started" understated the work | SOURCE (repo) |
| Item 21 rendered as "spring [sparring]" | The doc was honest about it, but both designs printed “Like a sparring partner.” as a quote. "Sparring" is the assistant's reading (item 22) | VERIFIED |
| The item-23 quote as one passage | It joins two copies. "which itself will never change … universal constant" exists only in the second copy | VERIFIED |
| The tagline is an owner statement | It is the owner's exact wording (item 3), but given as a translation of Cindy's slogan (items 1–3). No owner item adopts it as RiVaL's tagline | VERIFIED |
| Open item 4: note `b0b0a73` beside the handoff | Already done by the other agent: handoff line 157, with earlier copies kept as `*-before-github-verification.*` | VERIFIED |
| The export guide was overwritten at 22:48 | It still holds, and the guide was modified again at 22:55 | VERIFIED |
| The extraction source is `~/Downloads/making-of-RiVaL (1).html` | That path no longer exists. It was only read in this session, never moved. A same-hash copy is in `source-backing-html-continuation/` | VERIFIED |

## 3. A vs B: where each is closer to the owner

**A closer:**
- the tagline without "can" (3)
- item 19 used as the definition
- the "Min Maxer's" spelling (54)
- centering on item 56 (v2)
- the coat in the owner's words, with no fixed labels (v2)
- the rule "who sent it is not who wrote it"

SOURCE

**B closer:**
- "use and reflect the reflections" (63)
- "sparring" not put in quotes
- precise experiment status
- a trademark caveat (15–16)
- the product category "claude code / codex / paperclip kind" (17)
- a no-affiliation line
- plain "no runtime" and "licence not finalized" statements

SOURCE

**Both wrong, from the same upstream source**. A did not copy these from B; both inherited them:

| Shared error | Origin |
|---|---|
| "in all things" narrowed to "in deliberation" | assistant item 20, via the handoff |
| "sparring" presented as the owner's word | assistant item 22, plus the handoff |
| Each coat image fixed to one category | assistant item 24 (and pasted item 67 in v1) |
| Review framing rather than transformation | items 14/18, plus the handoff |
| "Working title" for Min Maxer's | items 59/60 |
| Experiment wording presented as the owner's | assistant widgets in 55/60 |
| The tagline adopted for RiVaL | items 4/14/35 |
| "Equal standing, different permissions" as a rule | item 20 |

SOURCE for the items; INTERPRETATION for the tracing.

Neither A nor B addresses item 76 (Atlas or a broader site, never answered) or item 77 (the
cindy.app capture). SOURCE

## 4. Where C itself was challenged

- **"The built-in" (56).** It is not settled. In items 43 and 53 the owner uses "this" for the
  Pi/Cindy platform, which supports v2's reading. Item 57 supports the other reading. v3 quotes 56
  exactly and states that both readings are open. VERIFIED (items 43, 53, 57)
- **"Design ready" is stale.** Withdrawn by Counter and Evidence. It matches the repo, and the
  revised criteria in items 68/74 were assistant proposals the owner never adopted. VERIFIED
- **Roles "contradict the source".** The cited items 22/50 are assistant text. The line is still
  dropped in v3, because it is assistant wording in the owner's voice, not because it contradicts
  anything. INTERPRETATION
- **"The owner chose to brand publicly."** This overreaches. A public repo and a subdomain fit a
  working codename. OPEN
- **The "must" in item 63.** The statement the owner calls dangerous is not in the extraction. v3 does not
  quote or paraphrase it. VERIFIED (not found in items 60–62)

## 5. Design v3 (`Main-v3.dc.html`, beside v1 and v2, which are unchanged)

- **Quotes.** Owner quotes are verbatim, spelling included, with any cut marked "…". All 11 owner
  quotes were checked by script against the owner items and all matched. VERIFIED
- **Removed from v2:**
  - "It started as a rival…"
  - “Like a sparring partner.” as a quote
  - "Contrarian performance…"
  - "Evidence over authorship"
  - "roles stay where they are"
  - "The agents are the built-in… not the destination"
  - "Working title · Min Maxer's…"
  - "Quoted from my own notes"
  - first-person copy not written by the owner
- **Added:**
  - an eyebrow line: "Working name · not trademark-cleared"
  - "like a spring partner", with the note that an assistant read it as "sparring"
  - item 63 as the rule "Reflections, not orders"
  - "Done means shown", adopted from the repo
  - the scope caveat on the GitHub-write case
  - an "Open" section with five owner decisions
  - a no-affiliation footer
- **Experiments.** Statuses read "Design complete · benchmark pending" for 01, "Outlined · queued
  behind 01" for 02, and "Outlined · queued" for 03–05. A note says who set the order (the owner) and
  who drafted the wording (an assistant).
- **Tagline.** Shown in the timeline as a translation, "not adopted as a tagline". It is not in the footer.
- **Placeholders.** The `[YOUR WORKFLOW]` cards are replaced by one labelled card: "open · owner decides".

## 6. Open, for the owner

1. **The name.** Item 16 found high naming-conflict risk. Keep it as a codename, clear it, or rename.
2. **Atlas or a broader site** (item 76).
3. **What "Min Maxer's Agent Theory craft" names** (item 54).
4. **What the cindy.app capture is for** (item 77).
5. **Which existing workflows come first.**
6. **Whether to adopt the pasted Cindy text** (items 59 and 67).
7. **Any revision of the repo's README/PHILOSOPHY/ARCHITECTURE.** It would be additive only; nothing is
   pushed without approval. ARCHITECTURE.md brings back the builder/challenger split that item 19 corrected.
8. **Repo privacy flags (low):**
   - private tool names
   - a hardware hint
   - the public RiVaL ↔ choTaKu ↔ email link
   - no licence

## 7. Not done or checked

- Nothing was pushed, deployed or written to GitHub.
- The designs were not rendered or screenshotted.
- Not checked: live DNS for rival.avatararts.org, live trademark records, `cindy-spp.zip`, Notion, and
  the content of PI_FOUNDATIONS.md.
- The evidence reviewer's match of items 59/67 against the local Cindy session log was not re-checked
  by the coordinator.

## 8. Late additions (from `compare-evidence.md`)

- **The handoff's structural claims hold** (HTML copy, entry count, handoff update, earlier versions
  kept), but its content still has two errors:
  - it calls "sparring" the owner's word;
  - it says the pasted Cindy text came "from this conversation".
  The handoff is not edited here. SOURCE (evidence report); not re-checked by the coordinator.
- **Repo text in the owner's voice.** The five-experiment programme doc and EXPERIMENT_01 contain
  first-person instructions written by ChatGPT, such as "my local agents" and "until I direct
  otherwise". These are published under the owner's account. This joins open item 7. SOURCE (evidence report)
- **Coverage note.** For independence, the evidence reviewer did not read the other two reviewers'
  reports; it used only what the coordinator relayed.
