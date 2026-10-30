# Changelog

All notable changes to the local RiVaL workspace. Newest first. Earlier versions are kept,
never replaced: a revision adds a new file or artboard beside the old one.

## 2026-10-29

### Added
- `extract-html-visible.py`: static text extraction of
  `~/Downloads/making-of-RiVaL (1).html` (SHA-256 `21ccdcfa…66053f`) into
  `rival-source-review/`: 77 items, 42 user / 35 assistant. No HTML scripts or assets run.
- `rival-design/` — Design canvas "RiVaL — Equal Partners" (private claude.ai artifact).
  - **v1** `project/Main.dc.html`: landing page covering the meaning, the coat and room,
    reciprocal review and the five experiments.
  - **v2** `project/Main-v2.dc.html`: beside v1, which is unchanged. Changes:
    - Leads with the work already being done (HTML item 56), using placeholders instead of invented workflows.
    - The coat section quotes the owner's own words (item 23) in place of a pasted assistant paraphrase (item 67) and the fixed wearer/coat/room mapping.
    - Adds the rule "who sent it is not who wrote it".
    - The experiments run in order, with rivals → batch → total. The four without a stated status are marked "Not started".
- `rival-source-review/swarm/`: reports from three independent rival reviewers
  (meaning, counter-reading, evidence). These are in progress and untracked.

### Verified
- `source-backing-html-continuation/`: the copied HTML's hash matches the original in Downloads, and it has
  15 more user entries than the JSON (42 vs 27). The previous handoff and manifest are kept as
  `*-before-html-continuation.*`.
- GitHub `AvaTar-ArTs/RiVaL` (public): commit `b0b0a73` exists (2026-10-30T02:08:53Z, adds
  `docs/research/SWARM_REVERSE_ENGINEERING.md`). The handoff listed it as asserted but unconfirmed.

### Noted, not changed
- `RiVaL-export-guide.md` was rewritten in place at 22:48 by another agent. No earlier copy was kept.
- The repo's `docs/PHILOSOPHY.md` fixes the coat metaphor as a mapping. Design v2 follows the owner's
  words instead.

### Not tracked in git (by design)
- Source copies, transcripts and the HTML extraction contain private paths and are kept out of git.
  The export guide says not to publish the package without a privacy review.

## 2026-10-29 (later)

### Added
- `rival-design/docs/2026-10-29-design-session-findings.md`: findings and reasoning to date. Covers:
  - source identity
  - authorship (who sent it vs who wrote it)
  - GitHub repo check (`b0b0a73` confirmed)
  - verification of the other agent's report
  - v1/v2 design decisions
  - swarm status, open items, and what was not checked

## 2026-10-29 (after the rival swarm)

### Added
- **v3** `rival-design/project/Main-v3.dc.html` beside v1/v2 (both unchanged); canvas.json gets a third board.
  - Owner quotes are verbatim, spelling included, with cuts marked "…". All 11 were checked against the source by script.
  - Assistant wording that read as the owner's is removed. This includes the "sparring" quote, "started as a rival",
    "roles stay where they are" and "agents are the built-in".
  - Item 56 is quoted with both readings left open.
  - The experiment statuses now match the repo.
  - New sections: "Open" (owner decisions) and a no-affiliation footer.
- `rival-design/docs/2026-10-29-three-way-comparison.md`: compares A (commit 2108945), B (GitHub @ f8afb36) and C (the swarm),
  and corrects the first findings doc.
- `export-full-transcript.py`: renders the full session log plus subagent logs to Markdown. `/export` only covers the conversation after compaction.
  It writes the full transcript to `rival-source-review/full-transcript-2026-10-29.md` (untracked; private).

### Corrected (recorded here; the earlier document is unchanged)
- The repo was written and pushed by ChatGPT through the owner's GitHub connector, not by Cindy.
- The repo has 9 files, not 10.
- Experiments 02–05 are outlined and queued, not "not started".

## 2026-10-29 (joined with the public repo)

### Changed
- `extract-html-visible.py` now takes the HTML path as an argument; the hard-coded local path is
  kept only as a `# v1:` comment. Re-run on the same-hash copy: 77 items, 42 user / 35 assistant.
- This history is merged with GitHub `AvaTar-ArTs/RiVaL` main (`f8afb36`, 9 commits) using
  `--allow-unrelated-histories`. Nothing was rewritten and nothing was force-pushed.
- `.gitignore` combines both: the local allowlist first (now also allowing `README.md` and `docs/`),
  then the public repo's secret and runtime rules, so those still exclude anything above them.

### Not changed
- The repo's README, PHILOSOPHY, ARCHITECTURE and research docs are left as they were.
  `rival-design/docs/2026-10-29-three-way-comparison.md` lists what the owner may want to revise there.

## 2026-10-29 (worktree `worktree-rival-coverart`: what was / what is to be)

### Added
- `WAS-AND-TO-BE.md`: the worktree as a hallway. It holds a timeline of what was (accidents kept)
  and the owner decisions still open.
- `outside-reference.py` and `reference/outside-manifest-2026-10-29.json`: a hashed reference
  (path, bytes, mtime, SHA-256) to the 116 files in `~/RiVaL` that git does not hold. It records
  file names only; no contents are copied.
- `coverart-arcana/`: three RiVaL covers in the visual language of the owner's Canva work
  (night sky, gold sacred geometry, spaced serif titles with ✦, water reflection, eye sigil,
  choTaKu credit). Each is built from SVG and type only, with no generated images.
  - **Vesica**: equal blue and ember circles in a flower of life, under "EQUAL ✦ OPPOSITE".
  - **Reflection**: RiVaL mirrored in water, with a blue beam and an ember beam meeting on the horizon.
  - **The One in the Coat**: a tarot card with an arch, a hallway, stairs, a coated figure and a sun-crown halo.
  - The v1 renders are kept. In v1, Cinzel Decorative forced all capitals (losing RiVaL /
    choTaKu) and the glow filters were clipped into squares. v2 uses Cinzel's small capitals and
    full-canvas filter regions.
  - `build-arcana.py` builds the covers and `render.py` renders them at 3000×3000. Neither overwrites existing files.

### Changed
- `.gitignore`: allowlists the files above. The reference rule is narrowed to
  `reference/outside-manifest-*.json` so it cannot re-include secret-shaped JSON.

### Tooling (outside the repo)
- `~/.local/bin/chrome-shot`: a headless-Chrome HTML→PNG wrapper with a plain command name, because
  worktree-isolated sessions refuse quoted executable paths that contain spaces.

### Not changed
- The `~/RiVaL/rival-coverart/` covers (Seam, Opposites, Collision, Rooms) stay local and untracked.
- `Arcana-3-coat-v2-3000-v2.png` is a duplicate left by the wrapper test. It is kept until the owner decides.
