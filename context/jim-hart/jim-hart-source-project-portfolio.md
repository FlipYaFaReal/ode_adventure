# AI-Assisted Project Portfolio

Projects in `C:\Code` built or developed with AI assistance — Claude Code, Lovable, and
other AI coding tools. Each entry lists what the project is, the problem it solves, and the
technology behind it.

---

## Full-Stack Applications

### CampfireCrm
A CRM built for *Overland South*, a biannual camping and overlanding event in Charleston, SC.
Event organizers were tracking attendees, vendors, and logistics across spreadsheets and
email threads; CampfireCrm consolidates that into a single authenticated system with
protected dashboards and per-user profiles. Auth is handled by Clerk, with an API client
that automatically injects JWTs on every request, and split CI/CD pipelines deploy the API
and web app independently.

**Stack:** React 18 · TypeScript · Vite · Tailwind CSS · React Router · .NET Minimal API ·
PostgreSQL · Clerk · Azure App Service + Azure Static Web Apps · GitHub Actions · hurl (API tests)

### ScrollForCause
A TikTok-style volunteer marketplace connecting nonprofits with volunteers. Nonprofits
struggle to reach volunteers and volunteers struggle to find causes worth their time;
ScrollForCause reframes the discovery problem as a short-form vertical feed you swipe
through, so finding a cause feels like scrolling social media rather than searching a job
board. Includes a standalone marketing landing page deployed separately from the app.

**Stack:** .NET 8 Web API · Entity Framework Core · React · TypeScript · Vite · xUnit ·
Vitest · Azure Static Web Apps

### ILMOSH
An event-planning and coordination app for a recurring annual gathering. Organizing a
multi-day group event means tracking who's attending, what food and drinks are covered, what
still needs to be brought, and collecting photos afterward — usually spread across group
chats. ILMOSH models all of it properly: events by year, participants, menu items, bar
items, pantry items, and a shared photo library, all tied to authenticated users.

**Stack:** .NET Web API · Entity Framework Core · PostgreSQL · React frontend · Clerk

### DoraTrack
A SaaS application for tracking and improving DORA metrics. Engineering organizations know
they should measure deployment frequency, lead time for changes, mean time to recovery, and
change failure rate — but rarely have a place to put the numbers or a way to interpret them.
DoraTrack provides dashboards with historical trend charts, benchmarks each metric against
the Elite/High/Medium/Low performance bands, and turns the results into actionable
recommendations. Supports both manual entry and automated ingestion through a REST API.

**Stack:** C# Web API · React · REST API for automated metric ingestion

### MerryPicks
A Secret Santa organizer. Running a gift exchange by hand means someone has to do the
drawing, keep the assignments secret, and chase people for wish lists — and that someone
inevitably ends up knowing who has whom. MerryPicks handles the draw and the assignments
behind authentication so the organizer can participate fairly too.

**Stack:** React 19 · TypeScript · Vite · Tailwind CSS · React Router 7 · .NET API · Clerk

### Talamar's Forgotten Tales
An interactive branching-narrative story game. Traditional choose-your-own-adventure
storytelling on the web is usually static text; this one plays a video for every scene while
narrative text types out alongside it, unlocking choices only once both finish — so pacing
feels cinematic rather than click-through. Stories are pure data: a manifest lists available
stories, each one a scene graph of branching choices with stat effects and requirement gates,
so new stories ship without code changes. Player state runs through a typed reducer with an
explicit status machine.

**Stack:** React 19 · TypeScript · Vite · Tailwind CSS v4 · React Context + useReducer ·
.NET 10 Web API (vertical slices)

### Huntr
A scavenger hunt platform for building and running hunts as a group activity — creating the
hunt, distributing it to participants, and tracking progress — packaged as a
cross-platform app rather than a website.

**Stack:** Quasar Framework · Vue · Node.js

---

## Developer Tools & Infrastructure

