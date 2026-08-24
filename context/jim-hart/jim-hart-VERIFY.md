# VERIFY — read before publishing any of this

Four provenance levels are used throughout:

- **verified** — from git history or files on this machine. Safe as-is.
- **quoted** — lifted from a document Jim wrote. Safe as-is.
- **reported** — Jim's recollection, not checkable here.
- **drafted** — Claude's analysis or inference. **Review before it goes anywhere public.**

Mining run: `C:\Code`, 45 directories, 2026-08-24.

---

# ⚠️ Redactions applied to this public copy

**1. `VirtuousSync-JimHart` is withheld.** 21 commits, 163 lines, Sep 2025. Virtuous is a nonprofit CRM and
this reads as employer- or client-adjacent. It is excluded from every total in `portfolio.json` and appears
in no tier. Held locally only.

**2. The LaceLab cluster is abstracted.** Four repositories — `LaceLab`, `LaceLabStudio`, `LaceLabFilms`,
`LaceLabFilmsLaunch` — are described by their engineering facts only: Electron desktop, the Azure Static Web
Apps + Functions + Blob Storage + Clerk port, the design-handoff canvases, and the commit and line counts.
**No subject matter is described anywhere in these documents.** Keep it that way. A sibling directory,
`UnchartedDesires`, is excluded entirely.

Both are marked here rather than silently omitted, per the repository convention.

---

# Corrections made during mining

## ✅ The first line count was wrong by a factor of seven
**First pass said:** 1,132,962 lines. **Actual:** 164,418.

Three causes, worth knowing about because they are the kind of error that destroys credibility if a
reviewer catches it first:

- **Vendored third-party source.** `CampfireCrm` contains full clones of `Npgsql` (Nino Floris) and
  `efcore.pg` (Shay Rojansky, 127 commits). Counting them credited Jim with 247,456 lines in that project.
  **Real figure: 33,297.** Every nested `.git` is now checked for authorship — clones by other people are
  dropped whole, Jim's own sub-repositories are kept.
- **Electron build output.** `ClipRenamer`, `PromptForgeStudio`, `MusicSorter` and `LaceLab` each ship a
  `release/` directory containing Chromium's `LICENSES.chromium.html` — a single file of 164,000–270,000
  lines. `ClipRenamer` fell from **224,018 lines to 1,272.**
- **Directories that are not Jim's projects.** `npgsql-temp` (87,770 lines) is a clone of the Npgsql
  library. `Auth0Quickstart` is a vendor sample. `test`, `sample import`, `voice_clips` and
  `memory-bank-backup` are not projects. All are excluded by name; the list is in `jim-hart-mine.py`, committed alongside these documents.

`meta.method` in `portfolio.json` records the exclusion list. **Never quote a figure that did not come from
that file.**

## ✅ The source document omits the largest body of work
`jim-hart-source-project-portfolio.md` does not mention the LaceLab cluster at all. It is **680 commits and
61,555 lines** — larger than any other project on the machine, and the only place a complete
desktop-to-cloud architectural migration exists. Now included, abstracted per the redaction above.

## ✅ `ScrollForCause` is `SwipeForCause` on disk
The source document calls it ScrollForCause. The directory, the repository and the code say SwipeForCause.
`portfolio.json` uses the on-disk name. **Which is correct?**

---

# Still needs Jim's confirmation

## Claims in the source document that the filesystem does not support

**1. ILMOSH's React frontend does not exist.**
The write-up says *".NET Web API · Entity Framework Core · PostgreSQL · React frontend · Clerk."* On disk,
`ILMOSH/Frontend/` contains **zero TypeScript, TSX or JSX files**. The 2,911 lines counted are all C#. The
root `.git` and the `Backend/Ilmosh.Api/.git` both exist but hold **no commits at all** — nothing was ever
committed. Was the frontend built and lost, never built, or is it somewhere else?

**2. jimhart.dev returns 404.**
The write-up describes it as *"statically exported, and served from a CDN with a CI gate."* The domain
resolves and something answers, but `https://jimhart.dev`, `www.` and `http://` all return **404**, checked
2026-08-24. 17 commits, one active day, 838 lines. Is it deployed and broken, taken down, or never
released? `portfolio.json` currently says `shipped` — **that status is unsafe until you answer.**

**3. Twenty projects have no git history.**
`DoraTrack`, `PromptForgeStudio`, `MusicSorter`, `Waterdeep`, `Foundation`, `Huntr`, `MerryPicks`,
`WordToEpub`, `VideoTranscripts`, `youtube-to-mp3`, `PDFtoPNG`, `Jexi`, `Navi`, `CommandCenter`,
`ClaudeCode`, `ImagineClicker`, `minecraft-mod-whereami`, `SuperTank`, `AI Thing A Week` and `ILMOSH` have
no commits. Their metrics are **filesystem-only** and are labelled that way in `portfolio.json`. This is the
same trap that caught Paul's HouseHelper: git said 103 lines, disk said 4,432. **Do not describe any of
these as unbuilt.** DoraTrack alone is 18,770 lines.

**4. `Foundation` and `Foundation_bak`.**
`Foundation` has 941 lines and no repository. `Foundation_bak` has 534 lines and **13 commits from
April–July 2024** — the oldest history on the machine, and the only record of the template's origin. Both
are counted in the headline totals. If `_bak` is a duplicate rather than a predecessor, the totals need a
small correction. **Which is it?**

**5. `SuperTank` contains no source.**
Zero counted lines. It is described as OCR and page-image extraction work, which may well be real but
produced no code. It sits in the experiments tier marked `parked`. (`UnchartedDesires` also holds no
counted source, but it is excluded from the portfolio entirely under the redaction above and appears in no
tier.)

**6. GPU Fluid Simulation lives in a directory called `ClaudeCode`.**
814 lines of HTML. The write-up describes a WebGL/GLSL fluid simulation. Assumed to be the same artifact —
**confirm**, because the directory name suggests otherwise.

## Inferences I made about you — all `drafted`

**7. "He went back to the code on purpose."** The `OVERVIEW.md` argument reads the Director of Engineering →
Senior Staff Engineer move as a deliberate return to IC work, because that framing matches the Staff SWE JD
almost word for word. LinkedIn shows both roles as *"May 2019 – Present"* and *"Jan 2024 – Present"*
simultaneously, which is ambiguous. **Was it a choice, a reorganisation, or are you still doing both?**
This is load-bearing for the whole pitch — if it was not a choice, the argument has to change.

**8. "He ports rather than restarts."** Drawn from LaceLab → LaceLab Studio being the only complete
migration in the record. One instance is a data point, not a pattern. Defensible if you can name the reason
you ported instead of rewriting.

**9. The Waterdeep / Paul parallel.** That you and Paul independently built simulated product organisations
is `verified` on both sides — his `systems/01-multi-agent-workflow.md`, your `Waterdeep/`. That neither knew
about the other's is **`reported` and unconfirmed.** If you did discuss it first, the claim has to be
softened, and it is the single strongest fact in the team argument — so get it right.

## Facts nobody has checked

- **Career figures are `quoted` from LinkedIn, not independently verified**: 16 FTE engineers, 6 nearshore,
  2 offshore teams, 3x growth over three years, five teams. Standard for a CV, but know that they rest on
  your own account.
- **No project has users, revenue or downloads.** Nothing in this portfolio has a usage metric of any kind.
  Do not let one appear.
- **Darryl has no folder, no surname on record here, and no Ode role that fits.** See `DEFERRED.md`.
