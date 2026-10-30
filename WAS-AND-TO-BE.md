# What was, and what is to be

This worktree (`.claude/worktrees/rival-coverart`, branch `worktree-rival-coverart`, from `a0c6fea`)
works like a hallway between two rooms. It is not a room of its own. It keeps two things:

- **What was:** the states RiVaL has passed through, including the accidents. Nothing is smoothed over.
- **What is to be:** the open turns ahead. They are named here but not decided.

It also serves as the **outside reference for the parts still within**. Most of `~/RiVaL` is not in git
on purpose (private sources, transcripts, exports). This branch does not copy those files. It points to
them by path, size, time and SHA-256 in `reference/outside-manifest-2026-10-29.json`, built by
`outside-reference.py`. If a file inside changes, a re-run shows it. The reference changes; the files themselves are not touched.

## What was

| When (UTC) | State | Where it lives |
|---|---|---|
| 10-30 01:18–02:29 | A ChatGPT conversation names RiVaL. ChatGPT drafts 9 doc commits through the owner's GitHub connector, ending at `f8afb36` | GitHub `main`, first parent of `a0c6fea` |
| 10-30 01:46–02:43 | Exports of that conversation: `making-of-RiVaL.{html,json,md}`, then `making-of-RiVaL (1).{html,json}` with 15 more user turns | inside (see manifest, root files) |
| 10-29 local | Design **v1**. Its coat cards came from pasted assistant text, presented as doctrine | `rival-design/project/Main.dc.html` |
| | **v2**. The owner's coat words, quoted with a dropped "but" and unmarked cuts | `Main-v2.dc.html` |
| | Three rival reviewers, then three three-way comparisons | inside: `rival-source-review/swarm/` |
| | **v3**. Exact quotes, the "built-in" left open, an "Open" section | `Main-v3.dc.html` |
| | First findings, kept with their errors (they attributed the repo to Cindy and counted 10 files) | `rival-design/docs/2026-10-29-design-session-findings.md` |
| | Corrections | `rival-design/docs/2026-10-29-three-way-comparison.md` |
| 10-30 ~02:49 | The landing page exported as a PDF and an HTML zip; a Hostinger zip at 02:56 | inside: root files |
| | Local and public histories merged and pushed as `a0c6fea`, with no force push | `main` |
| | Four typography covers, among them **Collision**: an accident kept as a cover | inside: `rival-coverart/` |

Kept on purpose: v1 and v2 beside v3, the first findings beside their corrections, and Collision beside the
clean mirror. **What was** stays readable as it was.

## What is to be

These are owner decisions. Nothing on this branch settles them.

1. **The name.** A preliminary screen found high naming-conflict risk.
2. **Atlas or a broader site** (item 76, never answered).
3. **What "Min Maxer's Agent Theory craft" names.**
4. **What the cindy.app capture is for** (item 77).
5. **Which existing workflows come first.** The "built-in" may be the work already done (item 56).
6. **The public repo's wording.** Parts are ChatGPT text in the owner's voice.
7. **Cover art.** Which covers to keep, and whether they enter git.

Seen but not yet read: **`making-of-RiVaL2.{html,json}`** (03:06, 3.4 MB of JSON). It is newer than everything
the swarm reviewed. It may continue the conversation beyond item 77.

## The parts still within (summary of the manifest)

116 files, 39.7 MB. The `.git`, `.claude`, `.tmp` and `__pycache__` folders are left out.

| Group | Files | Tracked here |
|---|---|---|
| root files (exports, the source HTML/JSON, zips, PDF) | 20 | 5 |
| `session-history-2026-10-29-through-225755/` | 5 | 0 |
| `rival-source-review/` (extraction, swarm, full transcripts) | 13 | 0 |
| `rival-coverart/` | 17 | 0 |
| `source-*` (backing, HTML continuation, share, reconstructed, GitHub snapshot) | 20 | 0 |
| `export-*`, `prior-*`, `transcript/` | 27 | 0 |
| `docs/`, `rival-design/` | 14 | 13 |

The manifest holds paths and hashes only. It holds no contents, so the privacy line stays where the export guide drew it.
The branch is **not pushed**, because file names alone describe private material. Pushing it is the owner's call.

## Re-run

```
./outside-reference.py /Users/steven/RiVaL --dry-run
./outside-reference.py /Users/steven/RiVaL -o reference/outside-manifest-2026-10-29.json   # writes -v2 if one exists
```

Compare two manifests by `sha256` to see what moved inside, and when.