### HartStack CLI
A scaffolding tool that generates production-ready full-stack SaaS projects in one command.
Every new SaaS idea otherwise starts with the same week of plumbing — auth, billing, CI/CD,
cloud provisioning — so HartStack templates all of it. The `scaffold` command walks a
Handlebars template tree, conditionally including files by filename prefix (`__b2b__`,
`__b2c__`, `__stripe__`) and substituting variables into filenames. The `deploy` command runs
a six-step Azure provisioning flow: validate, create resources, configure secrets, update
workflow files, set GitHub secrets, print summary.

**Stack:** Node.js (pure ESM) · yargs · Handlebars · Azure CLI · GitHub CLI · node:test

### Foundation
A .NET Web API template for multi-tenant SaaS backends. Instead of organizing code by
technical layer (services, repositories), it uses vertical slices: each feature owns its own
controller, handlers, and DTOs in a self-contained folder, with only minimal shared
infrastructure. Solves the problem of new backends drifting into tangled layered
architectures as they grow.

**Stack:** .NET 9 Web API · Entity Framework Core · PostgreSQL · vertical-slice architecture

### Waterdeep — AI Software Factory
An orchestration framework rather than an application: a system prompt that turns Claude
into the Orchestrator of an autonomous "software factory." The problem it addresses is AI
coding agents skipping straight to code without requirements, architecture, testing, or
review. Waterdeep forces a raw product idea through phased delivery with a panel of
specialized expert agents, resolving ambiguity through the right expert before proceeding
and tracking everything in a living on-disk kanban system (`WORKBOARD.md`, `DECISIONS.md`,
`REQUIREMENTS.md`, `ARCHITECTURE.md`, and per-task files).

**Stack:** Markdown-based agent prompt framework · Claude Code

### Navi
A conversational REPL assistant that routes typed input through an orchestrator and keeps a
persistent history of the exchange — a minimal harness for experimenting with agent
orchestration outside of a heavyweight framework.

**Stack:** Python

### Jexi
A chatbot service built directly against Azure OpenAI, exploring conversational AI in a
plain .NET application without an intermediate framework.

**Stack:** C# · .NET 8 · Azure.AI.OpenAI

---

## Desktop & Media Tools

### PromptForge Studio
A desktop app for generating consistent AI text-to-image and image-to-video prompts. The
problem is prompt drift: building a longer video out of many 5–10 second AI-generated clips
falls apart when characters, locations, and outfits look different in every clip. PromptForge
solves it with structured world-building and enforced canonical phrasing, so the same
character is described the same way every time and prompt generation becomes repeatable,
reviewable, and auditable. Storage is local, file-based Markdown plus standard media files.

**Stack:** Electron · React · TypeScript · Vite · Tailwind CSS · electron-builder ·
local Markdown storage

### VideoTrimmer (ClipForge)
A batch MP4 clipping tool for Windows. Trimming dozens of source videos one at a time in a
full NLE is enormous overhead for a simple in/out cut. ClipForge loads a whole folder and
walks through it file by file in a Premiere-style timeline: scrub, set in and out points,
save the trimmed copy, and the next video loads automatically while processed files move
themselves into a `done/` subfolder.

**Stack:** Electron · TypeScript · React · electron-vite · ffmpeg-static

### ClipRenamer
A desktop utility for rapidly reviewing and renaming video clips. Renaming a folder of
clips in Explorer means opening each one to remember what it is; ClipRenamer plays each
file in place with the rename field right beside it, so you watch, type a name, save or
skip, and advance automatically. Includes a fix for the Windows `EBUSY` file lock that
otherwise blocks renaming the video currently playing.

**Stack:** Electron · React 19 · TypeScript · Vite · Tailwind CSS · lucide-react

### MusicSorter
A desktop tool for triaging large audio libraries into categories. Sorting hundreds of
tracks by dragging files between folders is slow; MusicSorter plays each file with its
metadata visible and assigns it to a destination category folder with a single keyboard
shortcut, remembering configured categories, shortcut keys, volume, and session state
between runs.

**Stack:** Electron · React · TypeScript · Vite · Tailwind CSS · electron-builder

