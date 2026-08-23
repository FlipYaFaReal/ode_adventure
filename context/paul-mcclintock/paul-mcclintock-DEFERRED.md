# DEFERRED — parked for Paul to add later

Four items, parked 2026-08-22. **Not part of the current portfolio.** The session building the site should skip this file entirely.

This exists so nothing is lost and so the information architecture can leave room. Fill in the gaps below and they can be promoted into `portfolio.json` in a later pass.

| Item | Intended tier | What I have |
|---|---|---|
| [Kip](#1--kip) | Agents | A description, no artifacts |
| Security risk assessment | Judgment | **Withheld from this public repo** — confidentiality decision needed |
| [Contract evaluation](#3--contract-evaluation-project) | Unknown | Nothing |
| [Fable POC](#4--proof-of-concept-built-with-fable) | Unknown | Nothing |

---

## 1 · Kip

**OpenClaw agent · Notion board + Telegram**

### What I know
An OpenClaw-based agent wired to a Notion board for state and to Telegram as its interaction surface. No local repository or files for it exist on this machine.

### Why it's worth doing properly
It's structurally different from everything else here. The applications wait to be opened. The systems run on a schedule. **Kip is an always-on agent a human actually converses with**, backed by a real state store.

For a forward-deployed role at an AI services venture, that's arguably the most relevant single artifact you have — and it's the only one in the portfolio with a conversational surface a non-technical person could use.

### What I need from you
- What problem it was built to solve
- What the Notion board holds, and how Kip reads from or writes to it
- What the Telegram surface is actually used for day to day
- Is it still running?
- Any design notes, prompts, or configuration — and where they live

### How to get it
The Notion connector was live in this session but unused. If you want, point me at the board and I'll pull the structure and derive most of the above without you writing it up.

---

## 2 · Security risk assessment / Information Security Policy

> **Withheld from this public repository.**
>
> This item concerns client-confidential and employer-confidential work. It is parked pending a
> confidentiality decision by Paul, who is the security officer for the organization involved and
> therefore the person who would be asked to approve any public description of it.
>
> The full write-up is held locally and is not published here. Nothing further about it should be
> added to this repo without that decision being made first.

---

## 3 · Contract evaluation project

### What I know
You mentioned it on 2026-08-22. That's all I have. A search of `Documents` for *contract*, *MSA*, *SOW*, *agreement*, *redline*, and *clause* returned nothing, so it isn't on this machine under an obvious name.

### What I need from you
- What the evaluation was for, and who it was for
- **Work-related or personal?** This matters most — if it is work-related it likely carries the same confidentiality constraint as item 2 and should be handled the same way
- What was *built* versus what was *analysed*
- **Is there a scoring rubric?** If so it joins the rubric-design theme, which is currently the strongest claim in the portfolio — five domains would become six
- Where the artifacts live

---

## 4 · Proof of concept built with Fable

### What I know
You mentioned it on 2026-08-22. Nothing else.

### Why it might matter more than it sounds
Every other item in this portfolio runs on Claude — via Claude Code, the API, or a scheduled agent. A POC on a different model is **the only evidence here of deliberate model selection**, which is a distinct signal for a role that involves picking the right model for a client's problem and defending the choice.

If you compared it against an alternative on the same task, that's better still — that's an eval, and it would slot straight into the rubric-design theme.

### What I need from you
- What it does, and what problem it addressed
- **Why Fable specifically**, rather than the models used everywhere else
- When it was built
- Does it still run, and where's the code?
- Was it ever compared against another model on the same task?

---

## Promoting an item

When you're ready, give me whatever you have — a paragraph is enough. I'll write it up to the same schema as the rest, mark provenance honestly, and move it out of here into `portfolio.json`.
