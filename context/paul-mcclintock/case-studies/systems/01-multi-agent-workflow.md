# Multi-Agent Software Development Workflow

**March 2026 · Run across at least five projects · Verifiable on disk**
*The anchor artifact of this portfolio*

---

## The problem

Agentic coding produces volume easily and quality rarely. The characteristic failure is plausible-looking code that nobody validated, written against requirements nobody wrote down, with every ambiguity silently resolved by whichever agent hit it first — and no record that a decision was ever made.

## What it is

A Claude Code orchestration prompt defining a **simulated product organization**, run in three phases.

**Phase 1 — Requirements panel.** Product Manager, Lead Engineer, UX Designer, QA Lead. Output: a PRD, user stories, acceptance criteria.

**Phase 2 — Architecture.** Software Architect and Engineering Lead. Output: ADRs, technical design, a task breakdown with dependencies.

**Phase 3 — Implementation loop.** Engineer → Code Reviewer → Engineer revision → Security Reviewer → QA validation.

Underneath it, a `.workflow/` directory doing the bookkeeping: JSON state management, a decision record for every resolved ambiguity, a work-item state machine (backlog → in-progress → review → qa → done), and session logs for traceability. Enforced test-first development. Mandatory security review. A rule that every line of code traces back to an acceptance criterion. And a cap on review cycles with escalation, so the loop cannot run forever.

## What survives on disk

This is the one item reconstructed from chat history that is **directly corroborated by files**, and the corroboration is specific.

Five repositories carry a `.workflow/` directory: ListingLift, CaptureRapture, HouseHelper, CareerCalling, TradeParrot.

**HouseHelper's is the most complete** — four decision records, ten work items with acceptance criteria and dependency lists, a session log, and a state file tracking nine of ten items to done. The session log for March 9 opens:

> `00:01 - Agent: PM`
> `Action: Analyzing product idea - House hunting collaborative web app`
> `Output: Convening expert panel for requirements definition`

**CareerCalling's** holds three decision records and sixteen work items — for a project whose entire git history is a single squashed commit. The planning survived in more detail than the version control did.

**CaptureRapture's DEC-001** is the best single specimen. It weighs three MVP scope options for screenshot versus video capture, each with pros and cons, and defers video to v2 on the reasoning that most enterprise training guides are static step-by-step documents and video would roughly double the implementation timeline. Then, at the bottom:

> **Participants**
> Product Manager (decision owner) · Lead Engineer · UX Designer · QA Lead

None of those participants are people.

## Why this is the anchor

The first pass through this portfolio identified the throughline as "every project carries a dated design document, then an implementation plan, then the commits that satisfy it — 88 of them." That was correct, and it missed the point: it found the *output* of this system without finding the *system*.

Eighty-eight specification documents across eight projects is not a habit. It is a machine running.

And that changes what the portfolio is claiming. "I write good specs" is a personal quality, unverifiable and unremarkable. "I designed a repeatable process that produces specs, forces every ambiguity into a written decision, gates implementation behind review and security stages, and I ran it across five projects in four languages" is an engineering artifact with evidence attached.

For a role defined as converting ambiguous requirements into clear PRDs and evaluation criteria for AI systems, this is the thing that shows the conversion is systematic rather than intuitive — and that it can be handed to someone else.

## The honest limits

Worth stating precisely, because the evidence is good enough that overstating it would be a waste.

The `.workflow/` directories prove the system ran and produced structured artifacts on five projects. They do **not** prove every gate fired every time. TradeParrot's `.workflow/` is empty of records. No project shows work items physically moving through `review/` and `qa/` directories — only `backlog/`, with progress tracked in the state file's counters. The Security Reviewer and QA Validation stages are described in the design; nothing on disk independently confirms they ran on a given task.

The strongest defensible claim is: **a documented multi-role workflow with decision records and work-item tracking, applied across five projects.** That is plenty. It does not need to be inflated into a fully audited pipeline.

## The one thing worth adding

The system produced decision records for ambiguities it resolved. What it did not produce — and what would make it genuinely reusable by someone else — is a record of the ambiguities it *failed* to resolve and escalated to the human. The design mentions escalation after maximum review cycles; no escalation record survives on disk.

For a forward-deployed context, that gap matters more than it looks. The value of a system like this to a client is not that it decides things. It is that it knows which things it should not decide.