### VideoTranscripts
A batch video transcription tool. Getting text out of a folder of videos normally means
uploading them somewhere one at a time; this runs entirely locally, auto-detecting whether
to use CUDA or CPU, using voice-activity detection to skip silence, and emitting both plain
`.txt` transcripts and timestamped `.srt` subtitles. Handles errors per-file so one bad
video doesn't abort the batch, and can recurse through subfolders.

**Stack:** Python · faster-whisper · CUDA/CPU auto-detection · VAD filtering

### youtube-to-mp3
A command-line tool that extracts audio from a YouTube URL as an MP3, self-bootstrapping the
`yt-dlp` binary on first run so there's no separate install step, with an output-directory
flag for batch workflows.

**Stack:** Node.js CLI · yt-dlp-wrap · ffmpeg-static

### WordToEpub
A converter that turns Word documents into EPUB ebooks, parsing the `.docx` document model
and generating EPUB output with a converted table of contents — solving the gap between
writing in Word and publishing in a proper ebook format.

**Stack:** C# · .NET

### PDFtoPNG
A utility that renders PDF pages to PNG images, for pulling page images out of documents
that only exist as PDFs.

**Stack:** C# · .NET

---

## Games, Sites & Experiments

### jimhart.dev
A one-page lead-generation site for an AI consulting practice — the problem being that
consulting inquiries need a single credible destination rather than a résumé PDF. Built from
a written design spec, statically exported, and served from a CDN with a CI gate that runs
lint, typecheck, and build before anything ships.

**Stack:** Next.js (static export) · Tailwind CSS · Azure Static Web Apps · GitHub Actions

### CoordHud (minecraft-mod-whereami)
A Minecraft client mod that renders the player's current coordinates as a persistent HUD
overlay, so you don't have to open the debug screen every time you need to know where you
are.

**Stack:** Java · Fabric mod loader · Minecraft 1.21.11 · Gradle

### CombatHelper
A Warhammer 40k combat companion for an 11" touchscreen tablet. Running unit-versus-unit
combat calculations mid-game means flipping through rulebooks and doing arithmetic by hand;
this makes the combat calculator the default landing screen — side-by-side unit selectors
and real-time results with minimal taps.

**Stack:** React · TypeScript · Vite · Tailwind CSS · shadcn/ui · Bun · built with Lovable

### Rolling Respawn
A companion website for a tabletop RPG campaign, giving the party one shared place for the
adventure log, world map, companions, inventory, tavern, and shop instead of scattered notes.

**Stack:** Static HTML · CSS · Google Fonts (Cinzel / Lora)

### Command Center
A personal dashboard homepage — a single self-contained page pulling the things worth
glancing at into one dark, terminal-styled view with a live clock and panelized layout.

**Stack:** Single-file HTML · CSS custom properties · vanilla JavaScript

### GPU Fluid Simulation
A real-time fluid dynamics simulation running entirely on the GPU, rendered full-screen to a
canvas through hand-written GLSL vertex and fragment shaders — an exercise in shader-based
physics with no libraries or build step.

**Stack:** Single-file HTML · WebGL · GLSL shaders

### ImagineClicker
A browser extension that automates repetitive clicking on any page, for workflows where the
same UI element has to be triggered over and over.

**Stack:** Chrome Extension (Manifest V3) · JavaScript · content scripts · chrome.storage

### AI Thing A Week
A year-long creative challenge — build and document something new with AI every week for 52
weeks, inspired by Jonathan Coulton's "Thing A Week." The site itself was week one: the hub
that hosts every subsequent project, its writeups, and a subscription signup.

**Stack:** Static site · AI-assisted development

### SuperTank
A digital archaeology project recovering a type-in program from the November 1984 issue of
*COMPUTE!'s Gazette*. The source only exists as a scanned magazine, so the work is OCR and
page-image extraction — converting scanned pages into usable text and sprite/tile data.

**Stack:** OCR-extracted text · page image + tile extraction · Commodore 64 source material
